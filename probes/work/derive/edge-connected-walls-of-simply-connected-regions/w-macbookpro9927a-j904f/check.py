"""check.py -- edge-connected-walls-of-simply-connected-regions a1 (worker w-macbookpro9927a-j904f).

(a) The wall of every finite face-connected V in Z^3 with face-connected complement is connected through shared
    edges.  Exact combinatorial checks: exhaustive to 8 cells, random large regions (cavities filled), the lemma's
    ray-parity construction, and the sharpness examples.
(b) Block 117's certificate redone with the 12-neighbour tree count, in exact rationals.
Run from the repository root.
"""
import hashlib, itertools, math, os, random, subprocess, sys
from collections import Counter
from fractions import Fraction as Fr
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, cwd=HERE).stdout.strip()
FAILS = []; NOK = 0
def ok(name, cond, detail=""):
    global NOK
    if cond: NOK += 1
    else: FAILS.append(name); print("FAIL", name, detail)

# ------------------------------------------------------------------ Q: block 117 on its hand-off branch (PR #9160)
HEAD117 = "24cc9059fba92e8bfbeec3f61f8d056241784ec4"
N117 = ("docs/ADMISSIBILITY_RULE_THE_RECORD_GAS_DOES_MAKE_THE_CHESSBOARD_WHEN_A_RECORDED_BOND_COSTS_A_FACTOR_BELOW_NINE_OVER_62500_"
        "AND_THE_TWO_FRAMED_STATES_DIFFER_AT_EVERY_SITE_BOUNDED_THEOREM_NOTE_2026-09-24.md")
def gshow(rev, path):
    r = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, cwd=ROOT)
    if r.returncode:
        subprocess.run(["git", "fetch", "origin", "physics-loop/admissibility-induced-law-block117-the-record-gas-does-make-the-chessboard-when-bonds-are-expensive-20260924", "--quiet"], cwd=ROOT)
        r = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, cwd=ROOT)
    return r.stdout
b117 = gshow(HEAD117, N117); t117 = b117.decode()
ok("Q1 block 117 note pinned", hashlib.sha256(b117).hexdigest() == "cc2727f554303be434b0ec91409b4ba4573ca508c717c0cddb25ffa4b6659a2f")
ok("Q2 block 117 imports vertex connectedness and leaves edges open",
   "The wall is connected through shared vertices (imported below). A plaquette meets 32 others at a vertex." in t117
   and "1. *Edge-connected walls.* If every wall is connected through shared edges (true for every wall of at most six cells), the same certificate gives about `g ≤ 1.2·10⁻³` (a2). Not proved." in t117
   and "At `x₀ = 3/250`, which is below `30³⁰/31³¹`, `Σ_{V∋x} x₀^{|∂V|} ≤ 0.0897`." in t117
   and "At `ζ = g⁻³` (`H = 1`), `x ≤ 3/250` means `g³Λ⁶(Λ/m)⁵ ≤ (3/250)⁶`." in t117)

# ------------------------------------------------------------------ geometry in doubled coordinates
# cube c -> centre 2c (all even); plaquette between c and c+e_a -> 2c+e_a (one odd coordinate);
# edge centres have two odd coordinates, vertices three.
E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
NB = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
def add(a, b): return (a[0] + b[0], a[1] + b[1], a[2] + b[2])
def wall(V):
    Vs = set(V); W = []
    for c in Vs:
        for d in NB:
            if add(c, d) not in Vs:
                W.append((2 * c[0] + d[0], 2 * c[1] + d[1], 2 * c[2] + d[2]))
    return W
def pl_edges(P):
    a = [i for i in range(3) if P[i] % 2][0]; out = []
    for b in range(3):
        if b != a:
            for s in (1, -1):
                q = list(P); q[b] += s; out.append(tuple(q))
    return out
def pl_verts(P):
    a = [i for i in range(3) if P[i] % 2][0]; b, d = [i for i in range(3) if i != a]; out = []
    for s in (1, -1):
        for t in (1, -1):
            q = list(P); q[b] += s; q[d] += t; out.append(tuple(q))
    return out
def ncomp(W, keyf):
    par = {P: P for P in W}
    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    at = {}
    for P in W:
        for k in keyf(P):
            if k in at:
                ra, rb = find(P), find(at[k])
                if ra != rb: par[ra] = rb
            else: at[k] = P
    return len({find(P) for P in W})
def face_connected(S):
    S = set(S)
    if not S: return True
    st = [next(iter(S))]; seen = {st[0]}
    while st:
        c = st.pop()
        for d in NB:
            n = add(c, d)
            if n in S and n not in seen: seen.add(n); st.append(n)
    return len(seen) == len(S)
def complement_face_connected(V):
    Vs = set(V); lo = [min(c[i] for c in Vs) - 1 for i in range(3)]; hi = [max(c[i] for c in Vs) + 1 for i in range(3)]
    box = [(x, y, z) for x in range(lo[0], hi[0] + 1) for y in range(lo[1], hi[1] + 1) for z in range(lo[2], hi[2] + 1)]
    C = [c for c in box if c not in Vs]
    return face_connected(C)       # the box shell is in the complement and connects every outside region
def fill_cavities(V):
    Vs = set(V); lo = [min(c[i] for c in Vs) - 1 for i in range(3)]; hi = [max(c[i] for c in Vs) + 1 for i in range(3)]
    inb = lambda c: all(lo[i] <= c[i] <= hi[i] for i in range(3))
    start = tuple(lo); seen = {start}; st = [start]
    while st:
        c = st.pop()
        for d in NB:
            n = add(c, d)
            if inb(n) and n not in Vs and n not in seen: seen.add(n); st.append(n)
    return {(x, y, z) for x in range(lo[0], hi[0] + 1) for y in range(lo[1], hi[1] + 1) for z in range(lo[2], hi[2] + 1) if (x, y, z) not in seen}

# ------------------------------------------------------------------ A: the theorem
P0 = (1, 0, 0)
cand = [(x, y, z) for x in range(-3, 4) for y in range(-3, 4) for z in range(-3, 4) if (x % 2) + (y % 2) + (z % 2) == 1]
de = sum(1 for P in cand if P != P0 and set(pl_edges(P)) & set(pl_edges(P0)))
dv = sum(1 for P in cand if P != P0 and set(pl_verts(P)) & set(pl_verts(P0)))
ok("A1 a plaquette shares an edge with 12 others and a vertex with 32", (de, dv) == (12, 32), f"{de} {dv}")
# exhaustive: Redelmeier enumeration of fixed polycubes (origin = least cell in (z, y, x) order)
def key(c): return (c[2], c[1], c[0])
NMAX = 8
counts_fixed = Counter(); ck = Counter(); bad_edge = 0; bad_comp = 0; minwall = {}
def visit(V):
    n = len(V); W = wall(V); k = len(W)
    counts_fixed[n] += 1; minwall[n] = min(minwall.get(n, 99), k)
    global bad_edge, bad_comp
    if not complement_face_connected(V): bad_comp += 1; return
    if ncomp(W, pl_edges) != 1: bad_edge += 1
    if n <= 7 and k <= 22: ck[k] += n            # regions around a site: n placements contain the origin
def redel(V, untried, seen):
    visit(V)
    if len(V) == NMAX: return
    untried = list(untried)
    while untried:
        c = untried.pop()
        newc = []
        for d in NB:
            n = add(c, d)
            if n not in seen and key(n) > key((0, 0, 0)):
                newc.append(n)
        V.append(c)
        redel(V, untried + newc, seen | set(newc))
        V.pop()
start_nb = [d for d in NB if key(d) > key((0, 0, 0))]
redel([(0, 0, 0)], start_nb, set(start_nb) | {(0, 0, 0)})
fixed = [counts_fixed[n] for n in range(1, NMAX + 1)]
ok("A2 fixed polycubes 1..8 cells: 1, 3, 15, 86, 534, 3481, 23502, 162913", fixed == [1, 3, 15, 86, 534, 3481, 23502, 162913], str(fixed))
ok("A3 exhaustive: every polycube of at most 8 cells has a face-connected complement and an edge-connected wall", bad_comp == 0 and bad_edge == 0, f"{bad_comp} {bad_edge}")
rnd = random.Random(117)
big_ok = True; nbig = 0; pinch_seen = 0; sizes = []
for trial in range(400):
    # random site-percolation-like growth from the origin, then fill cavities
    p = rnd.choice([0.3, 0.45, 0.6]); target = rnd.randint(20, 260)
    V = {(0, 0, 0)}; front = [(0, 0, 0)]; rejected = set()
    while front and len(V) < target:
        c = front.pop(rnd.randrange(len(front)))
        for d in NB:
            n = add(c, d)
            if n not in V and n not in rejected:
                if rnd.random() < p: V.add(n); front.append(n)
                else: rejected.add(n)
    V = fill_cavities(V); W = wall(V)
    assert face_connected(V) and complement_face_connected(V)
    big_ok &= ncomp(W, pl_edges) == 1; nbig += 1; sizes.append(len(V))
    # count vertices where the wall is pinched (its plaquettes there split into >= 2 edge-classes locally)
    at = {}
    for P in W:
        for v in pl_verts(P): at.setdefault(v, []).append(P)
    for v, Ps in at.items():
        loc = [P for P in Ps]
        if ncomp(loc, lambda P, v=v: [e for e in pl_edges(P) if sum(abs(e[i] - v[i]) for i in range(3)) == 1]) > 1: pinch_seen += 1
ok("A4 400 random regions (20-260 cells, cavities filled): every wall edge-connected", big_ok and nbig == 400, f"{nbig}")
ok("A5 the random walls include locally pinched vertices (two edge-classes at a vertex), so the test is not vacuous", pinch_seen > 0, str(pinch_seen))
# the lemma's construction: U = cubes whose +e1 ray crosses Sigma an odd number of times; for Sigma = boundary of a random finite W, U = W
lem_ok = True
for trial in range(60):
    Wset = {(rnd.randint(-3, 3), rnd.randint(-3, 3), rnd.randint(-3, 3)) for _ in range(rnd.randint(1, 60))}
    Sig = set(wall(Wset))
    U = set()
    for x in range(-6, 7):
        for y in range(-5, 6):
            for z in range(-5, 6):
                cnt = sum(1 for j in range(0, 12) if (2 * (x + j) + 1, 2 * y, 2 * z) in Sig)
                if cnt % 2: U.add((x, y, z))
    lem_ok &= U == Wset
ok("A6 ray-parity construction recovers W from its wall for 60 random (disconnected) cube sets", lem_ok)
# the cycle condition used in the proof: every edge of a wall lies on 0, 2 or 4 wall plaquettes
even_ok = True
for trial in range(40):
    Wset = {(rnd.randint(-2, 2), rnd.randint(-2, 2), rnd.randint(-2, 2)) for _ in range(rnd.randint(1, 40))}
    at = Counter(e for P in wall(Wset) for e in pl_edges(P))
    even_ok &= all(v % 2 == 0 for v in at.values())
ok("A7 every edge lies on an even number of wall plaquettes (mod-2 cycle)", even_ok)
# sharpness: complement not face-connected (3x3x3 shell) -> two classes even through vertices; V touching at a vertex only
shell = {(x, y, z) for x in range(3) for y in range(3) for z in range(3)} - {(1, 1, 1)}
Wsh = wall(shell); two = [(0, 0, 0), (1, 1, 1)]; Wtwo = wall(two); edgepair = [(0, 0, 0), (1, 1, 0)]
ok("A8 sharpness: a cavity gives 2 wall classes (edges and vertices); two cubes meeting at a vertex give 2 edge-classes, 1 vertex-class; "
   "two cubes meeting along an edge stay edge-connected",
   (not complement_face_connected(shell)) and ncomp(Wsh, pl_edges) == 2 and ncomp(Wsh, pl_verts) == 2
   and ncomp(Wtwo, pl_edges) == 2 and ncomp(Wtwo, pl_verts) == 1 and ncomp(wall(edgepair), pl_edges) == 1)

# ------------------------------------------------------------------ B: block 117's certificate with 12 neighbours
ok("B1 regions around a site with |dV| <= 22 (block 117 T4(a)); seven or more cells need |dV| >= 24",
   dict(ck) == {6: 1, 10: 6, 14: 45, 16: 12, 18: 332, 20: 240, 22: 2538} and minwall[7] == 24 and minwall[8] == 24, str(dict(ck)))
def rk(D, k): return Fr(1) if k == 1 else Fr(D * comb((D - 1) * k, k - 2), k - 1)
# tree series: R = x(1+U)^D, U = x(1+U)^(D-1); check r_k = [x^k] R for k <= 30 (D = 12)
def tree_series(D, K):
    U = [Fr(0)] * (K + 1)
    for it in range(K):
        # U = x (1+U)^(D-1)
        P = [Fr(0)] * (K + 1); P[0] = Fr(1)
        base = U[:]; base[0] += 1
        for _ in range(D - 1):
            Q = [Fr(0)] * (K + 1)
            for i in range(K + 1):
                if P[i]:
                    for j in range(K + 1 - i): Q[i + j] += P[i] * base[j]
            P = Q
        U = [Fr(0)] + P[:K]
    P = [Fr(0)] * (K + 1); P[0] = Fr(1); base = U[:]; base[0] += 1
    for _ in range(D):
        Q = [Fr(0)] * (K + 1)
        for i in range(K + 1):
            if P[i]:
                for j in range(K + 1 - i): Q[i + j] += P[i] * base[j]
        P = Q
    return [Fr(0)] + P[:K]
TS = tree_series(12, 30)
ok("B2 r_k = (12/(k-1)) C(11k, k-2) equals the rooted-tree series coefficient for k <= 30", all(TS[k] == rk(12, k) for k in range(1, 31)))
def gf_bound(D, x0, Up, ck):
    assert x0 * (1 + Up) ** (D - 1) <= Up
    den = 1 - x0 * (D - 1) * (1 + Up) ** (D - 2); assert den > 0
    Rp = (1 + Up) ** D + x0 * D * (1 + Up) ** (D - 1) * ((1 + Up) ** (D - 1) / den)
    tail = x0 / 4 * Rp - sum(Fr(k, 4) * rk(D, k) * x0 ** k for k in range(1, 24))
    return sum(c * x0 ** k for k, c in ck.items()) + tail
xc = Fr(10 ** 10, 11 ** 11); x0, Up = Fr(347, 10000), Fr(88, 1000)
S12 = gf_bound(12, x0, Up, dict(ck))
S32 = gf_bound(32, Fr(3, 250), Fr(31, 1000), dict(ck))
ok("B3 at x0 = 347/10000 < 10^10/11^11: sum over regions around a site of x0^|dV| <= 0.1430 (exact rational); block 117's 32-neighbour sum reproduced (< 0.0897)",
   x0 < xc and S12 < Fr(1430, 10000) and S32 < Fr(897, 10000), f"{float(S12)} {float(S32)}")
TR = {"(3,1,2)": (3, 1, 2), "(5,2,4)": (5, 2, 4), "(12,1,2)": (12, 1, 2), "(9,8,8)": (9, 8, 8)}
GNEW = {"(3,1,2)": Fr(8575, 10 ** 8), "(5,2,4)": Fr(1536, 10 ** 7), "(12,1,2)": Fr(1628, 10 ** 9), "(9,8,8)": Fr(8147, 10 ** 7)}
gs_ok = True; lines = []
def cond(g, Lam, m, xx): return g ** 3 * Lam ** 6 * (Lam / m) ** 5 <= xx ** 6
for nm, (p, q, r) in TR.items():
    Mv = [Fr(6 * p, p + q + 4 * r), Fr(6 * q, p + q + 4 * r), Fr(6 * r, p + q + 4 * r)]; Lam, m = max(Mv), min(Mv)
    g = GNEW[nm]; step = g / 1000
    gs_ok &= cond(g, Lam, m, x0) and not cond(g + step, Lam, m, x0)     # g is g* to four figures
    lines.append(f"{nm} {float(g):.4g}")
g0 = x0 ** 2
ok("B4 new g*: without contents (347/10000)^2 = 120409/10^8; per triple to four figures (g holds, 1.001 g fails)", g0 == Fr(120409, 10 ** 8) and gs_ok)
ok("B5 ceiling of this certificate form: x0 < 10^10/11^11, so g* < (10^10/11^11)^2 without contents", float(xc) ** 2 < 1.2286e-3 and g0 < xc ** 2)
print(f"B sum(12 nbrs, x0=347/10000) = {float(S12):.5f} -> <sigma> >= {1 - 2 * float(S12):.3f}; g* = {float(g0):.6g} without contents; "
      + ", ".join(lines) + f"; ceiling (10^10/11^11)^2 = {float(xc) ** 2:.5g}")
print(f"A exhaustive walls to 8 cells: {sum(fixed)} fixed polycubes; random regions {min(sizes)}-{max(sizes)} cells; pinched vertices seen {pinch_seen}")

print(f"checks passed {NOK}, failed {len(FAILS)}")
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS)); sys.exit(1)
print("SUMMARY: PROVED (a) the wall of every finite face-connected V in Z^3 with face-connected complement is connected through shared "
      "edges: two edge-disjoint classes of wall plaquettes would each be mod-2 cycles bounding finite cube sets U_A, U_B with "
      "V = U_A xor U_B, and no face could separate cubes differing in both memberships, which the two face-connectednesses forbid; "
      "exhaustive to 8 cells, 400 random regions; (b) block 117's certificate with 12-neighbour trees: x0 = 347/10000, sum <= 0.143, "
      "g* = 1.204e-3 without contents and 8.575e-5 at (3,1,2)")
print("HIT: walls are edge-connected: for every finite face-connected V in Z^3 whose complement is face-connected, the plaquettes "
      "between V and its complement are connected through shared edges (12 neighbours), so block 117's import can be replaced and "
      "its certificate redone: at x0 = 347/10000 the sum over regions around a site is <= 0.143, giving the two framed states "
      "<sigma> >= 0.71 for g <= 1.204e-3 without contents (was 9/62500) and g <= 8.575e-5 at (3,1,2) (was 1e-5)")
