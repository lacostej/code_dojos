class TennisGame():

  playerOneScore = 0  
  playerTwoScore = 0

  def announceScore(self):
    if self.isWin():
      return "game " + self.getLeader()
    if self.isAdvantage():
      return "advantage " + self.getLeader()
    if self.isDeuce():
      return "deuce"
    if self.isAll():
      return self.spokenScore(self.playerOneScore) + "-all"
    else:
      return self.spokenScore(self.playerOneScore) + "-" + self.spokenScore(self.playerTwoScore) 

  def isAdvantage(self):
    return ((self.playerOneScore == 4 and self.playerTwoScore == 3) or
      (self.playerTwoScore == 4 and self.playerOneScore == 3))
  
  def isWin(self):
    return self.isPlayerTwoWin() or self.isPlayerOneWin()

  def isPlayerTwoWin(self):
    return self.playerTwoScore >= 4 and self.playerTwoScore - self.playerOneScore > 1

  def isPlayerOneWin(self):
    return self.playerOneScore >= 4 and self.playerOneScore - self.playerTwoScore > 1

  def getLeader(self):
    if self.playerOneScore > self.playerTwoScore: return "player one"
    return "player two" 

  def isAll(self):
    return self.playerOneScore == self.playerTwoScore

  def isDeuce(self):
    return self.isAll() and self.playerTwoScore == 3

  def spokenScore(self, score):
    if score == 0: return "love"
    if score == 1: return "fifteen"
    if score == 2: return "thirty"
    if score == 3: return "forty"

  def scorePlayerOne(self):
    self.playerOneScore += 1

  def scorePlayerTwo(self):
    self.playerTwoScore += 1
