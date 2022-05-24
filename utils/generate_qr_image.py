# coding=utf-8
import qrcode


def add_qr_data(input_data, image_location):
    """
    get data and create a qr image
    :param image_location: path to the image
    :param input_data: data to create a qr image
    :return: True if the qr image has been created or False when it has not been created
    """
    if not input_data:  # no data
        return False
    # Create QR Code Instance. It determines the size of the QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=15, border=4)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(image_location)
    return True
