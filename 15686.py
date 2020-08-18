from itertools import combinations
import sys
import random
import time

def problem5686():
    N, M, housesLocation, chickenLocation = parse()
    commands = combinations(chickenLocation, M)
    minCount = float("inf")
    for command in commands:
        #mark on grid
        #for location in command:
        #    i,j = location
            #grid[i][j] = 2

        #count
        count = countGrid(command, housesLocation)
        if count < minCount:
            minCount = count
        #unmark
        #for location in command:
        #    i, j = location
        #    grid[i][j] = 0
    print(minCount)

def distance(loc1, loc2):
    i1, j1 = loc1
    i2, j2 = loc2
    return abs(i1-i2) + abs(j1-j2)

def countGrid(command, houseLocation):
    return sum([min([distance(house, chicken) for chicken in command]) for house in houseLocation])

def parse():
    sys.stdin = open("15686.txt", "r")
    N, M = list(map(int, input().split()))
    #grid = [[0 for _ in range(N)] for _ in range(N)]
    housesLocation = []
    chickenLocation = []
    for i in range(N):
        line = list(map(int, input().split()))
        for j, num in enumerate(line):
            if num == 1:
                housesLocation.append((i,j))
                #grid[i][j] = 1
            elif num == 2:
                chickenLocation.append((i,j))
                # do not mark them on the grid

    return (N, M, housesLocation, chickenLocation)

def randomTestGeneration(N, M, houseCount, chickenCount):
    sys.stdout = open("15686.txt", "w")
    zeroCount = N * N - houseCount - chickenCount
    candidate = [0] * zeroCount + [1] * houseCount + [2] * chickenCount

    assert len(candidate) == N * N

    shuffle = random.sample(candidate, len(candidate))

    assert len(shuffle) == len(candidate)

    print("{} {}".format(N, M))
    for i in range(N):
        print(" ".join(map(str, shuffle[i* N:i*N + N])))

if __name__ == "__main__":
    count = 0
    while count < 10000:
        start = time.time()
        randomTestGeneration(50, 13, 100, 13)
        problem5686()
        end = time.time()
        assert start - end < 2.0
        count += 1