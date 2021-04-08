import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import datetime


def get_html(url):
    if url:
        r = requests.get(url, headers={'User-Agent': UserAgent().chrome})
        html = r.text
        return html


def parse(html):
    data_matches = []
    soup = BeautifulSoup(html, 'html')
    days = soup.find('div', class_='esport-match-future-list')
    matches = days.find_all('div', class_='esport-match-single')

    for i in range(len(matches)):
        match = matches[i].find('a', class_='team-vs-team')
        team_left = match.find('div', class_='team team-left')
        team_right = match.find('div', class_='team team-right')
        time = match.find('div', class_='time')
        print(time.text)
        if team_right:
            team_right_bet = team_right.find('span', class_='name')
            if team_right_bet:
                print(team_right_bet.text)
        if team_left:
            team_left_bet = team_left.find('span', class_='name')
            if team_left_bet:
                print(team_left_bet.text)
        data_matches.append(['Дата⏰:', time.text, team_left_bet.text, '🆚', team_right_bet.text])
    print(data_matches)
    return list(data_matches)

def get_matches():
    url = 'https://dota2.ru/esport/matches/'
    data = parse(get_html(url))
    return data
