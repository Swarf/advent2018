

count = 0
start = 372037
end = 905157
# end = start + 10

guesses = []

for i in range(start, end + 1):
    last_digit = None
    consecutive = 1
    qualified = False
    for digit in list(str(i)):
        if last_digit and last_digit > digit:
            qualified = False
            consecutive = 0
            break

        if last_digit == digit:
            consecutive += 1
        else:
            if consecutive == 2:
                qualified = True
            consecutive = 1
        last_digit = digit

    if qualified or consecutive == 2:
        guesses.append(i)

# For part 1, set the consecutive comparison to >= instead
print(len(guesses))
