import jwt

from utils.decrypt import decrypt_data
from utils.generate_qr_image import add_qr_data
key = "secret"


def encrypt_data(identifier, input_data):
    encoded_jwt = jwt.encode({identifier: input_data}, key, algorithm="HS256")  # encrypt your data
    add_qr_data(encoded_jwt)  # send data to the qr image
    # print(encoded_jwt)
    # print("****************************")
    # decrypt_data(encoded_jwt)
