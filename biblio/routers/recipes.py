from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/recipes",
)

@router.get("/search")
async def read_items():
    return fake_items_db
