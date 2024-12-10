import qrcode
import sys

def generer(donnees):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(donnees)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode.png')
    print("\n[INFO] QR Code généré avec succès : 'qrcode.png'\n")

if len(sys.argv) > 1 and sys.argv[1]:
    generer(sys.argv[1])