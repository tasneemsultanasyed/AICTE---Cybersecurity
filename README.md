# AICTE---Cybersecurity

# Image Encryption Script (Steganography)

This script embeds a secret message into an image file using the least significant bit (LSB) steganography technique. The message, along with an optional passcode, is encrypted into the pixel values of the image. The encrypted image is then saved as a new file.

### Prerequisites

To run this script, you'll need to have Python installed on your system along with the following libraries:
- OpenCV (`cv2`)

To install OpenCV, run:
```
pip install opencv-python
```

### Files

- **mypic.png**: The image file where the secret message will be hidden. (Make sure it's a PNG or other lossless format to avoid compression issues.)
- **passcode.txt**: A text file where the passcode is stored securely.
- **encryptedImage.png**: The output image file that contains the hidden message.

### How It Works

1. **Input**:
   - The user is prompted to enter a secret message that will be hidden in the image.
   - The user is also asked to enter a passcode, which is saved to a file (`passcode.txt`).

2. **Message Embedding**:
   - The length of the secret message is stored in the first 3 pixels of the image.
   - Each character of the message is then encoded into the pixel values, one by one, across the image in the order of BGR (Blue, Green, Red) channels.

3. **Output**:
   - The modified image, with the secret message embedded, is saved as `encryptedImage.png`.

### How to Use

1. Place the image file (`mypic.png`) in the same directory as the script or update the path in the script.
2. Run the script:
   ```
   python steganography_script.py
   ```
3. When prompted, input your secret message and passcode.

4. The encrypted image will be saved as `encryptedImage.png`, and the passcode will be saved in `passcode.txt`.

### Example

Here’s an example of the input and output:

#### Input:
```
Enter the secret message: Hello, World!
Enter the passcode: 12345
```

#### Output:
- `encryptedImage.png`: The image with the secret message embedded.
- `passcode.txt`: The file containing the passcode `12345`.

### Notes
- The image needs to be large enough to hold the message. If the image is too small, you may encounter errors. Ensure your image has enough pixels to store both the message and its length.
- This method uses a basic form of encryption and should not be relied on for highly sensitive data.

### Future Improvements

- **Enhanced Security**: The current method of embedding the message is relatively simple. Future improvements may include encrypting the message with algorithms like AES before hiding it in the image.
- **Larger Messages**: Handle larger messages and allow for multi-layer steganography or multi-image hiding.

### Troubleshooting

**Error**: "Image not found or failed to load."

- Ensure the file path to the image (`mypic.png`) is correct.
- Check if OpenCV can read the image format (PNG, JPG, etc.).

**Error**: "Image too small to hide the message!"

- Make sure your image has enough pixels to hold both the message length and the characters of the secret message.
