def parse_data(data):
    rotations = []
    distances = []
    for line in data:
        rot = line[0]
        dist = int(line[1:])
        
        rotations.append(rot)
        distances.append(dist)

    return rotations, distances


def part1(data):
    rotations, distances = parse_data(data)

    position = 50
    number_of_0 = 0

    for rot, dist in zip(rotations, distances):
        position += (1 if rot == 'R' else -1) * dist
        position %= 100

        number_of_0 += (position == 0)

    return number_of_0


def part2(data):
    rotations, distances = parse_data(data)

    position = 50
    number_of_0 = 0

    for rot, dist in zip(rotations, distances):
        dir = 1 if rot == 'R' else -1
        for i in range(dist):
            position += dir
            position %= 100
            number_of_0 += position == 0

    return number_of_0


if __name__ == "__main__":
    YEAR, DAY = 2025, 1
    with open(f"{YEAR}/{DAY:02d}/data/{DAY:02d}_test.txt") as file:
        data = file.read().splitlines()

    res_p1 = part1(data)
    print(res_p1)

    res_p2 = part2(data)
    print(res_p2)
