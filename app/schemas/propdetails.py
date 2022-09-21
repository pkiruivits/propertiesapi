from typing import List, Optional
from datetime import datetime, date
from pydantic import BaseModel

class imageBase(BaseModel):
    property_id:int
    image_url:str

class imageCreate(imageBase):
    pass

class image(imageBase):
    id:int
    class Config:
        orm_mode = True
class propdetailsBase(BaseModel):
    name: str
    description: str
    specification: str
    architects: str=""
    area: int=0
    year: int=0
    manufacturers: str=""
    
    #class Config:
     #   arbitrary_types_allowed = True

class propdetailsCreate(propdetailsBase):
    pass

class propdetails(propdetailsBase):
    id: int
    images:List[image]=None

    class Config:
        orm_mode = True
