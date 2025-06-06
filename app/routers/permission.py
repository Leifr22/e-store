from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, update
from starlette import status
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from app.backend.db_depends import get_db
from app.models.user import User
from .auth import get_current_user

router = APIRouter(prefix='/permission', tags=['permission'])

@router.patch('/')
async def supplier_permission(db: Annotated[AsyncSession, Depends(get_db)], get_user: Annotated[dict, Depends(get_current_user)], user_id: int):
    if get_user.get('is_admin'):
        user = await db.scalar(select(User).where(User.id == user_id))
        if not user or not user.is_active:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
        if user.is_supplier:
            await db.execute(update(User).where(User.id == user_id).values(is_customer=True, is_supplier=False))
            await db.commit()
            return {
                'status_code': status.HTTP_200_OK,
                'detail': 'User is no longer supplier'
            }
        else:
            await db.execute(update(User).where(User.id==user_id).values(is_customer=False, is_supplier=True))
            await db.commit()
            return {
                'status_code': status.HTTP_200_OK,
                'detail': 'User is now supplier'
            }
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='No admin rights'
        )
@router.get('/delete_user')
async def delete_user(db: Annotated[AsyncSession,Depends(get_db)], get_user: Annotated[dict,Depends(get_current_user)],user_id:int):
    if get_user.get('is_admin'):

         user=db.scalar(select(User).where(User.id==user_id))
         if not user:
             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
         if user.is_admin:
             raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You cannot delete admin user')
         if user.is_active:
             await db.execute(update(User).where(User.id==user_id)).values(is_active=False)
             await db.commit()
             return{
                 'status_code': status.HTTP_200_OK,
                 'detail': 'User is deleted'

             }

         else:
              return {
                'status_code': status.HTTP_200_OK,
                'detail': 'User has already been deleted'
            }
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='No admin rights'
        )


