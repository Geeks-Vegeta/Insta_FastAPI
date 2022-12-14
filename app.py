from typing import Union
from fastapi import Depends, FastAPI, HTTPException, status
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from route import reels_route, video_route, picture_route, igtv_route


description = '''

This is an Instagram api which is associated with instagrapi, instaloader

'''

app = FastAPI(
    title="Insta API",
    description=description,
    version=0.1
)


origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Ok"}

app.include_router(reels_route.route)
app.include_router(video_route.route)
app.include_router(picture_route.route)
app.include_router(igtv_route.route)
# app.include_router(kingcomics_route.route)


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, port=3000)