
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

highest3 = [0, 0, 0]


def try_insert_into_top3(candidate):
    replaced_index = None
    if (candidate > highest3[0]):
        replaced_index = 0
    elif (candidate > highest3[1]):
        replaced_index = 1
    elif (candidate > highest3[2]):
        replaced_index = 2
    if replaced_index is None:
        return
    replaced = highest3[replaced_index]
    highest3[replaced_index] = candidate
    # good ol' recursion
    try_insert_into_top3(replaced)


for total in totals:
    try_insert_into_top3(total)


highest3_total = highest3[0] + highest3[1] + highest3[2]

print("Sum of highest 3 totals is : " + str(highest3_total))
