from.scheduler import start_scheduler
from contextlib import asynccontextmanager
from fastapi import FastAPI

async def lifespan(app:FastAPI):
     start_scheduler()
     yield
api =FastAPI(lifespan=lifespan)

@api.get('/')

async def root():

    return{"message":"Data Fetching is done"}
