# YouTubeAutomationScript-Project
Winter 2024 Project by Adarsh Bellamane.

This script can be used to download MP4 audio/music files of your favourite artist..
You can download video by video or even an entire playlist!

This project makes use of pytubefix module along with REGEX (re) and urllib.requests module.
The pytubefix module is used for the main downloading part of the process instead of pytube.

The regex (re) module is used to search through the HTML code for the phrases that have '/watch?v=' in them and store
them in a list.
The Playlist function of the pytubefix module also does the same. Then we individually download the videos using 
pytubfix module's download stream function.

The urllib.request module is required to make a valid request to the www.youtube.com webpage.
The headers are used for bypassing the automation blockers from youtube, we make it look like the request is coming from a actual web browser
