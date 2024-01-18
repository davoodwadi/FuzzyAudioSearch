# FuzzyAudioSearch
Retrieve Audio Segment in Large Text Corpus 

# Installation
```
git clone https://github.com/davoodwadi/FuzzyAligner.git
cd FuzzyAligner
python -m venv venv

# if on Windows
source venv/Scripts/activate
# if on MacOS or Linux
source venv/bin/activate

pip install -r requirements.txt
```

# Usage
*Note.* The easiest way to use the aligner is to use a bash compatible terminal (e.g. MacOS/Linux Terminal or Windows [Git Bash](https://gitforwindows.org/))

```
python xaligner.py -a audiofile -t textfile
```

where ```audiofile``` is the path to the audio whose subtitles you need. 

```textfile``` is the path to the transcript.

You can optionally pass ```-d``` to set the duration (in seconds) of each chunk of the audio.
```
python xaligner.py -a audiofile -t textfile -d 60
```

This can be helpful if you run out of memory.

While the default model size, ```tiny```, is sufficient for many texts, for multilingual texts (e.g. books by Nietzsche, which contains English and German text) it helps to use larger ```whisper``` models.

```
python xaligner.py -a audiofile -t textfile -d 60 -m tiny
```

model options:
- tiny
- small
- medium
- large-v3

# Credits
- [Whisperx](https://github.com/m-bain/whisperX/tree/main)
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
