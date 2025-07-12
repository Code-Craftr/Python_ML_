alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt (original_text, shifting):
    shifted_text = ""
    original_text = original_text.lower()
    for letter in original_text:
        if letter not in alphabet:
            shifted_text += letter;
        else:
            shifted_position = (alphabet.index(letter) + (shifting))%26
            shifted_text += alphabet[shifted_position]
    print(f'your encrypted text is:  {shifted_text}')

def decrypt (encryted_texts, shifters):
    decrypted_text = ""
    encryted_texts = encryted_texts.lower()

    for ency in encryted_texts:
        if ency not in alphabet:
            decrypted_text += ency;
        else:
            shiters_position = (alphabet.index(ency) - shifters)%26
            decrypted_text += alphabet[shiters_position];
    print(f'The Decrypted version of your text is: {decrypted_text}')


texting = input('please enter the text you want to encrypt: ');
shifts = int(input('please enter the how much shifting you want: '))
encrypt(texting, shifts)


check = input('do you want to continue to decrytpion function? type yes or no: ')
 
if check == 'yes':
    provided = input('Please enter the text you want to decrypt: ')
    shifting = int(input('please enter the how much shifting is done in this text: '))
    decrypt(provided, shifting)
