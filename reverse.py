space = ' '

name = input('Input the word or sentence to reverse it, write down verticaly and make the stairs. ')

reverse = ''

print('Reversed:')

for char in name:
    reverse = char + reverse
    
print(reverse)

print('Vertical:')

spellOut = ''

for char in name:
    spellOut = char + space
    print(spellOut)

print('Staris:')

stairs = ''

for char in name:
    stairs += char
    print(stairs)

