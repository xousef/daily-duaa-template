import tweepy
from datetime import datetime
import os

# Get API credentials from environment variables
api_key = os.environ["API_KEY"]
api_secret = os.environ["API_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# Create Tweepy client for API v2 with OAuth 1.0a user context
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Read duas from file
with open("duas.txt", "r", encoding="utf-8") as f:
    ad3eya = [line.strip() for line in f if line.strip()]

# File to track the last tweeted index
index_file = "last_index.txt"

# Load last index, start at -1 if file doesn't exist
if os.path.exists(index_file):
    with open(index_file, "r") as f:
        last_index = int(f.read().strip())
else:
    last_index = -1

# Get next dua by order
next_index = last_index + 1

# Stop if we already tweeted them all
if next_index >= len(ad3eya):
    print("🚫 كل الأدعية تم نشرها.")
    exit()

duaa = ad3eya[next_index]

# Save updated index
with open(index_file, "w") as f:
    f.write(str(next_index))

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
