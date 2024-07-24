from easy_yt import YTDLWrapper


def download_video(url):
    ytdl = YTDLWrapper()

    # Download the video
    try:
        ytdl.download(url)
        print(f"Downloaded video from {url}")
    except Exception as e:
        print(f"Error downloading video: {e}")


def get_video_info(url):
    ytdl = YTDLWrapper()

    # Get video information
    try:
        info = ytdl.get_video_info(url)
        print("Video Title:", info.get('title', 'N/A'))
        print("Video Duration:", info.get('duration', 'N/A'), "seconds")
        print("Video Description:", info.get('description', 'N/A'))
    except Exception as e:
        print(f"Error retrieving video info: {e}")


if __name__ == "__main__":
    video_url = ""  # Replace with a valid YouTube video URL

    # Download the video
    download_video(video_url)

    # Get video information
    get_video_info(video_url)
