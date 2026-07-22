'''
Dataset: house sizes (sqft) vs price
[(650, 70), (785, 85), (1200, 130), (1500, 160), (1850, 190)]  // (sqft in hundreds, price in thousands)

1. Plot the data (scatter)
3. Compare your slope/intercept with sklearn's LinearRegression
4. Predict price for a 2000 sqft house
5. Calculate R² score
'''
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
sqft = np.array([[650],[785],[1200],[1500],[1850]])
price = np.array([70,85,130,160,190])
plt.scatter(sqft,price)
model = LinearRegression()
model.fit(sqft,price)
model.predict([[2000]])
y_pred = model.predict(sqft)
plt.plot(sqft,y_pred)
plt.show()
print(r2_score(price,y_pred))

'''
Dataset: hours studied vs pass/fail
[(1,0), (2,0), (3,0), (4,1), (5,1), (6,1), (7,1), (2.5,0), (4.5,1)]

1. Fit a LogisticRegression model using sklearn
2. Plot the sigmoid decision boundary
3. Predict probability of passing for 3.5 hours studied
4. Change the decision threshold from 0.5 to 0.3 - how do predictions change?
'''
# Dataset
hours_studied = np.array([[1],[2],[3],[4],[5],[6],[7],[2.5],[4.5]])
pass_fail = np.array([0,0,0,1,1,1,1,0,1])

# Train model
model2 = LogisticRegression()
model2.fit(hours_studied, pass_fail)

# Create smooth x-values for plotting
x = np.linspace(0, 8, 200).reshape(-1, 1)

# Predict probabilities
probs = model2.predict_proba(x)[:, 1]

# Probability for 3.5 hours
prob_35 = model2.predict_proba([[3.5]])[0][1]
print(f"Probability of passing for 3.5 hours: {prob_35:.4f}")

# Decision boundary
w = model2.coef_[0][0]
b = model2.intercept_[0]
boundary = -b / w

print(f"Decision Boundary: {boundary:.2f} hours")

# Plot
plt.scatter(hours_studied, pass_fail, color="red", label="Actual Data")
plt.plot(x, probs, color="blue", label="Sigmoid Curve")
plt.axhline(y=0.5, color="green", linestyle="--", label="Threshold = 0.5")
plt.axvline(x=boundary, color="purple", linestyle="--", label="Decision Boundary")

plt.xlabel("Hours Studied")
plt.ylabel("Probability of Passing")
plt.title("Logistic Regression")
plt.legend()
plt.grid(True)
plt.show()

# Compare thresholds on training data
train_probs = model2.predict_proba(hours_studied)[:, 1]

pred_05 = (train_probs >= 0.5).astype(int)
pred_03 = (train_probs >= 0.3).astype(int)

print("\nActual Labels:")
print(pass_fail)

print("\nPredictions (Threshold=0.5):")
print(pred_05)

print("\nPredictions (Threshold=0.3):")
print(pred_03)

'''
Use the Iris dataset (built into sklearn)

1. Train a LogisticRegression with multi_class='multinomial'
2. Predict on the test set
3. Print classification_report (precision, recall, f1 per class)
4. Plot the confusion matrix as a heatmap
5. Identify which class is hardest to predict correctly and why
'''