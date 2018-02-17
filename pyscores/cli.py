import os

import pendulum
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


def format_date(date_str):
    datetime = pendulum.parse(date_str)
    return datetime.strftime('%a, %d %b %Y, %H:%M')


def print_fixtures(array):
    current_matchday = array[0]['matchday']
    fixtures_list = []
    for fixture in array:
        if fixture['matchday'] == current_matchday:
            s = [
                colored(format_date(fixture['date']), 'cyan'),
                fixture['homeTeamName'],
                'vs',
                fixture['awayTeamName']
            ]
            fixtures_list.append(s)
    print(tabulate(fixtures_list, tablefmt="plain"))


# Prints and colour codes recent results
def print_results(array):
    results_list = []
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

            results_list.append(s)
    print(tabulate(results_list, tablefmt="plain"))


# Prints the league standings in a table
def print_standings(table):
    standings_list = []
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
        standings_list.append(entry)

    print(tabulate(standings_list, headers=['#', 'Team', 'Games', 'W', 'D', 'L', 'GD', 'Pts'],
                   tablefmt="simple"))


@click.group()
def main():
    """Provides football data in the command line."""
    pass


@main.command()
@click.option('--league', '-l', help='Specific league code to retrieve results for',
              type=click.Choice(config.LEAGUE_IDS.keys()))
def standings(league):
    """Current standings (league table) for a given league."""
    try:
        competition_id = config.LEAGUE_IDS[league]
        current_standings = api.competition_table(competition_id)
        print_standings(current_standings["standing"])
    except Exception as e:
        print(e)
        print("Error retrieving selected league table...")


@main.command()
@click.option('--league', '-l', type=click.Choice(config.LEAGUE_IDS.keys()),
              help='Specific league code to retrieve fixtures for')
@click.option('--days', '-d', default=7,
              help='Number of days for which to fetch fixtures. Defaults to next 7 days')
def fixtures(league, days):
    """Upcoming fixtures for a given league."""
    filters = {"timeFrame": "n{0}".format(days)}

    try:
        competition_id = config.LEAGUE_IDS[league]
        fixtures_list = api.competition_fixtures(competition_id, filters)
        if fixtures_list['count'] == 0:
            print("API returned 0 results within next {} days".format(days))
        else:
            print_fixtures(fixtures_list['fixtures'])
    except Exception as e:
        print(e)
        print("Error retrieving upcoming fixtures")


@main.command()
@click.option('--league', '-l', type=click.Choice(config.LEAGUE_IDS.keys()),
              help='Specific league code to retrieve results for')
@click.option('--days', '-d', default=7,
              help='Number of days for which to fetch results. Defaults to previous 7 days')
def results(league, days):
    """Recent results for a given league."""
    filters = {"timeFrame": "p{0}".format(days)}

    try:
        competition_id = config.LEAGUE_IDS[league]
        results_list = api.competition_fixtures(competition_id, filters)
        if results_list['count'] == 0:
            print("API returned 0 results within last {} days".format(days))
        else:
            print_results(results_list['fixtures'])
    except Exception as e:
        print(e)
        print("Error retrieving recent results")


if __name__ == '__main__':
    main()
