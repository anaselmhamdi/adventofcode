with open("../input.txt", "r") as f:
    line_data = f.read().splitlines()

elves = []
elf_calories = []
for line in line_data:
    if line != "":
        elf_calories.append(int(line.strip()))
    else:
        elves.append(elf_calories)
        elf_calories = []
print(f"The elf with the most calories has {sum(max(elves, key=sum))} calories.")

print(f"The sum of calories of the top 3 elves is: {sum(sorted(map(lambda x: sum(x),elves), reverse=True)[:3])}")
