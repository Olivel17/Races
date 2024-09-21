races_data = [
    {'Ferrari': 20, 'Mercedes': 5, 'Aston Martin': 10, 'Williams': 15},
    {'Mercedes': 15, 'Aston Martin': 20, 'Ferrari': 10, 'Williams': 0},
    {'Ferrari': 20, 'Williams': 15, 'Aston Martin': 10, 'Mercedes': 5}
]


def get_competition_data(data):
    teams = {}

    for race in data:
        for team, points in race.items():
            if team in teams:
                teams[team] += points
            else:
                teams[team] = points

    sorted_teams = sorted(teams.keys())
    winning_team = max(teams, key=teams.get)
    winning_score = teams[winning_team]

    teams_string = ', '.join(sorted_teams)

    print(f'Team that participated in the race: {teams_string}')
    print(f'The race was won by team {winning_team} with the score of {winning_score} points')


get_competition_data(races_data)
