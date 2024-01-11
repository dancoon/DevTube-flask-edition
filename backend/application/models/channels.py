class Video:
    """ "Video object for storing video-related details"""

    def __init__(self, *args, **kwargs):
        self.video_id = kwargs.get("video_id", "")
        self.video_title = kwargs.get("video_title", "")
        self.video_description = kwargs.get("video_description", "")
        self.thumbnail_url = kwargs.get("thumbnail_url", "")
        self.published_at = kwargs.get("published_at", "")
        self.tags = kwargs.get("tags", [])
        self.duration = kwargs.get("duration", 0)
        self.view_count = kwargs.get("view_count", 0)
        self.like_count = kwargs.get("like_count", 0)
        self.dislike_count = kwargs.get("dislike_count", 0)
        self.comment_count = kwargs.get("comment_count", 0)
        self.favorite_count = kwargs.get("favorite_count", 0)

    def add_tags(self, tags):
        """Add a list of tags to video"""
        self.tags.extend(tags)

    def to_dict(self):
        """Convert object to dictionary"""
        return {
            "video_id": self.video_id,
            "video_title": self.video_title,
            "video_description": self.video_description,
            "thumbnail_url": self.thumbnail_url,
            "published_at": self.published_at,
            "tags": self.tags,
            "duration": self.duration,
            "view_count": self.view_count,
            "like_count": self.like_count,
            "dislike_count": self.dislike_count,
            "comment_count": self.comment_count,
            "favorite_count": self.favorite_count,
        }


class Playlist:
    """UploadPlaylist object for storing upload playlist-related details"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
            if kwargs.get("videos", None):
                self.videos = [Video(**video) for video in kwargs["videos"]]

        self.playlist_id = kwargs.get("playlist_id", "")
        self.playlist_title = kwargs.get("playlist_title", "")
        self.playlist_description = kwargs.get("playlist_description", "")
        self.thumbnail_url = kwargs.get("thumbnail_url", "")
        self.published_at = kwargs.get("published_at", "")
        self.videos = kwargs.get("videos", [])

    def add_videos(self, videos):
        """Add a list of video objects to playlist"""
        self.videos.extend(videos)

    def to_dict(self):
        """Convert object to dictionary"""
        return {
            "playlist_id": self.playlist_id,
            "playlist_title": self.playlist_title,
            "playlist_description": self.playlist_description,
            "thumbnail_url": self.thumbnail_url,
            "published_at": self.published_at,
            "videos": [video.to_dict() for video in self.videos],
        }


class Channel:
    """Channel object for storing channel-related details"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
            if kwargs.get("upload_playlist", None):
                self.upload_playlist = Playlist(**kwargs["upload_playlist"])
            if kwargs.get("playlists", None):
                self.playlists = [
                    Playlist(**playlist) for playlist in kwargs["playlists"]
                ]

        self.channel_id = ""
        self.channel_title = ""
        self.channel_description = ""
        self.thumbnail_url = ""
        self.upload_playlist = Playlist()
        self.playlists = []

    def add_playlists(self, playlists):
        """Add a list of playlist objects to channel"""
        self.playlists.extend(playlists)

    def to_dict(self):
        """Convert object to dictionary"""
        return {
            "channel_id": self.channel_id,
            "channel_title": self.channel_title,
            "channel_description": self.channel_description,
            "thumbnail_url": self.thumbnail_url,
            "upload_playlist": self.upload_playlist.to_dict(),
            "playlists": [playlist.to_dict() for playlist in self.playlists],
        }

    def get_all_videos(self):
        """Get all videos from channel"""
        videos = []
        videos.extend(self.upload_playlist.videos)
        return videos
