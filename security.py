alphabet='abcdefghijklmnopqrstuvwxyz'
key=4

newmsg=' '
message=input('enter the text')

for character in message:
    position = alphabet.find(character)
    newposition = (position+key)%26
    newchar = alphabet(newposition)
    print('encrypted new character is',newchar)
    newmsg+=newchar
print('The final message is',newmsg)    
