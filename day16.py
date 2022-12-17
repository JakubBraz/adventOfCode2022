import re
import heapq
from collections import defaultdict
from random import sample
from multiprocessing import Pool, cpu_count

INF = 1024


def calculate_distance(graph, current):
    to_visit = []
    dist = defaultdict(lambda: INF)
    dist[current] = 0
    for v in graph.keys():
        if v != current:
            heapq.heappush(to_visit, (INF, v))
    heapq.heappush(to_visit, (0, current))
    while to_visit:
        dist_u, u = heapq.heappop(to_visit)
        for v in graph[u][1]:
            if v not in dist:
                alt = dist_u + 1
                dist[v] = min(alt, dist[v])
                heapq.heappush(to_visit, (dist[v], v))
    return dist


def result_for_permutation(graph, all_dists, perm, current, time):
    result = 0
    for v in perm:
        d = all_dists[current][v]
        time -= d
        if time <= 0:
            return result
        result += (time - 1) * graph[v][0]
        time -= 1
        current = v
    return result


def find_index1(graph, all_dists, done, to_find, prev_result, limit):
    time = 30
    result = prev_result
    for _ in range(limit):
        permutation = done + sample(to_find, len(to_find))
        res = result_for_permutation(graph, all_dists, permutation, 'AA', time)
        result = max(result, (res, permutation))
    return result


def find_index2(graph, all_dists, done, to_find, prev_result, limit):
    time = 26
    result = prev_result
    result_len = (len(done) + len(to_find)) // 2
    for _ in range(limit):
        permutation = done + sample(to_find, len(to_find))
        res1 = result_for_permutation(graph, all_dists, permutation[:result_len], 'AA', time)
        res2 = result_for_permutation(graph, all_dists, permutation[result_len:], 'AA', time)
        result = max(result, ((res1 + res2), permutation))
    return result


def simulation(graph, all_dists, not_zero, find_index_function, limit):
    done = []
    result = (0, [])
    for i in range(len(not_zero)):
        to_find = [x for x in not_zero - set(done)]
        result = find_index_function(graph, all_dists, done, to_find, result, limit)
        done.append(result[1][i])
    return result[0]


def run_process(args):
    graph, all_dists, not_zero, find_index, limit = args
    return simulation(graph, all_dists, not_zero, find_index, limit)


def main():
    # graph = parse_input(day_input_test())
    graph = parse_input(day_input())
    all_dists = {k: dict(calculate_distance(graph, k)) for k in graph}
    not_zero = {k for k, v in graph.items() if v[0] > 0}

    count = cpu_count()
    with Pool(count) as p:
        result1 = p.map(run_process, [(graph, all_dists, not_zero, find_index1, 10_000)] * 16)
        print(max(result1))
        result2 = p.map(run_process, [(graph, all_dists, not_zero, find_index2, 50_000)] * 16)
        print(max(result2))


def parse_input(arg):
    result = arg.split('\n')
    result = {
        re.findall('Valve (.+) has', line)[0]:
            (int(re.findall(r'rate=(\d+);', line)[0]), re.findall('to valves{0,1} (.+)', line)[0].split(', '))
        for line in result
    }
    return result


def day_input_test():
    return """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""


def day_input():
    return """Valve ZN has flow rate=0; tunnels lead to valves SD, ZV
Valve HO has flow rate=17; tunnel leads to valve LT
Valve FT has flow rate=6; tunnels lead to valves DW, BV, JA, FB, TV
Valve AD has flow rate=0; tunnels lead to valves AA, JG
Valve GE has flow rate=0; tunnels lead to valves JG, RD
Valve GI has flow rate=0; tunnels lead to valves WJ, RD
Valve RM has flow rate=0; tunnels lead to valves BU, WJ
Valve GV has flow rate=0; tunnels lead to valves WB, HS
Valve VA has flow rate=0; tunnels lead to valves AA, HS
Valve TJ has flow rate=21; tunnel leads to valve CK
Valve WB has flow rate=0; tunnels lead to valves GV, EV
Valve DV has flow rate=19; tunnels lead to valves OI, NK
Valve EL has flow rate=0; tunnels lead to valves HS, YC
Valve KU has flow rate=0; tunnels lead to valves WJ, OI
Valve WI has flow rate=16; tunnels lead to valves SD, AN, GS, JV
Valve JG has flow rate=3; tunnels lead to valves SV, BU, GC, GE, AD
Valve TC has flow rate=0; tunnels lead to valves TV, WJ
Valve GC has flow rate=0; tunnels lead to valves JG, JA
Valve LS has flow rate=0; tunnels lead to valves JH, YP
Valve OI has flow rate=0; tunnels lead to valves KU, DV
Valve ZH has flow rate=0; tunnels lead to valves YZ, RD
Valve YZ has flow rate=0; tunnels lead to valves ZH, AA
Valve YP has flow rate=0; tunnels lead to valves KS, LS
Valve CK has flow rate=0; tunnels lead to valves EG, TJ
Valve NY has flow rate=0; tunnels lead to valves HS, UU
Valve IQ has flow rate=18; tunnel leads to valve YC
Valve HI has flow rate=0; tunnels lead to valves SS, RD
Valve DW has flow rate=0; tunnels lead to valves FT, JH
Valve EV has flow rate=7; tunnels lead to valves SV, WB, SS, GS
Valve SV has flow rate=0; tunnels lead to valves JG, EV
Valve BU has flow rate=0; tunnels lead to valves JG, RM
Valve GS has flow rate=0; tunnels lead to valves EV, WI
Valve UY has flow rate=0; tunnels lead to valves WJ, FE
Valve AA has flow rate=0; tunnels lead to valves VA, YZ, AD, FB
Valve SD has flow rate=0; tunnels lead to valves WI, ZN
Valve KS has flow rate=23; tunnel leads to valve YP
Valve RD has flow rate=4; tunnels lead to valves GI, HI, BV, ZH, GE
Valve ZV has flow rate=15; tunnel leads to valve ZN
Valve HB has flow rate=0; tunnels lead to valves HS, AN
Valve UU has flow rate=0; tunnels lead to valves EG, NY
Valve SS has flow rate=0; tunnels lead to valves HI, EV
Valve HS has flow rate=12; tunnels lead to valves HB, EL, VA, GV, NY
Valve LT has flow rate=0; tunnels lead to valves DS, HO
Valve JH has flow rate=5; tunnels lead to valves LS, FE, QU, NK, DW
Valve AN has flow rate=0; tunnels lead to valves HB, WI
Valve NK has flow rate=0; tunnels lead to valves DV, JH
Valve JA has flow rate=0; tunnels lead to valves GC, FT
Valve EG has flow rate=14; tunnels lead to valves CK, UU, DS
Valve JV has flow rate=0; tunnels lead to valves QU, WI
Valve WJ has flow rate=8; tunnels lead to valves GI, RM, KU, UY, TC
Valve FE has flow rate=0; tunnels lead to valves JH, UY
Valve TV has flow rate=0; tunnels lead to valves FT, TC
Valve YC has flow rate=0; tunnels lead to valves IQ, EL
Valve QU has flow rate=0; tunnels lead to valves JV, JH
Valve DS has flow rate=0; tunnels lead to valves LT, EG
Valve BV has flow rate=0; tunnels lead to valves FT, RD
Valve FB has flow rate=0; tunnels lead to valves AA, FT"""


if __name__ == "__main__":
    main()
