import random
import os
import time
import string
import sys

def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")

def getStartChoice():
    """Q quits at startup, anything else starts"""
    choice = input("Press Enter to start, or Q to quit: ").strip()
    return choice.upper() != "Q"

def generateString(level):
    """Level 1 has 4 uppercase letters, +1 per level"""
    length = 4 + (level - 1)
    return "".join(random.choice(string.ascii_uppercase) for _ in range(length))

def countDown():
    """Five dots, one second apart."""
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(1)
    print()

def flushKeyboard():
    """Removes and keyboard inputs during the countdown"""
    if os.name == "nt":
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getwch()
    else:
        import termios
        import select
        try:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            termios.tcsetattr(fd, termios.TCSANOW, old_settings)
            while select.select([sys.stdin], [], [], 0)[0]:
                sys.stdin.read(1)
        except (termios.error, ValueError):
            pass

def getGuess(target_length):
    """Clears the keyboard inputs, then reads the player input"""
    flushKeyboard()
    while True:
        guess = input("Enter the string: ").strip().upper()
        if len(guess) == target_length and guess.isalpha():
            return guess
        print(f"Enter exactly {target_length} letters.")

def playAgain():
    """Y restarts at Level 1, N exits the program"""
    while True:
        answer = input("Play again? (Y/N): ").strip().upper()
        if answer == "Y":
            return True
        if answer == "N":
            return False
        print("Enter Y or N.")

if getStartChoice():
    playing = True
    while playing:
        level = 1
        completedLevels = 0
        while True:
            print(f"Level: {level}")
            target = generateString(level)
            print(target)
            countDown()
            clearScreen()
            guess = getGuess(len(target))
            if guess == target:
                print("Good job!")
                time.sleep(3)
                completedLevels += 1
                level += 1
            else:
                print("You lost!")
                print(f"Correct string: {target}")
                print(f"Your guess: {guess}")
                print(f"You completed {completedLevels} level(s)")
                break
        playing = playAgain()
    print("Thanks for playing!")
else:
    print("Goodbye!")