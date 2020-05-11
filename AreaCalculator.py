""" This program will create a calculator that computes the area of either a circle or a triangle and then display the area of the shape to the user
"""
print ("Starting Calculator")
option = raw_input("Enter C for Circle or T for Triangle:")
if option == "C": 
  radius = float(raw_input("Enter radius"))
  area = 3.14159 * radius**2
  print "Area %f" % area 
elif option == "T":
  base = float(raw_input("Enter base of triangle: "))
  height = float(raw_input("Enter height of triangle: "))
  area = .5 * base * height 
  print "Area %f" % area
else:
   print "Error! Invalid shape."
print "Exiting..."
