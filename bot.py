import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup

SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.environ.get('SPOTIPY_REDIRECT_URI')


def welcome_message():
    msg = '''\033[33m
        WELCOME TO

                   .___________. __    __   _______                                               
                   |           ||  |  |  | |   ____|                                              
         ______    `---|  |----`|  |__|  | |  |__                                                 
        |______|       |  |     |   __   | |   __|                                                
                       |  |     |  |  |  | |  |____                                               
                       |__|     |__|  |__| |_______|                                              

        .___  ___.  __    __       _______. __    ______    .___________. __  .___  ___.  _______ 
        |   \/   | |  |  |  |     /       ||  |  /      |   |           ||  | |   \/   | |   ____|
        |  \  /  | |  |  |  |    |   (----`|  | |  ,----'   `---|  |----`|  | |  \  /  | |  |__   
        |  |\/|  | |  |  |  |     \   \    |  | |  |            |  |     |  | |  |\/|  | |   __|  
        |  |  |  | |  `--'  | .----)   |   |  | |  `----.       |  |     |  | |  |  |  | |  |____ 
        |__|  |__|  \______/  |_______/    |__|  \______|       |__|     |__| |__|  |__| |_______|

        .___  ___.      ___       ______  __    __   __  .__   __.  _______                       
        |   \/   |     /   \     /      ||  |  |  | |  | |  \ |  | |   ____|                      
        |  \  /  |    /  ^  \   |  ,----'|  |__|  | |  | |   \|  | |  |__       ______            
        |  |\/|  |   /  /_\  \  |  |     |   __   | |  | |  . `  | |   __|     |______|           
        |  |  |  |  /  _____  \ |  `----.|  |  |  | |  | |  |\   | |  |____                       
        |__|  |__| /__/     \__\ \______||__|  |__| |__| |__| \__| |_______|                      



        Type a valid date in time and we'll create you a Spotify playlist with the top 100 songs
        played that day in the world.                                 
        Let's go for a ride.
    \033[m
    '''
    print(msg)


def log_into_spotify_with_credentials():
    scope = 'playlist-modify-private'
    sp = spotipy.Spotify(
        client_credentials_manager=SpotifyOAuth(
            scope=scope,
            client_id=SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            redirect_uri=SPOTIPY_REDIRECT_URI,
            show_dialog=True,
            cache_path="token.txt")
    )
    user_id = sp.current_user()['id']
    print(user_id)


def bye_message():
    print('\033[33mTime to take off. See you next time!\033[m')


def is_date_format_invalid(answer_date_split):
    # The idea here is not to treat an invalid date format and keep asking the user for valid input
    if len(answer_date_split) != 3:
        return True
    if len(answer_date_split) == 3:
        first_item_is_numeric = True if answer_date_split[0].isnumeric() and len(
            answer_date_split[0]) == 4 else False
        second_item_is_numeric = True if answer_date_split[1].isnumeric() and len(
            answer_date_split[1]) == 2 else False
        third_item_is_numeric = True if answer_date_split[2].isnumeric() and len(
            answer_date_split[2]) == 2 else False
        if first_item_is_numeric and second_item_is_numeric and third_item_is_numeric:
            return False
        return True


def send_request_to_billboard(date):
    url_billboard = f'https://www.billboard.com/charts/hot-100/{date}/'

    response = requests.get(url=url_billboard, allow_redirects=False)
    if response.status_code != 200:
        raise Exception(f'Error. We expeected a status_code value of 200, but we got {response.status_code} instead.'
                        f'.\nPlease, be sure to check if the URL is active.')
    return response


def grab_music_titles(response):
    soup = BeautifulSoup(response.content, 'lxml')
    containers = soup.find_all('div', {'class': 'o-chart-results-list-row-container'})
    if containers is None:
        raise Exception("Error. Please verify if the tags for each container exist in the response.")
    title_tags = [container.find('h3', {'id': 'title-of-a-story'}) for container in containers]
    title_names = [tag.text.strip() for tag in title_tags]
    index_number = 1
    for title in title_names:
        print(f'{index_number}. {title}')
        index_number += 1
    return title_names
