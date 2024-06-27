from helpers import get_summoner_info, get_match_ids, get_match_details
from gamedata import GameData, Participant

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

summoner = get_summoner_info()
matches = get_match_ids()
games = matches['games']['games']
summonerName = summoner['displayName']
for game in games:
  if game['gameType'] == 'CUSTOM_GAME':
    gameDetails = get_match_details(game['gameId'])
    if len(gameDetails['participantIdentities']) == 10:
      for participant in gameDetails['participantIdentities']:
        if participant['player']['summonerName'] == summonerName:
          participantId = participant['participantId']
          if participantId > 5:
            indexRange = range(5,10)
          else:
            indexRange = range(0,5)
          break
      gameData = GameData(gameData=gameDetails, teamData=gameDetails['teams'][0 if participantId < 6 else 1])
      patchData = gameDetails['gameVersion'].split('.')
      patchString = f'{patchData[0]}.{patchData[1]}.1'
      for index in indexRange:
        participantName = gameDetails['participantIdentities'][index]['player']['gameName']
        participantData = gameDetails['participants'][index]
        participantObj = Participant(summonerName=participantName, participantData=participantData, patch=patchString)
        gameData.add_participant(participantObj)
      gameData.write_to_excel()
