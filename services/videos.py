from instagrapi import Client


def download_video(url:str):

    try:
        cl = Client()
        cl.login(username, password)

        media_pk = cl.media_pk_from_url(url)
        media_path = cl.video_download(media_pk)
    except:
      print('An exception occurred')


# To upload video
def upload_video(username, password, path_data, caption):

    try: 
        rand_number = random.randint(1, 1023)

        file_name = "dance{0}.mp4".format(rand_number)
        with open(file_name, "wb") as f:
            f.write(path_data)

        cl = Client()
        cl.login(username, password)
        cl.video_upload(file_name, caption=caption)
        return {"message":"video uploaded"}

    except Exception as e:
      print(e)