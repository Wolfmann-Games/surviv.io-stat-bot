import json
import requests


def stats(name):
  try:
    headers = {'content-type': 'application/json; charset=UTF-8'}
    url = 'https://surviv.io/api/user_stats'
    payload = {"slug": name, "interval": "all", "mapIdFilter": "-1"}
    r = requests.post(url=url, headers=headers, data=json.dumps(payload))
    c = r.json()
    kills = str(c["kills"])
    wins = str(c["wins"])
    games = str(c["games"])
    kg = str(c["kpg"])
    mostkills = str(max([i["mostKills"] for i in c["modes"]]))
    maxdamage = str(max([i["mostDamage"] for i in c["modes"]]))
    print()
    print("Username:", name)
    print()
    print("Overall")
    print("Games:", games)
    print("Wins:", wins)
    print("Kills:", kills)
    print("K/G:", kg)
    print("Most Kills:", mostkills)
    print("Most Damage:", maxdamage)
    print()
    print("Solo")
    try:
      print("Games:", c['modes'][0]['games'])
      print("Wins:", c['modes'][0]['wins'])
      print("Kills:", c['modes'][0]['kills'])
      print("Win Rate:", c['modes'][0]['winPct'])
      print("Most Kills:", c['modes'][0]['mostKills'])
      print("Most Damage:", c['modes'][0]['mostDamage'])
      print("K/G:", c['modes'][0]['kpg'])
      print("Average Damage:", c['modes'][0]['avgDamage'])
      print("Average Time Alive:", c['modes'][0]['avgTimeAlive'], "s")
    except:
      print("No games played")
    print()
    print("Duo")
    try:
      print("Games:", c['modes'][1]['games'])
      print("Wins:", c['modes'][1]['wins'])
      print("Kills:", c['modes'][1]['kills'])
      print("Win Rate:", c['modes'][1]['winPct'])
      print("Most Kills:", c['modes'][1]['mostKills'])
      print("Most Damage:", c['modes'][1]['mostDamage'])
      print("K/G:", c['modes'][1]['kpg'])
      print("Average Damage:", c['modes'][1]['avgDamage'])
      print("Average Time Alive:", c['modes'][1]['avgTimeAlive'], "s")
    except:
      print("No games played")
    print()
    print("Squad")
    try:
      print("Games:", c['modes'][2]['games'])
      print("Wins:", c['modes'][2]['wins'])
      print("Kills:", c['modes'][2]['kills'])
      print("Win Rate:", c['modes'][2]['winPct'])
      print("Most Kills:", c['modes'][2]['mostKills'])
      print("Most Damage:", c['modes'][2]['mostDamage'])
      print("K/G:", c['modes'][2]['kpg'])
      print("Average Damage:", c['modes'][2]['avgDamage'])
      print("Average Time Alive:", c['modes'][2]['avgTimeAlive'], "s")
    except:
      print("No games played")
  except:
    print("That player does not exist")

while True:
  print()
  name = input("What is your Battletag? Please reply as it is in the stats url")

  stats(name)