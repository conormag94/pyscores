Pyscores: Football scores and data in your terminal 
===================================================
[![Build Status](https://travis-ci.org/conormag94/pyscores.svg?branch=master)](https://travis-ci.org/conormag94/pyscores)
[![PyPI version](https://badge.fury.io/py/pyscores.svg)](https://badge.fury.io/py/pyscores)

**Pyscores is a command line based python program to get football fixtures, results and standings.**

This is a work in progress. It was inspired by another trending repo I saw on github. I wanted to see if I could do my own implementation of it, as a learning exercise.

**Tested in Python 2.7 and >=3.3**

## Setup
**To use this you will need an api key from api.football-data.org. Without this the program will still work but will be limited to 50 requests per day.**

Once you have your key, you must set an environment variable called `PYSCORES_KEY` so the program can use it.

**To install (with pip):** 
```
pip install pyscores
```

**To Verify installation:**
```
scores --help
```

## Usage

**Recent results**
```
scores results --league=PL
```
```
scores results -l PL
```
where ` PL ` is the league code for the Premier League

![alt text](https://github.com/conormag94/pyscores/raw/master/assets/results.png "Results Output")

**Fixtures for next matchday**
```
scores fixtures --league=PL
```
```
scores fixtures -l PL
```
![alt text](https://github.com/conormag94/pyscores/raw/master/assets/fixtures.png "Fixtures Output")

**Specifying number of days for Fixtures or Results**
```
scores results --league=PL --days=20
```
```
scores results -l PL -d 20
```
The days argument is optional and will default to 7 if not specified.

**League standings**
```
scores standings --league=PL
```
```
scores standings -l PL
```
![alt text](https://github.com/conormag94/pyscores/raw/master/assets/standings.png "Standings Output")

## League codes

| League Code | League Name |
| ----------- | ----------- |
| BSA | Campeonato Brasileiro da Série A |
| PL | Premier League |
| ELC | Championship |
| EL1 | League One |
| EL2 | League Two |
| DED | Eredivisie |
| FL1 | Ligue 1 |
| FL2 | Ligue 2 |
| BL1 | 1. Bundesliga |
| BL2 | 2. Bundesliga |
| PD | Primera Division (La Liga) |
| SA | Serie A |
| SB | Serie B |
| PPL | Primeira Liga |
| DFB | DFB-Pokal |
| CL | Champions League |
| AAL | Australian A-League |



## Dependencies
* click
* requests
* tabulate
* termcolor
