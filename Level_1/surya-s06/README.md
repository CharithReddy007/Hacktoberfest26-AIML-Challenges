# Level 1

## 1. Similarity - Song Recommendation

Hypothetical favourite song has the following features:

- **Tempo:** 124 BPM
- **Duration:** 210 seconds
- **Energy:** 0.78
- **Danceability:** 0.82

My initial prediction was **Canteen Bass** because its energy (0.82) and danceability (0.85) are close to those of the hypothetical favourite song.

### Results

The cosine similarity between the hypothetical favourite song and all ten songs was calculated both before and after min-max normalization.

**Top 3 WITHOUT normalization:**
* Rooftop Monsoon: 0.999994
* Fresher Night: 0.999573
* Canteen Bass: 0.999164

**Top 3 WITH normalization:**
* Fresher Night: 0.995150
* Canteen Bass: 0.983837
* Hostel Corridor: 0.975356

| Rank | Without Normalization | With Normalization |
|---|---|---|
| 1 | Rooftop Monsoon | Fresher Night |
| 2 | Fresher Night | Canteen Bass |
| 3 | Canteen Bass | Hostel Corridor |

### Conclusion

The rankings changed after normalization. Tempo and duration have much larger numerical values than energy and danceability; features with larger values overpowered the ones with smaller values. Min-max normalization scales each feature to a range of 0 to 1, making the features more comparable. 

## 2. Squashing - Activation Functions

Three activation functions were implemented in pure Python using the `math` library.

- **Sigmoid:** Maps inputs to values between 0 and 1.
- **ReLU:** Returns 0 for negative inputs and the input itself for positive inputs.
- **Tanh:** Maps inputs to values between -1 and 1.

### Sigmoid Overflow and Fix

The original sigmoid formula,

`1 / (1 + math.exp(-x))`

fails for very large negative inputs, such as `x = -1000`, because `math.exp(1000)` exceeds the representable floating-point range and raises an `OverflowError`.

To fix this, equivalent formula is used, `exp(x) / (1 + exp(x))` when `x` is negative. This avoids the overflow and produces a stable result.

Testing with inputs `-1000`, `-2`, `0`, `2`, and `1000` completed successfully for all three activation functions.
