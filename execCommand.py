import webbrowser
import requests
import random
from bs4 import BeautifulSoup as scrapper


def openWebPage(url):

    url = 'https://www.youtube.com' + url
    webbrowser.open(url, new=1, autoraise=True)

    return True


def friendsProtocol(text):

    if 'friends' in text:
        url = 'https://www.youtube.com/results?search_query=friends'

        friends_list = list()

        webpage = requests.get(url).text
        webpage = scrapper(webpage, 'html.parser')

        for links in webpage.find_all('a', href=True):
            if '/watch' in links['href']:
                friends_list.append(links['href'])

        friends_list = list(set(friends_list))

        if openWebPage(random.choice(friends_list[:6])):
            return True

    return False


def execute(command):

    if friendsProtocol(command):
        to_say =  'Opening FRIENDS. Enjoy!'
    elif 'exit' in command:
        to_say =  'Ok! Bye. Have a great day.'
    else:
        to_say = 'Sorry I can\'t do that at this moment.'

    return to_say
