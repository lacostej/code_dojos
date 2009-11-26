import unittest
from game import *

class TestTennisGame(unittest.TestCase):

  def setUp(self):
    self.g = TennisGame()

  def testStartGameWithEmptyScore(self):
    assertEquals("love-all", self.g.announceScore())

  def testThatSinglePointIsAnnounced(self):
    self.scorePlayerOne(1)
    assertEquals("fifteen-love", self.g.announceScore())

  def testThatSecondPointIsAnnounced(self):
    self.scorePlayerOne(2)
    assertEquals("thirty-love", self.g.announceScore())

  def testThatPlayerTwoCanScore(self):
    self.scorePlayerTwo(2)
    assertEquals("love-thirty", self.g.announceScore())

  def testThatBothPlayersScoreTwice(self):
    self.scorePlayerOne(2)
    self.scorePlayerTwo(2)
    assertEquals("thirty-all", self.g.announceScore())
    
  def testThatDeuceIsAnnounced(self):
    self.scorePlayerOne(3)
    self.scorePlayerTwo(3)
    assertEquals("deuce", self.g.announceScore())

  def testThatPlayersCanScoreThrice(self):
    self.scorePlayerOne(3)
    assertEquals("forty-love", self.g.announceScore())

  def testThatPlayerOneWinsGameAfterFourPoints(self):
    self.scorePlayerOne(4)
    assertEquals("game player one", self.g.announceScore())

  def testThatPlayerOneGetsAdvantage(self):
    self.scorePlayerOne(3)
    self.scorePlayerTwo(3)
    self.scorePlayerOne(1)
    assertEquals("advantage player one", self.g.announceScore())

  def testThatPlayerTwoWinsAfterDeuce(self):
    self.scorePlayerOne(3)
    self.scorePlayerTwo(5)
    assertEquals("game player two", self.g.announceScore())

  def testThatPlayerTwoGetsAdvantage(self):
    self.scorePlayerTwo(3)
    self.scorePlayerOne(3)
    self.scorePlayerTwo(1)
    assertEquals("advantage player two", self.g.announceScore())

  def testThatPlayerTwoGetsAdvantageAfterPlayerOneGetsAdvantage(self):
    self.scorePlayerTwo(3)
    self.scorePlayerOne(4)
    self.scorePlayerTwo(2)
    assertEquals("advantage player two", self.g.announceScore())

  def testThatSecondDeuceIsAnnounced(self):
    self.scorePlayerTwo(3)
    self.scorePlayerOne(4)
    self.scorePlayerTwo(2)
    self.scorePlayerOne(1)
    assertEquals("deuce", self.g.announceScore())
 
  
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
