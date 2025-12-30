#kütüphane patlak

import pytube

url = "https://youtu.be/ja_CkweTmyk?si=dfrGxyux-1ze70it"
path = ""

pytube.YouTube(url).streams.get_highest_resolution().download()