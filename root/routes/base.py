from fastapi import APIRouter
from .catdog_route import router as catdog_cls_router

router = APIRouter ()
router.include_router ( catdog_cls_router, prefix = "/catdog_classification" )

@router.get ("/")
def home () :
    return {"message": "Welcome to CatDog API"}
