from fastapi import APIRouter, status, File
from typing import List, Union
from services.pictures import download_pictures, download_album


route = APIRouter(
    tags=["Photo / Pictures"],
)


@route.get("/picture_download")
async def video_download(url:str):
    return download_pictures(url)

@route.get("/album_download")
async def album_download(url:str):
    return download_album(url)