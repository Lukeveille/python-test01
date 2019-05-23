for i in range(100):
  word = '' if i % 3 else 'fizz'
  word += '' if i % 5 else 'buzz'
  print(i if word == '' else word)