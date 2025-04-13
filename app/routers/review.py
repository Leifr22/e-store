from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from typing import Annotated
from sqlalchemy import insert,select,update, delete
from slugify import slugify


from app.backend.db_depends import get_db
from app.models.user import User
from app.routers.auth import get_current_user
from app.models.review import Review
from app.routers.auth import get_current_user
from app.schemas import CreateProduct, ReviewOut, CreateReview
from app.models.categories import Category
from app.models.products import Product
router = APIRouter(prefix="/reviews", tags=["Reviews"])

@router.get('/', response_model=list[ReviewOut])
async def all_reviews(db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.scalars(select(Review).where(Review.is_active == True))
    reviews = result.all()
    return reviews
@router.get('/product/{product_id}')
async def products_reviews(product_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Review).where(Review.product_id == product_id, Review.is_active == True))
    reviews = result.scalars().all()
    return reviews
@router.post('/', response_model=ReviewOut)
async def add_reviews(
    db: Annotated[AsyncSession, Depends(get_db)],
    review: CreateReview,
    get_user: Annotated[dict, Depends(get_current_user)]
):

    if get_user.get('is_customer'):

        await db.execute(
            insert(Review).values(
                user_id=get_user['id'],
                product_id=review.product_id,
                comment=review.comment,
                grade=review.grade
            )
        )

        await db.commit()
        return {"message": "Review added successfully"}
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You need to be authorised to post reviews'
        )

@router.delete('/{review_id}')
async def delete_reviews(review_id: int,db: Annotated[AsyncSession, Depends(get_db)], get_user: Annotated[int, Depends(get_current_user)]):
    if get_user.get('is_admin'):
        review= await db.scalar(select(Review).where(Review.id==review_id))
        if review is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='No reviews found'
            )
        review.is_active = False
        await db.execute(delete(Review).where(Review.id == review_id))
        await db.commit()
        return {
            'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You have not enough permission for this action'
        )






