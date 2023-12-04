class ListPair:

    # input is a combination of two ranges which are represents list 
    # define the type of the input
    def __init__(self, start1: int, end1: int, start2: int, end2: int):

        self.start1 = start1
        self.end1 = end1
        self.start2 = start2
        self.end2 = end2
        self.list1 = self.getList(start1, end1)
        self.list2 = self.getList(start2, end2)
        self.intersection = self.getIntersection()
        self.isSubset = self.isSubset(self.list1, self.list2)

    # get the list of the range
    def getList(self, start, end):
        start = int(start)
        end = int(end)
        return [i for i in range(start, end + 1)]

    def getIntersection(self):
        return list(set(self.list1).intersection(set(self.list2)))

    # check if one list is a subset of a second list
    def isSubset(self, list1, list2):
        if len(list1) > len(list2):
            return set(list2).issubset(set(list1))
        else:
            return set(list1).issubset(set(list2))

    # isOverlapping function check if the two list are overlapping so if the intersection is not empty
    def isOverlapping(self):
        if len(self.intersection) > 0:
            return True
        else:
            return False
            

    def __str__(self) -> str:
        return f"List1: {self.list1} List2: {self.list2} Intersection: {self.intersection} IsSubset: {self.isSubset}"   


    # representation function of the class the both list and show the intersection in red
    # def print(self):
    #     print("List1: ", self.list1)
    #     print("List2: ", self.list2)
    #     print("Intersection: ", end="")
    #     for letter in self.intersection:
    #         print("\033[91m" + letter + "\033[0m", end=" ")
    #     print()


# open input file and read it
with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    # split the lines in groups of 2 '2-4,6-8' so 2-4 is group[0] and 6-8 is group[1]
    listPairs = []
    for line in lines:
        start1 = line.split(",")[0].split("-")[0]
        end1 = line.split(",")[0].split("-")[1]
        start2 = line.split(",")[1].split("-")[0]
        end2 = line.split(",")[1].split("-")[1]
        listPairs.append(ListPair(start1, end1, start2, end2))

    # make a list of the isSubset values
    isSubsetList = [listPair.isSubset for listPair in listPairs]
    print("Solution 1: ", sum(isSubsetList))

    # make a list of the isOverlapping values
    isOverlappingList = [listPair.isOverlapping() for listPair in listPairs]
    print("Solution 2: ", sum(isOverlappingList))
    
