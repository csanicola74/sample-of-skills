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
Claim ID           0
Patient ID         0
Age               79
Gender            70
Diagnosis Code     0
Claim Date         0
Service Code       0
Amount Billed     17
Amount Paid       40
Payment Date      40
Insurance Plan    32
Claim Status       0
Provider Name      0
'''

# 3. Decide on Handling Strategy
# for healthcare, we don't want to impute median or mean values in missing data
# remove rows with missing data
# df.dropna(inplace=True)
# if you want to remove rows with missing data in only a specific column:
# this is the best option because there isn't a patient associated with the claim
df.dropna(subset=['Claim ID'], inplace=True)
# see the new shape of the dataframe
print(df.shape)
# Sample Output: (165, 13)
# Step 3: Removing Duplicates
# 1. Identify Duplicates
duplicates = df[df.duplicated(subset='Claim ID')]
print(duplicates)
'''
Sample Output:
    Claim ID Patient ID   Age Gender  ... Payment Date Insurance Plan  Claim Status        Provider Name
56     C1030      P5742  47.0      f  ...   06/12/2023            PPO          Paid      Wellness Clinic
85     C1003      P1082  55.0    NaN  ...   02/22/2024       Medicare          Paid      Wellness Clinic
88     C1052      P2601  53.0    NaN  ...          NaN            PPO          Paid  Green Valley Clinic
97     C1141      P1050   NaN    NaN  ...   2023-03-15            PPO          Paid  Green Valley Clinic
107    C1090      P9713   NaN      M  ...   14-06-2024       Medicaid          Paid   East Valley Clinic
108    C1095      P2646  76.0      M  ...   2024-04-28       Medicare       Pending     Blue Sky Medical
118    C1113      P8287  79.0    NaN  ...   2023-05-02       Medicaid          Paid    Westside Hospital
122    C1084      P3161   NaN    NaN  ...   01/27/2024       Medicaid       Pending  Green Valley Clinic
129    C1060      P6967   NaN    NaN  ...   02/11/2024            NaN          Paid     Southside Clinic
131    C1075      P3588   NaN    NaN  ...   2023-06-07            NaN          Paid      Wellness Clinic
136    C1086      P8040  53.0      M  ...          NaN            HMO          Paid      Wellness Clinic
137    C1061      P7349  21.0    NaN  ...   02/15/2023            PPO          Paid   Northside Hospital
157    C1119      P1380  31.0    NaN  ...   04/25/2024            HMO          Paid         Health First
159    C1047      P2598  22.0    NaN  ...   03/22/2024            PPO          Paid  Green Valley Clinic
160    C1137      P4421  73.0      M  ...   07-09-2023       Medicare          Paid    Westside Hospital

[15 rows x 13 columns]
'''
# 2. Remove Duplicates
df.drop_duplicates(subset='Claim ID', inplace=True)
print(df.shape)

# this is better for healthcare where they can be duplicate information for everything other than the patient
