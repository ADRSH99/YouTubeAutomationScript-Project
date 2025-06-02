from pytubefix import Playlist, YouTube
from pytubefix.cli import on_progress
import urllib.request
from regex_utils import extract_youtube_video_ids

# WORKS ONLY FOR MUSIC — IF OTHER VIDEOS ARE USED, IT MAY NOT GIVE THE NECESSARY VIDEO RESULT/DOWNLOAD

# Run through terminal
# The loading bar for the playlist downloading lags behind a little bit.
# Make sure the folder link is correct before downloading.

print("Python Automation Project built by Adarsh Bellamane.")
print("This script downloads the song you like or a playlist.")

# For bypassing automation blockers from YouTube,
# we make it look like the request is coming from an actual web browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'www.google.com'
}

# Set your preferred folder path here
DOWNLOAD_DIR = ''  # Example: '/Users/YourName/Downloads'

def download_single_videos():
    """Handles downloading individual songs by searching YouTube."""
    while True:
        # Prompt user for video search
        name = input("Copy and paste the name of the video, along with the artist you're looking for: ")
        name_with_audio = name + " audio"  # Improve relevance for music
        search_query = "https://www.youtube.com/results?search_query=" + name_with_audio.replace(" ", "+")

        # Send search request to YouTube
        request = urllib.request.Request(search_query, headers=HEADERS)
        with urllib.request.urlopen(request) as response:
            html_content = response.read().decode('utf-8')

        # Extract first video ID using custom regex utility
        video_ids = extract_youtube_video_ids(html_content)
        if not video_ids:
            print("No video found. Please try a different search.")
            continue

        # Build the final video URL
        video_url = "https://www.youtube.com/watch?v=" + video_ids[0]
        yt = YouTube(video_url, on_progress_callback=on_progress)
        stream = yt.streams.get_highest_resolution()

        print(f'Downloading >> {yt.title}')
        stream.download(DOWNLOAD_DIR)  # Change DOWNLOAD_DIR if needed

        # Ask user whether to continue
        if input("One more video? (yes/no): ").strip().lower() != "yes":
            break


def download_playlist():
    """Handles downloading all videos from a YouTube playlist."""
    while True:
        playlist_url = input("Enter the playlist link: ")
        playlist = Playlist(playlist_url)

        for video_url in playlist:
            yt = YouTube(video_url, on_progress_callback=on_progress)
            stream = yt.streams.get_highest_resolution()
            print(f'Downloading >> {yt.title}')
            stream.download(DOWNLOAD_DIR)  # Change DOWNLOAD_DIR if needed

        # Ask user whether to download another playlist
        if input("Again? (yes/no): ").strip().lower() != "yes":
            break


# Main logic — ask the user if they're downloading a playlist or a single video
user_choice = input("Do you have a playlist to download? (yes/no): ").strip().lower()
if user_choice == "yes":
    download_playlist()
else:
    download_single_videos()
