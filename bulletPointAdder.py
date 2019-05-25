import pyperclip

lines = pyperclip.paste().split('\n')
output = []

for i in range(len(lines)):
  lines[i] = '* ' + lines[i]

pyperclip.copy('\n'.join(lines))

print(lines)