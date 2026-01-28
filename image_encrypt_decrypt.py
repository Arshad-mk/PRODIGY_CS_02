from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def select_image():
    """
    Opens a file picker so the user can select an image easily.
    """
    Tk().withdraw()  # Hide tkinter main window
    file_path = askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )
    return file_path


def encrypt_decrypt_image(input_path, output_path, key, mode):
    """
    Encrypts or decrypts an image by shifting RGB pixel values.
    """

    # Open image and convert to RGB format
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()

    width, height = img.size

    # Loop through every pixel in the image
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Encrypt: Add key value
            if mode == "E":
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256

            # Decrypt: Subtract key value
            elif mode == "D":
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256

            # Update pixel value
            pixels[x, y] = (r, g, b)

    # Save the output image
    img.save(output_path)
    print("✅ Output saved as:", output_path)


# ---------------- MAIN PROGRAM ---------------- #

print("\n--- Image Encryption & Decryption Tool (Task 2) ---")

# Select image file
print("📌 Please select an image file...")
input_file = select_image()

if not input_file:
    print("❌ No file selected. Exiting program.")
    exit()

print("✅ Selected File:", input_file)

# Input key
key = int(input("Enter secret key (1–255): "))

# Validate key range
if key < 1 or key > 255:
    print("❌ Invalid key! Key must be between 1 and 255.")
    exit()

# Encryption or Decryption choice
choice = input("Type E for Encrypt or D for Decrypt: ").upper()

if choice == "E":
    encrypt_decrypt_image(input_file, "encrypted.png", key, "E")

elif choice == "D":
    encrypt_decrypt_image(input_file, "decrypted.png", key, "D")

else:
    print("❌ Invalid choice! Please enter E or D.")
