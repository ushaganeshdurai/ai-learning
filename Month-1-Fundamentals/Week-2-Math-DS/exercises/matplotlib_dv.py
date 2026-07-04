'''
. Create x values: 0 to 10
2. Create y = x^2
3. Plot line
4. Add title "Quadratic Function"
5. Add x and y labels
6. Show grid
7. Display plot
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
xaxis = np.array([0,1,2,3,4,5,6,7,8,9,10])
yaxis = np.square(xaxis)
plt.title("Quadratic Function")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(visible=True)
plt.plot(xaxis,yaxis)
plt.show()

'''
1. Plot y = x
2. Plot y = x^2
3. Plot y = x^3
4. Add legend (y=x, y=x^2, y=x^3)
5. Customize line colors and styles
6. Add title and labels
'''

y=xaxis 
cubed_y=np.power(xaxis,3)
plt.plot(xaxis, y, label="y=x", color='red', linestyle='-', linewidth=2)
plt.plot(xaxis, yaxis, label="y=x^2", color='blue', linestyle='--', linewidth=2)
plt.plot(xaxis, cubed_y, label="y=x^3", color='green', linestyle=':', linewidth=2)
plt.title("Exercise 2")
plt.legend()
plt.show()

'''
Dataset: Iris or any dataset
1. Load dataset
2. Create subplot with:
   - Scatter: Feature1 vs Feature2
   - Histogram: Feature1 distribution
   - Box plot: All features
   - Heatmap: Correlation matrix
3. Add titles and labels to all
4. Save figure
'''
import seaborn as sns
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data,columns=iris.feature_names)
#scatter:
fig,axes = plt.subplots(2,2,figsize=(14,10))
fig.suptitle('Iris dataset analysis')
axes[0, 0].scatter(df.iloc[:, 0], df.iloc[:, 1],
                   alpha=0.6, c=iris.target, cmap='viridis', s=100)
axes[0, 0].set_xlabel(iris.feature_names[0])
axes[0, 0].set_ylabel(iris.feature_names[1])
axes[0, 0].set_title('Sepal Length vs Sepal Width')
axes[0, 0].grid(True, alpha=0.3)

# 2. Histogram (top-right): Distribution of Feature 1
axes[0, 1].hist(df.iloc[:, 0], bins=20, alpha=0.7,
                color='steelblue', edgecolor='black')
axes[0, 1].set_xlabel(iris.feature_names[0])
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].set_title('Distribution of Sepal Length')
axes[0, 1].grid(True, alpha=0.3, axis='y')

# 3. Box plot (bottom-left): All features
df.boxplot(ax=axes[1, 0])
axes[1, 0].set_title('Box Plot - All Features')
axes[1, 0].set_ylabel('Value (cm)')
axes[1, 0].tick_params(axis='x', rotation=45)

# 4. Heatmap (bottom-right): Correlation matrix
corr = df.corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0,
            ax=axes[1, 1], cbar_kws={'label': 'Correlation'})
axes[1, 1].set_title('Correlation Matrix')

# Adjust layout and save
plt.tight_layout()
plt.savefig('/home/lakshmi/iris_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Figure saved as iris_analysis.png")
plt.show()
