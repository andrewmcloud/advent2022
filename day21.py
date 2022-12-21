with open("resources/day21.txt") as f:
    input = f.readlines()

monkeys = {}

for line in input:
    match line.strip().split():
        case[monkey, one, oper, two]:
            monkeys[monkey.strip(":")] = one + " " + oper + " " + two

        case[monkey, number]:
            monkeys[monkey.strip(":")] = number

while True:
    for k, v in monkeys.items():
        match v.split():
            case[monkey1, operator, monkey2]:
                try:
                    monkeys[k] = str(eval(monkeys[monkey1] + operator + monkeys[monkey2]))
                except NameError:
                    continue
            case[_]:
                continue
    try:
        if eval(monkeys["root"]):
            break
    except NameError:
        continue

print(monkeys["root"])
