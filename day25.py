with open("resources/day25.txt") as f:
    input = [x.strip() for x in f.readlines()]

fromSNAFU = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
}

toSNAFU = {
    2: "2",
    1: "1",
    0: "0",
    -1: "-",
    -2: "=",
}


def snafu_to_decimal(snafu):
    total = 0
    for i, digit in enumerate(reversed(snafu)):
        total += 5**i * fromSNAFU[digit]
    return total


def decimal_to_base5(decimal):
    snafu = []
    while decimal:
        remainder = decimal % 5
        snafu.append(remainder)
        decimal = decimal // 5
    return snafu


def base5_to_decimal(base5):
    snafu = ""
    while base5:
        current = base5.pop(0)
        if current < 3:
            snafu += toSNAFU[current]
        else:
            snafu += toSNAFU[current - 5]
            try:
                base5[0] += 1
            except IndexError:
                base5.append(1)
    return snafu[::-1]

decimal_sum = 0
for snafu in input:
    decimal_sum += snafu_to_decimal(snafu)

print(base5_to_decimal(decimal_to_base5(decimal_sum)))
