from collections import defaultdict


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


def find_no_beacons(b_s, beacons, target_line):
    s_x, s_y, b_x, b_y = b_s
    dist = abs(s_x - b_x) + abs(s_y - b_y)
    # print("SENSOR BEACON", b_s)
    # print('dist to', dist)
    # res = set()
    # y_lim1 = s_y - dist
    # y_lim2 = s_y + dist + 1
    # if y_lim1 <= target_line <= y_lim2:
    #     for i in range(dist - abs(s_y - target_line) + 1):
    #         if (s_x + i, target_line) not in beacons:
    #             res.add((s_x + i, target_line))
    #         if (s_x - i, target_line) not in beacons:
    #             res.add((s_x - i, target_line))
    # return res
    i = dist - abs(s_y - target_line)
    r1, r2 = s_x - i, s_x + i
    if r1 > r2:
        return False
    return (r1, r2)


def range_len(ranges, beacons, row):
    result = 0
    for r in ranges:
        l = r[1] - r[0] + 1
        beacons_in = len([b for b in beacons if r[0] <= b[0] <= r[1] and b[1] == row])
        result += l - beacons_in
    return result


def range_len2(ranges):
    result = 0
    for r in ranges:
        l = r[1] - r[0] + 1
        # beacons_in = len([b for b in beacons if r[0] <= b[0] <= r[1] and b[1] == row])
        result += l
    return result


def filter_ranges(ranges, limit_left, limit_right):
    return {(max(r[0], limit_left), min(r[1], limit_right)) for r in ranges
            if r[1] >= limit_left and r[0] <= limit_right}


def solve1(b_s_list, beacons, target_line):
    result = set()
    for b_s in b_s_list:
        ran = find_no_beacons(b_s, beacons, target_line)
        result = add_range(result, ran)
    print(result)
    return range_len(result, beacons, target_line)


def solve2(b_s_list, beacons, column_limit, row_limit):
    no_beacons = defaultdict(set)
    occupied_columns = {}
    for row in range(row_limit + 1):
        # print("ROW", row)
        if row % 500_000 == 0: print("ROW", row)
        for b_s in b_s_list:
            ran = find_no_beacons(b_s, beacons, row)
            # print('--', ran)
            if ran:
                no_beacons[row] = add_range(no_beacons[row], ran)
        occupied_columns[row] = filter_ranges(no_beacons[row], 0, row_limit)
        # print(no_beacons[row])
        # print(filtered)
        # print(range_len2(no_beacons[row]))
        # print(range_len2(filtered))
    only_row = min(occupied_columns, key=lambda x: range_len2(occupied_columns[x]))
    print(occupied_columns[only_row])
    # print({k:v for k,v in occupied_columns.items() if len(v)>0})
    print(only_row)
    s = sorted(occupied_columns[only_row])
    return (s[0][1] + 1) * row_limit + only_row


def main():
    print(add_range({(0, 3), (5, 10), (100, 200)}, (3, 4)))
    # sensors_beacons = parse_input(day_input_test())
    sensors_beacons = parse_input(day_input())
    beacons = {(x[2], x[3]) for x in sensors_beacons}
    # result1 = solve1(sensors_beacons, beacons, 10)
    # result1 = solve1(sensors_beacons, beacons, 2_000_000)
    # print(result1)
    # result2 = solve2(sensors_beacons, beacons, 20, 20)
    result2 = solve2(sensors_beacons, beacons, 4_000_000, 4_000_000)
    print(result2)


def parse_input(arg):
    result = arg.split('\n')
    result = [''.join(x for x in line if x == ',' or x == ':' or x == '-' or x.isnumeric()) for line in result]
    result = [line.split(':') for line in result]
    result = [(line[0].split(','), line[1].split(',')) for line in result]
    result = [(int(line[0][0]), int(line[0][1]), int(line[1][0]), int(line[1][1])) for line in result]
    # sensors = [(line[0], line[1]) for line in result]
    # beacons = [(line[2], line[3]) for line in result]
    # return sensors, beacons
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
