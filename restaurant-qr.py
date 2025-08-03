import qrcode
from PIL import Image

# Step 1: QR code data and setup
menu_url = "https://palash-developer.github.io/refresh-cafe/"
qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(menu_url)
qr.make(fit=True)

# Step 2: Generate the QR code image
qr_img = qr.make_image(fill_color="darkgreen", back_color="white").convert('RGB')

# Step 3: Load and resize logo
logo = Image.open("logo.jpg")

# Calculate size and position
qr_width, qr_height = qr_img.size
logo_size = qr_width // 4
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

# Calculate position to paste the logo
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# Step 4: Paste the logo onto the QR code
qr_img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

# Step 5: Save the final QR code
qr_img.save("refresh_cafe_qr_with_logo.png")

print("✅ QR code with logo saved as refresh_cafe_qr_with_logo.png")
