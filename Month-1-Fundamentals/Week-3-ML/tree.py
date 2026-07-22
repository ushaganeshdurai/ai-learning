'''
Building a decision tree

Dataset: Titanic-style survival data (age, sex, class, fare -> survived 0/1)

1. Train a DecisionTreeClassifier with max_depth=3
2. Visualize the tree using plot_tree
3. Identify the root split - what feature does it split on first?
4. Compare train vs test accuracy - is it overfitting?
5. Try max_depth=None (unlimited) - what happens to overfitting?
'''
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score

data = pd.read_csv("Titanic-Dataset.csv")

# Select only numeric features (drop Name, Sex, Ticket, Cabin, Embarked, PassengerId)
X = data[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']]
y = data["Survived"]

# Encode Sex column (male=1, female=0)
X['Sex'] = (data['Sex'] == 'male').astype(int)

# Handle missing values
X = X.fillna(X.median(numeric_only=True))

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=99)
clf = DecisionTreeClassifier(random_state=1,max_depth=None)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)

# Print accuracy metrics
print(f"Train Accuracy: {clf.score(X_train, y_train):.3f}")
print(f"Test Accuracy: {clf.score(X_test, y_test):.3f}")

plt.figure(figsize=(12,8))
plot_tree(clf, filled=True, feature_names=X.columns, class_names=['Died', 'Survived'])
plt.show()

'''
Exercise 2

Use the same Titanic-style dataset

1. Train a single DecisionTreeClassifier
2. Train a RandomForestClassifier with 100 trees
3. Compare test accuracy of both
4. Plot feature_importances_ from the Random Forest
5. Explain in 2 sentences why the forest is more stable
'''

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
X1 = data[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']]
y1 = data["Survived"]
X1_train,X1_test,y1_train,y1_test = train_test_split(X1,y1,test_size=0.3,random_state=99)
rf_clf = RandomForestClassifier(max_depth=2, random_state=0,n_estimators=100)

rf_clf.fit(X1_train, y1_train)
importances = rf_clf.feature_importances_
importance_df = pd.DataFrame({'Feature': X1_train.columns, 'Importance': importances})
importance_df = importance_df.sort_values(by='Importance', ascending=False)
print("Important features: ",importance_df)
print(rf_clf.score(X1_train, y1_train))
y1_pred=rf_clf.predict(X1_test)
print(rf_clf.score(X1_test,y1_test))