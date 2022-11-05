# This is just an idea of how to solve this puzzle. I did this on my phone without proper testing.
# I know it doesn't work, and it's not optimized.

puzzle = ("435269781", "682571493", "197834562", "826195347", "374682915",
          "951743628", "519326874", "248957136", "763418259")

cols = [[], [], [], [], [], [], [], [], []]
blocks = [[], [], []]
valid = True

# TODO: fix nested for loop
for i in range(9):
    row = puzzle[i]
    for j in range(9):
        cols[j] += row[j]
    if len(set(row)) != 9:
        print(False)
        raise Exception("Row " + row + "is in correct")
    else:
        blocks[0].append(row[:3])
        blocks[1].append(row[3:6])
        blocks[2].append(row[6:])

for b in blocks:
    for i in range(3):
        section = "".join(b[i * 3: i * 3 + 3])
        if len(set(map(int, [*section]))) != 9:
            print(False)
            raise Exception("Block " + section + " is incorrect")

for c in cols:
    if len(set(map(int, c))) != 9:
        raise Exception("Error in column")

print(True)
