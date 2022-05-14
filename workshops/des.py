import base64
import io
import pyDes

def main(filename):
    with open(filename, 'rb') as image_file:
        image_bytes = io.BytesIO(image_file.read())
    des = pyDes.des('some key')
    encrypted = des.encrypt(image_bytes.getvalue(), padmode=pyDes.PAD_PKCS5)
    base64_data = base64.b64encode(encrypted)
    print(base64_data)
    encrypted_bytes = base64.b64decode(base64_data)
    decrypted = des.decrypt(encrypted_bytes)
    new_filename = 'decryted_' + filename
    with open(new_filename, 'wb') as image_file:
        image_file.write(decrypted)

if __name__ == '__main__':
    fname = input('Ingrese el nombre del archivo incluyendo su extensión: ')
    main(fname)