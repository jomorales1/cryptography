"""
    TEST CASES
    -> Encrypt:
        Plain text: 'WE WILL ATTACK AT DAWN THE LEFT FLANK'
        Parameter k: 3
        Output: ZHZLO ODWWD FNDWG DZQWK HOHIW IODQN
    -> Decrypt:
        Cipher text: 'WKLVL VHAWU HPHOB LQVHF XUHHQ FUBSW LRQGR QRWXV HLWWR SURWH FWYDO XDEOH LQIRU PDWLR Q'
        Parameter k: 3
        Output: THISI SEXTR EMELY INSEC UREEN CRYPT IONDO NOTUS EITTO PROTE CTVAL UABLE INFOR MATIO N
"""

letters = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plain_text, k):
    cipher_text = ''
    separator = 0
    for letter in plain_text.lower():
        if letter not in letters:
            continue
        l_index = letters.find(letter)
        cipher_text += letters[(l_index + k) % 26].upper()
        separator += 1
        if separator % 5 == 0:
            cipher_text += ' '
    return cipher_text

def decrypt(cipher_text, k):
    plain_text = ''
    separator = 0
    for letter in cipher_text.lower():
        if letter not in letters:
            continue
        l_index = letters.find(letter)
        plain_text += letters[(l_index - k) % 26].upper()
        separator += 1
        if separator % 5 == 0:
            plain_text += ' '
    return plain_text

def main():
    print('Caesar Cipher')
    print('1. Cifrar')
    print('2. Descifrar')
    option = int(input('Ingrese la opción: '))
    if option < 1 or option > 2:
        print('Opción incorrecta')
    elif option == 1:
        plain_text = input('Ingrese el mensaje en texto claro: ')
        k = int(input('Ingrese el parametro k: '))
        cipher_text = encrypt(plain_text, k)
        print(f'\nMensaje cifrado: {cipher_text}')
    elif option == 2:
        cipher_text = input('Ingrese el mensaje cifrado: ')
        k = int(input('Ingrese el parametro k: '))
        plain_text = decrypt(cipher_text, k)
        print(f'\nMensaje descifrado: {plain_text}')

if __name__ == '__main__':
    main()