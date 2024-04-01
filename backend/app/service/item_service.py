import os
import logging

def get_images(owner_id: str, user_id: str):
    try:
        images = []
        base_url = "http://localhost:8000"  # เปลี่ยนเป็น URL ของเว็บไซต์ของคุณ
        base_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image_folder = os.path.join(base_folder, "images", owner_id, "jobapplicants", user_id)
        for filename in os.listdir(image_folder):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image_path = os.path.join(image_folder, filename)
                image_url = f"{base_url}/images/{owner_id}/jobapplicants/{user_id}/{filename}"
                images.append(image_url)
        return images
    except FileNotFoundError as e:
        # ล็อกข้อผิดพลาด
        logging.error(f"Error: {e}")
        # ส่งกลับรายการรูปภาพเปล่าๆ
        return []
