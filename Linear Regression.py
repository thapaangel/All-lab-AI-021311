def predict(x1, x2, w1, w2, b):
    return w1 * x1 + w2 * x2 + b

def train_linear_regression(dataset, learning_rate=0.01, max_epochs=1000):
    w1, w2, b = 0.0, 0.0, 0.0
    
    for epoch in range(max_epochs):
        total_error = 0
        for x1, x2, y_true in dataset:
            y_pred = predict(x1, x2, w1, w2, b)
            error = y_true - y_pred
            
            # Update weights and bias
            w1 += learning_rate * error * x1
            w2 += learning_rate * error * x2
            b += learning_rate * error
            
            total_error += error ** 2
        
        if total_error < 1e-6:
            break
    
    return w1, w2, b

# Example dataset: (x1, x2, y)
dataset = [
    (1.0, 2.0, 10.0),
    (2.0, 0.5, 8.0),
    (3.0, 2.5, 15.0),
    (4.0, 3.0, 20.0),
]

# Train the model
w1, w2, b = train_linear_regression(dataset)

print(f"Trained weights: w1 = {w1:.3f}, w2 = {w2:.3f}, bias = {b:.3f}")

# Test prediction
x1_test, x2_test = 3.5, 2.0
y_pred = predict(x1_test, x2_test, w1, w2, b)
print(f"Prediction for input ({x1_test}, {x2_test}): {y_pred:.3f}")