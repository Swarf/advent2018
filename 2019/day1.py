

def fuel_needed(amount):
    total = 0
    while True:
        amount = int(amount / 3) - 2
        if amount <= 0:
            break
        total += amount

    return total


total_fuel = 0
total_all_fuel = 0
with open('data/day1') as data1:
    for line in data1:
        total_fuel += int(int(line) / 3) - 2
        total_all_fuel += fuel_needed(int(line))

print(total_fuel)
print(total_all_fuel)

