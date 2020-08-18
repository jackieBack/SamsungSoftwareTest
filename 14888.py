from itertools import permutations

operators = ['+', '-', '*', '/']
def calculate(A, op):
    res = A[0]
    for index, operator in zip(range(1, len(A)), op):
        a = A[index]
        if operator == 0:
            res += a
            continue
        elif operator == 1:
            res -= a
            continue
        elif operator == 2:
            res *= a
            continue
        else:
            if res >= 0:
                res = int(res / a)
            else:
                res = 0 - int(abs(res) / a)
    
    return res

def mod_permuations(ops):
    saw = set()
    for p in permutations(ops):
        if p in saw:
            continue
        saw.add(p)
        yield p

def problem14888():
    N = int(input())
    A = list(map(int, input().split()))
    ops = list(map(int, input().split()))

    command = []
    for count, operator in zip(ops, range(4)):
        command.extend([operator] * count)
    
    maxCount = float("-inf")
    minCount = float("inf")

    iterable = mod_permuations(command)
    
    for it in iterable:
        count = calculate(A, it)
        if count > maxCount:
            maxCount = count
        if count < minCount:
            minCount = count

    print(maxCount)
    print(minCount)

if __name__ == "__main__":
    problem14888()

    num = [1,2,3,4,5,6]
    ops = [1,3,0,0,2]
    ops2 = [0,0,3,1,2]
    #['-','/','+','+','*']
    #print(calculate(num, ops2))
