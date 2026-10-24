
# Decision Tree Algorithm

from sklearn.tree import DecisionTreeClassifier

# Training data
X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

# Create Decision Tree classifier
model = DecisionTreeClassifier()

# Train the model
model.fit(X, y)

# Predict the result
prediction = model.predict([[4]])

# Display the output
if prediction[0] == 1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")
