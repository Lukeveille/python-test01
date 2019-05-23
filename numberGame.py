import random
import sys
secretNumber = random.randint(1, 20)

print('I am thinking of a number between 1 and 20')

for count in range(1, 7):
  print('Take a guess.')
  guess = input()

  if guess == 'stop':
    sys.exit()
  elif int(guess) < secretNumber:
    print('Your guess is too low.')
    count += 1
  elif int(guess) > secretNumber:
    print('Your guess is too high')
    count += 1
  else:
    break

if int(guess) == secretNumber:
  print('Good job! You guessed my number in ' + str(count) + ' guesses!')
else:
  print('Nope. The number I was thinking of was ' + str(secretNumber))
