import sys
import json
import requests
import click
from tabulate import tabulate
from termcolor import colored

import leagues
import secret

BASE_URL = "http://api.football-data.org/alpha/"
API_KEY = secret.secret_key

headers = {'X-Auth-Token' : API_KEY}

def get_fixtures(league, time_frame=40):
	if league in leagues.LEAGUE_IDS:
		request_url = "{}soccerseasons/{}/fixtures?timeFrame=n{}".format(BASE_URL, leagues.LEAGUE_IDS[league], time_frame)
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

# Gets results for the most recent matchday
def get_results(league, time_frame=40):
	if league in leagues.LEAGUE_IDS:
		request_url = "{}soccerseasons/{}/fixtures?timeFrame=p{}".format(BASE_URL, leagues.LEAGUE_IDS[league], time_frame)
	else:
		print("Error: No such league code")

	try:
		resp = requests.get(request_url, headers=headers)
		data = resp.json()
		print_results(data['fixtures'])
	except:
		print("Error retrieving recent results")

# Prints and colour codes recent results
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
			team['teamName'].replace('AFC', '').replace('FC', ''),
			team['playedGames'],
			team['wins'],
			team['draws'],
			team['losses'],
			team['goalDifference'],
			team['points']
		]
		standings.append(entry)

	print(tabulate(standings, headers=['#', 'Team', 'Games', 'W', 'D', 'L', 'GD', 'Pts'], tablefmt="simple"))

def format_date(date_str):
	months = {'01':'Jan', '02':'Feb', '03':'Mar', '04':'Apr', '05':'May', '06':'Jun', '07':'Jul', '08':'Aug', '09':'Sep', '10':'Oct', '11':'Nov', '12':'Dec'}
	return (date_str[8:10] + " " + months[date_str[5:7]] + " " + date_str[:4])

@click.command()
@click.option('--standings', '-s', multiple=True, is_flag=True, help='Current league standings for a particular league')
@click.option('--results', '-r', is_flag=True, help='Most recent matchday results')
@click.option('--fixtures', '-f', is_flag=True, help='Upcoming fixtures for next matchday')
@click.option('--league', '-l', help='Specified league code to retrieve results for', type=click.Choice(leagues.LEAGUE_IDS.keys()))
def main(standings, results, fixtures, league):
	try:
		if league:
			if standings:
				get_standings(league)

			if results:
				get_results(league)

			if fixtures:
				get_fixtures(league)
		else:
			print("Please specify a league")
	except:
		print("Something went wrong")

if __name__ == '__main__':
	main()