import os

# Z stands for 'zero sleep'
LETTER = "Z"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write(LETTER)
