from collections import defaultdict, deque
from operator import itemgetter
from itertools import product, compress
from copy import deepcopy
import math
directions = [(-1,0), (0,1), (1,0), (0,-1)]

block = [
    [2, 3, 1, 0],
    [1,3,0,2],
    [3,2,0,1],
    [2,0,3,1]]


# UP Right Down Left
class GRID:
    def __init__(self, grid, wormhole):
        self.grid = grid
        self.wormhole = wormhole
        self.N = len(grid)

    def getCount(self, start, directionIndex):
        #start : (i, j)
        #direction : from directions
        #output : score from that iteration of pinball game
        score = 0
        i, j = start
        gettingStarted = True
        count = 0

        while(True):
            #print("location: {},{}".format(i,j))

            if i == start[0] and j == start[1]:
                if not gettingStarted:
                    return score
                gettingStarted = False

            if i < 0 or i >= self.N or j < 0 or j >= self.N:
                score += 1
                directionIndex = (directionIndex + 2) % 4
                di, dj = directions[directionIndex]
                i += di
                j += dj
                continue
            value = self.grid[i][j]
            if value == -1:
                #blackhole
                return score
            elif 6 <= value <= 10:
                #wormhole
                #print("wormhole")

                candidates = self.wormhole[value]
                #print(candidates)
                for candidate in candidates:
                    if i == candidate[0] and j == candidate[1]:
                        x = 5
                    else:
                        i, j = candidate
                        break
            elif 1 <= value <= 4:
                #block
                score += 1
                directionIndex = block[value-1][directionIndex]
            elif value == 5:
                #block - reverse direction
                score += 1
                directionIndex = (directionIndex + 2) % 4

            di, dj = directions[directionIndex]
            i += di
            j += dj            
             
def problem5650():
    T = int(input())
    for test in range(1 , T+1):
        N = int(input())
        grid = []
        wormhole = defaultdict(list)
        spaces = []
        for i in range(N):
            line = list(map(int, input().split()))
            for j, num in enumerate(line):
                if num == 0:
                    #0 space 
                    spaces.append((i,j))
                if 6 <= num <= 10:
                    #this is wormhole
                    wormhole[num].append((i,j))
            grid.append(line)

        pinball = GRID(grid, wormhole)

        #do some search algorithm        
        #result = pinball.getCount((2, 3), 1)
        #print(result)
        
        #using dynamic programming
        #memo = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]
        maxCount = 0
        for space in spaces:
            i, j = space
            for dir in range(4):
                count = pinball.getCount(space, dir)
                if count > maxCount:
                    maxCount = count
        print("#{} {}".format(test, maxCount))

moves = [(0,0), (-1, 0), (0,1), (1, 0), (0,-1)]

def distance(loc1, loc2):
    #calculate manhattan distance
    i, j = loc1
    l, m = loc2
    return abs(i - l) + abs(j - m)

def problem5644():
    T = int(input())
    for test in range(1 , T+1):
        M, A = list(map(int, input().split()))
        traj1 = list(map(int, input().split()))
        traj2 = list(map(int, input().split()))
        towers = []
        for i in range(A):
            line = list(map(int, input().split()))
            towers.append( [(line[1]-1, line[0]-1), line[2], line[3]])
        grid = [[0 for _ in range(10)]for _ in range(10)]
        #mark grid
        for i in range(10):
            for j in range(10):
                value = []
                for index, tower in enumerate(towers):
                    towerLoc = tower[0]
                    dist = distance((i,j), towerLoc)
                    if dist <= tower[1]:
                        #tower within distance
                        value.append((index, tower[2]))
                if value:
                    value.sort(key=itemgetter(1), reverse=True)
                grid[i][j] = value
        #print(grid)
        #loop through time
        time = 0
        start1 = (0,0)
        start2 = (9,9)
        i,j = start1
        l,m = start2
        result = 0
        while time <= M:
            #print("1: {},{}".format(i,j))
            #print("2: {},{}".format(l,m))
            value1 = grid[i][j]
            value2 = grid[l][m]
            #print(value1)
            #print(value2)

            if len(value1) != 0 and len(value2) != 0:
                maxSum = 0
                for item1 in value1:
                    for item2 in value2:
                        index1, power1 = item1
                        index2, power2 = item2
                        if index1 == index2:
                            summ = power1
                        else:
                            summ = power1 + power2
                        if summ > maxSum:
                            maxSum = summ
                result += maxSum
            else:
                #one of the  is missing
                if len(value1) == 0 and len(value2) != 0:
                    res2 = value2[0][1]
                    result += res2
                elif len(value2) == 0 and len(value1) != 0:
                    res1 = value1[0][1]
                    result += res1

            #move next step
            if time != M:
                move1 = moves[traj1[time]]
                di, dj = move1
                i += di
                j += dj
                move2 = moves[traj2[time]]
                dl, dm = move2
                l += dl
                m += dm

            time += 1
        
        print("#{} {}".format(test,result))

def getCount(distance, height, coms):
    height0, height1 = height
    to1 = sorted([dist[1] for dist, com in zip(distance, coms) if com])
    to0 = sorted([dist[0] for dist, com in zip(distance, coms) if not com])

    return max(time(to0, height0), time(to1, height1))

def time(dis, height):
    if not dis:
        return 0
    elif len(dis) <= 3:
        return dis[-1] + height + 1

    index = (len(dis)-1) % 3 
    start = index + 3
    count = dis[index]
    for i in range(start, len(dis), 3):
        count = max(count + height, dis[i])
    count = count + height + 1
    #print(count)
    return count

def Dis(loc1, loc2):
    i, j = loc1
    k, m = loc2
    return abs(i - k) + abs(j - m)

def problem2383():
    T = int(input())
    for test in range(1, T+1):
        N = int(input())

        grid = []
        persons = []
        stairs = []
        stairHeight = []
        for i in range(N):
            line = list(map(int, input().split()))
            for j, num in enumerate(line):
                if num == 1:
                #person
                    persons.append((i,j))
                elif num != 0:
                    #stair
                    stairHeight.append(num)
                    stairs.append((i,j))
            grid.append(line)
        
        distance = [[0 for _ in range(2)] for _ in range(len(persons))]
        for i, person in enumerate(persons):
            for j, stair in enumerate(stairs):
                d = Dis(person, stair)
                distance[i][j] = d
        #print(distance)
        #generate 2^N kinds of permutations
        #there will be only two stairs --> stored in binary 0 and 1
        minCount = float("inf")
        commands = product([0,1], repeat=len(persons))

        for com in commands:
            #dir = 1 * N length list
            count = getCount(distance, stairHeight, com)
            if count < minCount:
                minCount = count

        print("#{} {}".format(test, minCount))
        


"""
class cell:
    def __init__(self, loc, num, direction, N):
        self.loc = loc
        self.num = num
        self.direction = direction
        self.N = N

    def move():
        #move to next step, change num and direction if at edge
        i, j = self.loc
"""

directions = [(-1,0), (1,0), (0,-1), (0,1)]
directionChange = [ 1, 0, 3, 2]

def merge(grid, cellLocations):
    for location in cellLocations:
        i, j = location
        value = grid[i][j]

        if len(value) > 1:
            #merge
            value.sort(key=itemgetter(0), reverse=True)
            dir = value[0][1]
            count = sum([num[0] for num in value])
            new_value = (count, dir)
            grid[i][j] = new_value
        elif len(value) == 1:
            new_value = value[0]
            grid[i][j] = new_value

    return grid

def problem2382():
    T = int(input())
    for test in range(1 , T+1):
        N, M, K = list(map(int, input().split()))
        grid = [[0 for _ in range(N)] for _ in range(N)]
        #pad grid
        #for i in range(N):
        #    for j in range(N):
        #        if i == 0 or j == 0 or i == N - 1 or j == N - 1:
        #            grid[i][j] = -1

        #input cells
        cellLocations = []
        for _ in range(K):
            line = list(map(int, input().split()))
            grid[line[0]][line[1]] = (line[2], line[3] -1 )
            cellLocations.append( (line[0], line[1]) )
        #for i in range(N):
        #    print(grid[i])
        
        #print(cellLocations)
        #loop through time
        time = 0
        while time != M:
            new_grid = [[0 for _ in range(N)] for _ in range(N)]
            new_cellLocations = []

            #for i in range(N):
            #    print(grid[i])

            #print(cellLocations)

            for cellLocation in cellLocations:
                i, j = cellLocation
                #print(cellLocation)
                cell = grid[i][j]
                #print(cell)
                count, directionIndex = cell
                di, dj = directions[directionIndex]
                i += di
                j += dj

                new_cellLocations.append((i,j))

                #update direction, count if at edge
                if i == 0 or j == 0 or i == N - 1 or j == N - 1:
                    directionIndex = directionChange[directionIndex]
                    count = int(count / 2)

                #update grid
                new_cell = (count, directionIndex)
                if new_grid[i][j]:
                    new_grid[i][j].append(new_cell)
                else:
                    new_grid[i][j] = [new_cell]

            grid = new_grid

            cellLocations = list(set(new_cellLocations))

            #merge
            grid = merge(grid, cellLocations)

            #print(cellLocation)


            time += 1

        #count sum
        count = 0
        for cellLocation in cellLocations:
            i, j = cellLocation
            count += grid[i][j][0]
        print("#{} {}".format(test, count))

def cost(K):
    return K * K + (K - 1) * (K - 1)

def manDist(i,j,l,m):
    return abs(i - l) + abs(j - m)

def findCount(grid, loc, k, M, maxHouseCount):
    i, j = loc
    N = len(grid)
    #generate all possible locations tuples
    candidates = [ (l,m) for l,m in product(range(i-k+1, i+k), range(j-k+1, j+k)) if 0<= l < N and 0<= m < N and manDist(i,j,l,m) <= k-1]
    #print(candidates)
    total = len(candidates)
    minHouse = math.ceil(cost(k)/ M)
    #print("minHouse: {}".format(minHouse))
    #print("maxHouseSoFar: {}".format(maxHouseCount))
    threshold = max(minHouse, maxHouseCount)
    #print("threshold: {}".format(threshold))
    
    houseSoFar = 0

    for countSoFar, candidate in enumerate(candidates):
        i,j = candidate
        value = grid[i][j]
        if value:
            houseSoFar += 1
        if total - (countSoFar+1) < threshold - houseSoFar:
            return -1
    
    return houseSoFar

def problem2117():
    T = int(input())
    for test in range(1, T + 1):
        N, M = list(map(int, input().split()))
        H = 0 
        grid = []
        locations = []
        for i in range(N):
            line = list(map(int, input().split()))
            grid.append(line)
            for j, num in enumerate(line):
                if num == 1:
                    H += 1
                    locations.append((i,j))

        #print(M)
        #assume that K = 1 case is always met
        
        #find maxK

        if H == 1:
            print("#{} 1".format(test))
            continue

        K = 2
        maxHouseCount = 1
        thisRoundFlag = True
        profitable = True
        while True:
            if cost(K) > H * M:
                profitable = False
                break
            #print("K: {}".format(K))
            thisRoundFlag = False
            for i in range(N):
                for j in range(N):
                    loc = (i,j)
                    count = findCount(grid, loc, K, M, maxHouseCount)
                    if count >= maxHouseCount:
                        maxHouseCount = count
                        thisRoundFlag = True
            K += 1    
            #print("maxHouse: {}".format(maxHouseCount))
        print("#{} {}".format(test, maxHouseCount))
        
def checkGrid(grid, K):
    D = len(grid)
    W = len(grid[0])
    for j in range(W):
        prev = grid[0][j]
        count = 1
        flag = False
        for i in range(1, D):
            if prev == grid[i][j]:
                count += 1
                if count == K:
                    #found it - next col
                    flag = True
                    break
            else:
                count = 1
            prev = grid[i][j]
        if not flag:
            #not found
            return False
    return True

#minApply = float("inf")

def search(grid, i, apply, K):
    global minApply
    
    #print("i: {}".format(i))
    #print("apply: {}".format(apply))
    #print("minApply: {}".format(minApply))

    W = len(grid[0])

    if checkGrid(grid, K):
        if apply < minApply:
            minApply = apply
            return -1
            
    if i == len(grid):
        #end of film
        return -1

    if apply > minApply:
        #no need to look
        return -1

    search(grid, i+1, apply, K)

    temp = grid[i].copy()
    grid[i] = [0 for _ in range(W)]
    search(grid, i+1, apply + 1, K)
    grid[i] = temp

    grid[i] = [1 for _ in range(W)]
    search(grid, i+1, apply + 1, K)
    grid[i] = temp

def problem2112():
    T = int(input())
    for test in range(1, T+1):
        
        D, W, K = list(map(int, input().split()))
        grid = []
        for _ in range(D):
            line = list(map(int, input().split()))
            grid.append(line)
        
        #check original state

        if K == 1:
            print("#{} 0".format(test))
            continue

        if checkGrid(grid, K):
            print("#{} 0".format(test))
            continue

        #generate 3^N 
        #commands = product([0,1,2], repeat=D)
        global minApply
        minApply = float("inf")
        search(grid, 0, 0 ,K)
        
        """
        for command in commands:
            apply = len(command) - command.count(2)
            if apply > minApply:
                continue

            #transform grid
            indexs = [index for index, num in enumerate(command) if num != 2]

            store = deepcopy([row for index, row in enumerate(grid) if index in indexs])
            for index in indexs:
                AB = command[index]
                grid[index] = [AB for _ in range(W)]
            #print("before")
            #print(grid)
            #check grid
            if checkGrid(grid, K):
                if apply < minApply:
                    minApply = apply
            
            #return original
            for row, index in zip(store, indexs):
                grid[index] = row
            #print("after")
            #print(grid)
        """
        print("#{} {}".format(test, minApply))

def problem5656():
            

if __name__ == "__main__":
    #problem2112()
    grid = [
        [1,[100, 100, 100],1,1],
        [2,3,4,5],
        [2,2,4,1],
        [2,2,1,5],
    ]
    #print(checkGrid(grid, 3))
    temp = grid[0] # 1 1 1 1
    print(temp)

    grid[0] = 1
    print(grid)
    print(temp)

