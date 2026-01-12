import qrcode
from PIL import Image
import os

def create_qr_with_logo(data, logo_path, save_path):
    """
    Generates a QR code. 
    'data' can now be a URL, Wi-Fi string, or vCard text.
    """
    # Use version=None so the QR code expands automatically for larger data (like vCards)
    qr = qrcode.QRCode(
        version=None, 
        error_correction=qrcode.constants.ERROR_CORRECT_H, 
        box_size=10, 
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create the base QR image
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Logic to add logo if a path is provided and valid
    if logo_path and os.path.exists(logo_path):
        try:
            logo = Image.open(logo_path)
            
            # Ensure logo is in a compatible mode (handles transparency better)
            if logo.mode != 'RGBA':
                logo = logo.convert('RGBA')
                
            qr_w, qr_h = qr_img.size
            
            # Calculate logo size (roughly 25% of QR)
            logo_size = qr_w // 4
            logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
            
            # Center the logo
            pos = ((qr_w - logo_size) // 2, (qr_h - logo_size) // 2)
            
            # Paste using the logo itself as a mask to support transparent PNGs
            qr_img.paste(logo, pos, mask=logo)
            
        except Exception as e:
            print(f"Logo Error: {e}")
            # If the logo fails, the function will still save the plain QR code

    qr_img.save(save_path)
    return qr_img
