# Setting things up  
# [Overview](https://edgartools.readthedocs.io/en/latest/)
# https://github.com/dgunning/edgartools/blob/main/notebooks/Beginners-Guide.ipynb

# 0. Venv and install edgar library
# python3 -m venv .venv
# source .venv/bin/activate
# pip install -U edgartools # latest version -U
# pip install packaging

# 1. Import the edgar library and set up the local storage
# https://edgartools.readthedocs.io/en/latest/getting-started/
from edgar import *

# 2. Tell the SEC who you are (required by SEC regulations)
set_identity("email@address.com")  # Replace with your email

# 3. Set the local storage directory
# This is where the downloaded data will be stored
# download_edgar_data() - this will download the latest data from the SEC (to update the local database)
use_local_storage()

# 4. Retrieve data from the SEC
# Example: Retrieve company information and filings
company = Company("AAPL")  # Example: Apple Inc.
print("Name:", company.name)  # Print the company name
print("CIK:", company.cik)  # Print the Central Index Key (CIK) of the company

# Getting Filings
company_filings = company.get_filings()  # Get all filings for the company
print("Total Filings:", len(company_filings))  # Print the total number of filings

# Example: List recent filings2
filings = company.get_filings().latest(150)  # Get 3 most recent filings
for filing in filings:
    print(f"Form: {filing.form},  Accession: {filing.accession_number}, Date: {filing.filing_date}")

# Or
filings.head(150)  # Display the first 3 filings in a DataFrame format