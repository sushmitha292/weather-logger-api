from apscheduler.schedulers.background import BackgroundScheduler
from  .etl import fetch_and_store_weather
import asyncio
def start_scheduler():
    scheduler=BackgroundScheduler()
    def run_fetch():
        asyncio.run(fetch_and_store_weather())
    scheduler.add_job(run_fetch,"interval", minutes=5)
    scheduler.start()


