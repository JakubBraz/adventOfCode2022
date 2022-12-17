CAVE_WIDTH = 7

shapes = [
    # shape -
    lambda x, y: {(x, y), (x+1, y), (x+2, y), (x+3, y)},
    # shape +
    lambda x, y: {(x, y+1), (x+1, y), (x+1, y+1), (x+1, y+2), (x+2, y+1)},
    # shape L (mirrored)
    lambda x, y: {(x, y), (x+1, y), (x+2, y), (x+2, y+1), (x+2, y+2)},
    # shape |
    lambda x, y: {(x, y), (x, y+1), (x, y+2), (x, y+3)},
    # shape . (square)
    lambda x, y: {(x, y), (x+1, y), (x, y+1), (x+1, y+1)}
]


def collision(cave, rock):
    conditions = [bool(cave.intersection(rock)),
                  any(x < 0 for x, _y in rock),
                  any(x > CAVE_WIDTH - 1 for x, _y in rock),
                  any(y < 0 for _x, y in rock)
                  ]
    return any(conditions)


def rock_step(cave, rock, pattern):
    if pattern == '>':
        new_rock = {(x+1, y) for x, y in rock}
    elif pattern == '<':
        new_rock = {(x-1, y) for x, y in rock}
    else:
        new_rock = {(x, y-1) for x, y in rock}
    if collision(cave, new_rock):
        return False
    return new_rock


def move(cave, rock, patterns, moves):
    move_on = True
    while move_on:
        new_rock = rock_step(cave, rock, patterns[moves % len(patterns)])
        if not new_rock:
            pass
        else:
            rock = new_rock
        new_rock = rock_step(cave, rock, 'down')
        if not new_rock:
            move_on = False
            cave = cave | rock
        else:
            rock = new_rock
        moves += 1
    return cave, moves, rock


def simulation(patterns, target_steps, init_steps, init_high, init_moves, init_cave):
    cave = init_cave
    highest = init_high
    moves = init_moves
    for i in range(init_steps, target_steps):
        rock = shapes[i % len(shapes)](2, highest + 4)
        cave, moves, _new_rock = move(cave, rock, patterns, moves)
        highest = max(cave, key=lambda x: x[1])[1]
    return highest + 1


def update_floor_shape(floor_shape, rock):
    for x, y in rock:
        floor_shape[x] = max(floor_shape[x], y)


def normalize(floor):
    min_val = min(floor)
    return tuple(x - min_val for x in floor)


def floor_to_cave(floor, high):
    update_high = high - max(floor)
    return {(i, val + update_high) for i, val in enumerate(floor)}


def simulation2(patterns, target_step):
    highest = -1
    cave = set()
    moves = 0
    floor_shape = [-1] * CAVE_WIDTH
    states = set()
    i = 0
    cycles = []
    while len(cycles) < 2:
        states.add((normalize(floor_shape), i % len(shapes), moves % len(patterns)))
        rock = shapes[i % len(shapes)](2, highest + 4)
        cave, moves, new_rock = move(cave, rock, patterns, moves)
        highest = max(cave, key=lambda x: x[1])[1]
        update_floor_shape(floor_shape, new_rock)
        if (normalize(floor_shape), (i + 1) % len(shapes), moves % len(patterns)) in states:
            states = set()
            cycles.append((i, highest, moves))
        i += 1
    step_change, high_change, moves_change = \
        cycles[1][0] - cycles[0][0], cycles[1][1] - cycles[0][1], cycles[1][2] - cycles[0][2]

    current_step, current_high, current_moves = cycles[1]

    steps_skipped = (target_step - current_step) // step_change - 1
    current_step += steps_skipped * step_change
    current_high += steps_skipped * high_change
    current_moves += steps_skipped * moves_change

    current_cave = floor_to_cave(normalize(floor_shape), current_high)

    return simulation(patterns, target_step, current_step + 1, current_high, current_moves, current_cave)


def main():
    # patterns = parse_input(day_input_test())
    patterns = parse_input(day_input())
    result1 = simulation(patterns, 2022, 0, -1, 0, set())
    print(result1)
    result2 = simulation2(patterns, 1_000_000_000_000)
    print(result2)


def parse_input(arg):
    return arg


def day_input_test():
    return ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"


def day_input():
    return ">>><<<>>><><>>><<>>>><<>>>><<<<><<<<>>>><>>><<<>><<<>>><<<<>><<<<>><<<<>>><><<<<>><><<<<>>>><<<>><><<<><><<>><<<<>>>><<><<<<>>>><<<<>>><>><<>>><<>><<><>>>><<<>>><<<>>><<<>>>><>>><>><<<<>><<<<>><>>><><>><<<>>>><<<>>>><<>>>><<<>><<<>>><><<<>>><<<<>>><<<<>>><<<>><<><<<>><><<<>>>><>><<>><<><<<<><<<<>>><<<><<>>><>>><<><<><<>>><<<>><<<><>><<<>><<<><<<>>>><<><>><<<>>><<<>>><>>><<<<>>><<<<>>><>><>>><<>><<<>>>><<>>><<>>>><>>>><><<<>>><>><<>><<<<><<>>><<<><<>>><<<>>><<<<>>><<<<>>>><<<<>><<>><<<><<<<>><<<><>>><<<>>><<<><<<<><<<<>>><<>>>><<><<<><>>><<<<>>>><<<>><<<>><<<<><>><>><<<>><<<<><<><<<><<>>>><<<><<<>>>><<<<>>>><<>>><<><<>>><<>><<<>><>><<>>><<<<><<<>>><<<>>>><<<<><<<>>><<<>><<<>>>><<>>><<<>>>><<<<>>>><>>>><<>>><>><<>>><<<<><><<<<>>>><<<>><<<>>><<<<>>>><<<<>>><<>>>><>>>><<<<>>><<<>>>><<<<><<<<>>>><<<<>><<<><<<><<<>>><<<<>>>><<>><<>>>><<>>><<<<><>>>><<>>><<>><>>><<<<>>>><<<<>>><<<><<<>>><<><<<><<<><>>>><<<<>>>><<<<>><<<>>><><>>><<<<>><<<>>>><<<>>>><<>>>><<<<>><<><<<>><<<<><<<>>><<<<>><>>><<<>>>><<<<>>>><<<><><<<<>><<<>><<>>><<<<><>>><<<<>>>><<>>><<>><<><<>>><<>>>><<>>><>><>>>><>>>><>>><>>>><<>><<<<><>>><>>><>><<>>>><>><<>>>><<>>>><<<>><>><>><>>><><>>>><>>>><>><<><<<>>><<>><<<<>>><<<<>>><<<>>><<<>>><<<<>>>><>><<<<>><<<<>>><<<>>>><<<><>>>><<<<>>>><>><<>>><<<<>>><<<>><<>>>><<>><<<<><<<>><>><<<<>><<<<>>><<<<><<<>>><<>>><<><><<>>><<<>><<<>>><<<<>>><<>>><><<>>><<<<><<>>><<<<>>><<>><<<<>><<<>>>><<<>>>><<<<>><<>><<<>><<<>>><<<>>><<<>>>><<>><<>>><>><<<<>>><<<<><<>>><<<<>><<<<>>><<<<>>><<<<>>>><<<<><>>><>><<<>>><>>><<<<><<>><<>><<<<>><<><<<>><<<>>>><<<>>>><<<>>><<<<>><>><<<<>>><<>><<<<>>><<<>>><<>><<<>>><<>>>><<<>>>><<<>>>><><><<<<><<<<>><<>><>>>><<>><>>><>>>><<<<>>>><><<<>>>><>><>>>><<><<>><<><>>><<<<>>><>>>><<<><<>>>><<><<<>>>><<<>><<<><<>>>><<<><<<>>>><<>><>>>><<>>><<<<><<<>>><<>>><<<<><><<<<><>><><><<<<><><<>>>><<<>><<<<>><>><<<><<<<>>>><<>><<>>>><>>><<<><<<>><<<<>>><>><><><<>>>><><<<>><<>>><<<>>><<<<>>><<>>>><<<>><<<>>><<>><<>>>><<<<>>><<>>>><><<<>><>><<<>><<<><<><>>>><><<<>>>><>>><<>><<><<<<>>>><<>>><<<<>>>><>><><<>>><<<><>><<><>><>>>><>>>><<<><><<<>>><<>>>><<<>>><<<<>>>><<<>><<<<>>>><<<>>><<<<><<<><<<>>><><<><>><<<<>>><<<<>>><<<>>>><<<<>><<<>>><><<>><<><<>>>><<>><>>><<<<>><<<>>>><<<>>><<<><<><<><<<>>><<<<>>><>>>><<<>>>><>>>><<<>>>><<>>>><<>>><<<>><<<>>>><>><<>>><<<>>>><<>>><<<>>>><<><<>><<>>>><<<>><<>>>><<<>><>><>><<<<>>>><<<>>>><>>><>>>><<<>><<>><><<<<>>><<<<>>><<<<><<<>>><<<<><<>>>><<>><<>>><<<>>><<<<><<<>>><<><<<<><<>><><>><<>>><>>>><<<><>>>><<>><>><><<<<><<<<>>>><<<><<<><<<<>><<>>><<<<><<<>>><<<<>><<<><><<<<><<>>><<>>>><<>>>><<<<>><<<<><<>>><<>>><<<<>><<<<><<<>><<<>><>><>>><<><<<<><<>><>><<<><<>><<>>>><<<<>>><<<<>><<<><<<><<>>><<>>>><<>><>>>><<<>>>><<<><<<<><<<<>>><>>>><<<<>>>><<<>>><>>><<<>><<<<><>>>><>>><><<<>>>><>>><>><<><<>><<<<>><<<>><<<>><<<<>>>><<<<>>>><<>>><<<<>>>><<<<>><<>>><<>>><<<<><<>>><<<>>><>>>><<><<<<>><>><>>>><>>>><><<><<>>><<><<>>><>>>><<>>><<<<>><<<><<>><>>><>><<>>><<><<>>>><<<<>>><<<>>>><>>>><>>><<>>>><<<<>><<><<<<>>>><<<><<>>>><>>><<<><<>>><>>>><<><<>><<>><<<>>><<><><<<<>><<<<><>>>><<<>>>><>><<<<>><<<>>><<<>>>><<<<>>>><><<<>>><<>><><>>>><<<<>>>><<<<><>>><<<>>>><<><<<>><<<<><>>>><<>><<<>><<<>>><<><<<>>><<<><<<>><<><>><><<<<>>><<<<>>><<><<<<><>>>><<<<>>><<>>>><>>>><<<><>><>><<<<>><<>><<><<>>><<><<<<>><>><<<>>><<<>><<<><<<<>>><<<>>><<>>><>><<<>><<<>><<<>><<><<><><<>>>><<<<>><>>>><<<>>>><<<>>>><><<<<>>><<<<>><<>><<<>>>><>><<<<>>><<<>><<><>>><<<<><<<>>>><<<>>><<<<>>>><><<>>>><>><<<<><<<><><>><<<>>>><<<>><>>><<<>>>><<<<>>>><<<<><><>><<<<>><>><>><<<<>>><<<<>>><<<<>>>><<<><>>><>>><>><>>>><<<<>>>><<>><<>>><<<<><<<<>><<<<>><<<>><<<<>><<><<<>>>><>>><<><<<>><<<>><<><>>>><<<<>>><><><<<<>><>>><<><<>><<<>>>><>><<<><<<<>>><<>>><<<<><<<<>><<><<>><><<<<>>>><<<><<>>><<<<>>><>><<<<>>>><<>>>><<><<>>>><<<<>><<<>>>><<>>><<<><<>>>><><<>><>><<<><<>>>><<>>>><<><<><<<<>>><<<<>><<<<><>>>><<<><<><<><<<>><<<<><<<><<<<>>><<<<>>><<>>><>>>><<<>><<>><><<>>><>><<<><>><<<>>><<<<>>>><><<<<>>><<<>><>><<<<>>><<<><<<<>>><><<>>>><>>>><<<<>><<<>>><<<>>><<<<><<>><<>><<<<>>>><<>>>><<><<>>><<>>><<<>>><><>>>><>>><<>>><<<<>>>><>>>><>>><<<<>>><<<<>>><><<<>>><<<<>>>><>><><<>>><<<><>>><<<>>><<<>>><<<>>>><>>>><<<<>>>><<<<>>>><<<>>>><<><<>><<<<>>><<<>>>><<<>><<<<>>><<><<><<<<>>><>><<<><<<>>>><<>><<><<<>>>><<<><<<>>><<<<>>>><<>>>><<<<>>><><<><<<<><<<<>>><<>>><>>>><><><>>>><<<<>>><<<>>><<<><<<<>>>><>><><<<>><>><<<<>>><><<<<>>>><<<>>>><>><<<>>>><>><<<><<<<><><>>><>>><<<>>><<><<<>>>><>>>><<<>>><>><><<<<><<><<<>>>><<><<><<><<<>>>><<<><<<>>><<<<>><<<<>>>><>>>><><<<>>><<<<>>>><<><>>>><<<>><>>>><<><<<<>><<<>><<>>>><<><>><><<<<><<<<>>>><>>><<>><<><>>>><<<><<<>><<><>>>><<>>>><<<>>><<<>>>><<>>>><<<>><<<>>><<<>><<<<>>><<>>>><<<>>>><<<>><<<<>>><>>>><>>><<<<>>>><<<<>><>>><<>>>><<<><><><<>>><<<<>>><>>><<<<>>>><<>>>><<<<>>>><<<>>><<<<>><<>>>><>>><>>><<>>><<<<>>>><<<><><<<<>>>><<<>>>><<<<>>><<<<>>><<<>><<<>>>><<>>>><><<<<>>>><<<<>><>><<<><<<><<<<>>><<<<>>>><>>><>><>>>><<<<>>><<>><<<>>><<>><<>><<><<>>><<>>><<<>>>><<<><><<<><<<<>>><<<>><<<<>>>><<>><<<><>><<<><>>>><<<<>>><<<<>><<><>><<<>>><<>>><<<>>><<<<>>>><<<>><<<<>><<>><>>>><>>><>><<<>>><<<><<<<>><<>>><<>>>><<>>><><<>><<<>>>><<><<>>>><<<>>>><<<<>>>><<<<>><<<<>>><>><<<>><>>>><<<><<>><<><<<<><<>>><>>><>>>><<><<<<>><>>><<<<><<<<>><<><>>>><<>><<<>>><<<>>>><<<><><<<>><<<>>>><<<>>><<<<>><<<<>><>><>><<<<>>><<><<<<>><>>><<<>><<><<>><<>>>><>><<<<><<<<>>><>>><<<>><<<>><>><<<<><<<>>>><>><>>><<<>>>><<<<>>><<>>>><<<>><<>>>><<<<>>><<<<>>><<<<>>>><<<<>><<<<>>><>>><>>><<<<>>><<<<>>><<>>>><<<<>>><<<>>><<<>><><<<>>>><<>>><<><<<>>>><<<>><>><>>>><><<><<<>>><<>>>><<<<>><<<<>>>><>>><<><<<<><<<<>>><>>>><<<>><><>>>><<<>><>><<<>><<><<>><<<>>><>>><<>>><<><<<>>><<<>>>><>><>><<<<><<<<>>>><<<>>>><<<>>><<>><<>>><>><<<<>><<>>><<<<><>><<>>><<<>>><<<<>>><>>><<>>>><<<<><>>>><<<>><<<>>>><<<>>><<<<>>>><<>><<<<>>><<><>><>>>><>>>><<<>><<>>><<<>>>><<<>>>><<><<><<<>><>>>><<>>><<<<>>>><><<>>>><<>>>><<<>><<<>>><<<>>>><<<>><<>>>><><><<<><<>><>>>><<>>>><<>><<<><<<><><<<<>>><><<<><<><<<>><<<><<<>>>><<<>><<>>><<<<>>>><>>><>>>><<<<>>><<<>><<<<>>>><><>>><><>><<>><<>>>><><>>><<<><>>><<<>>>><<><<<<>>><>><<>>>><>><<<>>><<<<>>>><>><<>>><<<>>><<<<>><<>>><<<<>><<>>><<<<>>>><<>>><<<<>><><<<<>><<<>>><<<><<<<>>><<<<>>><<><>>>><<>>><<<>><>>>><<<<><><<<><<>>>><<><<><>>>><<<>>>><<<<>>><<><<>><<<>>>><<>>>><>>>><<><<<>><<><<>><<>><<<>>><>>>><<<<><<<>><<<<><<><<<<><<<<>><<<<>>>><<><<>>><>>><<<>>><>><<<>><<<>>><<<<><<<>><<<<>>>><<>>>><<<<>><<<<>>><<<>>><<<<>>>><<><<>><<><<<>>><<<<>>>><<><<>>>><>><<<<><<>>>><><<<<>>><<<>><<<<>>><<>>>><<<<>>><<<<><<<<>>><>>><>>><<<>><<<><>>>><><<<><>><<<<><<<><<<>>>><<<>><>><<<><>>>><<>>><>><<>>>><<>>>><<<>><<<<>>><<<>>>><<<<><<<<>><<<<>>><><<<<>>><<><>><<<<>><<>><>>><<<<>><<><<>>>><<<>>><<<<><<<<>>><<<>><<<><<<>><<<<><<<<><>>>><>>><<<>>>><>>><<>><<<<>><<<>>><<<<>><<<<>>><<<<><<<>>>><<>>><<>>><>>>><>><<>>>><<>><>>><<><<<<>>>><<<>>><<<>><<<><<<>>><>>>><<<><<<<><<<><<>>><<<>><<<<>><>><<>><<<<><><<<<>>><>>><<<<>>>><<>><<<<><<<<>>><<>>><<>><<<<>><><<<><<>>>><><<<><<<<>>>><>>><>><<<<>>><>>>><<<><<<<>>><<<<><<<><<<>>><<<<>>><<<>>><>>>><<<>><<<<>>><<>><<>>><>>><>>><<<><<><<<<><<<>><<<>><<<<>><>>>><<<<>>><<>>><>>>><<<<>><<<<><>>>><<<<>><>>><<<<>>>><<>>>><<<<>><<<<>><<<>>>><<<>>>><<>>><<<<>>>><>>>><<<>>><><<<><<<<>><<>><<<>><>>><>><<><<<<>>>><<<<>>>><>><<>><<<>>><>>>><>>>><><<<<><<<>>>><<<<><<<>>><>>><<>>><<>>><<<<>>>><>>>><>>><<<<>>>><<<<>><<<<><<<>><<<<><<>><<>>><>><<>><>>>><<><<<<>><><>>><<<<>><<<><<>>>><>>>><<<<><><<<<><<>><<<>><<<<>>><<<><<<>><<<>>><><>>><><>>><<<<><<>><<<>>>><<<<>>><<<<>>>><>>>><>><<<<>><<<>><<>>>><<>><<>>><>>>><><><<>>>><<<<>>><>>>><<<>>>><<<<>><>>><<<<>>>><>><<<>><<><<<<>>><<<<>>><<<>>>><<<<>><<>>><<>>>><<<<>>>><<<<>>><<>><<<<>><<<>>>><<<>>>><<<>><<<<>>><<>>><>>>><><<>>>><<<<>>><<>>><<<><<<<>>>><>>><<<<>><<<<>><<<>><>>><>><<<<>>><<><>>><<>><<>>><<><<>><><><>>><<<>>>><<<<>>>><>>><<<>>>><<<><<>>>><>><<<<><<<<>>>><<<>>>><<<<>>><<<><<>>><><<<><<<>><<<>>>><<>>><<<<>>>><<<<>><<>><<<<>>>><<>><<<>>><<<><<<>><>><<<>>><<><<<><<><<<><<<<>>><<<><<<<>><>>><<<>>><>><<>>><<<><<>><<<<>>>><<<<>><<<>>>><<><>><<>>>><<<><<>><<<<>>><<>>><<<<>>>><<<>>><<><<>>><<>>>><<<>><>>><<<<>>><<>>><><>><>>><<<>><<<><<>><<>><<<<>>>><<<<><>><<<>>><<>>><><<<<>><<<<>><<>>><<><<<<><<><>>><<<><>>>><>><<<>><>><<<<>>>><<<>>>><<<<>>><<<<>>>><<>>><<>><<<<><>>>><<<>>>><<>><>><<><<<<>>>><<<>>>><<>>>><>><<<>><<><<<>>><<<>><<><<><<>>><<<>>><<<>><<<>><<><<<<>>>><<<>>><<><<<<>><<<>>><<>>><<>>><>><<<>>>><<<<>>><<<<>><<<>><>>>><<<>>><<<<>>><<><<<><<>><>><<>>><<>>><<><<>>><<<<>><<>>>><<>>><<<>>>><<<>><<><<>><<<<>><<>>>><<<<>><<>>><>>><<<>><<<><<>>><>><<<<>>>><<<<>><<<<><<><<<>>><<<<>>>><<<>>>><<><<<>><<<<>>>><<<<><<><<<>>>><<>>><<<>>>><<<<><>>>><>>>><<<<>>><>>>><<<><>>><<>>><>>><<<><<<<>>><<>>><>>>><<>><>>>><<>>><<<<>>>><<<<>>>><<<<>>><<>><<<<>>>><<<<>>><<<>><><<<<>>><<>><>>><>>>><<<<>><>>>><<<<>>><<<<>>><<<<><>>><<<<>><<<>>><<<>><<<<>>>><<<><<<<>>><<>><<<<>>><<<><<<<>>><<<>><>>>><<<<>>>><>>>><<<>>>><>>><<<>>><<<>><<>>>><<>><<<<>><>><<<><<<>>><<<<>>><>><<<>><>><<<>>>><<<<>>>><<<<><>>>><<<<><<<<><<<<>>>><<<<>><<>>>><>><<<<>><<>>><<<<><<<<>><<<>><<>>><<<>>>><<<<>>><<>><<<<>><<<<>><<>><<<<>>>><<><>><>><<><<<>>>><<>>><<<<>><<<><>>>><<<<><<>>>><<<<>>>><<>>><<<><<<>><>>><>>>><>>><<<>>>><>><>><>><<>><>><>>><<><>>>><<<>>><>><>>>><<<<>>><<<>><<>>>><>>>><<<>><>><<<<>><<><<<>>><<>>><<>>><<<<>><>>><>>><<<>><<>>>><<>>>><<><<<<>>>><<<<>>><>>><<<<><<<>>>><>><<<<>>>><<<<><<>><<<>>><<<<>>><><<><<>>><<<><<<>><<<<><<<<>><<>>>><><<<>>>><<<<>>><<<>><>>>><<>>><<<<>>>><><<><<<><<<>>><<<<>><<<>>><<<<><<<<>>>><><>><<<<><<><<>><<>><><<>><<<<>><<<<>>>><<<>>>><<<<>>><>>><<<>>>><<<<>>><<<><<<<>><<<>><<<>><<<>><>>>><<<>><<>>><>>>><>>>><<<><<<<>>>><<>>>><<<>>><<<><<<>>>><>>>><<><>>><><><<>>><<>>><>><<<><>>><<>>><<><<<><<<>><<>><>>>><>><<<><<<><<<>><>><>>><<><<>><<<<>>><<<<>>>><<<<><<>>>><<>>>><<>><<<>>>><>>>><<><<<>>>><<<<>>>><<<<>>><<>>><<><<>><<<<>>>><>>><<<>><<<>>><>>>><<<>>><<<>><<<<><<<>><<<<><<<>>>><<>>>><<<<><>>><>>>><>>><<<>>><<<>>><<>>><<<<>>><<<>><<>><<>><<<<>>>><<<>><<<<><<<>>>><>>><<><<><<<<><<<<>>>><<<><><<<>><><<<>>><<<<>>><<<<>><<<><<<<><<<<>><<<<>><<<>>><<<<>><<<><>>>><<<<>>>><<<><<<> "


if __name__ == "__main__":
    main()