from json import JSONEncoder

class newPlayer:
    def __init__(self, name, playerId, killType, deaths, prefWeapon, matchID):
        self.name = name
        self.playerId = playerId
        if killType == "Kill":
            self.kills = 1
            self.teamKills = 0
        else:
            self.kills = 0
            self.teamKills = 1
        self.deaths = deaths
        if self.deaths == 0:
            self.kd = self.kills
        else:
            self.kd = self.kills / self.deaths
        self.prefWeapon = prefWeapon
        self.matchID = matchID

class newPlayerEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

    # def getInfo(self):
        