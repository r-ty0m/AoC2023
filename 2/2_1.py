def parse_line(line):
    parts = line.split(': ')
    game_id = int(parts[0].split(' ')[1])
    pulls = parts[1].split('; ')
    return game_id, [(parse_pull(pull)) for pull in pulls]

def parse_pull(pull):
    counts = {'red': 0, 'green': 0, 'blue': 0}
    for part in pull.split(', '):
        number, color = part.split(' ')
        counts[color] += int(number)
    return counts

def is_possible_game(pulls, max_counts):
    for pull in pulls:
        for color in max_counts:
            if pull[color] > max_counts[color]:
                return False
    return True


with open('input.txt', 'r') as file:
    games = [parse_line(line.strip()) for line in file]

max_counts = {'red': 12, 'green': 13, 'blue': 14}
possible_games_sum = 0

for game_id, pulls in games:
    if is_possible_game(pulls, max_counts):
        possible_games_sum += game_id

print("Sum of possible game IDs:", possible_games_sum)
