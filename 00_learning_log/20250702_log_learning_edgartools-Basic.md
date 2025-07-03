## 📅 2025-07-02

### 🔍 Gemini Prompt(s)
- Tell me about this repo

### ✅ Gemini Output Summary
- This repository contains edgartools, a Python library for extracting and analyzing data from SEC EDGAR filings. It
  provides an intuitive API to access financial data, including company financials, insider trades, and fund holdings,
  aiming to simplify the process of financial analysis.


  Key features include:
   * Access to any SEC filing since 1994 (10-K, 10-Q, 8-K, 13F, etc.).
   * Easy extraction of financial statements (Balance Sheets, Income Statements, Cash Flows).
   * Automatic parsing of filings into structured Python objects and pandas DataFrames.
   * Analysis of 13F fund holdings and insider transactions (Forms 3, 4, 5).
   * Conversion of filing HTML to clean, readable text suitable for NLP and AI pipelines.
   * Targeted extraction of specific sections from filings.


  The library is designed to be user-friendly, allowing you to get started with just a few lines of code. For example,
  you can get a company's balance sheet with:

   1 from edgar import *
   2 set_identity("your.name@example.com")
   3 balance_sheet = Company("AAPL").get_financials().balance_sheet()



  The project has extensive documentation, welcomes community contributions, and is actively being developed with a
  roadmap that includes enhanced visualization tools and machine learning integrations.

### 🔍 Gemini Prompt(s)
- Summarize the overall purpose and architecture of this codebase. What are the key modules and what do they do?

### ✅ Gemini Output Summary
- Overall Purpose and Architecture


  The edgartools library is a Python package designed to simplify the process of accessing and analyzing data from the
  SEC's EDGAR database. It acts as a high-level API, abstracting away the complexities of web scraping and data parsing,
  and provides users with clean, structured Python objects and pandas DataFrames.


  The architecture is modular, with a clear separation of concerns. The core functionality is built around a few key
  concepts:


   * Identity Management: The library requires users to set an identity (User-Agent) to comply with SEC regulations. This
     is handled by the core module.
   * HTTP Client: A robust HTTP client (httpclient) manages requests to the SEC's servers, including throttling and error
     handling.
   * Filing Retrieval: The _filings module is responsible for finding and retrieving filings from EDGAR.
   * Data Parsing: Various modules are dedicated to parsing specific types of filings (e.g., thirteenf for 13F forms,
     ownership for Forms 3, 4, and 5, financials for XBRL data).
   * Data Representation: The parsed data is presented in user-friendly data objects and pandas DataFrames.

  Key Modules and Their Functions

  Here's a breakdown of the most important modules in the edgar directory:


   * `__init__.py`: This is the main entry point for the library. It imports and exposes the most commonly used classes
     and functions, such as Company, Filing, set_identity, and the find function. It also defines several convenience
     functions for retrieving specific types of filings (e.g., get_insider_transaction_filings).


   * `core.py`: This module provides the foundational building blocks of the library. It handles:
       * Identity Management: set_identity and get_identity manage the User-Agent string required by the SEC.
       * HTTP Client Configuration: It defines different access modes (NORMAL, CAUTION, CRAWL) to control the rate of
         requests to EDGAR.
       * Utility Functions: It contains various helper functions for tasks like decoding content, handling dates, and
         managing asynchronous operations.


   * `_filings.py`: This module is responsible for retrieving filings from the SEC. It defines the Filing and Filings
     classes, which allow users to search for and access individual filings and collections of filings.

   * `financials.py`: This module handles the extraction and parsing of financial data from XBRL filings. The Financials
     class provides methods to access the balance sheet, income statement, and cash flow statement.


   * `thirteenf.py`: This module is dedicated to parsing 13F filings, which disclose the holdings of institutional
     investment managers. The ThirteenF class extracts the infotable and provides access to the holdings data.


   * `ownership/forms.py`: This module handles the parsing of ownership forms (Forms 3, 4, and 5), which report insider
     transactions. The Ownership class and its subclasses (Form3, Form4, Form5) extract information about the reporting
     owner, the issuer, and the transactions themselves.


   * `entity/`: This directory contains modules related to SEC entities, such as companies and funds. Company is a key
     class that allows you to retrieve information about a specific company, including its filings.


   * `xbrl/`: This directory contains the logic for parsing and interpreting XBRL data, which is used to represent
     financial information in a structured format.


  In essence, the library is designed to provide a clean and Pythonic interface to the wealth of data available in the
  SEC EDGAR database, making it easier for developers and financial analysts to work with this information.

### 🔍 Gemini Prompt(s)
- Show me how a user would retrieve and parse a 10-K filing from EDGAR using this repo.

### ✅ Gemini Output Summary
Here is an example of how a user would retrieve and parse a 10-K filing from EDGAR using this library. This code will
  get the five most recent 10-K filings for Microsoft, extract the income statement from each, and then combine them into
  a single pandas DataFrame.



    1 from edgar import set_identity, Company
    2 from edgar.xbrl import XBRLS
    3 
    4 # 1. Set your identity to comply with SEC regulations
    5 set_identity("Your Name your.email@example.com")
    6 
    7 # 2. Get the company object for Microsoft
    8 company = Company("MSFT")
    9 
   10 # 3. Get the 5 most recent 10-K filings
   11 filings = company.get_filings(form="10-K").latest(5)
   12 
   13 # 4. Extract the XBRL data from the filings
   14 xbrls = XBRLS.from_filings(filings)
   15 
   16 # 5. Get the income statement
   17 income_statement = xbrls.statements.income_statement()
   18 
   19 # 6. Convert the income statement to a pandas DataFrame
   20 income_df = income_statement.to_dataframe()
   21 
   22 # Now you can work with the income statement data
   23 print(income_df)

### 💡 Insight
- tbd

### ❓ Follow-Up Questions
- tbd