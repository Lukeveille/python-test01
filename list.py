stuff = []

while True:
  print('Enter thing #' + str(len(stuff)+1) + ':' )
  thing = input()

  if thing == '':
    break
  stuff = stuff + [thing]

print('The list:')
for things in stuff:
  print('  ' + things)