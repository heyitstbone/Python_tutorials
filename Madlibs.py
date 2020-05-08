"""
This program generates passages that are generated in mad-lib format
Author: Travis 
"""

# The template for the story

STORY = """This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %ss in stores. They began to %s to the rhythm of the %s, which made all the %s very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."""

print "Our story begins like this: "
name = raw_input("Enter a name: ")
adj1 = raw_input("Enter an adjective: ")
adj2 = raw_input("Enter another adjective: ")
adj3 = raw_input("Enter one more adjective: ")
verb = raw_input("Now enter a verb: ")
noun1 = raw_input("Now enter a noun: ")
noun2 = raw_input("Enter one more noun please: ")
animal = raw_input("Give me an animal: ")
food = raw_input("Now give me the name of a food: ")
fruit = raw_input("What is your favorite fruit? ")
superhero = raw_input("Who is your favorite superhero? ")
country = raw_input("Now tell me the name of a country: ")
dessert = raw_input("Name a dessert: ")
year = raw_input("Finally, give me a year: ")

print STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, noun2)
