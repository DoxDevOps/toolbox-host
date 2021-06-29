import jwt
import qrcode

key = "secret"


class encrypt:
    def _init_(self, identifier, input_data):
        self.input_data = input_data
        self.identifier = identifier

    def encrypt_data(self, identifier, input_data):
        if len(identifier) < 1 and len(input_data) <1:
            return False
        encoded_jwt = jwt.encode({identifier: input_data}, key, algorithm="HS256")  # encrypt your data
        return encoded_jwt


class generate_qr_image:
    def _init_(self, input_data):
        self.input_data = input_data

    def add_qr_data(self, input_data):
        if not input_data:
            return False
        # Create QR Code Instance. It determines the size of the QR code
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(input_data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save('templates/static/images/toolbox.png')
        return True
