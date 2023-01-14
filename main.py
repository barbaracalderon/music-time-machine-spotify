from bot import *


welcome_message()
answer = ""

while True:
    answer_playlist = input("Would you like to create a Spotify Playlist? [Y/N]: ").upper()[0]
    while answer_playlist not in ('Y', 'N'):
        print('\033[31mError. Invalid format.\033[m')
        answer_playlist = input("Would you like to create a Spotify Playlist? [Y/N]: ").upper()[0]
    if answer_playlist == 'N':
        bye_message()
        break
    print("Great! Let's do this :)")
    answer_date = input("Please, type a date of your choice in the following format (YYYY-MM-DD): ")
    while '-' not in answer_date:
        print('\033[31mError. Invalid format.\033[m')
        answer_date = input("Please, type a date of your choice in the following format (YYYY-MM-DD): ")
    answer_date_split = answer_date.split('-')
    invalid_format = is_date_format_invalid(answer_date_split)
    if invalid_format:
        print('''\033[31mAgain. This is not a valid date format...
                We're shutting down.\033[m''')
    print("Awesome! We're reaching the Billboard Charts for that date now...")
    response = send_request_to_billboard(answer_date)
    song_titles = grab_music_titles(response)
    if len(song_titles) == 0:
        raise Exception("Error. The list is empty. Please verify.")
    spotify_create_playlist(answer_date=answer_date, song_titles=song_titles)
    print("All done!\nBe sure to check your Spotify account. :)")

print('\033[31mExiting...\033[m')
