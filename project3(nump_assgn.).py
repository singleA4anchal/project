#NumPy
#(numpy_assignment.ipynb)
# Step 1: Import NumPy
import numpy as np

# 1. 1D Array from 1 to 20
arr1 = np.arange(1, 21)
print("Array:", arr1)

# a. Statistics
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Median:", np.median(arr1))
print("Standard Deviation:", np.std(arr1))

# b. Indices of elements > 10
print("Indices where arr1 > 10:", np.where(arr1 > 10))

# 2. 2D Array 4x4
arr2 = np.arange(1, 17).reshape(4, 4)
print("2D Array:\n", arr2)

print("Transpose:\n", arr2.T)
print("Row-wise sum:", np.sum(arr2, axis=1))
print("Column-wise sum:", np.sum(arr2, axis=0))

# 3. Random 3x3 arrays
a = np.random.randint(1, 21, (3, 3))
b = np.random.randint(1, 21, (3, 3))
print("Array A:\n", a)
print("Array B:\n", b)

print("Addition:\n", a + b)
print("Subtraction:\n", a - b)
print("Multiplication:\n", a * b)
print("Dot Product:\n", np.dot(a, b))

# 4. Reshaping and slicing
arr3 = np.arange(1, 13).reshape(3, 4)
print("Reshaped Array:\n", arr3)
print("First 2 rows & last 2 columns:\n", arr3[:2, -2:])


Pandas (pandas_assignment.ipynb)
import pandas as pd
# 1. Create DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'HR'],
    'Salary': [45000, 54000, 50000, 62000, 47000]
}
df = pd.DataFrame(data)
print(df.head())

print(df[['Age', 'Salary']].describe())
print("Average Salary in HR:", df[df['Department'] == 'HR']['Salary'].mean())

# 2. Add Bonus column
df['Bonus'] = df['Salary'] * 0.1

# 3. Filter employees aged 25–30
print(df[(df['Age'] >= 25) & (df['Age'] <= 30)])

# 4. Group by Department
print(df.groupby('Department')['Salary'].mean())

# 5. Sort by Salary & save
sorted_df = df.sort_values(by='Salary', ascending=True)
print(sorted_df)
sorted_df.to_csv("sorted_employees.csv", index=False)


Matplotlib (matplotlib_assignment.ipynb)
import matplotlib.pyplot as plt
import numpy as np

# 1. Line Plot
x = [1, 2, 3, 4, 5]
y = [10, 15, 25, 30, 50]

plt.plot(x, y, marker='o')
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# 2. Bar Graph
students = ['John', 'Jane', 'Alice', 'Bob']
marks = [75, 85, 60, 90]

plt.bar(students, marks, color=['blue', 'green', 'orange', 'red'])
plt.title("Student Marks")
plt.show()

# 3. Pie Chart
regions = ['North America', 'Europe', 'Asia', 'Others']
revenue = [45, 25, 20, 10]

explode = [0.1 if r == max(revenue) else 0 for r in revenue]
plt.pie(revenue, labels=regions, autopct='%1.1f%%', explode=explode)
plt.title("Company Revenue by Region")
plt.show()

# 4. Histogram
data = np.random.randint(1, 101, 1000)
plt.hist(data, bins=20, color='purple', edgecolor='black')
plt.title("Histogram of Random Integers")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()