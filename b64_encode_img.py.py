import base64

# Open the image file in binary read mode
with open('C:\\Users\\j1024z\\Desktop\\vtt_rt\\phish\\vtt_sig_logo.png', 'rb') as image_file:
    # Read the image file as binary data
    image_binary = image_file.read()
    # Encode the binary data as base64
    base64_encoded = base64.b64encode(image_binary).decode()

print(base64_encoded)
