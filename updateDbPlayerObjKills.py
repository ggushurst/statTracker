from pymongo import MongoClient

def updateDbPlayerObjKills(matchID, playerID, killType, weapon):
    
    client = MongoClient()

    database = client["20thPlayerStats"]
    collection = database[matchID]

    filter = {"_id" : playerID}
    newValues = { "$inc" : { "Kills" : 1, "Weapons.{}".format(weapon) : 1}}
    collection.update_one(filter, newValues)