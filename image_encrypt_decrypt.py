from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def select_image():
    """Open file picker to select an image"""
    Tk().withdraw()  # Hide tkinter window
    file_path = askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )
    return file_path


def encrypt_decrypt_image(input_path, output_path, key, mode):
    """Encrypt or decrypt an image using pixel manipulation"""

    img = Image.open(input_path).convert("RGB")
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            if mode == "E":  # Encrypt
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256

            elif mode == "D":  # Decrypt
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256

            pixels[x, y] = (r, g, b)

    img.save(output_path)
    print("✅ Output saved as:", output_path)


# ---------------- MAIN PROGRAM ---------------- #

print("\n--- Image Encryption Tool (Task 2) ---")

print("📌 Select an image file...")
input_file = select_image()

if not input_file:
    print("❌ No file selected. Exiting.")
    exit()

print("✅ Selected File:", input_file)

key = int(input("Enter secret key (1–255): "))
choice = input("Type E for Encrypt or D for Decrypt: ").upper()

if choice == "E":
    encrypt_decrypt_image(input_file, "encrypted.png", key, "E")

elif choice == "D":
    encrypt_decrypt_image(input_file, "decrypted.png", key, "D")

else:
    print("❌ Invalid choice. Please enter E or D.")
