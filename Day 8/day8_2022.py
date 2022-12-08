"""The one with the visible trees"""

tree = open("input.txt").read().splitlines()
ROWS, COLS = len(tree), len(tree[0])
part1, part2 = 0, 0
for r in range(ROWS):
    for c in range(COLS):
        is_visible = False
        scenic_score = 1
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            r_end, c_end = r + dr, c + dc
            while 0 <= r_end < ROWS and 0 <= c_end < COLS:
                if tree[r_end][c_end] >= tree[r][c]:
                    break
                r_end, c_end = r_end + dr, c_end + dc
            else:
                r_end, c_end = r_end - dr, c_end - dc 
                is_visible = True
            scenic_score *= abs(r - r_end) + abs(c - c_end)
        if is_visible:
            part1 += 1
        part2 = max(part2, scenic_score)
print(part1, part2)
