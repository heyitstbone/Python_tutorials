""" This project is a calendar
    that will allow users to interact with it from the command line
"""
from time import sleep, strftime
USER_FIRST_NAME= "Travis"
calendar = {}
def welcome():
  print "Welcome, " + USER_FIRST_NAME + "." 
  print "Calendar is opening..."
  sleep (1) 
  print "Today is: " + strftime("%A %B %d %Y")
  print "The current time is: " + strftime( "%H:%M:%S")
  sleep (1) 
  print "What would you like to do?"
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to exit: ")
    user_choice = user_choice.upper()
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print "Calendar empty."
      else:
        print calendar
    elif user_choice == 'U':
        date = raw_input("What date? ")
        update = raw_input("Enter the update: ")
        calendar[date] = update
        print "Calendar update successful. "
        print calendar
    elif user_choice == 'A':
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")) :
        print "You have entered an invalid date. "
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper() 
        if try_again == 'Y':
          continue
        else:
          start = False 
      else:
        calendar[date] = event 
        print "The event was successfully added. "
        print calendar
    elif user_choice == 'D':
      if (len(calendar.keys())) < 1 :
        print "Calendar empty. "
      else:
        event = raw_input("What event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print "Event succesfully deleted. "
            print calendar 
          else:
            print "Incorrect event specified. "
    elif user_choice == 'X':
      start = False 
    else:
      print "An invalid command was entered. "
      start = False 
start_calendar()






