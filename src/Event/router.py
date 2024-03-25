from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException

from database import get_async_session
from models import Event
from Event.schema import CreateEventSchema

from sqlalchemy import insert,select
from sqlalchemy.ext.asyncio import AsyncSession

import redis
router = APIRouter(
    prefix="/event",
    tags=["Event_Operation"]
)

@router.post("/addevent")
async def add_event(new_event:CreateEventSchema, session: AsyncSession = Depends(get_async_session)):
    if new_event.start_at < datetime.now():
        return {"status": "error",
                "detail": "incorrect time"} 
    query = select(Event).where(Event.uniq_code == new_event.uniq_code)
    res = (await session.execute(query)).scalar_one_or_none() 
    if res != None:
        return  {"status": "error",
                "detail": "incorrect uniq_code"} 
    try:
        query = insert(Event).values(**new_event.dict())
        await session.execute(query)
        await session.commit()
        query = select(Event.id).where(Event.uniq_code == new_event.uniq_code)
        res = (await session.execute(query)).scalar_one_or_none()
        rd = redis.Redis()
        rd.lpush(res,f"{new_event.start_at}")
        return {"status": "success"}
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })
    

@router.post("/datetime")
async def date_time(uniq_code: str,date_time: datetime,session: AsyncSession = Depends(get_async_session)):
    if date_time < datetime.now():
        return{"status": "error",
                "data": "incorrect time"} 
    try:
        query = select(Event.id).where(Event.uniq_code == uniq_code)
        res = (await session.execute(query)).scalar_one_or_none()
        if res == None:
            return{"status": "error",
                "detail": "event not found"}
        rd = redis.Redis()
        rd.rpush(f"{res}", f"{date_time}")
        return {"status": "succes"}
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })

@router.get("/optimaldatetime")
async def optimal_datetime(id_event: int):
    try:
        rd = redis.Redis()
        if not rd.exists(id_event):
            return {"status": "index not found"} 
        res_redis = rd.lrange(id_event, 0, -1)
        opttime = {}
        for optdt in res_redis:
            if optdt in opttime:
                opttime[optdt] += 1
            else:
                opttime[optdt] = 1
        opttime = dict(sorted(opttime.items(), key=lambda item: item[1]))
        return list(opttime.keys())[-1]
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })