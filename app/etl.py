import os
import httpx
from dotenv import load_dotenv
from .db import db

load_dotenv()
API_KEY=os.getenv("OPENWEATHER_API_KEY")
city ="chennai"


async def fetch_and_store_weather():
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        # Keep it simple for now
        await db.weather_data.insert_one(data)
        print("Weather data fetched & saved ✅")

