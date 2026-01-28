# PRODIGY_CS_02 - Image Encryption and Decryption Using Pixel Manipulation

## Internship Task
This project is part of my **Cyber Security Internship at Prodigy InfoTech**.

Task 2: Develop a simple image encryption tool using pixel manipulation techniques.

---

## Concept
A digital image is made up of pixels, and each pixel contains RGB values:

- **Red (0–255)**
- **Green (0–255)**
- **Blue (0–255)**

This program encrypts an image by mathematically shifting pixel values using a secret key and decrypts it by reversing the operation.

---

## Features
- Encrypt an image using a numeric key  
- Decrypt the encrypted image back to its original form  
- Uses modular arithmetic to keep pixel values valid  
- Includes a **file picker option** for easy image selection (user-friendly)

---

## Requirements

This project uses the following Python libraries:

- **Pillow (PIL)** → Image processing and pixel manipulation  
- **Tkinter** → File picker for selecting images easily  

Install required packages on Kali Linux:

```bash
sudo apt install python3-pil python3-tk
```
How to Run
```
python3 image_encrypt_decrypt.py



