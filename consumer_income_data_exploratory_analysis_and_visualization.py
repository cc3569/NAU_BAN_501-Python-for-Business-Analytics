# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Import data
df = pd.read_csv("/content/consumer_income (1).csv")
print(df.head())
print()

# Print the descriptive statistics
print(df.describe())
print()

# Check for missing data
print(df.isnull().sum())
print()

# Drow rows of missing income data
df = df.dropna(subset=['Income'])

# Recheck for missing data
print(df.isnull().sum())
print()

# Print the shape of the data
print(df.shape)

# Create an age column using the datetime function
df['Age'] = datetime.now().year - df['Year_Birth']

# Print the hader of the data to verify Age column
print(df.head())
print()

# Plot the age variable using a histogram
plt.hist(df['Age'], bins=10)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()
print()

# Remove three of the year birth outliers
# Sort values
print(df['Year_Birth'].sort_values())
print()
# Remove the three outliers by row ID
df = df.drop([239,339,192], axis=0)
# Print sorted values to verify drops.
print(df['Year_Birth'].sort_values())
print()

# Plot the age variable using a histogram again without outliers
plt.hist(df['Age'], bins=10)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()
print()

# Create a basic plot of income
# plt.plot(df['Income'])
# Plot a dot plot instead
plt.plot(df['Income'], 'o')
plt.title('Basic plot of income.')
plt.ylabel('Incomes')
plt.xlabel('Records')
plt.show()
print()

# Remove the income outlier
print(df['Income'].sort_values(ascending=False))
print()
df = df.drop(2233, axis=0)

# Reprint sorted values
print(df['Income'].sort_values(ascending=False))

# Replot dot plot
plt.plot(df['Income'], 'o')
plt.title('Basic plot of income.')
plt.ylabel('Incomes')
plt.xlabel('Records')
plt.show()
print()

# Create a scatterplot to show the relationship between age and income
plt.scatter(df['Age'], df['Income'])
plt.title('Relationship Between Age and Income')
plt.xlabel('Age')
plt.ylabel('Income')
plt.show()
print()

# Create a boxplot showing a comparison of incomes for different subgroups
plt.boxplot(
    [
        df[df['Marital_Status'] == 'Married']['Income'],
        df[df['Marital_Status'] == 'Single']['Income'],
        df[df['Marital_Status'] == 'Divorced']['Income']
    ],
    labels=['Married', 'Single', 'Divorced']
)
plt.title('Comparison of Income by Marital Status')
plt.ylabel('Income')
plt.xlabel('Marital Status')
plt.show()
print()
