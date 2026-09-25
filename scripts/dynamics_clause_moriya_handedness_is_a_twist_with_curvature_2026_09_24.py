#!/usr/bin/env python3
"""The Moriya coupling's handedness: a twist that cannot be gauged away in three
dimensions and that shows in record statistics.

Supplied and not adopted: the fully soldered dynamics clause of the supplied companion construction,
bond term J s_x.s_y + K (e.s_x)(e.s_y) + D e.(s_x x s_y) on the bond (x, y=x+e).
The axioms name proper rotations only; the improper inversion maps D to -D.

Checks:

A. Twisted bond: J s1.s2 + D e.(s1 x s2) = V (A (s1.s2 - (e.s1)(e.s2)) +
   J (e.s1)(e.s2)) V^dag with A = sqrt(J^2 + D^2) and V = exp(-i phi e.s2 / 2),
   tan phi = D/J, for e = x, y, z: an XXZ bond in a frame turned about the bond
   axis by phi (exact, symbolic).
B. Along one line the twist is a gauge: a periodic J-D ring of N sites along e
   has the spectrum of the XXZ ring whose closing bond carries the total twist
   N phi (N = 5, 6, 7).
C. Where bond directions meet it is not: the frame turns R_x(phi), R_y(phi)
   about two different axes have nonzero holonomy around a plaquette for
   0 < phi < pi; twisted and untwisted bonds have equal spectra on a straight
   open chain but different spectra on a bent chain and on the cube, so there
   no unitary maps one to the other.
D. Records: the two-site ground state (J > 0) has record correlations on
   antipodal menus with antisymmetric part E(a,b) - E(b,a) = c (a x b).e,
   c = -2 sin(phi), odd in D and zero at D = 0; the CHSH maximum stays
   2 sqrt 2.
E. Handed ground states: on the open 2x2x2 cube with J-K-D coupling, the mean
   bond vector chirality <f.(s_x x s_{x+f})> of the ground state is odd in D,
   and the inversion of the cube maps H(D) to H(-D) exactly.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys
from functools import reduce

AUDIT_INPUT_PATHS = ('docs/DYNAMICS_CLAUSE_MORIYA_HANDEDNESS_IS_A_TWIST_WITH_CURVATURE_GAUGED_ALONG_A_LINE_NOT_IN_THREE_DIMENSIONS_AND_SEEN_IN_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
AUDIT_TIMEOUT_SEC = 300

import numpy as np
import sympy as sp

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


# -------------------------------------------------------------- A: twisted bond
print("A. a Moriya-twisted bond is a turned XXZ bond")
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
Ssym = [sx, sy, sz]
I2s = sp.eye(2)
J, D = sp.symbols("J D", positive=True)
A = sp.sqrt(J ** 2 + D ** 2)
phi = sp.atan2(D, J)
kp = sp.kronecker_product
ok_all = True
for ax in range(3):
    e = [0, 0, 0]
    e[ax] = 1
    others = [a for a in range(3) if a != ax]
    b, c = others
    heis = sum((kp(Ssym[a], Ssym[a]) for a in range(3)), sp.zeros(4, 4))
    # e.(s1 x s2) with e along ax: s1_b s2_c - s1_c s2_b for (ax, b, c) cyclic
    cyc = (ax, (ax + 1) % 3, (ax + 2) % 3)
    moriya = kp(Ssym[cyc[1]], Ssym[cyc[2]]) - kp(Ssym[cyc[2]], Ssym[cyc[1]])
    lhs = J * heis + D * moriya
    xxz = A * (kp(Ssym[b], Ssym[b]) + kp(Ssym[c], Ssym[c])) + J * kp(Ssym[ax], Ssym[ax])
    V2 = sp.cos(phi / 2) * sp.eye(2) - sp.I * sp.sin(phi / 2) * Ssym[ax]
    V = kp(I2s, V2)
    rhs = V * xxz * V.H
    diff = (lhs - rhs).applyfunc(lambda z: sp.simplify(sp.expand_trig(sp.expand(z))))
    ok_all &= diff == sp.zeros(4, 4)
check("J s1.s2 + D e.(s1 x s2) = V (A (in-plane) + J (along e)) V^dag, V = exp(-i phi e.s2/2), tan phi = D/J",
      ok_all, "exact for bonds along x, y and z")

# numerics helpers
S = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1.0])]
I2 = np.eye(2, dtype=complex)


def op(n, placed):
    return reduce(np.kron, [placed.get(k, I2) for k in range(n)])


def rot(ax, ang):
    c, s = np.cos(ang), np.sin(ang)
    R = np.eye(3)
    i, j = (ax + 1) % 3, (ax + 2) % 3
    R[i, i], R[i, j], R[j, i], R[j, j] = c, -s, s, c
    return R


# ----------------------------------------------------------- B: a line is a gauge
print("B. along one line the twist is a gauge")
Jn, Dn = 1.0, 0.7
ph = np.arctan2(Dn, Jn)
An = np.hypot(Jn, Dn)
worst = 0.0
for N in (5, 6, 7):
    ax = 2
    H_jd = np.zeros((2 ** N, 2 ** N), dtype=complex)
    for i in range(N):
        j = (i + 1) % N
        H_jd += Jn * sum(op(N, {i: S[a], j: S[a]}) for a in range(3))
        H_jd += Dn * (op(N, {i: S[0], j: S[1]}) - op(N, {i: S[1], j: S[0]}))
    # XXZ ring with the closing bond turned by N*phi about z
    H_x = np.zeros_like(H_jd)
    for i in range(N):
        j = (i + 1) % N
        if j != 0:
            H_x += An * (op(N, {i: S[0], j: S[0]}) + op(N, {i: S[1], j: S[1]})) + Jn * op(N, {i: S[2], j: S[2]})
        else:
            th = N * ph
            Vc = np.cos(th / 2) * I2 - 1j * np.sin(th / 2) * S[2]
            xxz = An * (np.kron(S[0], S[0]) + np.kron(S[1], S[1])) + Jn * np.kron(S[2], S[2])
            Vb = np.kron(I2, Vc)
            b = Vb @ xxz @ Vb.conj().T
            # place the two-site operator b on sites (N-1, 0)
            full = np.zeros_like(H_jd)
            for a1 in range(2):
                for a2 in range(2):
                    for b1 in range(2):
                        for b2 in range(2):
                            val = b[2 * a1 + a2, 2 * b1 + b2]
                            if abs(val) < 1e-15:
                                continue
                            E1 = np.zeros((2, 2), dtype=complex)
                            E1[a1, b1] = 1
                            E2 = np.zeros((2, 2), dtype=complex)
                            E2[a2, b2] = 1
                            full += val * op(N, {N - 1: E1, 0: E2})
            H_x += full
    ev1 = np.linalg.eigvalsh(H_jd)
    ev2 = np.linalg.eigvalsh(H_x)
    worst = max(worst, np.abs(ev1 - ev2).max())
check("a J-D ring along e has the spectrum of the XXZ ring with total twist N phi on the closing bond",
      worst < 1e-10, f"N = 5, 6, 7; max eigenvalue difference {worst:.1e}")

# --------------------------------------------------------- C: 3D holonomy
print("C. in three dimensions the twists have curvature")
angs = []
ok = True
for p in np.linspace(0.05, np.pi - 0.05, 60):
    Hol = rot(0, p) @ rot(1, p) @ rot(0, -p) @ rot(1, -p)
    ang = np.arccos(np.clip((np.trace(Hol) - 1) / 2, -1, 1))
    angs.append(ang)
    ok &= ang > 1e-6
hol0 = rot(0, 0) @ rot(1, 0) @ rot(0, 0) @ rot(1, 0)
hol_pi = rot(0, np.pi) @ rot(1, np.pi) @ rot(0, -np.pi) @ rot(1, -np.pi)
check("plaquette holonomy R_x(phi) R_y(phi) R_x(-phi) R_y(-phi) is a nonzero rotation for 0 < phi < pi",
      ok and np.allclose(hol0, np.eye(3)) and np.allclose(hol_pi, np.eye(3)),
      f"smallest angle on the grid {min(angs):.4f}; at phi = 0.61 (D/J = 0.7): "
      f"{np.degrees(np.arccos(np.clip((np.trace(rot(0, ph) @ rot(1, ph) @ rot(0, -ph) @ rot(1, -ph)) - 1) / 2, -1, 1))):.2f} deg")

# spectra: twisted versus untwisted bonds, on a tree (open chain) and on the cube
def bond_ops(n, i, j, M):
    return sum(M[a, b] * op(n, {i: S[a], j: S[b]}) for a in range(3) for b in range(3) if M[a, b] != 0)


def cmat(f):
    return np.array([[0, f[2], -f[1]], [-f[2], 0, f[0]], [f[1], -f[0], 0]], dtype=float)


def twisted(f):
    return Jn * np.eye(3) + Dn * cmat(f)


def untwisted(f):
    return An * (np.eye(3) - np.outer(f, f)) + Jn * np.outer(f, f)


def chain_gap(dirs):
    ch = [(k, k + 1, np.array(d, dtype=float)) for k, d in enumerate(dirs)]
    n = len(dirs) + 1
    Ht = sum(bond_ops(n, i, j, twisted(f)) for i, j, f in ch)
    Hu = sum(bond_ops(n, i, j, untwisted(f)) for i, j, f in ch)
    return np.abs(np.linalg.eigvalsh(Ht) - np.linalg.eigvalsh(Hu)).max()


straight_gap = chain_gap([(0, 0, 1)] * 4)
bent_gap = chain_gap([(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 0, 0)])
V8c = list(itertools.product((0, 1), repeat=3))
ixc = {v: i for i, v in enumerate(V8c)}
cube_bonds = []
for v in V8c:
    for a in range(3):
        if v[a] == 0:
            w = list(v)
            w[a] = 1
            f = np.zeros(3)
            f[a] = 1
            cube_bonds.append((ixc[v], ixc[tuple(w)], f))
Hct = sum(bond_ops(8, i, j, twisted(f)) for i, j, f in cube_bonds)
Hcu = sum(bond_ops(8, i, j, untwisted(f)) for i, j, f in cube_bonds)
cube_gap = np.abs(np.linalg.eigvalsh(Hct) - np.linalg.eigvalsh(Hcu)).max()
check("twisted and untwisted spectra agree on a straight open chain and differ on a bent chain and on the cube",
      straight_gap < 1e-10 and bent_gap > 1e-2 and cube_gap > 1e-2,
      f"straight 5-site chain: {straight_gap:.1e}; bent chain x,y,z,x: {bent_gap:.4f}; cube: {cube_gap:.4f}")

# ------------------------------------------------------------- D: records
print("D. handed record statistics of the twisted pair")
rng = np.random.default_rng(6)


def pair_ground(Jv, Dv, ax=2):
    cyc = (ax, (ax + 1) % 3, (ax + 2) % 3)
    H = Jv * sum(np.kron(S[a], S[a]) for a in range(3)) + Dv * (np.kron(S[cyc[1]], S[cyc[2]]) - np.kron(S[cyc[2]], S[cyc[1]]))
    ev, V = np.linalg.eigh(H)
    return V[:, 0]


def E(psi, a, b):
    return np.real(psi.conj() @ np.kron(sum(a[k] * S[k] for k in range(3)), sum(b[k] * S[k] for k in range(3))) @ psi)


ez = np.array([0.0, 0.0, 1.0])
res = {}
for Dv in (0.7, -0.7, 0.0):
    psi = pair_ground(1.0, Dv)
    worst, cs = 0.0, []
    for _ in range(100):
        a, b = rng.normal(size=3), rng.normal(size=3)
        a, b = a / np.linalg.norm(a), b / np.linalg.norm(b)
        anti = E(psi, a, b) - E(psi, b, a)
        tri = np.cross(a, b) @ ez
        if abs(tri) > 0.2:
            cs.append(anti / tri)
    res[Dv] = (np.mean(cs), np.std(cs))
c_plus, c_minus, c_zero = res[0.7][0], res[-0.7][0], res[0.0][0]
phv = np.arctan2(0.7, 1.0)
consistent = max(v[1] for v in res.values()) < 1e-10
T = lambda psi: np.array([[E(psi, np.eye(3)[i], np.eye(3)[j]) for j in range(3)] for i in range(3)])
chsh = {Dv: 2 * np.sqrt(sum(sorted(np.linalg.eigvalsh(T(pair_ground(1.0, Dv)).T @ T(pair_ground(1.0, Dv))))[1:]))
        for Dv in (0.7, -0.7, 0.0)}
check("E(a,b) - E(b,a) = c (a x b).e with c odd in D and zero at D = 0",
      consistent and abs(c_plus + c_minus) < 1e-10 and abs(c_zero) < 1e-10 and abs(c_plus) > 0.1
      and abs(c_plus + 2 * np.sin(phv)) < 1e-10,
      f"c = {c_plus:.6f} (D = +0.7), {c_minus:.6f} (D = -0.7), {c_zero:.1e} (D = 0); |c| = 2 sin(phi)")
check("the CHSH maximum of the twisted pair stays 2 sqrt 2", all(abs(v - 2 * np.sqrt(2)) < 1e-10 for v in chsh.values()),
      ", ".join(f"{v:.6f}" for v in chsh.values()))

# ------------------------------------------------------------- E: the cube
print("E. handed ground states on the 2x2x2 cube")
V8 = list(itertools.product((0, 1), repeat=3))
ix = {v: i for i, v in enumerate(V8)}
bonds = []
for v in V8:
    for a in range(3):
        if v[a] == 0:
            w = list(v)
            w[a] = 1
            f = np.zeros(3)
            f[a] = 1
            bonds.append((ix[v], ix[tuple(w)], f))


def cross_mat(f):
    return np.array([[0, f[2], -f[1]], [-f[2], 0, f[0]], [f[1], -f[0], 0]], dtype=float)


def cube_H(Jv, Kv, Dv):
    H = np.zeros((256, 256), dtype=complex)
    for (i, j, f) in bonds:
        M = Jv * np.eye(3) + Kv * np.outer(f, f) + Dv * cross_mat(f)
        for a in range(3):
            for b in range(3):
                if M[a, b] != 0:
                    H += M[a, b] * op(8, {i: S[a], j: S[b]})
    return H


def chirality(psi):
    tot = 0.0
    for (i, j, f) in bonds:
        cyc = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
        O = np.zeros((256, 256), dtype=complex)
        for (p, q, r) in cyc:
            # f.(s_i x s_j) = sum_p f_p (s_i^q s_j^r - s_i^r s_j^q)
            if f[p] != 0:
                O += f[p] * (op(8, {i: S[q], j: S[r]}) - op(8, {i: S[r], j: S[q]}))
        tot += np.real(psi.conj() @ O @ psi)
    return tot / len(bonds)


chis = {}
for Dv in (0.5, -0.5, 0.0):
    ev, V = np.linalg.eigh(cube_H(1.0, 0.3, Dv))
    gap = ev[1] - ev[0]
    chis[Dv] = (chirality(V[:, 0]), gap)
# inversion of the cube: v -> (1,1,1) - v, spins axial (unchanged)
perm = [ix[tuple(1 - np.array(v))] for v in V8]
P = np.zeros((256, 256))
for s in range(256):
    bits = [(s >> (7 - k)) & 1 for k in range(8)]
    nb = [0] * 8
    for k in range(8):
        nb[perm[k]] = bits[k]
    P[sum(nb[k] << (7 - k) for k in range(8)), s] = 1
inv_ok = np.abs(P @ cube_H(1.0, 0.3, 0.5) @ P.T - cube_H(1.0, 0.3, -0.5)).max() < 1e-12
check("mean bond vector chirality of the ground state is odd in D; inversion maps H(D) to H(-D)",
      inv_ok and all(v[1] > 1e-3 for v in chis.values()) and abs(chis[0.5][0] + chis[-0.5][0]) < 1e-9 and abs(chis[0.5][0]) > 1e-3 and abs(chis[0.0][0]) < 1e-9,
      f"chirality {chis[0.5][0]:.6f} (D = 0.5), {chis[-0.5][0]:.6f} (D = -0.5), {chis[0.0][0]:.1e} (D = 0); "
      f"gaps {chis[0.5][1]:.4f}, {chis[-0.5][1]:.4f}")

print('per_element: Bond twist matrices and the signed pair correlator are tested.')
print('per_site: Local spin rotations and their finite compatibility constraints are tested.')
print('per_mode: checked and not executed — no dispersion or continuum parity theorem is claimed.')
print('per_block: Line, plaquette, pair and finite cube comparisons are tested.')
print('lattice_wide: checked and not executed — finite spectra do not certify all three-dimensional models.')

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
