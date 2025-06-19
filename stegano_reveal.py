from PIL import Image

def decode_text(image_path):
    img = Image.open(image_path)
    width, height = img.size
    message = ""

    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            char = chr(b)
            message += char
            if message.endswith('###'):
                print("Hidden Message:", message[:-3])
                return

if __name__ == "__main__":
    decode_text("output.png")
