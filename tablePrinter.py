tableData = [
  ['apples', 'oranges', 'cherries', 'banana'],
  ['Alice', 'Bob', 'Carol', 'David'],
  ['dogs', 'cats', 'moose', 'goose']
]

def printTable(tableData):
  tableData = list(tableData)

  for i in range(len(tableData)):
    longest = len(max(tableData[i], key=len))

    for j in range(len(tableData[i])):
      tableData[i][j] = tableData[i][j].rjust(longest + 1)

  rows = len(max(tableData, key=len))
  for i in range(rows):
    line = ''
    for j in range(len(tableData)):
      line += tableData[j][i] + ' '

    print(line)

printTable(tableData)