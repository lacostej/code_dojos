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

#### infrastructure

def assertEquals(o1, o2):
  print str(o1) + " - " + str(o2)
  assert o1 == o2
