class TennisGame():

  playerOneScore = 0  

  def announceScore(self):
    if self.playerOneScore == 1:
      return "fifteen-love"
    elif self.playerOneScore == 2:
      return "thirty-love"
    else:
      return "love-all"

  def scorePlayerOne(self):
    self.playerOneScore += 1
