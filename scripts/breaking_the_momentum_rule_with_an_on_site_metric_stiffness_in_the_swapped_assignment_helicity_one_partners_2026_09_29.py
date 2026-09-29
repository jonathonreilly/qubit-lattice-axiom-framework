#!/usr/bin/env python3
"""Breaking the momentum rule with an on-site metric stiffness in the swapped assignment: linear TT modes, with helicity-1 partners that move with them.

Question (probe 15's open route (i), and its second referee's remark,
2026-09-29): in the swapped assignment (metric stored, exact scalar Gauss
law, kinetic terms from Gauss-law-compatible moves), a light-cone TT mode
needs a bounded metric susceptibility. An on-site metric stiffness gives
one, at the price of breaking the momentum rule. Pre-registered in the
probe's scratch file: PASS if the TT modes turn linear with no other gapless
mode; FAIL if partners (the former gauge directions) turn gapless too.
Revised after the first referees: the premise S >= 1 (for a qubit, (S^z)^2
is constant and the stiffness is trivial), the isotropic analysis, the
Fierz-Pauli stiffness, and the exact stability threshold.

Harmonic comparators (specified): the landed lattice E-H symbol; kinetic
terms from the 2^3 integer box kernel of S (U = 1; a basis-dependent,
non-covariant Gram sum), or from isotropic families (alpha: gauge patterns
sym(K x xi); beta: symmetric curls sym(K cross A)); on-site stiffness
m^2 |h|^2 or Fierz-Pauli m^2 (|h|^2 - (tr h)^2), both in the tensor norm.
  A  the |h|^2 stiffness commutes with the scalar Gauss law and breaks the
     momentum strings (spin S >= 1; for S = 1/2 it is a constant).
  B  box-kernel kinetic form, scalar law exact: E-H is positive semidefinite
     on ker S(q), so the comparator is stable for every m^2 > 0; all five
     modes are gapless with omega ~ q (fitted exponents 1.00 +- 0.02); the
     q -> 0 slopes scale as m (m^2 = 1, 4, 16). The five modes mix
     helicities because the box-kernel form is not covariant.
  C  isotropic kinetic forms: the modes carry clean helicities and their
     q -> 0 speeds obey c1^2 = c0^2/2 + c2^2/4, so the helicity +-1 partners
     move at no less than half the TT speed whenever the TT modes move;
     without gauge-family moves (alpha = 0) the helicity-0 partner is
     frozen; a Fierz-Pauli stiffness freezes the helicity-0 partner for any
     kinetic form tested.
  D  both rules soft (single-slot moves, tensor-normalised): exact zone
     stability needs m^2 > 12 = max |K|^2 (the conformal eigenvalue is
     -|K|^2 on the transverse trace); then every mode is gapped, the
     smallest gap sqrt(m^2 - 12) at the zone corner, omega -> m as q -> 0.
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
spin_half_const = all(abs(v * v - 0.25) < 1e-15 for v in (0.5, -0.5))
okA &= spin_half_const
check("A: the on-site metric stiffness m^2 |h|^2 is diagonal (it commutes with the scalar Gauss law) but changes under every sampled gauge shift, so it breaks the momentum-rule strings (slots of spin S >= 1; for S = 1/2, (S^z)^2 = 1/4 and the stiffness is a constant)",
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
check("B: box-kernel kinetic form, scalar law exact, momentum rule broken by m^2 |h|^2: E-H is positive semidefinite on ker S(q), so the comparator is stable for every m^2 > 0; all five modes of ker S(q) (spanned by the TT and the former gauge directions) are gapless with omega ~ q, and the q -> 0 slopes scale as m (a stronger stiffness gaps none); the modes mix helicities because this form is not covariant",
      okB, "; ".join(rowsB) + f"; min eigenvalue of E-H on ker S / K^2: {min(xmins):.1e}; gauge directions inside ker S (rank 3): {in_kerS}; omega/(m K) at m^2 = 1, 4, 16 (generic direction): {[list(np.round(x, 3)) for x in scal]}")

# ---------------------------------------------------------------- C: isotropic kinetic forms: clean helicities, c1^2 = c0^2/2 + c2^2/4
def qc(T):
    return np.array([T[0, 0], T[1, 1], T[2, 2], 2 * T[0, 1], 2 * T[1, 2], 2 * T[0, 2]])


def tens(v):
    return np.array([[v[0], v[3] / 2, v[5] / 2], [v[3] / 2, v[1], v[4] / 2], [v[5] / 2, v[4] / 2, v[2]]])


EPS = np.zeros((3, 3, 3))
for (i_, j_, k_), sg in [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)]:
    EPS[i_, j_, k_] = sg
symbasis = []
for i_ in range(3):
    for j_ in range(i_, 3):
        Mb = np.zeros((3, 3)); Mb[i_, j_] = Mb[j_, i_] = 1; symbasis.append(Mb / np.linalg.norm(Mb))


def kappa_iso(q, alpha, beta):
    K = 2 * np.sin(q / 2); kap = np.zeros((6, 6), complex)
    for j_ in range(3):
        xi = np.zeros(3); xi[j_] = 1; g = qc((np.outer(K, xi) + np.outer(xi, K)) / 2); kap += alpha * np.outer(g, g.conj())
    for A_ in symbasis:
        Cx = np.einsum("ikl,k,lj->ij", EPS, K, A_); v = qc((Cx + Cx.T) / 2); kap += beta * np.outer(v, v.conj())
    return kap


def helicity(hq, K):
    h = tens(hq); kh = K / np.linalg.norm(K); a_ = np.array([1., 0, 0]) if abs(kh[0]) < 0.9 else np.array([0, 1., 0])
    u = np.cross(kh, a_); u /= np.linalg.norm(u); v = np.cross(kh, u); ep = (u + 1j * v) / np.sqrt(2); em = (u - 1j * v) / np.sqrt(2)
    bas = {2: [np.outer(ep, ep), np.outer(em, em)], 1: [(np.outer(ep, kh) + np.outer(kh, ep)) / np.sqrt(2), (np.outer(em, kh) + np.outer(kh, em)) / np.sqrt(2)],
           0: [np.outer(kh, kh), (np.outer(u, u) + np.outer(v, v)) / np.sqrt(2)]}
    w = {m_: sum(abs(np.sum(np.conj(T) * h)) ** 2 for T in Ts) for m_, Ts in bas.items()}; t = sum(w.values())
    return max(w, key=w.get), max(w.values()) / t


def modes_iso(q, alpha, beta, m2, fp):
    s_ = S_sym(q); B = np.linalg.svd(s_[None, :])[2][1:].conj().T
    trq = np.array([1, 1, 1, 0, 0, 0.])
    V = Xr(q) + m2 * (Nmet - (np.outer(trq, trq) if fp else 0))
    Gi = np.linalg.inv(B.conj().T @ B); kred = Gi @ B.conj().T @ kappa_iso(q, alpha, beta) @ B @ Gi; Vred = B.conj().T @ V @ B
    w2, vec = np.linalg.eig(Vred @ kred); o = np.argsort(w2.real); K = 2 * np.sin(q / 2)
    speeds = np.sqrt(np.maximum(w2.real[o], 0)) / np.linalg.norm(K)
    labels = []
    for j_ in o:
        hv = B @ (kred @ vec[:, j_])
        labels.append(helicity(hv, K) if np.linalg.norm(hv) > 1e-12 else (None, 1.0))
    return speeds, labels


okC = True; rowsC = []
nC = np.array([0.3, -0.5, 0.81]) / np.linalg.norm([0.3, -0.5, 0.81])
for (al, be, fp) in [(1, 1, False), (0, 1, False), (1, 0, False), (2, 0.5, False), (1, 1, True), (2, 0.5, True)]:
    sp_, lab = modes_iso(1e-3 * nC, al, be, 1.0, fp)
    c = {0: [], 1: [], 2: []}
    for spd, (hl, pur) in zip(sp_, lab):
        if hl is not None:
            okC &= pur > 0.999; c[hl].append(spd)
        else:
            c.setdefault("frozen", []).append(spd)
    c0 = c[0][0] if c[0] else 0.0; c1 = c[1][0] if c[1] else 0.0; c2 = c[2][0] if c[2] else 0.0
    if not fp:
        okC &= abs(c1 ** 2 - (c0 ** 2 / 2 + c2 ** 2 / 4)) < 1e-4 and (be == 0 or c1 >= c2 / 2 - 1e-6)
        if al == 0:
            okC &= c0 == 0.0
    else:
        okC &= c0 == 0.0 and c1 > 0 and c2 > 0
    rowsC.append(f"alpha={al}, beta={be}, {'Fierz-Pauli' if fp else '|h|^2'}: speeds/m (c0, c1, c2) = ({c0:.3f}, {c1:.3f}, {c2:.3f})")
check("C: isotropic kinetic forms (gauge-pattern family alpha, symmetric-curl family beta): the modes carry clean helicities; with |h|^2 the q -> 0 speeds obey c1^2 = c0^2/2 + c2^2/4, so the helicity +-1 partners move at no less than half the TT speed whenever the TT modes move; alpha = 0 freezes the helicity-0 partner; a Fierz-Pauli stiffness m^2 (|h|^2 - (tr h)^2) freezes the helicity-0 partner and keeps the helicity +-1 partners",
      okC, "; ".join(rowsC))

# ---------------------------------------------------------------- D: both rules soft: exact threshold m^2 > 12, corner gap
Kc = np.array([np.pi, np.pi, np.pi]); Kcorner2 = float((2 * np.sin(Kc / 2)) @ (2 * np.sin(Kc / 2)))
conf_corner = eigh(Xr(Kc), Nmet, eigvals_only=True).min()
m2c = 13.0
gap_corner = np.sqrt(eigh(Xr(Kc) + m2c * Nmet, Nmet, eigvals_only=True).min())
gaps = [np.sqrt(eigh(Xr(e * n) + m2c * Nmet, Nmet, eigvals_only=True).min()) for n in [np.array([0, 0, 1.]), np.array([1, 1, 1.]) / np.sqrt(3)] for e in (0.2, 0.05, 0.01)]
zone_min = min(eigh(Xr(rng.uniform(-np.pi, np.pi, 3)) + m2c * Nmet, Nmet, eigvals_only=True).min() for _ in range(2000))
okD = abs(Kcorner2 - 12) < 1e-12 and abs(conf_corner + 12) < 1e-9 and abs(gap_corner - np.sqrt(m2c - 12)) < 1e-9 and zone_min >= m2c - 12 - 1e-9 and abs(gaps[-1] - np.sqrt(m2c)) < 1e-3
check("D: both rules soft (single-slot moves, tensor-normalised kinetic term): the conformal eigenvalue is -|K|^2, largest at the zone corner where |K|^2 = 12, so exact zone stability needs m^2 > 12; then every mode is gapped, the smallest gap sqrt(m^2 - 12) at the corner, and omega -> m as q -> 0",
      okD, f"|K|^2 at (pi, pi, pi) = {Kcorner2:.1f}; conformal eigenvalue there {conf_corner:.3f}; at m^2 = 13 the corner gap {gap_corner:.4f} (= sqrt(m^2 - 12)) and the zone minimum of omega^2 over 2000 momenta {zone_min:.4f}; lowest omega at |q| = 0.2, 0.05, 0.01 (axis, body): {np.round(gaps, 4)}")

print("N5 resolution 1: an on-site metric stiffness (spin S >= 1) gives the swapped assignment a bounded chi_h and linear TT modes, but only by breaking the momentum rule.")
print("N5 resolution 2: the helicity +-1 partners then move too: in isotropic comparators c1^2 = c0^2/2 + c2^2/4, so they are gapless whenever the TT modes move; the helicity-0 partner is linear or frozen (frozen with a Fierz-Pauli stiffness). Pre-registered outcome: FAIL.")
print("N5 resolution 3: with both rules soft, exact stability needs m^2 > 12 and then every mode is gapped.")
print("per_element: the stiffness under each sampled gauge pattern; the box kernel's integer moves; the isotropic families' basis patterns.")
print("per_site: the Gauss law and 30 sampled gauge patterns on the 4^3 torus.")
print("per_mode: five modes of ker S(q) for the box-kernel form (three directions, four momenta) and six isotropic forms (one direction); the gapped spectrum and the zone corner.")
print("per_block: the 2^3 integer box kernel of S as moves; isotropic move families.")
print("lattice_wide: resolves the exact zone threshold m^2 > 12 (the conformal eigenvalue -|K|^2 is maximal in magnitude at the corner) and the gap sqrt(m^2 - 12); checked and not executed - states beyond harmonic comparators, derivative stiffnesses.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
