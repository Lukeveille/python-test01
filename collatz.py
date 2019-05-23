def collatz(num):
  num = int(num)
  return num * 3 + 1 if num % 2 else int(num / 2)

number = input()

try:
  while number != 1:
    number = collatz(number)
    print(number)
except:
  print('Error: invalid input')
