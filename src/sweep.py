import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID="your_client_id"
CLIENT_SECRET="your_client_secret"

PLAYLIST_ID="your_playlist_to_add_songs_tos_id"
DISOVER_WEEKLY_ID="discover_weekly_playlist_id"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://localhost:8080",
                                               scope="user-library-read, playlist-modify-public"))


spotify_playlist_prefix = 'spotify:playlist:'

discover_weekly_pid = spotify_playlist_prefix + DISOVER_WEEKLY_ID
playlist_add_id = spotify_playlist_prefix + PLAYLIST_ID
offset = 0

def addToPlaylist(trackIds): 
    if len(trackIds) > 0:
        sp.playlist_add_items(playlist_add_id, trackIds)
    
    

while True:
    disoverWeeklyResponse = sp.playlist_items(discover_weekly_pid,
                                 offset=offset,
                                 fields='items.track.id,total',
                                 additional_types=['track'])
                                 
    playlistTracksResponse = sp.playlist_items(playlist_add_id,
                                 offset=offset,
                                 fields='items.track.id,total',
                                 additional_types=['track'])

    savedTracksResponse = sp.current_user_saved_tracks()

    savedTracks = savedTracksResponse['items']
    disocoverWeeklyTracks = disoverWeeklyResponse['items']
    playlistTracks = playlistTracksResponse['items']

    savedTrackIds = []
    trackIdsToAdd = []
    playListTrackIds = []

    
    for i in playlistTracks:
        playListTrackIds.append(i['track']['id'])

    for i in savedTracks:
        savedTrackIds.append(i['track']['id'])
    
    for i in disocoverWeeklyTracks:
        id = i['track']['id']
        trackSaved = id in savedTrackIds
        trackAlreadyIn = id in playListTrackIds
        if trackSaved and not trackAlreadyIn:
            trackIdsToAdd.append(id)


    addToPlaylist(trackIdsToAdd)
    
    print('added ' + str(len(trackIdsToAdd)) + ' to the playlist')
    break;