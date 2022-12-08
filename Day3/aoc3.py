data = open("input.txt").read()
beta = "abcdefghijklmnopqrstuvwxyz"
p1 = p2 = 0
for i, r in enumerate(data.strip().split("\n")):
    c1, c2 = set(r[:len(r)//2]), set(r[len(r)//2:])
    pack = c1.intersection(c2).pop()
    p1 += beta.find(pack.lower()) + 1 if pack.islower() else beta.find(pack.lower()) + 27
    group = set(r) if i % 3 == 0 else group.intersection(r)
    if i % 3 == 2:
        group = group.pop()
        p2 += beta.find(group.lower()) + 1 if group.islower() else beta.find(group.lower()) + 27

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")