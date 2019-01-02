rent = int (raw_input("What's the rent ?"))

"""
if rent > 2000 :
    print "Its not affordable"
elif rent == 2000 :
    print "Partially affordable"
else:
    print "Affordable"

#ternary

affordable = True if (rent <= 2000) else False

print affordable
"""
# while loop
while (rent >= 2000):
    print "Rent " + str (rent) + " is not affordable"
    rent = rent - 100

print "Rent " + str (rent) + " is affordable"