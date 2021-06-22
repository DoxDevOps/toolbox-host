import jwt

from utils.generate_qr_image import add_qr_data
key = "secret"


def decrypt_data(input_data):
    decoded_jwt = jwt.decode(input_data, "secret", algorithms="HS256")  # encrypt your data
    add_qr_data(decoded_jwt)
    print(decoded_jwt)
