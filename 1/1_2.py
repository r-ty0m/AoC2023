def findNumbers(line):
    numbers = {
        'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r',
        'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'
    }
    for word, digit in numbers.items():
        line = line.replace(word, digit)
    return line
    
total = 0
with open("input.txt", "r") as file:
    for line in file:
        line = findNumbers(line)
        digits = [char for char in line if char.isdigit()]
        if digits:
            total += int(digits[0] + digits[-1])
          
print(f"The answer is {total}")
