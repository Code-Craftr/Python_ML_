alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#def encrypt(original_text, shift_amount)
name = 'Manankush!'
name = name.lower()
shift = 3
cyphered_text = []

for Letters in name:
    if Letters in alphabet:
        indexes = alphabet.index(Letters)
        indexes += shift;
        cyphered_text.append(alphabet[indexes])
        print(alphabet[indexes])


print(''.join(cyphered_text))

