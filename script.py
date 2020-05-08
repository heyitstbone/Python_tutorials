meal = 44.50
tax = float(6.75) / 100
tip = float(15.0) / 100
meal += meal * tax
total = meal + meal * tip
print total 