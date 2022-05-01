"""
    TEST CASES
    -> Encrypt:
        Plain text: 'JIM ATTACKS AT DAWN'
        Matrix size: 4
        Direction: 0
        Holes: [(0, 0), (2, 1), (2, 3), (3, 2)]
        Output: JKTD SAAT WIAM CNAT
    -> Decrypt:
        Cipher text: 'JKTD SAAT WIAM CNAT'
        Matrix size: 4
        Direction: 0
        Holes: [(0, 0), (2, 1), (2, 3), (3, 2)]
        Output: JIMA TTAC KSAT DAWN
    -> Encrypt:
        Plain text: 'THIS IS A MESSAGE THAT I AM ENCRYPTING WITH A TURNING GRILLE TO PROVIDE THIS ILLUSTRATIVE EXAMPLE'
        Matrix size: 9
        Direction: 0
        Holes: [(0, 0), (0, 3), (0, 5), (1, 2), (1, 8), (2, 1), (2, 6), (3, 2), (3, 4), (3, 7), (4, 4), (4, 6), (4, 8), (5, 3), (5, 7), (6, 0), (6, 5), (7, 1), (7, 4), (7, 8), (8, 2)]
        Output: TESHN INCIG LSRGY LRIUS PITSA TLILM REENS ATTOG SIAWG IPVER TOTEH HVAEA XITDT UAIME RANPM TLHIE I
    -> Decrypt:
        Cipher text: 'TESHN INCIG LSRGY LRIUS PITSA TLILM REENS ATTOG SIAWG IPVER TOTEH HVAEA XITDT UAIME RANPM TLHIE I'
        Matrix size: 9
        Direction: 0
        Holes: [(0, 0), (0, 3), (0, 5), (1, 2), (1, 8), (2, 1), (2, 6), (3, 2), (3, 4), (3, 7), (4, 4), (4, 6), (4, 8), (5, 3), (5, 7), (6, 0), (6, 5), (7, 1), (7, 4), (7, 8), (8, 2)]
        Output: THIS IS A MESSAGE THAT I AM ENCRYPTING WITH A TURNING GRILLE TO PROVIDE THIS ILLUSTRATIVE EXAMPLE
"""

def rotate(row, col, matrix_size, direction):
    if direction == 0:
        return matrix_size - 1 - col, row
    return col, matrix_size - 1 - row

def encrypt(plain_text, matrix_size, direction, holes):
    cipher_text = ''
    matrix = []
    for i in range(matrix_size):
        matrix.append(['' for j in range(matrix_size)])
    plain_text = plain_text.replace(' ', '')
    current = 0
    for step in range(4):
        if step > 0:
            holes = [rotate(hole[0], hole[1], matrix_size, direction) for hole in holes]
        holes.sort()
        for hole in holes:
            if matrix[hole[0]][hole[1]] != '':
                continue
            matrix[hole[0]][hole[1]] = plain_text[current].upper()
            current += 1
    count = 0
    for i in range(matrix_size):
        for j in range(matrix_size):
            cipher_text += matrix[i][j]
            count += 1
            if count % len(holes) == 0:
                cipher_text += ' '
    return cipher_text

def decrypt(cipher_text, matrix_size, direction, holes):
    plain_text = ''
    matrix = []
    cipher_text = cipher_text.replace(' ', '')
    pos = 0
    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            row.append(cipher_text[pos])
            pos += 1
        matrix.append(row)
    count = 0
    for step in range(4):
        if step > 0:
            holes = [rotate(hole[0], hole[1], matrix_size, direction) for hole in holes]
        holes.sort()
        for index in range(len(holes)):
            plain_text += matrix[holes[index][0]][holes[index][1]]
        plain_text += ' '
    return plain_text

def read_holes():
    n_holes = int(input('Ingrese el numero de agujeros: '))
    holes = []
    print('Ingrese las posiciones de cada agujero (0 based indexing):')
    for i in range(n_holes):
        print(f'Agujero {str(i + 1)}')
        row = int(input('Fila: '))
        col = int(input('Columna: '))
        holes.append((row, col))
    return holes

def main():
    print('Turning Grill Cipher')
    print('1. Cifrar')
    print('2. Descifrar')
    option = int(input('Ingrese la opción: '))
    if option < 1 or option > 2:
        print('Opción incorrecta')
    elif option == 1:
        plain_text = input('Ingrese el mensaje en texto claro: ')
        matrix_size = int(input('Ingrese el tamaño de la matriz: '))
        direction = int(input('Ingrese la rotación de la rotacion: '))
        holes = read_holes()
        cipher_text = encrypt(plain_text, matrix_size, direction, holes)
        print(f'\nMensaje cifrado: {cipher_text.strip()}')
    elif option == 2:
        cipher_text = input('Ingrese el mensaje cifrado: ')
        matrix_size = int(input('Ingrese el tamaño de la matriz: '))
        direction = int(input('Ingrese la rotación de la rotacion: '))
        holes = read_holes()
        plain_text = decrypt(cipher_text, matrix_size, direction, holes)
        print(f'\nMensaje descifrado: {plain_text.strip()}')

if __name__ == '__main__':
    main()