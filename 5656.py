from collections import deque
from copy import deepcopy

def dropAndFall(grid, count, m,n):      
    count = drop(grid, count, m, n)
    grid, top = fall(grid)

    return (count, top)

def fall(grid):
    #print(&quot;testing fall&quot;)
    H = len(grid)
    W = len(grid[0])
    top = [H] * W
    for j in range(W):
    	for i in reversed(range(H)):
            value = grid[i][j]
            if value != 0:
                grid[i][j] = 0
                grid[top[j]-1][j] = value
                top[j] -= 1
    #print(&quot;testing fall over&quot;)
    return(grid, top)

def drop(grid, count, m, n):
#    print(&quot;testing drop&quot;)
    R = grid[m][n] - 1
    
    if R < 0:
        #no change
        return count
    
    grid[m][n] = 0
    count -= 1
    
    if R == 0:
        #print(&quot;only this change&quot;)
        return count
    N = len(grid)
    candidates = [(m,j) for j in range(n - R, n + R + 1) if 0<= j < N  and j != n] + [(i, n) for i in range(m - R, m + R + 1) if 0 <= i < N and i != m]
        
    for candidate in candidates:
        i, j = candidate
        value = grid[i][j]
        if value == 1:
            grid[i][j] = 0
            count -= 1
        if value > 1:
            count = drop(grid, count, candidate[0], candidate[1])

    return count
        
def getNeighbors(grid, count, W, H, top):

    neighbors = []
    for i in range(W):
        if top[i] == H:
            #no more
            continue
        new_grid = deepcopy(grid)
        neighbor = dropAndFall(new_grid, count, top[i], i) #new_count, new_top

        neighbors.append((new_grid, neighbor[0], neighbor[1]))
    return neighbors

def problem5656():
    T = int(input())
    for test in range(1, T+1):
        N, W, H = list(map(int, input().split()))
        
        grid = []
        top = [0] * W
        zeroCount = 0

        for _ in range(H):
            line = list(map(int, input().split()))
            for index, num in enumerate(line):
                if num == 0:
                    zeroCount += 1
                    top[index] += 1
            grid.append(line)

        

        print(top)
        count = W * H - zeroCount
        turn = 0
        initialState = (grid, top, count, turn)
        
        frontier = deque()
        frontier.append(initialState)
        minCount = float("inf")

        while(True):
            state = frontier.popleft()
            grid, top, count, turn = state
            
            #check final turn
            if turn == N:
                break
        
            #iterate through neighbors
            neighbors = getNeighbors(grid, count, W, H, top)

            if not neighbors:
                minCount = 0
                break

            for neighbor in neighbors:
                new_grid, new_count, new_top = neighbor

                neighbor = (new_grid, new_top, new_count, turn + 1)
                frontier.append(neighbor)
                    #frontierSet.add(neighbor)
                
                if new_count < minCount:
                    minCount = new_count
        
        print(minCount)

if __name__ == "__main__": 
    problem5656()
    #[(m,j) for j in range(n - R, n + R + 1) if 0<= j < N] and j != n]
    #[(i, n) for i in range(m - R, m + R + 1) if 0 <= i < N and i != m]
    #res = list(set([(m,i) for i in range(n - R, n + R + 1)] +  [(i, n) for i in range(m - R, m + R + 1)]).remove((i,j)))
    #print(res)