users = {'admin':'admin123'}
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
    elif current_user == 'admin':
        print("\nLogged in as Admin")
        print("Admin Menu: \n 1. View all users \n 2. Delete a user \n 3. View a user's playlist \n 4. Add song to a user's playlist \n 5. Delete song from a user's playlist \n 6. Logout \n 7. Exit")
        admin_choice = input("Enter your choice: ")

        if admin_choice == '1':
            print("List of all users:")
            for user in users:
                if user != 'admin':  # Exclude admin from the list
                    print(user)

        elif admin_choice == '2':
            delete_user = input("Enter the username to delete: ")
            if delete_user in users and delete_user != 'admin':
                del users[delete_user]
                del user_playlists[delete_user]
                print(f"User '{delete_user}' deleted successfully.")
            else:
                print("User not found or cannot delete admin.")

        elif admin_choice == '3':
            username_to_view = input("Enter the username to view playlist: ")
            if username_to_view in user_playlists:
                if user_playlists[username_to_view]['playlist']:
                    print(f"Playlist for user '{username_to_view}':")
                    for song, details in user_playlists[username_to_view]['playlist'].items():
                        print(f"Song: {song}, Artist: {details['artist']}")
                else:
                    print("User's playlist is empty.")
            else:
                print("User not found.")

        elif admin_choice == '4':
            username_to_add = input("Enter the username to add song: ")
            if username_to_add in user_playlists:
                song = input("Enter song name: ")
                artist = input("Enter artist: ")
                user_playlists[username_to_add]['playlist'][song] = {"artist": artist}
                user_playlists[username_to_add]['songlst'].append(song)
                print(f"Song '{song}' added to '{username_to_add}' playlist successfully.")
            else:
                print("User not found.")

        elif admin_choice == '5':
            username_to_delete_from = input("Enter the username to delete song from: ")
            if username_to_delete_from in user_playlists:
                song_to_delete = input("Enter the song name to delete: ")
                if song_to_delete in user_playlists[username_to_delete_from]['playlist']:
                    user_playlists[username_to_delete_from]['songlst'].remove(song_to_delete)
                    del user_playlists[username_to_delete_from]['playlist'][song_to_delete]
                    print(f"Song '{song_to_delete}' deleted from '{username_to_delete_from}' playlist successfully.")
                else:
                    print("Song not found in user's playlist.")
            else:
                print("User not found.")

        elif admin_choice == '6':
            print("Logging out...")
            current_user = None

        elif admin_choice == '7':
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