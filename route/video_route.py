from fastapi import APIRouter, status, File
from typing import List, Union
from services.videos import download_video, upload_video


route = APIRouter(
    tags=["Video"],
)


@route.post("/video_upload")
async def video_upload(*,file: bytes=File(),username:str, password:str, caption:str):
    return upload_video(username, password, file, caption)

@route.post("/video_download")
async def video_download(url:str):
    return download_video(username, password, url)