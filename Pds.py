import pandas as pd

# Load the dataset
data = pd.read_csv('your_dataset.csv')

# Data Cleaning Steps

# Step 1: Check for missing values
missing_values = data.isnull().sum()
print("Missing Values:\n", missing_values)

# Step 2: Drop rows with missing values (if necessary)
data.dropna(inplace=True)

# Step 3: Check for duplicates
duplicates = data.duplicated().sum()
print("Duplicate Rows:", duplicates)

# Step 4: Drop duplicate rows (if necessary)
data.drop_duplicates(inplace=True)

# Step 5: Check for inconsistencies or anomalies
# Example: Check unique values of a categorical column
unique_values = data['categorical_column'].unique()
print("Unique Values of Categorical Column:", unique_values)

# Step 6: Correct any inconsistencies or anomalies (if necessary)
# Example: Replace incorrect values
data['categorical_column'].replace({'incorrect_value': 'correct_value'}, inplace=True)

# Step 7: Check for outliers
# Example: Visualize boxplot to identify outliers in numerical columns
import seaborn as sns
sns.boxplot(data=data[['numerical_column1', 'numerical_column2']])
plt.title('Boxplot of Numerical Columns')
plt.show()

# Step 8: Handle outliers (if necessary)
# Example: Remove outliers using IQR method
Q1 = data['numerical_column1'].quantile(0.25)
Q3 = data['numerical_column1'].quantile(0.75)
IQR = Q3 - Q1
data = data[~((data['numerical_column1'] < Q1 - 1.5 * IQR) | (data['numerical_column1'] > Q3 + 1.5 * IQR))]

# Step 9: Check for data type inconsistencies
# Example: Check data types of columns
data_types = data.dtypes
print("Data Types:\n", data_types)

# Step 10: Convert data types if necessary
# Example: Convert a column to datetime format
data['date_column'] = pd.to_datetime(data['date_column'])

# Step 11: Save the cleaned data to a new file
data.to_csv('cleaned_data.csv', index=False)






#----------------------------------------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('your_dataset.csv')

# Visualization 1: Histogram
plt.figure(figsize=(8, 6))
data['numerical_column'].hist()
plt.title('Histogram of Numerical Column')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Visualization 2: Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='category_column', y='numerical_column', data=data)
plt.title('Boxplot of Numerical Column by Category')
plt.xlabel('Category')
plt.ylabel('Numerical Column')
plt.show()

# Visualization 3: Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(data['numerical_column1'], data['numerical_column2'])
plt.title('Scatter Plot of Numerical Column1 vs Numerical Column2')
plt.xlabel('Numerical Column1')
plt.ylabel('Numerical Column2')
plt.show()

# Visualization 4: Bar Plot
plt.figure(figsize=(8, 6))
data['category_column'].value_counts().plot(kind='bar')
plt.title('Bar Plot of Category Column')
plt.xlabel('Category')
plt.ylabel('Frequency')
plt.show()

# Visualization 5: Line Plot
plt.figure(figsize=(8, 6))
plt.plot(data['datetime_column'], data['numerical_column'])
plt.title('Line Plot of Numerical Column over Time')
plt.xlabel('Date')
plt.ylabel('Numerical Column')
plt.show()

# Visualization 6: Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Visualization 7: Pair Plot
plt.figure(figsize=(8, 6))
sns.pairplot(data)
plt.title('Pairwise Relationship Plot')
plt.show()

# Visualization 8: Violin Plot
plt.figure(figsize=(8, 6))
sns.violinplot(x='category_column', y='numerical_column', data=data)
plt.title('Violin Plot of Numerical Column by Category')
plt.xlabel('Category')
plt.ylabel('Numerical Column')
plt.show()

# Visualization 9: Pie Chart
plt.figure(figsize=(8, 6))
data['category_column'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Pie Chart of Category Column')
plt.ylabel('')
plt.show()

# Visualization 10: Distribution Plot
plt.figure(figsize=(8, 6))
sns.distplot(data['numerical_column'])
plt.title('Distribution Plot of Numerical Column')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()

# --------------------------------------------------------------------------------------------------------------------
#Bi variate,Univariate,multivariate analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('your_dataset.csv')

# Univariate Visualization 1: Histogram
plt.figure(figsize=(8, 6))
data['numerical_column'].hist()
plt.title('Histogram of Numerical Column')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Univariate Visualization 2: Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='category_column', y='numerical_column', data=data)
plt.title('Boxplot of Numerical Column by Category')
plt.xlabel('Category')
plt.ylabel('Numerical Column')
plt.show()

# Univariate Visualization 3: Kernel Density Estimation (KDE) Plot
plt.figure(figsize=(8, 6))
sns.kdeplot(data['numerical_column'], shade=True)
plt.title('Kernel Density Estimation Plot of Numerical Column')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()

# Bivariate Visualization 1: Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(data['numerical_column1'], data['numerical_column2'])
plt.title('Scatter Plot of Numerical Column1 vs Numerical Column2')
plt.xlabel('Numerical Column1')
plt.ylabel('Numerical Column2')
plt.show()

# Bivariate Visualization 2: Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Multivariate Visualization: Pair Plot
plt.figure(figsize=(8, 6))
sns.pairplot(data)
plt.title('Pairwise Relationship Plot')
plt.show()

# Multivariate Visualization: Violin Plot
plt.figure(figsize=(8, 6))
sns.violinplot(x='category_column', y='numerical_column', data=data)
plt.title('Violin Plot of Numerical Column by Category')
plt.xlabel('Category')
plt.ylabel('Numerical Column')
plt.show()

# Multivariate Visualization: Joint Plot
sns.jointplot(x='numerical_column1', y='numerical_column2', data=data, kind='scatter')
plt.title('Joint Plot of Numerical Column1 and Numerical Column2')
plt.show()

# Univariate Visualization 4: Pie Chart
plt.figure(figsize=(8, 6))
data['category_column'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Pie Chart of Category Column')
plt.ylabel('')
plt.show()

# Univariate Visualization 5: Distribution Plot
plt.figure(figsize=(8, 6))
sns.distplot(data['numerical_column'])
plt.title('Distribution Plot of Numerical Column')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()
