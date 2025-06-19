from PIL import Image

def encode_text(image_path, output_path, message):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    message += '###'  # End-of-message marker
    msg_index = 0

    for row in range(height):
        for col in range(width):
            if msg_index < len(message):
                r, g, b = img.getpixel((col, row))
                ascii_val = ord(message[msg_index])
                new_pixel = (r, g, ascii_val)
                encoded.putpixel((col, row), new_pixel)
                msg_index += 1
            else:
                break
    encoded.save(output_path)
    print(f"Text hidden successfully in {output_path}!")

if __name__ == "__main__":
    input_img = "input.png"
    output_img = "output.png"
    secret_msg = "hi,Aasritha"
    encode_text(input_img, output_img, secret_msg)
