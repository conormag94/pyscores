# pyscores
######A command line based python program to get football fixtures, results and standings.

This is a work in progress. It was inspired by another trending repo I saw on github. I wanted to see if I could do my own implementation of it, as a learning exercise.

-Should work in python 2 or 3

##Setup
**To use this you will need an api key from api.football-data.org. Without this the program will be limited to 50 requests per day.**

Once you have your key, in the same directory as __main.py__, create a file called __secret.py__ with the following code, replacing "YOUR KEY HERE" with the key you were given.
```python
secret_key = "YOUR KEY HERE"
```
##Usage
######Depending on the installed version of python, it may be necessary to substitute `python` for `python3`.

**Recent results**
```
python pyscores.py --results --league=PL
```
```
python pyscores.py -r -l PL
```
where ` PL ` is the league code for the Premier League

![alt text] (https://github.com/conormag94/pyscores/raw/master/assets/results.png "Results Output")

**Fixtures for next matchday**
```
python pyscores.py --fixtures --league=PL
```
```
python pyscores.py -f -l PL
```
![alt text](https://github.com/conormag94/pyscores/raw/master/assets/fixtures.png "Fixtures Output")

**League standings**
```
python pyscores.py --standings --league=PL
```
```
python pyscores.py -s -l PL
```
![alt text](https://github.com/conormag94/pyscores/raw/master/assets/standings.png "Standings Output")


##Python Modules needed
* click
* requests
* tabulate
* termcolor
