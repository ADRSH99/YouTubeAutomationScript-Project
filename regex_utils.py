
def extract_youtube_video_ids(html_string):
    """
    Custom implementation to extract YouTube video IDs from HTML content.
    Looks for '/watch?v=' followed by exactly 11 non-whitespace characters.

    Parameters: html_string (str): HTML content of the YouTube search page.

    Returns a list[str]: A list of 11-character YouTube video IDs.
    """
    video_ids = []
    key = "/watch?v="
    idx = 0

    while idx < len(html_string):
        idx = html_string.find(key, idx)
        if idx == -1:
            break
        start = idx + len(key)
        potential_id = html_string[start:start+11]

        # Validate that it's 11 characters and doesn't include invalid terminators
        if len(potential_id) == 11 and not any(c in potential_id for c in ['"', '&', '\\', '<', '>', ' ']):
            video_ids.append(potential_id)

        idx = start  # continue search

    return list(dict.fromkeys(video_ids))  #remove duplicates 
