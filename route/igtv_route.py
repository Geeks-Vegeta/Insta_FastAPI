from fastapi import APIRouter, status, File
from typing import List, Union
from services.igtv import download_igtv


route = APIRouter(
    tags=["igtv"],
)


@route.get("/igtv_download")
async def video_download(url:str):
    return download_igtv(url)