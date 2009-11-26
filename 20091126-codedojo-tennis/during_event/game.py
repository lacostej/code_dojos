class TennisGame():
  PLAYER_ONE = 0
  PLAYER_TWO = 1

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
    return self.getPlayerTwoScore() >= 4 and self.getPlayerTwoScore() - self.getPlayerOneScore() > 1

  def isPlayerOneWin(self):
    return self.getPlayerOneScore() >= 4 and self.getPlayerOneScore() - self.getPlayerTwoScore() > 1

  def getLeader(self):
    if self.getPlayerOneScore() > self.getPlayerTwoScore(): return "player one"
    return "player two" 

  def isAll(self):
    return self.getPlayerOneScore() == self.getPlayerTwoScore()

  def isDeuce(self):
    return self.isAll() and self.getPlayerTwoScore() >= 3

  def spokenScore(self, score):
    if score == 0: return "love"
    if score == 1: return "fifteen"
    if score == 2: return "thirty"
    if score == 3: return "forty"

  def getPlayerOneScore(self):
    return self.scores[self.PLAYER_ONE]

  def getPlayerTwoScore(self):
    return self.scores[self.PLAYER_TWO]

  def scorePlayerOne(self):
    self.scores[self.PLAYER_ONE] += 1
    self.printScores()

  def scorePlayerTwo(self):
    self.scores[self.PLAYER_TWO] += 1
    self.printScores()

  def printScores(self):
    print "p1: " + str(self.getPlayerOneScore()) + " p2: " + str(self.getPlayerTwoScore())

