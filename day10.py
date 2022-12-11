def parse(arg):
    result = []
    for x in arg.split('\n'):
        temp = x.split()
        if len(temp) == 2:
            result.append([temp[0], int(temp[1])])
        else:
            result.append(temp)
    return result


def solve(arg, init_execute):
    to_execute = []
    i = 1
    for c in arg:
        if c[0] == 'addx':
            i += 2
            to_execute.append((c, i))
        else:
            i += 1
    to_execute.extend(init_execute)
    to_execute.sort(key=lambda x: x[1])
    memory = {'x': 1}
    result = 0
    picture = ''
    for c, cycle in to_execute:
        if c[0] == 'draw':
            c = (cycle - 1) % 40
            val = '#' if c in [memory['x'] - 1, memory['x'], memory['x'] + 1] else '.'
            picture += val
        elif c[0] == 'print':
            val = cycle * memory['x']
            result += val
        elif c[0] == 'addx':
            memory['x'] += c[1]
    return result, picture


def draw_image(img):
    acc = ''
    for i in range(0, 240):
        acc += img[i]
        if (i+1) % 40 == 0:
            print(acc)
            acc = ''


def main():
    inpt = parse(day_input())
    prints = [(['print'], x) for x in [20, 60, 100, 140, 180, 220]]
    draws = [(['draw'], x) for x in range(1, 241)]
    result1, result2 = solve(inpt, prints + draws)
    print(result1)
    draw_image(result2)


def day_input_test():
    return """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


def day_input():
    return """noop
noop
addx 5
addx 3
noop
addx 14
addx -12
noop
addx 5
addx 1
noop
addx 19
addx -15
noop
noop
noop
addx 7
addx -1
addx 4
noop
noop
addx 5
addx 1
addx -38
noop
addx 21
addx -18
addx 2
addx 2
noop
addx 3
addx 5
addx -6
addx 11
noop
addx 2
addx 19
addx -18
noop
addx 8
addx -3
addx 2
addx 5
addx 2
addx 3
addx -2
addx -38
noop
addx 3
addx 4
addx 5
noop
addx -2
addx 5
addx -8
addx 12
addx 3
addx -2
addx 5
addx 11
addx -31
addx 23
addx 4
noop
noop
addx 5
addx 3
addx -2
addx -37
addx 1
addx 5
addx 2
addx 12
addx -10
addx 3
addx 4
addx -2
noop
addx 6
addx 1
noop
noop
noop
addx -2
addx 7
addx 2
noop
addx 3
addx 3
addx 1
noop
addx -37
addx 2
addx 5
addx 2
addx 32
addx -31
addx 5
addx 2
addx 9
addx 9
addx -15
noop
addx 3
addx 2
addx 5
addx 2
addx 3
addx -2
addx 2
addx 2
addx -37
addx 5
addx -2
addx 2
addx 5
addx 2
addx 16
addx -15
addx 4
noop
addx 1
addx 2
noop
addx 3
addx 5
addx -1
addx 5
noop
noop
noop
noop
addx 3
addx 5
addx -16
noop"""
