# List comprehensions provide a concise, readable and efficient way to create new lists

# General Format:
# [expression for item in iterable if condition] 
# #iterable is something like a list, tuple, or dictionary
# expression: what you want to do with each item (eg. x * 2)
# for item in iterable: the loop that goes through each value (eg. for x in range(1,11))
# if condition: (optional): A filter that decides which items to include

#example (traditional method - without list comprehension):
doubles = []

for x in range(1, 11):  # range(1, 11) gives numbers 1–10
    doubles.append(x * 2)

print(doubles)

# simplify the above and do it in ONE line!!!!!
doubles_lc = [x*2 for x in range(1,11)]
print(doubles_lc)

# note we can unpack lists by prepending a * to them
alternateIdea = [*[x*2 for x in range(1,11)], 99]
print(alternateIdea)

alternateIdea += [x*2 for x in range(1,11)]
print(alternateIdea)

# we only want multiples of five
# do it without a step function on range
multiplesOf5 = [x for x in range(0,51) if x % 5 == 0]
print(multiplesOf5)

games = ["half life 2", "quake", "doom", "bloons td 6", "the binding of isaac"]

# use list comprehension to make a list of these titles in title case
gameTitles = [games.title() for games in games]
print(gameTitles)

# update the above to only give back titles with more than one word
gameTitles = [game.title() for game in games if " " in game]

students = [("Paul", 70), ("Edward", 63), ("Nico", 56), ("Ivy", 59), ("Samantha", 75)]

passing = [x[0] for x in students if x[1] >= 70]
failing = [x[0] for x in students if x[1] < 70]
print(passing)
print(failing)