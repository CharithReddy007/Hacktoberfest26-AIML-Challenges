
import math


def sigmoid(x):
    """Squash a number into the range (0, 1)."""
    if x >= 0:
        return 1 / (1 + math.exp(-x))

    exp_x = math.exp(x)
    return exp_x / (1 + exp_x)


def relu(x):
    """Return zero for negative inputs; otherwise return x."""
    return max(0, x)


def tanh(x):
    """Squash a number into the range (-1, 1)."""
    return math.tanh(x)


if __name__ == "__main__":
    test_values = [-1000, -2, 0, 2, 1000]

    print("Input | Sigmoid | ReLU | Tanh")
    for value in test_values:
        print(
            f"{value:5} | {sigmoid(value):.6f} | "
            f"{relu(value):.6f} | {tanh(value):.6f}"
        )

    print("\nAll activation functions ran successfully.")
