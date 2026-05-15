import os
from datetime import datetime, timedelta

# ==================================
# PERFECT SHAGOR GITHUB ART
# ==================================

FONT = {
    "S": [
        "0111110",
        "1100011",
        "1100000",
        "0111110",
        "0000011",
        "1100011",
        "0111110",
    ],

    "H": [
        "1100011",
        "1100011",
        "1100011",
        "1111111",
        "1100011",
        "1100011",
        "1100011",
    ],

    "A": [
        "0011100",
        "0110110",
        "1100011",
        "1111111",
        "1100011",
        "1100011",
        "1100011",
    ],

    "G": [
        "0011110",
        "0110001",
        "1100000",
        "1101111",
        "1100011",
        "0110001",
        "0011110",
    ],

    "O": [
        "0011100",
        "0110110",
        "1100011",
        "1100011",
        "1100011",
        "0110110",
        "0011100",
    ],

    "R": [
        "1111110",
        "1100011",
        "1100011",
        "1111110",
        "1101100",
        "1100110",
        "1100011",
    ]
}

TEXT = "SHAGOR"

HEIGHT = 7
SPACE = 2

canvas = [""] * HEIGHT

# Build text canvas
for char in TEXT:

    pattern = FONT[char]

    for row in range(HEIGHT):
        canvas[row] += pattern[row]
        canvas[row] += "0" * SPACE


# First Sunday of 2022
START_DATE = datetime(2022, 1, 2)

# Create file
with open("data.txt", "w") as f:
    f.write("SHAGOR\n")


def commit(date, number):

    with open("data.txt", "a") as f:
        f.write(f"{number} {date}\n")

    os.system("git add .")

    date_string = date.strftime("%Y-%m-%d 12:00:00")

    os.system(
        f'GIT_AUTHOR_DATE="{date_string}" '
        f'GIT_COMMITTER_DATE="{date_string}" '
        f'git commit --allow-empty -m "art-{number}" > /dev/null 2>&1'
    )


count = 0

# GitHub layout:
# weeks = x
# days = y
for y in range(HEIGHT):

    for x in range(len(canvas[y])):

        if canvas[y][x] == "1":

            date = START_DATE + timedelta(weeks=x, days=y)

            # brighter pixel
            for i in range(5):

                count += 1
                commit(date, count)

print("DONE")
print("COMMITS:", count)