import tweepy
import random
from datetime import datetime
import os




# مفاتيح API من متغيرات البيئة
api_key = os.environ["O5HuuSperjzQ54O04BWABP6gA"]
api_secret = os.environ["aW1qW3EZhmoHQ75iR5kqvKlXRcTJ5wOkyoYlOcOyNk51iYM8A1"]
access_token = os.environ["131717037-aseMDUG1TN81pSud8dP9Kv7av39CxsLqEqOMAttW"]
access_token_secret = os.environ["EIKrc1HLzsnlAzWAkPugHZJRsPk7sHniEhfoqNQ2xki6C"]

# الاتصال بـ X API
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# قراءة الأدعية من الملف
with open("duas.txt", "r", encoding="utf-8") as f:
    ad3eya = [line.strip() for line in f if line.strip()]

# اختيار دعاء عشوائي
duaa = random.choice(ad3eya)

# إضافة التاريخ
today = datetime.now().strftime("%Y-%m-%d")
tweet = f"{duaa}\n\nليلة {today}"

# نشر الدعاء
api.update_status(tweet)
print("✅ تم نشر الدعاء!")
