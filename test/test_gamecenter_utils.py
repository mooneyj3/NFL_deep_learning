import unittest
from data_extraction import gamecenter_utils as gcu


class TestGamecenterUtils(unittest.TestCase):

    def setUp(self):
        pass

    '''
    testing data source:  http://www.nfl.com/liveupdate/game-center/2016081152/2016081152_gtd.json
    game_id = 2016081152
    '''
    def test_fetch_json(self):
        game_id = 2016081152
        data = gcu.fetch_json(game_id)
        self.assertEqual(str(game_id), next(iter(data)))
        ATL = data[str(game_id)]['home']['abbr']
        self.assertEqual("ATL", ATL)
        pass

    def test_fetch_game_ids(self):
        year = 2016
        season = 'REG'
        game_ids = gcu.fetch_game_ids(year, season)
        for game in game_ids:
            print(game)
        pass