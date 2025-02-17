import redis
import os
import dotenv
# Use your Redis URL
dotenv.load_dotenv(r"API.env")
REDIS_URL = os.getenv("REDIS_URL")

try:
    redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)
    pong = redis_client.ping()
    if pong:
        print("✅ Redis is accessible!")
    else:
        print("❌ Redis connection failed!")
except Exception as e:
    print(f"❌ Error: {e}")
