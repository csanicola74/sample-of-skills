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
DIAGNOSIS_CODES = ['E11.9', 'I10', '']
