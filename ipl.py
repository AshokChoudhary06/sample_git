import pandas as pd
import numpy as np

link_data = "data\IPL_Matches_2008_2022.csv"
df = pd.read_csv(link_data)

def teams_played():
    teams = list(set(list(df['Team1']) + list(df['Team2'])))
    team_dict = {
        'teams':
        teams
    }
    return team_dict

def teamvteamApi(team1, team2):
    df_team = df[(df.Team1 == team1) & (df.Team2 == team2) | (df.Team1 == team2) & (df.Team2 == team1)]
    matches_played = df_team.shape[0]
    team1_win = df_team['WinningTeam'].value_counts()[team1]
    team2_win = df_team['WinningTeam'].value_counts()[team2]

    team_dict = {
        'team1': team1,
        'team2': team2,
        'matches_played': str(matches_played),
         team1: str(team1_win),
         team2: str(team2_win)
    }
    return team_dict