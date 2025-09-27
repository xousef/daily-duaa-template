import tweepy
from datetime import datetime
import os
import random

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

# --- Use date as random seed ---
today = datetime.now().strftime("%Y-%m-%d")
random.seed(today)  # same shuffle for the same day

# Shuffle and pick first dua
shuffled = ad3eya[:]
random.shuffle(shuffled)
duaa = shuffled[0]

# --- Format tweet ---
tweet = f"""
َ
َ
          {duaa}
َ
"""

# --- Post the dua ---
response = client.create_tweet(text=tweet)
print(f"✅ Tweet posted! Tweet ID: {response.data['id']} | Date: {today}")