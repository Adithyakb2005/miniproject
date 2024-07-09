playlist = {}
songlst = []

while True:
    print("\n 1. Add song \n 2. Display songs \n 3. Update song \n 4. Remove song \n"
          "\n 5. Clear playlist \n 6. Exit ")
    
    ch = input("Enter your choice: ")

    if ch == '1':
        song = input("Enter song name: ")
        artist = input("Enter artist: ")
        playlist[song] = {"artist": artist}
        songlst.append(song)
        print("Song added successfully!")

    elif ch == '2':
        if not playlist:
            print("Playlist is empty.")
        else:
            print("Playlist:")
            for song, details in playlist.items():
                print(f"Song: {song}, Artist: {details['artist']}")

    elif ch == '3':
        song_name = input("Enter the song name to update: ")
        if song_name in playlist:
            new_name = input("Enter the new name: ")
            playlist[new_name] = playlist.pop(song_name)
            index = songlst.index(song_name)
            songlst[index] = new_name
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

    
    elif ch == '5':
        confirm = input("Are you sure you want to clear the entire playlist? (yes/no): ")
        if confirm.lower() == 'yes':
            playlist.clear()
            songlst.clear()
            print("Playlist cleared.")
        else:
            print("Clear operation cancelled.")
    elif ch == '6':
        print("Exiting...")
    break
    
   