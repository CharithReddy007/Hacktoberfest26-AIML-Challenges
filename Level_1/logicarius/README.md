# Level 1: Similarity and Squashing

## Files
- `similarity.py`: dot product, magnitude, cosine similarity and min-max normalization. It loads `datasets/songs.csv` and prints the top 3 songs for my favourite song, once on raw data and once after normalization.
- `squashing.py`: sigmoid, ReLU and tanh, plus a demo of sigmoid breaking on -1000 and the fix.
- `RESULTS.md`: my prediction (written before running any code), both top-3 lists, and whether they agree.
- `NOTES.md`: plain-language notes on why a score of 47 is a problem and when to use sigmoid or tanh.

## How to run
Python 3. No installs.

From this folder:

    python similarity.py
    python squashing.py

From the repo root:

    python Level_1/logicarius/similarity.py
    python Level_1/logicarius/squashing.py

## Constraints
Pure Python. Only `math`, `csv` and `os` are used. No NumPy.

## What you should see
- `similarity.py`: a few test lines, the 10 songs, then the raw top 3 (Rooftop Monsoon, Fresher Night, Canteen Bass) and the normalized top 3 (Fresher Night, Canteen Bass, Hostel Corridor).
- `squashing.py`: sigmoid, ReLU and tanh test values, the line `naive sigmoid breaks: math range error`, then the fixed sigmoid and tanh values at extreme inputs.