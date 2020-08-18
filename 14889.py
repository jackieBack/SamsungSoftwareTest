from itertools import combinations, product

def teamScore(grid, team):
    twins = [(i,j) for i,j in product(team, repeat=2) if i != j]
    res = 0
    for twin in twins:
        res += grid[twin[0]][twin[1]]
    return res

def calDiff(grid, team):
    N = len(grid)
    oppo = [index for index in range(N) if index not in team]
    return abs(teamScore(grid, team) - teamScore(grid, oppo))

def problem14889():
    N = int(input())
    grid = []
    for _ in range(N):
        line = list(map(int, input().split()))
        grid.append(line)

    #command = [0] * int(N/2) + [1] * int(N/2)
    minGap = float("inf")
    iterable = combinations(range(N), r=int(N/2))
    for it in iterable:
        diff = calDiff(grid, it)
        if diff < minGap:
            minGap = diff
        if it[0]:
            break
    
    print(minGap)

if __name__ == "__main__":
    
    problem14889()
    grid = [0,1,4,8]
    team = (1,2)
    #calDiff(grid, team)
