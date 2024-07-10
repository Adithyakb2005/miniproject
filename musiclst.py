users = {}
user_playlists = {}
current_user = None
while True:
    if not current_user:
        print("\n 1. Register \n 2. Login \n 3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            if username in users:
                print("Username already exists. Please choose another username.")
                continue

            password = input("Enter password: ")
            users[username] = password
            user_playlists[username] = {'playlist': {}, 'songlst': []}
            print("Registration successful!")

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username in users and users[username] == password:
                print(f"Login successful, welcome {username}!")
                current_user = username
            else:
                print("Invalid username or password.")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
    
    else:
        print(f"\nLogged in as {current_user}")
        print("Playlist Menu: \n 1. Add song \n 2. Display songs \n 3. Update song \n 4. Remove song \n 5. Clear playlist \n 6. Logout \n 7. Exit")

        ch = input("Enter your choice: ")

        if ch == '1':
            song = input("Enter song name: ")
            artist = input("Enter artist: ")
            user_playlists[current_user]['playlist'][song] = {"artist": artist}
            user_playlists[current_user]['songlst'].append(song)
            print("Song added successfully!")

        elif ch == '2':
            if not user_playlists[current_user]['playlist']:
                print("Playlist is empty.")
            else:
                print("Playlist:")
                for song, details in user_playlists[current_user]['playlist'].items():
                     print(f"Song: {song}, Artist: {details['artist']}")

        elif ch == '3':
            song_name = input("Enter the song name to update: ")
            if song_name in user_playlists[current_user]['playlist']:
                new_name = input("Enter the new name: ")
                user_playlists[current_user]['playlist'][new_name] = user_playlists[current_user]['playlist'].pop(song_name)
                index = user_playlists[current_user]['songlst'].index(song_name)
                user_playlists[current_user]['songlst'][index] = new_name
                print("Song updated successfully!")
            else:
                print("Song not found!")

        elif ch == '4':
            song_name = input("Enter the song name to remove: ")
            if song_name in user_playlists[current_user]['playlist']:
                user_playlists[current_user]['songlst'].remove(song_name)
                del user_playlists[current_user]['playlist'][song_name]
                print("Song removed successfully!")
            else:
                print("Song not found!")

        elif ch == '5':
            confirm = input("Are you sure you want to clear the entire playlist? (yes/no): ")
            if confirm.lower() == 'yes':
                user_playlists[current_user]['playlist'].clear()
                user_playlists[current_user]['songlst'].clear()
                print("Playlist cleared.")
            else:
                print("Clear operation cancelled.")

        elif ch == '6':
            print("Logging out...")
            current_user = None

        elif ch == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")