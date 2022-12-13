# create a elve class to store the calories
class Elve:
    # the constructor
    def __init__(self, calories, count=None):
        # store the calories
        self.calories = calories
        # store the name
        self.count = count


    # the function to calculate the total calories
    def total_calories(self):
        # return the sum of all calories
        return sum(self.calories)

# open input file and read it
with open("input.txt", "r") as file:
    # read the file and split it into a list
    # the split function splits the string at every newline
    # and returns a list with all lines
    lines = file.read().splitlines()

# create a list to store the elves
elves = []

# create a list to store the calories
calories = []

# count the elves
elf_count = 1


# loop over all lines
for line in lines:
    # if the line is not empty
    if line:
        # append the calories to the list
        calories.append(int(line))
    # if the line is empty
    else:
        # create a new elf with the calories
        elves.append(Elve(calories=calories, count=elf_count))
        # clear the calories list
        calories = []
        # increase the elf count
        elf_count += 1



# convert the elves list to a set and sort it in reverse order
elves.sort(reverse=True, key=lambda elve: elve.total_calories())

def print_elves(elves):
    for elve in elves:
        print(elve.total_calories())

solution1 = elves[0].total_calories()
print("Solution 1: ", solution1)

# create a total calories list 
total_calories = []
for elve in elves:
    total_calories.append(elve.total_calories())

solution2 = sum(total_calories[:3])
print("Solution 2: ", solution2)
