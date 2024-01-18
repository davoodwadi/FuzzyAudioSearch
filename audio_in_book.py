
import gc 
from tqdm import tqdm
from fuzzysearch import find_near_matches
from faster_whisper import WhisperModel
from faster_whisper.audio import decode_audio
from pathlib import Path
import torch
from phonemizer import phonemize

import re
from unidecode import unidecode
from argparse import ArgumentParser

parser = ArgumentParser()  
parser.add_argument("--segment_size", '-s', type=int, default=1)
parser.add_argument("--chunk_size", '-c', type=int, default=100)
parser.add_argument("--audio_file", '-a')
parser.add_argument("--text_file", '-t')
parser.add_argument("--model", '-m', default='tiny')
args = parser.parse_args()

def main():
    patience = 35
    chunk_size = args.chunk_size
    audio_fn = Path(args.audio_file)
    text_fn = Path(args.text_file)
    print(f'audio fn: {audio_fn}')
    print(f'text fn: {text_fn}')
    
    with open(text_fn, encoding='utf-8') as f:
        book = f.read()

    audio = decode_audio(str(audio_fn))
    start_audio = audio[:chunk_size*16_000]
    end_audio = audio[-chunk_size*16_000:]
    model = WhisperModel(args.model, device="cuda", compute_type="int8", )

    start_segments, _ = model.transcribe(start_audio, language='en')
    start_segment_list=[]
    for segment in start_segments:
        start_segment_list.append(segment.text)

    segment_size=args.segment_size # default=1
    start_segment = ''.join(start_segment_list[:segment_size])
    start_segment = start_segment[1:]
    max_l_dist = 1
    sm = []
    print(f'finding start:\n{start_segment}')
    while len(sm)==0:
        sm = find_near_matches(start_segment.lower(), book.lower(), max_l_dist=max_l_dist)
        max_l_dist+=1
    print(f'start segment found')

    end_segments, _ = model.transcribe(end_audio, language='en')
    end_segment_list=[]
    for segment in end_segments:
        end_segment_list.append(segment.text)
    
    segment_size=args.segment_size
    end_segment = ''.join(end_segment_list[-segment_size:])

    
    end_segment = end_segment[1:]
    max_l_dist = 1
    em = []
    print(f'finding end:\n{end_segment}')
    while len(em)==0:
        em = find_near_matches(end_segment.lower(), book.lower(), max_l_dist=max_l_dist)
        max_l_dist+=1
    print(f'end segment found')
    
    output_fn = audio_fn.parent/f'{audio_fn.stem}.txt'
    with open(output_fn, 'w', encoding='utf-8') as f:
        f.write(book[sm[0].start:em[0].end])
    print(f'chunk wrote to {str(output_fn)}')

if __name__=='__main__':
    main()