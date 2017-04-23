import os

import requests
import click
from tabulate import tabulate
from termcolor import colored

from pyscores import config
from pyscores import api_wrapper

try:
    API_KEY = os.environ['PYSCORES_KEY']
except KeyError:
    API_KEY = ''
    print("Warning: No API key found. You will be limited to 50 API calls per day")

api = api_wrapper.APIWrapper(base_url=config.BASE_URL, auth_token=API_KEY)


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


# Prints and colour codes recent results
def print_results(array):
    results = []
    for fixture in array:
        res = fixture['result']['goalsHomeTeam']
        if res is not -1:
            s = [
                colored(format_date(fixture['date']), 'cyan'),
                fixture['homeTeamName'],
                fixture['result']['goalsHomeTeam'],
                '-',
                fixture['result']['goalsAwayTeam'],
                fixture['awayTeamName']
            ]
            if int(s[2]) > int(s[4]):
                s[1] = colored(s[1], 'green')
                s[-1] = colored(s[-1], 'red')
            elif int(s[2]) < int(s[4]):
                s[1] = colored(s[1], 'red')
                s[-1] = colored(s[-1], 'green')
            else:
                s[1] = colored(s[1], 'yellow')
                s[-1] = colored(s[-1], 'yellow')

            results.append(s)
    print(tabulate(results, tablefmt="plain"))


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


def get_fixtures(league, time_frame=7):
    filters = {"timeFrame": "n{0}".format(time_frame)}

    try:
        competition_id = config.LEAGUE_IDS[league]
        fixtures = api.competition_fixtures(competition_id, filters)
        if fixtures['count'] == 0:
            print("API returned 0 results within next {} days".format(time_frame))
        else:
            print_fixtures(fixtures['fixtures'])
    except Exception as e:
        print(e)
        print("Error retrieving upcoming fixtures")


def get_results(league, time_frame=7):
    filters = {"timeFrame": "p{0}".format(time_frame)}

    try:
        competition_id = config.LEAGUE_IDS[league]
        results = api.competition_fixtures(competition_id, filters)
        if results['count'] == 0:
            print("API returned 0 results within last {} days".format(time_frame))
        else:
            print_results(results['fixtures'])
    except Exception as e:
        print(e)
        print("Error retrieving recent results")


def get_standings(league):
    try:
        competition_id = config.LEAGUE_IDS[league]
        standings = api.competition_table(competition_id)
        print_standings(standings["standing"])
    except Exception as e:
        print(e)
        print("Error retrieving selected league table...")


def format_date(date_str):
    months = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug',
              '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
    return (date_str[8:10] + " " + months[date_str[5:7]] + " " + date_str[:4])


@click.command()
@click.option('--standings', '-s', multiple=False, is_flag=True,
              help='Current league standings for a particular league')
@click.option('--results', '-r', is_flag=True, help='Most recent matchday results')
@click.option('--fixtures', '-f', is_flag=True, help='Upcoming fixtures for next matchday')
@click.option('--league', '-l', help='Specific league code to retrieve results for',
              type=click.Choice(config.LEAGUE_IDS.keys()))
@click.option('--days', '-d', default=7, help="Number of days for which to fetch results/fixtures (Default = 7)")
def main(standings, results, fixtures, league, days):
    try:
        if league:
            if standings:
                get_standings(league)

            if results:
                get_results(league, time_frame=days)

            if fixtures:
                get_fixtures(league, time_frame=days)
        else:
            print("Please specify a league")
    except:
        print("Something went wrong")


if __name__ == '__main__':
    main()
