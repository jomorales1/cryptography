"""
    TEST CASES
    -> Encrypt:
        Plain text: 'THIS SECRET MESSAGE IS ENCRYPTED'
        Keyword: 'YOAN PINZON'
        Output: WE DL LK HW LY LF XP QP HF DL HY HW OY YL KP
    -> Decrypt:
        Cipher text: 'WE DL LK HW LY LF XP QP HF DL HY HW OY YL KP'
        Keyword: 'YOAN PINZON'
        Output: TH [IJ]S SE CR ET ME SX SA GE [IJ]S EN CR YP TE DX
"""

letters = 'abcdefghijklmnopqrstuvwxyz'

def construct_matrix(keyword):
    positions = {}
    matrix = [[], [], [], [], []]
    row, col = 0, 0
    seen = {}
    for letter in letters:
        seen[letter] = False
    for letter in keyword.lower() + letters:
        if seen[letter]:
            continue
        if letter == 'i' or letter == 'j':
            positions['i'] = (row, col)
            positions['j'] = (row, col)
            matrix[row].append('[ij]')
            seen['i'] = True
            seen['j'] = True
        else:
            positions[letter] = (row, col)
            matrix[row].append(letter)
            seen[letter] = True
        col += 1
        if col == 5:
            row += 1
            col = 0
    print('\nMatriz generada:')
    for line in matrix:
        print(line)
    return positions, matrix

def encrypt(plain_text, keyword):
    plain_text = ''.join([letter for letter in plain_text.lower() if letter in letters])
    formatted = ''
    for index in range(0, len(plain_text) - 1, 2):
        formatted = formatted + plain_text[index].lower()
        if plain_text[index] == plain_text[index + 1]:
            formatted = formatted + 'x'
        formatted = formatted + plain_text[index + 1].lower()
    if len(formatted) % 2 != 0:
        formatted = formatted + 'x'
    keyword = ''.join([letter for letter in keyword.lower() if letter in letters])
    positions, matrix = construct_matrix(keyword)
    cipher_text = ''
    for index in range(0, len(formatted), 2):
        first = positions[formatted[index]]
        second = positions[formatted[index + 1]]
        if first[0] == second[0]:
            cipher_text += matrix[first[0]][(first[1] + 1) % 5]
            cipher_text += matrix[second[0]][(second[1] + 1) % 5]
        elif first[1] == second[1]:
            cipher_text += matrix[(first[0] + 1) % 5][first[1]]
            cipher_text += matrix[(second[0] + 1) % 5][second[1]]
        else:
            cipher_text += matrix[first[0]][second[1]]
            cipher_text += matrix[second[0]][first[1]]
    return cipher_text

def decrypt(cipher_text, keyword):
    cipher_text = ''.join([letter for letter in cipher_text.lower() if letter in letters])
    keyword = ''.join([letter for letter in keyword.lower() if letter in letters])
    if len(cipher_text) % 2 != 0:
        print('\nError: mensaje incompleto')
        return ''
    positions, matrix = construct_matrix(keyword)
    plain_text = ''
    for index in range(0, len(cipher_text), 2):
        first = positions[cipher_text[index]]
        second = positions[cipher_text[index + 1]]
        if first[0] == second[0]:
            plain_text += matrix[first[0]][(first[1] - 1) % 5]
            plain_text += matrix[second[0]][(second[1] - 1) % 5]
        elif first[1] == second[1]:
            plain_text += matrix[(first[0] - 1) % 5][first[1]]
            plain_text += matrix[(second[0] - 1) % 5][second[1]]
        else:
            plain_text += matrix[first[0]][second[1]]
            plain_text += matrix[second[0]][first[1]]
        plain_text += '-'
    return plain_text

def main():
    print('Playfair Cipher')
    print('1. Cifrar')
    print('2. Descifrar')
    option = int(input('Ingrese la opción: '))
    if option < 1 or option > 2:
        print('Opción incorrecta')
    elif option == 1:
        plain_text = input('Ingrese el mensaje en texto claro: ')
        keyword = input('Ingrese la clave: ')
        cipher_text = encrypt(plain_text, keyword)
        result = ''
        for index in range(0, len(cipher_text), 2):
            result += cipher_text[index : index + 2].upper() + ' '
        print(f'\nMensaje cifrado: {result.strip()}')
    elif option == 2:
        cipher_text = input('Ingrese el mensaje cifrado: ')
        keyword = input('Ingrese la clave: ')
        plain_text = decrypt(cipher_text, keyword)
        result = ' '.join([part.upper() for part in plain_text.split('-') if part])
        if plain_text:
            print(f'\nMensaje descifrado: {result.strip()}')

if __name__ == '__main__':
    main()