import qrcode

# Create QR Code Instance. It determines the size of the QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)


def add_qr_data(input_data):
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('templates/static/images/toolbox.png')

