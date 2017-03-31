"""A wrapper class for the football-data API"""

import os

import requests


class APIWrapper(object):

    def __init__(self, base_url=None, auth_token=None):

        if base_url:
            self.base_url = base_url
        else:
            self.base_url = "http://api.football-data.org/v1"

        if auth_token:
            self.headers = {
                'X-Auth-Token': auth_token
            }
        else:
            self.headers = {}

    def do_request(self, url, filters=None):
        params = filters if filters else {}
        r = requests.get(url=url, params=params, headers=self.headers)
        if r.status_code == requests.codes.ok:
            return r.json()
        return None

    def all_competitions(self):
        url = "{0}/competitions".format(self.base_url)
        response = self.do_request(url=url)
        return response

    def competition(self, competition_id):
        """Return a JSON object for a competition by its id."""
        url = "{0}/competitions/{1}".format(self.base_url, competition_id)
        response = self.do_request(url=url)
        return response

    #TODO: Add filters
    def competition_teams(self, competition_id):
        """Return a JSON list of teams in a particular competition."""
        url = "{0}/competitions/{1}/teams".format(self.base_url, competition_id)
        response = self.do_request(url=url)
        return response

    # TODO: Add filters
    def competition_fixtures(self, competition_id):
        """Returns a JSON list of all fixtures, past and present, in a competition"""
        url = "{0}/competitions/{1}/fixtures".format(self.base_url, competition_id)
        response = self.do_request(url=url)
        return response

    def competition_table(self, competition_id, filters=None):
        """Return the current league table for a competition"""
        url = "{0}/competitions/{1}/leagueTable".format(self.base_url, competition_id)
        response = self.do_request(url=url, filters=filters)
        return response

def main():
    api = APIWrapper(auth_token=os.environ["PYSCORES_KEY"])
    res = api.do_request("http://api.football-data.org/v1/competitions")
    print(res)

if __name__ == "__main__":
    main()

