import re


def extract_video_id(url: str) -> str:
    """extract the 11-character video ID from a youtube URL.

    supports formats:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/shorts/VIDEO_ID
    """

    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, url)

    if not match:
        raise ValueError(
            "could not extract a valid Youtube video ID from the provided URL."
        )

    return match.group(1)