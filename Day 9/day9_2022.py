"""The one with the rope bridge/The one with the snake"""

d = {"U": +1j, "D": -1j, "L": -1, "R": +1}
rope = [0 + 0j] * 10
seen_1, seen_9 = {rope[1]}, {rope[-1]}

for line in open("input.txt").read().splitlines():
    dir, steps = line.split()

    for _ in range(int(steps)):
        for i in range(len(rope)):
            if i == 0:
                rope[i] += d[dir]
                continue

            if abs(diff := rope[i - 1] - rope[i]) >= 2:
                if (a := abs(diff.real)) > 0:
                    rope[i] += complex(diff.real / a, 0)
                if (a := abs(diff.imag)) > 0:
                    rope[i] += complex(0, diff.imag / a)

        seen_1.add(rope[1])
        seen_9.add(rope[-1])

print(len(seen_1))
print(len(seen_9))