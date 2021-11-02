def p1Wins(sticks, p1turn):
    """
    returns True if player1 would win a game of Nim in the current state, and False otherwise.
    On their turn, a player can pick up 1, 2 or 3 sticks from the Nim pile.
    :param sticks: integer.  number of sticks remaining in the pile
    :param p1turn: boolean.  indicates whether it is player1's turn to move
    :return: True if player1 wins in the current state, False otherwise
    """
    if sticks == 1:
        # player1 loses if it is turn, because he must take the last stick
        return not p1turn
    elif sticks <= 4:
        # the player to move has a guaranteed win, because they can leave
        # only 1 stick for the opponent
        return p1turn
    else:
        if p1turn:
            # p1 wins on his turn if he has ANY winning move
            return p1Wins(sticks-1, not p1turn) or p1Wins(sticks-2, not p1turn) or p1Wins(sticks-3, not p1turn)
        else:
            # it's p2's turn, which means p1 will win only if ALL moves lead to a win for p1
            return p1Wins(sticks-1, not p1turn) and p1Wins(sticks-2, not p1turn) and p1Wins(sticks-3, not p1turn)


numsticks = int(input("Enter the number of sticks for nim:"))
print("Will player1 win?")
print(p1Wins(numsticks, True))