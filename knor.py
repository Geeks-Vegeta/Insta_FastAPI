from instagrapi import Client


cl = Client()
# cl.login("getcomicsx", "Hentaimanga4321")
ww=cl.media_pk_from_url("https://www.instagram.com/reel/ChhsGIMjIJC/?utm_source=ig_web_copy_link")
# xx=cl.photo_download(ww) //pic download without uname, password
# xx=cl.video_download(ww) 
# pk = cl.story_pk_from_url("https://www.instagram.com/stories/missamberfields/2987568729286260276/")
# s = cl.story_info(pk)
# we=cl.story_download_by_url(s.video_url)
# xx=cl.story_download(pk)
# we=cl.album_download(ww) #album download
# we=igtv_download() # igtv download
we=cl.clip_download(ww)	 # reel donwload
print(we)