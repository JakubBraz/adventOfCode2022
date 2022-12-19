import random
import re

# A - ORE
# B - CLAY
# C - OBSIDIAN
# D - GEODE


MAX_ROBOTS = 7
LIMIT = 10_000_000


def resources_per_blueprint(build_order, costs):
    robots = {"A": 1, "B": 0, "C": 0, "D": 0}
    resources = {"A": 0, "B": 0, "C": 0, "D": 0}
    new_robot = ""
    to_build = build_order[0]
    build_order = build_order[1:]
    for m in range(24):
        if to_build:
            cond = (resources["A"] >= costs[to_build]["A"] and
                    resources["B"] >= costs[to_build]["B"] and
                    resources["C"] >= costs[to_build]["C"])
            if cond:
                new_robot = to_build
                resources["A"] -= costs[to_build]["A"]
                resources["B"] -= costs[to_build]["B"]
                resources["C"] -= costs[to_build]["C"]
                if build_order:
                    to_build = build_order[0]
                    build_order = build_order[1:]

        resources = {k: resources[k] + v for k, v in robots.items()}
        if new_robot:
            robots[new_robot] += 1
            new_robot = ""

    # print('robots', robots)
    # print('resources', resources)
    return resources


def simulation(blueprints):
    result = 0
    for i, b in enumerate(blueprints):
        max_blueprint = find_max(b)
        result += (i+1) * max_blueprint
        print('blueprint', i, 'result', max_blueprint)
    return result


def find_max(blueprint):
    current_max = 0
    # for i in range(LIMIT):
    for i in range(1_000_000_000):
        if i % 100_000 == 0: print(i)
        # A = random.randint(1, MAX_ROBOTS)
        # B = random.randint(1, MAX_ROBOTS)
        # C = random.randint(1, MAX_ROBOTS)
        # D = random.randint(1, MAX_ROBOTS)
        A = random.randint(1, 5)
        B = random.randint(1, 5)
        C = random.randint(1, 5)
        D = random.randint(1, 5)
        # A = random.randint(1, random.randint(1, 10))
        # B = random.randint(1, random.randint(1, 10))
        # C = random.randint(1, random.randint(1, 3))
        # D = random.randint(1, random.randint(1, 2))
        permutation = ["A"] * A + ["B"] * B + ["C"] * C + ["D"] * D
        # permutation = ["A"] * A + ["B"] * B + ["C"] * C
        random.shuffle(permutation)
        # perm_len = 20
        # permutation = permutation[:perm_len]
        # d_index = random.randint(0, perm_len)
        # permutation = permutation[:d_index] + ["D"] + permutation[d_index+1:]

        # permutation = "BBBCBCDD"
        # permutation = ['B', 'B', 'B', 'C', 'B', 'C', 'D', 'D']

        result = resources_per_blueprint(permutation, blueprint)['D']
        if result > current_max:
            current_max = result
            print(permutation, result)
    return current_max


def find_best_d(blueprint, prefix):
    current_max = (0, [])
    # for i in range(LIMIT):
    for i in range(2_000_000):
        if i % 100_000 == 0: print(i)
        A = random.randint(1, 10)
        B = random.randint(1, 10)
        C = random.randint(1, 10)
        permutation = ["A"] * A + ["B"] * B + ["C"] * C
        random.shuffle(permutation)
        permutation = prefix + permutation + ['D']

        result = (resources_per_blueprint(permutation, blueprint)['D'], permutation)
        if result[0] > current_max[0]:
            current_max = result
            print(permutation, result[0])
    return current_max


def geode_cost(costs):
    a_cost = costs['A']['A']
    b_cost = costs['B']['A']


def main():
    blueprints = parse_input(day_input_test())
    print(blueprints)
    # result = find_max(blueprints[1])
    # print(result)
    # result1 = simulation(blueprints)
    # print(result1)
    # permutation = [c for c in "AABBBBBACCBCCCD"]
    # permutation = [c for c in "AABBBCBCCBCD"]
    permutation = ['A', 'A', 'B', 'B', 'B', 'B', 'B', 'C', 'B', 'C', 'B', 'C', 'C', 'C', 'C', 'D']
    # JAK TO MOZLIWE, ZE PO DODANIU 'A' JEST GORSZY WYNIK??????
    # permutation = ['A', 'A', 'B', 'B', 'B', 'B', 'B', 'C', 'B', 'C', 'B', 'C', 'C', 'C', 'C', 'D', 'A']
    r = resources_per_blueprint(permutation, blueprints[1])
    print('*')
    print(r)

    # best, perm = find_best_d(blueprints[1], [])
    # print(best, perm)
    # best2, perm2 = find_best_d(blueprints[1], perm)
    # print(best2, perm2)



def parse_input(arg):
    result = arg.split('\n')
    result = [re.findall(r"\d+", line) for line in result]
    result = [{"A": {"A": int(line[1]), "B": 0, "C": 0},
               "B": {"A": int(line[2]), "B": 0, "C": 0},
               "C": {"A": int(line[3]), "B": int(line[4]), "C": 0},
               "D": {"A": int(line[5]), "B": 0, "C": int(line[6])}}
              for line in result]
    return result


def day_input_test():
    return """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""


def day_input():
    return """Blueprint 1: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 3 ore and 17 obsidian.
Blueprint 2: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 17 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 3: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 16 clay. Each geode robot costs 2 ore and 11 obsidian.
Blueprint 4: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 14 clay. Each geode robot costs 4 ore and 15 obsidian.
Blueprint 5: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 17 clay. Each geode robot costs 3 ore and 16 obsidian.
Blueprint 6: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 7 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 7: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 19 clay. Each geode robot costs 4 ore and 12 obsidian.
Blueprint 8: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 10 clay. Each geode robot costs 3 ore and 14 obsidian.
Blueprint 9: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 8 clay. Each geode robot costs 3 ore and 19 obsidian.
Blueprint 10: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 14 clay. Each geode robot costs 3 ore and 20 obsidian.
Blueprint 11: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 11 clay. Each geode robot costs 3 ore and 14 obsidian.
Blueprint 12: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 6 clay. Each geode robot costs 4 ore and 11 obsidian.
Blueprint 13: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 20 clay. Each geode robot costs 4 ore and 8 obsidian.
Blueprint 14: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 15: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 13 clay. Each geode robot costs 3 ore and 11 obsidian.
Blueprint 16: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 17 clay. Each geode robot costs 3 ore and 11 obsidian.
Blueprint 17: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 7 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 18: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 15 clay. Each geode robot costs 2 ore and 15 obsidian.
Blueprint 19: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 18 clay. Each geode robot costs 4 ore and 16 obsidian.
Blueprint 20: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 5 clay. Each geode robot costs 3 ore and 18 obsidian.
Blueprint 21: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 6 clay. Each geode robot costs 3 ore and 11 obsidian.
Blueprint 22: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 4 ore and 15 obsidian.
Blueprint 23: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 17 clay. Each geode robot costs 3 ore and 19 obsidian.
Blueprint 24: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 18 clay. Each geode robot costs 4 ore and 8 obsidian.
Blueprint 25: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 17 clay. Each geode robot costs 4 ore and 16 obsidian.
Blueprint 26: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 17 clay. Each geode robot costs 4 ore and 20 obsidian.
Blueprint 27: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 10 clay. Each geode robot costs 3 ore and 10 obsidian.
Blueprint 28: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 10 clay. Each geode robot costs 4 ore and 10 obsidian.
Blueprint 29: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 14 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 30: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 11 clay. Each geode robot costs 4 ore and 8 obsidian."""


if __name__ == "__main__":
    main()
