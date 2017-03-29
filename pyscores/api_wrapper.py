import json
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
        url = "%s/competitions" % self.base_url
        response = self.do_request(url=url)
        return response


def main():
    api = APIWrapper(auth_token=os.environ["PYSCORES_KEY"])
    res = api.do_request("http://api.football-data.org/v1/competitions")
    print(res)

if __name__ == "__main__":
    main()

