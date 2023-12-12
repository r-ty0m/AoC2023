def is_adjacent_to_symbol(x, y, schematic):
    rows = len(schematic)
    cols = len(schematic[0])
    
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < cols) and (not schematic[nx][ny].isdigit() and 
                                                        schematic[nx][ny]!='.'):
                return True
    return False

def sum_part_numbers(schematic):
    total_sum = 0
    for i, row in enumerate(schematic):
        number = ""
        for j, char in enumerate(row):
            if char.isdigit():
                number += char
                if j == len(row) - 1 or not row[j+1].isdigit():
                    flag = False
                    for c in range(len(number)):
                        if is_adjacent_to_symbol(i,j-c, schematic):
                            flag = True
                    if flag == True:
                        total_sum += int(number)
                    number = ""
    return total_sum

with open("input.txt", "r") as file:
    schematic = [line.strip() for line in file]

print("Sum of part numbers:", sum_part_numbers(schematic))
