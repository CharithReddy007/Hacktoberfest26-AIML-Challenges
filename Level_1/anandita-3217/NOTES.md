## Notes
1. A linear model scores a song as 47. Why is that a problem if you wanted the probability that you will like it, and what does sigmoid do about it?

- Probabilty lies between 0 and 1. 
- 1 -> event will def occur
- 0 -> event will not occur
- Probability of 47 means the event occurs with a 4700% chance which doesnt make sense.
- sigmoid will squash the value to between 0 and 1 and so the probability will now lie between 0 and 1.
- Greater the given value the closer it is to 1 and the smaller the value the closer it is to 0




2. Sigmoid and tanh look similar. When might you prefer one over the other? 

- Sigmoid Range : [0,1]
- Tanh Range : [-1,1]

- Sigmoid preferred when we are dealing with probabilitic/ stochastic(problems where chance is involved) problems or classification problems. output is always non negative
- Tanh preferred when value can be neative negative input gives negative output and positive input gives positive output




