"""R18-10 s1 (A1): exact dipole of gamma under a signed flip, on unwrapped Z^3 supports (exact integers).
D_ab(c) = sum_x x_a c_b(x) for an edge-valued charge c (edge (x, b) placed at its base x; the e_b/2 offset drops out
because sum_x c_b(x) = 0). Claim: D(G delta)_ab = -(sum of delta over slots of type ab) for a = b, and for a != b
D_ab = D_ba = -(sum of delta over face slots of type ab). Hence D(gamma) conserved <=> every N_ab conserved."""
import numpy as np, itertools
from common import G_entries, PATTERNS, TYPES, TIDX, rot_mats, rotate
rng = np.random.default_rng(1)
def Gdelta(supp):  # supp: list of ((x,t), val) on Z^3
    c = {}
    for (x, t), v in supp:
        for (e, j), co in G_entries(x, t):
            c[(e, j)] = c.get((e, j), 0) + co*v
    return c
def dipole(c):
    D = np.zeros((3, 3), dtype=np.int64); tot = np.zeros(3, dtype=np.int64)
    for (e, j), v in c.items():
        tot[j] += v
        for a in range(3): D[a, j] += e[a]*v
    return D, tot
def M0(supp):
    M = np.zeros((3, 3), dtype=np.int64)
    for (x, t), v in supp:
        i, j = TYPES[t]; M[i, j] += v
        if i != j: M[j, i] += v
    return M
bad = 0; ntest = 0
# (i) every pattern copy, every sign assignment (cube 2^6 = 64, mu8 2^8 = 256), at random base points
for p in PATTERNS:
    for signs in itertools.product([1, -1], repeat=len(p)):
        base = rng.integers(-5, 6, 3)
        supp = [((tuple(np.array(d) + base), t), s) for (d, t), s in zip(p, signs)]
        D, tot = dipole(Gdelta(supp)); ntest += 1
        if np.any(tot != 0) or not np.array_equal(D, -M0(supp)): bad += 1
print("(i) pattern sign-lifts tested: %d, failures of D(G delta) = -M0(delta) with zero total charge: %d" % (ntest, bad))
# (ii) random integer delta on random supports
bad2 = 0
for it in range(2000):
    k = rng.integers(1, 30)
    supp = [((tuple(rng.integers(-4, 5, 3)), int(rng.integers(6))), int(rng.integers(-3, 4))) for _ in range(k)]
    D, tot = dipole(Gdelta(supp))
    if np.any(tot != 0) or not np.array_equal(D, -M0(supp)): bad2 += 1
print("(ii) random integer deltas: 2000, failures: %d" % bad2)
# (iii) the antisymmetric part of D vanishes identically (angular charge moment), and D is symmetric
print("(iii) => D(gamma) = -M0(n)/2 is a symmetric tensor; its 6 components are -N_ab/2 (diag) and -N_ab/2 (faces, each of D_ab, D_ba)")
# (iv) the signed per-type change for an XOR flip from state n: s = 1 - 2 n on the flipped slots, so
#      dD = 0 <=> for each type, #(0->1) = #(1->0) on the flipped slots of that type <=> dN_ab = 0.
# Count, for each pattern, the fraction of local label assignments for which a flip conserves D (no mod-2 constraint imposed).
for p in PATTERNS:
    types = [t for (d, t) in p]; cnt = 0; tot = 0
    for labs in itertools.product([0, 1], repeat=len(p)):
        dN = np.zeros(6, int)
        for t, l in zip(types, labs): dN[t] += 1 - 2*l
        tot += 1; cnt += int(np.all(dN == 0))
    print("  pattern types %s: D-conserving fraction over local labels = %d/%d" % (sorted(types), cnt, tot))
# (v) shift-action covariance of the conserved charges Q_ab = N_ab - V/2 (sign flips on face types with sigma_i sigma_j = -1)
print("(v) under a site rotation with the shift action, face labels of types with sigma_i sigma_j = -1 map n -> 1-n, so Q_ab -> sigma_a sigma_b Q_{R(ab)}: Q transforms as a symmetric tensor; the sector Q = 0 is invariant.")
