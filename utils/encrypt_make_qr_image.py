import jwt
import qrcode

key = "secret"


class encrypt:
    def _init_(self, identifier, input_data):
        self.input_data = input_data
        self.identifier = identifier

    def encrypt_data(self):
        encoded_jwt = jwt.encode({self.identifier: self.input_data}, key, algorithm="HS256")  # encrypt your data
        generate_qr_image.add_qr_data(encoded_jwt)  # send data to the qr image
        # print(encoded_jwt)
        # print("****************************")


class generate_qr_image:
    def _init_(self, input_data):
        self.input_data = input_data

    def add_qr_data(self):
        # Create QR Code Instance. It determines the size of the QR code
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(self.input_data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save('templates/static/images/toolbox.png')
