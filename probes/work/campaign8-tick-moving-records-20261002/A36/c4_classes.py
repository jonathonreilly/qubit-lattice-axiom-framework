"""
A36 check C4: what a record-timed rule can use. Count the classes of recorded-neighbour patterns that a
rule covariant under the 24 proper cubic turns can distinguish (Burnside, by explicit orbit enumeration).
- 2 colours: neighbour recorded or not (contents ignored).
- 3 colours: empty / content r / content -r (the quiet class, contents on one axis); with the swap
  r <-> -r (turning the possibilities alone, unglued) and without it (glued to a fixed axis).
- with and without mirror reflections (the Lattice axiom names proper rotations only).
"""
import signal, itertools
import numpy as np
signal.alarm(55)

dirs = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def perm_of(M):
    return tuple(dirs.index(tuple(int(v) for v in M @ np.array(d))) for d in dirs)
mats = []
for p in itertools.permutations(range(3)):
    for s in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3):
            M[i, p[i]] = s[i]
        mats.append(M)
proper = [perm_of(M) for M in mats if round(np.linalg.det(M)) == 1]
full = [perm_of(M) for M in mats]
assert len(proper) == 24 and len(full) == 48

def orbits(ncol, group, swap=False):
    seen, n = set(), 0
    reps = []
    for col in itertools.product(range(ncol), repeat=6):
        if col in seen:
            continue
        n += 1
        reps.append(col)
        orb = set()
        for g in group:
            c2 = tuple(col[g.index(i)] for i in range(6))
            orb.add(c2)
            if swap:
                orb.add(tuple({0: 0, 1: 2, 2: 1}[v] for v in c2))
        seen |= orb
    return n, reps

n2p, reps2 = orbits(2, proper)
n2f, _ = orbits(2, full)
print("C4. Recorded-neighbour pattern classes on Z^3 (6 neighbours):")
print(f"  recorded / not, 24 proper turns: {n2p} classes (with mirrors: {n2f}); with at least one recorded")
print(f"  neighbour (gate open): {n2p - 1}.  By count k:", [sum(1 for r in reps2 if sum(r) == k) for k in range(7)])
n3p, _ = orbits(3, proper)
n3f, _ = orbits(3, full)
n3ps, _ = orbits(3, proper, swap=True)
n3fs, _ = orbits(3, full, swap=True)
print(f"  empty / r / -r, 24 proper turns: {n3p} classes (with mirrors {n3f});"
      f" with the swap r<->-r: {n3ps} (with mirrors {n3fs})")
print(f"  -> mirror-image pairs among the r/-r patterns (proper - full): {n3p - n3f} without swap, {n3ps - n3fs} with swap")

# 2D for comparison (4 neighbours, 4 proper turns)
d2 = [(1,0),(0,1),(-1,0),(0,-1)]
rot = [tuple((i + s) % 4 for i in range(4)) for s in range(4)]
seen, n = set(), 0
for col in itertools.product(range(2), repeat=4):
    if col in seen:
        continue
    n += 1
    seen |= {tuple(col[g.index(i)] for i in range(4)) for g in rot}
print(f"  2D (4 neighbours, 4 turns): {n} classes, {n-1} with a recorded neighbour")

# identify the mirror-image (chiral) class among empty / r / -r patterns under the 24 proper turns
names = ['+x', '-x', '+y', '-y', '+z', '-z']
sym = {0: '.', 1: 'r', 2: '-r'}
def orbit(col, group):
    return {tuple(col[g.index(i)] for i in range(6)) for g in group}
inv = perm_of(-np.eye(3, dtype=int))        # central inversion (improper)
found = set()
for col in itertools.product(range(3), repeat=6):
    o = orbit(col, proper)
    if min(o) in found:
        continue
    mirror = tuple(col[inv.index(i)] for i in range(6))
    if mirror not in o:
        found.add(min(o))
        print("  chiral pattern (and its mirror image is a different class):",
              {names[i]: sym[c] for i, c in enumerate(min(o))})
