#global sets
softball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', "Carmen", 'Alicia', 'Sarah'])

#header softball players
print('The following students are on the softball team:')
#for loop to abtain names
for player in softball:
    print(player)
    
print()
#header basketball players
print('The following students are on the basketball team:')
#loop for names
for player in basketball:
    print(player)
    
print()
#header basketball and softball only
print('The following students play both softball AND basketball:')
#intersection
bask_soft = basketball.intersection(softball)
#loop
for player in bask_soft:
    print(player)
print()

#header for softball or basketball
print('The following students play either softball OR basketball:')
#union
combined = basketball.union(softball)
#loop
for player in combined:
    print(player)
print()

#header for softball but not basketball:
print('The following students play softball, BUT NOT basketball:')
#difference
onlysoft = softball.difference(basketball)
#loop
for player in onlysoft:
    print(player)
print()

#header for basketball but not softball
print('The following students play basketball, BUT NOT softball:')
#difference
onlybask = basketball.difference(softball)
#loop
for player in onlybask:
    print(player)
print()

#play one sport but not both
print('The following students play on sport, but not both:')
#symmetric
one_sport = basketball.symmetric_difference(softball)
#loop
for player in one_sport:
    print(player)
print()

