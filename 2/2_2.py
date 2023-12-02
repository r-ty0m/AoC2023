def parse_line(line):
    parts = line.split(': ')
    game_id_str, pulls_str = parts
    game_id = int(game_id_str.split(' ')[1])
    pulls = pulls_str.split('; ')
    return game_id, [parse_pull(pull) for pull in pulls]

def parse_pull(pull):
    counts = {'red': 0, 'green': 0, 'blue': 0}
    parts = pull.split(', ')
    for part in parts:
        number_str, color = part.split(' ')
        counts[color] += int(number_str)
    return counts

def find_minimum_cubes(pulls):
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for pull in pulls:
        for color in min_cubes:
            min_cubes[color] = max(min_cubes[color], pull[color])
    return min_cubes

def calculate_power(cubes):
    return cubes['red'] * cubes['green'] * cubes['blue']

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]
    games = [parse_line(line) for line in lines]

total_power_sum = 0

for game_id, pulls in games:
    min_cubes = find_minimum_cubes(pulls)
    power = calculate_power(min_cubes)
    total_power_sum += power

print("Sum of the power of minimum sets of cubes:", total_power_sum)
