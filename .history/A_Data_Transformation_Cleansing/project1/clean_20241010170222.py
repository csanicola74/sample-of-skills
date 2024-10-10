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
count  23.000000     23.000000      23.000000    23.000000
mean   59.695652  99205.695652     296.995217   225.276957
std    21.401858      4.856437     108.582070    87.317991
min    25.000000  99201.000000     137.060000   102.130000
25%    43.000000  99202.000000     198.690000   138.255000
50%    60.000000  99204.000000     292.540000   226.520000
75%    78.500000  99208.000000     363.470000   315.055000
max    90.000000  99215.000000     477.330000   346.840000
'''
