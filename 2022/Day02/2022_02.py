# The winner of the whole tournament is the player with the highest score.
# Your total score is the sum of your scores for each round.
# The score for a single round is the score for the
# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round(0 if you lost,
# 3 if the round was a draw, and 6 if you won).


# a class to represent a single round of the scissors, paper, rock tournament
class Round:
    def __init__(self, me="", opponent="", outcome="", mode="sol1"):
        # convert the letter to a shape
        self.mode = mode
        if mode == "sol1":
            self.me = me
            self.opponent = opponent
        elif mode == "sol2":
            self.opponent = opponent
            self.outcome = outcome

    def __str__(self):
        return f"{self.me} vs {self.opponent} = {self.score()}"

    def return_the_weak(self):
        if self.opponent == "Rock":
            return "Scissors"
        elif self.opponent == "Paper":
            return "Rock"
        elif self.opponent == "Scissors":
            return "Paper"

    def return_the_stronger(self):
        if self.opponent == "Rock":
            return "Paper"
        elif self.opponent == "Paper":
            return "Scissors"
        elif self.opponent == "Scissors":
            return "Rock"

    def return_the_same(self):
        return self.opponent

    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
    def define_outcome(self):
        if self.outcome == "X":
            self.me = self.return_the_weak()
        elif self.outcome == "Y":
            self.me = self.return_the_same()
        elif self.outcome == "Z":
            self.me = self.return_the_stronger()

    def shape_score(self):
        if self.me == "Rock":
            return 1
        elif self.me == "Paper":
            return 2
        elif self.me == "Scissors":
            return 3

    def winner_score(self):
        if self.me == self.opponent:
            return 3
        elif self.me == "Rock" and self.opponent == "Scissors":
            return 6
        elif self.me == "Scissors" and self.opponent == "Paper":
            return 6
        elif self.me == "Paper" and self.opponent == "Rock":
            return 6
        else:
            return 0

    def score(self):
        if self.mode == "sol1":
            return self.shape_score() + self.winner_score()
        elif self.mode == "sol2":
            
            self.define_outcome()
            return self.shape_score() + self.winner_score()


def letter_to_shape(letter):
    letter = letter.strip()
    if letter == "A" or letter == "X":
        return "Rock"
    elif letter == "B" or letter == "Y":
        return "Paper"
    elif letter == "C" or letter == "Z":
        return "Scissors"


# open input file and read it
with open("input.txt", "r") as file:
    # read the file and split it into a list
    # the split function splits the string at every newline
    # and returns a list with all lines
    lines = file.read().splitlines()

################
## SOLUTION 1 ##
################

# create a list to store all rounds
rounds = []

# loop over all lines
for line in lines:
    # split the line at the colon
    # the first element is the shape I played
    # the second element is the shape my opponent played
    opponent, me = line.split(" ")

    # create a new round object
    round = Round(me=letter_to_shape(me), opponent=letter_to_shape(opponent))
    # add the round to the list
    rounds.append(round)


# calculate the total score
total_score = 0
for round in rounds:
    total_score += round.score()

solution1 = total_score
print("Solution 1: ", solution1)

################
## SOLUTION 2 ##
################

# create a list to store all rounds
rounds.clear()

# loop over all lines
for line in lines:
    # split the line at the colon
    # the first element is the shape I played
    # the second element is the shape my opponent played
    opponent, outcome = line.split(" ")

    # create a new round object
    round = Round(mode="sol2", opponent=letter_to_shape(opponent), outcome=outcome)

    # add the round to the list
    rounds.append(round)

# calculate the total score
total_score = 0
for round in rounds:
    total_score += round.score()

solution2 = total_score
print("Solution 2: ", solution2)