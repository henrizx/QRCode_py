import qrcode

def generate_vcard_qr_code(name, number, email, website, filename):
    vcard_data = f"BEGIN:VCARD\nVERSION:3.0\nN:{name}\nTEL:{number}\nEMAIL:{email}\nURL:{website}\nEND:VCARD"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Exemplo de uso
name = "Antônio Jose de Souza"
number = "+5519992584548"
email = "toninho@tfdistribuicao.com.br"
website = "https://tfdistribuicao.com.br/"
filename = "vcard_qrcode.png"

generate_vcard_qr_code(name, number, email, website, filename)
print("QR code do VCard gerado com sucesso.")