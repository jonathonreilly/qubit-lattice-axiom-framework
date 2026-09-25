#!/usr/bin/env python3
"""Time-reversal-odd star terms: what covariance allows, and whether any keeps the cube carving's Majoranas free.

Time reversal flips every Pauli, so a Pauli string is odd under it exactly
when its weight is odd. The smallest odd terms are one-site fields and
three-spin terms. Inside one Admissibility neighbourhood (a site m and its
six neighbours: a star) a three-spin term sits on one of four classes of
triples: through the centre with perpendicular or with collinear
neighbours, the three neighbours of one octant, or a collinear pair of
neighbours plus a third (mixed). The runner certifies (supplied models,
finite diagnostics, no physical reading):

1. Possibility covariance (lattice rotations on positions, every internal
   rotation) allows exactly one T-odd star term of weight at most three:
   the orientation-weighted scalar chirality of each octant's neighbours,
   sum det[d1 d2 d3] s_d1 . (s_d2 x s_d3). It avoids the centre.
2. Under the four landed actions the covariant T-odd star terms of weight
   at most three span 68, 50, 49, 37 dimensions (trivial, sign twist, axis,
   full); by class: fields 3/1/0/0, through-centre perpendicular
   18/12/12/12, through-centre collinear 18/8/8/2, octant 11/11/11/11,
   mixed 18/18/18/12.
3. None contains Kitaev's pattern s^a_i s^c_m s^b_k (a, b the bond axes to
   i and k, c the third axis): zero intersection for every action.
4. On the 8-site cube carving the Pauli strings that commute with all six
   loop operators are exactly the 2048 products of bond operators
   s^a_j s^a_k over edge sets. In Kitaev's representation a bond operator
   is i u_jk c_j c_k, so a product leaves Majorana matter on the sites of
   odd degree: its Majorana degree is 0, 2 or 4. Kitaev's pattern has
   degree 2; the tripod s^x_{m+dx} s^y_{m+dy} s^z_{m+dz} equals
   -i (s^x_m s^x_{m+dx})(s^y_m s^y_{m+dy})(s^z_m s^z_{m+dz}) and has degree 4.
5. On the cube, under every covariance, no nonzero covariant T-odd star term
   inside the carving both keeps the six loops and is bilinear in the
   Majoranas. Under the axis and full actions exactly one keeps the loops:
   the tripod summed over octants with sign d_x d_y d_z, which is quartic.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys
from functools import reduce

AUDIT_INPUT_PATHS = ('docs/DYNAMICS_CLAUSE_TIME_REVERSAL_ODD_STAR_TERMS_COVARIANCE_ALLOWS_THEM_AND_ON_THE_CUBE_CARVING_NONE_KEEPS_THE_MAJORANAS_FREE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/DYNAMICS_CLAUSE_RECORDS_CARVE_KITAEV_MODELS_AT_THE_COMPASS_POINT_ZERO_FIELD_CARVINGS_ARE_CUBES_AND_TUBES_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/THE_SOLDERING_MENU_FOUR_ACTIONS_OF_THE_PROPER_CUBIC_ROTATIONS_ON_QUBIT_POSSIBILITIES_AND_WHAT_EACH_LETS_FORMATION_BUILD_BOUNDED_THEOREM_NOTE_2026-09-22.md')
AUDIT_TIMEOUT_SEC = 300

import numpy as np

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


rots = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[i, perm[i]] = signs[i]
        if np.isclose(np.linalg.det(R), 1):
            rots.append(R)


def perm_sign(R):
    return round(np.linalg.det(np.abs(R)))


ACTS = {"trivial": lambda R: np.eye(3), "sign twist": lambda R: np.diag([1.0, perm_sign(R), perm_sign(R)]),
        "axis": lambda R: perm_sign(R) * np.abs(R), "full": lambda R: R}
POS = [np.zeros(3, dtype=int)] + [np.array(v) for v in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]
CLASSES = ["field", "centre-perp", "centre-collinear", "octant", "mixed"]


def sidx(v):
    return [k for k, u in enumerate(POS) if np.array_equal(u, v)][0]


def cls(sup):
    if len(sup) == 1:
        return "field"
    if 0 in sup:
        a, b = [POS[s] for s in sup if s != 0]
        return "centre-perp" if a @ b == 0 else "centre-collinear"
    a, b, c = [POS[s] for s in sup]
    return "octant" if a @ b == 0 and b @ c == 0 and a @ c == 0 else "mixed"


# basis: the centre field (a field on a neighbour is the same lattice-wide term) and every three-spin string in the star
basis = {}
for sup in [(0,)] + list(itertools.combinations(range(7), 3)):
    for labs in itertools.product(range(3), repeat=len(sup)):
        basis[(sup, labs)] = len(basis)
n = len(basis)
classes = [cls(k[0]) for k in basis]


def rot_matrix(R, r):
    M = np.zeros((n, n))
    for (sup, labs), col in basis.items():
        new = [sidx(R @ POS[s]) for s in sup]
        for labs2 in itertools.product(range(3), repeat=len(sup)):
            coef = np.prod([r[b, a] for a, b in zip(labs, labs2)])
            if abs(coef) > 1e-12:
                order = sorted(range(len(sup)), key=lambda t: new[t])
                M[basis[(tuple(new[t] for t in order), tuple(labs2[t] for t in order))], col] += coef
    return M


def invariant(Ms):
    P = sum(Ms) / len(Ms)
    w, v = np.linalg.eigh((P + P.T) / 2)
    return v[:, w > 0.5]


def class_dims(C):
    return [int(np.linalg.matrix_rank(C[[i for i in range(n) if classes[i] == c]], tol=1e-9)) if C.shape[1] else 0
            for c in CLASSES]


covs = {name: invariant([rot_matrix(R, rho(R)) for R in rots]) for name, rho in ACTS.items()}

# ------------------------------------------------ 1. possibility covariance
GEN = [np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]]), np.array([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
       np.array([[0, -1, 0], [1, 0, 0], [0, 0, 0]])]


def gen_matrix(L):
    G = np.zeros((n, n))
    for (sup, labs), col in basis.items():
        for t in range(len(sup)):
            for b in range(3):
                if L[b, labs[t]]:
                    labs2 = list(labs)
                    labs2[t] = b
                    G[basis[(sup, tuple(labs2))], col] += L[b, labs[t]]
    return G


Ct = covs["trivial"]
_, sv, vt = np.linalg.svd(np.vstack([gen_matrix(L) @ Ct for L in GEN]))
covs["possibility"] = Ct @ vt[int(np.sum(sv > 1e-9)):].T
eps = np.zeros((3, 3, 3))
for p in itertools.permutations(range(3)):
    eps[p] = np.linalg.det(np.eye(3)[list(p)])
chir = np.zeros(n)
for (sup, labs), col in basis.items():
    if cls(sup) == "octant":
        chir[col] = np.linalg.det(np.array([POS[s] for s in sup])) * eps[labs]
Cp = covs["possibility"]
resid = np.linalg.norm(chir - Cp @ (Cp.T @ chir)) / np.linalg.norm(chir)
check("possibility covariance allows one T-odd star term of weight <= 3: the orientation-weighted octant chirality",
      Cp.shape[1] == 1 and class_dims(Cp) == [0, 0, 0, 1, 0] and resid < 1e-12,
      f"dimension {Cp.shape[1]}; by class (field, centre-perp, centre-collinear, octant, mixed) {class_dims(Cp)}; "
      f"sum det[d1 d2 d3] s_d1.(s_d2 x s_d3) residual {resid:.1e}")

# ------------------------------------------------ 2. the landed actions
dims = {name: class_dims(covs[name]) for name in ACTS}
expect = {"trivial": [3, 18, 18, 11, 18], "sign twist": [1, 12, 8, 11, 18], "axis": [0, 12, 8, 11, 18],
          "full": [0, 12, 2, 11, 12]}
check("under the four landed actions the covariant T-odd star terms of weight <= 3 span 68, 50, 49, 37 dimensions",
      dims == expect and [covs[k].shape[1] for k in ACTS] == [68, 50, 49, 37],
      f"totals {[covs[k].shape[1] for k in ACTS]}; by class " + "; ".join(f"{k} {v}" for k, v in dims.items()))


# ------------------------------------------------ 3. Kitaev's pattern
def axis_of(v):
    return int(np.argmax(np.abs(v)))


kit = []
for (sup, labs), col in basis.items():
    if cls(sup) == "centre-perp":
        i, k = [s for s in sup if s != 0]
        a, c = axis_of(POS[i]), axis_of(POS[k])
        li, lm, lk = [labs[sup.index(s)] for s in (i, 0, k)]
        if li == a and lk == c and lm == 3 - a - c:
            kit.append(col)
Q = np.zeros((n, len(kit)))
for j, col in enumerate(kit):
    Q[col, j] = 1
inters = [covs[k].shape[1] + Q.shape[1] - np.linalg.matrix_rank(np.hstack([covs[k], Q]), tol=1e-9)
          for k in list(ACTS) + ["possibility"]]
check("no covariant T-odd star term contains Kitaev's pattern s^a_i s^c_m s^b_k",
      len(kit) == 12 and inters == [0] * 5, f"pattern terms {len(kit)}; intersections {[int(x) for x in inters]}")

# ------------------------------------------------ 4. the cube: loop commutant, bond products, Majorana degree
cube = list(itertools.product((0, 1), repeat=3))
cid = {s: i for i, s in enumerate(cube)}
edges = [(cid[s], cid[tuple(1 if t == ax else s[t] for t in range(3))], ax) for s in cube for ax in range(3) if s[ax] == 0]
MUL = {}
for a in range(4):
    for b in range(4):
        MUL[(a, b)] = a if b == 0 else b if a == 0 else 0 if a == b else 6 - a - b


def pmul(p, q):
    return tuple(MUL[(a, b)] for a, b in zip(p, q))


def commutes(p, q):
    return sum(1 for a, b in zip(p, q) if a and b and a != b) % 2 == 0


loops = [tuple(ax + 1 if s[ax] == val else 0 for s in cube) for ax in range(3) for val in (0, 1)]
degree = {}
for mask in range(1 << len(edges)):
    p, deg = (0,) * 8, [0] * 8
    for e, (i, j, ax) in enumerate(edges):
        if mask >> e & 1:
            q = [0] * 8
            q[i] = q[j] = ax + 1
            p = pmul(p, tuple(q))
            deg[i] += 1
            deg[j] += 1
    odd = sum(d % 2 for d in deg)
    degree[p] = min(degree.get(p, 9), odd, 8 - odd)
commutant = [p for p in itertools.product(range(4), repeat=8) if all(commutes(p, W) for W in loops)]
I2 = np.eye(2, dtype=complex)
PAU = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1.0])]


def op(ops):
    return reduce(np.kron, [ops.get(i, I2) for i in range(8)])


m0, nx, ny, nz = cid[(0, 0, 0)], cid[(1, 0, 0)], cid[(0, 1, 0)], cid[(0, 0, 1)]
tripod = op({nx: PAU[0], ny: PAU[1], nz: PAU[2]})
kkk = op({m0: PAU[0], nx: PAU[0]}) @ op({m0: PAU[1], ny: PAU[1]}) @ op({m0: PAU[2], nz: PAU[2]})
theta = reduce(np.kron, [PAU[1]] * 8)                      # time reversal: prod_j i s^y_j, then complex conjugation
t_odd = np.linalg.norm(theta @ tripod.conj() @ theta.conj().T + tripod)
kit_p = [0] * 8
kit_p[nx], kit_p[m0], kit_p[ny] = 1, 3, 2                  # s^x_{m+x} s^z_m s^y_{m+y}
tri_p = [0] * 8
tri_p[nx], tri_p[ny], tri_p[nz] = 1, 2, 3
check("on the cube, loop-commuting Pauli strings are the bond-operator products; Majorana degree 0, 2 or 4",
      len(degree) == 2048 and len(commutant) == 2048 and all(p in degree for p in commutant)
      and sorted(set(degree.values())) == [0, 2, 4] and degree[tuple(kit_p)] == 2 and degree[tuple(tri_p)] == 4
      and np.linalg.norm(tripod - (-1j) * kkk) < 1e-12 and t_odd < 1e-12,
      f"commutant {len(commutant)} = products {len(degree)}; Kitaev pattern degree {degree[tuple(kit_p)]}; "
      f"tripod = -i K_x K_y K_z residual {np.linalg.norm(tripod + 1j * kkk):.0e}, degree {degree[tuple(tri_p)]}, "
      f"time-reversal odd residual {t_odd:.0e}")

# ------------------------------------------------ 5. covariant T-odd terms on the cube
rows = {}
for m in cube:
    for (sup, labs), col in basis.items():
        sites = [tuple(np.array(m) + POS[s]) for s in sup]
        if all(x in cid for x in sites):
            p = [0] * 8
            for x, a in zip(sites, labs):
                p[cid[x]] = a + 1
            rows.setdefault(tuple(p), {}).setdefault(col, 0)
            rows[tuple(p)][col] += 1
strs = list(rows)
A = np.zeros((len(strs), n))
for r, p in enumerate(strs):
    for col, v in rows[p].items():
        A[r, col] = v
keeps = np.array([all(commutes(p, W) for W in loops) for p in strs])
free = np.array([keeps[r] and degree[p] <= 2 for r, p in enumerate(strs)])


def restricted(C, allowed):
    Y = A @ C
    if not C.shape[1]:
        return 0, None
    _, sv, vt = np.linalg.svd(Y[~allowed]) if (~allowed).any() else (None, np.zeros(0), np.eye(C.shape[1]))
    N = vt[int(np.sum(sv > 1e-9)):].T
    return (int(np.linalg.matrix_rank(Y @ N, tol=1e-9)) if N.shape[1] else 0), (C @ N if N.shape[1] else None)


tri_vec = np.zeros(n)
for (sup, labs), col in basis.items():
    if cls(sup) == "octant":
        d = [POS[s] for s in sup]
        if list(labs) == [axis_of(x) for x in d]:
            tri_vec[col] = np.prod([x[axis_of(x)] for x in d])
table, tripod_ok = [], True
for name in list(ACTS) + ["possibility"]:
    C = covs[name]
    on_cube = int(np.linalg.matrix_rank(A @ C, tol=1e-9))
    n_keep, Nk = restricted(C, keeps)
    n_free, _ = restricted(C, free)
    table.append((name, on_cube, n_keep, n_free))
    if n_keep:
        Y = A @ Nk
        degs = {degree[strs[r]] for r in range(len(strs)) if np.linalg.norm(Y[r]) > 1e-9}
        w = Nk[:, int(np.argmax(np.linalg.norm(Y, axis=0)))]
        yw, yt = A @ w, A @ tri_vec
        match = np.linalg.norm(yw / np.linalg.norm(yw) - np.sign(yw @ yt) * yt / np.linalg.norm(yt))
        tripod_ok &= degs == {4} and match < 1e-9
check("on the cube no covariant T-odd star term keeps the loops and the Majoranas free; the loop-keeper is the quartic tripod",
      [t[1] for t in table] == [32, 24, 23, 23, 1] and [t[3] for t in table] == [0] * 5 and [t[2] for t in table] == [0, 0, 1, 1, 0] and tripod_ok,
      "; ".join(f"{t[0]}: on cube {t[1]}, keep loops {t[2]}, free {t[3]}" for t in table)
      + "; the loop-keeper is sum sign(dx dy dz) s^x s^y s^z over octants, degree 4")

print('per_element: Pauli compression, signed group actions and declared Clifford identities are the element-level checks.')
print('per_site: Local supports and explicit carving-site constraints are checked only under the supplied record rules.')
print('per_mode: checked and not executed: this finite cube obstruction makes no momentum-band or continuum claim.')
print('per_block: Named finite cells and covariance coefficient spaces are checked with their explicit size and support restrictions.')
print('lattice_wide: General lattice conclusions rely only on displayed conditional arguments; finite searches do not certify physical emergence.')
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
