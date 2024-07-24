import os
import yt_dlp
from .exceptions import DownloadError
from .utils import get_default_ydl_options, create_directory_if_not_exists


class YTDLWrapper:
    """A wrapper for yt-dlp to simplify video and audio downloading from various sources."""

    def __init__(self, default_download_dir='downloads'):
        """
        Initialize the YTDLWrapper.

        Args:
            default_download_dir (str): The default directory where downloads will be saved.
        """
        self.default_download_dir = default_download_dir
        create_directory_if_not_exists(self.default_download_dir)

    def download(self, url, is_playlist=False, download_dir=None):
        """
        Download a video or a playlist based on the is_playlist flag.

        Args:
            url (str): The URL of the video or playlist to download.
            is_playlist (bool): Flag indicating if the URL is a playlist.
            download_dir (str, optional): The directory to save the downloaded file. Defaults to the default download directory.

        Returns:
            dict: Information about the downloaded video or playlist.

        Raises:
            DownloadError: If an error occurs during the download process.
        """
        download_dir = download_dir or self.default_download_dir
        ydl_opts = get_default_ydl_options(download_playlist=is_playlist, download_dir=download_dir)
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
            return info_dict
        except Exception as e:
            raise DownloadError(f"An error occurred during the download: {str(e)}")

    def get_video_info(self, url):
        """
        Retrieve information about a video without downloading it.

        Args:
            url (str): The URL of the video.

        Returns:
            dict: Information about the video.

        Raises:
            DownloadError: If an error occurs while retrieving video information.
        """
        ydl_opts = get_default_ydl_options(download_playlist=False, download_dir=self.default_download_dir)
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
            return info_dict
        except Exception as e:
            raise DownloadError(f"An error occurred while retrieving video info: {str(e)}")

    def download_audio(self, url, download_dir=None):
        """
        Download the audio of a video.

        Args:
            url (str): The URL of the video.
            download_dir (str, optional): The directory to save the downloaded audio file. Defaults to the default download directory.

        Returns:
            dict: Information about the downloaded audio.

        Raises:
            DownloadError: If an error occurs during the audio download process.
        """
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(download_dir or self.default_download_dir, '%(title)s.%(ext)s'),
            'noplaylist': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
            return info_dict
        except Exception as e:
            raise DownloadError(f"An error occurred during the audio download: {str(e)}")

    def download_video_simple(self, url, download_dir=None):
        """
        Convenience method to download a video with default options.

        Args:
            url (str): The URL of the video.
            download_dir (str, optional): The directory to save the downloaded video file. Defaults to the default download directory.

        Returns:
            dict: Information about the downloaded video.
        """
        return self.download(url, is_playlist=False, download_dir=download_dir)

    def download_audio_simple(self, url, download_dir=None):
        """
        Convenience method to download audio with default options.

        Args:
            url (str): The URL of the video.
            download_dir (str, optional): The directory to save the downloaded audio file. Defaults to the default download directory.

        Returns:
            dict: Information about the downloaded audio.
        """
        return self.download_audio(url, download_dir=download_dir)

    def download_playlist(self, url, download_dir=None):
        """
        Convenience method to download an entire playlist.

        Args:
            url (str): The URL of the playlist.
            download_dir (str, optional): The directory to save the downloaded files. Defaults to the default download directory.

        Returns:
            dict: Information about the downloaded playlist.
        """
        return self.download(url, is_playlist=True, download_dir=download_dir)
