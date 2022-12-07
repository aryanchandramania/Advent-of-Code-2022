"""The one with the tree structure"""
import collections

directory_tree = collections.defaultdict(int)
pwd = ""

for line in open('input.txt').readlines()[1:]:
    if '..' in line:
        pwd = pwd[:pwd.rindex('/')]
    elif '$ cd' in line:
        pwd = pwd + '/' + line[5:]
    elif line.split(' ')[0].isnumeric():
        cwd = pwd
        directory_tree[""] += int(line.split(' ')[0])
        while cwd:
            directory_tree[cwd] += int(line.split(' ')[0])
            if '/' in cwd:
                cwd = cwd[:cwd.rindex('/')]
            else:
                cwd = ""

print(sum([v for v in directory_tree.values() if v <= 100000]))
minimum_to_free = directory_tree[""] + 30000000 - 70000000
print([x for x in sorted(directory_tree.values()) if x - minimum_to_free > 0][0])
