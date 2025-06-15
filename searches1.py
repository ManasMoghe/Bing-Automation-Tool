import subprocess
import time

# Path to Microsoft Edge
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Your search queries
queries = ["weather today", "AI news", "python tricks"]

# Open 3 Bing searches
for query in queries:
    url = f"https://www.bing.com/search?q={query}"
    subprocess.Popen([edge_path, url])
    time.sleep(2)  # delay between opening tabs
