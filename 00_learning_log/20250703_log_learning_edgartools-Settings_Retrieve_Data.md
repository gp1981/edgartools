## 📅 2025-07-02

## Refers to GPT4.1
gp1981:  Based on the repository and the explanation in my log folder I want to learn how to retrieve data in the current py file. Let's make 3 or for examples i can code. I am in learning mode and the instructions are included in GEMINI.md

GitHub Copilot: You have exceeded your premium request allowance. We have automatically switched you to GPT-4.1 which is included with your plan. [Enable additional paid premium requests](command:chat.enablePremiumOverages) to continue using premium models.Great! Based on your learning goals and the guidelines in GEMINI.md, here are **three incremental examples** you can try in your 20250703_code_Retrieve_data.py file to learn how to retrieve data with `edgartools`. Each example builds on the previous one and is explained for someone with general programming knowledge.

---

## **Example 1: Fetch Basic Company Info**

**Goal:** Get and print basic information about a company (e.g., Apple).

````python
# ...existing code...

# Example 1: Fetch basic company info
from edgar import Company

set_identity("your.email@example.com")  # Always set your identity

company = Company("AAPL")  # "AAPL" is Apple's ticker symbol

print("Company Name:", company.name)
print("CIK:", company.cik)  # CIK is a unique SEC identifier
print("Ticker:", company.ticker)
# ...existing code...
````

---

## **Example 2: List Recent Filings for a Company**

**Goal:** Get the 3 most recent filings for Apple and print their type and date.

````python
# ...existing code...

# Example 2: List recent filings
filings = company.get_filings().latest(3)  # Get 3 most recent filings

for filing in filings:
    print(f"Form: {filing.form}, Date: {filing.date}, Accession: {filing.accession_number}")
# ...existing code...
````

---

## **Example 3: Retrieve and Display an Income Statement**

**Goal:** Get the latest 10-K filing for Apple and display its income statement as a table.

````python
# ...existing code...

# Example 3: Retrieve and display an income statement
from edgar.xbrl import XBRLS

# Get the latest 10-K filing
latest_10k = company.get_filings(form="10-K").latest(1)

# Extract XBRL data (structured financials)
xbrls = XBRLS.from_filings(latest_10k)

# Get the income statement (as a DataFrame)
income_statement = xbrls.statements.income_statement()
income_df = income_statement.to_dataframe()

print(income_df.head())  # Show the first few rows
# ...existing code...
````

---

**Tips:**
- Run each example separately at first to see what it does.
- You can change `"AAPL"` to another ticker (like `"MSFT"` for Microsoft).
- If you see errors, check that you have set your identity and installed all dependencies.

Let me know if you want a fourth, more advanced example (like extracting data for multiple years or saving to a CSV)!

### 💡 Insight
- tbd

### ❓ Follow-Up Questions
- tbd