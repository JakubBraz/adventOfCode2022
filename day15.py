from multiprocessing import Pool, cpu_count
import time


def add_range(ranges, r):
    result = set(ranges)
    inter = find_intersect(ranges, r)
    result -= inter
    new_range = {(min(x[0] for x in inter), max(x[1] for x in inter))}
    return result | new_range


def find_intersect(ranges, ran):
    result = {r for r in ranges if (ran[0] <= r[0] <= ran[1] or ran[0] <= r[1] <= ran[1] or
                                    r[0] <= ran[0] <= r[1] or r[0] <= ran[1] <= r[1])}
    return result | {(ran[0], ran[1])}


def find_no_beacons(b_s, target_line):
    s_x, s_y, b_x, b_y = b_s
    dist = abs(s_x - b_x) + abs(s_y - b_y)
    i = dist - abs(s_y - target_line)
    r1, r2 = s_x - i, s_x + i
    if r1 > r2:
        return False
    return r1, r2


def range_len(ranges):
    result = 0
    for r in ranges:
        l = r[1] - r[0] + 1
        result += l
    return result


def filter_ranges(ranges, limit_left, limit_right):
    return {(max(r[0], limit_left), min(r[1], limit_right)) for r in ranges
            if r[1] >= limit_left and r[0] <= limit_right}


def solve1(b_s_list, beacons, target_line):
    result = set()
    for b_s in b_s_list:
        ran = find_no_beacons(b_s, target_line)
        if ran:
            result = add_range(result, ran)
    len_without_beacons = len([b for b in beacons for r in result if r[0] <= b[0] <= r[1] and b[1] == target_line])
    return range_len(result) - len_without_beacons


def solve3(args):
    b_s_list, limit, range_from, range_to = args
    for row in range(range_from, range_to):
        no_beacons = set()
        for b_s in b_s_list:
            new_range = find_no_beacons(b_s, row)
            if new_range:
                no_beacons = add_range(no_beacons, new_range)
        occupied_columns = filter_ranges(no_beacons, 0, limit)
        if len(occupied_columns) == 2:
            s = sorted(occupied_columns)
            if s[1][0] - s[0][1] == 2:
                return (s[0][1] + 1) * limit + row


def solve2(args):
    b_s_list, limit, row = args
    no_beacons = set()
    for b_s in b_s_list:
        new_range = find_no_beacons(b_s, row)
        if new_range:
            no_beacons = add_range(no_beacons, new_range)
    occupied_columns = filter_ranges(no_beacons, 0, limit)
    if len(occupied_columns) == 2:
        s = sorted(occupied_columns)
        if s[1][0] - s[0][1] == 2:
            return (s[0][1] + 1) * limit + row


def solve2_millions_processes(b_s_list, limit):
    with Pool() as p:
        result = p.map(solve2, ((b_s_list, limit, row) for row in range(limit+1)))
        result = [r for r in result if r]
        return result[0]


def solve2_few_processes(b_s_list, limit):
    with Pool() as p:
        count = cpu_count() // 2
        chunks = [(i * (limit // count), (i+1) * (limit // count) - 1) for i in range(count+1)]
        result = p.map(solve3, ((b_s_list, limit, c[0], c[1]) for c in chunks))
        result = [r for r in result if r]
        return result[0]


def main():
    # sensors_beacons = parse_input(day_input_test())
    sensors_beacons = parse_input(day_input())
    beacons = {(x[2], x[3]) for x in sensors_beacons}
    result1 = solve1(sensors_beacons, beacons, 2_000_000)
    print(result1)
    print('part 2 in progress...')
    t = time.time()
    result2 = solve2_few_processes(sensors_beacons, 4_000_000)
    print(f'{result2} (time elapsed: {time.time() - t} - multi CPU, few processes)')
    t = time.time()
    result2 = solve2_millions_processes(sensors_beacons, 4_000_000)
    print(f'{result2} (time elapsed: {time.time() - t} - multi CPU, millions processes, possible context switching)')
    t = time.time()
    result2 = solve3([sensors_beacons, 4_000_000, 0, 4_000_000])
    print(f'{result2} (time elapsed: {time.time() - t} - single CPU)')


def parse_input(arg):
    result = arg.split('\n')
    result = [''.join(x for x in line if x == ',' or x == ':' or x == '-' or x.isnumeric()) for line in result]
    result = [line.split(':') for line in result]
    result = [(line[0].split(','), line[1].split(',')) for line in result]
    result = [(int(line[0][0]), int(line[0][1]), int(line[1][0]), int(line[1][1])) for line in result]
    return result


def day_input_test():
    return """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


def day_input():
    return """Sensor at x=251234, y=759482: closest beacon is at x=-282270, y=572396
Sensor at x=2866161, y=3374117: closest beacon is at x=2729330, y=3697325
Sensor at x=3999996, y=3520742: closest beacon is at x=3980421, y=3524442
Sensor at x=3988282, y=3516584: closest beacon is at x=3980421, y=3524442
Sensor at x=3005586, y=3018139: closest beacon is at x=2727127, y=2959718
Sensor at x=3413653, y=3519082: closest beacon is at x=3980421, y=3524442
Sensor at x=2900403, y=187208: closest beacon is at x=2732772, y=2000000
Sensor at x=1112429, y=3561166: closest beacon is at x=2729330, y=3697325
Sensor at x=3789925, y=3283328: closest beacon is at x=3980421, y=3524442
Sensor at x=3991533, y=3529053: closest beacon is at x=3980421, y=3524442
Sensor at x=3368119, y=2189371: closest beacon is at x=2732772, y=2000000
Sensor at x=2351157, y=2587083: closest beacon is at x=2727127, y=2959718
Sensor at x=3326196, y=2929990: closest beacon is at x=3707954, y=2867627
Sensor at x=3839244, y=1342691: closest beacon is at x=3707954, y=2867627
Sensor at x=2880363, y=3875503: closest beacon is at x=2729330, y=3697325
Sensor at x=1142859, y=1691416: closest beacon is at x=2732772, y=2000000
Sensor at x=3052449, y=2711719: closest beacon is at x=2727127, y=2959718
Sensor at x=629398, y=214610: closest beacon is at x=-282270, y=572396
Sensor at x=3614706, y=3924106: closest beacon is at x=3980421, y=3524442
Sensor at x=3999246, y=2876762: closest beacon is at x=3707954, y=2867627
Sensor at x=3848935, y=3020496: closest beacon is at x=3707954, y=2867627
Sensor at x=123637, y=2726215: closest beacon is at x=-886690, y=3416197
Sensor at x=4000000, y=3544014: closest beacon is at x=3980421, y=3524442
Sensor at x=2524955, y=3861248: closest beacon is at x=2729330, y=3697325
Sensor at x=2605475, y=3152151: closest beacon is at x=2727127, y=2959718"""


if __name__ == "__main__":
    main()
