import subprocess
import time

# Path to Microsoft Edge
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
profile_dir = ("Profile 2","Profile 1", "Profile 3")

# Your search queries
queries = ["weather today", "AI news", "python tricks"]

# Open 3 Bing searches
for query in queries:
    url = f"https://www.bing.com/search?q={query}"
    subprocess.Popen([edge_path, f"--profile-directory={profile_dir}", "https://www.bing.com"])
    time.sleep(2)
