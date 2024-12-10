import qrcode

class CreerQR:

    def __init__(self, lien):
        self._lien = lien

    def generer(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self._lien)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.save('qrcode.png')

qr = CreerQR("guthib.com")
qr.generer()