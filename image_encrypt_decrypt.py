from PIL import Image


def encrypt_decrypt_image(input_path, output_path, key, mode):
    """
    Encrypts or decrypts an image using simple pixel manipulation.
    """

    # Open image and convert to RGB
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()

    width, height = img.size

    # Loop through every pixel
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Encrypt: Add key
            if mode == "E":
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256

            # Decrypt: Subtract key
            elif mode == "D":
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256

            pixels[x, y] = (r, g, b)

    # Save the output image
    img.save(output_path)
    print("✅ Output saved as:", output_path)


# ---------------- MAIN PROGRAM ---------------- #

print("\n--- Image Encryption & Decryption Tool (Task 2) ---")

# User provides full image path
input_file = input("Enter full image path (example: /home/zoro/Pictures/img.png): ")

# Secret key input
key = int(input("Enter secret key (1–255): "))

if key < 1 or key > 255:
    print("❌ Invalid key! Key must be between 1 and 255.")
    exit()

# Choose operation
choice = input("Type E for Encrypt or D for Decrypt: ").upper()

if choice == "E":
    encrypt_decrypt_image(input_file, "encrypted.png", key, "E")

elif choice == "D":
    encrypt_decrypt_image(input_file, "decrypted.png", key, "D")

else:
    print("❌ Invalid choice! Please enter E or D.")
