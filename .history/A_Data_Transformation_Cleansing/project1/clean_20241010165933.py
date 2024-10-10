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
 0   Claim ID        23 non-null     object 
 1   Patient ID      23 non-null     object 
 2   Age             23 non-null     float64
 3   Gender          23 non-null     object 
 4   Diagnosis Code  23 non-null     object 
 5   Claim Date      23 non-null     object 
 6   Service Code    23 non-null     int64  
 7   Amount Billed   23 non-null     float64
 8   Amount Paid     23 non-null     float64
 9   Payment Date    23 non-null     object 
 10  Insurance Plan  23 non-null     object 
 11  Claim Status    23 non-null     object 
 12  Provider Name   23 non-null     object 
'''
print(df.describe())
