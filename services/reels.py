from instagrapi import Client
import io
import random
import os



# To upload reels
def upload_reels(username, password, path_data, caption):

    try: 
        rand_number = random.randint(1, 1023)

        file_name = "dance{0}.mp4".format(rand_number)
        with open(file_name, "wb") as f:
            f.write(path_data)

        cl = Client()
        cl.login(username, password)
        cl.clip_upload(file_name, caption=caption)
        return {"message":"reels uploaded"}

    except Exception as e:
      print(e)
    


def download_reel(url:str):
    
    try:
      cl = Client()
      reel_pk=cl.media_pk_from_url(url)
      reel_path = cl.clip_download(reel_pk)	 
      return {"message":"reels download"}


    except Exception as e:
      print(e)