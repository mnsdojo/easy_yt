import os
from .exceptions import DirectoryCreationError


def create_directory_if_not_exists(directory):
    """Create a directory if it does not exist."""
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        raise DirectoryCreationError(f"Could not create the directory: {directory}")


def get_default_ydl_options(format='best', download_playlist=False, download_dir='downloads'):
    """Return default options for yt-dlp."""
    create_directory_if_not_exists(download_dir)
    return {
        'format': format,
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'noplaylist': not download_playlist,

    }
