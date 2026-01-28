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
            if mode

