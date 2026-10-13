"""R16-11 s4 (written before running).  Minimal-weight qubit (spin-1/2: entries in {-1,0,1}) pattern m with
G m = 0 exactly (N0914 stencil), compactly supported in a box, containing a prescribed slot.
Its weight w is the lowest Schrieffer-Wolff order at which a transverse-field 'tensor ice'
H = U sum_j (G_j E)^2 - J_perp sum_s S^x_s can generate an exactly invariant hop (amplitude ~ J_perp^w / U^(w-1)).
Expectation: w <= 20 (2x2 planar Airy, s1 (B)); w >= 3 (s1 (C)); possibly smaller non-planar patterns.
Uses scipy.optimize.milp with a time limit; reports optimality status honestly.
"""
import numpy as np, itertools
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix
TYPES = [(0,0),(1,1),(2,2),(0,1),(1,2),(0,2)]
E3 = np.eye(3, dtype=int)
def G_entries(x, t):
    i, j = TYPES[t]; x = np.array(x); out = []
    if i == j: out += [((tuple(x - E3[j]), j), 1), ((tuple(x), j), -1)]
    else: out += [((tuple(x), j), 1), ((tuple(x + E3[i]), j), -1), ((tuple(x), i), 1), ((tuple(x + E3[j]), i), -1)]
    return out
for B, fix in [(4, ((1, 1, 1), 0)), (4, ((1, 1, 1), 3))]:
    slots = [(x, t) for x in itertools.product(range(B), repeat=3) for t in range(6)]
    sidx = {s: n for n, s in enumerate(slots)}
    gs = {}
    for s in slots:
        for g, v in G_entries(*s):
            gs.setdefault(g, len(gs))
    nS = len(slots); nv = 2*nS
    A = lil_matrix((len(gs), nv))
    for n, s in enumerate(slots):
        for g, v in G_entries(*s):
            A[gs[g], n] += v; A[gs[g], nS + n] -= v
    cons = [LinearConstraint(A.tocsr(), 0, 0)]
    P = lil_matrix((nS, nv))
    for n in range(nS): P[n, n] = 1; P[n, nS + n] = 1
    cons.append(LinearConstraint(P.tocsr(), 0, 1))
    lb = np.zeros(nv); ub = np.ones(nv); lb[sidx[fix]] = 1   # fixed slot: m = +1
    res = milp(c=np.ones(nv), constraints=cons, integrality=np.ones(nv), bounds=Bounds(lb, ub),
               options={'time_limit': 200, 'disp': False})
    if res.x is None:
        print("box %d fix %s: no solution (%s)" % (B, fix, res.message)); continue
    m = np.round(res.x[:nS] - res.x[nS:]).astype(int)
    supp = [(slots[n], m[n]) for n in range(nS) if m[n]]
    # verify exactly
    chk = {}
    for (x, t), v in supp:
        for g, c in G_entries(x, t): chk[g] = chk.get(g, 0) + c*v
    ok = all(v == 0 for v in chk.values())
    xs = np.array([x for (x, t), v in supp])
    print("box %d, fixed slot %s: status=%s ; weight w=%d ; exact Gm=0: %s ; extent=%s ; types used=%s" %
          (B, fix, res.message, len(supp), ok, xs.max(0) - xs.min(0) + 1, sorted(set(TYPES[t] for (x, t), v in supp))))
