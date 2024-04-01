from fastapi import APIRouter, Request, HTTPException
from app.service.item_service import get_images
import json

router = APIRouter()

@router.post("/")  
async def read_images(request: Request):
    try:
        # รับข้อมูล request body และแปลงเป็น dictionary
        request_data = await request.body()
        data = json.loads(request_data)

        # เข้าถึงค่า owner_id และ user_id
        owner_id = data.get("owner_id")
        user_id = data.get("user_id")
        
        images = get_images(owner_id, user_id)
        return {"images": images}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Images not found")