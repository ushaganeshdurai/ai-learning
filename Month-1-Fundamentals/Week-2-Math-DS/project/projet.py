'''
# Mini Project: Employee Salary & Performance Analytics

## Scenario

You are given data for **1000 employees** in a company. Create a dataset and analyze employee performance, salaries, and experience using NumPy, Pandas, Matplotlib, Linear Algebra, Statistics, and Probability.

***

## Dataset Requirements

Create the following columns:

* Employee\_ID
* Age
* Years\_of\_Experience
* Salary
* Performance\_Score
* Training\_Hours

Use realistic values and randomly generate the data.

***

# Part 1: NumPy & Arrays

### Tasks

1. Generate 1000 employee records.
2. Store numeric features initially as NumPy arrays.
3. Check:
   * Shape of each array
   * Data type
   * Minimum and maximum values
4. Create a matrix containing all numerical features.

***

# Part 2: Pandas & Data Analysis

### Tasks

1. Convert the dataset into a Pandas DataFrame.
2. Display:
   * First 5 rows
   * Last 5 rows
3. Find:
   * Average salary
   * Average performance score
   * Average experience
4. Determine:
   * Highest-paid employee
   * Lowest-paid employee
5. Create a new column:
   * Salary Category (Low, Medium, High)

### Questions

* Which salary category has the most employees?
* What is the average performance score for each category?

***

# Part 3: Statistics & Probability

### Tasks

1. Calculate:

   * Mean
   * Median
   * Mode
   * Variance
   * Standard Deviation

   for:

   * Salary
   * Performance Score

2. Identify outliers in Salary.

### Probability Questions

1. Probability that an employee earns more than a specified salary threshold.
2. Probability that a performance score exceeds a specified value.
3. Probability that an employee has more than a specified years of experience.

### Interpretation

Compare your sample statistics with the expected values used while generating the data.

***

# Part 4: Data Visualization

### Create the following plots

1. Histogram of salaries.
2. Histogram of performance scores.
3. Scatter plot:
   * Experience vs Salary
4. Scatter plot:
   * Training Hours vs Performance Score
5. Bar chart:
   * Number of employees in each Salary Category
6. Box plot:
   * Salary distribution

### Questions

* Is salary normally distributed?
* Are there outliers?
* Does experience appear related to salary?

***

# Part 5: Linear Algebra

Using the numerical features matrix:

### Tasks

1. Find matrix dimensions.
2. Compute:
   * Mean vector
   * Covariance matrix
3. Calculate:
   * Eigenvalues
   * Eigenvectors

### Questions

* Which feature contributes most to data variance?
* Which feature appears most important based on the covariance matrix?

***

# Final Insights Report

Write a short report answering:

1. What is the average employee profile?
2. Which metric has the highest variability?
3. Is experience strongly related to salary?
4. What percentage of employees are high performers?
5. What business recommendations would you provide based on the analysis?

***

## Stretch Goal (Optional)

Perform a simple PCA using the covariance matrix and visualize the employees in 2D using the first two principal components.

This single project covers:

* ✅ NumPy Arrays
* ✅ Pandas Data Analysis
* ✅ Statistics
* ✅ Probability
* ✅ Matplotlib Visualization
* ✅ Linear Algebra (Covariance, Eigenvalues, Eigenvectors)

It's an excellent Notion portfolio exercise because it mirrors a real-world HR analytics problem rather than isolated topic-wise questions.

'''