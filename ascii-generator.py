import os
from PIL import Image


ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
OUTPUT_PATH = "sample/"


def generator():
    path = input("Enter the path to the image file : \n")
    try:
        image = Image.open(path)
    except Exception as err:
        print(path, "Unable to find image ", err)
        return

    # resize image
    image = resize(image)
    # convert image to greyscale image
    greyscale_image = to_greyscale(image)
    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""

    # split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i + img_width] + "\n"

    # save the string to a file
    file_name = get_file_name(path)
    with open(OUTPUT_PATH + file_name + ".txt", "w") as f:
        f.write(ascii_img)


def get_file_name(path: str):
    _, tail = os.path.split(path)
    return tail.split(".")[0]


def resize(image: Image, new_width: int = 100):
    width, height = image.size
    new_height = new_width * height / width
    new_height = int(new_height)
    return image.resize((new_width, new_height))


def to_greyscale(image: Image):
    return image.convert("L")


def pixel_to_ascii(image: Image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str


if __name__ == "__main__":
    generator()
