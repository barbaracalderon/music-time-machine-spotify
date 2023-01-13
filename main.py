from bot import Bot

bot = Bot()

answer = ''
bot.show_welcome_message()

while True:
    answer_playlist = input('Would you like to create a Spotify Playlist? [Y/N]: ').upper()[0]
    while answer_playlist not in ('Y', 'N'):
        print('This answer is not valid. Please type "N" for "No" or "Y" for "Yes".')
        answer_playlist = input('Would you like to create a Spotify Playlist? [Y/N]: ').upper()[0]
    if answer_playlist == 'N':
        bot.show_bye_message()
        break
    print("Great! Let's do this :)")
    answer_date = input('Please, type a date of your choice in the following format (YYYY-MM-DD): ')
    while '-' not in answer_date:
        print('This is not a valid date format.')
        answer_date = input('Please, type a date of your choice in the following format (YYYY-MM-DD): ')
    answer_date_split = answer_date.split('-')
    invalid_format = bot.is_date_format_invalid(answer_date_split)
    if invalid_format:
        print('Again. This is not a valid date format...')
        print("We're shutting down.")
    response = bot.send_request_to_billboard(answer_date)
    music_titles = bot.grab_music_titles(response)

print('Exiting...')