# pyscores
######A command line based python program to get football fixtures, results and standings.

This is very much a work in progress and is currently being worked on. It was inspired by another trending repo I saw on github. I wanted to see if I could do my own implementation of it, as a learning exercise.

-Should work in python 2 or 3

##Setup
**To use this you will need an api key from api.football-data.org. Without this the program will be limited to 50 requests per day.**

Once you have your key, in the same directory as __main.py__, create a file called __secret.py__ with the following code, replacing "YOUR KEY HERE" with the key you were given.
```python
secret_key = "YOUR KEY HERE"
```
Then run using
```
python pyscores.py PL
```
where ` PL ` is the league code for the Premier League

Modules needed
* click
* requests
* tabulate
* termcolor
