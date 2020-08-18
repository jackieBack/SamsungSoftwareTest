from collections import Counter
import sys
from operator import itemgetter
import random
import time

def problem17140():
    r, c, K, grid = parse()
    time = 0
    #new_grid = grid
    noFind = False
    while True:
        if 0<= r < len(grid) and 0<= c < len(grid[0]) and grid[r][c] == K:
            break
        R = len(grid)
        C = len(grid[0])
        if R >= C:
            grid = list(map(flatten, [
                sorted([(key, value) for key, value in Counter(grid[i]).items() if key != 0], key=itemgetter(1, 0)) for i in range(R)]))
            maxLen = min(100, max([len(grid[i]) for i in range(R)]))
            for i in range(R):
                if maxLen - len(grid[i]) > 0:
                    grid[i].extend([0] * (maxLen - len(grid[i])))
        else:
            grid = list(zip(*grid))
            grid = list(map(flatten, [sorted([(key, value) for key, value in Counter(grid[i]).items() if key != 0],key=itemgetter(1,0)) for i in range(C)]))
            maxLen = min(100, max([len(grid[i]) for i in range(C)]))
            for i in range(C):
                if maxLen - len(grid[i]) > 0:
                    grid[i].extend([0] * (maxLen - len(grid[i])))
            grid = list(zip(*grid))
        time += 1
        if time > 100:
            noFind = True
            break
    if noFind:
        print(-1)
    else:
       print(time)

def flatten(input):
    return [element for t in input for element in t]

def parse():
    sys.stdin = open("17140.txt", "r")
    R, C, K = list(map(int, input().split()))
    grid = []
    for _ in range(3):
        line = list(map(int, input().split()))
        grid.append(line)
    return R-1, C-1, K, grid

def randomTestGenerator(r, c, k):
    sys.stdout = open("17140.txt", "w")
    print("{} {} {}".format(r, c, k))
    for _ in range(3):
        print(" ".join(list(map(str, [random.randint(1, 10) for _ in range(3)]))))

if __name__ == "__main__":
    for _ in range(10000):
        start = time.time()
        randomTestGenerator(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
        problem17140()
        end = time.time()
        assert end - start < 0.5
    #print("finished")
    """x    line = [3 ,1 ,1 ,2 ,3]

    counter = Counter(line)
    new_list = []
    for key, value in counter.items():
        new_list.append(key)
        new_list.append(value)


    print(counter)"""