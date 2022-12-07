from fastapi import APIRouter, status, File
from typing import List, Union
from services.reels import upload_reels, download_reel


route = APIRouter(
    tags=["Reels"],
)


@route.post("/reels_upload")
async def reels_upload(*,file: bytes=File(),username:str, password:str, caption:str):
    return upload_reels(username, password, file, caption)

@route.get("/download_reel")
async def reel_download(url:str):
    return download_reel(url)