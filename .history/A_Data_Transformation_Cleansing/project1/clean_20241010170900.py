# Clean healthcare data

# Import necessary libraries
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv(
    "/Users/carolinesanicola/Documents/GitHub/sample-of-skills/A_Data_Transformation_Cleansing/project1/data/healthcare_claims_sample.csv")

# Display the first 5 rows
print(df.head())

# Inspect the data structure:
# - Understand the dataset by examining its structure: column names, data types, and basic statistics.
print(df.info())
'''
Sample Output:
Data columns (total 13 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   Claim ID        165 non-null    object 
 1   Patient ID      165 non-null    object 
 2   Age             86 non-null     float64
 3   Gender          95 non-null     object 
 4   Diagnosis Code  165 non-null    object 
 5   Claim Date      165 non-null    object 
 6   Service Code    165 non-null    int64  
 7   Amount Billed   148 non-null    float64
 8   Amount Paid     125 non-null    float64
 9   Payment Date    125 non-null    object 
 10  Insurance Plan  133 non-null    object 
 11  Claim Status    165 non-null    object 
 12  Provider Name   165 non-null    object 
'''
print(df.describe())
'''
Sample Output:
             Age  Service Code  Amount Billed  Amount Paid
count  86.000000    165.000000     148.000000   125.000000
mean   52.186047  99207.927273     286.227230   219.012720
std    19.229580      5.315146     116.212449   108.745482
min    19.000000  99201.000000     101.920000    55.940000
25%    36.000000  99203.000000     188.462500   128.190000
50%    50.500000  99205.000000     277.815000   199.570000
75%    70.000000  99213.000000     380.062500   284.740000
max    89.000000  99215.000000     499.340000   457.440000
'''

# Get a value count of the categorical columns to see if there are inconsistent formats
print(df['Gender'].value_counts())  # capitalization isnt consistent
print(df['Diagnosis Code'].value_counts())  # no issues
print(df['Claim Date'].value_counts())  # inconsistent date format
print(df['Payment Date'].value_counts())  # inconsistent date format
print(df['Insurance Plan'].value_counts())  # no issues
print(df['Claim Status'].value_counts())  # no issues
print(df['Provider Name'].value_counts())  # no issues

# Step 2: Handling Missing Data
# 1. Identify Missing Data:
missing_data = df.isnull().sum()
print(missing_data)
'''
Sample Output:
'''
