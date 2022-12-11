"""The one with the monkey business"""

from functools import reduce

items = [0] * 8
operation = [0] * 8
test = [0] * 8
true = [-1] * 8
false = [-1] * 8

def read():
    # reading from file so that script can be used for any input easily
    for line in open("input.txt").read().split('\n'):
        if 'Monkey' in line:                          
            m = int(line[-2])
        if 'items' in line:
            items[m] = line[18:].split(',')
        if 'Operation' in line:
            operation[m] = line[23:]
        if 'Test' in line:
            test[m] = int(line.split()[-1])
        if 'true' in line:
            true[m] = int(line.split()[-1])
        if 'false' in line:
            false[m] = int(line.split()[-1])

def solve(no_of_rounds, part):
    read()
    count = [0 for _ in range(8)]
    for _ in range(no_of_rounds):
        for m in range(len(items)):
            for item in items[m]:
                val = int(item)
                op = operation[m]
                if 'old' in op:
                    val *= val
                elif '*' in op:
                    val *= int(op.split()[-1])
                elif '+' in operation[m]:
                    val += int(op.split()[-1])
                val %= reduce(lambda x, y: x*y, test)    # not strictly necessary for part 1 but why not
                if part == 1:
                    val //= 3
                if val % test[m] == 0:
                    items[true[m]].append(val)
                else:
                    items[false[m]].append(val)
            count[m] += len(items[m])
            items[m] = []
    count.sort()
    print(count[-1]*count[-2])

solve(20, 1)
solve(10000, 2)