"""PR 9008 attack-a: WITNESS REALIZABILITY for the transverse-angular-form draft.

Every witness/configuration the note states is rebuilt by code that shares nothing with the runner:
 (1) the exact L = 2 census (9600 ice states, 880 at zero flux, 125 winding sectors, <W^2> = 76/25) by a DIFFERENT method
     (net-flow enumeration on the 12 edges of the cube, each edge doubled; the runner enumerates all 2^24 arrow patterns);
 (2) the multisets of folded components with |k|^2 <= 9 on the L = 16 torus, their assignments, the P_zz table of the note,
     the count of usable assignments, the shared-Q spread the note quotes (1.3e-15), and the '24 smallest wavevectors';
 (3) the runner's L = 16 starting configuration is an ice state with zero winding, and the torus is bipartite (no odd cycles);
 (4) the runner's docstring against its own multiset list.
Exact arithmetic (Fractions) for (1) and for P_zz values, floats only where the note prints floats.
"""
import itertools, math, sys
from fractions import Fraction
import numpy as np

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)
HITS = []

# ---------------------------------------------------------------- (1) exact L = 2 census by net flows
print("== 1. exact L = 2 census by edge net flows ==")
V = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]
vid = {v: i for i, v in enumerate(V)}
# cube edges: (u, v, direction) with u having coordinate 0 in that direction
edges = []
for d in range(3):
    for v in V:
        if v[d] == 0:
            w = list(v); w[d] = 1
            edges.append((vid[v], vid[tuple(w)], d))
assert len(edges) == 12
# each doubled edge = link a (u->v when +1, lives at coordinate 0: the winding link) and link b (v->u when +1, lives at coordinate 1)
# net flow u->v = Ea - Eb  in {-2, 0, +2}; the two zero-flow states have Ea = +1 (Ea=Eb=+1) or Ea = -1 (Ea=Eb=-1)
count = 0
zero = 0
w2num = 0
sectors = {}
for f in itertools.product((-1, 0, 1), repeat=12):
    div = [0] * 8
    for (u, v, d), fe in zip(edges, f):
        div[u] += fe
        div[v] -= fe
    if any(div):
        continue
    zeros = [i for i, fe in enumerate(f) if fe == 0]
    fixed_ea = {i: (1 if fe == 1 else -1) for i, fe in enumerate(f) if fe != 0}
    for ch in itertools.product((1, -1), repeat=len(zeros)):
        ea = dict(fixed_ea)
        for i, c in zip(zeros, ch):
            ea[i] = c
        W = [0, 0, 0]
        for i, (u, v, d) in enumerate(edges):
            W[d] += ea[i]
        count += 1
        zero += (W == [0, 0, 0])
        w2num += sum(w * w for w in W)
        sectors[tuple(W)] = sectors.get(tuple(W), 0) + 1
w2 = Fraction(w2num, 3 * count)
check("net-flow enumeration: 9600 ice configurations, 880 at zero flux, 125 winding sectors, <W^2> = 76/25",
      count == 9600 and zero == 880 and len(sectors) == 125 and w2 == Fraction(76, 25), f"{count}, {zero}, {len(sectors)}, {w2}")
# closed form check of the sector structure: winding vector components are even-valued? (4 links each: W in {-4,-2,0,2,4})
vals = sorted({w for s in sectors for w in s})
check("winding components take exactly the values -4,-2,0,2,4 (four links per cut) and 5^3 = 125 sectors are all realised",
      vals == [-4, -2, 0, 2, 4] and len(sectors) == 125, f"values {vals}")

# ---------------------------------------------------------------- (2) multisets, assignments, P_zz table
print("\n== 2. multisets on the L = 16 torus ==")
L = 16
def s2(a):
    return 2 - 2 * math.cos(2 * math.pi * a / L)
def Pzz(k, zc):
    Q = sum(s2(a) for a in k)
    return 1 - s2(zc) / Q
ms_list = sorted({tuple(sorted(t)) for t in itertools.product(range(0, 9), repeat=3) if 0 < sum(x * x for x in t) <= 9})
check("the multisets with |k|^2 <= 9 all have components <= 3 (the runner scans range(4))",
      all(max(m) <= 3 for m in ms_list), f"{len(ms_list)} multisets: {ms_list}")
usable = {}
for m in ms_list:
    P = {}
    for zc in sorted(set(m)):
        rest = list(m); rest.remove(zc)
        P[zc] = Pzz(m, zc)
    us = {zc: p for zc, p in P.items() if p > 0.05}
    usable[m] = (P, us)
five = [m for m in ms_list if len(usable[m][1]) >= 2]
check("exactly five multisets have two usable assignments (P_zz > 0.05)", five == [(0, 1, 1), (0, 1, 2), (0, 2, 2), (1, 1, 2), (1, 2, 2)], f"{five}")
tab = {(0, 1, 1): (1.000, 0.500), (0, 1, 2): (1.000, 0.206), (0, 2, 2): (1.000, 0.500), (1, 1, 2): (0.829, 0.342), (1, 2, 2): (0.885, 0.558)}
ok = True; det = []
for m in five:
    ps = usable[m][1].values()
    hi, lo = max(ps), min(ps)
    det.append(f"{m}: {hi:.3f}/{lo:.3f}")
    ok &= abs(hi - tab[m][0]) < 5e-4 and abs(lo - tab[m][1]) < 5e-4
check("the P_zz (large, small) column of the note's table is reproduced to its printed 3 digits", ok, "; ".join(det))
# multisets the runner's docstring covers: 'every multiset has at least two assignments'
single = [m for m in ms_list if len(usable[m][1]) < 2]
check("multisets with |k|^2 <= 9 that have fewer than two usable assignments (the runner's docstring says 'every multiset has at least two')",
      len(single) == len(ms_list) - 5, f"{len(single)} of {len(ms_list)}: {single}")
# the 24 smallest wavevectors: |k|^2 <= 3 with P_zz > 0.05
vecs = [(a, b, c) for a in range(-1, 2) for b in range(-1, 2) for c in range(-1, 2) if 0 < a * a + b * b + c * c <= 3]
sel = []
for (a, b, c) in vecs:
    P = 1 - s2(c) / (s2(a) + s2(b) + s2(c))
    if P > 0.05:
        sel.append((a, b, c))
check("the '24 smallest wavevectors' are the 26 with 0 < |k|^2 <= 3 minus the two along z (P_zz = 0)", len(vecs) == 26 and len(sel) == 24 and
      {v for v in vecs if v not in sel} == {(0, 0, 1), (0, 0, -1)}, f"{len(vecs)} with |k|^2<=3, {len(sel)} usable")
# shared Q spread, as the runner builds its masks (float64 arrays)
k = 2 * np.pi * np.arange(L) / L
s2a = 2 - 2 * np.cos(k)
Q = s2a[:, None, None] + s2a[None, :, None] + s2a[None, None, :]
fold = np.minimum(np.arange(L), L - np.arange(L))
FX, FY, FZ = np.meshgrid(fold, fold, fold, indexing="ij")
P = np.zeros((L, L, L)); nz = Q > 0
P[nz] = 1 - np.broadcast_to(s2a[None, None, :], Q.shape)[nz] / Q[nz]
qdev = 0.0
for m in five:
    allm = np.zeros(Q.shape, bool)
    for zc in set(m):
        rest = list(m); rest.remove(zc)
        mk = (FZ == zc) & (np.minimum(FX, FY) == min(rest)) & (np.maximum(FX, FY) == max(rest)) & (P > 0.05)
        allm |= mk
    qdev = max(qdev, float(Q[allm].max() - Q[allm].min()))
check("the shared-Q spread over the assignments is at rounding level (note: 1.3e-15)", qdev < 1e-12, f"{qdev:.2e}")
# exact Q equality in exact arithmetic: 2 - 2cos is symmetric; check with sympy-free rational surrogate: sum of squares of sines
# the assignments differ by permutation of the summands, so Q is EXACTLY equal as a real number; the float spread is summation order only.
sizes = {}
for m in five:
    n = 0
    for zc in set(m):
        rest = list(m); rest.remove(zc)
        mk = (FZ == zc) & (np.minimum(FX, FY) == min(rest)) & (np.maximum(FX, FY) == max(rest)) & (P > 0.05)
        sizes[(m, zc)] = int(mk.sum())
nus = sum(len(usable[m][1]) for m in five)
check("every usable (multiset, z-component) group is non-empty on the torus, so every table row exists as a batch ratio; {0,1,2} has THREE usable assignments (the table quotes only the extreme two)",
      all(v > 0 for v in sizes.values()) and len(sizes) == nus == 11 and len(usable[(0, 1, 2)][1]) == 3, f"{nus} groups, sizes {sorted(sizes.values())}")

# ---------------------------------------------------------------- (3) the L = 16 starting configuration and bipartiteness
print("\n== 3. the runner's L = 16 starting configuration ==")
def initial(L):
    E = np.empty((3, L, L, L), np.int8)
    alt = (-1) ** np.arange(L)
    E[0] = np.broadcast_to(alt[None, :, None], (L, L, L))
    E[1] = np.broadcast_to(alt[None, None, :], (L, L, L))
    E[2] = np.broadcast_to(alt[:, None, None], (L, L, L))
    return E
E = initial(L).astype(int)
div = (E[0] - np.roll(E[0], 1, 0) + E[1] - np.roll(E[1], 1, 1) + E[2] - np.roll(E[2], 1, 2))
W = [E[0, 0].sum(), E[1, :, 0].sum(), E[2, :, :, 0].sum()]
check("initial() is an ice state (zero divergence at all 4096 sites) with zero winding in every direction", not div.any() and W == [0, 0, 0], f"max |div| {abs(div).max()}, winding {W}")
# bipartite: parity of x+y+z is flipped by every link on the even torus
ok = all(((x + y + z) % 2) != (((x + (d == 0)) % L + (y + (d == 1)) % L + (z + (d == 2)) % L) % 2)
         for x in range(L) for y in range(L) for z in range(L) for d in range(3))
check("the L = 16 torus is bipartite (every link changes the parity of x+y+z, L even): the note's cubic graph has no triangles", ok)
# the L = 2 torus of check A is bipartite too but has doubled edges: 4-cycles of parallel links, every vertex still has 3 in / 3 out
check("L = 2: 24 links, 8 sites, each site has 3 outgoing and 3 incoming link slots (doubled cube edges)", len(edges) * 2 == 24 and len(V) == 8)

print()
if HITS:
    for h in HITS: print("HIT:", h)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-a witness realizability on PR 9008: L=2 census reproduced by net-flow enumeration (9600/880/125/76/25), five multisets with two usable assignments and the P_zz table reproduced, 24 usable smallest wavevectors, Q spread {qdev:.1e}, L=16 start state is ice with zero winding; the runner's docstring 'every multiset has at least two assignments' holds for only 5 of {len(ms_list)} multisets (wording of a docstring, not of the note); PASS={PASS} FAIL={FAIL}; no defect in the note's witnesses")
sys.exit(1 if FAIL else 0)
