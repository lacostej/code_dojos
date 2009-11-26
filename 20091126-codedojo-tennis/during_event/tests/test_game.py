import unittest
from game import *

class TestTennisGame(unittest.TestCase):

  def setUp(self):
    self.g = TennisGame()

  def testStartGameWithEmptyScore(self):
    assertEquals("love-all", self.g.announceScore())

  def testThatSinglePointIsAnnounced(self):
    self.g.scorePlayerOne()
    assertEquals("fifteen-love", self.g.announceScore())

  def testThatSecondPointIsAnnounced(self):
    self.g.scorePlayerOne()
    self.g.scorePlayerOne()
    assertEquals("thirty-love", self.g.announceScore())

  def testThatPlayerTwoCanScore(self):
    self.g.scorePlayerTwo()
    self.g.scorePlayerTwo()
    assertEquals("love-thirty", self.g.announceScore())

  def testThatBothPlayersScoreTwice(self):
    self.g.scorePlayerOne()
    self.g.scorePlayerOne()
    self.g.scorePlayerTwo()
    self.g.scorePlayerTwo()
    assertEquals("thirty-all", self.g.announceScore())
    
  def testThatDeuceIsAnnounced(self):
    self.g.scorePlayerOne()
    self.g.scorePlayerOne()
    self.g.scorePlayerOne()
    self.g.scorePlayerTwo()
    self.g.scorePlayerTwo()
    self.g.scorePlayerTwo()
    assertEquals("deuce", self.g.announceScore())

  def testThatPlayersCanScoreThrice(self):
    self.g.scorePlayerOne(); self.g.scorePlayerOne(); self.g.scorePlayerOne()
    assertEquals("forty-love", self.g.announceScore())

  def testThatPlayerOneWinsGameAfterFourPoints(self):
    self.g.scorePlayerOne(); self.g.scorePlayerOne(); self.g.scorePlayerOne(); self.g.scorePlayerOne()
    assertEquals("game player one", self.g.announceScore())

  def testThatPlayerOneGetsAdvantage(self):
    self.g.scorePlayerOne(); self.g.scorePlayerOne(); self.g.scorePlayerOne()
    self.g.scorePlayerTwo(); self.g.scorePlayerTwo(); self.g.scorePlayerTwo()
    self.g.scorePlayerOne()
    assertEquals("advantage player one", self.g.announceScore())

  def testThatPlayerTwoWinsAfterDeuce(self):
    self.g.scorePlayerOne(); self.g.scorePlayerOne(); self.g.scorePlayerOne()
    self.g.scorePlayerTwo(); self.g.scorePlayerTwo(); self.g.scorePlayerTwo()
    self.g.scorePlayerTwo(); self.g.scorePlayerTwo()
    assertEquals("game player two", self.g.announceScore())

  def testThatPlayerTwoGetsAdvantage(self):
    self.scorePlayerTwo(3)
    self.g.scorePlayerOne(); self.g.scorePlayerOne(); self.g.scorePlayerOne()
    self.g.scorePlayerTwo()
    assertEquals("advantage player two", self.g.announceScore())

  def testThatPlayerOneGetsAdvantageAfterPlayerOneGetsAdvantage(self):
    pass
  
  def scorePlayerOne(self, times):
    for each in range(times):
      self.g.scorePlayerOne()

  def scorePlayerTwo(self, times):
    for each in range(times):
      self.g.scorePlayerTwo() 

#### infrastructure

def assertEquals(o1, o2):
  print str(o1) + " - " + str(o2)
  assert o1 == o2
