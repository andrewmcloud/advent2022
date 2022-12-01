with open('resources/day1_1.txt') as f:
    elves = [x for x in f.read().split("\n\n")]

elve = [x.split() for x in elves]
calorie_list = sorted([sum(int(snack) for snack in snacks) for snacks in elve], reverse=True)

# part 1
print(calorie_list[0])

# part 2
print(sum(calorie_list[:3]))
