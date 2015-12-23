import sys
import json
import requests
from tabulate import tabulate
from termcolor import colored

import leagues
import secret

BASE_URL = "http://api.football-data.org/alpha/"
API_KEY = secret.secret_key

headers = {'X-Auth-Token' : API_KEY}

def get_fixtures(league):
	if league in leagues.LEAGUE_IDS:
		request_url = "{}soccerseasons/{}/fixtures?timeFrame=n60".format(BASE_URL, leagues.LEAGUE_IDS[league])
	else:
		print("Error: No such league code")

	try:
		resp = requests.get(request_url, headers=headers)
		data = resp.json()
		print_fixtures(data['fixtures'])
	except:
		print("Error retrieving fixtures")

def print_fixtures(array):
	current_matchday = array[0]['matchday']
	fixtures = []
	for fixture in array:
		if fixture['matchday'] == current_matchday:
			s = [
				colored(format_date(fixture['date']), 'cyan'),
				colored(fixture['date'][11:16], 'blue'),
				fixture['homeTeamName'],
				'vs',
				fixture['awayTeamName']
			]
			fixtures.append(s)
	print(tabulate(fixtures, tablefmt="plain"))


def get_past_results(league):
	if league in leagues.LEAGUE_IDS:
		request_url = "{}soccerseasons/{}/fixtures?timeFrame=p40".format(BASE_URL, leagues.LEAGUE_IDS[league])
	else:
		print("Error: No such league code")

	try:
		resp = requests.get(request_url, headers=headers)
		data = resp.json()
		print_results(data['fixtures'])
	except:
		print("Error retrieving recent results")

def print_results(array):
	current_matchday = array[0]['matchday']
	results = []
	for fixture in array:
		if fixture['matchday'] == current_matchday:
			s = [
				colored(format_date(fixture['date']), 'cyan'),
				colored(fixture['date'][11:16], 'blue'),
				fixture['homeTeamName'],
				fixture['result']['goalsHomeTeam'],
				'vs',
				fixture['result']['goalsAwayTeam'],
				fixture['awayTeamName']
			]
			if int(s[3]) > int(s[5]):
				s[2] = colored(s[2], 'green')
				s[-1] = colored(s[-1], 'red')
			elif int(s[3]) < int(s[5]):
				s[2] = colored(s[2], 'red')
				s[-1] = colored(s[-1], 'green')
			else:
				s[2] = colored(s[2], 'yellow')
				s[-1] = colored(s[-1], 'yellow')

			results.append(s)
	print(tabulate(results, tablefmt="plain"))

# Gets current league table from selected league and calls print function
def get_standings(league):
	if league in leagues.LEAGUE_IDS:
		request_url = "{}soccerseasons/{}/leagueTable".format(BASE_URL, leagues.LEAGUE_IDS[league])
	else:
		print("Error: No such league code")
		
	try:
		resp = requests.get(request_url, headers=headers)
		data = resp.json()	
		print_standings(data['standing'])
	except:
		print("Error retrieving selected league table...")

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

	print(tabulate(standings, headers=['Pos', 'Club', 'Played', 'Points'], tablefmt="rst"))

def format_date(date_str):
	months = {'01':'Jan', '02':'Feb', '03':'Mar', '04':'Apr', '05':'May', '06':'Jun', '07':'Jul', '08':'Aug', '09':'Sep', '10':'Oct', '11':'Nov', '12':'Dec'}
	return (date_str[8:10] + " " + months[date_str[5:7]] + " " + date_str[:4])

def main():
	arg = sys.argv[1]
	get_standings(sys.argv[1])
	get_past_results(arg)
	get_fixtures(arg)

if __name__ == '__main__':
	main()
