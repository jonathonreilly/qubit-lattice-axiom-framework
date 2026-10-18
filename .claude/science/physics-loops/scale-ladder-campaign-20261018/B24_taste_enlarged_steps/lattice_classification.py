#!/usr/bin/env python3
"""B24 part 1: classify the translation/taste lattices Lambda_t with 2pi Z^3 <= Lambda_t <= (pi/4) Z^3 that are
invariant under the PSG rotations, and for each one compare
   (a) the C2-pair points: k fixed mod Lambda_t (under the PSG affine action k -> R k + c_R) by two distinct
       commuting C2 rotations (the points where the projective spin-1/2 rep can force even levels), and
   (b) the T-fixed points: k fixed mod Lambda_t by all 12 elements of T (where linear cones are forced isotropic, L4).
The affine shifts c_R are read off the PSG operators of the model (B20_check chklib, op_bloch), as in B20_check/chk3.
Exact integer arithmetic: points on (pi/16) Z^3 mod 2pi (32^3 points), lattices in units of pi/16.
A finer grid check ((pi/32)Z^3) confirms that no C2-pair point lies off (pi/16)Z^3.
Also: 'level-preserving' version. A taste with omega = -1 maps level E to E + pi; for the isotropy/even-level question at a
fixed E only the omega = 1 sublattice Lambda_0 = ker omega counts.  Because omega is rotation-invariant, (R-1)Lambda_t <= Lambda_0,
so the T-fixed set at level E is the T-fixed set mod Lambda_0: the classification over invariant lattices covers both.
Prints PASS/FAIL and TOTAL."""
import os, sys, time, itertools, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from b24base import *          # noqa  (B23 b23lib copy -> B20_check chklib -> B18_check chk_model)
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)

# ---- affine action from operators (units pi/2 mod 4 on the L=4 grid), as chk3
ACT = []
for (P, s), R in zip(rots, ROTS):
    R = np.array(R, int); cs = set()
    for k in GRIDK:
        kk, U = op_bloch(P, s, k)
        n = np.round(k / (np.pi / 2)).astype(int); n2 = np.round(kk / (np.pi / 2)).astype(int)
        cs.add(tuple((n2 - R @ n) % 4))
    ACT.append((R, cs))
check("PSG rotations act affinely, k -> R k + c_R, c_R in pi Z^3", all(len(c) == 1 and all(x % 2 == 0 for x in list(c)[0]) for _, c in ACT))
N = 32                                   # 2pi = 32 units of pi/16
ACT = [(R, (np.array(list(c)[0]) // 2) * 16) for R, c in ACT]     # c_R in units pi/16
def typ(R):
    tr = int(round(np.trace(R)))
    return {3: 'E', -1: 'C2', 0: 'C3', 1: 'C4'}[tr]
isT = [typ(R) == 'E' or typ(R) == 'C3' or (typ(R) == 'C2' and np.allclose(np.abs(np.diag(R)), 1)) for R, _ in ACT]
check("T has 12 elements", sum(isT) == 12)
C2s = [i for i, (R, _) in enumerate(ACT) if typ(R) == 'C2']
C2pairs = [(i, j) for i in C2s for j in C2s if i < j and np.array_equal(ACT[i][0] @ ACT[j][0], ACT[j][0] @ ACT[i][0])]
check("9 C2 rotations and 12 commuting C2 pairs (4 D2 subgroups x 3 pairs: the normal {C2x,C2y,C2z} and three {C2z, C2(110), C2(1-10)}-type)", len(C2s) == 9 and len(C2pairs) == 12, f"{len(C2s)} {len(C2pairs)}")

# ---- invariant subgroups of (Z/8)^3 (units pi/4), i.e. lattices 2piZ^3 <= Lam <= (pi/4)Z^3 invariant under O (hence O_h)
M8 = 8
ROT_L = [R for R, _ in ACT]
def orbit(v): return {tuple(int(x) % M8 for x in R @ np.array(v)) for R in ROT_L} | {tuple((-int(x)) % M8 for x in R @ np.array(v)) for R in ROT_L}
def span(gens):
    H = {(0, 0, 0)}; frontier = [(0, 0, 0)]
    gens = list(gens)
    while frontier:
        new = []
        for h in frontier:
            for g in gens:
                x = tuple((a + b) % M8 for a, b in zip(h, g))
                if x not in H: H.add(x); new.append(x)
        frontier = new
    return frozenset(H)
allv = list(itertools.product(range(M8), repeat=3))
orbits = []; seen = set()
for v in allv:
    if v in seen: continue
    o = orbit(v); seen |= o; orbits.append(sorted(o))
subs = {span([])}; frontier = [span([])]
while frontier:
    new = []
    for H in frontier:
        for o in orbits:
            if o[0] in H: continue
            H2 = span(list(H) + o)  # H is a group; adding generators
            if H2 not in subs: subs.add(H2); new.append(H2)
    frontier = new
subs = sorted(subs, key=len)
check("invariant lattices enumerated by orbit-closure BFS; each is a subgroup closed under all 24 rotations",
      all(all(tuple(int(x) % M8 for x in R @ np.array(v)) in H for v in H for R in ROT_L) for H in subs), f"{len(subs)} lattices, {len(orbits)} orbits")

def name_lat(H):
    # generators in units of pi/4: a minimal description
    gens = []; cur = span([])
    for v in sorted(H, key=lambda v: (sum(min(x, M8 - x) for x in v), v)):
        if v not in cur: gens.append(v); cur = span(gens)
        if cur == H: break
    return ' + '.join('(pi/4)' + str(tuple(x if x <= 4 else x - 8 for x in g)) for g in gens) or '2piZ^3'
def in_lat16(H, v):   # v in units pi/16 (mod 32): in Lam iff all components divisible by 4 and v/4 mod 8 in H
    v = [int(x) % N for x in v]
    return all(x % 4 == 0 for x in v) and tuple((x // 4) % M8 for x in v) in H

pts = np.array(list(itertools.product(range(N), repeat=3)))
def fixers(H, v):
    return [i for i, (R, c) in enumerate(ACT) if in_lat16(H, R @ v + c - v)]
results = []
ks16 = tuple(np.round(kst / (np.pi / 16)).astype(int) % N)
named = {'k*': np.array(ks16), 'k*+pi e_x': (np.array(ks16) + [16, 0, 0]) % N, 'Gamma': np.zeros(3, int), 'X_pi': np.array([16, 0, 0]),
         'X_r=(pi/2)e_x': np.array([8, 0, 0]), 'M_r=(pi/2)(1,1,0)': np.array([8, 8, 0]), '(pi/4)e_x': np.array([4, 0, 0]), '(pi/4)(1,1,0)': np.array([4, 4, 0]),
         '(pi/4)(1,1,1)': np.array([4, 4, 4])}
for H in subs:
    c2pts = []; tpts = []
    for v in pts:
        f = set(fixers(H, v))
        hasT = all(i in f for i in range(24) if isT[i])
        hasPair = any(i in f and j in f for i, j in C2pairs)
        if hasPair: c2pts.append(tuple(v))
        if hasT: tpts.append(tuple(v))
    # classes mod Lambda
    def cls(v): return min(tuple((np.array(v) + 4 * np.array(h)) % N) for h in H)
    c2cls = sorted({cls(v) for v in c2pts}); tcls = sorted({cls(v) for v in tpts})
    bad = [v for v in c2cls if v not in tcls]
    results.append(dict(lat=name_lat(H), index=512 // len(H), size=len(H), contains_piZ3=all(h in H for h in [(4, 0, 0), (0, 4, 0), (0, 0, 4)]),
                        n_c2=len(c2cls), n_T=len(tcls), n_bad=len(bad), Tcls=tcls, bad_examples=bad[:6],
                        named={k_: ('T' if all(i in fixers(H, v) for i in range(24) if isT[i]) else
                                    ('C2pair' if any(i in fixers(H, v) and j in fixers(H, v) for i, j in C2pairs) else '-')) for k_, v in named.items()}))
print(f"\n  {len(subs)} invariant lattices (index = [(pi/4)Z^3 : Lam]); classes mod Lam on the (pi/16)Z^3 grid:")
for r in results:
    print(f"  |Lam/2piZ^3|={r['size']:3d}  {r['lat']:<60s}  C2-pair classes {r['n_c2']:4d}  T-fixed classes {r['n_T']:3d}  C2-pair-not-T {r['n_bad']:4d}"
          f"  e.g. {[tuple(int(x) for x in v) for v in r['bad_examples'][:3]]} (pi/16 units)")
    print(f"        named points: {r['named']}")
# genuine finer-grid test: (pi/32) units, N2 = 64
N2 = 64
def in_lat32(H, v):
    v = [int(x) % N2 for x in v]; return all(x % 8 == 0 for x in v) and tuple((x // 8) % M8 for x in v) in H
off = 0
for H in (subs[0], subs[-1], subs[len(subs) // 2]):
    for v in itertools.product(range(N2), repeat=3):
        v = np.array(v)
        if all(x % 2 == 0 for x in v): continue
        f = {i for i, (R, c) in enumerate(ACT) if in_lat32(H, R @ v + 2 * c - v)}
        if any(i in f and j in f for i, j in C2pairs): off += 1
check("no C2-pair-fixed point off (pi/16)Z^3 (tested on (pi/32)Z^3 for three lattices: 2piZ^3, (pi/4)Z^3 and a middle one)", off == 0, f"{off} off-grid")
good = [r for r in results if r['n_bad'] == 0]
check("STRUCTURAL: no invariant lattice 2piZ^3 <= Lam <= (pi/4)Z^3 makes every C2-pair-fixed point T-fixed mod Lam", len(good) == 0,
      f"{len(good)} lattices with all C2-pair points T-fixed")
mn = min(results, key=lambda r: (r['n_bad'] / max(r['n_c2'], 1)))
print(f"  smallest fraction of non-T C2-pair classes: {mn['lat']}  {mn['n_bad']}/{mn['n_c2']}")
json.dump([{k_: (v if k_ not in ('Tcls', 'bad_examples') else [list(map(int, x)) for x in v]) for k_, v in r.items()} for r in results],
          open(os.path.join(HERE, 'lattice_classification.json'), 'w'), indent=1)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
