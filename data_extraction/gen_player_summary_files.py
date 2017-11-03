""" Generates player game summary files."""

import os
import datetime
from data_extraction import gamecenter_utils as gc_utils

'''Process single game
TODO:  define output requirements
Code up this method next
'''


def process_single_game(game_id, data_dict):
    """Process single game
    TODO:  define output requirements
    Code up this method next
    :param game_id:
    :param data_dict:
    :return:
    """
    print("Processing: " + str(game_id))


def prompt_year(lower_limit, upper_limit, prompt):
    year = 0
    while not lower_limit <= year <= upper_limit:
        print("\t" + prompt + ": ")
        year = int(input('\tStart Year: '))
    return year

if __name__ == '__main__':
    # get output directory
    # /Users/J-Moneyham/NFL_exp
    output_dir = input('Specify Output Dir: ')
    if not os.path.isdir(output_dir):
        print("Invalid or non-accessible file path")
        exit()

    # get start year and end year for data collection range
    # must be greater than 2009
    start_year = end_year = 0
    min_year = 2009
    max_year = datetime.datetime.now().year + 1

    while not min_year <= start_year <= max_year:
        print("Input start year greater than " + str(min_year - 1) + ".")
        start_year = int(input('\tStart Year: '))
    while not start_year <= end_year <= max_year:
        print("Input end year greater than " + str(start_year - 1) + " and less than  " + str(max_year + 1))
        end_year = int(input('\tEnd Year: '))

    # get season type
    season = input('Season (PRE,POST,REG): ')

    # process games for each year
    for yr in range(start_year, end_year+1):

        # create a new directory for each year_season
        new_dir = output_dir + "/" + str(yr) + "_" + season
        if os.path.isdir(new_dir):
            print("Skipping year " + str(yr) + "; directory already exist.")
            continue
        else:
            os.mkdir(new_dir)

        # get list of game ids for current year
        game_ids = gc_utils.fetch_game_ids(yr, season)

        # process each game
        for id in game_ids:
            json_data = gc_utils.fetch_json(id)
            process_single_game(id, json_data)
