# Level 1 

## 1. Why do we need sigmoid?

A linear model might give a song a score of 47. But 47 cannot be a probability because probabilities must be between 0 and 1. Sigmoid converts any real-number score into a value between 0 and 1. For example, a large positive score produces a value close to 1, suggesting a higher likelihood. 

## 2. Sigmoid vs. tanh

Sigmoid produces values between 0 and 1, so it is useful when we want an output that represents a probability, such as whether someone might like a song.

Tanh produces values between -1 and 1.
I would prefer tanh when both positive and negative values are useful, because its output is centered around zero. For example, negative values could represent dislike and positive values could represent liking.

Both functions smoothly squash large inputs into limited ranges, but the best choice depends on what the model needs to represent.

