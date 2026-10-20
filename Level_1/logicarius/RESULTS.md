# Level 1 Results

## Prediction (written before running any code)

Song I would recommend: Fresher Night

Why: Because the 3 features namely tempo, energy and danceability of Fresher Night are really close to the same 3 feature values of my favourite song. Duration feature doesn't affect the relatability of a song, thus it wasn't considered.

## Results

Top 3 raw cosine:
1. Rooftop Monsoon (0.99999)
2. Fresher Night (0.99957)
3. Canteen Bass (0.99916)

Top 3 after min-max normalization:
1. Fresher Night (0.9952)
2. Canteen Bass (0.9838)
3. Hostel Corridor (0.9754)

Agree with my prediction? Normalized: yes (Fresher Night is #1). Raw: no (Rooftop Monsoon was #1) because tempo and duration are much bigger numbers than energy and danceability so they dominated the score. Normalizing to 0–1 gave every feature an equal say even though that includes the duration feature which I had ignored in my prediction.