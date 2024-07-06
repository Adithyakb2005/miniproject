#music list

playlist={}
songlst=[]

while True:
    print("\n 1.add song \n 2.display song \n 3.update song \n 4.remove song \n 5.exit")
    ch=input("Enter the choice:")
    if ch=='1':
        song=input("Enter song name: ")
        artist=input("Enter the artist: ")
        playlist[song]={"artist":artist}
        songlst.append(song)
    elif ch == '2':
        if not playlist:
            print("Playlist is empty.")
        else:
            print("Playlist:")
            for song, details in playlist.items():
                print(f"Song: {song}, Artist: {details['artist']}")

    elif ch == '3':
        song_name = input("Enter the song name to update: ")
        song_artist=input("Enter song artist name:")
        if song_name in playlist:
            new_name = input("Enter the new name: ")
            new_artist=input("Enter new artist name:")
            playlist[new_name] = playlist.pop(song_name)
            playlist[new_artist]=playlist.pop(song_artist)
            index = songlst.index(song_name)
            index=songlst.index(song_artist)
            songlst[index] = new_name
            songlst[index]=new_artist
            print("Song updated successfully!")
        else:
            print("Song not found!")

    elif ch == '4':
        song_name = input("Enter the song name to remove: ")
        if song_name in playlist:
            songlst.remove(song_name)
            del playlist[song_name]
            print("Song removed successfully!")
        else:
            print("Song not found!")

    elif ch=='5':
        print("exiting.....")
        break