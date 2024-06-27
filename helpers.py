import config
import requests
import openpyxl

def get_summoner_info():
  api_url = f"{config.BASE_URL}/lol-summoner/v1/current-summoner"
  headers = {
    "Authorization": config.AUTHENTICATION
  }
  try:
    response = requests.get(api_url, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()
  except requests.exceptions.RequestException as ex:
    print(f'Error getting data from summoner endpoint: {ex}')
    return None
  
def get_match_ids():
  headers = {
    "Authorization": config.AUTHENTICATION
  }
  api_url = f"{config.BASE_URL}/lol-match-history/v1/products/lol/current-summoner/matches"
  try:
    response = requests.get(api_url, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()
  except requests.exceptions.RequestException as ex:
    print(f'Error getting matchIds: {ex}')
    return None
  
def get_match_details(gameId):
  headers = {
    "Authorization": config.AUTHENTICATION
  }
  api_url = f"{config.BASE_URL}/lol-match-history/v1/games/{gameId}"
  try:
    response = requests.get(api_url, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()
  except requests.exceptions.RequestException as ex:
    print(f'Error getting matchIds: {ex}')
    return None

championsList = {}

def get_champion_name(championId, patch):
  if len(championsList) == 0:
    try:
      response = requests.get(f'http://ddragon.leagueoflegends.com/cdn/{patch}/data/en_US/champion.json')
      response.raise_for_status()
      championData = response.json()
    except requests.exceptions.RequestException as ex:
      print(f'Error getting champion data: {ex}')
      return None
    for key in championData['data']:
      championId = int(championData['data'][key]['key'])
      championsList[championId] = key
  return championsList[championId]