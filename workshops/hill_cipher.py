"""
    TEST CASES
    -> Encrypt:
        Plain text: 'JULY'
        Keyword: [[11, 8], [3, 7]]
        Output: DELW
    -> Decrypt:
        Cipher text: 'VKFZRVWTIAZSMISGKA'
        Keyword: [[11, 8], [3, 7]]
        Output: NUMBERTHEORYISEASY
"""

letters = 'abcdefghijklmnopqrstuvwxyz'

def det(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def adj(matrix):
    return [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gcde(a, b):
    if b == 0:
        return (a, 1, 0)
    d_p, x_p, y_p = gcde(b, a % b)
    return (d_p, y_p, x_p - (a // b) * y_p)

def check(matrix):
    if det(matrix) == 0:
        print('El determinante de la matriz es 0, por tanto no es invertible')
        return False
    if gcd(det(matrix), 26) != 1:
        print('El determinante de la matriz no es coprimo con 26, por tanto no es invertible')
        return False
    return True

def mult(v, k):
    return ((k[0][0] * v[0] + k[1][0] * v[1]) % 26, (k[0][1] * v[0] + k[1][1] * v[1]) % 26)

def encrypt(plain_text, keyword):
    cipher_text = ''
    for index in range(0, len(plain_text), 2):
        m = [letters.find(plain_text[index].lower()), letters.find(plain_text[index + 1].lower())]
        c = mult(m, keyword)
        cipher_text += letters[c[0]].upper() + letters[c[1]].upper()
    return cipher_text

def decrypt(cipher_text, keyword):
    plain_text = ''
    _, x, _ = gcde(det(keyword), 26)
    adj_matrix = adj(keyword)
    inv_matrix = [[0, 0], [0, 0]]
    print('Matriz inversa:')
    for i in range(2):
        row = '|'
        for j in range(2):
            inv_matrix[i][j] = (x * adj_matrix[i][j]) % 26
            row += str(inv_matrix[i][j]) + '\t'
        print(row.strip() + '|')
    for index in range(0, len(cipher_text), 2):
        c = [letters.find(cipher_text[index].lower()), letters.find(cipher_text[index + 1].lower())]
        m = mult(c, inv_matrix)
        plain_text += letters[m[0]].upper() + letters[m[1]].upper()
    return plain_text

def read_keyword():
    print('Ingrese la clave (matriz 2x2):')
    keyword = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            keyword[i][j] = int(input(f'K[{i}][{j}] = '))
    return keyword

def print_matrix(matrix):
    print('Matriz ingresada:')
    for i in range(2):
        row = '|'
        for j in range(2):
            row += str(matrix[i][j]) + '\t'
        print(row.strip() + '|')

def main():
    print('Hill Cipher')
    print('1. Cifrar')
    print('2. Descifrar')
    option = int(input('Ingrese la opción: '))
    if option < 1 or option > 2:
        print('Opción incorrecta')
    elif option == 1:
        plain_text = input('Ingrese el mensaje en texto claro: ')
        keyword = read_keyword()
        print_matrix(keyword)
        if not check(keyword):
            return
        cipher_text = encrypt(plain_text.replace(' ', ''), keyword)
        print(f'\nMensaje cifrado: {cipher_text.strip()}')
    elif option == 2:
        cipher_text = input('Ingrese el mensaje cifrado: ')
        keyword = read_keyword()
        print_matrix(keyword)
        if not check(keyword):
            return
        plain_text = decrypt(cipher_text.replace(' ', ''), keyword)
        print(f'\nMensaje descifrado: {plain_text.strip()}')

if __name__ == '__main__':
    main()