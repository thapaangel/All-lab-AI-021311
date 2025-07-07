import numpy as np

class Perceptron:
    def __init__(self, input_size, alpha=0.1, theta=0.5, epochs=100):
        self.alpha = alpha  # learning rate
        self.theta = theta  # threshold
        self.epochs = epochs
        self.weights = np.random.rand(input_size + 1)  # +1 for bias

    def activation(self, x):
        # Step function
        return 1 if x >= self.theta else 0

    def predict(self, inputs):
        # Add bias input as 1
        inputs = np.insert(inputs, 0, 1)
        weighted_sum = np.dot(inputs, self.weights)
        return self.activation(weighted_sum)

    def train(self, X, y):
        # Insert bias input as 1 in all inputs
        X = np.insert(X, 0, 1, axis=1)

        for epoch in range(self.epochs):
            total_error = 0
            for i in range(len(X)):
                output = self.activation(np.dot(X[i], self.weights))
                error = y[i] - output
                self.weights += self.alpha * error * X[i]
                total_error += abs(error)
            if total_error == 0:
                break

# Example usage:
# Sample data: OR gate
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 1, 1, 1])

model = Perceptron(input_size=2, alpha=0.1, theta=0.5, epochs=10)
model.train(X, y)

# Test
for sample in X:
    print(f"Input: {sample}, Predicted: {model.predict(sample)}")