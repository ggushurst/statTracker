from pymongo import MongoClient

def updateDbPlayerObj(matchID, playerID, killType, weapon):
    
    client = MongoClient()

    database = client["20thPlayerStats"]
    collection = database[matchID]

    playerIdQuery = { "_id" : playerID }
    playerKillQuery = 
    playerDoc = collection.find_one_and_update(
        playerDataQuery,
        
    )
    for line in playerDoc:
        print(line)

    # if killType == "Kill":
    #     killCount += 1 

updateDbPlayerObj('asdf3feawfaw432', '16743vfads83', 'Kill', 'BAR')