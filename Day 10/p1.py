"""The one with the CRT display"""

lines = open("input.txt").read().splitlines()
count = 1
interesting = 20
strength = 0
x = [1]

def check(y):
    global count, interesting, x, strength
    count += 1
    x.append(x[-1] + y)
    if count == interesting:
        strength += x[-1]*count
        interesting += 40

for line in lines:
    check(0)
    if 'addx' in line:
        check(int(line[5:]))

print(strength)

cycle = 0
while cycle < len(x):
    if abs(x[cycle] - (cycle % 40)) < 2:
        print('\u2588', end='')
    else:
        print(' ', end='')
    cycle += 1
    if cycle % 40 == 0:
        print("")
