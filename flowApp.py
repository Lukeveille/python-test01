while True:
  print('enter a word:')
  word = input()
  if word == 'yes':
    print('That\'s the magic word!')
    break
  elif  word == 'no':
    print('Okay...')
    break
  elif word == 'count':
    num = input()
    for i in range(int(num)+1):
      print(str(i))
  else:
    print('sure')