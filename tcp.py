#!/usr/bin/python

from random import random

class Gambler:
  def __init__(self, wallet = 0):
    self.wallet = wallet
    self.initial = wallet / 20
    self.memory = 0
    self.state = None

  def gamble(self):
    """Determine how monies"""
    if self.state is None:
      gambled = self.initial
    elif self.state is 'grow':
      gambled = self.memory * 2
    elif self.state is 'half':
      gambled = self.memory / 2
    elif self.state is 'linear':
      gambled = self.memory + self.initial

    gambled = round(gambled)

    if gambled > self.wallet:
      gambled = self.wallet

    return gambled

  def spend(self, gambled = 0):
    """Give monies"""
    self.memory = gambled
    self.wallet -= gambled

  def earn(self, winnings):
    """Receive monies"""
    self.wallet += winnings
    self.react(winnings)

  def react(self, winnings):
    if winnings > 0:
      if self.state is None or self.state is 'grow':
        self.state = 'grow'
      else:
        self.state = 'linear'
    else:
      self.state = 'half'
    
  def exits(self):
    return self.wallet > self.initial * 29 

class Casino:
  def __init__(self, minimum_gamble = 5):
    self.minimum_gamble = minimum_gamble

  def is_valid_gambler(self, gambler):
    """Bouncer"""
    if gambler.wallet < self.minimum_gamble:
      return False
    return True

  def play(self, gambled):
    """Represents total return for play"""
    return self.play_game() * 2 * gambled
      
  def play_game(self):
    """Represents if during a play the result was a win or loss"""
    card = random()
    if card > 0.5055:
      return 1
    return 0

###

casino = Casino(1)
counters = []
maxers = []
enders = []

total_plays = 100
initial = 20

for i in xrange(total_plays):
  gambler = Gambler(initial)
  counter = 0
  maximum = 0

  while not gambler.exits() and casino.is_valid_gambler(gambler):
    gambled = gambler.gamble()

    if gambled <= 0:
      print " Gambled 0 - quit"
      break

    if gambled < casino.minimum_gamble:
      gambled = casino.minimum_gamble

    gambler.spend(gambled)
    earned = casino.play(gambled)
    gambler.earn(earned)

    if gambler.wallet > maximum:
      maximum = gambler.wallet

    print " Gambling %3d - earned %3d - has %4d" % \
      (gambled, earned, gambler.wallet)
    counter += 1

  counters.append(counter)
  maxers.append(maximum)

  enders.append(gambler.wallet - initial)

  print "played %d, max %d" % (counter, maximum)

enders_count = len(filter(lambda x: x > 0, enders))

print "average play length: %f" % (float(sum(counters)) / len(counters))
print "average max: %f - max max: %d" % (float(sum(maxers)) / len(maxers), max(maxers))
print "winning plays: %d / %d" % (enders_count, total_plays)
print "outcome: %d ($%d)" % (sum(enders), sum(enders) * 5)
