moonMass = 60
everyYear = 2 #pounds converted from kilo
newYear = moonMass

for x in range(1, 16):
    newYear = newYear + everyYear 
    print('My moon weight each year will be %s pounds on year %s' % (newYear, x))