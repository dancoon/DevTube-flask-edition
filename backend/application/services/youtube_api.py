import requests


class YoutubeAPI:
    API_KEY = "AIzaSyCuZrXqIuO0L2g_k3DvyMBTPvp9M7El030"

    def __init__(self):
        self.base_url = "https://www.googleapis.com/youtube/v3/"

    def fetch_channel_details(
        self, part="snippet,contentDetails", username=None, channel_id=None
    ):
        url, data = None, None
        if username is None and channel_id is None:
            raise Exception("Please specify either username or channel_id.")
        if username is not None and channel_id is not None:
            raise Exception("Please specify either username or channel_id, not both.")
        if username:
            url = f"{self.base_url}channels?part={part}&forUsername={username}&key={self.API_KEY}"
        if channel_id:
            url = f"{self.base_url}channels?part={part}&id={channel_id}&key={self.API_KEY}"

        try:
            response = requests.get(url)
            data = response.json()
        except Exception as e:
            print(e)
            return None
        return data

    def fetch_channel_playlist(self, channel_id=None, next_page_token=None):
        if channel_id is None:
            raise Exception("Please specify channel_id.")
        url = None
        if next_page_token is None:
            url = f"{self.base_url}playlists?part=snippet,contentDetails&channelId={channel_id}&key={self.API_KEY}"
        else:
            url = f"{self.base_url}playlists?part=snippet,contentDetails&channelId={channel_id}&pageToken={next_page_token}&key={self.API_KEY}"
        try:
            response = requests.get(url)
            data = response.json()
        except Exception as e:
            print(e)
            return None
        return data

    def fetch_playlist_items(self, playlist_id=None, next_page_token=None):
        if playlist_id is None:
            raise Exception("Please specify playlist_id.")
        url = None
        if next_page_token is None:
            url = f"{self.base_url}playlistItems?part=contentDetails&playlistId={playlist_id}&key={self.API_KEY}"
        else:
            url = f"{self.base_url}playlistItems?part=contentDetails&playlistId={playlist_id}&pageToken={next_page_token}&key={self.API_KEY}"
        try:
            response = requests.get(url)
            data = response.json()
        except Exception as e:
            print(e)
            return None
        return data


class YouTubeDataProcessor:
    def __init__(self):
        self.youtube_api = YoutubeAPI()
        self.channel_details = None

    def get_channel_details(self, username=None, channel_id=None):
        response = self.youtube_api.fetch_channel_details(
            username=username, channel_id=channel_id
        )
        if response:
            channel_id = response["items"][0]["id"]
            channel_title = response["items"][0]["snippet"]["title"]
            channel_description = response["items"][0]["snippet"]["description"]
            thumbnail_url = response["items"][0]["snippet"]["thumbnails"]["default"][
                "url"
            ]
            upload_playlist_id = response["items"][0]["contentDetails"][
                "relatedPlaylists"
            ]["uploads"]
            self.channel_details = {
                "channel_id": channel_id,
                "channel_title": channel_title,
                "channel_description": channel_description,
                "thumbnail_url": thumbnail_url,
                "upload_playlist_id": upload_playlist_id,
            }

    def get_channel_playlists(self, channel_id=None):
        """DONT USE THIS FUNCTION. USE get_channel_details() INSTEAD."""
        playlists = []
        next_page_token = None
        while True:
            data = self.youtube_api.fetch_channel_playlist(
                channel_id=channel_id, next_page_token=next_page_token
            )
            if data:
                playlists.extend(data["items"])
                if "nextPageToken" in data:
                    next_page_token = data["nextPageToken"]
                else:
                    break
            else:
                break
        return (playlists,)

    def get_playlist_items(self, playlist_id=None):
        playlist_items = []
        next_page_token = None
        while True:
            data = self.youtube_api.fetch_playlist_items(
                playlist_id=playlist_id, next_page_token=next_page_token
            )
            if data:
                playlist_items.extend(data["items"])
                if "nextPageToken" in data:
                    next_page_token = data["nextPageToken"]
                else:
                    break
            else:
                break
        return playlist_items

    def get_video_details(self, video_id=None):
        url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={YoutubeAPI.API_KEY}"
        try:
            response = requests.get(url)
            data = response.json()
        except Exception as e:
            print(e)
            return None
        return data

    def upload_channel_details(self):
        pass


# Example usage
api_key = "AIzaSyCuZrXqIuO0L2g_k3DvyMBTPvp9M7El030"
# Example usage
# username = "googledevelopers"
# channel_details = YoutubeAPI().fetch_channel_details(username=username)
# if channel_details:
#     channel_id, channel_title, channel_description = channel_details
#     print(f"Channel ID: {channel_id}")
#     print(f"Channel Title: {channel_title}")
#     print(f"Channel Description: {channel_description}")
# else:
#     print("Channel not found.")

# Example usage
channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"
# playlists = YoutubeAPI().get_channel_playlist(channel_id=channel_id)
# if playlists:
#     print(playlists)
# else:
#     print("No playlists found.")

# Example usage
playlist_id = "UU_x5XG1OV2P6uZZ5FSM9Ttw"
# playlist_items = YoutubeAPI().get_playlist_items(playlist_id=playlist_id)

# channel_details = YouTubeDataProcessor().get_channel_details(channel_id=channel_id)
# print(channel_details)

playlists = YouTubeDataProcessor().get_playlist_items(playlist_id=playlist_id)
print(playlists)
