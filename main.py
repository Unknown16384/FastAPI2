from to_send import to_send
from sellers import sellers
from fastapi import FastAPI
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

app = FastAPI()
@app.on_event('startup')
async def startup():
    redis = aioredis.from_url('redis://localhost', encoding='utf8', decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')
@app.get('/statistics')
def statistics(mail):
    to_send.delay(mail)

app.include_router(sellers, tags=['Sellers'], prefix='/sellers')