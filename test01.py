def diver(div):
  try:
    return 256/div
  except ZeroDivisionError:
    print('Error: dun fukd up')
  
print(diver(2))
print(diver(3))
print(diver(0))
print(diver(16))