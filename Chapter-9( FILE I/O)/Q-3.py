import os

# 3. Write a program to generate multiplication tables from 2 to 20 and write it to different files.
# Place these files in a folder for a 13-year-old.

OUTPUT_DIR = "tables"


def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n * i}\n"

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    file_path = os.path.join(OUTPUT_DIR, f"table_{n}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(table)


if __name__ == "__main__":
    for i in range(2, 21):
        generateTable(i)
