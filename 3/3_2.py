def find_number(nx, ny, schematic):
    number = ""

    temp_ny = ny
    while temp_ny >= 0 and schematic[nx][temp_ny].isdigit():
        number = schematic[nx][temp_ny] + number
        temp_ny -= 1

    temp_ny = ny + 1
    while temp_ny < len(schematic[0]) and schematic[nx][temp_ny].isdigit():
        number += schematic[nx][temp_ny]
        temp_ny += 1

    return int(number)

def is_gear(x, y, schematic):
    if schematic[x][y] != '*':
        return False, []

    adjacent_numbers = set()
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue

            nx, ny = x + dx, y + dy
            if 0 <= nx < len(schematic) and 0 <= ny < len(schematic[0]) and (
                schematic[nx][ny].isdigit()):
                
                number = find_number(nx, ny, schematic)
                adjacent_numbers.add(number)

    return len(adjacent_numbers) == 2, adjacent_numbers

def sum_gear_ratios(schematic):
    total_sum = 0
    for i, row in enumerate(schematic):
        for j, char in enumerate(row):
            is_gear_flag, numbers = is_gear(i, j, schematic)
            if is_gear_flag:
                total_sum += list(numbers)[0] * list(numbers)[1]
    return total_sum


with open("input.txt", "r") as file:
    schematic = [line.strip() for line in file]

print("Sum of all gear ratios:", sum_gear_ratios(schematic))
