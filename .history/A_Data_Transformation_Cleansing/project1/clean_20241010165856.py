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
print(df.describe())
