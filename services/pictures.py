from instagrapi import Client



# To upload video
def upload_video(username, password, path_data, caption):

    try: 
        rand_number = random.randint(1, 1023)

        file_name = "dance{0}.jpg".format(rand_number)
        with open(file_name, "wb") as f:
            f.write(path_data)

        cl = Client()
        cl.login(username, password)
        cl.clip_upload(file_name, caption=caption)
        return {"message":"video uploaded"}

    except Exception as e:
      print(e)

def download_pictures(url:str):

    try:
        cl = Client()

        media_pk = cl.media_pk_from_url(url)
        media_path = cl.photo_download(media_pk)
        return {"message":"photo downloaded"}

    except:
      print('An exception occurred')

    

def download_album(url:str):
    try:
        cl = Client()

        media_pk = cl.media_pk_from_url(url)
        media_path = cl.album_download(media_pk)
        return {"message":"photo downloaded"}

    except:
      print('An exception occurred')

