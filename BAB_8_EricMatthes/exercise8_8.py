def make_album(artist, title, tracks=None):
    """Return a dictionary representing an album."""
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    print("\nEnter 'q' at any time to quit.")
    artist = input("Enter the artist's name: ")
    if artist.lower() == 'q':
        break
    title = input("Enter the album title: ")
    if title.lower() == 'q':
        break
    tracks_input = input("Enter the number of tracks (or leave blank): ")
    if tracks_input.lower() == 'q':
        break
    tracks = int(tracks_input) if tracks_input else None

    album = make_album(artist, title, tracks)
    print(f"\nAlbum details: {album}")