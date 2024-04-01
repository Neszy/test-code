from fastapi import FastAPI , Path
from starlette.responses import FileResponse
from app.router.item_routes import router as item_router
import os

app = FastAPI()

@app.get("/images/{owner_id}/jobapplicants/{user_id}/{filename}")

async def get_image(owner_id: str = Path(..., description="Owner ID"),
                     user_id: str = Path(..., description="User ID"),
                     filename: str = Path(..., description="Filename")):
    base_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    image_folder = os.path.join(base_folder, "backend","app","images", owner_id, "jobapplicants", user_id)
    image_path = os.path.join(image_folder, filename)
    
    if os.path.exists(image_path):
        return FileResponse(image_path)
    else:
        return {"error": f"File {filename} not found in {image_folder}"}
app.include_router(item_router)
