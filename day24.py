from math import gcd


def lcm(x, y):
    return x * y // gcd(x, y)


def do_step(blizzards, max_x, max_y):
    new_up = {(x - 1, y) if x > 1 else (max_x, y) for x, y in blizzards['^']}
    new_down = {(x + 1, y) if x < max_x else (1, y) for x, y in blizzards['v']}
    new_left = {(x, y - 1) if y > 1 else (x, max_y) for x, y in blizzards['<']}
    new_right = {(x, y + 1) if y < max_y else (x, 1) for x, y in blizzards['>']}
    return {'^': new_up, 'v': new_down, '<': new_left, '>': new_right}


def memo_blizzards(i, blizzards, max_x, max_y):
    memo = {}
    step = 0
    for step in range(i):
        memo[step] = blizzards
        blizzards = do_step(blizzards, max_x, max_y)
    memo[step + 1] = blizzards
    return memo


def draw(blizzards, max_x, max_y):
    for x in range(max_x + 2):
        line = ''
        for y in range(max_y + 2):
            element = '#' if x == 0 or y == 0 or x == max_x + 1 or y == max_y + 1 else (
                [k for k, v in blizzards.items() if (x, y) in v]
            )
            if type(element) == list:
                if len(element) == 1:
                    element = element[0]
                elif len(element) == 0:
                    element = '.'
                else:
                    element = str(len(element))
            line += element
        print(line)
    print()


def solve(blizzards, start, goal, limit_x, limit_y, cycle, init_i):
    queue = [(init_i, start)]
    visited = set()
    while True:
        i, (x, y) = queue.pop(0)
        moves = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x, y)]
        to_move = [(i + 1, (nx, ny)) for nx, ny in moves
                   if all((nx, ny) not in b for b in blizzards[(i + 1) % cycle].values())]

        result = [ni for ni, (nx, ny) in to_move if (nx, ny) == goal]
        if result:
            return result[0]

        to_move = [(ni, (nx, ny)) for ni, (nx, ny) in to_move
                   if ((0 < nx <= limit_x and 0 < ny <= limit_y) or (nx, ny) == start)
                   and (ni % cycle, (nx, ny)) not in visited]

        for ni, (nx, ny) in to_move:
            visited.add((ni % cycle, (nx, ny)))

        queue.extend(to_move)


def solve1(blizzards, start, goal, max_x, max_y, cycle):
    return solve(blizzards, start, goal, max_x, max_y, cycle, 0)


def solve2(blizzards, start, goal, max_x, max_y, cycle, result1):
    temp = solve(blizzards, goal, start, max_x, max_y, cycle, result1)
    return solve(blizzards, start, goal, max_x, max_y, cycle, temp)


def main():
    # start, goal, blizzards = parse_input(day_input_test())
    start, goal, blizzards = parse_input(day_input())
    max_x, max_y = goal[0] - 1, goal[1]
    cycle = lcm(max_x, max_y)
    memo = memo_blizzards(cycle - 1, blizzards, max_x, max_y)

    result1 = solve1(memo, start, goal, max_x, max_y, cycle)
    print(result1)
    result2 = solve2(memo, start, goal, max_x, max_y, cycle, result1)
    print(result2)


def parse_input(arg):
    result = arg.split('\n')
    start = [i for i, x in enumerate(result[0]) if x == '.'][0]
    start = (0, start)
    goal = [i for i, x in enumerate(result[-1]) if x == '.'][0]
    goal = (len(result) - 1, goal)
    blizzards_up = {(x, y) for x in range(len(result)) for y in range(len(result[x])) if result[x][y] == '^'}
    blizzards_down = {(x, y) for x in range(len(result)) for y in range(len(result[x])) if result[x][y] == 'v'}
    blizzards_left = {(x, y) for x in range(len(result)) for y in range(len(result[x])) if result[x][y] == '<'}
    blizzards_right = {(x, y) for x in range(len(result)) for y in range(len(result[x])) if result[x][y] == '>'}
    return start, goal, {'^': blizzards_up, 'v': blizzards_down, '<': blizzards_left, '>': blizzards_right}


def day_input_test():
    return """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""


def day_input():
    return """#.####################################################################################################
#<<<..>>><v<><><v^<><^vv^<<v<^<>>.v^vvvv<v.>v^<<v>>.v>><..<v^>v>.v^v>.><>>^><<.vv<^<>>^v<^.<>>>vvv^v<#
#>><vv.^v>>v>v.v^^^.><^<>>v.^>v^>v><.^>><>>^^.vvv^^^>^>^<vvv.<^.>.><>v.>vv<v.^>>^<><>><>v<v^.>^^^<.<<#
#>>v<v>vv<^^^^^<<v><<^v>^<vv^.v>>.>vv^v<^^..v^>><<>^>v>v<^v.><^<^^v><^^vv<.v..<^<.>^>^<^^^><^<v<^>>v>#
#<v<<<v<.^^^<>v^^^v<v^<<>.v<><v.<<<<><v^>>vv>^>v.^v..<><.<><^.<v^>^<^^<^<v.v.^<v><>v>..>>^^>>^^vv>v>>#
#>^v<><>vvv>>>v^^<^v<v<<<^<.<v^v^^.vvvvv<>vvvv^>v<v^v><<>...>v<^>^.^^^<><^.v<^v>^<v^^<<v^<^<>vv^>^><>#
#<<<<><>^<>><v<^^^>^>v<.^<^<.v<.><><<v<^^><v><>^^.^>>>v^<v^><^^.^<<<.v^>^^<^>^><^^.^v><v^>^<vv^v^<<><#
#>^>v><<<>>.v.>v<^^v<.vvv^vv>>v^v^^><^><>>.>^>^v^v><^v.v<^<v<<v<vv^v<^<<><<v><..^^<.v.v><^<.><>^>>>v<#
#<^^v<.<.vv>>vv<.<.<>><v^^>vv><v<>v^.v>v<.>v^>>>^.v>^<>v<<^vv>^<v^>^><^<v^^<v><>v.>vv^v<<v.vv^>v^...<#
#>^v>>><>^.^<v^<^<^<>>v<>^>>v><^<<v^^>>^.^<<v>.^>>^^><^^v<v.v<^v>>v><>^<>>v^v^<>^<^<^v<vv<v<vv<>^>><.#
#<<>^v<^^^<^<<<.vvv><v><^.<>v>^>v^v.v<<<>.<>vv>v>v>..^.^v<<v<>v^>vv<>v<v>^>>^^<>^.<>^v^<>v^^><<<v^<<<#
#<.>>>><.>^v<^<>.v>^^<v^v.<.^..v^v>^v.<v^.v.vv.>.<v^....>^>v^v>^^^>v<^<^<^^^>><.^>v<<v^<.<v^<.>>>v^>.#
#<.>v<v><>>^^><v^<>^>>v>>^<v>.v^><..^vv^>><><.<^<><^^v^<^^>>v<>^<^>v^<^>v<<^>.<>v^<^v><>v^^vv<<vv<>><#
#><^^.^>>^^vv.vv^v<v<.^<.>v^>>v^^<<<>^<<>^v^v>.^<^.><v>>^v>><v<>.<>.>v<^<^v.<v>^^vv^^>>v.>^.<>.^<^.v>#
#>v<^^^v^^<^v^>^<^^^.>^^<^.>v<<><>vv<>..^^<^>>>><<>v<<v^^^>v.<>>^<v^>^<<v.^..>^>v^^.<<>><v<.>>v^<^v>.#
#<><.^<^^^^.><<^v.^<><vv<v<<v<^v^>^<^v^><>vv>v<<v><<<<><<.>^vv<v.^v<^>^<>>>v<vvvv^^<<<^><^v><<vv><>v.#
#>>v>v<>vvv>^>v<^<>><>v<vv.v<^^^vv>v<vv<>>>v..^.<>vv>^v>>^.<>^>v^.<<<v>v^<v><^^v..><^v<^^^v<.^^^v><^<#
#.>^.>>^><vvv<^vv^>v^v^<..>>^<^>^^vv>^v<^^..^v^^^<<^<v.<>><<>v<v<^^.>^vv><>v^v^v>v^>v^.v^vv>^><^>>^<>#
#><<v^<^>.>vv^v><^^^<v^<<>>.v<.^<.v^^v^^^v<v^>v><><v><<v>>>^<v^.^v^v^>>^v.v>><>^<.><.^vv<vvv.>v.vv^v<#
#<<^v><<^>.vv.>v>^>><^>.<<>v><^>v<v>^<>>>^v<<vvvvv^vv^>>.<>>^><>.>>v^>^v.v^^^^.<^.^vvv<>v<<v>^v^v<.>>#
#<^^>^>^..v<v^^.^>>v^^>v^.^>vv>vv><.>>><v^<><v>.<^<<<><<<<v>v^.v.^v^>^..^<.vv><<<^v^.>.<<<<v>>^<^vvv>#
#>>^^<.^^v>^^>^>>>^v^<v...<>v^<^>^>^v^><>.^><v^.<<v.^<><^<>^>^.<v>.^^>^<>.^<^<><<>><>v.^.<>>>>vv^>>.<#
#><v>.>v>vv<>v^^v>^v><^.<^<<<^v.>v^v<>>v><><>^^.><vvv^.^>>^^<^>^>>^vv<<>>^>>>^<>v>.^^^<<.v<<<v>>><v<>#
#<^v.v<v>^>v.<<.>vv^<><>>>.<^.><>>^^>v<>..>^<^^v^.<^^.><>v<<^.^vv<>v^^<v>^.v<vv>vv.^v^><<<^<<>v<>^v>>#
#><v^<>>^^><^>v.><>.^>v>vv>v>>v^>.^><^^.^<v><.<<.>v.>.<><^^^^>^v>^<><<v>v^<<>v<<^<v>v<.<<v>.><^^>^>v>#
#>^<<..^v>.v<>^.<<>v><.^^^><^><>vv>^.<<<^v^^^>^.<.v><v<<.<<^<<^>>v><<vvv.<>.^vv^^>v.>.v>^><>.<^^<vv^<#
#>><^^>v><^v^<vvv>^.<.v^>>><<>v<^.v>v><<<>..><.^^.>^^>>vv<<.>^<.^^>v^v>^..v>>>v<><>^.v<.>^>^.>.>^<^<<#
#>^^<.>vv<>vv>^>.^^>v^^<^<v^<<vv>v<<^vv<<v<<>.v^><v<.>v^>>^v<<v.<^.>^>v^>v<vv<^>^<^v^<<vv^<v>^>v<^.^<#
#><><v<.<^^v<.v<>^^^.>><^.vvv^<>>v>^^<.v>>.>^<v^><^..<..^<><>.v>^v<<>..vv>vvv^.v>v><<v..^^^<>>><^<>><#
#<v<>>>v>^v><vv^^>.<><<>>^v>^^><.<<<^.v.<^>>v.^v.<v^^.^.<v^><v<<<>v^><^>v<<^v^^>v><.<^.v<.<>>v<^v^>>>#
#<.v^vv<<^^..<^<>^><>>vv^^^<.<^<<^<.^>>^^.<><>^>^v>vv>v.^>v><vvv^<<>v>>^^.>>>vv<>^^v<.<><>>.<<<^^>>><#
#<v<^>^vv^><>>v^<^v<v<.^<^^vvvvv>><^><^>v<>v<^v<v..>>^^><v^<^.<v>>^^.>^.>>.v<v>v^^^^<.vvv<v>^<.v..^<.#
#>><><^^^^>^^<^^v>>.>><.>><^v^>^^>v>^<v.<^v^<<.<v.>^><^^^^v.>>v<^>>>^>><>^.^<^v><>^<.>>^<v<><vv^v^v>>#
#.>.v<^<>>v.v>^><^<v><v<^>><^vv>v^<^v><^v>.^v>v^.>..^<><<<><<vv.^<>vv<^<^v^v.^><>v<^^^^^.<<vvvv<>^^v<#
#<>>^>>>v^^vv>><>vv^.v<>^v^^v>^<v^vv<^^vv>^<v<.>>v^v^>v^<>><<<v.^vv<^><>>v<vv^vv^<<^v^^>.>v>v.^^^<<<>#
#<<^v^.^v<vv.^>v<v^vvv^<v.<.>>^<^<<<<^<<<.><><v>^><<<<vv^v.vv^>>^>^>v<^<^^>v<>^^>vv>^v..v^v^<<v<<<v<.#
####################################################################################################.#"""


if __name__ == "__main__":
    main()
