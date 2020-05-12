"""this program will roll a pair of virtual dice and compare the user's guess against the number rolled"""
from random import randint
from time import sleep
def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum possible value is %d" % max_val
  guess = get_user_guess()
  if guess > max_val:
    print "That number is too big"
  else:
    print "Rolling..."
    sleep(2)
    print "The first roll is %d" % first_roll
    sleep(1)
    print "The second roll is %d" % second_roll
    total_roll = first_roll + second_roll
    sleep(2)
    print "Result...%d" % total_roll
    if total_roll == guess:
      print "Winner winner chicken dinner!"
    else:
      print "Sorry...better luck next time!"
 
roll_dice(20)
