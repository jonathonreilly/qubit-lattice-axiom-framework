"""synthesis-2 small check: the zoom-m family register under the FULL tetrahedral group.

Question: family-register counted protected families with ONE three-fold turn (F3 = m for a
(2m)^3 cell).  Does the count survive when the generic light-partner mass must be invariant
under all 12 tetrahedral rotations (the group the copy mass / mirror terms keep), and does any
protection survive if light-light masses are allowed (vector-like content)?

Model: m^3 register copies (sub-cube positions of a (2m)^3 cell, rotated about the cell centre);
light copy carries the 1-dim character E' (three-fold turn -> w), the partner copy E'' (w^2).
A bilinear mass M_{cc'} psibar_partner,c psi_light,c' is invariant iff P_g M P_g^T = lam(g) M,
lam = chi_light chi_partner^*.  Generic invariant M = group average of a random matrix.
Protected light copies = m^3 - rank(M).  Pure group theory; no dynamics.
"""
import itertools
import numpy as np

AUDIT_TIMEOUT_SEC = 60
rng = np.random.default_rng(7)
w = np.exp(2j * np.pi / 3)
npass = nfail = 0


def check(name, ok, detail=""):
    global npass, nfail
    if ok:
        npass += 1
    else:
        nfail += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")


# 12 rotations of T: det +1 signed permutations preserving the regular tetrahedron
tet = {(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)}
T = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        g = np.zeros((3, 3), dtype=int)
        for i in range(3):
            g[i, perm[i]] = signs[i]
        if round(np.linalg.det(g)) != 1:
            continue
        if {tuple(g @ np.array(v)) for v in tet} == tet:
            T.append(g)


def axis_perm_char(g):
    """A4 -> Z3 through the induced permutation of the three axes (V4 maps to 1)."""
    p = [int(np.nonzero(g[i])[0][0]) for i in range(3)]  # row i has its entry in column p[i]
    if p == [0, 1, 2]:
        return 1.0 + 0j
    if p == [1, 2, 0]:
        return w
    if p == [2, 0, 1]:
        return w ** 2
    raise ValueError("odd permutation in T")


chis = [axis_perm_char(g) for g in T]
# homomorphism check: chi(gh) = chi(g) chi(h)
hom_err = max(abs(axis_perm_char(g @ h) - axis_perm_char(g) * axis_perm_char(h)) for g in T for h in T)
check("A1 T has 12 rotations and g -> (axis 3-cycle) is a homomorphism onto Z3 (the E' character)",
      len(T) == 12 and hom_err < 1e-12, f"|T| = {len(T)}, hom error {hom_err:.0e}")


def perm_matrices(m):
    pts = [np.array(p) for p in itertools.product(range(m), repeat=3)]
    cen = [2 * p - (m - 1) for p in pts]  # centred integer coordinates
    index = {tuple(c): i for i, c in enumerate(cen)}
    Ps = []
    for g in T:
        P = np.zeros((len(pts), len(pts)))
        for i, c in enumerate(cen):
            P[index[tuple(g @ c)], i] = 1.0
        Ps.append(P)
    return Ps


def protected(m, group_idx, lam_fn):
    Ps = perm_matrices(m)
    n = m ** 3
    M0 = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Minv = sum(np.conj(lam_fn(k)) * Ps[k] @ M0 @ Ps[k].T for k in group_idx) / len(group_idx)
    # invariance residual
    res = max(np.abs(Ps[k] @ Minv @ Ps[k].T - lam_fn(k) * Minv).max() for k in group_idx)
    s = np.linalg.svd(Minv, compute_uv=False)
    rank = int((s > 1e-9 * np.linalg.norm(M0)).sum())  # absolute threshold: an all-forbidden M is pure rounding noise
    return n - rank, res


full = list(range(12))
turn = [k for k, g in enumerate(T) if np.array_equal(g @ np.array([1, 1, 1]), np.array([1, 1, 1]))]  # Z3 about (1,1,1)
lam_lp = lambda k: chis[k] * np.conj(chis[k] ** 2)  # light E' x conj(partner E'')

rows_full, rows_turn, ok_full, ok_turn = [], [], True, True
for m in range(1, 7):
    pf, rf = protected(m, full, lam_lp)
    pt, rt = protected(m, turn, lam_lp)
    rows_full.append(f"m={m}:{pf}")
    rows_turn.append(f"m={m}:{pt}")
    ok_full &= (pf == m and rf < 1e-9)
    ok_turn &= (pt == m and rt < 1e-9)
check("A2 one three-fold turn (family-register A1/B2 rederived): protected light copies = m for a (2m)^3 register",
      ok_turn, " ".join(rows_turn))
check("A3 full 12-element T: generic invariant light-partner mass still leaves exactly m protected copies "
      "(= n_A - n_E' = fixed points of a three-fold turn)", ok_full, " ".join(rows_full))

# character decomposition of the 3^3 register under T
Ps3 = perm_matrices(3)
chiP = np.array([np.trace(P) for P in Ps3])
irreps = {"A": np.ones(12), "E'": np.array(chis), "E''": np.array(chis) ** 2,
          "T": np.array([3 if np.array_equal(g, np.eye(3, dtype=int)) else (-1 if np.trace(g) == -1 else 0) for g in T])}
mult = {k: (chiP @ np.conj(v)).real / 12 for k, v in irreps.items()}
check("A4 3^3 register = 5A + 2E' + 2E'' + 6T, so n_A - n_E' = 3",
      all(abs(mult[k] - v) < 1e-9 for k, v in {"A": 5, "E'": 2, "E''": 2, "T": 6}.items()),
      ", ".join(f"{k} {v:.0f}" for k, v in mult.items()))

# vector-like control: light-light masses (trivial character) are allowed -> nothing protected
rows_v, ok_v = [], True
for m in range(1, 5):
    pv, rv = protected(m, full, lambda k: 1.0 + 0j)
    rows_v.append(f"m={m}:{pv}")
    ok_v &= (pv == 0)
check("A5 control: if light-light (same-character) masses are allowed, as on vector-like content, no copy is protected",
      ok_v, " ".join(rows_v))

# factor-2 rungs never give 3 | F3; zoom-3 is the smallest (2m)^3 register with 3 | m
f2 = [2 ** n for n in range(0, 8)]
check("A6 factor-2 blocks (m = 2^n) never have 3 | F3; m = 3 (6^3 cell) is the smallest with 3 | F3",
      all(x % 3 for x in f2) and min(mm for mm in range(1, 10) if mm % 3 == 0) == 3, f"F3 on 2^n blocks {f2}")

# mode count of one block-level reading: 6^3 sites = 27 sub-cubes x 8 corners
check("A7 arithmetic: a 6^3 block has 216 one-mode sites = 27 register sub-cubes x 8 corners ((4,2) cell labels)",
      6 ** 3 == 27 * 8, "216 = 27 x 8")

print("supplied: the register reading (sub-cube positions rotated about the cell centre), the light/partner")
print("  characters E'/E'' (the two copies of the three-fold turn), bilinear masses only; no dynamics, no anomaly input.")
print(f"TOTAL: PASS={npass} FAIL={nfail}")
