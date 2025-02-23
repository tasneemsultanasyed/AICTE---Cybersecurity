import cv2

# Load the encrypted image
image = cv2.imread("encryptedImage.png")  # Use the same lossless format (PNG)

# Load the passcode from the file (optional, if you stored it during encryption)
with open("passcode.txt", "r") as f:
    original_passcode = f.read()

# Get user input for passcode
entered_passcode = input("Enter passcode for decryption: ")

if entered_passcode == original_passcode:  # Check if passcode is correct
    # Extract the length of the secret message from the first few pixels
    row, col, color_channel = 0, 0, 0
    message_length = 0
    for i in range(3):  # Read the first 3 pixels to get the length of the message
        byte_value = image[row, col, color_channel]
        message_length |= byte_value << (8 * i)
        row += 1
        col += 1
        color_channel = (color_channel + 1) % 3  # Change color channel (0,1,2 for BGR)

    # Reset pixel positions after reading the message length
    row, col, color_channel = 3, 3, 0  # Start decrypting the message after the first 3 pixels

    # Decrypt the message using the extracted length
    decrypted_message = ""
    for _ in range(message_length):  # Read same number of characters
        decrypted_char = chr(image[row, col, color_channel])  # Convert ASCII back to character
        decrypted_message += decrypted_char
        row += 1
        col += 1
        color_channel = (color_channel + 1) % 3  # Change color channel (0,1,2 for BGR)
    
    print("Decrypted message:", decrypted_message)
else:
    print("ACCESS DENIED! Incorrect passcode.")
