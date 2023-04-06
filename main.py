import csv
import pandas as pd

class Team:

    def __init__(self, name, elo):
        self.__name = name
        self.__elo = elo

    def get_team_name(self):
        return self.__name

    def get_elo(self):
        return self.__elo

    def set_team_name(self, name):
        self.__name = name

    def set_elo(self, elo):
        self.__elo = elo

    def __str__(self):
        return f'Team: {self.__name}, ELO: {self.__elo}'

path = 'fixtures.csv'


def import_data_from_csv(file_path: str):
    """

    :param file_path: the relative path to the csv file to be read
    :return: df: the dataframe returned as a result from reading the dataframe
    """
    df = pd.read_csv(file_path)

    return df


results_df = import_data_from_csv(path)

# Getting all team names and sorting them into alphabetical order
team_names = results_df['Home'].unique()
team_names.sort()

teams = []

for name in team_names:
    team = Team(name, 1000)
    teams.append(team)

for t in teams:
    print(t)


