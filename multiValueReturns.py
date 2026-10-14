# In python, a function can return mutliple values using one return statement.
# When the interpreter encounters a return statement in a function, control is sent back
# to the calling code.

# returning multiple values:
def getPlayerStats():
    name = "Big Boy Bartholomew Jameson Jr."
    score = 95
    level = 3

    return name, score, level

playerName, playerScore, playerLevel = getPlayerStats()

print(playerName)
print(playerScore)
print(playerLevel)

# get values as tuple:
player = getPlayerStats()
print(player)
print(player[0])

# values can be ignored

pname, _, plevel = getPlayerStats() # note: _ is only a convention in python
print(pname)
print(_)
print(pname)