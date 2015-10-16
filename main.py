import json
import requests
from tabulate import tabulate

BASE_URL = "http://api.football-data.org/alpha/"
soccer_seasons = "soccerseasons/"

epl_current_season = "soccerseasons/398/"
league_table = "leagueTable/"


def print_standings(table):
	standings = []
	for team in table:
		entry = [team['position'], team['teamName'], team['points']]
		standings.append(entry)

	print tabulate(standings, headers=['Pos', 'Club', 'Points'], tablefmt="rst")

def main():
	resp = requests.get(BASE_URL + epl_current_season + league_table)
	data = resp.json()

	league_standings = data['standing']
	
	print_standings(league_standings)

if __name__ == '__main__':
	main()
