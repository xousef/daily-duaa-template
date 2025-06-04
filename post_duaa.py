import tweepy
import random
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

# Pick a random dua
duaa = random.choice(ad3eya)

# Add today's date
today = datetime.now().strftime("%Y-%m-%d")
tweet = f"{duaa}\n\nلـ{today}"

# Post the dua using API v2
response = client.create_tweet(text=tweet)

print(f"✅ تم نشر الدعاء! Tweet ID: {response.data['id']}")
