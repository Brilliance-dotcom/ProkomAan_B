def make_album(artist, title, tracks=None):
    """Return a dictionary representing an album."""
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

album1 = make_album('tyler, the creator', 'chromakopia')
album2 = make_album('kendrick lamar', 'good kid, m.A.A.d city', tracks=12)
album3 = make_album('billie eilish', 'happier than ever')

print(album1)
print(album2)
print(album3)