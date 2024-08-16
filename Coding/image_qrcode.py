import qrcode

def generate_qr_code(data, filename):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Generate QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save QR code image
    img.save(filename)

# Example usage:
data = "https://example.com"  # Data you want to encode in the QR code
filename = "batman.png"       # Output filename for the QR code image
generate_qr_code(data, filename)
print("QR code generated successfully.")
