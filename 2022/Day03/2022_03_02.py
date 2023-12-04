def getPriority(letter):
    letter = str(letter)
    if letter.isupper():
        return ord(letter) - 64 + 26
    else:
        return ord(letter) - 96


def matchingLetter(list1, list2, list3=None):
    matches1 = []
    matches2 = []

    if list3 != None:
        for letter in list2:
            if letter in list3:
                matches1.append(letter)

        for letter in list1:
            if letter in list2:
                matches2.append(letter)

        # convert list to set
        set1 = set(matches1)
        set2 = set(matches2)

        # find intersection
        intersection = set1.intersection(set2)
       
        return intersection

    else:
        for letter in list1:
            if letter in list2:
                # print("Match found:", letter)
                return letter


# open input file and read it
with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    # split lines into groups of 3
    groups = [lines[i : i + 3] for i in range(0, len(lines), 3)]
    priority = []

    # for each group, find the matching letter
    for group in groups:
        priority.append(getPriority(list(matchingLetter(group[0], group[1], group[2]))[0]))
      
solution2 = sum(priority)
print("Solution 2: ", solution2)
