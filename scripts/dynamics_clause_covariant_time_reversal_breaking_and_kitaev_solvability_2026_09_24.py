#!/usr/bin/env python3
"""Time-reversal-odd star terms: what covariance allows, and why they cannot keep carvings solvable.

A three-spin term s^alpha_i s^beta_m s^gamma_k on a site m and two of its
neighbours i, k is odd under time reversal. It is the smallest term that
breaks time reversal in the dynamics, and it lies in m's neighbourhood (a
star term). The runner certifies (supplied models, finite diagnostics, no
physical reading):

1. Under possibility covariance (every internal rotation) the only
   three-spin form is the scalar chirality s_i . (s_m x s_k). Its covariant
   sum over neighbour pairs vanishes, because a proper rotation swaps any
   ordered pair of neighbour directions while the chirality changes sign.
2. Under the four landed actions, covariant T-odd three-spin star terms on
   perpendicular pairs span dimensions 18, 12, 12, 12 (trivial, sign twist,
   axis, full soldering).
3. None has Kitaev's solvable pattern s^a_i s^c_m s^b_k (a, b the bond axes
   to i and k, c the third axis): the intersection is zero for all four
   actions.
4. On the 8-site cube carving, Kitaev-pattern terms commute with all six
   loop operators, while no nonzero covariant T-odd term (full soldering)
   commutes with all of them. So a covariant T-odd star term does not keep
   the cube exactly solvable.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys
from functools import reduce

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
NB = [np.array(v) for v in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]


def idx(v):
    return [k for k, u in enumerate(NB) if np.array_equal(u, v)][0]


def axis_of(v):
    return int(np.argmax(np.abs(v)))


# ------------------------------------------------ 1. possibility covariance
ok1 = True
for kind in ("perp", "collinear"):
    pairs = [(i, k) for i in range(6) for k in range(6) if i != k and
             ((kind == "perp" and NB[i] @ NB[k] == 0) or (kind == "collinear" and NB[i] @ NB[k] == -1))]
    i0, k0 = pairs[0]
    tot = {}
    for R in rots:
        i2, k2 = idx(R @ NB[i0]), idx(R @ NB[k0])
        tot[(i2, k2)] = tot.get((i2, k2), 0) + 1
        tot[(k2, i2)] = tot.get((k2, i2), 0) - 1          # chi_{i m k} = -chi_{k m i}
    ok1 &= all(abs(v) < 1e-12 for v in tot.values())
check("possibility covariance: the covariant sum of scalar chiralities s_i.(s_m x s_k) over neighbour pairs vanishes",
      ok1, "perpendicular and collinear pairs: every group-averaged coefficient is 0")

# ------------------------------------------------ 2-3. covariant T-odd terms and the Kitaev pattern
pairs = [(i, k) for i in range(6) for k in range(6) if i != k and NB[i] @ NB[k] == 0]
basis = {}
for (i, k) in pairs:
    for a, b, c in itertools.product(range(3), repeat=3):
        key = min((i, k, a, b, c), (k, i, c, b, a))
        basis.setdefault(key, len(basis))
n = len(basis)
kit = [col for (i, k, a, b, c), col in basis.items() if a == axis_of(NB[i]) and c == axis_of(NB[k]) and b == 3 - a - c]
Q = np.zeros((n, len(kit)))
for j, col in enumerate(kit):
    Q[col, j] = 1
dims, inters, covspaces = [], [], {}
for name, rho in ACTS.items():
    P = np.zeros((n, n))
    for R in rots:
        r = rho(R)
        M = np.zeros((n, n))
        for (i, k, a, b, c), col in basis.items():
            i2, k2 = idx(R @ NB[i]), idx(R @ NB[k])
            for a2, b2, c2 in itertools.product(range(3), repeat=3):
                coef = r[a2, a] * r[b2, b] * r[c2, c]
                if abs(coef) > 1e-12:
                    key = min((i2, k2, a2, b2, c2), (k2, i2, c2, b2, a2))
                    M[basis[key], col] += coef
        P += M
    P /= len(rots)
    w, v = np.linalg.eigh((P + P.T) / 2)
    cov = v[:, w > 0.5]
    covspaces[name] = cov
    dims.append(cov.shape[1])
    inters.append(cov.shape[1] + Q.shape[1] - np.linalg.matrix_rank(np.hstack([cov, Q]), tol=1e-9))
check("covariant T-odd three-spin star terms exist under the four landed actions",
      dims == [18, 12, 12, 12], f"dimensions (trivial, sign twist, axis, full) {dims}")
check("none has Kitaev's solvable pattern s^a_i s^c_m s^b_k: the intersection is zero for every action",
      inters == [0, 0, 0, 0], f"Kitaev-pattern terms {len(kit)}; intersections {[int(x) for x in inters]}")

# ------------------------------------------------ 4. the cube carving
I2 = np.eye(2, dtype=complex)
PAU = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1.0])]
cube = list(itertools.product((0, 1), repeat=3))
cid = {s: i for i, s in enumerate(cube)}


def op(ops):
    return reduce(np.kron, [ops.get(i, I2) for i in range(8)])


loops = []
for axn in range(3):
    for val in (0, 1):
        face = [s for s in cube if s[axn] == val]
        loops.append(op({cid[s]: PAU[axn] for s in face}))


def cube_term(i_s, m_s, k_s, a, b, c):
    return op({cid[i_s]: PAU[a], cid[m_s]: PAU[b], cid[k_s]: PAU[c]})


kit_worst, cov_broken = 0.0, 0
for m_s in cube:
    nbrs_c = []
    for axn in range(3):
        t = list(m_s)
        t[axn] = 1 - t[axn]
        nbrs_c.append((tuple(t), axn))
    for (i_s, a), (k_s, b) in itertools.permutations(nbrs_c, 2):
        c = 3 - a - b
        T = cube_term(i_s, m_s, k_s, a, c, b)
        kit_worst = max(kit_worst, max(np.linalg.norm(T @ W - W @ T) for W in loops))
# every covariant T-odd term (full soldering), evaluated on the cube's triples, against the loop operators
def cube_H(vec):
    H = np.zeros((256, 256), dtype=complex)
    for m_s in cube:
        for (i, k, a, b, c), col in basis.items():
            if abs(vec[col]) < 1e-12:
                continue
            i_s = tuple(np.array(m_s) + NB[i])
            k_s = tuple(np.array(m_s) + NB[k])
            if i_s in cid and k_s in cid:
                H += vec[col] * cube_term(i_s, m_s, k_s, a, b, c)
    return H


covf = covspaces["full"]
Hs = [cube_H(covf[:, j]) for j in range(covf.shape[1])]
comm_rows = np.array([np.concatenate([(H @ W - W @ H).ravel() for W in loops]) for H in Hs])
nonzero_on_cube = np.linalg.matrix_rank(np.array([H.ravel() for H in Hs]), tol=1e-9)
solvable_dim = nonzero_on_cube - np.linalg.matrix_rank(comm_rows, tol=1e-9)
check("on the cube carving, Kitaev-pattern terms commute with every loop operator; no nonzero covariant T-odd term does",
      kit_worst < 1e-12 and nonzero_on_cube > 0 and solvable_dim == 0,
      f"largest Kitaev-pattern commutator {kit_worst:.1e}; covariant T-odd terms nonzero on the cube {nonzero_on_cube}, of which loop-preserving {solvable_dim}")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
