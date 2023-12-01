total = 0
with open("input.txt", "r") as file:
    for line in file:
        digits = [char for char in line if char.isdigit()]
        if digits:
            total += int(digits[0] + digits[-1])
          
print(f"The answer is {total}")
