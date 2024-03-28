from fastapi import FastAPI

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

from config import REDIS_HOST, REDIS_PORT

from User.routers import router as user_router
from Event.router import router as event_router
from message.router import router as message_router


app = FastAPI(
    title="Events Together App"
)

@app.get("/")
async def home():
    return {"data":"test project" }

app.include_router(user_router)
app.include_router(event_router)
app.include_router(message_router)

@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    