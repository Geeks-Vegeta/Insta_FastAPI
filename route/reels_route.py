from fastapi import APIRouter, status, File
from typing import List, Union
from route.reels_route import *


route = APIRouter(
    tags=["Reels"],
)


@route.post("/reels_upload")
async def reels_upload(*,file: bytes=File(),username:str, password:str, caption:str):
    return upload_reels(username, password, file, caption)