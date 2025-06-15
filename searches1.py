import webbrowser
import time

# List of 3 search queries
search_queries = ["weather today", "news headlines", "coding tutorials"]

for query in search_queries:
    # Format the Bing search URL
    url = f"https://www.bing.com/search?q={query}"
    webbrowser.open_new_tab(url)
    time.sleep(2)  # Wait a bit between tabs
