def counter(num):
  for i in range(int(num)):
    print(str(i+1))

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
    counter(num)
  else:
    print('sure')