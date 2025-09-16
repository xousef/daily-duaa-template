import tweepy
from datetime import datetime
import os

# Get API credentials from environment variables
api_key = os.environ["API_KEY"]
api_secret = os.environ["API_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# Create Tweepy client
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Read duas from file
with open("duas.txt", "r", encoding="utf-8") as f:
    ad3eya = [line.strip() for line in f if line.strip()]

# File to track last index + date
index_file = "last_index.txt"

today = datetime.now().strftime("%Y-%m-%d")

# Default values
last_index = -1
last_date = None

if os.path.exists(index_file):
    with open(index_file, "r") as f:
        content = f.read().strip().split(",")
        if len(content) == 2:
            last_index = int(content[0])
            last_date = content[1]

# Only move to next dua if date changed
if last_date == today:
    print("⏸️ Already tweeted today.")
    exit()

next_index = last_index + 1

# Stop if we already tweeted them all
if next_index >= len(ad3eya):
    print("🚫 كل الأدعية تم نشرها.")
    exit()

duaa = ad3eya[next_index]

# Save updated index and today’s date
with open(index_file, "w") as f:
    f.write(f"{next_index},{today}")

# Format tweet
tweet = f"""
َ


َ

          {duaa}

َ

"""

# Post the dua
response = client.create_tweet(text=tweet)
print(f"✅ تم نشر الدعاء! Tweet ID: {response.data['id']} | Index: {next_index}")