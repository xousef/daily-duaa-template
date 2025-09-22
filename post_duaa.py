import tweepy
from datetime import datetime
import os

# --- API credentials from GitHub Secrets ---
api_key = os.environ["API_KEY"]
api_secret = os.environ["API_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# --- Tweepy client (v2) ---
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# --- Load duas from file ---
with open("duas.txt", "r", encoding="utf-8") as f:
    ad3eya = [line.strip() for line in f if line.strip()]

# --- File to track last index + date ---
index_file = "last_index.txt"
today = datetime.now().strftime("%Y-%m-%d")

# Defaults
last_index = -1
last_date = None

# Ensure the index file exists
if not os.path.exists(index_file):
    with open(index_file, "w", encoding="utf-8") as f:
        f.write("-1,1970-01-01")  # initial values

# Load progress
with open(index_file, "r", encoding="utf-8") as f:
    content = f.read().strip().split(",")
    if len(content) == 2:
        last_index = int(content[0])
        last_date = content[1]

# Skip if already tweeted today
if last_date == today:
    print("⏸️ Already tweeted today. Index:", last_index)
    exit()

# Get next dua
next_index = last_index + 1

# Wrap around if all duas are tweeted
if next_index >= len(ad3eya):
    next_index = 0  # start from beginning

duaa = ad3eya[next_index]

# Save progress
with open(index_file, "w", encoding="utf-8") as f:
    f.write(f"{next_index},{today}")

print(f"💾 Progress saved: Index {next_index} on {today}")

# --- Format tweet ---
tweet = f"""
َ
َ
          {duaa}
َ
"""

# --- Post the dua ---
response = client.create_tweet(text=tweet)
print(f"✅ Tweet posted! Tweet ID: {response.data['id']} | Index: {next_index}")