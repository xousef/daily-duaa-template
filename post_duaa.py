import tweepy
import random
from datetime import datetime
import os

# --- Step 1: Auth ---
api_key = os.environ["API_KEY"]
api_secret = os.environ["API_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# v1.1 Auth for trends
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api_v1 = tweepy.API(auth)

# v2 Auth for tweeting
client_v2 = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# --- Step 2: Read duas ---
with open("duas.txt", "r", encoding="utf-8") as f:
    ad3eya = [line.strip() for line in f if line.strip()]

duaa = random.choice(ad3eya)
today = datetime.now().strftime("%Y-%m-%d")

# --- Step 3: Get Saudi trending hashtags ---
try:
    woeid_saudi = 23424938
    trends = api_v1.get_place_trends(id=woeid_saudi)
    hashtags = [
        trend["name"] for trend in trends[0]["trends"]
        if trend["name"].startswith("#")
    ][:3]  # Limit to 3
except Exception as e:
    print("⚠️ Could not fetch trending hashtags:", e)
    hashtags = []

# --- Step 4: Create and post tweet ---
tweet = f"{duaa}\n\nليلة {today}\n{' '.join(hashtags)}"

try:
    response = client_v2.create_tweet(text=tweet)
    print(f"✅ Tweet posted: https://x.com/user/status/{response.data['id']}")
except Exception as e:
    print("❌ Error posting tweet:", e)
