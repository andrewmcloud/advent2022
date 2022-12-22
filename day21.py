from copy import deepcopy
with open("resources/day21.txt") as f:
    input = f.readlines()


def make_monkeys(input):
    monkeys = {}
    for line in input:
        match line.strip().split():
            case[monkey, one, oper, two]:
                if oper == "/":
                    oper = "//"
                monkeys[monkey.strip(":")] = one + " " + oper + " " + two

            case[monkey, number]:
                monkeys[monkey.strip(":")] = number
    return monkeys


def yell(monkeys):
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
    return monkeys


def find_human_number():
    m = make_monkeys(input)
    m1, op, m2 = m["root"].split()
    offset = 1000000000000
    human = m["humn"]
    last = float("inf")
    while True:
        monkeys = deepcopy(m)
        monkeys["humn"] = human
        monkeys = yell(monkeys)
        diff = abs(int(monkeys[m1]) - int(monkeys[m2]))
        if diff == 0:
            break
        if last < diff:
            offset = -offset // 10
        last = diff
        human = str(int(human) + offset)
    return human


# part 1:
print(yell(make_monkeys(input))["root"])
# part 2:
print(find_human_number())