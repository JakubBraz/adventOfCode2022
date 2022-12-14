from math import prod


def parse_monkey(arg):
    arg = arg.split('\n')
    items = ''.join(x for x in arg[1] if x.isalnum() or x==' ')
    items = items.split()
    items = [x for x in items if x[0].isdigit()]
    items = [int(x) for x in items]

    op_str = 'new = old '
    operation = arg[2][arg[2].find(op_str) + len(op_str):]
    operation = operation.split()
    if operation[1].isdigit():
        operation = [operation[0], int(operation[1])]
    else:
        operation = [operation[1]]

    div_by = ''.join(x for x in arg[3] if x.isdigit())
    div_by = int(div_by)

    throw_to_true = ''.join(x for x in arg[4] if x.isdigit())
    throw_to_true = int(throw_to_true)
    throw_to_false = ''.join(x for x in arg[5] if x.isdigit())
    throw_to_false = int(throw_to_false)
    return [items, operation, div_by, throw_to_true, throw_to_false]


def parse_input(arg):
    monkeys = arg.split('\n\n')
    return [parse_monkey(m) for m in monkeys]


def play_monkey(monkey, monkeys, i, manage_worry, activities):
    items, operation, div_by, throw_true, throw_false = monkey
    while items:
        activities[i] += 1
        item = items.pop(0)
        if operation[0] == '*':
            item *= operation[1]
        elif operation[0] == '+':
            item += operation[1]
        else:
            item *= item
        item = manage_worry(item)
        append_monkey = monkeys[throw_true] if item % div_by == 0 else monkeys[throw_false]
        append_monkey[0].append(item)


def play_round(monkeys, manage_worry, activities):
    for i, monkey in enumerate(monkeys):
        play_monkey(monkey, monkeys, i, manage_worry, activities)


def solve(monkeys, rounds, manage_worry):
    activities = [0 for _ in monkeys]
    for _ in range(rounds):
        play_round(monkeys, manage_worry, activities)
    activities.sort(reverse=True)
    return activities[0] * activities[1]


def main():
    i = day_input()
    monkeys = parse_input(i)
    result1 = solve(monkeys, 20, lambda x: x // 3)
    print(result1)
    monkeys = parse_input(i)
    result2 = solve(monkeys, 10_000, lambda x: x % prod(m[2] for m in monkeys))
    print(result2)


def day_input_test():
    return """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


def day_input():
    return """Monkey 0:
  Starting items: 76, 88, 96, 97, 58, 61, 67
  Operation: new = old * 19
  Test: divisible by 3
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 93, 71, 79, 83, 69, 70, 94, 98
  Operation: new = old + 8
  Test: divisible by 11
    If true: throw to monkey 5
    If false: throw to monkey 6

Monkey 2:
  Starting items: 50, 74, 67, 92, 61, 76
  Operation: new = old * 13
  Test: divisible by 19
    If true: throw to monkey 3
    If false: throw to monkey 1

Monkey 3:
  Starting items: 76, 92
  Operation: new = old + 6
  Test: divisible by 5
    If true: throw to monkey 1
    If false: throw to monkey 6

Monkey 4:
  Starting items: 74, 94, 55, 87, 62
  Operation: new = old + 5
  Test: divisible by 2
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 5:
  Starting items: 59, 62, 53, 62
  Operation: new = old * old
  Test: divisible by 7
    If true: throw to monkey 4
    If false: throw to monkey 7

Monkey 6:
  Starting items: 62
  Operation: new = old + 2
  Test: divisible by 17
    If true: throw to monkey 5
    If false: throw to monkey 7

Monkey 7:
  Starting items: 85, 54, 53
  Operation: new = old + 3
  Test: divisible by 13
    If true: throw to monkey 4
    If false: throw to monkey 0"""


if __name__ == '__main__':
    main()
