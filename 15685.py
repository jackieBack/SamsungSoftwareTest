import sys

directions = [(1,0), (0,-1), (-1,0),(0,1)]

def problem15685():
    N, dragons = parse()

    grid = [[0 for _ in range(101)] for _ in range(101)]

    #represent dragons on grid
    grid, explored = represent(grid, dragons)

    #count squares on grid
    count = countGrid(grid, explored)
    print(count)

def represent(grid, dragons):
    explored = []
    for index, dragon in enumerate(dragons):
        path = []
        x, y, directionIndex, generations = dragon
        explored.append((x,y))
        currentx, currenty = x, y
        grid[currenty][currentx] = 1
        currentD = directionIndex
        for generation in range(generations+1):
            new_path = []
            if generation == 0:
                new_path.append(currentD)
            else:
                new_path = list(map(turn, reversed(path)))
            for direction in new_path:
                dx, dy = directions[direction]
                currentx += dx
                currenty += dy
                grid[currenty][currentx] = 1
                explored.append((currentx, currenty))
            path.extend(new_path)
    explored = list(set(explored))
    return (grid, explored)
def turn(direction):
    return (direction + 1) % 4

def countGrid(grid, explored):
    #return count of squares in grid
    #explored - set
    count = 0
    for location in explored:
        x, y = location
        if x == 100 or y == 100:
            #edge case
            continue

        #check down / left / down left
        if grid[y][x] == 1 and grid[y+1][x] == 1 and grid[y][x+1] == 1 and grid[y+1][x+1] == 1:
            count += 1
    return count

def parse():
    #sys.stdin = open("15685.txt", "r")
    N = int(input())
    dragons = []
    for _ in range(N):
        line = list(map(int, input().split()))
        dragons.append(line)
    return (N, dragons)

if __name__ == "__main__":
    problem15685()