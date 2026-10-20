# pls just work
import math

def sigmoid_break(x):
    return 1 / (1+math.exp(-x))
    #This will cause an overflow 

def sigmoid(x):
    if x >=0:
        return 1 /(1+math.exp(-x))
    e = math.exp(x)
    return e /(1+e)

def relu(x):
    # Rectified Linear Unit
    if x >=0:
        return x
    else:

        return 0

def tanh(x):
    return math.tanh(x)

if __name__ == "__main__":
    try:
        print(sigmoid_break(-1000))
    except OverflowError as err:
        print("Sigmoid Function broke: ", err)
    print(f"sigmoid(0): {sigmoid(0)}")
    print(f"sigmoid(2): {sigmoid(2)}")
    print("Fixed sigmoids: ",sigmoid(1000))
    print("Fixed sigmoids: ",sigmoid(-1000))
    print(f"sigmoid(-8): {sigmoid(-8)}")
    print(f"sigmoid(47): {sigmoid(47)}")
    
    print(f"tanh(0): {tanh(0)}")
    print(f"tanh(2): {tanh(2)}")
    print(f"tanh(1000): {tanh(1000)}")
    print(f"tanh(-1000): {tanh(-1000)}")
    print(f"tanh(-8): {tanh(-8)}")


    print(f"relu(-5): {relu(-5)}")
    print(f"relu(5): {relu(5)}")
    print(f"relu(0): {relu(0)}")

    