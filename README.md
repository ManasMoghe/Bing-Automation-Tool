# 🔍 Bing Automation Tool

This tool automates Bing searches in Microsoft Edge using predefined queries. It helps users complete search-related reward tasks quickly and easily.

---

## ⚙️ Features

- Automatically opens Edge with a specified user profile
- Performs multiple searches from a list (`search_queries.txt`)
- Each search opens in a **new tab** (to prevent slow internet issues)
- Ensures the script runs only once per day (unless forced)
- GUI with buttons for:
  - Run (daily check)
  - Force Run (bypass daily limit)
  - Exit

---

## 📦 How to Use

### 1. 📁 Files Needed
Place the following in the same folder:
- `BingAutomationTool.exe` (from the `dist/` folder)
- `search_queries.txt` — one search query per line

### 2. ▶️ Running the Tool
Just **double-click** the `BingAutomationTool.exe`.  
A window will appear:

- Click **Run** to execute the script (if not already run today)
- Click **Force Run** to override daily check and run anyway
- Click **Exit** to close the tool

---

## 📌 Requirements

- ✅ **Microsoft Edge** installed
- ✅ Windows system
- 🚫 Do NOT close the Edge window while the script is running
- 💡 Make sure `search_queries.txt` has **at least 10 queries**

---

## 🔧 Customization

### Modify the Query List
Open `search_queries.txt` and add or remove search terms.  
Each term should be on a new line:

