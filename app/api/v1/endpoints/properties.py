from ast import Str
from typing import List,Union
import json
from fastapi import Depends, APIRouter, HTTPException, Request, Response, Form,UploadFile,File
from fastapi.responses import PlainTextResponse
#from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession, session

from app.crud import propdetails as crud
from app.api.deps.db import get_db_session
from app.models import propdetails as propdetailsmodel
from app.schemas import propdetails as propdetailsschema

router = APIRouter()
#app = FastAPI()

@router.get("/readyinbounds/", tags=['ready inbounds'])
async def ready_inbounds(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db_session)):
    inbounds =await crud.get_ready_inbounds(db, limit=limit)
    return inbounds

@router.get("/properties/",response_model=List[propdetailsschema.propdetails], tags=['get properties'])
async def get_properties(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db_session)):
    properties =await crud.get_properties(db, limit=limit)
    return properties

@router.get("/images/", tags=['get images'])
async def get_images( db: AsyncSession = Depends(get_db_session)):
    images =await crud.get_images(db)
    return images
@router.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open("uploads/uploaded_" + file.filename, "wb") as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        
    return {"message": f"Successfuly uploaded {file.filename}"}

@router.post("/uploadfile/")
async def create_upload_file(name:str,description:str,specification:str,architects:str,area:int,year:int,manufacturers:str,files: List[UploadFile]= File(...),db: AsyncSession = Depends(get_db_session)):
    
    #json_object = json.loads(rbody)
    print('First entry',name,description,specification)
    try:
        property=propdetailsschema.propdetailsCreate(name=name,description=description,specification=specification,architects=architects,area=area,year=year,manufacturers=manufacturers)
        db_property=await crud.create_property(db=db,property=property)
        if db_property:
            print('second entry',db_property)
            for file in files:
                img_details=propdetailsschema.imageCreate(property_id=db_property.id,image_url=file.filename)
                db_image=await crud.create_Image(db=db,image=img_details)
                contents = file.file.read()
                with open("uploads/" + file.filename, "wb") as f:
                    f.write(contents)
        
    except Exception as ex:
        print('error found',ex)
    return {"filenames": [file.filename for file in files]}