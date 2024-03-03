# Program: A table has some blocks were each player check two boxes and the player who can't find two boxes loses
# Instuctions:
# BOX_NUMBER SPACE DIRECTION(r,l,u,d)
# Box Number as shown in the table
# Space is required between the number and direction
# Directions are right,left,up,down


# Regex library to search for a pattern in a text
import re
# The squares list, where True is checked
squares = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

print("Description: Each player must check two squares till a player can't then the other wins")
print("The valid input from: BOX_NUMBER SPACE DIRECTION(r,l,u or d)")
print("r: right, l:left, u:up, d:down")
print("Example: \"3 d\"")
# The square 1 and square 2 are false
def rFalse(i1,i2):
    return not (squares[i1] or squares[i2])
# return True if an index is at the left edge
def leftEdge(n):
    if n%4 == 0:
        return True
    else:
        return False
# return True if an index is at the right edge
def rightEdge(n):
    if n%4 == 3:
        return True
    else:
        return False
# Take a text "index move" and check it's valid
def validSquares(txt):
    # Make sure the pattern is right
    if not re.search("^(?:[1-9]|1[0-6]) [rlud]$",txt):
        return False
    sq1 = (txt.split()[0])
    sq1 = int(sq1)
    # Because the index is zero based and the user enters a one based index
    sq1 -= 1
    move = txt.split()[1]
    # Move to the left
    if move == 'l':
        if not leftEdge(sq1):
            sq2 = sq1
            sq1 -=1
            if rFalse(sq1,sq2):
                return True
    # Move to the right
    elif move == 'r':
        if not rightEdge(sq1):
            sq2 = sq1 + 1
            if rFalse(sq1,sq2):
                return True
    # Move upward
    elif move == 'u':
        if sq1 > 3:
            sq2 = sq1
            sq1 -= 4
            if rFalse(sq1,sq2):
                return True
    # Move downward
    elif move == 'd':
        if sq1 < 12:
            sq2 = sq1 + 4
            if rFalse(sq1,sq2):
                return True
    # Else than all this returns False
    return False
# Marking a square with moving it
def mark(txt):
    if not validSquares(txt):
        return False
    sq1 = int(txt.split()[0]) - 1
    move = txt.split()[1]
    # Move to the left
    if move == 'l':
        sq2 = sq1
        sq1 -=1
        squares[sq1]=True
        squares[sq2]=True
        return True
    # Move to the right
    elif move == 'r':
        sq2 = sq1 + 1
        squares[sq1]=True
        squares[sq2]=True
        return True
    # Move downward
    elif move == 'd':
        sq2 = sq1 + 4
        squares[sq1]=True
        squares[sq2]=True
        return True
    # Move upward
    elif move == 'u':
        sq2 = sq1
        sq1 -= 4
        squares[sq1]=True
        squares[sq2]=True
        return True
    return False
# Show the list as a table like
def showit():
    print()
    for i in range(4):
        for ii in range(4):
            print("[x]" if squares[ii+i*4] else f"[{ii+i*4+1}]",end='\t')
        print("")
    print()
# Check that there is now other possible two squares can be entered
def noMore():
    for i in range(16):
        for ii in "rlud":
            if validSquares(str(i)+' '+ii):
                return False
    return True
# The main program
while not noMore():
    # Guessing the input to make it not valid and the while loop starts like do while
    thein = "1 l"
    # Guessing that the player 1 didn't play
    p1played = False
    # A while loop till player one inserts a valid input
    while not validSquares(thein):
        showit()
        if p1played: print("\nInvalid input\n")
        p1played = True
        thein = input("Player 1 must check: ")
    mark(thein)
    # If there is no more games then player one wins
    if noMore():
        print("\n"+"#"*20+"\nPlayer 1 wins &_&\n"+"#"*20)
        break
    thein = "1 l"
    p2played = False
    # A while loop till player two inserts a valid input
    while not validSquares(thein):
        showit()
        if p2played : print("\nInvalid input\n")
        p2played = True
        thein = input("Player 2 must check: ")
    mark(thein)
    # If there is no more games then player two wins
    if noMore():
        print("\n"+"#"*20+"\nPlayer 2 wins &_&\n"+"#"*20)
        break
