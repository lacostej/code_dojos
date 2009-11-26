import unittest
from game import *

class TestTennisGame(unittest.TestCase):

  def setUp(self):
    self.g = TennisGame()

  def testStartGameWithEmptyScore(self):
    self.assertAnnouncement("love-all")

  def testThatSinglePointIsAnnounced(self):
    self.scorePlayerOne(1)
    self.assertAnnouncement("fifteen-love")

  def testThatSecondPointIsAnnounced(self):
    self.scorePlayerOne(2)
    self.assertAnnouncement("thirty-love")

  def testThatPlayerTwoCanScore(self):
    self.scorePlayerTwo(2)
    self.assertAnnouncement("love-thirty")

  def testThatBothPlayersScoreTwice(self):
    self.scorePlayerOne(2)
    self.scorePlayerTwo(2)
    self.assertAnnouncement("thirty-all")
    
  def testThatDeuceIsAnnounced(self):
    self.scorePlayerOne(3)
    self.scorePlayerTwo(3)
    self.assertAnnouncement("deuce")

  def testThatPlayersCanScoreThrice(self):
    self.scorePlayerOne(3)
    self.assertAnnouncement("forty-love")

  def testThatPlayerOneWinsGameAfterFourPoints(self):
    self.scorePlayerOne(4)
    self.assertAnnouncement("game player one")

  def testThatPlayerOneGetsAdvantage(self):
    self.scorePlayerOne(3)
    self.scorePlayerTwo(3)
    self.scorePlayerOne(1)
    self.assertAnnouncement("advantage player one")

  def testThatPlayerTwoWinsAfterDeuce(self):
    self.scorePlayerOne(3)
    self.scorePlayerTwo(5)
    self.assertAnnouncement("game player two")

  def testThatPlayerTwoGetsAdvantage(self):
    self.scorePlayerTwo(3)
    self.scorePlayerOne(3)
    self.scorePlayerTwo(1)
    self.assertAnnouncement("advantage player two")

  def testThatPlayerTwoGetsAdvantageAfterPlayerOneGetsAdvantage(self):
    self.scorePlayerTwo(3)
    self.scorePlayerOne(4)
    self.scorePlayerTwo(2)
    self.assertAnnouncement("advantage player two")

  def testThatSecondDeuceIsAnnounced(self):
    self.scorePlayerTwo(3)
    self.scorePlayerOne(4)
    self.scorePlayerTwo(2)
    self.scorePlayerOne(1)
    self.assertAnnouncement("deuce")
 
  def assertAnnouncement(self,expectedAnnouncement):
    assertEquals(expectedAnnouncement,self.g.announceScore())
  
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
