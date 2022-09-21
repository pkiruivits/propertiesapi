from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from sqlalchemy.orm import Session,selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import propdetails as propmodels #models
from app.schemas import propdetails as propschema #models
from sqlalchemy import select, update
from fastapi.encoders import jsonable_encoder
import http.client
import json
#from . import models, schemas

async def get_properties(db: AsyncSession, skip: int = 0, limit: int = 100)-> List[propmodels.propdetail]:
        result = await db.execute(
            select(propmodels.propdetail)
            .order_by(propmodels.propdetail.id)
            .options(selectinload(propmodels.propdetail.images))
            .offset(skip)
            .limit(limit)
        )
        await db.commit()
        return result.scalars().all()

async def get_propimages(db: AsyncSession, prop_id: int)-> List[propmodels.Images]:
    result = await db.execute(
        select(propmodels.Images)
        .filter(propmodels.Images.property_id==prop_id)
        )
    await db.commit()
    return result.scalars().all()
async def get_images(db: AsyncSession)-> List[propmodels.Images]:
    result = await db.execute(
        select(propmodels.Images)
        
        )
    await db.commit()
    return result.scalars().all()

async def get_property_by_id(db: AsyncSession, prop_id: str):
    result = await db.execute(
            select(propmodels.propdetail)
            .filter(propmodels.propdetail.id==prop_id)
             )
    await db.commit()
    return result.scalars().one_or_none()
    
async def create_property(db: Session, property: propschema.propdetailsCreate,commit=True):
    print('called create')
    obj_in_data = jsonable_encoder(property, exclude_unset=True)
    db_property = propmodels.propdetail(**obj_in_data)
    db.add(db_property)
    if commit:
        await db.commit()
    else:
        await db.flush()
    
    return db_property

async def create_Image(db: Session, image: propschema.imageCreate,commit=True):

    obj_in_data = jsonable_encoder(image, exclude_unset=True)
    db_image = propmodels.Images(**obj_in_data)
    db.add(db_image)
    if commit:
        await db.commit()
    else:
        await db.flush()
    
    return db_image 


async def sentsms(tokenstr:str,phone:str,message:str,prevsmsid:str):
    payload=""
    return payload 
async def sentsmsinteractive(tokenstr:str,phone:str,message:str,prevsmsid:str,db:AsyncSession):
    payload1=""
   
    return payload1

  
