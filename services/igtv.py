from instagrapi import Client


def download_igtv(url:str):

    try:
        cl = Client()

        media_pk = cl.media_pk_from_url(url)
        media_path = we=igtv_downloadmedia_pk()
        return {"message":"igtv downloaded"}

    except:
      print('An exception occurred')
