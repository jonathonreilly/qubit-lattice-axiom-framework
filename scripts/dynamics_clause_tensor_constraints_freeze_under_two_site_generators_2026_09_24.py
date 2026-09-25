#!/usr/bin/env python3
"""Supplied commuting tensor-electric slots: local freeze and explicit kernel moves.
Integer closed-neighbourhood obstructions have exact Smith certificates.
The radius-two MILP, coefficient bound four and fixed anchor one define a
restricted search, not a box-free minimum theorem. Planar ten-slot moves
are constructive witnesses; global minimality remains deferred.
"""
import itertools
import sys
from functools import reduce

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = ['docs/DYNAMICS_CLAUSE_THE_LANDED_TENSOR_CONSTRAINTS_FREEZE_UNDER_TWO_SITE_GENERATORS_AND_NO_SINGLE_NEIGHBOURHOOD_MOVES_THEM_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md']

import numpy as np
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
from scipy.optimize import Bounds, LinearConstraint, milp

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


E3 = np.eye(3, dtype=int)
PAIRS = [(0, 1), (1, 2), (0, 2)]


def key(x, i, j):
    return (tuple(x), (min(i, j), max(i, j)))


def slot_pos(k):
    """Doubled-coordinate site of a slot."""
    x, (i, j) = k
    p = 2 * np.array(x)
    if i != j:
        p = p + E3[i] + E3[j]
    return p


def row_terms(x, j):
    x = np.array(x)
    t = [(key(x + E3[j], j, j), 1), (key(x, j, j), -1)]
    for i in range(3):
        if i != j:
            t += [(key(x, i, j), 1), (key(x - E3[i], i, j), -1)]
    return t


# ------------------------------------------------------- 1. placement
L = 4
cells = list(itertools.product(range(L), repeat=3))


def wrap(k):
    x, ij = k
    return (tuple(int(c) % L for c in x), ij)


rows = {}
for x in cells:
    for j in range(3):
        r = {}
        for k, c in row_terms(x, j):
            kk = wrap(k)
            r[kk] = r.get(kk, 0) + c
        rows[(x, j)] = r
D = 2 * L


def dmod(p):
    return tuple(int(c) % D for c in p)


nbr_ok, coef_ok = True, True
for (x, j), r in rows.items():
    site = dmod(2 * np.array(x) + E3[j])
    nbrs = {dmod(np.array(site) + s * E3[a]) for a in range(3) for s in (1, -1)}
    pos = {dmod(slot_pos(k)) for k in r}
    nbr_ok &= pos == nbrs
    coef_ok &= all(abs(c) == 1 for c in r.values())
appear = {}
for (x, j), r in rows.items():
    for k in r:
        appear.setdefault(k, set()).add(dmod(2 * np.array(x) + E3[j]))
min_rows = min(len(v) for v in appear.values())
roles = {dmod(slot_pos(k)) for k in appear}
adjacent_fields = sum(1 for p in roles for a in range(3) for s in (1, -1) if dmod(np.array(p) + s * E3[a]) in roles)
check("placement: each row uses exactly its link site's six neighbours with coefficients +-1; each slot enters rows at >= 2 distinct link sites; slot sites are never adjacent",
      nbr_ok and coef_ok and min_rows >= 2 and adjacent_fields == 0,
      f"{len(rows)} rows on the L = {L} torus; fewest link sites per slot {min_rows} (diagonal 2, face 4); adjacent slot-site pairs {adjacent_fields}")

# --------------------------------------------------- 2. freeze, Z2 window
I2 = np.eye(2)
Xp = np.array([[1.0, 0], [0, -1.0]])        # clock operator diagonal in the slot value (Z2)
P1 = [np.eye(2, dtype=complex), np.array([[0, 1], [1, 0]], dtype=complex),
      np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1.0])]


def kron(*o):
    return reduce(np.kron, o)


# qubits: 0,1,2 = vertex v slots (xx, yy, zz); 3 = charge at x-link at v; 4 = charge at y-link at v; 5 = xy face at v
NQ = 6


def op1(m, k):
    return kron(*[m if i == k else I2 for i in range(NQ)])


tau = np.array([[1.0, 0], [0, -1.0]])
stabs = [op1(Xp, 0) @ op1(Xp, 5) @ op1(tau, 3),       # row at the x-link: p_xx(v), p_xy(v), charge
         op1(Xp, 1) @ op1(Xp, 5) @ op1(tau, 4),       # row at the y-link: p_yy(v), p_xy(v), charge
         op1(Xp, 0), op1(Xp, 1), op1(Xp, 2), op1(Xp, 2), op1(Xp, 5), op1(Xp, 5)]   # window parts of the other rows
groups = [(0, 1, 2, 3), (0, 1, 2, 4), (3, 5), (4, 5)]
basis = []
for g in groups:
    for idx in itertools.product(range(4), repeat=len(g)):
        basis.append(kron(*[P1[idx[g.index(q)]] if q in g else np.eye(2) for q in range(NQ)]))
cols = np.array([np.concatenate([(b @ s - s @ b).ravel() for s in stabs]) for b in basis]).T
gram = cols.conj().T @ cols                         # same null space as cols, small and square
gw, gv = np.linalg.eigh(gram)
ns = gv[:, gw < 1e-9 * max(1.0, gw.max())]
ops = [sum(ns[k, c] * basis[k] for k in range(len(basis))) for c in range(ns.shape[1])]
M = np.array([o.ravel() for o in ops])
sv = np.linalg.svd(M, compute_uv=False)
rank = int(np.sum(sv > 1e-9 * sv[0]))
worst = max(np.linalg.norm(o @ op1(Xp, q) - op1(Xp, q) @ o) for o in ops for q in (0, 1, 2, 5))
check("freeze: on a Z2 window, two-site operators commuting with every row's window part commute with every slot",
      rank == 27 and worst < 1e-9, f"invariant operator span of rank {rank}; max |[H, X_slot]| {worst:.1e}")

# ------------------------------------------- 3. no single neighbourhood
star_smith = {}
def star_null(center):
    center = np.array(center)
    near = [center] + [center + s * E3[a] for a in range(3) for s in (1, -1)]
    near = {tuple(p) for p in near}
    # slots whose site lies in the closed neighbourhood, on an open lattice patch
    sl = []
    for p in near:
        p = np.array(p)
        odd = [a for a in range(3) if p[a] % 2]
        if len(odd) == 0:
            x = p // 2
            sl += [key(x, j, j) for j in range(3)]
        elif len(odd) == 2:
            x = (p - E3[odd[0]] - E3[odd[1]]) // 2
            sl.append(key(x, odd[0], odd[1]))
    if not sl:
        return 0, 0
    sid = {k: i for i, k in enumerate(sl)}
    rr = []
    for x in itertools.product(range(-3, 4), repeat=3):
        for j in range(3):
            v = np.zeros(len(sl))
            hit = False
            for k, c in row_terms(x, j):
                if k in sid:
                    v[sid[k]] += c
                    hit = True
            if hit:
                rr.append(v)
    A = np.array(rr,dtype=int)
    Dsmith = smith_normal_form(Matrix(A),domain=ZZ)
    factors = [abs(int(Dsmith[i,i])) for i in range(len(sl))]
    star_smith[tuple(center)] = factors
    if tuple(center) == (1,1,1):
        assert np.all((A @ np.ones(len(sl),dtype=int)) % 2 == 0)
    return len(sl), factors.count(0)


stars = {"vertex": (0, 0, 0), "link": (1, 0, 0), "plaquette": (1, 1, 0), "cube": (1, 1, 1)}
res = {name: star_null(c) for name, c in stars.items()}
check("no single neighbourhood (integer slots): no nonzero Gauss-invariant slot change fits in any site's closed neighbourhood",
      all(nul == 0 for n_, nul in res.values()),
      "; ".join(f"{name}: {n_} slots, null dimension {nul}" for name, (n_, nul) in res.items()))

check("exact Smith factors: odd-N neighbourhood freeze; even-N cube half-period witness",
      [star_smith[c] for c in stars.values()] == [[1]*3,[1]*10,[1],[1]*5+[2]],
      str({name:star_smith[c] for name,c in stars.items()}))

# ------------------------------------------------ 4. the smallest moves
R = 2
bcells = list(itertools.product(range(-R, R + 1), repeat=3))
bslots = []
for x in bcells:
    for j in range(3):
        bslots.append(key(x, j, j))
    for (i, j) in PAIRS:
        bslots.append(key(x, i, j))
bid = {k: i for i, k in enumerate(bslots)}
brows = []
for x in itertools.product(range(-R - 1, R + 2), repeat=3):
    for j in range(3):
        v = {}
        for k, c in row_terms(x, j):
            if k in bid:
                v[bid[k]] = v.get(bid[k], 0) + c
        if v:
            brows.append(v)
nS, nR = len(bslots), len(brows)
G = np.zeros((nR, nS))
for r_, v in enumerate(brows):
    for s_, c in v.items():
        G[r_, s_] = c
Mb = 4
results = []
for s0 in [bid[key((0, 0, 0), 0, 0)], bid[key((0, 0, 0), 0, 1)]]:
    nvar = 2 * nS
    cost = np.concatenate([np.zeros(nS), np.ones(nS)])
    A = np.vstack([np.hstack([G, np.zeros((nR, nS))]), np.hstack([np.eye(nS), -Mb * np.eye(nS)]),
                   np.hstack([-np.eye(nS), -Mb * np.eye(nS)])])
    lb = [0] * nR + [-np.inf] * (2 * nS)
    ub = [0] * nR + [0] * (2 * nS)
    e = np.zeros(nvar)
    e[s0] = 1
    A = np.vstack([A, e])
    lb.append(1)
    ub.append(1)
    bounds = Bounds(np.concatenate([-Mb * np.ones(nS), np.zeros(nS)]), np.concatenate([Mb * np.ones(nS), np.ones(nS)]))
    sol = milp(cost, constraints=LinearConstraint(A, lb, ub), integrality=np.ones(nvar), bounds=bounds,
               options={"time_limit": 240})
    assert sol.status == 0 and sol.x is not None, f"restricted MILP did not finish: {sol.message}"
    d = np.round(sol.x[:nS]).astype(int)
    supp = [(bslots[s_], int(d[s_])) for s_ in range(nS) if d[s_] != 0]
    sites = {tuple(slot_pos(k)) for k, _ in supp}
    ext = [int(max(p[a] for p in sites) - min(p[a] for p in sites)) for a in range(3)]
    results.append((sol.status, len(supp), len(sites), sorted(ext), sorted({abs(c) for _, c in supp}), not np.any(G @ d), supp))
# the landed scalar-gauge pattern at a site, and its planar pieces
def s_row(x):
    x = np.array(x)
    v = {}
    for j in range(3):
        for i in range(3):
            if i == j:
                continue
            for s in (1, -1):
                v[key(x + s * E3[i], j, j)] = v.get(key(x + s * E3[i], j, j), 0) + 1
            v[key(x, j, j)] = v.get(key(x, j, j), 0) - 2
    for (i, j) in PAIRS:
        for sh, c in [((0, 0, 0), -1), (tuple(-E3[i]), 1), (tuple(-E3[j]), 1), (tuple(-E3[i] - E3[j]), -1)]:
            k = key(x + np.array(sh), i, j)
            v[k] = v.get(k, 0) + c
    return v


def planar(x, n_):
    a, b = [c for c in range(3) if c != n_]
    x = np.array(x)
    v = {}
    for (j, i) in ((a, b), (b, a)):
        for s in (1, -1):
            v[key(x + s * E3[i], j, j)] = v.get(key(x + s * E3[i], j, j), 0) + 1
        v[key(x, j, j)] = v.get(key(x, j, j), 0) - 2
    i, j = min(a, b), max(a, b)
    for sh, c in [((0, 0, 0), -1), (tuple(-E3[i]), 1), (tuple(-E3[j]), 1), (tuple(-E3[i] - E3[j]), -1)]:
        k = key(x + np.array(sh), i, j)
        v[k] = v.get(k, 0) + c
    return v


total = {}
for n_ in range(3):
    for k, c in planar((0, 0, 0), n_).items():
        total[k] = total.get(k, 0) + c
srow = s_row((0, 0, 0))
sum_ok = {k: c for k, c in total.items() if c} == {k: c for k, c in srow.items() if c}


def g_on(vec):
    worst_ = 0
    for x in itertools.product(range(-3, 4), repeat=3):
        for j in range(3):
            worst_ = max(worst_, abs(sum(c * vec.get(k, 0) for k, c in row_terms(x, j))))
    return worst_


planar_ok = all(g_on(planar((0, 0, 0), n_)) == 0 for n_ in range(3)) and g_on(srow) == 0
match = any(set((k, c) for k, c in results[1][6]) == set((k, s * c) for k, c in planar(x, 2).items() if c)
            for x in bcells for s in (1, -1))
ok4 = all(r[0] == 0 and r[1] == 10 and r[2] == 9 and r[3] == [0, 4, 4] and r[4] == [1, 2] and r[5] for r in results)
check("restricted radius-two, coefficient-bound-four, anchor-one minima: 10 slots on 9 sites, planar, coefficients 1 and 2; a planar piece of the landed scalar-gauge pattern, which is the sum of the three pieces",
      ok4 and sum_ok and planar_ok and match,
      f"through a diagonal slot: support {results[0][1]} on {results[0][2]} sites, doubled extent {results[0][3]}; through a face slot: support {results[1][1]} on {results[1][2]} sites; "
      f"solver optimal {all(r[0] == 0 for r in results)}; planar pieces in the kernel {planar_ok}; sum of pieces = S^T delta {sum_ok}; face-slot optimum is a planar piece {match}")

for resolution in ['N5 resolution 1: Commuting electric slots permit a product-basis freeze argument; arbitrary noncommuting on-site operators are outside scope.', 'N5 resolution 2: Exact Smith factors prove the integer and odd-N neighbourhood obstruction without numerical-rank inference.', 'N5 resolution 3: The even-N cube half-period vector is an explicit escaping modular move, so an all-N obstruction is false.', 'N5 resolution 4: Ten-slot planar patterns are exact kernel witnesses; the bounded MILP does not settle box-free minimality.', 'N5 resolution 5: Long winding shifts and changed supports remain available outside the stated finite-support neighbourhood class.']:
    print(resolution)
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
