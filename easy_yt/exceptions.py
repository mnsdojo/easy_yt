class YTDLWrapperError(Exception):
    """Base class for exceptions in the YTDLWrapper module."""

    def __init__(self, message="An error occurred in the YTDLWrapper module"):
        self.message = message
        super().__init__(self.message)


class DownloadError(YTDLWrapperError):
    """Exception raised for errors during video or audio download."""

    def __init__(self, url=None, message="An error occurred during the download"):
        self.url = url
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. URL: {self.url}" if self.url else self.message


class InvalidURLException(YTDLWrapperError):
    """Exception raised for invalid URL errors."""

    def __init__(self, url=None, message="The provided URL is invalid"):
        self.url = url
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. URL: {self.url}" if self.url else self.message


class DirectoryCreationError(YTDLWrapperError):
    """Exception raised for errors during directory creation."""

    def __init__(self, directory=None, message="An error occurred while creating the download directory"):
        self.directory = directory
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Directory: {self.directory}" if self.directory else self.message
