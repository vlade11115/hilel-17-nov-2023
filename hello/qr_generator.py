import io

import qrcode


def generate_qr(text):
    file_holder = io.BytesIO()
    img = qrcode.make(text)
    img.save(file_holder)
    file_holder.seek(0)
    return file_holder
