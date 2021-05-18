from pymongo import MongoClient

def createDbPlayerObj(matchID, playerID, playerName):

    client = MongoClient()

    database = client["20thPlayerStats"]
    collection = database[matchID]

    post = {
        "_id" : playerID,
        "playerName" : playerName,
        "Kills" : 0,
        "TeamKills" : 0,
        "Deaths" : 0,
        "Weapons" : {
            "Kar98k" : 0,
            "Gewehr43" : 0,
            "M1 Garand" : 0,
            "M1 Carbine" : 0,
            "M1903 Springfield" : 0,
            "Karabiner 98k x8" : 0,
            "M1918A2 BAR" : 0,
            "StG 44" : 0,
            "M1A1 Thompson" : 0,
            "M3 Grease Gun" : 0,
            "MP40" : 0,
            "Browning M1919" : 0,
            "MG42" : 0,
            "MG34" : 0,
            "Colt M1911" : 0,
            "Luger P08" : 0,
            "Walter P38" : 0,
            "MK2 Grenade" : 0,
            "M43 Stielhandgranate" : 0
        }
    }

    insertConfirmation = collection.insert_one(post)

createDbPlayerObj('asdf3feawfaw432', '16743vfads83', 'Airehtrsh')
