import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: largeur du batiment (y).
# h: longueur du batiment (x).
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
batmanPos = [x0,y0]
buildHeight = [w,h]

# game loop
while True:
    batmanPos = [int(w/2),int(h/2)]
    print(batmanPos[0],batmanPos[1])
    print("w = ",buildHeight[0], file=sys.stderr, flush=True)
    print("h = ",buildHeight[1], file=sys.stderr, flush=True)
    jumpDown = 0
    jumpRight = 0
    rounds = 1

    for rounds in range(n):
        bomb_dir = input()    # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
        jumpUp = buildHeight[1] - (buildHeight[1]/rounds)
        jumpDown = jumpDown + (buildHeight[1]/rounds)
        jumpRight = jumpDown + (buildHeight[0]/rounds)
        jumpLeft = buildHeight[0] - (buildHeight[0]/rounds)
        if   bomb_dir == "U":
            print(jumpUp)
        elif bomb_dir == "UR":
            print(jumpUp,jumpRight)
        elif bomb_dir == "R":
            print(jumpRight)
        elif bomb_dir == "DR":
            print(jumpDown,jumpRight)
        elif bomb_dir == "D":
            print(jumpDown)
        elif bomb_dir == "DL":
            print(jumpDown,jumpLeft)
        elif bomb_dir == "L":
            print(jumpLeft)
        elif bomb_dir == "UL":
            print(jumpUp,jumpLeft)
        rounds = rounds * 2
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)