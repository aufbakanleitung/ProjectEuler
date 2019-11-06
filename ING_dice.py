# ING dice challenge
example1 = [1, 2, 3]  # 2
example2 = [1, 1, 6]  # 2
example3 = [1, 6, 2, 3]  # 3

die_dict = {1: [2, 3, 4, 5], 2: [1, 3, 4, 6], 3: [1, 2, 5, 6], 4: [1, 2, 5, 6], 5: [1, 3, 4, 6], 6: [2, 3, 4, 5]}


def turn_die(dice_set, die):
    total = 0
    for nr in [x for x in range(len(dice_set)) if x != die]:
        if dice_set[die] == dice_set[nr]:
            total += 0
        elif dice_set[die] in die_dict[dice_set[nr]]:
            total += 1
        else:
            total += 2
    return total


def iter_set(dice_set):
    minimum_turns = len(dice_set) + 1
    for die in range(len(dice_set)):
        current_minimum = turn_die(dice_set, die)
        if minimum_turns > current_minimum:
            minimum_turns = current_minimum
    return minimum_turns


print(iter_set(example1))
print(iter_set(example2))
print(iter_set(example3))
