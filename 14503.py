directions = [(-1,0), (0,1), (1,0), (0,-1)]
rotation = [3,0,1,2]

def problem14503():
    N, M = list(map(int, input().split()))
    i, j, d = list(map(int, input().split()))

    grid = []
    for _ in range(N):
        line = list(map(int, input().split()))
        grid.append(line)
    
    currentLoc = (i,j)
    currentD = d
    #cleaned = []
    cleaned = set()
    count4 = 0
    while True:
        i,j = currentLoc
        #print("currentLoc: {}, {}".format(i,j))
        #print("direction: {}".format(currentD))
        #clean currentLoc
        #if currentLoc not in cleaned:
        cleaned.add(currentLoc)
        #cleaned.add(currentLoc)

        #check left
        left = rotation[currentD]
        left_di, left_dj = directions[left]

        #2a
        if d % 2:
            #<-, -> : check j 
            if  grid[i+left_di][j+left_dj] != 1 and (i+left_di,j+left_dj) not in cleaned:
                i += left_di
                j += left_dj
                currentD = left
                currentLoc = (i,j)
                count4 = 0
                continue
        else:
            #^ v : check i
            if  grid[i+left_di][j+left_dj] != 1 and (i+left_di,j+left_dj) not in cleaned:
                i += left_di
                j += left_dj
                currentD = left
                currentLoc = (i,j)
                count4 = 0
                continue

        #2b
        currentD = rotation[currentD]
        count4 += 1

        if count4 == 4:
            #go back
            back = rotation[rotation[currentD]]
            back_di, back_dj = directions[back]
            if back % 2:
            #<-, -> : check j 
                if grid[i+back_di][j+back_dj] != 1:
                    i += back_di
                    j += back_dj
                    currentLoc = (i,j)
                    count4 = 0
                    continue
                break
            else:
            #^ v : check i
                if grid[i+back_di][j+back_dj] != 1:
                    i += back_di
                    j += back_dj
                    currentLoc = (i,j)
                    count4 = 0
                    continue
                break
    #count = 1
    #for loc in cleaned:
    #    i, j = loc
    #    grid[i][j] = count
    #    count += 1
    
    #for i in range(N):
    #    print(grid[i])
    print(len(cleaned))


if __name__ == "__main__":
    problem14503()