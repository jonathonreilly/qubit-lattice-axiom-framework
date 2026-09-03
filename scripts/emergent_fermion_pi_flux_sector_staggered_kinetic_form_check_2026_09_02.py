#!/usr/bin/env python3
"""The staggered kinetic form as the pi-flux sector of the emergent fermion.

Self-contained finite-cluster runner. The coarse lattice is 2Z^3 -- the
sublattice carrying one fermionic mode per coarse vertex in the
Bravyi-Kitaev superfast encoding written on it -- and the object under test
is the Kawamoto-Smit (KS) link sign field
    eta_1 = 1,  eta_2(x) = (-1)^{x_1},  eta_3(x) = (-1)^{x_1+x_2}
of the landed staggered kinetic-form clause, read on that coarse lattice.

  A  KINETIC FORM.  With one 2x2x2 cell of coarse sites as the unit cell the
     KS hopping has Bloch Hamiltonian
        H(q) = sum_a [ (1 + cos q_a) Xi_a + sin q_a Gamma_a ],
        Gamma = (Y1, Z1 Y2, Z1 Z2 Y3),   Xi = (X1, Z1 X2, Z1 Z2 X3),
     six anticommuting hermitian involutions -- a Cl(6) set -- so that
     H(q)^2 = (6 + 2 sum_a cos q_a) I and tr H(q) = 0.  Exact torus spectra.
  B  SPIN AND TASTE.  The exact intertwiner U with
        U Gamma_a U^dag = sigma_a (x) T,   U Xi_a U^dag = I (x) B_a,
     T = diag(1,1,-1,-1), B = (XX, XY, XZ), built by Clifford averaging so
     its entries lie in Z[i]; unique up to a phase; the taste-mixing term is
     a spin singlet.
  C  PI-FLUX CLASS.  Every plaquette holonomy of the KS signs is -1, no site
     gauge carries the plain signs to them, and the sign is a function of the
     fine coordinates mod 4, not of the fine-mod-2 role pattern.
  D  CUBIC GROUP.  All 24 proper rotations lift to signed permutations
     preserving H; the lift is a genuine representation of O; on the eight
     zero modes it is 2 A1 + 2 T1 and factorises into individually projective
     spin and taste factors.
  E  CHIRALITY.  epsilon = Z1 Z2 Z3 is the chirality grading and maps to
     I (x) (+- T B1 B2 B3), not to the pseudoscalar I (x) T.
  F  FLUX SECTOR.  Transport of one encoded excitation around a coarse face
     equals the face stabilizer S_f exactly, Z4 phase included; the all-(-1)
     face sector exists exactly when every F2 relation among the S_f has even
     support; in that sector the encoded hopping is in the KS local gauge
     class, with an explicit witness and the same one-particle spectrum.
  G  MANY-BODY CROSS-CHECK.  Dense check on the open 2x2x2 coarse cube.

Groups A-C, E and F are exact: Z[i] and integer matrix arithmetic, sympy
symbolic identities, F2/Z4 symplectic bit arithmetic and exhaustive search.
The tagged [numerical] items are floating-point cross-checks of exact
statements already established, at the stated tolerance.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import itertools
import sys
from collections import Counter, deque

import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 300

PASS = 0
FAIL = 0


def check(label, cond):
    """Record and print one check."""
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + label)


# ========================================================== KS phases, lattice

EX = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
DIRS = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]


def eta_ks(v, a):
    """KS link sign of the coarse bond (v, v + e_a); axes 0,1,2 = 1,2,3."""
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


def va(a, b):
    return tuple(a[i] + b[i] for i in range(3))


def wrap(v, dims):
    return tuple(v[i] % dims[i] for i in range(3))


# ================================================== one-cell 8-dimensional algebra

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.diag([1, -1]).astype(complex)


def kr(*ms):
    o = np.array([[1.0 + 0j]])
    for m in ms:
        o = np.kron(o, m)
    return o


XI = [kr(SX, I2, I2), kr(SZ, SX, I2), kr(SZ, SZ, SX)]
GAM = [kr(SY, I2, I2), kr(SZ, SY, I2), kr(SZ, SZ, SY)]
SIX = GAM + XI
EPS8 = kr(SZ, SZ, SZ)
TT = np.diag([1, 1, -1, -1]).astype(complex)
BB = [kr(SX, SX), kr(SX, SY), kr(SX, SZ)]
SIG = [SX, SY, SZ]


def bloch_numeric(q):
    """8x8 Bloch block built from the KS hopping rules, no closed form used."""
    H = np.zeros((8, 8), dtype=complex)
    for s in range(8):
        sv = [(s >> (2 - a)) & 1 for a in range(3)]
        for a in range(3):
            e = eta_ks(sv, a)
            bit = 1 << (2 - a)
            if sv[a] == 0:
                t = s | bit
                H[t, s] += e
                H[s, t] += e
            else:
                t = s & ~bit
                H[t, s] += e * np.exp(-1j * q[a])
                H[s, t] += e * np.exp(1j * q[a])
    return H


def bloch_closed(q):
    return sum((1 + np.cos(q[a])) * XI[a] + np.sin(q[a]) * GAM[a] for a in range(3))


# ============================================================== group A: Cl(6)

RNG = np.random.default_rng(20260902)

is_clifford_set = (
    all(np.array_equal(A @ A, np.eye(8, dtype=complex)) for A in SIX)
    and all(np.array_equal(A, A.conj().T) for A in SIX)
    and all(
        np.array_equal(A @ B + B @ A, np.zeros((8, 8), dtype=complex))
        for i, A in enumerate(SIX)
        for B in SIX[i + 1:]
    )
)

QS = sp.symbols("q1 q2 q3", real=True)
sXs = sp.Matrix([[0, 1], [1, 0]])
sYs = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sZs = sp.Matrix([[1, 0], [0, -1]])
sIs = sp.eye(2)


def krs(*ms):
    o = sp.Matrix([[1]])
    for m in ms:
        o = sp.Matrix(sp.kronecker_product(o, m))
    return o


XIS = [krs(sXs, sIs, sIs), krs(sZs, sXs, sIs), krs(sZs, sZs, sXs)]
GAMS = [krs(sYs, sIs, sIs), krs(sZs, sYs, sIs), krs(sZs, sZs, sYs)]
HS = sp.zeros(8, 8)
for a in range(3):
    HS += (1 + sp.cos(QS[a])) * XIS[a] + sp.sin(QS[a]) * GAMS[a]

HD = sp.zeros(8, 8)
for s in range(8):
    sv = [(s >> (2 - a)) & 1 for a in range(3)]
    for a in range(3):
        e = eta_ks(sv, a)
        bit = 1 << (2 - a)
        ph = sp.cos(QS[a]) + sp.I * sp.sin(QS[a])
        if sv[a] == 0:
            t = s | bit
            HD[t, s] += e
            HD[s, t] += e
        else:
            t = s & ~bit
            HD[t, s] += e * sp.conjugate(ph)
            HD[s, t] += e * ph
closed_form_exact = sp.expand(HD - HS) == sp.zeros(8, 8)

check(
    "A1 [exact, sympy] Gamma = (Y1, Z1Y2, Z1Z2Y3), Xi = (X1, Z1X2, Z1Z2X3) are a Cl(6) set, and the 2x2x2-cell Bloch "
    "block of KS hopping is sum_a (1+cos q_a) Xi_a + sin q_a Gamma_a in q",
    is_clifford_set and closed_form_exact,
)

SQ = sp.expand_trig(sp.expand(HS * HS))
TARG = 6 + 2 * sum(sp.cos(QS[a]) for a in range(3))
sq_ok = sp.simplify(SQ - TARG * sp.eye(8)) == sp.zeros(8, 8)
tr_ok = sp.simplify(HS.trace()) == 0
check(
    "A2 [exact, sympy] H(q)^2 = (6 + 2 sum_a cos q_a) I and tr H(q) = 0, so the cell spectrum is "
    "E(q) = +- sqrt(6 + 2 sum_a cos q_a), each fourfold",
    sq_ok and tr_ok,
)


def exact_torus_spectrum(L):
    """Exact multiset of eigenvalues from the Cl(6) identity of A2."""
    out = Counter()
    for m in itertools.product(range(L // 2), repeat=3):
        s = 6 + 2 * sum(sp.cos(sp.Rational(4 * mi, L) * sp.pi) for mi in m)
        E = sp.sqrt(sp.nsimplify(sp.simplify(s)))
        out[sp.simplify(E)] += 4
        out[sp.simplify(-E)] += 4
    return out


spec4 = exact_torus_spectrum(4)
want4 = Counter()
for val, mult in ((-2 * sp.sqrt(3), 4), (-2 * sp.sqrt(2), 12), (-2, 12), (0, 8)):
    want4[sp.simplify(val)] += mult
    if val != 0:
        want4[sp.simplify(-val)] += mult
    else:
        want4[sp.simplify(val)] += 0
spec4_ok = spec4 == want4 and sum(spec4.values()) == 64
check(
    "A3 [exact, sympy] coarse torus L=4, 64 modes: the eight cell blocks give exactly the spectrum "
    "-2sqrt3 x4, -2sqrt2 x12, -2 x12, 0 x8 and its mirror",
    spec4_ok,
)


def ks_matrix(dims, periodic, signs=None):
    sites = [v for v in itertools.product(*(range(d) for d in dims))]
    idx = {v: i for i, v in enumerate(sites)}
    M = np.zeros((len(sites), len(sites)))
    for v in sites:
        for a in range(3):
            w = list(v)
            w[a] += 1
            if periodic:
                w[a] %= dims[a]
            elif w[a] >= dims[a]:
                continue
            w = tuple(w)
            e = eta_ks(v, a) if signs is None else signs[(v, a)]
            M[idx[w], idx[v]] += e
            M[idx[v], idx[w]] += e
    return M, sites, idx


def spec_pairs(M, dec=6):
    e = np.round(np.linalg.eigvalsh(M), dec) + 0.0
    v, c = np.unique(e, return_counts=True)
    return list(zip(["%+.6f" % x for x in v], c.tolist()))


def bloch_prediction(L, dec=6):
    pred = []
    for m in itertools.product(range(L // 2), repeat=3):
        q = [4 * np.pi * mi / L for mi in m]
        E = np.sqrt(max(0.0, 6 + 2 * sum(np.cos(x) for x in q)))
        pred += [E] * 4 + [-E] * 4
    v, c = np.unique(np.round(sorted(pred), dec) + 0.0, return_counts=True)
    return list(zip(["%+.6f" % x for x in v], c.tolist()))


num_ok = True
zmodes = []
for L in (6, 8):
    M, _, _ = ks_matrix((L, L, L), True)
    num_ok = num_ok and spec_pairs(M) == bloch_prediction(L)
    zmodes.append(int(np.sum(np.abs(np.linalg.eigvalsh(M)) < 1e-9)))
check(
    "A4 [numerical, 1e-9] coarse tori L=6 (216 modes) and L=8 (512) reproduce the same Bloch prediction "
    "eigenvalue by eigenvalue, with %d and %d zero modes" % tuple(zmodes),
    num_ok and zmodes == [0, 8],
)

# ================================================== group B: spin and taste split


def targets(sg):
    return [sg * np.kron(SIG[a], TT) for a in range(3)] + [np.kron(I2, BB[a]) for a in range(3)]


def averaging_intertwiner(N):
    """U = sum_S N_S M G_S^dag: exact Z[i] intertwiner, U G_k = N_k U."""
    pg, pn = {}, {}
    for m in range(64):
        g = np.eye(8, dtype=complex)
        n = np.eye(8, dtype=complex)
        for k in range(6):
            if (m >> k) & 1:
                g = g @ SIX[k]
                n = n @ N[k]
        pg[m] = g.conj().T
        pn[m] = n
    for r in range(8):
        for c in range(8):
            M = np.zeros((8, 8), dtype=complex)
            M[r, c] = 1
            U = sum(pn[m] @ M @ pg[m] for m in range(64))
            if abs(np.linalg.det(U)) > 1e-6:
                return U
    return None


UEX = {}
b_ok = True
for sg in (1, -1):
    N = targets(sg)
    U = averaging_intertwiner(N)
    if U is None:
        b_ok = False
        continue
    gauss = all(
        float(z.real).is_integer() and float(z.imag).is_integer() for z in U.ravel()
    )
    inter = all(np.array_equal(U @ SIX[k], N[k] @ U) for k in range(6))
    UU = U @ U.conj().T
    scal = UU[0, 0].real
    unit = np.array_equal(UU, scal * np.eye(8, dtype=complex)) and scal > 0
    b_ok = b_ok and gauss and inter and unit
    UEX[sg] = U / np.sqrt(scal)
target_cl = all(
    np.array_equal(A @ A, np.eye(8, dtype=complex))
    for A in targets(1)
) and all(
    np.array_equal(A @ B + B @ A, np.zeros((8, 8), dtype=complex))
    for i, A in enumerate(targets(1))
    for B in targets(1)[i + 1:]
)
check(
    "B1 [exact] sigma_a (x) T, I (x) B_a (T = diag(1,1,-1,-1); B = XX, XY, XZ) is a Cl(6) set, and Clifford averaging "
    "gives U with Z[i] entries, U U^dag = 16 I, intertwining exactly on both branches",
    b_ok and target_cl,
)

FP = 998244353
IFP = pow(3, (FP - 1) // 4, FP)


def to_fp(M):
    return (
        np.rint(M.real).astype(np.int64) % FP
        + (np.rint(M.imag).astype(np.int64) % FP) * IFP
    ) % FP


def rank_fp(A):
    A = A.copy() % FP
    m, n = A.shape
    r = 0
    for c in range(n):
        piv = None
        for i in range(r, m):
            if A[i, c] % FP:
                piv = i
                break
        if piv is None:
            continue
        A[[r, piv]] = A[[piv, r]]
        A[r] = (A[r] * pow(int(A[r, c]), FP - 2, FP)) % FP
        col = A[:, c].copy()
        col[r] = 0
        A = (A - np.outer(col, A[r])) % FP
        r += 1
        if r == m:
            break
    return r


ranks = []
for sg in (1, -1):
    N = targets(sg)
    rows = [
        np.kron(np.eye(8, dtype=complex), SIX[k].T) - np.kron(N[k], np.eye(8, dtype=complex))
        for k in range(6)
    ]
    ranks.append(rank_fp(to_fp(np.vstack(rows))))
check(
    "B2 [exact rank] the 384x64 intertwining system has rank %d over F_p, p = 1 mod 4, and U is a nonzero exact "
    "solution, so each branch nullspace is 1-dimensional and U is unique up to a phase" % ranks[0],
    ranks == [63, 63],
)

maxdev = 0.0
Um = UEX[-1]
tG = [np.kron(SIG[a], TT) for a in range(3)]
tB = [np.kron(I2, BB[a]) for a in range(3)]
for _ in range(300):
    p = RNG.uniform(-np.pi, np.pi, 3)
    lhs = Um @ bloch_numeric(np.pi + p) @ Um.conj().T
    rhs = sum(np.sin(p[a]) * tG[a] + (1 - np.cos(p[a])) * tB[a] for a in range(3))
    maxdev = max(maxdev, float(np.abs(lhs - rhs).max()))
spin_singlet = all(np.array_equal(tB[a], np.kron(I2, BB[a])) for a in range(3))
check(
    "B3 [numerical, 1e-12] U H(pi+p) U^dag = sum_a sin p_a (sigma_a (x) T) + (1 - cos p_a)(I (x) B_a) over 300 random "
    "p, max dev %.1e; the taste-mixing term carries I on spin, a singlet" % maxdev,
    maxdev < 1e-12 and spin_singlet,
)

# ============================================== group C: the KS sign is a flux class

parity_hol = set()
for par in itertools.product((0, 1), repeat=3):
    for (a, b) in ((0, 1), (0, 2), (1, 2)):
        parity_hol.add(
            eta_ks(par, a) * eta_ks(va(par, EX[a]), b) * eta_ks(va(par, EX[b]), a) * eta_ks(par, b)
        )
torus_hol = {}
for L in (4, 6, 8):
    hs = set()
    for v in itertools.product(range(L), repeat=3):
        for (a, b) in ((0, 1), (0, 2), (1, 2)):
            hs.add(
                eta_ks(v, a)
                * eta_ks(wrap(va(v, EX[a]), (L, L, L)), b)
                * eta_ks(wrap(va(v, EX[b]), (L, L, L)), a)
                * eta_ks(v, b)
            )
    torus_hol[L] = hs
check(
    "C1 [exact] every plaquette holonomy of the KS signs is -1: all 24 parity-class/plane holonomies, and all "
    "192, 648 and 1536 plaquettes of the coarse tori L = 4, 6, 8",
    parity_hol == {-1} and all(v == {-1} for v in torus_hol.values()),
)

open_sites = [v for v in itertools.product(range(2), repeat=3)]
open_links = []
for v in open_sites:
    for a in range(3):
        w = va(v, EX[a])
        if all(c < 2 for c in w):
            open_links.append((v, w, a))
brute = None
for m in range(256):
    s = {v: (1 if not ((m >> i) & 1) else -1) for i, v in enumerate(open_sites)}
    if all(s[v] * s[w] * 1 == eta_ks(v, a) for (v, w, a) in open_links):
        brute = s
        break
check(
    "C2 [exact] no site gauge c_v -> s(v) c_v carries plain to KS: loop holonomy is gauge invariant, plain gives +1 and "
    "KS -1 on each plaquette, and all 2^8 patterns on the open 2x2x2 fail",
    brute is None,
)

roles = set()
for v in itertools.product(range(4), repeat=3):
    roles.add(
        tuple(
            tuple((2 * v[i] + d[i]) % 2 for i in range(3))
            for d in itertools.product((0, 1), repeat=3)
        )
    )
mod4_tab = {}
for v in itertools.product(range(2), repeat=2):
    f = (2 * v[0] % 4, 2 * v[1] % 4)
    mod4_tab[f] = (eta_ks((v[0], v[1], 0), 0), eta_ks((v[0], v[1], 0), 1), eta_ks((v[0], v[1], 0), 2))
mod4_ok = True
for v in itertools.product(range(8), repeat=3):
    if (eta_ks(v, 0), eta_ks(v, 1), eta_ks(v, 2)) != mod4_tab[(2 * v[0] % 4, 2 * v[1] % 4)]:
        mod4_ok = False
eta_varies = len({eta_ks(v, 1) for v in itertools.product(range(4), repeat=3)}) == 2
check(
    "C3 [exact] every coarse 2v is a corner and its cell's fine-mod-2 role pattern takes %d value, so any function of it "
    "is constant while the KS sign varies; that sign is a function of 2v mod 4 on 8^3" % len(roles),
    len(roles) == 1 and eta_varies and mod4_ok,
)
print("  2v mod 4 in (x, y) -> (eta_x, eta_y, eta_z), independent of z:")
for f in sorted(mod4_tab):
    print("    (%d,%d) -> (%s,%s,%s)" % (f[0], f[1], *("+" if t > 0 else "-" for t in mod4_tab[f])))

# ==================================================== group D: the cubic group

L4 = 4
S4 = [v for v in itertools.product(range(L4), repeat=3)]
IDX4 = {v: i for i, v in enumerate(S4)}
N4 = len(S4)
H4 = np.zeros((N4, N4))
for v in S4:
    for a in range(3):
        w = wrap(va(v, EX[a]), (L4,) * 3)
        H4[IDX4[w], IDX4[v]] += eta_ks(v, a)
        H4[IDX4[v], IDX4[w]] += eta_ks(v, a)

ROTS = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), dtype=int)
        for i in range(3):
            M[i, perm[i]] = sg[i]
        if round(np.linalg.det(M)) == 1:
            ROTS.append(M)
RKEY = {tuple(M.flatten()): i for i, M in enumerate(ROTS)}


def rot_act(M, v):
    return tuple(int(sum(M[i, j] * v[j] for j in range(3))) % L4 for i in range(3))


def class_of(M):
    tr = int(round(np.trace(M)))
    if tr == 3:
        return "E"
    if tr == 0:
        return "8C3"
    if tr == 1:
        return "6C4"
    return "3C2" if np.count_nonzero(M - np.diag(np.diag(M))) == 0 else "6C2p"


def gauge_to(target):
    g = {(0, 0, 0): 1}
    dq = deque([(0, 0, 0)])
    while dq:
        v = dq.popleft()
        for a in range(3):
            for sgn in (1, -1):
                w = list(v)
                w[a] += sgn
                w = tuple(x % L4 for x in w)
                src = v if sgn == 1 else w
                r = target(src, a) * eta_ks(src, a)
                if w in g:
                    if g[w] != g[v] * r:
                        return None
                else:
                    g[w] = g[v] * r
                    dq.append(w)
    return g


CS = []
lift_ok = True
for M in ROTS:
    def tgt(v, a, M=M):
        return H4[IDX4[rot_act(M, v)], IDX4[rot_act(M, wrap(va(v, EX[a]), (L4,) * 3))]]

    g = gauge_to(tgt)
    if g is None:
        lift_ok = False
        continue
    C = np.zeros((N4, N4))
    for v in S4:
        C[IDX4[rot_act(M, v)], IDX4[v]] = g[v]
    CS.append(C)
lift_ok = (
    lift_ok
    and len(CS) == 24
    and all(np.allclose(C @ H4 @ C.T, H4) for C in CS)
    and all(
        np.allclose(C @ C.T, np.eye(N4)) and set(np.unique(C)).issubset({-1.0, 0.0, 1.0})
        for C in CS
    )
)
check(
    "D1 [exact] all 24 proper cubic rotations lift to signed permutations of the L=4 torus with "
    "C_R H C_R^T = H, each orthogonal with entries in {0, +-1}, one nonzero per row and column",
    lift_ok,
)

KER = np.zeros((N4, 8))
for s in range(8):
    sv = [(s >> (2 - a)) & 1 for a in range(3)]
    for R in itertools.product(range(2), repeat=3):
        KER[IDX4[tuple(2 * R[a] + sv[a] for a in range(3))], s] = (-1) ** sum(R)
KER /= np.linalg.norm(KER[:, 0])
MS = [KER.T @ C @ KER for C in CS]
ker_ok = (
    np.allclose(KER.T @ KER, np.eye(8))
    and abs(H4 @ KER).max() < 1e-12
    and int(np.sum(np.abs(np.linalg.eigvalsh(H4)) < 1e-9)) == 8
    and max(abs(CS[i] @ KER - KER @ MS[i]).max() for i in range(24)) < 1e-12
)


def closure_counts(reps, tol=1e-9):
    bad = neg = 0
    for i in range(24):
        for j in range(24):
            k = RKEY[tuple((ROTS[i] @ ROTS[j]).flatten())]
            P = reps[i] @ reps[j]
            if np.allclose(P, reps[k], atol=tol):
                continue
            if np.allclose(P, -reps[k], atol=tol):
                neg += 1
            else:
                bad += 1
    return bad, neg


badN, negN = closure_counts(CS)
bad8, neg8 = closure_counts(MS)
check(
    "D2 [exact] the lift closes on the nose: all 576 products C_R C_R' = C_{RR'} at the 64x64 level and all 576 on the "
    "8 zero modes, %d carrying -1 -- a genuine representation of O, not projective" % (negN + neg8),
    ker_ok and (badN, negN, bad8, neg8) == (0, 0, 0, 0),
)

CHARS = {}
for i, M in enumerate(ROTS):
    CHARS.setdefault(class_of(M), set()).add(round(float(np.trace(MS[i])), 6))
TAB = {
    "A1": [1, 1, 1, 1, 1],
    "A2": [1, 1, 1, -1, -1],
    "E": [2, -1, 2, 0, 0],
    "T1": [3, 0, -1, 1, -1],
    "T2": [3, 0, -1, -1, 1],
}
ORDER = ["E", "8C3", "3C2", "6C4", "6C2p"]
SZ = [1, 8, 3, 6, 6]
tab_ok = all(
    abs(sum(SZ[i] * TAB[x][i] * TAB[y][i] for i in range(5)) / 24 - (1 if x == y else 0)) < 1e-9
    for x in TAB
    for y in TAB
)
chi = [sorted(CHARS[c])[0] for c in ORDER]
decomp = {k: round(sum(SZ[i] * TAB[k][i] * chi[i] for i in range(5)) / 24, 9) for k in TAB}
check(
    "D3 [exact] characters on the eight zero modes (E, 8C3, 3C2, 6C4, 6C2') = (%d, %d, %d, %d, %d) decompose, against a "
    "self-checked table of O, as 2 A1 + 2 T1, sharpening the landed 1 + 3 + 3 + 1 grading"
    % tuple(int(x) for x in chi),
    tab_ok
    and [len(CHARS[c]) for c in ORDER] == [1] * 5
    and chi == [8.0, 2.0, 0.0, 4.0, 0.0]
    and decomp == {"A1": 2.0, "A2": 0.0, "E": 0.0, "T1": 2.0, "T2": 0.0},
)


def kron_factor(M):
    A = M.reshape(2, 4, 2, 4).transpose(0, 2, 1, 3).reshape(4, 16)
    u, s, vh = np.linalg.svd(A)
    return u[:, 0].reshape(2, 2), (s[0] * vh[0]).reshape(4, 4), s[1] / s[0]


SPIN, TASTE = [], []
worst_ratio = 0.0
fac_ok = True
for i in range(24):
    Mst = Um @ MS[i] @ Um.conj().T
    S, T, ratio = kron_factor(Mst)
    worst_ratio = max(worst_ratio, float(ratio))
    fac_ok = fac_ok and np.allclose(np.kron(S, T), Mst, atol=1e-9)
    f = S.ravel()
    k0 = int(np.argmax(np.abs(f)))
    ph = np.conj(f[k0]) / abs(f[k0])
    S, T = S * ph, T / ph
    lam = np.sqrt(np.linalg.det(S))
    SPIN.append(S / lam)
    TASTE.append(T * lam)


def cocycle(reps, tol=1e-8):
    cc = {}
    bad = 0
    for i in range(24):
        for j in range(24):
            k = RKEY[tuple((ROTS[i] @ ROTS[j]).flatten())]
            P = reps[i] @ reps[j]
            if np.allclose(P, reps[k], atol=tol):
                cc[(i, j)] = 0
            elif np.allclose(P, -reps[k], atol=tol):
                cc[(i, j)] = 1
            else:
                bad += 1
    return cc, bad


def is_coboundary(cc):
    piv = {}
    for (i, j), c in cc.items():
        k = RKEY[tuple((ROTS[i] @ ROTS[j]).flatten())]
        r = 0
        for t in (i, j, k):
            r ^= 1 << t
        while r:
            b = r & -r
            p = b.bit_length() - 1
            if p in piv:
                pr, pc = piv[p]
                r ^= pr
                c ^= pc
            else:
                piv[p] = (r, c)
                r = 0
                break
        else:
            if c:
                return False
    return True


ccs, bs = cocycle(SPIN)
cct, bt = cocycle(TASTE)
negs, negt = sum(ccs.values()), sum(cct.values())
spin_chi = {}
for i in range(24):
    spin_chi.setdefault(class_of(ROTS[i]), set()).add(round(abs(np.trace(SPIN[i])), 6))
spinor = [sorted(spin_chi[c])[0] for c in ORDER] == [2.0, 1.0, 0.0, round(2 ** 0.5, 6), 0.0]
check(
    "D4 [numerical, svd ratio %.0e] in the B basis every lift factorises as (2x2 spin) (x) (4x4 taste); det-normalised, "
    "both carry one cocycle, %d of 576 pairs -1, no coboundary: each factor projective, the product genuine"
    % (worst_ratio, negs),
    fac_ok
    and (bs, bt) == (0, 0)
    and negs == negt
    and negs > 0
    and not is_coboundary(ccs)
    and not is_coboundary(cct)
    and spinor,
)

# ================================================ group E: the chirality grading

eps_anti = all(
    np.array_equal(EPS8 @ A + A @ EPS8, np.zeros((8, 8), dtype=complex)) for A in SIX
)
TBBB = TT @ BB[0] @ BB[1] @ BB[2]
img = {}
for sg in (1, -1):
    U = UEX[sg]
    im = U @ EPS8 @ U.conj().T
    img[sg] = (
        np.allclose(im, np.kron(I2, TBBB), atol=1e-9),
        np.allclose(im, -np.kron(I2, TBBB), atol=1e-9),
        any(np.allclose(im, t * np.kron(I2, TT), atol=1e-9) for t in (1, -1)),
    )
check(
    "E1 [exact] epsilon = Z1 Z2 Z3 anticommutes with all six generators, hence with H(q) at every q, and "
    "U epsilon U^dag = I (x) (+- T B1 B2 B3) on the two branches, never +- I (x) T",
    eps_anti
    and all(img[sg][0] != img[sg][1] for sg in (1, -1))
    and all(img[sg][0] or img[sg][1] for sg in (1, -1))
    and not any(img[sg][2] for sg in (1, -1)),
)

# ============================ group F: the flux sector of the superfast encoding


def pcnt(n):
    return bin(n).count("1")


class Q:
    """i^k X^x Z^z on a register of qubits indexed by bit position."""

    __slots__ = ("k", "x", "z")

    def __init__(self, k, x, z):
        self.k = k & 3
        self.x = x
        self.z = z

    def __mul__(a, b):
        return Q(a.k + b.k + 2 * pcnt(a.z & b.x), a.x ^ b.x, a.z ^ b.z)

    def scal(s, t):
        return Q(s.k + t, s.x, s.z)

    def neg(s):
        return Q(s.k + 2, s.x, s.z)

    def __eq__(a, b):
        return a.k == b.k and a.x == b.x and a.z == b.z

    def herm(s):
        return (s.k & 1) == (pcnt(s.x & s.z) & 1)

    def isI(s):
        return s.x == 0 and s.z == 0 and s.k == 0

    def ismI(s):
        return s.x == 0 and s.z == 0 and s.k == 2

    def vec(s, n):
        return s.x | (s.z << n)


IDQ = Q(0, 0, 0)


def qprod(seq):
    o = IDQ
    for p in seq:
        o = o * p
    return o


class Lat:
    """Coarse cubic block or torus with the BK superfast encoding on its edges."""

    def __init__(self, dims, periodic):
        self.dims = tuple(dims)
        self.per = periodic
        self.V = [v for v in itertools.product(*(range(d) for d in dims))]
        self.nv = len(self.V)
        self.E = []
        for v in self.V:
            for ax in range(3):
                if self.step(v, EX[ax]) is not None:
                    self.E.append((v, ax))
        self.ei = {e: i for i, e in enumerate(self.E)}
        self.nq = len(self.E)
        self.inc = {}
        for v in self.V:
            d = {}
            for r in range(6):
                w = self.step(v, DIRS[r])
                if w is None:
                    continue
                d[r] = (w, self.ei[(v, r - 3) if r >= 3 else (w, r)])
            self.inc[v] = d
        self.star = {v: sum(1 << q for (_, q) in self.inc[v].values()) for v in self.V}

    def step(self, v, d):
        w = va(v, d)
        if self.per:
            return wrap(w, self.dims)
        return w if all(0 <= w[i] < self.dims[i] for i in range(3)) else None

    def A(self, v, r):
        w, q = self.inc[v][r]
        x, z = 1 << q, 0
        for r2, (_, q2) in self.inc[v].items():
            if r2 < r:
                z ^= 1 << q2
        rb = (r + 3) % 6
        for r2, (_, q2) in self.inc[w].items():
            if r2 < rb:
                z ^= 1 << q2
        p = Q(pcnt(x & z) & 1, x, z)
        return p if r >= 3 else p.neg()

    def Aij(self, i, j):
        for r in range(6):
            if r in self.inc[i] and self.inc[i][r][0] == j:
                return self.A(i, r)
        raise KeyError("not adjacent")

    def B(self, v):
        return Q(0, 0, self.star[v])

    def faces(self):
        out = []
        for v in self.V:
            for d1 in range(3):
                for d2 in range(d1 + 1, 3):
                    a = self.step(v, EX[d1])
                    b = self.step(v, EX[d2])
                    if a is None or b is None:
                        continue
                    c = self.step(a, EX[d2])
                    if c is None:
                        continue
                    out.append((v, a, c, b))
        return out

    def loop(self, cyc):
        n = len(cyc)
        return qprod([self.Aij(cyc[a], cyc[(a + 1) % n]) for a in range(n)]).scal(n)


def transport(L, path):
    """Ordered product of the encoded hops T_{i_{k+1} i_k} = (i/2) A (B - B) along path.

    On any configuration where every step is legal -- source occupied, target
    empty -- each factor contributes (i/2)(+1 - (-1)) = i, hence the i^n.
    """
    n = len(path) - 1
    ops = [L.Aij(path[k + 1], path[k]) for k in range(n)]
    return qprod(ops[::-1]).scal(n)


def f2_pivots(gens):
    piv = {}
    for j, g in enumerate(gens):
        v, c = g, 1 << j
        while v:
            p = v.bit_length() - 1
            if p in piv:
                pv, pc = piv[p]
                v ^= pv
                c ^= pc
            else:
                piv[p] = (v, c)
                break
    return piv


def f2_express(target, piv):
    v, c = target, 0
    while v:
        p = v.bit_length() - 1
        if p not in piv:
            return None
        pv, pc = piv[p]
        v ^= pv
        c ^= pc
    return c


def f2_relations(gens):
    piv, rel = {}, []
    for j, g in enumerate(gens):
        v, c = g, 1 << j
        while v:
            p = v.bit_length() - 1
            if p in piv:
                pv, pc = piv[p]
                v ^= pv
                c ^= pc
            else:
                piv[p] = (v, c)
                break
        if v == 0:
            rel.append(c)
    return rel, len(piv)


def bits(m):
    out = []
    while m:
        b = m & -m
        out.append(b.bit_length() - 1)
        m ^= b
    return out


def solve_f2(rows, nunk):
    mask = (1 << nunk) - 1
    piv, R = [], []
    for r in rows:
        for i, p in enumerate(piv):
            if (r >> p) & 1:
                r ^= R[i]
        low = r & mask
        if low == 0:
            if r:
                return None
            continue
        p = low.bit_length() - 1
        for i in range(len(R)):
            if (R[i] >> p) & 1:
                R[i] ^= r
        R.append(r)
        piv.append(p)
    sol = 0
    for i, p in enumerate(piv):
        if (R[i] >> nunk) & 1:
            sol |= 1 << p
    return sol


FACE_BLOCKS = [
    ((2, 2, 2), False, "o222"),
    ((3, 3, 3), False, "o333"),
    ((4, 4, 4), False, "o444"),
    ((3, 3, 3), True, "3x3x3"),
    ((3, 3, 4), True, "3x3x4"),
    ((3, 4, 5), True, "3x4x5"),
    ((4, 4, 4), True, "4x4x4"),
    ((4, 4, 5), True, "4x4x5"),
    ((4, 4, 6), True, "4x4x6"),
    ((4, 5, 6), True, "4x5x6"),
    ((5, 5, 5), True, "5x5x5"),
    ((5, 5, 6), True, "5x5x6"),
]

hop_face_ok = True
hop_counts = []
for dims, per, tag in FACE_BLOCKS[:2] + [((3, 3, 3), True, "T3"), ((4, 4, 4), True, "T4")]:
    L = Lat(dims, per)
    F = L.faces()
    for f in F:
        Sf = L.loop(f)
        Wf = transport(L, [f[0], f[1], f[2], f[3], f[0]])
        if not (Wf == Sf and Sf.herm() and (Sf * Sf).isI()):
            hop_face_ok = False
    hop_counts.append(len(F))

L222 = Lat((2, 2, 2), False)
nq222 = L222.nq
ar222 = np.arange(1 << nq222, dtype=np.int64)


def popc64(a):
    c = np.zeros_like(a)
    for i in range(16):
        c += (a >> i) & 1
    return c


BD = {v: (1 - 2 * (popc64(ar222 & L222.star[v]) & 1)).astype(np.int64) for v in L222.V}
legal_ok = True
D_LEGAL = (1 << nq222) // 4
for (v, ax) in L222.E:
    w = L222.step(v, EX[ax])
    diff = BD[w] - BD[v]
    legal = (BD[v] == -1) & (BD[w] == 1)
    back = (BD[v] == 1) & (BD[w] == -1)
    rest = ~(legal | back)
    if not (
        np.all(diff[legal] == 2)
        and np.all(diff[back] == -2)
        and np.all(diff[rest] == 0)
        and legal.sum() == D_LEGAL
    ):
        legal_ok = False
check(
    "F1 [exact, symplectic] (B_j - B_i) = 2 on exactly the legal steps, so T_ji = (i/2) A_ji (B_j - B_i) acts there as "
    "i A_ji, and the ordered four-hop product round a face equals S_f exactly, Z4 phase included, on %d, %d, %d, %d faces"
    % tuple(hop_counts),
    hop_face_ok and legal_ok,
)

rel_rows = []
prod_ok = True
consistency = {}
f2_agree = True
for dims, per, tag in FACE_BLOCKS:
    L = Lat(dims, per)
    F = L.faces()
    S = [L.loop(f) for f in F]
    rels, rk = f2_relations([s.vec(L.nq) for s in S])
    sizes, cons = set(), True
    for r in rels:
        idxs = bits(r)
        pr = qprod([S[j] for j in idxs])
        if not pr.isI():
            prod_ok = False
        sizes.add(len(idxs))
        if len(idxs) % 2:
            cons = False
    rows = []
    for f in F:
        m = 0
        for k in range(4):
            p, q = f[k], f[(k + 1) % 4]
            for ax in range(3):
                if L.step(p, EX[ax]) == q:
                    m ^= 1 << L.ei[(p, ax)]
                    break
                if L.step(q, EX[ax]) == p:
                    m ^= 1 << L.ei[(q, ax)]
                    break
        rows.append(m | (1 << L.nq))
    solvable = solve_f2(rows, L.nq) is not None
    if solvable != cons:
        f2_agree = False
    consistency[tag] = (L.nv, L.nq, len(F), rk, len(rels), sorted(sizes), cons)
    rel_rows.append((tag, L.dims, per, cons))
check(
    "F2 [exact] every F2 relation among the face stabilizers has ordered product exactly +I on all %d blocks and tori, "
    "so S_f = -1 for all f is consistent iff every relation has even support" % len(FACE_BLOCKS),
    prod_ok,
)

pair_rule = {}
for tag, dims, per, cons in rel_rows:
    if per:
        want = all((dims[a] * dims[b]) % 2 == 0 for a, b in ((0, 1), (0, 2), (1, 2)))
    else:
        want = True
    pair_rule[tag] = (want == cons)
check(
    "F3 [exact] the all-(-1) face sector exists on every open block, and on an L1xL2xL3 torus iff every pairwise product "
    "L_a L_b is even -- at most one odd period, the KS periodicity condition",
    all(pair_rule.values()),
)
line = []
for tag in consistency:
    nv, nq, nf, rk, nr, sizes, cons = consistency[tag]
    line.append(
        "%s %d/%d/%d/%d %s %s"
        % (tag, nv, nf, rk, nr, ",".join(str(x) for x in sizes), "YES" if cons else "no")
    )
print("  V/faces/rank/rel, supports, all-(-1):")
for i in range(0, len(line), 3):
    print("   " + " | ".join(line[i:i + 3]))
check(
    "F4 [exact] an independent F2 test, solving 'four edge signs sum to 1' for a pi-flux sign field over all %d faces "
    "of the twelve, is solvable on exactly the blocks of F3" % sum(c[2] for c in consistency.values()),
    f2_agree,
)


def induced_eta(L, wilson=(1, 1, 1)):
    """Sign field read off the sector S_f = -1, with no input from KS."""
    root = L.V[0]
    par = {root: None}
    dq = deque([root])
    while dq:
        v = dq.popleft()
        for r in range(6):
            if r not in L.inc[v]:
                continue
            w = L.inc[v][r][0]
            if w not in par:
                par[w] = v
                dq.append(w)
    tree = {frozenset((v, w)) for w, v in par.items() if v is not None}

    def tpath(v):
        p = [v]
        while par[p[-1]] is not None:
            p.append(par[p[-1]])
        return p[::-1]

    gens = [L.loop(f) for f in L.faces()]
    vals = [-1] * len(gens)
    if L.per:
        for ax in range(3):
            cyc = [wrap(tuple((k if i == ax else 0) for i in range(3)), L.dims) for k in range(L.dims[ax])]
            gens.append(transport(L, cyc + [cyc[0]]))
        vals += list(wilson)
    gv = [g.vec(L.nq) for g in gens]
    piv = f2_pivots(gv)
    cons = True
    rels, _ = f2_relations(gv)
    for r in rels:
        idxs = bits(r)
        pr = qprod([gens[j] for j in idxs])
        eps = 1 if pr.isI() else (-1 if pr.ismI() else 0)
        pv = 1
        for j in idxs:
            pv *= vals[j]
        if eps == 0 or pv != eps:
            cons = False
    eta = {}
    for (v, ax) in L.E:
        w = L.step(v, EX[ax])
        if frozenset((v, w)) in tree:
            eta[(v, ax)] = 1
            continue
        pv, pw = tpath(v), tpath(w)
        op = transport(L, pv + [w] + pw[::-1][1:])
        c = f2_express(op.vec(L.nq), piv)
        if c is None:
            return None, False
        idxs = bits(c)
        pr = qprod([gens[j] for j in idxs])
        resid = (op.k - pr.k) & 3
        if resid not in (0, 2):
            return None, False
        e = 1 if resid == 0 else -1
        for j in idxs:
            e *= vals[j]
        eta[(v, ax)] = e
    return eta, cons


def holonomies(L, eta):
    out = set()
    for f in L.faces():
        v, a, c, b = f
        pr = 1
        for (p, q) in ((v, a), (a, c), (b, c), (v, b)):
            for ax in range(3):
                if L.step(p, EX[ax]) == q and (p, ax) in eta:
                    pr *= eta[(p, ax)]
                    break
                if L.step(q, EX[ax]) == p and (q, ax) in eta:
                    pr *= eta[(q, ax)]
                    break
        out.add(pr)
    return out


def gauge_witness(L, e1, e2):
    s = {L.V[0]: 1}
    dq = deque([L.V[0]])
    adj = {}
    for (v, ax) in L.E:
        w = L.step(v, EX[ax])
        adj.setdefault(v, []).append((w, v, ax))
        adj.setdefault(w, []).append((v, v, ax))
    while dq:
        v = dq.popleft()
        for (w, src, ax) in adj.get(v, []):
            r = e1[(src, ax)] * e2[(src, ax)]
            if w in s:
                if s[w] != s[v] * r:
                    return None
            else:
                s[w] = s[v] * r
                dq.append(w)
    return s if len(s) == L.nv else None


def one_particle(L, eta):
    idx = {v: i for i, v in enumerate(L.V)}
    M = np.zeros((L.nv, L.nv))
    for (v, ax) in L.E:
        w = L.step(v, EX[ax])
        M[idx[w], idx[v]] += eta[(v, ax)]
        M[idx[v], idx[w]] += eta[(v, ax)]
    return M


GAUGE_BLOCKS = [((2, 2, 2), False), ((3, 3, 3), False), ((4, 4, 4), False), ((4, 4, 4), True)]
gauge_ok = True
spec_ok = True
neg_sites = []
ETA222 = None
for dims, per in GAUGE_BLOCKS:
    L = Lat(dims, per)
    eta, cons = induced_eta(L)
    ks = {(v, ax): eta_ks(v, ax) for (v, ax) in L.E}
    s = gauge_witness(L, eta, ks)
    ok = (
        cons
        and holonomies(L, eta) == {-1}
        and holonomies(L, ks) == {-1}
        and s is not None
        and all(s[v] * s[L.step(v, EX[ax])] * eta[(v, ax)] == ks[(v, ax)] for (v, ax) in L.E)
    )
    gauge_ok = gauge_ok and ok
    neg_sites.append(0 if s is None else sum(1 for v in L.V if s[v] < 0))
    spec_ok = spec_ok and np.allclose(
        np.sort(np.linalg.eigvalsh(one_particle(L, eta))),
        np.sort(np.linalg.eigvalsh(one_particle(L, ks))),
        atol=1e-9,
    )
    if dims == (2, 2, 2) and not per:
        ETA222 = eta
check(
    "F5 [exact] eta', read off the all-(-1) sector by spanning-tree gauge fixing and cycle transport with no KS input, "
    "has holonomy -1 on every plaquette and a gauge witness s(v) to KS on the open 2x2x2, 3x3x3, 4x4x4 and the 4x4x4 "
    "torus (%d, %d, %d, %d minus sites)" % tuple(neg_sites),
    gauge_ok,
)
check(
    "F6 [numerical, 1e-9] the one-particle spectra of eta' and KS agree eigenvalue by eigenvalue on all four blocks: the "
    "flux-sector hopping is the staggered form up to a relabelling",
    spec_ok,
)

# ============================================ group G: many-body cross-check

D222 = 1 << nq222
IPOW = np.array([1, 1j, -1, -1j])


def apply_q(op, psi):
    j = ar222 ^ op.x
    return IPOW[op.k] * (1 - 2 * (popc64(j & op.z) & 1)) * psi[j]


prodB = qprod([L222.B(v) for v in L222.V]).isI()
FACES222 = L222.faces()
S222 = [L222.loop(f) for f in FACES222]
gv222 = [s.vec(nq222) for s in S222]
indep, seen = [], []
for j, g in enumerate(gv222):
    _, rk_with = f2_relations(seen + [g])
    _, rk_without = f2_relations(seen)
    if rk_with > rk_without:
        seen.append(g)
        indep.append(j)
cfg = np.zeros(D222, dtype=np.int64)
for i, v in enumerate(L222.V):
    cfg |= ((1 - BD[v]) // 2) << i
groups = {int(c): np.where(cfg == c)[0] for c in np.unique(cfg)}
states = {}
proj_ok = True
for c, ix in groups.items():
    psi = np.zeros(D222, dtype=complex)
    psi[ix] = RNG.normal(size=len(ix))
    for j in indep:
        psi = (psi - apply_q(S222[j], psi)) / 2
    nr = np.linalg.norm(psi)
    if nr < 1e-9:
        proj_ok = False
        continue
    psi /= nr
    for j in range(len(S222)):
        if not np.allclose(apply_q(S222[j], psi), -psi, atol=1e-9):
            proj_ok = False
    states[c] = psi
check(
    "G1 [exact] open 2x2x2 cube, %d edge qubits, dimension %d: prod_i B_i = +I, faces of F2 rank %d, and the joint "
    "S_f = -1 eigenspace is 1-dimensional on each of the %d B-configurations -- %d = 2^(V-1) states, the even-parity "
    "Fock space" % (nq222, D222, len(indep), len(groups), len(states)),
    prodB and proj_ok and len(states) == 128 and len(indep) == 5,
)

keys = sorted(states)
Psi = np.array([states[c] for c in keys])
cols = []
for c in keys:
    out = np.zeros(D222, dtype=complex)
    for (v, ax) in L222.E:
        w = L222.step(v, EX[ax])
        Aop = L222.Aij(v, w)
        out += 0.5j * apply_q(Aop * L222.B(v), states[c]) - 0.5j * apply_q(Aop * L222.B(w), states[c])
    cols.append(out)
Hm = Psi.conj() @ np.array(cols).T
herm = np.allclose(Hm, Hm.conj().T, atol=1e-9)
ev = np.sort(np.linalg.eigvalsh(Hm))
epsv = np.linalg.eigvalsh(one_particle(L222, ETA222))
pred = np.sort(
    np.array(
        [
            sum(epsv[i] for i in range(8) if (m >> i) & 1)
            for m in range(256)
            if bin(m).count("1") % 2 == 0
        ]
    )
)
dev = float(np.abs(ev - pred).max())
check(
    "G2 [numerical, 1e-13] the encoded hopping there is hermitian and its %d levels equal the even-parity spectrum of "
    "sum_ij eta'_ij c_i^dag c_j, max deviation %.1e" % (len(ev), dev),
    herm and dev < 1e-13,
)

print(
    "SUMMARY: on the coarse lattice 2Z^3 the staggered kinetic form is a Cl(6) operator with an exact spin x taste split, "
    "its KS sign a pi-flux class, and it is the all-(-1) face sector of the fermion's Z2 gauge structure."
)
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
