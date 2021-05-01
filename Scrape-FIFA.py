import requests
from bs4 import BeautifulSoup
import csv


playerID = 1
playerType = 'gold'

with open('FIFADB.csv', mode='w', encoding='utf-8', newline='') as csv_file:
    fieldnames = ['PlayerID','PlayerName','PlayerRating','PlayerPOS','PAC','SHO','PAS','DRI','DEF','PHY','PlayerIMG','ClubIMG','CountryIMG']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for pg in range(210):
        URL = 'https://www.futhead.com/21/players/?level=all_nif&page=' + str(pg) + '&bin_platform=ps'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        # Player Rating
        playerList = soup.find_all('div', {'class':'content player-item font-24'})
        for player in playerList:
            playerRating = player.find('a').find('span',{'class':'player-rating stream-col-50 text-center'}).find('span',{'class':'revision-gradient shadowed font-12 fut21 ' + playerType + ' nif'}).text
            playerStats = player.find('a').find('span',{'class':'player-right text-center hidden-xs'}).find_all('span',{'class':'player-stat stream-col-60 hidden-md hidden-sm'})
            # print(playerStats.le)
            playerPAC = playerStats[0].find('span',{'class':'value'}).text
            playerSHO = playerStats[1].find('span',{'class':'value'}).text
            playerPAS = playerStats[2].find('span',{'class':'value'}).text
            playerDRI = playerStats[3].find('span',{'class':'value'}).text
            playerDEF = playerStats[4].find('span',{'class':'value'}).text
            playerPHY = playerStats[5].find('span',{'class':'value'}).text

            playerName = player.find('a').find('span',{'class':'player-info'}).find('span',{'class':'player-name'}).text
            playerPOS = player.find('a').find('span',{'class':'player-info'}).find('span',{'class':'player-club-league-name'}).find('strong').text

            playerIMG = player.find('a').find('span',{'class':'player-info'}).find_all('img')[0]['data-src']
            clubIMG = player.find('a').find('span',{'class':'player-info'}).find_all('img')[1]['data-src']
            countryIMG = player.find('a').find('span',{'class':'player-info'}).find_all('img')[2]['data-src']
            # for elem in job_elems:
            #     print(elem)
            #print(playerRating + ' ' + playerPAC + ' ' + playerSHO + ' ' + playerPAS + ' ' + playerDRI + ' ' + playerDEF + ' ' + playerPHY + ' ' + playerName + ' ' + playerPOS + '\n')
            print("Writing " + str(playerID) + " to CSV \n")
            writer.writerow({
                'PlayerID' : playerID,
                'PlayerName' : playerName,
                'PlayerRating' : playerRating,
                'PlayerPOS' : playerPOS,
                'PAC' : playerPAC,
                'SHO' : playerSHO,
                'PAS' : playerPAS,
                'DRI' : playerDRI,
                'DEF' : playerDEF,
                'PHY': playerPHY,
                'PlayerIMG' : playerIMG,
                'ClubIMG' : clubIMG,
                'CountryIMG' : countryIMG
            })
            playerID = playerID + 1
            if(playerID == 1921):
                playerType = 'silver'
