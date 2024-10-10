# Creates random sample data for this project
# The data is newly randomized each time this script is ran
'''
Data Dictionary:
- Claim ID: Unique identifier for each healthcare claim
- Patient ID: Unique identifier for each patient.
- Age: Age of the patient.
- Gender: Patient’s gender (M = Male, F = Female, Nonbinary).
- Diagnosis Code: ICD-10 diagnosis code for the patient's condition.
- Claim Date: Date the healthcare claim was submitted.
- Service Code: CPT/HCPCS code for the medical service provided.
- Amount Billed: Amount billed by the healthcare provider.
- Amount Paid: Amount paid by the insurance company.
- Payment Date: Date the payment was made by the insurance.
- Insurance Plan: Type of insurance plan (e.g., PPO, HMO).
- Claim Status: Status of the claim (Paid, Pending, Denied).
- Provider Name: Name of the healthcare provider or clinic.
'''
# Install the necessary Python libraries if they are not already installed
# !pip3 install pandas numpy faker

# Import the necessary libraries
from datetime import datetime, timedelta
import random
from faker import Faker
import numpy as np
import pandas as pd

# Initialize Faker
fake = Faker()

# Configuration
NUM_RECORDS = 150
DUPLICATE_PROBABILITY = 0.25
MISSING_VALUE_PROBABILITY = 0.1
GENDER_OPTIONS = ['M', 'F', 'Nonbinary']
INSURANCE_PLANS = ['PPO', 'HMO', 'Medicare', 'Medicaid', 'None']
CLAIM_STATUS = ['Paid', 'Pending', 'Denied']
SERVICE_CODES = ['99201', '99202', '99203', '99204',
                 '99205', '99211', '99212', '99213', '99214', '99215']
DIAGNOSIS_CODES = ['E11.9', 'I10', 'J45.909',
                   'Z00.00', 'M54.5', 'E11.65', 'N18.9']
PROVIDER_NAMES = ['Green Valley Clinic', 'Blue Sky Medical', 'Wellness Clinic',
                  'Health First', 'Westside Hospital', 'East Valley Clinic', 'Southside Clinic', 'Northside Hospital']

# Function to randomly introduce missing values


def introduce_missing(value):
    if random.random() < MISSING_VALUE_PROBABILITY:
        return np.nan
    return value

# Function to generate random dates within the last year


def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


# Generate unique records
records = []
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 10, 10)

for i in range(1, NUM_RECORDS + 1):
    claim_id = f"C{1000 + i}"
    patient_id = f"P{random.randint(1000, 9999)}"
    age = random.choice([random.randint(18, 90), np.nan]
                        )  # Introduce missing ages
    # Introduce missing genders
    gender = random.choice(GENDER_OPTIONS + [np.nan])
    diagnosis_code = random.choice(DIAGNOSIS_CODES)
    claim_date = random_date(start_date, end_date).strftime("%m/%d/%Y")
    service_code = random.choice(SERVICE_CODES)
    amount_billed = round(random.uniform(
        100, 500), 2) if random.random() > 0.05 else np.nan  # 5% missing
    amount_paid = round(amount_billed * random.uniform(0.5, 1.0), 2) if not pd.isna(
        amount_billed) and random.random() > 0.2 else np.nan  # 20% missing
    payment_date = (datetime.strptime(claim_date, "%m/%d/%Y") + timedelta(days=random.randint(1, 30))
                    # 10% missing
                    ).strftime("%m/%d/%Y") if not pd.isna(amount_paid) and random.random() > 0.1 else np.nan
    insurance_plan = random.choice(INSURANCE_PLANS)
    claim_status = random.choices(CLAIM_STATUS, weights=[0.7, 0.2, 0.1])[0]
    provider_name = random.choice(PROVIDER_NAMES)

    # Introduce inconsistent gender capitalization
    if isinstance(gender, str) and random.random() < 0.3:
        gender = gender.lower()

    record = {
        "Claim ID": claim_id,
        "Patient ID": patient_id,
        "Age": introduce_missing(age),
        "Gender": introduce_missing(gender),
        "Diagnosis Code": diagnosis_code,
        "Claim Date": claim_date,
        "Service Code": service_code,
        "Amount Billed": introduce_missing(amount_billed),
        "Amount Paid": introduce_missing(amount_paid),
        "Payment Date": payment_date,
        "Insurance Plan": insurance_plan,
        "Claim Status": claim_status,
        "Provider Name": provider_name
    }

    records.append(record)

# Convert to DataFrame
df = pd.DataFrame(records)

# Introduce duplicates
duplicates = df.sample(frac=DUPLICATE_PROBABILITY, random_state=None)
df = pd.concat([df, duplicates], ignore_index=True)

# Shuffle the DataFrame
df = df.sample(frac=1).reset_index(drop=True)

# Introduce some inconsistent date formats


def inconsistent_date_format(date_str):
    if pd.isna(date_str):
        return date_str
    date_obj = datetime.strptime(date_str, "%m/%d/%Y")
    # Randomly choose a different format
    formats = ["%m/%d/%Y", "%Y-%m-%d", "%d-%m-%Y"]
    return date_obj.strftime(random.choice(formats))


df['Claim Date'] = df['Claim Date'].apply(
    lambda x: inconsistent_date_format(x))
df['Payment Date'] = df['Payment Date'].apply(
    lambda x: inconsistent_date_format(x))

# Save to CSV
df.to_csv("/Users/carolinesanicola/Documents/GitHub/sample-of-skills/A_Data_Transformation_Cleansing/project1/data/healthcare_claims_sample.csv", index=False)

print("Sample healthcare claims data has been generated and saved to 'healthcare_claims_sample.csv'.")
