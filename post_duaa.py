import tweepy
import random
from datetime import datetime
import os

# Get API credentials from GitHub secrets (environment variables)
api_key = os.environ["API_KEY"]
api_secret = os.environ["API_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# Connect to X (Twitter) API
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Read duas from file
with open("duas.txt", "r", encoding="utf-8") as f:
    ad3eya = [line.strip() for line in f if line.strip()]

# Pick a random dua
duaa = random.choice(ad3eya)

# Add today's date
today = datetime.now().strftime("%Y-%m-%d")
tweet = f"{duaa}\n\nليلة {today}"

# Post the dua
api.update_status(tweet)
print("✅ تم نشر الدعاء!")
