# Clean healthcare data

# Import necessary libraries
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv(
    "/Users/carolinesanicola/Documents/GitHub/sample-of-skills/A_Data_Transformation_Cleansing/project1/data/healthcare_claims_sample.csv")

# Display the first 5 rows
print(df.head())

# Step 1: Handle missing values
df = df.dropna()

# Step 2: Handle duplicate rows
df = df.drop_duplicates()

# Step 3: Standardize Formats
# get counts of each column to see which columns need standardization
