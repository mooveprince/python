states = {"Missouri" : "Jefferson City", "Tennesse" : "Nashville", "Florida" : "Tallahassee"}

states ["Ontario"] = "Toronto"

print states ["Tennesse"]

del states ["Missouri"]

for k,v in states.iteritems ():
    print k + "'s capital is " + v

