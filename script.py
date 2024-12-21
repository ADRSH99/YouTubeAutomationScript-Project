from pytubefix import Playlist
from pytubefix import YouTube
from pytubefix.cli import on_progress
import urllib.request
import re

#WORKS ONLY FOR MUSIC, IF OTHER VIDS ARE USED. IT MAY NOT GIVE THE 
#NECESSARY VIDEO RESULT/DOWNLOAD

#run through terminal
#the loading bar for the playlist downloading lags behind a little bit.
#make sure the folder link is correct

print("Python Automation Project built by Adarsh Bellamane.")
print("This script downloads the Song you like or a playlist.")

audiostring="audio"

#for bypassing the automation blockers from youtube, we make it look like 
#the request is coming from a actual web browser

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'www.google.com'
}


type=input("Do you have a playlist to download?(yes/no)")
if type=="yes":
    condition1=False
    condition2=True
elif type=="no":
    condition1=True
    condition2=False


while condition1==True:
    searchquery="https://www.youtube.com/results?search_query=" #the link structure for any search query
    videolink="https://www.youtube.com/watch?v=" #the link structure for any video on yt
    name = input("Copy and paste the name of the video, along with the artist you're looking for: ")
    name_with_audio = name + " audio"
    searchquery += name_with_audio
    searchquery = searchquery.replace(" ", "+")
    req=urllib.request.Request(searchquery, headers=headers)
    html=urllib.request.urlopen(req)
    html_content = html.read()  # This should be in bytes
    html_string = html_content.decode('utf-8')
    video_ids = re.findall(r"/watch\?v=(\S{11})", html_string)
    videolink+=(video_ids[0])
    yt=YouTube(videolink, on_progress_callback=on_progress)
    yd=yt.streams.get_highest_resolution()
    print(f'Downloading >> {yt.title}')
    yd.download('') #put folder address here for ex: /Users/Lenovo/Downloads
    answer=input("One more video?(yes/no)")
    if answer=="yes": condition1=True
    elif answer=="no": condition1=False
    
while condition2==True:
    playlistlink=input("Enter the playlsit link")
    playlist=Playlist(playlistlink)
    for videolink in playlist:
        yt=YouTube(videolink, on_progress_callback=on_progress)
        yd=yt.streams.get_highest_resolution()
        print(f'Downloading >> {yt.title}')
        yd.download('') #put folder address here for ex: /Users/Lenovo/Downloads
    answer=input("Again?(yes/no)")
    if answer=="yes": condition2=True
    elif answer=="no": condition2=False
    
 