import os

BASE_DIR = os.path.dirname(__file__)

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
PROFILE_DIRS = ["Profile 2"]
REWARDS_URL = "https://rewards.bing.com/?form=edgepredeem"

QUERIES_FILE = os.path.join(BASE_DIR, "search_queries.txt")
LAST_RUN_FILE = os.path.join(BASE_DIR, "last_run.txt")
LOG_FILE = os.path.join(BASE_DIR, "search_log.txt")
