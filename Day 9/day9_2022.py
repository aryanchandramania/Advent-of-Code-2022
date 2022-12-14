"""The one with the rope bridge/The one with the snake  """

directions = {"U": +1j, "D": -1j, "L": -1, "R": +1}
rope = [0 + 0j] * 10
seen_1, seen_9 = {rope[1]}, {rope[-1]}

for line in open("input.txt").read().splitlines():
    d, steps = line.split()

    for _ in range(int(steps)):
        for i in range(len(rope)):
            if i == 0:
                rope[i] += directions[d]
                continue

            if abs(diff := rope[i - 1] - rope[i]) >= 2:
                if (movement := abs(diff.real)) > 0:
                    rope[i] += complex(diff.real / movement, 0)
                if (movement := abs(diff.imag)) > 0:
                    rope[i] += complex(0, diff.imag / movement)

        seen_1.add(rope[1])
        seen_9.add(rope[-1])

print(len(seen_1))
print(len(seen_9))