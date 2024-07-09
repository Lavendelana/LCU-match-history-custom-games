from helpers import get_summoner_info, get_match_ids, get_match_details
from gamedata import GameData, Participant

import urllib3
import datetime
import config
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def run_data(gameDetails, participantId, writeToExcel):
  gameData = GameData(gameData=gameDetails, teamData=gameDetails['teams'][0 if participantId < 6 else 1])
  patchData = gameDetails['gameVersion'].split('.')
  patchString = f'{patchData[0]}.{patchData[1]}.1'
  for index in indexRange:
    participantName = gameDetails['participantIdentities'][index]['player']['gameName']
    participantData = gameDetails['participants'][index]
    participantObj = Participant(summonerName=participantName, participantData=participantData, patch=patchString)
    gameData.add_participant(participantObj)
  if writeToExcel:
    gameData.write_to_excel()
  return gameData

summoner = get_summoner_info()
matches = get_match_ids()
games = matches['games']['games']
summonerName = summoner['displayName']
writeGames = []
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
      if len(config.DATE) == 10:
        gameDate = datetime.datetime.strptime(gameDetails['gameCreationDate'][:10], '%Y-%m-%d')
        compareDate = datetime.datetime.strptime(config.DATE, '%Y-%m-%d')
        if (gameDate == compareDate):
          writeGames.append(run_data(gameDetails, participantId, False))
      else:
        run_data(gameDetails, participantId, True)
if len(writeGames) > 0:
  # Write from bottom to top
  for index in range(0, len(writeGames)):
    currentIndex = len(writeGames) - index -1
    writeGames[currentIndex].write_to_excel()

      
