import requests
from bs4 import BeautifulSoup

class Bot:

    def __init__(self):
        self.date_in_time = ''

    @staticmethod
    def show_welcome_message():
        welcome = 'Welcome!'
        return welcome

    @staticmethod
    def show_bye_message():
        return print('Bye!')

    @staticmethod
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


    def send_request_to_billboard(self, date):
        url_billboard = f'https://www.billboard.com/charts/hot-100/{date}/'

        response = requests.get(url=url_billboard, allow_redirects=False)
        if response.status_code != 200:
            raise Exception(f'Erro. Status_code esperado era 200, mas recebemos {response.status_code}.\nVerificar se '
                            'a URL está funcionando e ativa.')
        return response

    def grab_music_titles(self, response):
        soup = BeautifulSoup(response.content, 'lxml')
        containers = soup.find_all('div', {'class': 'o-chart-results-list-row-container'})
        if containers is None:
            raise Exception("Error. Please verify if the tags for each container exist in the response.")
        title_tags = [container.find('h3', {'id': 'title-of-a-story'}) for container in containers]
        title_names = [tag.text.strip() for tag in title_tags]
        return title_names
