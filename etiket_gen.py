import qrcode
from PIL import Image, ImageDraw

AD      = "DİNAR Novruzlu"
TELEFON = "+994993718881"
ƏŞYA    = "Açar dəsti"
MESAJ   = "Tapan bizimlə əlaxə saxlasın"

qr = qrcode.make(f"tel:{TELEFON}").resize((240, 240))

card = Image.new("RGB", (360, 480), "#1a1060")
draw = ImageDraw.Draw(card)

draw.rectangle([0, 0, 360, 44], fill="#ff3355")
draw.text((180, 22), "ITMİŞ ƏŞYA", fill="white", anchor="mm")
draw.text((180, 72), ƏŞYA, fill="white", anchor="mm")
draw.rounded_rectangle([40, 96, 320, 356], radius=16, fill="white")
card.paste(qr.convert("RGB"), (60, 108))
draw.text((180, 375), "QR oxudun - zeng acilir", fill="#7aa8ff", anchor="mm")
draw.text((180, 405), TELEFON, fill="white", anchor="mm")
draw.text((180, 432), f"Sahibi: {AD}", fill="#aac0ff", anchor="mm")
draw.text((180, 460), MESAJ, fill="#ffd050", anchor="mm")

card.save("etiket.png")
print("etiket.png hazirlanir!")