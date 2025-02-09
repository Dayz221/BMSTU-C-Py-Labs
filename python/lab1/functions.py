# Файл functions.py - файл, содержащий функции перевода и вспомогательные функции


def deleteZeros(num: str):
    sign = ""
    if num[0] == '-': 
        num = num[1:]
        sign = "-"
    parts = num.split(".")
    if len(parts) == 1:
        num = sign+parts[0].lstrip("0")
    elif len(parts) == 2:
        parts[0] = parts[0].lstrip("0")
        parts[1] = parts[1].rstrip("0")
        num = f"{sign}{parts[0] if len(parts[0]) else 0}{f'.{parts[1]}' if len(parts[1]) else ''}"
    else:
        raise ValueError("Incorrect number!")

    if len(num) == 0: return "0"
    else: return num

def to4(num: str, precision: int = 5) -> str:
    answ = ""
    sign = ""
    num = float(num)

    if num != 0 and num/abs(num) == -1:
        sign = "-"
        num *= -1
    
    int_part, float_part = int(num), num - int(num)

    if int_part == 0: answ += "0"
    while int_part != 0:
        answ += str(int_part%4)
        int_part //= 4
    answ = answ[::-1]
    answ += "."

    cnt = 0
    while cnt < precision:
        float_part *= 4
        answ += str(int(float_part))
        float_part -= int(float_part)
        cnt += 1

    answ = deleteZeros(answ)

    return sign + answ


def from4(num: str, precision: int = 4) -> str:
    answ = 0
    int_part, float_part = "", ""

    sign = 1
    if num[0] == "-":
        sign = -1
        num = num[1:]

    parts = num.split(".")
    if len(parts) == 1:
        int_part, float_part = parts[0], ""
    elif len(parts) == 2:
        int_part, float_part = parts
    else:
        raise ValueError("Incorrect number!")
    
    power = 0
    for digit in int_part[::-1]:
        answ += int(digit) * 4**power
        power += 1

    power = -1
    for digit in float_part:
        answ += int(digit) * 4**power
        power -= 1

    return f"{answ * sign:.{precision}f}"


if __name__ == "__main__":
    num = input("n: ")
    print(deleteZeros(num))
