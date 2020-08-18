import sys

def distance(loc1, loc2):
    i1, j1 = loc1
    i2, j2 = loc2
    return abs(i1-i2) + abs(j1-j2)

def probelm16236():
    N, grid, fish, shark = parse()

    size = 2
    i, j = shark
    steps = 0

    while True:
        move = findMoves(grid, i, j, size)
        if not moves:
            #no available move
            break

        #available move
        


def parse():
    sys.stdin = open("16236.txt", "r")
    N = int(input())
    grid = []
    fish = []
    for i in range(N):
        line = list(map(int, input().split()))
        for j, num in enumerate(line):
            if num == 9:
                shark = (num, i,j)
            elif 1 <= num <= 6:
                grid[i][j] = num
                fish.append((i,j))

    return (N, grid, fish, shark)