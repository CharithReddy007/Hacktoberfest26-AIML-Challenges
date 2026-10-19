import math

def sigmoid_naive(x): # sigmoid is 1 / (1 + e^(-x))
    return 1/(1 + math.exp(-x)) 

def sigmoid(x):
    if x>= 0:
        return 1/(1 + math.exp(-x))
    else:
        e = math.exp(x) # for negative x: use e^x and not e^(-x), to prevent overflow unlike sigmoid_naive
        return e/(1 + e)

def relu(x): # relu(x) = max(0,x)
    if x > 0:
        return x
    return 0

def tanh(x): # tanh(x) = (2*sigmoid(2x)) - 1
    return 2 * sigmoid(2*x) - 1 

if __name__ == "__main__":
    print(sigmoid(0)) # 0.5
    print(sigmoid(1)) # 0.731
    print(relu(-5), relu(3)) # 0, 3
    print(tanh(0)) # 0

    try:
        print(sigmoid_naive(-1000)) # raises OverflowError
    except OverflowError as err:
        print("naive sigmoid breaks:", err)

    print(sigmoid(-1000)) # 0
    print(sigmoid(1000)) # 1
    print(tanh(-1000), tanh(1000)) # -1.0, 1.0