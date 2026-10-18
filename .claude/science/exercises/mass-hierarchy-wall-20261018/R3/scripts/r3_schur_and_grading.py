#!/usr/bin/env python3
"""R3 test 3.
Part A (Schur ceiling): for each placement of a generation triplet, the space of lattice-symmetric
Hermitian matrices (an anomalous-dimension matrix, or any chirality-even RG generator) and the number
of distinct eigenvalues of a generic element. Scalar cocycles (projective phases) cancel in
g X g^-1, so a PSG's scalar cocycle cannot change these counts.
Part B (charge grading): Z2^3 translation charges of chirality-odd mass terms are odd (HIER-2 R4a).
For a harmonic set S of a period-2 spurion, the minimal insertion order reaching charge c is the
Cayley-graph distance d_S(c). Enumerate all S.
"""
import itertools as it
import numpy as np

rng = np.random.default_rng(7)

# ---------- groups ----------
def proper_rotations():
    Rs = []
    for p in it.permutations(range(3)):
        for sg in it.product((1, -1), repeat=3):
            R = np.zeros((3, 3))
            for i in range(3):
                R[i, p[i]] = sg[i]
            if round(np.linalg.det(R)) == 1:
                Rs.append(R)
    return Rs

O = proper_rotations()
assert len(O) == 24

def perm_part(R):
    return np.abs(R)

def perm_sign(P):
    return round(np.linalg.det(P))

def su2_lift(R):
    # axis-angle -> U = cos(th/2) - i sin(th/2) n.sigma
    th = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
    if abs(th) < 1e-12:
        return np.eye(2, dtype=complex)
    if abs(th - np.pi) < 1e-9:
        M = (R + np.eye(3)) / 2
        k = np.argmax(np.diag(M)); n = M[:, k] / np.sqrt(M[k, k])
    else:
        n = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(th))
    return np.cos(th / 2) * np.eye(2) - 1j * np.sin(th / 2) * (n[0] * sx + n[1] * sy + n[2] * sz)

def is_T(R):  # tetrahedral rotations = those whose axis permutation is even
    return perm_sign(perm_part(R)) == 1

# ---------- commutant tools ----------
def commutant_dim(mats):
    n = mats[0].shape[0]
    rows = [np.kron(np.eye(n), g) - np.kron(g.T, np.eye(n)) for g in mats]  # vec(gX - Xg) = 0
    A = np.vstack(rows)
    s = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(s < 1e-9 * max(1, s.max())))  # complex dimension of commutant

def generic_levels(mats, trials=5):
    n = mats[0].shape[0]
    best = 0
    for _ in range(trials):
        X = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n)); X = X + X.conj().T
        Y = sum(g @ X @ np.linalg.inv(g) for g in mats) / len(mats)
        ev = np.sort(np.linalg.eigvalsh((Y + Y.conj().T) / 2))
        lv = 1 + int(np.sum(np.diff(ev) > 1e-8 * max(1, abs(ev).max())))
        best = max(best, lv)
    return best

def report(name, mats):
    print(f"  {name:62s} dim={mats[0].shape[0]:2d}  commutant(C)={commutant_dim(mats):2d}  distinct levels (generic)={generic_levels(mats)}")

print("Part A: lattice-symmetric Hermitian matrices on generation placements")
placements = {
    "X2' internal label (lattice acts trivially)": [np.eye(3) for R in O],
    "axis labels, permutation rep of O (O->S3)": [perm_part(R) for R in O],
    "axis labels, sign-twisted permutation (A2 x perm)": [perm_sign(perm_part(R)) * perm_part(R) for R in O],
    "orientations: vector rep T1 of O (GEN-2)": [R for R in O],
    "axis labels under T only (O\\T broken, e.g. A2 staggered term)": [perm_part(R) for R in O if is_T(R)],
}
for k, v in placements.items():
    report(k, v)
lifts = [(R, su2_lift(R)) for R in O]
lifts = lifts + [(R, -U) for R, U in lifts]          # binary octahedral 2O, 48 elements
report("axis labels x spin-1/2 under 2O", [np.kron(perm_part(R), U) for R, U in lifts])
report("T1 orientations x spin-1/2 under 2O", [np.kron(R, U) for R, U in lifts])
report("axis labels x spin-1/2 under 2T (O\\T broken)", [np.kron(perm_part(R), U) for R, U in lifts if is_T(R)])
# three corners at momenta pi e_i with translations: phase (-1)^{a_i} on corner i, rotations permute
trans = [np.diag([(-1) ** a[0], (-1) ** a[1], (-1) ** a[2]]).astype(complex) for a in it.product((0, 1), repeat=3)]
grp = [t @ perm_part(R) for t in trans for R in O]
report("corners pi e_i: Z2^3 translations x| O (no spin)", grp)
grp_s = [np.kron(t, np.eye(2)) @ np.kron(perm_part(R), U) for t in trans for R, U in lifts]
report("corners pi e_i x spin-1/2: Z2^3 x| 2O", grp_s)
grp_T = [t @ perm_part(R) for t in trans for R in O if is_T(R)]
report("corners pi e_i: Z2^3 x| T (O\\T broken)", grp_T)
# check the stated circulant form under T: commutant of C3 perm rep = a I + b C + conj(b) C^2
C = np.roll(np.eye(3), 1, axis=0)
X = 0.3 * np.eye(3) + (0.2 + 0.15j) * C + (0.2 - 0.15j) * C @ C
print("  circulant a=0.3, b=0.2+0.15i: eigenvalues", np.round(np.linalg.eigvalsh(X), 4),
      "; commutes with all T labels:", all(np.allclose(g @ X, X @ g) for g in placements["axis labels under T only (O\\T broken, e.g. A2 staggered term)"]))

# ---------- Part B ----------
print("\nPart B: minimal insertion order d_S(c) on odd Z2^3 charges")
els = [np.array(v) for v in it.product((0, 1), repeat=3)]
key = lambda v: tuple(int(x) for x in v)
nonzero = [v for v in els if v.any()]
odd = [v for v in els if v.sum() % 2 == 1]
hw = lambda v: int(v.sum())
# parity homomorphism
assert all((hw(a ^ b) - hw(a) - hw(b)) % 2 == 0 for a in els for b in els)
print("  hw mod 2 is additive on Z2^3: checked on all 64 pairs")

def dist(S, maxn=7):
    d = {key(np.zeros(3, int)): 0}
    frontier = [np.zeros(3, int)]
    for n in range(1, maxn + 1):
        new = []
        for v in frontier:
            for s in S:
                w = v ^ s
                if key(w) not in d:
                    d[key(w)] = n; new.append(w)
        frontier = new
    return [d.get(key(c), np.inf) for c in odd]

def axis_perm_images(S):
    imgs = set()
    for p in it.permutations(range(3)):
        imgs.add(frozenset(key(s[list(p)]) for s in S))
    return imgs

allS = []
for r in range(1, 8):
    for S in it.combinations(nonzero, r):
        allS.append(list(S))
cls = {h: [v for v in nonzero if hw(v) == h] for h in (1, 2, 3)}
print("  odd charges:", [key(c) for c in odd], " (hw:", [hw(c) for c in odd], ")")
for h in (1, 2, 3):
    print(f"  S = whole hw-{h} class: orders {dist(cls[h])}")
for combo in ((1, 2), (1, 3), (2, 3), (1, 2, 3)):
    S = sum((cls[h] for h in combo), [])
    print(f"  S = union of hw classes {combo}: orders {dist(S)}")
# single-class subsets (a spurion direction inside one irrep can switch off harmonics)
single = [S for S in allS if len({hw(s) for s in S}) == 1]
vals = set()
for S in single:
    vals |= {x for x in dist(S)}
print(f"  every subset of a single hw class ({len(single)} sets): finite orders used = {sorted(v for v in vals if v < np.inf)}; max distinct finite per set = {max(len({x for x in dist(S) if x < np.inf}) for S in single)}")
three = [S for S in allS if len({x for x in dist(S) if x < np.inf}) >= 3]
sym3 = [S for S in three if len(axis_perm_images(S)) == 1]
print(f"  all {len(allS)} harmonic sets: {len(three)} give >= 3 distinct finite orders; of these, S3-invariant: {len(sym3)}")
print(f"  of the {len(three)}, mixing hw parities: {sum(1 for S in three if len({hw(s)%2 for s in S})==2)}; using >= 2 hw classes: {sum(1 for S in three if len({hw(s) for s in S})>=2)}")
ex = min(three, key=len)
print(f"  smallest example: S = {[key(s) for s in ex]} -> orders {dist(ex)} on {[key(c) for c in odd]}")
