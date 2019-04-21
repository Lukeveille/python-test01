end = True
while end:
  print('enter a word:')
  word = input()
  if word == 'yes':
    print('That\'s the magic word!')
    end = False
  elif  word == 'no':
    print('Okay...')
    end = False
  else:
    print('sure')