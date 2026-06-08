import uvicorn
from fastapi import APIRouter, HTTPException
from models import User
from database import user_collection
from utils.logger import logger

router = APIRouter()

@router.post("/create-user")
def create_user(user: User):
    try:
        user_dict = user.dict()
        user_collection.insert_one(user_dict)

        logger.info("User created successfully")

        return {
            "message": "User created",
            "status_code": 201
        }

    except Exception as e:
        logger.error(f"Error creating user: {str(e)}")

        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )
if __name__ == "__main__":
    uvicorn.run(router, host="0.0.0.0", port=8001)