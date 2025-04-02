from PIL import Image


def changeBit(num: int, val: int):
    num = (num >> 1) << 1
    num |= val
    return num


def encodeImage(img_path: str, text: str) -> Image:
    with Image.open(img_path) as img:
        size_x, size_y = img.size

        if len(text) >= (size_x * size_y) // 3:
            raise Exception("Too large text!")

        img_bytes = bytearray(img.tobytes())

        for i, letter in enumerate(text):
            letter_id = ord(letter)
            for j in range(8):
                img_bytes[i * 9 + j] = changeBit(
                    img_bytes[i * 9 + j], (letter_id >> (7 - j)) & 0b1
                )

        for j in range(8):
            img_bytes[len(text) * 9 + j] = changeBit(
                img_bytes[len(text) * 9 + j], (ord("\0") >> (7 - j)) & 0b1
            )

        return Image.frombytes("RGB", (size_x, size_y), img_bytes)


def decodeImage(img_path: str) -> str:
    with Image.open(img_path) as img:
        max_len = (img.size[0] * img.size[1]) // 3
        text = ""

        img_bytes = bytearray(img.tobytes())

        i = 0
        while i <= max_len:
            simb_id = 0
            for j in range(8):
                simb_id |= (img_bytes[i * 9 + j] & 1) << (7 - j)

            simb = chr(simb_id)
            if simb == "\0":
                break

            text += simb
            i += 1

    return text


if __name__ == "__main__":
    encodeImage("./img.bmp", "hello world!").save("answ.bmp")
    print(decodeImage("./answ.bmp"))
