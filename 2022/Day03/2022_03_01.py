

# create a class to represent one backback and every backpack has two compartments  (class Compartments)
class Backpack:

    def __init__(self, content):
        length = len(content)
        self.content = content
        self.compartment1 = Compartments(content[0:length//2])
        self.compartment2 = Compartments(content[length//2:])
        self.error = self.compartment1 - self.compartment2
        self.priority = self.getPriority()

    def __str__(self):
        return str(self.compartment1) + str(self.compartment2)

     # function to find the matching letter in two compartments
    def __sub__(self, other):
        # create a list to store the matching letters
        matchingLetters = []
        # iterate over all letters in the first compartment
        for letter in self.content:
            # check if the letter is in the second compartment
            if letter in other.content:
                # if the letter is in the second compartment add it to the matching letters list
                matchingLetters.append(letter)
                # remove the letter from the second compartment
                other.content.remove(letter)
        # return the list with the matching letters
        return matchingLetters

    def getPriority(self):
        error = self.error[0]
        if error.isupper():

            return ord(error) - 64 + 26

        else:

            return ord(error) - 96


class Compartments:

    def __init__(self, content):
        # split content and put it in a list and store it in self.content
        self.content = list(content)

    def __str__(self):
        return str(self.content)

    # function to find the matching letter in two compartments
    def __sub__(self, other):
        # create a list to store the matching letters
        matchingLetters = []
        # iterate over all letters in the first compartment
        for letter in self.content:
            # check if the letter is in the second compartment
            if letter in other.content:
                # if the letter is in the second compartment add it to the matching letters list
                matchingLetters.append(letter)
                # remove the letter from the second compartment
                other.content.remove(letter)
        # return the list with the matching letters
        return matchingLetters


# open input file and read it
with open("input.txt", "r") as file:
    # read the file and split it into a list
    # the split function splits the string at every newline
    # and returns a list with all lines
    lines = file.read().splitlines()
    # create a dict with a key for every backpack and a value for the priorite of the error
    backpacks = []

    # iterate over all lines
    for line in lines:
        backpack = Backpack(str(line))
        backpacks.append(backpack)
        # backpacks[backpack] = backpack.get_error()


################
## SOLUTION 1 ##
################

solution1 = sum([backpack.priority for backpack in backpacks])
print("Solution 1: ", solution1)
