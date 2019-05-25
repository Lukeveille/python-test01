def displayInventory(inventory):
  print('Inventory:')
  total = 0
  for k, v in inventory.items():
    total += v
    print(str(v) + ' ' + k)
  
  print('Total number of items: ' + str(total))

def addInventory(inventory, addedItems):
  newInventory = dict(inventory)
  for item in addedItems:
    newInventory.setdefault(item, 0)
    newInventory[item] += 1

  return newInventory


stuff = {'gold coin': 42, 'rope': 1}

displayInventory(stuff)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuff = addInventory(stuff, dragonLoot)
displayInventory(stuff)