from fastapi import FastAPI
from routes.user_routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "FastAPI Running"}

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)