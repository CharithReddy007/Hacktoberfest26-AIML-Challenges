## Why 47 is a problem

A probability is a number from 0 (no chance) to 1 (certain). A score of 47 can't be one. It's like telling someone a student got 15 marks without saying whether it's out of 20 or 100. Thus, the number means nothing without the scale.

Sigmoid fixes this. It squashes any number into the range 0 to 1. Big negative numbers become close to 0, zero becomes 0.5 and big positive numbers become close to 1. So 47 becomes almost 1: nearly certain you'll like the song.

## Sigmoid or tanh?

Pick sigmoid when you want a yes/no answer. An output of 0.8 means an 80% chance you'll like the song.

Pick tanh when it matters whether the answer is positive or negative. It ranges from -1 to 1, with 0 meaning average. For example: is this song's mood more cheerful (positive) or more gloomy (negative) than average?