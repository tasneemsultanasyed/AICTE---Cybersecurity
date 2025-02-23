import cv2

# Load the image
image = cv2.imread("mypic.png")  # Use a lossless format (PNG) to avoid compression issues

# Get user inputs
secret_message = input("Enter the secret message: ")
passcode = input("Enter a passcode: ")

# Save the passcode to a file (optional, for secure storage)
with open("passcode.txt", "w") as f:
    f.write(passcode)

# Variables to track pixel positions
row, col, color_channel = 0, 0, 0

# Embed the length of the secret message into the first few pixels
message_length = len(secret_message)
for i in range(3):  # Use the first 3 pixels to store the length of the message
    image[row, col, color_channel] = (message_length >> (8 * i)) & 0xFF
    row += 1
    col += 1
    color_channel = (color_channel + 1) % 3  # Change color channel (0,1,2 for BGR)

# Reset pixel positions after storing the message length
row, col, color_channel = 3, 3, 0  # Start embedding the message after the first 3 pixels

# Encrypt message into the image
for char in secret_message:
    image[row, col, color_channel] = ord(char)  # Convert character to ASCII number
    row += 1
    col += 1
    color_channel = (color_channel + 1) % 3  # Change color channel (0,1,2 for BGR)

# Save the encrypted image in a lossless format (PNG)
cv2.imwrite("encryptedImage.png", image)
print("Encryption complete. Encrypted image saved as 'encryptedImage.png'.")
