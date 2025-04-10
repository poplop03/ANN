import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.01, epochs=1000):
        # Initialize weights and bias
        self.weights = np.zeros(input_size)
        self.bias = 0
        self.learning_rate = learning_rate
        self.epochs = epochs

    def activation_function(self, x):
        # Step activation function
        return 1 if x >= 0 else 0

    def predict(self, x):
        # Calculate the linear combination of inputs and weights
        linear_output = np.dot(x, self.weights) + self.bias
        # Apply the activation function
        return self.activation_function(linear_output)

    def fit(self, X, y):
        # Training the perceptron
        for _ in range(self.epochs):
            for idx, x_i in enumerate(X):
                # Make a prediction
                prediction = self.predict(x_i)
                # Calculate the error
                error = y[idx] - prediction
                # Update the weights and bias
                self.weights += self.learning_rate * error * x_i
                self.bias += self.learning_rate * error

# Example usage
if __name__ == "__main__":
    # Training data: logical AND function
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 0, 0, 1])

    # Create a perceptron with 2 inputs
    perceptron = Perceptron(input_size=2)
    # Train the perceptron
    perceptron.fit(X, y)

    # Test the perceptron
    for x in X:
        print(f"Input: {x}, Predicted Output: {perceptron.predict(x)}")