import json
import requests
from tabulate import tabulate

import leagues
import secret

BASE_URL = "http://api.football-data.org/alpha/"
API_KEY = secret.secret_key

headers = {'X-Auth-Token' : API_KEY}

# Gets current league table from selected league and calls print function
def get_standings(league):
	if league in leagues.LEAGUE_IDS:
		request_url = "{}soccerseasons/{}/leagueTable".format(BASE_URL, leagues.LEAGUE_IDS[league])
	else:
		print "Error: No such league code"
		
	try:
		resp = requests.get(request_url, headers=headers)
		data = resp.json()	
		print_standings(data['standing'])
	except:
		print "Error retrieving selected league table..."

# Prints the league standings in a table
def print_standings(table):
	standings = []
	for team in table:
		entry = [
			team['position'],
			team['teamName'],
			team['playedGames'],
			team['points']
		]
		standings.append(entry)

	print tabulate(standings, headers=['Pos', 'Club', 'Played', 'Points'], tablefmt="rst")

def main():
	get_standings("EPL")

if __name__ == '__main__':
	main()
