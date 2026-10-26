#!/usr/bin/env python3
"""Checker for J:derive:review-20260929-record-birth-cost-and-observability:a1.

Own machinery (Fock-space exact diagonalisation, sympy exact arithmetic, Gaussian 3-mode reductions).
No code from the source branch is used.  One process, numpy/scipy/sympy/mpmath only.

Units: the walker hop t = 1.  lam = <|s(k)|>_BZ is the energy of one coin mode of the sea.
"""
import itertools
import sys
import time
from fractions import Fraction

import numpy as np
import scipy.linalg as sl
import scipy.sparse as sp
import scipy.sparse.linalg as sla
import sympy as sy
import mpmath as mp

T0 = time.time()
PASS = 0
FAIL = 0
HIT_LINES = []


def ok(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"PASS {name} {detail}".rstrip())
    else:
        FAIL += 1
        print(f"FAIL {name} {detail}".rstrip())


def H2(x):
    x = float(x)
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * np.log2(x) - (1 - x) * np.log2(1 - x)


# ---------------------------------------------------------------------------------------------
# Part A.  Exact model: antiperiodic ring of two sites, walker hop, half filling (sympy, exact).
#          single-particle h = [[0, -i s_x],[ i s_x, 0]] has eigenvalues +-1 (doubly), so lam = 1.
# ---------------------------------------------------------------------------------------------
I_ = sy.I
Rat = sy.Rational


def jw_sym(n):
    Z = sy.Matrix([[1, 0], [0, -1]])
    a = sy.Matrix([[0, 1], [0, 0]])
    E = sy.eye(2)
    out = []
    for k in range(n):
        mats = [Z] * k + [a] + [E] * (n - k - 1)
        m = mats[0]
        for o in mats[1:]:
            m = sy.kronecker_product(m, o)
        out.append(m)
    return out


cs = jw_sym(4)
sx2 = sy.Matrix([[0, 1], [1, 0]])
h2 = sy.zeros(4, 4)
h2[0:2, 2:4] = -I_ * sx2
h2[2:4, 0:2] = I_ * sx2
H = sy.zeros(16, 16)
for i in range(4):
    for j in range(4):
        if h2[i, j] != 0:
            H += h2[i, j] * (cs[i].H * cs[j])
H = sy.simplify(H)

# spectrum bound and unique ground state
Z16 = sy.eye(16)
prod = Z16
for e in (-2, -1, 0, 1, 2):
    prod = prod * (H - e * Z16)
prod = sy.simplify(prod)
ok("A1 exact: H annihilated by prod_{e=-2..2}(H-e), so spectrum in {-2..2}", prod == sy.zeros(16, 16))
ns = (H + 2 * Z16).nullspace()
ok("A2 exact: lowest level -2 is nondegenerate (unique half-filled ground state)", len(ns) == 1)
g = ns[0]
g = g / sy.sqrt((g.H * g)[0])
g = sy.simplify(g)
E0 = sy.simplify((g.H * H * g)[0])
ok("A3 exact: E0 = -2 = -N lam with N = 2 sites, lam = <|s|> = 1", E0 == -2)

# site block of the sea correlation matrix and the K lemma ingredients
G = sy.Matrix(4, 4, lambda i, j: sy.simplify((g.H * cs[i].H * cs[j] * g)[0]))  # G_ij=<c_i^+ c_j>
ok("A4 exact: site block of <c^+ c> is 1/2 identity (maximally mixed coin pair)",
   sy.simplify(G[0:2, 0:2] - Rat(1, 2) * sy.eye(2)) == sy.zeros(2, 2))
anom = sy.Matrix(4, 4, lambda i, j: sy.simplify((g.H * cs[i] * cs[j] * g)[0]))
ok("A5 exact: anomalous correlators <c c> vanish (number conserving Slater state)", anom == sy.zeros(4, 4))
# K lemma: sum_m h_{am} <c_b^+ c_m> = -(lam/2) delta_ab
K = sy.Matrix(2, 2, lambda a, b: sy.simplify(sum(h2[a, m] * G[b, m] for m in range(4))))
ok("A6 exact: K_ab = sum_m h_am <c_b^+ c_m> = -(lam/2) delta_ab with lam = 1",
   sy.simplify(K + Rat(1, 2) * sy.eye(2)) == sy.zeros(2, 2))

# site operators (site = modes 0,1, first in the JW order) and embedded Kraus operators
c0s = sy.kronecker_product(sy.Matrix([[0, 1], [0, 0]]), sy.eye(2))
c1s = sy.kronecker_product(sy.Matrix([[1, 0], [0, -1]]), sy.Matrix([[0, 1], [0, 0]]))
site_c = [c0s, c1s]
EMB = sy.eye(4)


def embed(K4):
    return sy.kronecker_product(K4, EMB)


def direct_cost(Ks):
    tot = sy.zeros(16, 16)
    for K4 in Ks:
        Ke = embed(K4)
        tot += Ke.H * H * Ke
    return sy.simplify((g.H * tot * g)[0] - E0)


def Phi_star(Ks, X):
    out = sy.zeros(4, 4)
    for K4 in Ks:
        out += K4.H * X * K4
    return out


def formula_cost(Ks, lam=1):
    A = sy.zeros(2, 2)
    for a in range(2):
        Y = Phi_star(Ks, site_c[a].H)
        for b in range(2):
            A[a, b] = sy.simplify((site_c[b] * Y).trace() / 2)
    return sy.simplify(lam * (2 - sy.re(sy.simplify(A.trace())))), A


def check_inst(name, Ks, expect=None):
    # completeness
    S = sy.zeros(4, 4)
    for K4 in Ks:
        S += K4.H * K4
    comp = sy.simplify(S - sy.eye(4)) == sy.zeros(4, 4)
    # even (parity-block-diagonal) Kraus
    par = sy.diag(1, -1, -1, 1)
    even = all(sy.simplify(par * K4 - K4 * par) == sy.zeros(4, 4) for K4 in Ks)
    d = direct_cost(Ks)
    f, A = formula_cost(Ks)
    good = comp and even and sy.simplify(d - f) == 0 and (expect is None or sy.simplify(d - expect) == 0)
    ok(name, good, f"direct={d} formula={f}")
    return d


def proj(vecs):
    M = sy.Matrix.hstack(*vecs)
    return sy.simplify(M * (M.H * M).inv() * M.H)


e4 = [sy.Matrix([1 if i == j else 0 for i in range(4)]) for j in range(4)]  # |00>,|01>,|10>,|11>
n_u = proj([e4[2], e4[3]])
Id4 = sy.eye(4)
check_inst("B1 exact: one coin-mode occupation record n_u costs lam", [Id4 - n_u, n_u], 1)
Pf = [proj([e4[j]]) for j in range(4)]
check_inst("B2 exact: complete rank-one lock of the site (4 outcomes) costs 2 lam", Pf, 2)
check_inst("B3 exact: fermion-parity record of the site costs 2 lam",
           [proj([e4[0], e4[3]]), proj([e4[1], e4[2]])], 2)
v_e = sy.Matrix([1, 1 + 2 * I_, 0, 0])
check_inst("B4 exact: vacuum-vs-rest projector (1,0) costs lam", [proj([e4[0]]), Id4 - proj([e4[0]])], 1)
ve = sy.Matrix([2, 0, 0, 1 - I_])
vo = sy.Matrix([0, 1 + I_, 3, 0])
Pe = proj([ve])
Po = proj([vo])
check_inst("B5 exact: Bogoliubov-type (1,1) projector with Gaussian-rational vectors costs lam",
           [Pe + Po, Id4 - Pe - Po], 1)
Ie = proj([e4[0], e4[3]])
Io = proj([e4[1], e4[2]])
check_inst("B6 exact: (1,2) type projector costs lam", [Pe + Io, Id4 - Pe - Io], 1)
check_inst("B7 exact: 3-outcome sharp partition (1,1)+(1,0)+(0,1) costs 3/2 lam",
           [Pe + Po, Ie - Pe, Io - Po], Rat(3, 2))
# weak QND instrument with Pythagorean pairs: coherence factor c = 24/25 -> cost lam (1 - c) = 1/25
nf = n_u
Kp = Rat(3, 5) * (Id4 - nf) + Rat(4, 5) * nf
Km = Rat(4, 5) * (Id4 - nf) + Rat(3, 5) * nf
check_inst("B8 exact: weak QND instrument with c=24/25 costs lam(1-c)=1/25", [Kp, Km], Rat(1, 25))


# random exact even instruments from Gaussian-rational unitaries (Cayley transform)
def cayley(n, rng):
    S = sy.zeros(n, n)
    for i in range(n):
        for j in range(i, n):
            re_, im_ = (int(x) for x in rng.integers(-3, 4, 2))
            S[i, j] = Rat(re_, 2) + I_ * Rat(im_, 3) if i != j else I_ * Rat(re_, 2)
            if i != j:
                S[j, i] = -sy.conjugate(S[i, j])
    return ((sy.eye(n) - S) * (sy.eye(n) + S).inv()).applyfunc(sy.simplify)


def random_even_instrument(rng, m=2):
    Ks = [sy.zeros(4, 4) for _ in range(m)]
    for idx in ([0, 3], [1, 2]):
        U = cayley(2 * m, rng)
        V = U[:, 0:2]
        for y in range(m):
            blk = V[2 * y:2 * y + 2, :]
            for r, ri in enumerate(idx):
                for c, ci in enumerate(idx):
                    Ks[y][ri, ci] = blk[r, c]
    return Ks


rng = np.random.default_rng(11)
for t in range(2):
    check_inst(f"B9.{t} exact: random even CP instrument (Q(i) entries) obeys cost = lam(2 - Re Tr A)",
               random_even_instrument(rng, 2))

# ledger with a pointer qubit (exact): impulsive controlled rotation, pointer gap omega
sy_pauli = sy.Matrix([[0, -I_], [I_, 0]])
cth, sth = Rat(5, 13), Rat(12, 13)
om = Rat(1, 3)
Rot = cth * sy.eye(2) - I_ * sth * sy_pauli
nf16 = embed(nf)
U32 = sy.kronecker_product(sy.eye(16) - nf16, sy.eye(2)) + sy.kronecker_product(nf16, Rot)
HA = sy.Matrix([[0, 0], [0, 1]])
Htot0 = sy.kronecker_product(H, sy.eye(2)) + om * sy.kronecker_product(sy.eye(16), HA)
psi0 = sy.kronecker_product(g, sy.Matrix([1, 0]))
psi1 = U32 * psi0
W = sy.simplify((psi1.H * Htot0 * psi1)[0] - (psi0.H * Htot0 * psi0)[0])
pocc = sy.simplify((g.H * nf16 * g)[0])
ok("C1 exact: <n_f> = 1/2 for a coin mode", pocc == Rat(1, 2))
ok("C2 exact: impulsive pointer coupling ledger W = lam(1-cos th) + omega p sin^2 th",
   sy.simplify(W - ((1 - cth) * 1 + om * pocc * sth ** 2)) == 0, f"W={W}")
ok("C3 exact: system part = dephasing part lam(1-cos th) and pointer part = omega p sin^2 th (split)",
   sy.simplify((psi1.H * sy.kronecker_product(H, sy.eye(2)) * psi1)[0] - E0 - (1 - cth)) == 0)

# ---------------------------------------------------------------------------------------------
# Part B.  Sharp floor: combinatorics of parity-block rank patterns (exact enumeration).
# ---------------------------------------------------------------------------------------------
parts = [(a, b) for a in range(3) for b in range(3) if (a, b) != (0, 0)]


def partitions_into(parts_left, target, cur, out):
    if target == (0, 0):
        out.append(tuple(cur))
        return
    for i, p in enumerate(parts_left):
        if p[0] <= target[0] and p[1] <= target[1]:
            cur.append(p)
            partitions_into(parts_left[i:], (target[0] - p[0], target[1] - p[1]), cur, out)
            cur.pop()


allp = []
partitions_into(parts, (2, 2), [], allp)
vals = {}
for pt in allp:
    s = sum(a * b for a, b in pt)
    vals.setdefault(len(pt), set()).add(s)
sums_nontriv = {sum(a * b for a, b in pt) for pt in allp if len(pt) >= 2}
sums_triv = {sum(a * b for a, b in pt) for pt in allp if len(pt) == 1}
ok("D1 exact: trivial instrument (one projector, rank pattern (2,2)) has sum r_e r_o = 4 (cost 0)",
   sums_triv == {4})
ok("D2 exact: every nontrivial sharp partition has sum r_e r_o in {0,1,2}, max 2 (cost >= lam)",
   sums_nontriv == {0, 1, 2}, f"values={sorted(sums_nontriv)} over {len(allp)} partitions")
ratio_ok = True
for pt in allp:
    if len(pt) < 2:
        continue
    cost = Fraction(4 - sum(a * b for a, b in pt), 2)
    q = [Fraction(a + b, 4) for a, b in pt]
    Hq = -sum(float(x) * np.log2(float(x)) for x in q)
    ratio_ok &= float(cost) >= Hq - 1e-12
ok("D3 checked: for every sharp partition cost/lam >= outcome entropy in bits (cost per bit >= lam)", ratio_ok)

# Majorana identity: sum_k g_k M g_k = (-1)^d (4-2d) M on all 16 monomials (exact integer matrices)
Zm = np.diag([1, -1])
am = np.array([[0, 1], [0, 0]])
c0n = np.kron(am, np.eye(2))
c1n = np.kron(Zm, am)
gam = [c0n + c0n.T, -1j * (c0n - c0n.T), c1n + c1n.T, -1j * (c1n - c1n.T)]
good = True
for subset in itertools.chain.from_iterable(itertools.combinations(range(4), r) for r in range(5)):
    M = np.eye(4, dtype=complex)
    for k in subset:
        M = M @ gam[k]
    S = sum(gk @ M @ gk for gk in gam)
    d = len(subset)
    good &= np.allclose(S, (-1) ** d * (4 - 2 * d) * M)
ok("D4 exact: sum_k gamma_k M gamma_k = (-1)^d (4-2d) M for all 16 Majorana monomials", good)

# TrR = sum_i r_e r_o for random parity-block-diagonal projective partitions
rng2 = np.random.default_rng(3)


good = True
for pt in allp:
    if len(pt) < 2 or len(pt) > 4:
        continue
    # common orthonormal frames per parity block
    frames = {}
    for key, idx in (("e", [0, 3]), ("o", [1, 2])):
        M = rng2.normal(size=(2, 2)) + 1j * rng2.normal(size=(2, 2))
        frames[key] = np.linalg.qr(M)[0]
    pe = po = 0
    Ps = []
    for (a, b) in pt:
        P = np.zeros((4, 4), complex)
        if a:
            F = frames["e"][:, pe:pe + a]
            P[np.ix_([0, 3], [0, 3])] = F @ F.conj().T
        if b:
            F = frames["o"][:, po:po + b]
            P[np.ix_([1, 2], [1, 2])] = F @ F.conj().T
        pe += a
        po += b
        Ps.append(P)
    TrR = sum(np.trace(gk @ sum(P @ gk @ P for P in Ps)).real for gk in gam) / 4
    good &= abs(TrR - sum(a * b for a, b in pt)) < 1e-12
ok("D5 checked: (1/4) sum_k Tr[gamma_k Phi*(gamma_k)] = sum_i r_e^i r_o^i for all rank patterns", good)

# ---------------------------------------------------------------------------------------------
# Part C.  Full Fock-space exact diagonalisation on rings (independent of any Gaussian formula).
# ---------------------------------------------------------------------------------------------
sxn = np.array([[0, 1], [1, 0]], complex)


def ring_h(L):
    h = np.zeros((2 * L, 2 * L), complex)
    for x in range(L):
        y = (x + 1) % L
        sgn = -1 if x == L - 1 else 1
        blk = sgn * sxn / (2j)
        h[2 * x:2 * x + 2, 2 * y:2 * y + 2] += blk
        h[2 * y:2 * y + 2, 2 * x:2 * x + 2] += blk.conj().T
    return h


def jw_sparse(n):
    I2 = sp.identity(2, format="csr")
    Z = sp.csr_matrix(np.diag([1.0, -1.0]))
    a = sp.csr_matrix(np.array([[0, 1.0], [0, 0]]))
    out = []
    for k in range(n):
        ms = [Z] * k + [a] + [I2] * (n - k - 1)
        m = ms[0]
        for o in ms[1:]:
            m = sp.kron(m, o, format="csr")
        out.append(m)
    return out


def fock_H(h, cs_):
    n = len(cs_)
    Hm = sp.csr_matrix((cs_[0].shape[0], cs_[0].shape[0]), dtype=complex)
    for i in range(n):
        for j in range(n):
            if abs(h[i, j]) > 1e-14:
                Hm = Hm + h[i, j] * (cs_[i].T @ cs_[j])
    return Hm.tocsr()


def rand_even_kraus(rng, m):
    def norm(Ms):
        S = sum(M.conj().T @ M for M in Ms)
        w_, U_ = np.linalg.eigh(S)
        Si = U_ @ np.diag(w_ ** -0.5) @ U_.conj().T
        return [M @ Si for M in Ms]

    Me = norm([rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)) for _ in range(m)])
    Mo = norm([rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)) for _ in range(m)])
    Ks = []
    for e, o in zip(Me, Mo):
        K = np.zeros((4, 4), complex)
        K[np.ix_([0, 3], [0, 3])] = e
        K[np.ix_([1, 2], [1, 2])] = o
        Ks.append(K)
    return Ks


c0f = np.kron(am, np.eye(2))
c1f = np.kron(Zm, am)
site_cn = [c0f.astype(complex), c1f.astype(complex)]


def formula_np(Ks, lam):
    A = np.zeros((2, 2), complex)
    for a in range(2):
        Y = sum(K.conj().T @ site_cn[a].T @ K for K in Ks)
        for b in range(2):
            A[a, b] = np.trace(site_cn[b] @ Y) / 2
    return lam * (2 - np.trace(A).real)


for L in (4, 6):
    n = 2 * L
    h = ring_h(L)
    cs_ = jw_sparse(n)
    Hm = fock_H(h, cs_)
    if L == 4:
        ev, V = np.linalg.eigh(Hm.toarray())
        g0 = V[:, 0]
        E0n = ev[0]
        gap = ev[1] - ev[0]
    else:
        ev, V = sla.eigsh(Hm, k=3, which="SA")
        o = np.argsort(ev)
        ev, V = ev[o], V[:, o]
        g0, E0n, gap = V[:, 0], ev[0], ev[1] - ev[0]
    lam = np.mean(np.abs(np.sin(2 * np.pi * (np.arange(L) + 0.5) / L)))
    ok(f"E{L}.1 checked: ring L={L} ground state nondegenerate, E0 = -L lam", gap > 1e-3 and abs(E0n + L * lam) < 1e-9,
       f"gap={gap:.4f} lam={lam:.6f}")
    rest = 2 ** (n - 2)
    rng3 = np.random.default_rng(100 + L)
    maxdev = 0.0
    maxneg = 1.0
    for trial in range(8):
        Ks = rand_even_kraus(rng3, int(rng3.integers(1, 5)))
        Kb = [sp.kron(sp.csr_matrix(K), sp.identity(rest), format="csr") for K in Ks]
        EH = sum((K.conj().T @ Hm @ K) @ g0 for K in Kb)
        dE = (g0.conj() @ EH).real - E0n
        pred = formula_np(Ks, lam)
        maxdev = max(maxdev, abs(dE - pred))
        maxneg = min(maxneg, dE)
    ok(f"E{L}.2 checked: random even CP site instruments, cost = lam(2-Re Tr A), max dev {maxdev:.1e}",
       maxdev < 1e-9 and maxneg > -1e-9)
    # sharp values on ED
    nfm = (cs_[0].T @ cs_[0]).tocsr()
    nfm1 = (cs_[1].T @ cs_[1]).tocsr()
    Id = sp.identity(2 ** n, format="csr")
    Hg = Hm @ g0
    def pinch_cost(Ps):
        return sum((g0.conj() @ (P @ (Hm @ (P @ g0)))).real for P in Ps) - E0n
    c_mode = pinch_cost([Id - nfm, nfm])
    Pl = [(Id - nfm) @ (Id - nfm1), (Id - nfm) @ nfm1, nfm @ (Id - nfm1), nfm @ nfm1]
    c_lock = pinch_cost(Pl)
    ok(f"E{L}.3 checked: mode record costs lam, complete site lock costs 2 lam on full Fock space",
       abs(c_mode - lam) < 1e-9 and abs(c_lock - 2 * lam) < 1e-9, f"{c_mode:.6f} {c_lock:.6f}")
    if L == 6:
        # additivity of records at graph distance >= 2 and failure at distance 1 (mode records)
        def mode_n(j):
            return (cs_[j].T @ cs_[j]).tocsr()
        def seq_cost(js):
            v = g0.copy()
            rho_E = None
            # mean post state after sequential pinchings = apply channel to |g0><g0|; do on density matrix of small rank via Kraus products
            # energy of channel composition: E = sum over outcome strings of <g0|P...H...P|g0>
            tot = 0.0
            for bits in itertools.product([0, 1], repeat=len(js)):
                Pprod = Id
                for j, bt in zip(js, bits):
                    Nj = mode_n(j)
                    Pprod = (Nj if bt else (Id - Nj)) @ Pprod
                w = Pprod @ g0
                tot += (w.conj() @ (Hm @ w)).real
            return tot - E0n
        a_ = seq_cost([0])
        b_ = seq_cost([6])
        ab_far = seq_cost([0, 6])
        c_ = seq_cost([3])
        ac_near = seq_cost([0, 3])
        ok("E6.4 checked: records at sites 0 and 3 (distance 3) cost exactly the sum",
           abs(ab_far - a_ - b_) < 1e-9, f"{ab_far:.6f} vs {a_ + b_:.6f}")
        ok("E6.5 checked: records on modes 0 and 3 of adjacent sites 0 and 1 (they share the hop h_03) are NOT additive",
           abs(ac_near - a_ - c_) > 1e-3, f"{ac_near:.6f} vs {a_ + c_:.6f}")

# ---------------------------------------------------------------------------------------------
# Part D.  3D walker sea (antiperiodic torus L=8): Gaussian 3-mode reductions (own code).
# ---------------------------------------------------------------------------------------------
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]


def build3d(Ls):
    N = Ls ** 3
    idx = lambda x, y, z: ((x % Ls) * Ls + (y % Ls)) * Ls + (z % Ls)
    hh = np.zeros((2 * N, 2 * N), complex)
    for x in range(Ls):
        for y in range(Ls):
            for z in range(Ls):
                i = idx(x, y, z)
                for j in range(3):
                    r = [x, y, z]
                    r[j] += 1
                    sgn = -1 if r[j] == Ls else 1
                    k = idx(*r)
                    blk = sgn * sig[j] / 2j
                    hh[2 * i:2 * i + 2, 2 * k:2 * k + 2] += blk
                    hh[2 * k:2 * k + 2, 2 * i:2 * i + 2] += blk.conj().T
    return hh, idx


Ls = 8
h3, idx3 = build3d(Ls)
w3, v3 = np.linalg.eigh(h3)
Pm = v3[:, w3 < 0] @ v3[:, w3 < 0].conj().T
G3 = Pm.T.copy()  # <c_i^+ c_j>
lam3 = -w3[w3 < 0].sum() / Ls ** 3
ok("F1 checked: 3D lam = <|s|> on 8^3 antiperiodic torus (old value 2.389890/2)", abs(2 * lam3 - 2.389890) < 2e-6,
   f"lam={lam3:.6f}")
ok("F2 checked: 3D site block of <c^+c> = 1/2 identity and (h P_-)_xx = -(lam/2) identity",
   np.allclose(G3[0:2, 0:2], 0.5 * np.eye(2)) and np.allclose((h3 @ Pm)[0:2, 0:2], -lam3 / 2 * np.eye(2), atol=1e-10))
cs3 = [m.toarray() for m in jw_sparse(3)]


def rho_gauss(Gm):
    lam_, U = np.linalg.eigh(Gm)
    d = [sum(U[j, k] * cs3[j] for j in range(3)) for k in range(3)]
    rho = np.eye(8, dtype=complex)
    for k in range(3):
        nk = d[k].conj().T @ d[k]
        rho = rho @ ((1 - lam_[k]) * (np.eye(8) - nk) + lam_[k] * nk)
    return rho


nbs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
terms = []
for d_ in nbs:
    y = idx3(*d_)
    for b in range(2):
        m = 2 * y + b
        rho3 = rho_gauss(G3[np.ix_([0, 1, m], [0, 1, m])])
        O = sum(h3[a, m] * cs3[a].conj().T @ cs3[2] + h3[m, a] * cs3[2].conj().T @ cs3[a] for a in (0, 1))
        terms.append((rho3, O))


def cost3(Ks):
    tot = 0.0
    Kb = [np.kron(K, np.eye(2)) for K in Ks]
    for rho3, O in terms:
        tot += np.trace(rho3 @ (sum(K.conj().T @ O @ K for K in Kb) - O)).real
    return tot


rng4 = np.random.default_rng(21)
dev = 0.0
for t in range(10):
    Ks = rand_even_kraus(rng4, int(rng4.integers(1, 5)))
    dev = max(dev, abs(cost3(Ks) - formula_np(Ks, lam3)))
ok("F3 checked: 3D (Wick 3-mode reductions) random even CP instruments obey cost = lam(2-Re Tr A)", dev < 1e-9,
   f"max dev {dev:.1e}")
dev = 0.0
vals3 = []
for t in range(40):
    # random sharp parity-block partitions with two or more outcomes
    pt = [p for p in allp if len(p) >= 2][int(rng4.integers(0, len([p for p in allp if len(p) >= 2])))]
    frames = {k: np.linalg.qr(rng4.normal(size=(2, 2)) + 1j * rng4.normal(size=(2, 2)))[0] for k in "eo"}
    pe = po = 0
    Ps = []
    for (a, b) in pt:
        P = np.zeros((4, 4), complex)
        if a:
            F = frames["e"][:, pe:pe + a]
            P[np.ix_([0, 3], [0, 3])] = F @ F.conj().T
        if b:
            F = frames["o"][:, po:po + b]
            P[np.ix_([1, 2], [1, 2])] = F @ F.conj().T
        pe += a
        po += b
        Ps.append(P)
    c = cost3(Ps)
    vals3.append(c)
    dev = max(dev, abs(c - lam3 * (4 - sum(a * b for a, b in pt)) / 2))
ok("F4 checked: 3D sharp site-local instruments cost lam(4-sum r_e r_o)/2; minimum nontrivial = lam = 1.1949",
   dev < 1e-9 and min(vals3) > lam3 - 1e-9, f"min over 40 random sharp partitions={min(vals3):.6f}")

# stored / released split for a held (locked) coin mode, and for the complete site lock, 3D 8^3
Ncur = h3.shape[0]
Nf = Ncur // 2
E0_3 = w3[w3 < 0].sum()
def gs_comp(drop, nocc):
    keep = [i for i in range(Ncur) if i not in drop]
    ev_ = np.linalg.eigvalsh(h3[np.ix_(keep, keep)])
    return ev_[:nocc].sum()
stored_mode = [gs_comp([0], Nf - o) - E0_3 for o in (0, 1)]
stored_site = [gs_comp([0, 1], Nf - o) - E0_3 for o in (0, 1, 2)]
ok("F5 checked: held mode record: stored defect energy same for both outcomes; released share ~ 3 %",
   abs(stored_mode[0] - stored_mode[1]) < 1e-9 and 0.02 < 1 - stored_mode[0] / lam3 < 0.05,
   f"stored={stored_mode[0]:.4f} of {lam3:.4f}, released={lam3 - stored_mode[0]:.4f}")
ok("F6 checked: held complete site lock (8^3): stored fraction 0.97 (source quotes 0.96 at 12^3)",
   abs(stored_site[0] - stored_site[2]) < 1e-9 and 0.95 < stored_site[0] / (2 * lam3) < 0.985,
   f"stored={stored_site[0]:.4f} of {2 * lam3:.4f}")

# ---------------------------------------------------------------------------------------------
# Part E.  Classical-information criterion for the QND class.
# ---------------------------------------------------------------------------------------------
u = sy.symbols("u", positive=True)
beta = sy.symbols("beta", positive=True)
q = (1 - sy.sqrt(1 - beta ** 2)) / 2
hnat = -q * sy.log(q) - (1 - q) * sy.log(1 - q)
h1 = sy.diff(hnat, beta)
h2d = sy.diff(hnat, beta, 2)
good1 = good2 = True
mp.mp.dps = 30
for bv in [Rat(1, 10), Rat(1, 3), Rat(1, 2), Rat(7, 10), Rat(9, 10), Rat(99, 100)]:
    uv = sy.sqrt(1 - bv ** 2)
    v1 = h1.subs(beta, bv).evalf(25)
    f1 = (bv * sy.atanh(uv) / uv).evalf(25)
    good1 &= abs(v1 - f1) < 1e-15
    v2 = h2d.subs(beta, bv).evalf(25)
    closed = ((sy.atanh(uv) - uv) / uv ** 3).evalf(25)
    good2 &= abs(v2 - closed) < 1e-12 and closed > 0
ok("G1 exact/checked: h'(beta) = beta artanh(u)/u with u=sqrt(1-beta^2) (h = binary entropy of (1-u)/2, nats)", good1)
ok("G2 checked: h''(beta) = (artanh u - u)/u^3 = sum_{m>=0} u^{2m}/(2m+3) > 0, so h is convex on (0,1)", good2)
mm = sy.symbols("m", integer=True, nonnegative=True)
ok("G3 exact: coefficient identity for h''", sy.simplify(1 / (2 * mm + 1) - 2 * (mm + 1) / (2 * mm + 3)
                                                         + 2 * mm / (2 * mm + 1) - 1 / (2 * mm + 3)) == 0)


def Istar(bc):
    # information bound: 1 - H2((1+sqrt(1-bc^2))/2)  [bits]
    return 1 - H2((1 + np.sqrt(max(0.0, 1 - bc ** 2))) / 2)


def mutual_info(P0, P1):
    P0 = np.asarray(P0)
    P1 = np.asarray(P1)
    pm = (P0 + P1) / 2
    I = 0.0
    for p, pmi in ((P0, pm), (P1, pm)):
        mask = p > 0
        I += 0.5 * np.sum(p[mask] * np.log2(p[mask] / pmi[mask]))
    return I


rng5 = np.random.default_rng(77)
worst = -1.0
tight = 0.0
for t in range(30000):
    m = int(rng5.integers(2, 7))
    P0 = rng5.dirichlet(np.ones(m) * rng5.choice([0.2, 1.0, 5.0]))
    P1 = rng5.dirichlet(np.ones(m) * rng5.choice([0.2, 1.0, 5.0]))
    if rng5.random() < 0.3:
        P1 = 0.6 * P0 + 0.4 * P1
    bc = np.sum(np.sqrt(P0 * P1))
    worst = max(worst, mutual_info(P0, P1) - Istar(bc))
for e in np.linspace(0.01, 0.99, 50):
    P0 = np.array([(1 + e) / 2, (1 - e) / 2])
    P1 = P0[::-1]
    tight = max(tight, abs(mutual_info(P0, P1) - Istar(np.sum(np.sqrt(P0 * P1)))))
ok("G4 checked: I(n;Y) <= 1 - H2((1+sqrt(1-BC^2))/2) over 30000 random classical channel pairs; max excess "
   f"{worst:.2e}", worst < 1e-12)
ok("G5 checked: the bound is attained by the symmetric binary channel", tight < 1e-12, f"max gap {tight:.1e}")

# pure pointer qubit: accessible information over projective readouts
def pointer_info(theta):
    p0 = np.array([1.0, 0.0])
    p1 = np.array([np.cos(theta), np.sin(theta)])
    best = 0.0
    for ph in np.linspace(0, np.pi, 721):
        v = np.array([np.cos(ph / 2), np.sin(ph / 2)])
        w_ = np.array([-np.sin(ph / 2), np.cos(ph / 2)])
        P0 = np.array([(v @ p0) ** 2, (w_ @ p0) ** 2])
        P1 = np.array([(v @ p1) ** 2, (w_ @ p1) ** 2])
        best = max(best, mutual_info(P0, P1))
    return best


good = True
for th in (0.2, 0.5, 0.9, 1.2, np.pi / 2):
    good &= abs(pointer_info(th) - (1 - H2((1 - np.sin(th)) / 2))) < 1e-5
ok("G6 checked: pure pointer qubit with overlap cos(th): best readout information = 1 - H2((1-sin th)/2)", good)

lam_ref = lam3


def eps_of_I(I):
    lo, hi = 1e-12, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if 1 - H2((1 - mid) / 2) < I:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def cost_front(I, lam):
    e = eps_of_I(I)
    return lam * (1 - np.sqrt(1 - e ** 2))


Is = np.linspace(0.001, 0.999, 400)
ratio = np.array([cost_front(I, 1.0) / I for I in Is])
ok("H1 checked: QND frontier cost(I)/lam rises from ln 2 (I->0) to 1 (I=1 bit): cost >= ln2 * lam * I; sharp copy is "
   "the most expensive way per bit", ratio.min() > np.log(2) - 5e-3 and np.all(np.diff(ratio) > -1e-9)
   and abs(cost_front(1 - 1e-12, 1.0) - 1) < 1e-4,
   f"min ratio {ratio.min():.4f} (ln2={np.log(2):.4f})")
rows = []
for I in (0.1, 0.5, 0.9, 0.99, 0.999):
    rows.append((I, cost_front(I, 1.0)))
ok("H2 checked: reliable pointer needs nearly the full price", rows[3][1] > 0.7 and rows[4][1] > 0.85 and rows[0][1] < 0.1,
   "cost/lam at I=0.1,0.5,0.9,0.99,0.999: " + ", ".join(f"{c:.4f}" for _, c in rows))
print(f"INFO 3D prices in units of t: weak-limit floor ln2*lam={np.log(2) * lam3:.4f} per bit, sharp mode record "
      f"lam={lam3:.4f}, complete lock {2 * lam3:.4f}")

# finite-time coherent coupling on the L=4 ring with a pointer qubit
L = 4
n = 2 * L
h4 = ring_h(L)
cs4 = jw_sparse(n)
H4 = fock_H(h4, cs4).toarray()
ev4, V4 = np.linalg.eigh(H4)
g4 = V4[:, 0]
E04 = ev4[0]
lam4 = np.mean(np.abs(np.sin(2 * np.pi * (np.arange(L) + 0.5) / L)))
nf4 = (cs4[0].T @ cs4[0]).toarray()
d4 = 2 ** n
syn = np.array([[0, -1j], [1j, 0]])
szn = np.diag([1.0, -1.0])
sxn_ = np.array([[0, 1], [1, 0]], complex)
I2n = np.eye(2)
Hs4 = np.kron(H4, I2n)


def pulse(gc, theta, omega):
    tau = theta / gc
    HA_ = omega * np.kron(np.eye(d4), np.diag([0.0, 1.0]))
    V_ = np.kron(nf4, syn)
    Ht = Hs4 + HA_ + gc * V_
    psi0 = np.kron(g4, np.array([1.0, 0.0], complex))
    psi = sl.expm(-1j * Ht * tau) @ psi0
    Eb0 = (psi0.conj() @ (Hs4 + HA_) @ psi0).real
    Eb1 = (psi.conj() @ (Hs4 + HA_) @ psi).real
    Wk = Eb1 - Eb0
    Vx = (psi.conj() @ V_ @ psi).real
    M = psi.reshape(d4, 2)
    sg = []
    for a_ in range(2):
        Pa = (np.eye(d4) - nf4) if a_ == 0 else nf4
        Ma = Pa @ M
        sg.append(Ma.T @ Ma.conj())
    best = 0.0
    for ph in np.linspace(0, np.pi, 91):
        for ch in np.linspace(0, 2 * np.pi, 181):
            nv = np.array([np.sin(ph) * np.cos(ch), np.sin(ph) * np.sin(ch), np.cos(ph)])
            Mm = nv[0] * sxn_ + nv[1] * syn + nv[2] * szn
            Pp = [(I2n + Mm) / 2, (I2n - Mm) / 2]
            J = np.array([[np.trace(sg[a_] @ Pp[b_]).real for b_ in range(2)] for a_ in range(2)])
            J = np.clip(J, 1e-300, None)
            pa = J.sum(1)
            pb = J.sum(0)
            best = max(best, (J * np.log2(J / np.outer(pa, pb))).sum())
    return Wk, Vx, best, (psi.conj() @ Hs4 @ psi).real - E04


ident_ok = True
conv_ok = True
above_ok = True
details = []
for theta in (np.pi / 2, np.pi / 4):
    for omega in (0.0, 0.5):
        ideal = (1 - np.cos(theta)) * lam4 + omega * 0.5 * np.sin(theta) ** 2
        prevdev = None
        for gc in (1.0, 3.0, 10.0, 30.0):
            Wk, Vx, Irep, ES = pulse(gc, theta, omega)
            ident_ok &= abs(Wk + gc * Vx) < 1e-9
            dev_ = abs(Wk - ideal)
            if prevdev is not None:
                conv_ok &= dev_ < prevdev + 1e-12
            prevdev = dev_
            front = cost_front(min(Irep, 1 - 1e-12), lam4)
            above_ok &= (ES >= front - 1e-6)
            details.append((theta, omega, gc, Wk, ideal, Irep, ES, front))
ok("I1 checked: work done by a square coupling pulse = -g tau-end expectation of the coupling (energy bookkeeping)",
   ident_ok)
ok("I2 checked: finite-g work converges monotonically to the impulsive ledger (1-cos th) lam + omega p sin^2 th "
   "as g grows", conv_ok)
ok("I3 checked: system-side energy of finite-g pulses stays above the QND frontier evaluated at the measured "
   "reproducibility information (coherent back-action only adds)", above_ok)
w1 = [d for d in details if d[0] == np.pi / 2 and d[1] == 0.0]
print("INFO pulse table (theta=pi/2, omega=0): g, W, ideal, I_rep, front(I_rep):",
      "; ".join(f"g={d[2]:g} W={d[3]:.4f} ideal={d[4]:.4f} I={d[5]:.4f} front={d[7]:.4f}" for d in w1))

# ---------------------------------------------------------------------------------------------
# Part F.  An open law with a monotone record count (exact, sympy) and its energy ledger.
# ---------------------------------------------------------------------------------------------
cs2 = jw_sym(2)
Hs2 = Rat(1, 1) * (cs2[0].H * cs2[1] + cs2[1].H * cs2[0]) * Rat(3, 5) + Rat(1, 4) * (cs2[0].H * cs2[0] - cs2[1].H * cs2[1])
n_f2 = cs2[0].H * cs2[0]
kap = Rat(7, 5)
def ket3(i):
    v = sy.zeros(3, 1)
    v[i] = 1
    return v
J0 = sy.sqrt(kap) * sy.kronecker_product(sy.eye(4) - n_f2, ket3(1) * ket3(0).T)
J1 = sy.sqrt(kap) * sy.kronecker_product(n_f2, ket3(2) * ket3(0).T)
Pnull = sy.kronecker_product(sy.eye(4), ket3(0) * ket3(0).T)
Ncnt = sy.eye(12) - Pnull
HSfull = sy.kronecker_product(Hs2, sy.eye(3))


def adj(X):
    out = sy.zeros(12, 12)
    for J in (J0, J1):
        out += J.H * X * J - Rat(1, 2) * (J.H * J * X + X * J.H * J)
    return sy.simplify(out)


comm = sy.simplify(HSfull * Ncnt - Ncnt * HSfull)
ok("J1 exact: H_S commutes with the record counter N (pointer states empty/0/1; counter = 1 - P_empty)",
   comm == sy.zeros(12, 12))
ok("J2 exact: Lindbladian adjoint L*(N) = kappa P_empty >= 0: count is non-decreasing for EVERY state (open law)",
   sy.simplify(adj(Ncnt) - kap * Pnull) == sy.zeros(12, 12))
Pup = [sy.eye(4) - n_f2, n_f2]
PhiH = Pup[0] * Hs2 * Pup[0] + Pup[1] * Hs2 * Pup[1]
ok("J3 exact: energy injection rate L*(H_S) = kappa P_empty (x) (Phi*(H_S) - H_S): record formed once pays the "
   "dephasing cost, spread over the formation time 1/kappa",
   sy.simplify(adj(HSfull) - kap * sy.kronecker_product(PhiH - Hs2, ket3(0) * ket3(0).T)) == sy.zeros(12, 12))
# numerical integration from a random mixed state
Hn = np.array(Hs2.evalf(), dtype=complex)
J0n = np.array(J0.evalf(), dtype=complex)
J1n = np.array(J1.evalf(), dtype=complex)
Hfull = np.kron(Hn, np.eye(3))
d12 = 12
Ls_ = -1j * (np.kron(Hfull, np.eye(d12)) - np.kron(np.eye(d12), Hfull.T))
for J in (J0n, J1n):
    JdJ = J.conj().T @ J
    Ls_ += np.kron(J, J.conj()) - 0.5 * np.kron(JdJ, np.eye(d12)) - 0.5 * np.kron(np.eye(d12), JdJ.T)
rngp = np.random.default_rng(9)
Mr = rngp.normal(size=(4, 4)) + 1j * rngp.normal(size=(4, 4))
rhoS = Mr @ Mr.conj().T
rhoS /= np.trace(rhoS)
Nn = np.eye(12) - np.kron(np.eye(4), np.diag([1.0, 0, 0]))
PhiHn = np.array(PhiH.evalf(), dtype=complex)
Dn = PhiHn - Hn


def evolve_open(rhoS_, T):
    rho0_ = np.kron(rhoS_, np.diag([1.0, 0, 0]))
    return (sl.expm(Ls_ * T) @ rho0_.reshape(-1)).reshape(12, 12), rho0_


# (i) count monotone from a random mixed state
Ns = []
for tt in np.linspace(0, 6, 61):
    rt, r0_ = evolve_open(rhoS, tt)
    Ns.append(np.trace(Nn @ rt).real)
Ns = np.array(Ns)
# (ii) stationary (ground) state: total injected energy equals the T1 dephasing cost exactly
evS, VS = np.linalg.eigh(Hn)
gS = VS[:, 0]
rhoG = np.outer(gS, gS.conj())
rinf, r0_ = evolve_open(rhoG, 40.0)
dE_open = np.trace(Hfull @ rinf).real - np.trace(Hfull @ r0_).real
dE_pred = np.trace(rhoG @ Dn).real
# (iii) non-stationary state: cost is the exponentially time-averaged dephasing cost
rinf2, r02 = evolve_open(rhoS, 40.0)
dE_open2 = np.trace(Hfull @ rinf2).real - np.trace(Hfull @ r02).real
tg = np.linspace(0, 40, 8001)
avg = 0.0
vals_ = []
for tt in tg:
    U_ = sl.expm(-1j * Hn * tt)
    vals_.append(np.trace(U_ @ rhoS @ U_.conj().T @ Dn).real * 1.4 * np.exp(-1.4 * tt))
avg = np.trapezoid(vals_, tg)
ok("J4 checked: count rises monotonically to 1 as 1-exp(-kappa t) from a random mixed state",
   np.all(np.diff(Ns) > -1e-12) and abs(Ns[-1] - (1 - np.exp(-1.4 * 6))) < 1e-7, f"N(6)={Ns[-1]:.5f}")
ok("J5 checked: from the (stationary) ground state the total energy injected by the open law equals the dephasing "
   "cost Tr rho(Phi*(H)-H); from a non-stationary state it equals its exponentially time-averaged value",
   abs(dE_open - dE_pred) < 1e-8 and abs(dE_open2 - avg) < 1e-5,
   f"ground: {dE_open:.8f} vs {dE_pred:.8f}; mixed: {dE_open2:.6f} vs avg {avg:.6f}")

# ---------------------------------------------------------------------------------------------
# Part G.  Rate and accumulation accounting (exact scaling) and heat-budget arithmetic.
# ---------------------------------------------------------------------------------------------
t, t0, r, s = sy.symbols("t t0 r s", positive=True)
a_t = lambda x: x ** Rat(2, 3)  # matter era a ~ t^(2/3)
rad = sy.simplify(sy.integrate(a_t(s) ** 4 * r, (s, 0, t0)) / a_t(t0) ** 4)
mat = sy.simplify(sy.integrate(a_t(s) ** 3 * r, (s, 0, t0)) / a_t(t0) ** 3)
ok("K1 exact: constant proper-volume injection in the matter era leaves a fraction 3/11 (radiation-like, "
   "redshifts) or 1/3 (rest mass, dilutes) of the undiluted r t0",
   sy.simplify(rad - Rat(3, 11) * r * t0) == 0 and sy.simplify(mat - Rat(1, 3) * r * t0) == 0)
hbarc_eVm = 1.973269804e-7
eVJ = 1.602176634e-19
a_m = 1e-19
unit_J = hbarc_eVm / a_m * eVJ
P_earth = 7e-12
rate_full = P_earth / (lam3 * unit_J)
rate_lock = P_earth / ((lam3 - stored_mode[0]) * unit_J)
rate_lock_tot = P_earth / (2 * lam3 * unit_J)
ok("K3 checked (reference constants): at a=1e-19 m, 1.19 hop energies = 3.8e-7 J; Earth's heat 7e-12 W/kg allows "
   "~2e-5 fully-released records per kg per s; a held mode record releases only ~3 % so the heat bound loosens ~33x "
   "but the stored 97 % is rest mass, a separate budget",
   abs(lam3 * unit_J - 3.78e-7) < 5e-9 and 1.5e-5 < rate_full < 2.1e-5 and 25 < rate_lock / rate_full < 40,
   f"rate_full={rate_full:.2e} rate_held={rate_lock:.2e} complete-lock={rate_lock_tot:.2e}")
Ibits_rate = P_earth / (np.log(2) * lam3 * unit_J)
ok("K4 checked: QND records bound the information rate: bits per kg per s <= P / (ln2 lam hbar c/a) under the "
   "stated assumptions (distinct fresh sites >= 2 apart, additive cost, all cost released as heat)",
   Ibits_rate > rate_full, f"{Ibits_rate:.2e} bits/kg/s")

# ---------------------------------------------------------------------------------------------
print(f"INFO runtime {time.time() - T0:.1f} s")
if FAIL == 0:
    print("HIT: In the inversion-paired massless walker sea any parity-respecting site-supported record instrument "
          "costs exactly lam(2 - Re Tr A) (proved; Fock-checked), so every nontrivial SHARP site-local instrument "
          "costs at least lam = 1.19 t (equality for every binary type, 2.39 t for complete locks), while weak or "
          "collective instruments cost less: 1.19 is the exact floor of a stated sharp class, not a minimum over "
          "record laws; a reliable (I -> 1 bit) QND pointer pays lam(1 - BC*(I)) -> lam.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("SUMMARY: exact general site-instrument cost law cost = lam(2 - Re Tr A) in the maximally mixed walker sea, "
      "its exact sharp floor lam = 1.19 t, the weak/QND cost-information frontier, the pointer ledger with finite "
      "coupling, an open-law monotone count and rate/accumulation accounting; unproved: non-QND frontier, pointer "
      "lock cost, interacting/gapped vacua.")
sys.exit(0 if FAIL == 0 else 1)
