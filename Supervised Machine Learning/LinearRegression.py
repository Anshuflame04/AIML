# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Sample dataset: Study hours vs. Exam scores
data = {
    "Hours": [2.5, 5.1, 3.2, 8.5, 1.5, 9.2, 5.5, 8.3, 2.7, 7.7],
    "Scores": [21, 47, 27, 75, 20, 88, 60, 81, 25, 85]
}
df = pd.DataFrame(data)

# Separate features and target variable
X = df[["Hours"]]  # Input: hours studied
y = df["Scores"]   # Output: exam scores

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model on the training set
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)  #coefficient of determination
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)


# Predicting based on user input
try:
    hours_studied = float(input("Enter the number of study hours: "))
    predicted_score = model.predict([[hours_studied]])
    print(f"Predicted exam score for {hours_studied} hours of study: {predicted_score[0]:.2f}")
except ValueError:
    print("Invalid input! Please enter a numeric value for study hours.")

# Visualize the training data, test data, and the regression line
plt.scatter(X_train, y_train, color="blue", label="Training Data")
plt.scatter(X_test, y_test, color="green", label="Test Data")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.legend()
plt.show()
