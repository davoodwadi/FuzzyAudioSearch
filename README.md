# FuzzyAudioSearch
Retrieve Audio Segment in Large Text Corpus 

# Installation
```
git clone https://github.com/davoodwadi/FuzzyAudioSearch.git
cd FuzzyAudioSearch
python -m venv venv

# if on Windows
source venv/Scripts/activate
# if on MacOS or Linux
source venv/bin/activate

pip install -r requirements.txt
```

# Usage

```
python FuzzyAudioSearch.py -a audio_file -t text_file
```

where ```audio_file``` is the path to the audio file you want to use to search.

```text_file``` is the path to the large corpus.

You can optionally pass ```-c``` to set the chunk of the start and end of audio to find matches.
```
python FuzzyAudioSearch.py -a audio_file -t text_file -c 100
```

While the default model size, ```tiny```, is sufficient for many texts, for multilingual texts (e.g. books by Nietzsche, which contain English and German text) it helps to use larger ```whisper``` models.

```
python FuzzyAudioSearch.py -a audio_file -t text_file -c 100 -m tiny
```

model options:
- tiny
- small
- medium
- large-v3

# Credits
- [faster_whisper](https://github.com/SYSTRAN/faster-whisper)
- [FuzzySearch](https://github.com/taleinat/fuzzysearch)

# Citation
```
@software{Wadi_Forced_Alignment_of_2023,
author = {Wadi, Davood},
month = jan,
title = {{Forced Alignment of Long Audio using Fuzzy String Search}},
version = {0.0.1},
year = {2023}
}
```
