#!/usr/bin/env python3
"""Breaking the momentum rule with an on-site metric stiffness in the swapped assignment.

Question (probe 15's open route (i), and its second referee's remark,
2026-09-29): in the swapped assignment (metric diagonal, exact scalar Gauss
law, kinetic terms from Gauss-law-compatible moves), a light-cone TT mode
needs a bounded metric susceptibility. An on-site metric stiffness m^2 |h|^2
gives one, at the price of breaking the momentum rule (linearised
diffeomorphisms). What happens to the modes? Pre-registered in the probe's
scratch file: PASS if the TT modes turn linear with no other gapless mode;
FAIL if partners (the former gauge directions) turn gapless too.

Harmonic comparators, specified (U = 1; the 2^3 integer box kernel of S as
moves; the landed lattice E-H symbol; m^2 on-site in the tensor norm):
  A  the on-site stiffness commutes with the scalar Gauss law (diagonal) but
     not with the momentum-rule strings: X_m(n + g) != X_m(n) for gauge
     patterns g (integer check on the 4^3 torus).
  B  variant (b), scalar law exact, momentum rule broken: the physical space
     is ker S(q), 5-dimensional (TT plus the 3 former gauge directions); E-H
     is positive semidefinite there, so the model is stable for every
     m^2 > 0; all five modes are gapless with omega ~ q (fitted exponents
     1.00 +- 0.02, axis, body and a generic direction), with speeds
     proportional to m (m^2 = 1, 4, 16). Against probe 15's
     variant (a) (both rules exact: 2 modes, omega ~ q^2), three partner
     modes appear, carrying helicity +-1 and 0 weight.
  C  variant (c), both rules soft (single-slot moves, tensor-normalised):
     stability needs m^2 above the largest conformal instability over the
     zone (about 11.97, sampled), and then every mode is gapped, omega -> m.
Prints one line per check, the N5 lines and TOTAL.
"""
import itertools
import numpy as np
import sympy as sp
from scipy.linalg import eigh

AUDIT_TIMEOUT_SEC = 900
PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


rng = np.random.default_rng(20260929)
E3 = np.eye(3, dtype=int); FACE = {(0, 1): 3, (1, 2): 4, (0, 2): 5}; FI = {v: k for k, v in FACE.items()}
Nmet = np.diag([1, 1, 1, .5, .5, .5])                                  # the tensor norm in q-coordinates


def offset(a):
    if a < 3:
        return np.zeros(3)
    i, j = FI[a]
    return (E3[i] + E3[j]) / 2


def S_row(x):
    x = np.array(x); d = {}
    def add(c, a, v): d[(tuple(c), a)] = d.get((tuple(c), a), 0) + v
    for j in range(3):
        for i in range(3):
            if i != j:
                add(x + E3[i], j, 1); add(x - E3[i], j, 1); add(x, j, -2)
    for (i, j), f in FACE.items():
        add(x, f, -1); add(x - E3[i], f, 1); add(x - E3[j], f, 1); add(x - E3[i] - E3[j], f, -1)
    return d


def G_row(x, j):
    x = np.array(x); d = {}
    def add(c, a, v): d[(tuple(c), a)] = d.get((tuple(c), a), 0) + v
    add(x + E3[j], j, 1); add(x, j, -1)
    for i in range(3):
        if i != j:
            f = FACE[tuple(sorted((i, j)))]; add(x, f, 1); add(x - E3[i], f, -1)
    return d


def Xr(q):                 # landed lattice E-H symbol (2026-09-24 note), midpoint convention, q-coordinates
    K = 2 * np.sin(q / 2); X = np.zeros((6, 6)); fc = {3: (0, 1), 4: (1, 2), 5: (0, 2)}
    for a in range(3):
        for b in range(3):
            if a != b:
                X[a, b] = -K[3 - a - b] ** 2
    for a in range(3):
        for f, (i, jj) in fc.items():
            if a not in (i, jj):
                X[a, f] = X[f, a] = K[i] * K[jj]
    for f, (i, jj) in fc.items():
        X[f, f] = K[3 - i - jj] ** 2 / 2
        for g, (kk, l) in fc.items():
            if g != f:
                sh = set((i, jj)) & set((kk, l)); X[f, g] = -K[(set((i, jj)) - sh).pop()] * K[(set((kk, l)) - sh).pop()] / 2
    return X


def S_sym(q):
    K = 2 * np.sin(q / 2); KK = K @ K
    return np.array([K[0] ** 2 - KK, K[1] ** 2 - KK, K[2] ** 2 - KK, K[0] * K[1], K[1] * K[2], K[0] * K[2]], complex)


# ---------------------------------------------------------------- A: the on-site stiffness breaks the momentum strings, not the Gauss law
L = 4
cells = list(itertools.product(range(L), repeat=3)); cidx = {c: i for i, c in enumerate(cells)}; nslot = 6 * len(cells)
def sl(c, a):
    return 6 * cidx[tuple(np.array(c).astype(int) % L)] + a
Nfull = np.kron(np.eye(len(cells)), Nmet)
gp = []
for c in cells:
    for j in range(3):
        v = np.zeros(nslot)
        for (cc, a), val in G_row(c, j).items():
            v[sl(cc, a)] += val
        gp.append(v)
changes = []
for g in gp[:30]:
    n = rng.integers(-3, 4, size=nslot).astype(float)
    changes.append(abs((n + g) @ Nfull @ (n + g) - n @ Nfull @ n))
okA = min(changes) > 0.1
check("A: the on-site metric stiffness m^2 |h|^2 is diagonal (it commutes with the scalar Gauss law) but changes under every sampled gauge shift, so it breaks the momentum-rule strings",
      okA, f"|X_m(n + g) - X_m(n)| over 30 gauge patterns and random integer n (m^2 = 1): min {min(changes):.2f}")

# ---------------------------------------------------------------- the 2^3 integer box kernel of S (the Gauss-law-compatible moves)
nb = 2
box = list(itertools.product(range(nb), repeat=3)); slots = [(c, a) for c in box for a in range(6)]; sidx = {s: i for i, s in enumerate(slots)}
rows = []
for y in itertools.product(range(-2, nb + 2), repeat=3):
    d = S_row(y); row = [0] * len(slots); t = False
    for k, v in d.items():
        if k in sidx:
            row[sidx[k]] += v; t = True
    if t and any(row):
        rows.append(row)
KS = []
for v in sp.Matrix(rows).nullspace():
    den = sp.ilcm(*[sp.fraction(z)[1] for z in v]); w = np.array([int(z * den) for z in v]); KS.append(w // np.gcd.reduce(np.abs(w[w != 0])))
KS = np.array(KS).T.astype(float)


def rhat(t, q):
    out = np.zeros(6, complex)
    for i, (c, a) in enumerate(slots):
        v = KS[i, t]
        if v:
            out[a] += v * np.exp(-1j * q @ (np.array(c, float) + offset(a)))
    return out


def gauge_projector(K):     # projector (tensor metric) onto sym(K (x) xi) inside q-coordinates
    cols = []
    for j in range(3):
        xi = np.zeros(3); xi[j] = 1; T = (np.outer(K, xi) + np.outer(xi, K)) / 2
        cols.append(np.array([T[0, 0], T[1, 1], T[2, 2], 2 * T[0, 1], 2 * T[1, 2], 2 * T[0, 2]]))
    return np.array(cols).T


# ---------------------------------------------------------------- B: variant (b): scalar law exact, momentum rule broken by m^2
def modes_b(q, m2):
    s = S_sym(q); B = np.linalg.svd(s[None, :])[2][1:].conj().T                  # 6 x 5 basis of ker S(q)
    kap = sum(np.outer(rhat(t, q), rhat(t, q).conj()) for t in range(KS.shape[1]))
    V = Xr(q) + m2 * Nmet
    Gi = np.linalg.inv(B.conj().T @ B)
    kred = Gi @ B.conj().T @ kap @ B @ Gi; Vred = B.conj().T @ V @ B
    w = np.sort(np.linalg.eigvals(kred @ Vred).real)
    xmin = np.linalg.eigvalsh(B.conj().T @ Xr(q) @ B).min() / (np.linalg.norm(2 * np.sin(q / 2)) ** 2)
    return np.sqrt(np.maximum(w, 0)), np.linalg.norm(2 * np.sin(q / 2)), xmin


okB = True; rowsB = []; xmins = []
for n in [np.array([0, 0, 1.]), np.array([1, 1, 1.]) / np.sqrt(3), np.array([0.3, -0.5, 0.81]) / np.linalg.norm([0.3, -0.5, 0.81])]:
    res = [modes_b(e * n, 1.0) for e in (0.2, 0.1, 0.05, 0.025)]
    Kn = np.array([r[1] for r in res]); om = np.array([r[0] for r in res]); xmins += [r[2] for r in res]
    fits = [np.polyfit(np.log(Kn), np.log(om[:, j]), 1)[0] for j in range(5)]
    okB &= len(fits) == 5 and all(abs(f - 1) < 0.02 for f in fits)
    rowsB.append(f"n = {np.round(n, 2)}: five exponents {np.round(fits, 3)}")
# the 3 extra modes live in the former gauge directions: the gauge 3-plane lies inside ker S(q) and carries helicity 1 and 0
q = 0.05 * np.array([0.3, -0.5, 0.81]) / np.linalg.norm([0.3, -0.5, 0.81]); Kq = 2 * np.sin(q / 2)
Pg = gauge_projector(Kq); in_kerS = np.abs(S_sym(q) @ Pg).max() < 1e-12 and np.linalg.matrix_rank(Pg) == 3
okB &= min(xmins) > -1e-9 and in_kerS
# a stronger stiffness speeds every mode up (omega ~ m K) and gaps none
nsc = np.array([0.3, -0.5, 0.81]) / np.linalg.norm([0.3, -0.5, 0.81]); scal = []
for m2 in (1.0, 4.0, 16.0):
    w_, K_, _ = modes_b(0.02 * nsc, m2); scal.append(w_ / K_ / np.sqrt(m2))
okB &= np.allclose(scal[0], scal[1], rtol=1e-3) and np.allclose(scal[0], scal[2], rtol=1e-3)
check("B: variant (b), scalar law exact and momentum rule broken by an on-site metric stiffness: E-H is positive semidefinite on ker S(q), so the model is stable for every m^2 > 0; all five modes of ker S(q) (TT plus the three former gauge directions, which carry helicity +-1 and 0) are gapless with omega ~ q and speeds proportional to m (a stronger stiffness gaps none); against probe 15's two modes with omega ~ q^2, three partner modes appear",
      okB, "; ".join(rowsB) + f"; min eigenvalue of E-H on ker S / K^2: {min(xmins):.1e}; gauge directions inside ker S (rank 3): {in_kerS}; omega/(m K) at m^2 = 1, 4, 16 (generic direction): {[list(np.round(x, 3)) for x in scal]}")

# ---------------------------------------------------------------- C: variant (c): both rules soft
worst = 0.0
for _ in range(3000):
    qq = rng.uniform(-np.pi, np.pi, 3); worst = min(worst, eigh(Xr(qq), Nmet, eigvals_only=True).min())
m2c = 13.0; gaps = []
for n in [np.array([0, 0, 1.]), np.array([1, 1, 1.]) / np.sqrt(3)]:
    for e in (0.2, 0.05, 0.01):
        gaps.append(np.sqrt(eigh(Xr(e * n) + m2c * Nmet, Nmet, eigvals_only=True).min()))
stable_zone = min(eigh(Xr(rng.uniform(-np.pi, np.pi, 3)) + m2c * Nmet, Nmet, eigvals_only=True).min() for _ in range(3000)) > 0
okC = worst < -11 and stable_zone and abs(gaps[-1] - np.sqrt(m2c)) < 1e-3
check("C: variant (c), both rules soft (single-slot moves, tensor-normalised kinetic term): stability over the zone needs m^2 above the largest conformal instability of E-H (about 11.97, sampled); at m^2 = 13 every mode is gapped, omega -> m as q -> 0",
      okC, f"most negative tensor-metric eigenvalue of E-H over 3000 zone momenta: {worst:.3f}; stable at m^2 = 13: {stable_zone}; lowest omega at |q| = 0.2, 0.05, 0.01 (axis, body): {np.round(gaps, 4)}")

print("N5 resolution 1: an on-site metric stiffness gives the swapped assignment a bounded chi_h and linear TT modes, but only by breaking the momentum rule.")
print("N5 resolution 2: with the scalar law exact, the three former gauge directions (helicity +-1, 0) become gapless linear partners: five linear modes instead of two soft ones. Pre-registered outcome: FAIL.")
print("N5 resolution 3: with both rules soft, stability needs m^2 above the conformal instability and then every mode is gapped.")
print("per_element: the on-site stiffness under each sampled gauge pattern; the box kernel's integer moves.")
print("per_site: the Gauss law and the gauge patterns at every site of the 4^3 torus (30 sampled for A).")
print("per_mode: five modes of ker S(q) in three directions at four momenta; the gapped spectrum at three momenta in two directions.")
print("per_block: the 2^3 integer box kernel of S as the move set.")
print("lattice_wide: checked and not executed - any quantum state beyond the harmonic comparators, other symmetry-breaking stiffnesses, anisotropic partner speeds' origin, a phase.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
