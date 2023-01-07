file = open("input.txt", "r")
lines = file.readlines()
totals = []
total = 0
for line in lines:
    if line is "\n":
        totals.append(total)
        total = 0
    else:
        total += int(line)

highest = 0
for total in totals:
    if total > highest:
        highest = total

print("Highest total is : " + str(highest))
