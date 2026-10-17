"""Step 0: classify the 720 orderings into stabilizer groups (edge model, L=4,
unsigned spans) and the bare-rotation orbits. Writes codes.json."""
import itertools, json, sys
from model import Edge, ROTS, rot_order, classify_rotation

L = 4


def canon(gens, n):
    rows = {}
    for g in gens:
        v = g[0] | (g[1] << n)
        while v:
            t = v.bit_length() - 1
            if t in rows:
                v ^= rows[t]
            else:
                rows[t] = v
                break
    # full reduction
    keys = sorted(rows)
    for t in keys:
        r = rows[t]
        for u in keys:
            if u > t and (rows[u] >> t) & 1:
                rows[u] ^= r
    return tuple(sorted(rows.values()))


orders = list(itertools.permutations(range(6)))
key_of = {}
classes = {}
for o in orders:
    E = Edge(L, o)
    gens = [g for _, _, g in E.generators((0, 0, 0))]
    c = canon(gens, E.n)
    key_of[o] = c
    classes.setdefault(c, []).append(o)
keys = list(classes)
idx = {k: i for i, k in enumerate(keys)}
print("distinct stabilizer groups:", len(keys))
rank = len(keys[0])
print("rank", rank, "n", 3 * L ** 3, "log2 dim", 3 * L ** 3 - rank)

code_of = {o: idx[key_of[o]] for o in orders}
# bare rotation action on codes
act = [[code_of[rot_order(M, classes[k][0])] for M in ROTS] for k in keys]
# consistency: every ordering in a class maps to the same class
for k in keys:
    for o in classes[k]:
        for j, M in enumerate(ROTS):
            assert code_of[rot_order(M, o)] == act[idx[k]][j]
info = []
for i in range(len(keys)):
    stab = [classify_rotation(ROTS[j]) for j in range(24) if act[i][j] == i]
    orbit = sorted(set(act[i]))
    info.append(dict(code=i, rep=list(classes[keys[i]][0]), n_orderings=len(classes[keys[i]]),
                     orbit_size=len(orbit), stab=stab))
from collections import Counter
print("orbit size counts:", Counter(x["orbit_size"] for x in info))
for sz in (4, 6, 12):
    ex = next(x for x in info if x["orbit_size"] == sz)
    print(sz, Counter(ex["stab"]))
json.dump(dict(info=info, code_of={"".join(map(str, o)): code_of[o] for o in orders}),
          open("codes.json", "w"), indent=0)
