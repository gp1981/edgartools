## 📅 {{date}}

### 🔍 Gemini Prompt(s)
> {{your_prompt}}

### ✅ Gemini Output Summary
- {{summary of what you learned}}

### 💡 Insight
- {{core ideas, patterns, or "aha" moments}}

### ❓ Follow-Up Questions
- {{things you want to explore next}}

# Prompt 1: Summarize the repo
"Summarize the overall purpose and architecture of this codebase. What are the key modules and what do they do?"

# Prompt 2: Extract workflows
"Show me how a user would retrieve and parse a 10-K filing from EDGAR using this repo."

# Prompt 3: Learning support
"Based on the Pandas operations used in this repo, generate 10 practice problems at intermediate level."

# Prompt 4: Deep dive
"Explain what happens inside edgartools/filing_downloader.py. What are the key classes, and what edge cases does it handle?"

---- ---- 

# Prompt 1: High-level map
"Read the entire codebase and give me a high-level architecture diagram or map of the repo. What are the key modules and what does each do?"

# Prompt 2: Entry points
"What are the main entry points or scripts used to interact with this repo? What happens when I run them?"

# Prompt 3: Class/function overview
"List the most important classes and functions in this codebase and briefly describe what they do. Rank them by frequency of use or centrality."

# Prompt 4: Dependencies
"Generate a dependency map or import graph for this repo. What are the core external libraries it uses?"

# Prompt 5: Learn patterns
"Identify how this repo loads, parses, and processes SEC filings. What are the core steps? Summarize the full ETL pipeline used."

# Prompt 6: API analysis
"Which parts of this codebase make HTTP requests to the SEC EDGAR database or similar sources? Show me how data is requested and parsed."

# Prompt 7: Explain a file
"Explain what `edgartools/sec_parser.py` does, step-by-step. Highlight any important design choices or edge cases handled."
