"""
Utility functions to interact with NFL Game Center.


Each game has a unique game center URL
Game Center URL's have the following format:
    http://www.nfl.com/scores/YYYY/SSNWK
Where YYYY is the year, SSN is the season (PRE, REG, POST), and WK is the week
    http://www.nfl.com/scores/2016/REG17
"""

import json, urllib.request
from bs4 import BeautifulSoup as soup


'''
Fetches the JSON object from NFL Game Center
The json's are available as follows

example: http://www.nfl.com/liveupdate/game-center/2016081152/2016081152_gtd.json
sample game_id:  2009091000
'''


def fetch_json(game_id):
    prefix = "http://www.nfl.com/liveupdate/game-center/"
    suffix = "_gtd.json"
    URL = prefix + str(game_id) + "/" + str(game_id) + suffix
    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())
    return data


'''
Fetches a list of game id's given input params.
Season must be one of: PRE, POST, REG

NFL game center stores game id's in URL's.
This is the easiest way I know to extract all game ID's in a given year and season.
'''


def fetch_game_ids(year, season):
    first_week = 1
    if season == "PRE":
        weeks = 4
    elif season == "REG":
        weeks = 17
    elif season == "POST":
        first_week = 18
        weeks = 22
    else:
        print('Season must be one of: PRE, POST, REG')
        return None

    game_ids = []
    prefix = "http://www.nfl.com/scores/"

    for wk in range(first_week, weeks + 1):
        # generate the specific game center URL
        url = prefix + str(year) + "/" + season + str(wk)

        # get the webpage and read it
        response = urllib.request.urlopen(url)
        html = response.read()
        s = soup(html, "lxml")

        # loop through all game center anchors
        for tag in s.find_all("a", class_="game-center-link", href=True):
            game_ids.append(tag.get('href')[12:22])

    return game_ids