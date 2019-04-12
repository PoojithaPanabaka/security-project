# security-project
both encryption and decryption of the text given by the user

A text will be given by the user and that text is encrypted into a code which takes the next fourth alphabet of that respective alphabet


1   2   3   4   5   6   7   8   9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26  
A   B   C   D   E   F   G   H   I   J    K    L    M    N    O    P    Q    R    S    T    U    V    W    X    Y    Z


for example:

Text : Hello
encryption : H=8
           8+4=12
           12=L
           therefore,H=L
           similarly,E=I
                     L=P
                     L=P
                     O=S
                     
In the same way the decryption of the text is done by substracting 4 from the text.

for example:

Text : Lipps
decryption : L=12
             12-4=8
             8=H
             therefore,L=H
             similarly,I=E
                       P=L
                       P=L
                       S=O
                   
 This can be done by the code :
 Alphabet = "abcdefghijklmnopqrstuvwxyz"
 Key=4
 
 position = alphabet.find(character)
 newposition = (position+key)%26
 
