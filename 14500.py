from copy import deepcopy

class GRID:
    def __init__(self, grid):
        self.grid = grid

    def rotate(self):
        #rotate grid by 90 degrees left
        temp = [[0 for _ in range(len(self.grid))] for _ in range(len(self.grid[0]))]

        for i in range(len(self.grid[0])):
            for j in range(len(self.grid)):
                temp[i][j] = self.grid[j][len(self.grid[0]) - i - 1]

        self.grid = deepcopy(temp)

    def count1(self):
        #count 4 x 1 blocks in grid
        N = len(self.grid)
        M = len(self.grid[0])

        maxSum = float("-inf")
        for i in range(N - 4 + 1):
            for j in range(M):
                temp = sum([self.grid[i][j],
                self.grid[i+1][j],
                self.grid[i+2][j],
                self.grid[i+3][j]])

                #print(temp)

                if maxSum < temp:
                    maxSum = temp
        
        self.rotate()
        N = len(self.grid)
        M = len(self.grid[0])

        for i in range(N - 4 + 1):
            for j in range(M):
                temp = sum([self.grid[i][j],
                self.grid[i+1][j],
                self.grid[i+2][j],
                self.grid[i+3][j]])

                #print(temp)

                if maxSum < temp:
                    maxSum = temp
        
        return maxSum
    def count2(self):
        #count 2 x 2 blocks in grid
        N = len(self.grid)
        M = len(self.grid[0])

        maxSum = float("-inf")
        for i in range(N - 2 + 1):
            for j in range(M - 2 + 1):
                temp = sum([self.grid[i][j],
                self.grid[i+1][j],
                self.grid[i][j+1],
                self.grid[i+1][j+1]])

                if maxSum < temp:
                    maxSum = temp
        
        return maxSum
    def count3(self):
        #count three kinds 3 x 2 blocks in grid

        maxSum = float("-inf")

        for _ in range(4):
            N = len(self.grid)
            M = len(self.grid[0])
            for i in range(N - 3 + 1):
                for j in range(M - 2 + 1):
                    list1 = [self.grid[i][j],
                    self.grid[i+1][j],
                    self.grid[i+2][j],
                    self.grid[i][j+1]]

                    list2 = [self.grid[i][j],
                    self.grid[i+1][j],
                    self.grid[i+2][j],
                    self.grid[i+1][j+1]]

                    list3 = [self.grid[i][j],
                    self.grid[i+1][j],
                    self.grid[i+2][j],
                    self.grid[i+2][j+1]]

                    list4 = [self.grid[i][j],
                    self.grid[i+1][j],
                    self.grid[i+1][j+1],
                    self.grid[i+2][j+1]]

                    temp = max(sum(list1), sum(list2), sum(list3), sum(list4))

                    if maxSum < temp:
                        maxSum = temp
            self.rotate()

        return maxSum
def problem14500():
    N, M = list(map(int, input().split()))
    #print("{} {}".format(N, M))

    grid = []
    for _ in range(N):
        line = list(map(int, input().split()))
        grid.append(line)

    #print(grid)
    tetro = GRID(grid)

    #print(tetro.grid)

    #tetro.rotate()

    #print(tetro.grid)

    max1 = tetro.count1()
    #print(max1)
    max2 = tetro.count2()
    #print(max2)
    max3 = tetro.count3()
    #print(max3)
    print(max(max1, max2, max3))

if __name__ == "__main__":
    problem14500()