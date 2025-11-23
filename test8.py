# python code for data analysis    
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Load dataset
data = pd.read_csv('c:\\Users\\leno\\HousePrices.csv')  
# Display first few rows
print(data.head())
# Summary statistics
print(data.describe())  
# Check for missing values
