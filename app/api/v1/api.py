

from fastapi import APIRouter, Depends

from app.api.v1.endpoints import (
    users,webhooks,properties
    
)

router = APIRouter(prefix="/v1")

router.include_router(users.router, prefix="/users")
router.include_router(webhooks.router, prefix="/webhooks") 
router.include_router(properties.router, prefix="/properties")
# router.include_router(test.router, prefix="/test")