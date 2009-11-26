class TennisGame():
  PLAYER_ONE = 0
  PLAYER_TWO = 1
  SPOKEN_SCORES = ["love", "fifteen", "thirty", "forty"]

  def __init__(self):
    self.scores = [0, 0]
    self.printScores()

  def announceScore(self):
    if self.isWin():
      return "game " + self.getLeader()
    if self.isAdvantage():
      return "advantage " + self.getLeader()
    if self.isDeuce():
      return "deuce"
    if self.isAll():
      return self.spokenScore(self.getPlayerOneScore()) + "-all"
    else:
      return self.spokenScore(self.getPlayerOneScore()) + "-" + self.spokenScore(self.getPlayerTwoScore()) 

  def isAdvantage(self):
    return (not self.isWin() and 
      self.getPlayerOneScore() >= 3 and self.getPlayerTwoScore() >= 3 and 
      self.getPlayerOneScore() != self.getPlayerTwoScore())
  
  def isWin(self):
    return self.isPlayerTwoWin() or self.isPlayerOneWin()

  def isPlayerTwoWin(self):
    return self.isPlayerWin(self.PLAYER_TWO, self.PLAYER_ONE)

  def isPlayerOneWin(self):
    return self.isPlayerWin(self.PLAYER_ONE, self.PLAYER_TWO)

  def isPlayerWin(self, playerA, playerB):
    return self.getPlayerScore(playerA) >= 4 and self.getPlayerScore(playerA) - self.getPlayerScore(playerB) > 1

  def getLeader(self):
    if self.getPlayerOneScore() > self.getPlayerTwoScore(): return "player one"
    return "player two" 

  def isAll(self):
    return self.getPlayerOneScore() == self.getPlayerTwoScore()

  def isDeuce(self):
    return self.isAll() and self.getPlayerTwoScore() >= 3

  def spokenScore(self, score):
    return self.SPOKEN_SCORES[score]

  def getPlayerOneScore(self):
    return self.getPlayerScore(self.PLAYER_ONE)

  def getPlayerTwoScore(self):
    return self.getPlayerScore(self.PLAYER_TWO)

  def getPlayerScore(self, player):
    return self.scores[player]

  def scorePlayerOne(self):
    self.scores[self.PLAYER_ONE] += 1
    self.printScores()

  def scorePlayerTwo(self):
    self.scores[self.PLAYER_TWO] += 1
    self.printScores()

  def printScores(self):
    print "p1: " + str(self.getPlayerOneScore()) + " p2: " + str(self.getPlayerTwoScore())

