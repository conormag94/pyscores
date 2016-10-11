# pyscores [![Build Status](https://travis-ci.org/conormag94/pyscores.svg?branch=master)](https://travis-ci.org/conormag94/pyscores)
######A command line based python program to get football fixtures, results and standings.

This is a work in progress. It was inspired by another trending repo I saw on github. I wanted to see if I could do my own implementation of it, as a learning exercise.

**Tested in Python 2.7, 3.4 and 3.5**

##Setup
**To use this you will need an api key from api.football-data.org. Without this the program will still work but will be limited to 50 requests per day.**

Once you have your key, you must set an environment variable called `PYSCORES_KEY` so the program can use it.

**To install dependencies:** 
```pip install -r requirements.txt```

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

**Specifying number of days for Fixtures or Results**
```
python pyscores.py --fixtures --league=PL --days=20
```
```
python pyscores.py -f -l PL -d 20
```
The days argument is optional and will default to 7 if not specified.

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
