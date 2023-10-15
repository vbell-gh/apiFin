from fastapi import APIRouter
from crud import c_parties
router = APIRouter()

@router.get("/c_parties")