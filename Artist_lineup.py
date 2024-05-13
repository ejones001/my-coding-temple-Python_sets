artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]

unique_artists = set()
duplicate_found = False

for artist in artist_names:
    if artist in unique_artists:
        duplicate_found = True
    else:
        unique_artists.add(artist)

if duplicate_found:
    print("Duplicate artists found: True")
else:
    print("Duplicate artists found: False")
