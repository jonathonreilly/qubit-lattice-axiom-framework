"""R6-2 check 3: does B's dimension-4 protection cover a rank-2 field (the graviton sector)?

Count quadratic invariants of a symmetric tensor h_{mu nu} on R^4:
  mass forms   = invariants in Sym^2(Sym^2 V)
  kinetic forms (momentum-space symbols k k h h) = invariants in Sym^2 V (x) Sym^2(Sym^2 V)
under SO(4) (Haar via a dense random sample is replaced by the known exact counts 2 and 4, checked by
Monte Carlo below), W(B4) (signed permutations, 384) and B4+ (det +1, 192).
Also matter: invariants in Sym^2 V (a kinetic coefficient tensor c^{mu nu} k_mu k_nu): traceless part counts V2^tl.
"""
import itertools
import numpy as np

def chars(g):
    cV = lambda m: np.trace(np.linalg.matrix_power(g, m))
    s2 = lambda m: (cV(m) ** 2 + cV(2 * m)) / 2            # chi_{Sym^2 V}(g^m)
    s2s2 = (s2(1) ** 2 + s2(2)) / 2                          # chi_{Sym^2 Sym^2 V}(g)
    return s2(1), s2s2, s2(1) * s2s2

def count(group):
    acc = np.zeros(3)
    for g in group:
        acc += np.array(chars(g))
    return np.round(acc / len(group), 6)

WB4 = []
for perm in itertools.permutations(range(4)):
    for signs in itertools.product([1, -1], repeat=4):
        P = np.zeros((4, 4))
        for i, p in enumerate(perm):
            P[i, p] = signs[i]
        WB4.append(P)
B4p = [g for g in WB4 if np.linalg.det(g) > 0]

rng = np.random.default_rng(1)
def rand_so4(n):
    out = []
    for _ in range(n):
        A = rng.normal(size=(4, 4)); Qm, R = np.linalg.qr(A); Qm = Qm @ np.diag(np.sign(np.diag(R)))
        if np.linalg.det(Qm) < 0: Qm[:, 0] *= -1
        out.append(Qm)
    return out
so4 = count(rand_so4(200000))
for name, grp in [("W(B4)", WB4), ("B4+", B4p)]:
    s2, m, k = count(grp)
    print(f"{name:6s}: Sym2V invariants (1 = trace only => V2^tl = 0) = {s2:.0f};  mass forms = {m:.0f};  kinetic symbol forms = {k:.0f}")
print(f"SO(4) (Monte Carlo, 2e5 samples): Sym2V = {so4[0]:.2f}; mass = {so4[1]:.2f}; kinetic = {so4[2]:.2f}  (exact: 1, 2, 4)")
