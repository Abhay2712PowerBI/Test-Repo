# reading a file and perform data analysis using pandas 
import pandas as pd

# Load the dataset
df = pd.read_csv('C:/Companies Courses/Simpli Learn/Cohort- IG DA/7357_Data_Analytics_with_Python/Demo/Lesson 4/HousePrices_dataset.csv')

# Display the first few rows of the dataframe
print(df.head())

# Get a summary of the dataframe
print(df.describe())

# Check for missing values
print(df.isnull().sum())
# Fill missing values with the mean of the column
df.fillna(df.mean(), inplace=True)  
# Perform a simple data analysis: calculate the mean of a specific column
mean_value = df['column_name'].mean()
print(f"The mean value of 'column_name' is: {mean_value}")
# Group by a specific column and calculate the sum of another column
grouped_data = df.groupby('group_column')['value_column'].sum() 
print(grouped_data)
# Save the cleaned dataframe to a new CSV file