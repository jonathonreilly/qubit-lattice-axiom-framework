#!/usr/bin/env python3
"""R7-2: admissible-configuration counts for local cubic-covariant support rules on Z^3
with binary (one-bit) site possibilities.

Rule C (cube rule): for every elementary cube, the XOR of its 8 corner bits is 0.
  Range: the 8 corners of a unit cube (distances 1, sqrt2, sqrt3) -- NOT nearest-neighbour.
  Invariant under Z^3 translations and the full cubic group O_h.
Count log2 N_adm(region) = |sites| - rank(constraints on cubes inside region), exact GF(2) rank.

Also: binary nearest-neighbour symmetric pair rules (all 8 of them) are O(1) or volume-law (argument
in the report); here we just tabulate the hard-core rule's count growth for contrast (transfer-free brute
force on tiny boxes)."""
import itertools, math
import numpy as np

def gf2_rank(rows):
    """rows: list of python ints (bitmasks). Returns rank over GF(2)."""
    pivots = {}
    r = 0
    for v in rows:
        while v:
            h = v.bit_length() - 1
            if h in pivots:
                v ^= pivots[h]
            else:
                pivots[h] = v
                r += 1
                break
    return r

def count_region(sites):
    idx = {s: i for i, s in enumerate(sites)}
    S = set(sites)
    rows = []
    for (x, y, z) in sites:
        corners = [(x + a, y + b, z + c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
        if all(cc in S for cc in corners):
            m = 0
            for cc in corners:
                m |= 1 << idx[cc]
            rows.append(m)
    rk = gf2_rank(rows)
    return len(sites), len(rows), rk, len(sites) - rk

def count_torus(L):
    sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
    idx = {s: i for i, s in enumerate(sites)}
    rows = []
    for (x, y, z) in sites:
        m = 0
        for a in (0, 1):
            for b in (0, 1):
                for c in (0, 1):
                    m |= 1 << idx[((x + a) % L, (y + b) % L, (z + c) % L)]
        rows.append(m)
    rk = gf2_rank(rows)
    return len(sites) - rk

print("Rule C on an open L x L x L box: log2 N_adm vs L^3 - (L-1)^3 = 3L^2 - 3L + 1")
for L in range(2, 10):
    sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
    n, ncon, rk, k = count_region(sites)
    print(f"  L={L}: sites={n}, cubes={ncon}, rank={rk}, log2 N_adm={k}, 3L^2-3L+1={3*L*L-3*L+1}, ratio to surface 6L^2: {k/(6*L*L):.4f}")

print("\nRule C on the L^3 torus: log2 N_adm (expect 3L^2 - 3L + 1 over GF(2) for the kernel of D_x D_y D_z)")
for L in range(2, 9):
    print(f"  L={L}: log2 N_adm={count_torus(L)}, 3L^2-3L+1={3*L*L-3*L+1}")

print("\nRule C on lattice balls |x| <= R (sites of Z^3): log2 N_adm vs surface 4 pi R^2")
for R in [2, 3, 4, 5, 6, 7, 8]:
    rng = range(-R - 1, R + 2)
    sites = [(x, y, z) for x in rng for y in rng for z in rng if x * x + y * y + z * z <= R * R]
    n, ncon, rk, k = count_region(sites)
    print(f"  R={R}: sites={n}, cubes inside={ncon}, log2 N_adm={k}, k/(4 pi R^2)={k/(4*math.pi*R*R):.4f}, k/sites={k/n:.4f}")

print("\nExplicit admissible family for rule C: s(x,y,z) = f(y,z) xor g(x,z) xor h(x,y).")
L = 5
rng = np.random.default_rng(1)
f = rng.integers(0, 2, (L, L)); g = rng.integers(0, 2, (L, L)); h = rng.integers(0, 2, (L, L))
s = np.zeros((L, L, L), int)
for x in range(L):
    for y in range(L):
        for z in range(L):
            s[x, y, z] = f[y, z] ^ g[x, z] ^ h[x, y]
bad = 0
for x in range(L - 1):
    for y in range(L - 1):
        for z in range(L - 1):
            bad += int(s[x:x+2, y:y+2, z:z+2].sum() % 2)
print(f"  random f,g,h on L={L}: violated cubes = {bad}")

print("\nCubic covariance of rule C: the set of 8 corners of a unit cube is mapped to the corners of a unit cube")
print("by every element of O_h and every translation (checked over all 48 signed permutations):")
corners = {(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)}
ok = True
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        img = {tuple(signs[i] * v[perm[i]] for i in range(3)) for v in corners}
        mn = tuple(min(p[i] for p in img) for i in range(3))
        img = {tuple(p[i] - mn[i] for i in range(3)) for p in img}
        ok &= (img == corners)
print(f"  all 48 map the unit cube to a unit cube: {ok}")

print("\nContrast: binary NN hard-core rule (no two adjacent 1s) on L^3 open boxes (brute force, small L)")
def hardcore_count(L):
    sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
    idx = {s: i for i, s in enumerate(sites)}
    nb = []
    for (x, y, z) in sites:
        for d in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            t = (x + d[0], y + d[1], z + d[2])
            if t in idx:
                nb.append((idx[(x, y, z)], idx[t]))
    n = len(sites); cnt = 0
    for m in range(1 << n):
        if all(not ((m >> i) & 1 and (m >> j) & 1) for i, j in nb):
            cnt += 1
    return n, cnt
for L in [2]:
    n, cnt = hardcore_count(L)
    print(f"  L={L}: sites={n}, N_adm={cnt}, log2={math.log2(cnt):.3f}, per site={math.log2(cnt)/n:.3f}")
print("  lower bound for any L: every subset of one sublattice is admissible -> log2 N_adm >= floor(L^3/2) (volume law)")
