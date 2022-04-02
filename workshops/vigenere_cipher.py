"""
    TEST CASES
    -> Encrypt:
        Plain text: 'TO BE OR NOT TO BE THAT IS THE QUESTION'
        Keyword: 'RELATIONS'
        Parameter t: 5
        Output: KSMEH ZBBLK SMEMP OGAJX SEJCS FLZSY
    -> Decrypt:
        Cipher text: 'KSMEH ZBBLK SMEMP OGAJX SEJCS FLZSY'
        Keyword: 'RELATIONS'
        Parameter t: 5
        Output: TOBEO RNOTT OBETH ATIST HEQUE STION
"""

letters = 'abcdefghijklmnopqrstuvwxyz'

def contruct_matrix():
    matrix = []
    positions = {}
    for index in range(len(letters)):
        row = []
        for index2 in range(index, len(letters) + index):
            row.append(letters[index2 % len(letters)].upper())
        matrix.append(row)
        positions[letters[index].upper()] = index
    return matrix, positions

def encrypt(plain_text, keyword, t):
    cipher_text = ''
    pos = 0
    matrix, positions = contruct_matrix()
    for letter in plain_text.lower():
        if letter not in letters:
            continue
        index = positions[letter.upper()]
        k_letter = keyword[pos % len(keyword)].upper()
        cipher_text += matrix[positions[k_letter]][index]
        pos += 1
        if pos % t == 0:
            cipher_text += ' '
    return cipher_text

def decrypt(cipher_text, keyword, t):
    plain_text = ''
    pos = 0
    matrix, positions = contruct_matrix()
    for letter in cipher_text.lower():
        if letter not in letters:
            continue
        k_letter = keyword[pos % len(keyword)].upper()
        index = (positions[letter.upper()] - positions[k_letter]) % len(letters)
        plain_text += letters[index].upper()
        pos += 1
        if pos % t == 0:
            plain_text += ' '
    return plain_text

def main():
    print('Vigenere Cipher')
    print('1. Cifrar')
    print('2. Descifrar')
    option = int(input('Ingrese la opción: '))
    if option < 1 or option > 2:
        print('Opción incorrecta')
    elif option == 1:
        plain_text = input('Ingrese el mensaje en texto claro: ')
        keyword = input('Ingrese la clave: ')
        t = int(input('Ingrese el parametro t: '))
        cipher_text = encrypt(plain_text, keyword, t)
        print(f'\nMensaje cifrado: {cipher_text.strip()}')
    elif option == 2:
        cipher_text = input('Ingrese el mensaje cifrado: ')
        keyword = input('Ingrese la clave: ')
        t = int(input('Ingrese el parametro t: '))
        plain_text = decrypt(cipher_text, keyword, t)
        print(f'\nMensaje descifrado: {plain_text.strip()}')

if __name__ == '__main__':
    main()