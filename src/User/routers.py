from fastapi import APIRouter, Depends, HTTPException

from database import get_async_session
from models import User,Event
from User.schemas import CreateUserSchema

from sqlalchemy import insert,select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload


router = APIRouter(
    prefix="/user",
    tags=["User_Operation"]
)

@router.post("/register")
async def register_user(new_user:CreateUserSchema, session: AsyncSession = Depends(get_async_session)):
    query = select(User).where(User.email == new_user.email)
    res = (await session.execute(query)).scalar_one_or_none()
    if res != None:
            return {"status" : "error",
                    "detail" : "such a user already exists"}
    stmt = insert(User).values(**new_user.dict())
    try:
        await session.scalar(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception:
         raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })
    

@router.get("/select")
async def select_user(email:str , session: AsyncSession = Depends(get_async_session)):
    query = select(User).where(User.email == email)
    try:
        res = (await session.execute(query)).scalar_one_or_none()
        return {
                "status": "success",
                "data": res,
                "details": None
            }
    except Exception:
         raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.get("/auth")
async def auth_user(email: str, password: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(User).where(User.email == email and User.password == password) 
        res = (await session.execute(query)).scalar_one_or_none()
        if res == None:
            return {"status": "error",
                    "details": "password or email not found"}
        return {"status": "succes",
                "details": None}
    except Exception:
         raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.post("/connectevent")
async def con_event(uniq_code: str,user_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        get_event = select(Event).options(selectinload(Event.paticipants)).filter_by(uniq_code = uniq_code)
        get_user = select(User).options(selectinload(User.events)).filter_by(id = user_id)
        res_event = (await session.execute(get_event)).scalar_one()
        res_user = (await session.execute(get_user)).scalar_one()
        res_user.events.append(res_event)
        await session.commit()
        return {"status" : "succes"}
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })