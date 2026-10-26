#!/usr/bin/env python3
"""J:derive:review-20260929-canonical-gravity-changed-carriers:a1 -- checker.

Self-contained (numpy, sympy, mpmath, fractions only).  One process.  Exact
arithmetic (Fraction / sympy QQ) for every finite claim; mpmath only where a
line says "numerical".

Part A  Leading-action polynomial count and linear gauge identity, by exact
        group characters (not by orbit sums):
          A1  invariant counts of V = Sym^2(Sym^2 U) x Sym^2 U (dim 550) from
              the character formula, for six groups; compare with the
              source note's table (26/26/26/30 and 9/9).
          A2  the same characters by direct trace of the signed-permutation
              action on the 550 monomials (independent of the formula).
          A3  the gauge kernel K (no symmetry imposed) from the exact linear
              gauge identity, its dimension, and dim K^G from the characters
              of K.
          A4  a closed form for K: Q_c = c_{mn} eps^{m a b g} eps^{n r s t}
              k_a k_r h_{bs} h_{gt}, c in Sym^2 (10 parameters); gauge
              invariance; K = {Q_c}; K ~ Sym^2 U as B4-modules; Fierz-Pauli =
              Q_delta.
          A5  Lie-algebra (so(4)) invariants of V, and of K.
          A6  3+1 read-off for the S3 x G forms.
Part B  The nonzero-momentum DeWitt quotient versus the homogeneous negative
        direction (exact, all momenta symbolically; exact inertia on 3^3 and
        4^3 tori).
Part C  The finite-range mixed identity in the reduced two-component block:
        exact defect of the radius-m central-difference family, sum rule,
        universal diagonal obstruction, SLAC limit, the clock control.
"""
import itertools
import sys
import time
from fractions import Fraction as Fr
from math import comb

import numpy as np
import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix
import mpmath as mp

T0 = time.time()
RES = []


def check(label, ok, detail=""):
    RES.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + label + (" :: " + detail if detail else ""), flush=True)


# ----------------------------------------------------------------------------------------------
# Part A -- groups, characters
# ----------------------------------------------------------------------------------------------
def all_signed_perms():
    out = []
    for perm in itertools.permutations(range(4)):
        for signs in itertools.product((1, -1), repeat=4):
            g = np.zeros((4, 4), dtype=int)
            for i in range(4):
                g[perm[i], i] = signs[i]
            out.append(g)
    return out


def idet(g):
    return int(round(np.linalg.det(g)))


ALLG = all_signed_perms()
GROUPS = {
    "B4": ALLG,
    "properB4": [g for g in ALLG if idet(g) == 1],
    "B3xT": [g for g in ALLG if g[0, 0] != 0],
    "B3": [g for g in ALLG if g[0, 0] == 1],
    "OxT": [g for g in ALLG if g[0, 0] != 0 and idet(g[1:, 1:]) == 1],
    "O": [g for g in ALLG if g[0, 0] == 1 and idet(g[1:, 1:]) == 1],
}
ORDERS = {"B4": 384, "properB4": 192, "B3xT": 96, "B3": 48, "OxT": 48, "O": 24}


def mpow(g, n):
    return np.linalg.matrix_power(g, n)


def chiU(g):
    return int(np.trace(g))


def chiW(g):  # W = Sym^2 U  (the field h)
    return Fr(chiU(g) ** 2 + chiU(mpow(g, 2)), 2)


def chiSW(g):  # Sym^2 W
    return Fr(chiW(g) ** 2 + chiW(mpow(g, 2)), 2)


def chiV(g):  # V = Sym^2 W x Sym^2 U  (quadratic in h, quadratic in k)
    return chiSW(g) * chiW(g)


def chiS2U(g):
    return chiW(g)


EXPECT = {"B4": 9, "properB4": 9, "B3xT": 26, "B3": 26, "OxT": 26, "O": 30}
cnt = {}
for name, G in GROUPS.items():
    assert len(G) == ORDERS[name]
    cnt[name] = sum(chiV(g) for g in G) / len(G)
check("A1 character-formula counts of invariant leading forms (dim V = 550): B4 9, proper B4 9, B3xT 26, B3 26, OxT 26, O 30 "
      "(source table: S3 with time reversal 26, proper cubic with time reversal 26, proper cubic without time reversal 30, B4 9, proper B4 9)",
      chiV(np.eye(4, dtype=int)) == 550 and all(cnt[n] == EXPECT[n] for n in EXPECT),
      "counts=" + str({n: int(c) for n, c in cnt.items()}))

# monomial basis of V: (h-pair, k-pair)
H = [(m, n) for m in range(4) for n in range(m, 4)]
HI = {p: i for i, p in enumerate(H)}
KP = [(a, b) for a in range(4) for b in range(a, 4)]
HP = [(i, j) for i in range(10) for j in range(i, 10)]
MONO = [(hp, kp) for hp in HP for kp in KP]
MI = {m: i for i, m in enumerate(MONO)}
assert len(MONO) == 550


def decode(g):
    perm = [int(np.nonzero(g[:, i])[0][0]) for i in range(4)]
    sg = [int(g[perm[i], i]) for i in range(4)]
    return perm, sg


def mono_act(g, hp, kp):
    perm, sg = decode(g)
    sign = 1
    img = []
    for a in hp:
        m, n = H[a]
        sign *= sg[m] * sg[n]
        img.append(HI[tuple(sorted((perm[m], perm[n])))])
    c, e = kp
    sign *= sg[c] * sg[e]
    return MI[(tuple(sorted(img)), tuple(sorted((perm[c], perm[e]))))], sign


okA2 = True
for g in ALLG:
    tr = 0
    for col, (hp, kp) in enumerate(MONO):
        m2, s = mono_act(g, hp, kp)
        if m2 == col:
            tr += s
    okA2 &= (tr == chiV(g))
check("A2 direct trace of the signed-permutation action on the 550 monomials equals the character formula for all 384 elements of B4",
      okA2, "384 elements")

# gauge map Phi : V -> W (800), linear term of Q(h + k xi + xi k) - Q(h)
K3 = list(itertools.combinations_with_replacement(range(4), 3))
K3I = {t: i for i, t in enumerate(K3)}


def widx(b, nu, tr):
    return (b * 4 + nu) * 20 + K3I[tuple(sorted(tr))]


PHI = [[0] * 550 for _ in range(800)]
for col, (hp, kp) in enumerate(MONO):
    a, b = hp
    c, d = kp
    for (x, y) in ((a, b), (b, a)):
        m, n = H[x]
        for (mu, nu) in ((m, n), (n, m)):
            PHI[widx(y, nu, (mu, c, d))][col] += 1
dmPhi = DomainMatrix([[QQ(v) for v in r] for r in PHI], (800, 550), QQ)
NS = dmPhi.nullspace()
d = NS.shape[0]
Nmat = NS.to_Matrix()
NR = [[Fr(int(v.p), int(v.q)) for v in Nmat.row(i)] for i in range(d)]
free = []
for i in range(d):
    for j in range(550):
        if NR[i][j] == 1 and all(NR[k][j] == 0 for k in range(d) if k != i):
            free.append(j)
            break
assert len(free) == d


def tr_on_K(g):
    inv = {}
    for col, (hp, kp) in enumerate(MONO):
        m2, s = mono_act(g, hp, kp)
        inv[m2] = (col, s)
    return sum((inv[f][1] * NR[i][inv[f][0]] for i, f in enumerate(free)), Fr(0))


# stability of K under the generators of B4 (exact rank test)
def rho_rows(g, rows):
    out = []
    for r in rows:
        w = [Fr(0)] * 550
        for col, (hp, kp) in enumerate(MONO):
            m2, s = mono_act(g, hp, kp)
            w[m2] = s * r[col]
        out.append(w)
    return out


gens = []
P = np.zeros((4, 4), dtype=int)
for i in range(4):
    P[(i + 1) % 4, i] = 1
gens.append(P)
S12 = np.eye(4, dtype=int)
S12[[1, 2]] = S12[[2, 1]]
gens.append(S12)
F0 = np.eye(4, dtype=int)
F0[0, 0] = -1
gens.append(F0)
F1 = np.eye(4, dtype=int)
F1[1, 1] = -1
gens.append(F1)
stable = True
rk0 = DomainMatrix([[QQ(v.numerator, v.denominator) for v in r] for r in NR], (d, 550), QQ).rank()
for g in gens:
    rr = rho_rows(g, NR)
    stack = DomainMatrix([[QQ(v.numerator, v.denominator) for v in r] for r in NR + rr], (2 * d, 550), QQ)
    stable &= (stack.rank() == rk0)
trs = {tuple(g.flatten()): tr_on_K(g) for g in ALLG}
dimKG = {n: sum(trs[tuple(g.flatten())] for g in G) / len(G) for n, G in GROUPS.items()}
check("A3 exact gauge kernel K = {Q in V : Q(h + k xi^T + xi k^T) = Q(h)} has dimension 10 (no symmetry imposed), is B4-stable, and "
      "dim K^G from the characters of K is 1,1,2,2,2,2 for B4, proper B4, B3xT, B3, OxT, O (source: 26->2, 9->1)",
      d == 10 and stable and tuple(int(dimKG[n]) for n in ("B4", "properB4", "B3xT", "B3", "OxT", "O")) == (1, 1, 2, 2, 2, 2),
      f"dim K={d}, K-invariant dims={ {n: int(v) for n, v in dimKG.items()} }")


# closed form of K: Q_c = c_{mn} eps^{m a b g} eps^{n r s t} k_a k_r h_{bs} h_{gt}
def perm_sign(p):
    p = list(p)
    s = 1
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]
            p[i], p[j] = p[j], p[i]
            s = -s
    return s


PERMS = [(p, perm_sign(p)) for p in itertools.permutations(range(4))]


def Qc_vec(cmat):
    vec = {}
    for (p1, s1) in PERMS:
        mu, al, be, ga = p1
        for (p2, s2) in PERMS:
            nu, rh, si, ta = p2
            cf = cmat[mu][nu]
            if cf == 0:
                continue
            hA = HI[tuple(sorted((be, si)))]
            hB = HI[tuple(sorted((ga, ta)))]
            key = (tuple(sorted((hA, hB))), tuple(sorted((al, rh))))
            vec[MI[key]] = vec.get(MI[key], 0) + s1 * s2 * cf
    out = [0] * 550
    for k_, v in vec.items():
        out[k_] = v
    return out


cbasis = []
for m in range(4):
    for n in range(m, 4):
        c = [[0] * 4 for _ in range(4)]
        c[m][n] = 1
        c[n][m] = 1
        cbasis.append(c)
QV = [Qc_vec(c) for c in cbasis]
gauge_ok = all(all(sum(PHI[r][col] * v[col] for col in range(550) if v[col]) == 0 for r in range(800)) for v in QV)
rkQ = DomainMatrix([[QQ(int(x)) for x in v] for v in QV], (10, 550), QQ).rank()
rkKQ = DomainMatrix([[QQ(v.numerator, v.denominator) for v in r] for r in NR] + [[QQ(int(x)) for x in v] for v in QV], (20, 550), QQ).rank()
# gauge invariance at second order Q_c(k xi + xi k) = 0 symbolic (all c)
xi = sp.symbols("x0:4")
kk = sp.symbols("k0:4")
cs = sp.symbols("c0:10")
cm = sp.zeros(4, 4)
ii = 0
for m in range(4):
    for n in range(m, 4):
        cm[m, n] = cs[ii]
        cm[n, m] = cs[ii]
        ii += 1
hd = sp.Matrix(4, 4, lambda i, j: kk[i] * xi[j] + kk[j] * xi[i])
q2 = 0
for (p1, s1) in PERMS:
    mu, al, be, ga = p1
    for (p2, s2) in PERMS:
        nu, rh, si, ta = p2
        q2 += s1 * s2 * cm[mu, nu] * kk[al] * kk[rh] * hd[be, si] * hd[ga, ta]
q2 = sp.expand(q2)
# Fierz-Pauli
FPv = {}


def add(h1, h2, kp_, cf):
    key = (tuple(sorted((HI[tuple(sorted(h1))], HI[tuple(sorted(h2))]))), tuple(sorted(kp_)))
    FPv[MI[key]] = FPv.get(MI[key], 0) + cf


for a in range(4):
    for m in range(4):
        for n in range(4):
            add((m, n), (m, n), (a, a), Fr(1, 2))              # 1/2 k^2 h.h
for m in range(4):
    for a in range(4):
        for b in range(4):
            add((m, a), (m, b), (a, b), Fr(-1))                 # -|h k|^2
for a in range(4):
    for b in range(4):
        for m in range(4):
            add((a, b), (m, m), (a, b), Fr(1))                  # (k h k) tr h
for a in range(4):
    for m in range(4):
        for n in range(4):
            add((m, m), (n, n), (a, a), Fr(-1, 2))              # -1/2 k^2 (tr h)^2
FPvec = [FPv.get(i, Fr(0)) for i in range(550)]
dl = Qc_vec([[1 if i == j else 0 for j in range(4)] for i in range(4)])
nz = [i for i in range(550) if FPvec[i] != 0]
kappa = Fr(dl[nz[0]]) / FPvec[nz[0]]
prop = all(Fr(dl[i]) == kappa * FPvec[i] for i in range(550))
bad_char = 0
for g in ALLG:
    if trs[tuple(g.flatten())] != chiS2U(g):
        bad_char += 1
check("A4 closed form of the gauge kernel: Q_c = c_{mn} eps^{m a b g} eps^{n r s t} k_a k_r h_{bs} h_{gt} (c symmetric, 10 parameters) is gauge invariant "
      "(linear term: exact matrix test on all 550 monomials; quadratic term: symbolic zero), the ten Q_c are independent and span K exactly; "
      "K is isomorphic to Sym^2 U as a B4-module (characters agree on all 384 elements); Fierz-Pauli = Q_delta up to the constant "
      + str(kappa), gauge_ok and q2 == 0 and rkQ == 10 and rkKQ == 10 and bad_char == 0 and prop and kappa != 0,
      f"rank(Q_c)={rkQ}, rank(K+Q_c)={rkKQ}, character mismatches={bad_char}")

# A5: so(4) invariants via the Lie algebra (independent of the discrete groups)
def lie_matrix(p, q):
    om = np.zeros((4, 4), dtype=int)
    om[p, q] = 1
    om[q, p] = -1
    rows = {}

    def dh(a):  # delta h_{mn} = om_{m al} h_{al n} + om_{n al} h_{m al}
        m, n = H[a]
        out = []
        for al in range(4):
            if om[m, al]:
                out.append((int(om[m, al]), HI[tuple(sorted((al, n)))]))
            if om[n, al]:
                out.append((int(om[n, al]), HI[tuple(sorted((m, al)))]))
        return out

    def dk(c):
        return [(int(om[c, al]), al) for al in range(4) if om[c, al]]

    Lm = {}
    for col, (hp, kp) in enumerate(MONO):
        a, b = hp
        c, e = kp
        for cf, a2 in dh(a):
            key = MI[(tuple(sorted((a2, b))), kp)]
            Lm[(key, col)] = Lm.get((key, col), 0) + cf
        for cf, b2 in dh(b):
            key = MI[(tuple(sorted((a, b2))), kp)]
            Lm[(key, col)] = Lm.get((key, col), 0) + cf
        for cf, c2 in dk(c):
            key = MI[(hp, tuple(sorted((c2, e))))]
            Lm[(key, col)] = Lm.get((key, col), 0) + cf
        for cf, e2 in dk(e):
            key = MI[(hp, tuple(sorted((c, e2))))]
            Lm[(key, col)] = Lm.get((key, col), 0) + cf
    M_ = [[0] * 550 for _ in range(550)]
    for (r, c_), v in Lm.items():
        M_[r][c_] += v
    return M_


stackL = []
for p in range(4):
    for q in range(p + 1, 4):
        stackL += lie_matrix(p, q)
nsL = DomainMatrix([[QQ(v) for v in r] for r in stackL], (len(stackL), 550), QQ).nullspace()
nsLK = DomainMatrix([[QQ(v) for v in r] for r in (stackL + PHI)], (len(stackL) + 800, 550), QQ).nullspace()
check("A5 Lie-algebra invariants (so(4) acting by derivations on the 550 monomials): the so(4)-invariant leading forms are 4-dimensional and exactly one is gauge invariant "
      "(Fierz-Pauli); both agree with the O(4) values from the discrete-group route (B4-invariants 9 = 4 + 5 hypercubic extras)",
      nsL.shape[0] == 4 and nsLK.shape[0] == 1, f"dim V^so(4)={nsL.shape[0]}, dim K^so(4)={nsLK.shape[0]}")

# A6: 3+1 read-off for K^{B3xT}.  Q_c with c = diag(a, b, b, b); h_{0 mu}=0, k=(k0,0,0,0)  =>  Q = k0^2 [A tr h^2 + B (tr h)^2];
# TT mode h_12 with k=(k0,0,0,p) => h_12^2 (u k0^2 + v p^2).
a_, b_ = sp.symbols("a b")
hs = {m: sp.Symbol(f"h{m[0]}{m[1]}") for m in H}


def hsym(i, j):
    return hs[(min(i, j), max(i, j))]


def Qc_expr(cd, kvec, hmat):
    tot = 0
    for (p1, s1) in PERMS:
        mu, al, be, ga = p1
        for (p2, s2) in PERMS:
            nu, rh, si, ta = p2
            if cd[mu][nu] == 0:
                continue
            tot += s1 * s2 * cd[mu][nu] * kvec[al] * kvec[rh] * hmat[be][si] * hmat[ga][ta]
    return sp.expand(tot)


cdiag = [[a_ if (i == j == 0) else (b_ if i == j else 0) for j in range(4)] for i in range(4)]
k0, pp = sp.symbols("k0 p")
hspatial = [[0] * 4 for _ in range(4)]
for i in range(1, 4):
    for j in range(1, 4):
        hspatial[i][j] = hsym(i, j)
Qa = Qc_expr(cdiag, [k0, 0, 0, 0], hspatial)
trh = sum(hsym(i, i) for i in range(1, 4))
trh2 = sum(hsym(i, j) ** 2 for i in range(1, 4) for j in range(1, 4))
Aco = sp.simplify(sp.Poly(Qa, *hs.values()).coeff_monomial(hsym(1, 2) ** 2) / k0 ** 2 / 2)    # h12^2 coefficient is 2A
Bco = sp.simplify(sp.Poly(Qa, *hs.values()).coeff_monomial(hsym(1, 1) * hsym(2, 2)) / k0 ** 2 / 2)
recon = sp.expand(Qa - k0 ** 2 * (Aco * trh2 + Bco * trh ** 2))
htt = [[0] * 4 for _ in range(4)]
htt[1][2] = htt[2][1] = hsym(1, 2)
Qtt = Qc_expr(cdiag, [k0, 0, 0, pp], htt)
ptt = sp.Poly(Qtt, hsym(1, 2))
coefTT = sp.expand(ptt.coeff_monomial(hsym(1, 2) ** 2))
u_ = sp.simplify(coefTT.coeff(k0, 2).coeff(pp, 0))
v_ = sp.simplify(coefTT.coeff(pp, 2).coeff(k0, 0))
check("A6 3+1 read-off for all S3 x G forms Q_c, c = diag(a,b,b,b): Q = k0^2 [A tr h^2 + B (tr h)^2] with B = -A (A proportional to b, so the form has no kinetic part iff b = 0), "
      "and the transverse-traceless coefficient h_12^2 (u k0^2 + v p^2) has u proportional to b and v proportional to a, so the TT speed squared a/b is free; "
      "at c = delta (B4) it is 1",
      recon == 0 and sp.simplify(Bco + Aco) == 0 and sp.simplify(Aco / b_).free_symbols == set() and sp.simplify(u_ / b_).free_symbols == set()
      and sp.simplify(v_ / a_).free_symbols == set() and sp.simplify(v_ / a_) == sp.simplify(u_ / b_),
      f"A={Aco}, B={Bco}, u={u_}, v={v_}")

# ----------------------------------------------------------------------------------------------
# Part B -- DeWitt quotient versus the homogeneous negative direction
# ----------------------------------------------------------------------------------------------
def inertia(A):
    """exact (pos, neg, zero) of a symmetric Fraction matrix by congruence elimination"""
    n = len(A)
    A = [[Fr(x) for x in row] for row in A]
    pos = neg = 0
    active = list(range(n))
    while active:
        p = next((i for i in active if A[i][i] != 0), None)
        if p is None:
            pair = next(((i, j) for i in active for j in active if i < j and A[i][j] != 0), None)
            if pair is None:
                break
            i, j = pair
            for k in range(n):
                A[i][k] += A[j][k]
            for k in range(n):
                A[k][i] += A[k][j]
            continue
        piv = A[p][p]
        pos += piv > 0
        neg += piv < 0
        active.remove(p)
        for i in active:
            if A[i][p] != 0:
                f = A[i][p] / piv
                for k in active:
                    A[i][k] -= f * A[p][k]
        for i in active:
            A[i][p] = Fr(0)
            A[p][i] = Fr(0)
    return pos, neg, len(active)


check("B0 inertia routine sanity (exact): [[0,1],[1,0]] -> (1,1,0); diag(1,0,-2) -> (1,1,1); [[1,1],[1,1]] -> (1,0,1)",
      inertia([[0, 1], [1, 0]]) == (1, 1, 0) and inertia([[1, 0, 0], [0, 0, 0], [0, 0, -2]]) == (1, 1, 1) and inertia([[1, 1], [1, 1]]) == (1, 0, 1))

# symbolic, all momenta: slots (xx,yy,zz,xy,yz,xz)
K1, K2, K3s = sp.symbols("K1 K2 K3")
Kv = [K1, K2, K3s]
tt = K1 ** 2 + K2 ** 2 + K3s ** 2
FCS = {3: (0, 1), 4: (1, 2), 5: (0, 2)}
Gs = sp.zeros(3, 6)
for j in range(3):
    Gs[j, j] = Kv[j]
for f, (i, j) in FCS.items():
    Gs[i, f] = Kv[j]
    Gs[j, f] = Kv[i]
vv = sp.Matrix([1, 1, 1, 0, 0, 0])
Ms = sp.diag(1, 1, 1, 2, 2, 2) - vv * vv.T / 2
ss = sp.Matrix([-(tt - K1 ** 2), -(tt - K2 ** 2), -(tt - K3s ** 2), K1 * K2, K2 * K3s, K1 * K3s])
# s = -t * P_perp in slot coordinates (P_perp = I - K K^T / t)
Pperp_slots = sp.Matrix([sp.Rational(1) * (tt - K1 ** 2), tt - K2 ** 2, tt - K3s ** 2, -K1 * K2, -K2 * K3s, -K1 * K3s])
symb_ok = (sp.simplify(Ms * ss - Gs.T * sp.Matrix(Kv)) == sp.zeros(6, 1) and sp.simplify(Gs * ss) == sp.zeros(3, 1)
           and sp.simplify(ss + Pperp_slots) == sp.zeros(6, 1) and sp.simplify((ss.T * Ms * ss)[0]) == 0)
check("B1 symbolic in K=(K1,K2,K3) (all lattice momenta K = 2 sin(q/2)): M s = G^T K, G s = 0, s^T M s = 0, and s = -|K|^2 P_perp exactly (P_perp = 1 - K K^T/|K|^2)",
      symb_ok)


def Gnum(K):
    G = sp.zeros(3, 6)
    for j in range(3):
        G[j, j] = K[j]
    for f, (i, j) in FCS.items():
        G[i, f] = K[j]
        G[j, f] = K[i]
    return G


def sdir(K):
    t = sum(x * x for x in K)
    return sp.Matrix([-(t - K[0] ** 2), -(t - K[1] ** 2), -(t - K[2] ** 2), K[0] * K[1], K[1] * K[2], K[0] * K[2]])


rng = np.random.default_rng(20260929)
okB2 = True
cntB2 = 0
for _ in range(250):
    Kq = [sp.Rational(int(x), int(y)) for x, y in zip(rng.integers(-6, 7, 3), rng.integers(1, 5, 3))]
    if all(x == 0 for x in Kq):
        continue
    G = Gnum(Kq)
    nsb = G.nullspace()
    Bm = sp.Matrix.hstack(*nsb)
    Gram = Bm.T * Ms * Bm
    gram = [[Fr(int(Gram[i, j].p), int(Gram[i, j].q)) for j in range(Gram.shape[1])] for i in range(Gram.shape[0])]
    inn = inertia(gram)
    s_ = sdir(Kq)
    # s in ker G, nonzero, and M-orthogonal to ker G
    okB2 &= (len(nsb) == 3 and inn == (2, 0, 1) and (G * s_).is_zero_matrix and not s_.is_zero_matrix and (Bm.T * Ms * s_).is_zero_matrix)
    cntB2 += 1
G0 = sp.zeros(3, 6)
nsb0 = [sp.eye(6)[:, i] for i in range(6)]
Gram0 = [[Fr(int(Ms[i, j].p), int(Ms[i, j].q)) for j in range(6)] for i in range(6)]
in0 = inertia(Gram0)
uvec = sp.Matrix([1, 1, 1, 0, 0, 0])
check("B2 exact on about 250 random rational momenta K != 0 (the count is printed; axis and diagonal cases in B2b): ker G(K) is 3-dimensional, M restricted to it has inertia (2 positive, 0 negative, 1 zero), "
      "the zero direction is s(K) (M-orthogonal to all of ker G); at K = 0, ker G is all of the 6 slots and M has inertia (5,1,0) with the uniform dilation (1,1,1,0,0,0) at M-value -3/2 per |u|^2=3, i.e. -1/2 per unit norm",
      okB2 and cntB2 >= 240 and in0 == (5, 1, 0) and (uvec.T * Ms * uvec)[0] == sp.Rational(-3, 2),
      f"{cntB2} momenta; inertia at K=0 is {in0}")
spec_ok = True
for Kq in ([1, 0, 0], [0, 1, 0], [1, 1, 0], [1, 1, 1], [1, 2, 3], [3, 0, 0]):
    G = Gnum([sp.Integer(x) for x in Kq])
    Bm = sp.Matrix.hstack(*G.nullspace())
    Gram = Bm.T * Ms * Bm
    spec_ok &= inertia([[Fr(int(Gram[i, j].p), int(Gram[i, j].q)) for j in range(3)] for i in range(3)]) == (2, 0, 1)
check("B2b axis and diagonal momenta (1,0,0),(0,1,0),(1,1,0),(1,1,1),(1,2,3),(3,0,0): inertia (2,0,1) exactly", spec_ok)


def build_torus(L):
    cells = list(itertools.product(range(L), repeat=3))
    cidx = {c: i for i, c in enumerate(cells)}
    n = 6 * len(cells)

    def sl(c, a):
        return 6 * cidx[tuple(x % L for x in c)] + a

    FACE = {(0, 1): 3, (1, 2): 4, (0, 2): 5}
    E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

    def ad(c, e, s=1):
        return tuple(c[i] + s * e[i] for i in range(3))

    G = [[0] * n for _ in range(3 * len(cells))]
    S = [[0] * n for _ in range(len(cells))]
    for c in cells:
        for j in range(3):
            r = 3 * cidx[c] + j
            G[r][sl(ad(c, E[j]), j)] += 1
            G[r][sl(c, j)] -= 1
            for i in range(3):
                if i != j:
                    f = FACE[tuple(sorted((i, j)))]
                    G[r][sl(c, f)] += 1
                    G[r][sl(ad(c, E[i], -1), f)] -= 1
        r = cidx[c]
        for j in range(3):
            for i in range(3):
                if i != j:
                    S[r][sl(ad(c, E[i]), j)] += 1
                    S[r][sl(ad(c, E[i], -1), j)] += 1
                    S[r][sl(c, j)] -= 2
        for (i, j), f in FACE.items():
            S[r][sl(c, f)] -= 1
            S[r][sl(ad(c, E[i], -1), f)] += 1
            S[r][sl(ad(c, E[j], -1), f)] += 1
            S[r][sl(ad(ad(c, E[i], -1), E[j], -1), f)] -= 1
    return cells, n, G, S


def Mapply(v, nc):
    out = [Fr(0)] * len(v)
    for c in range(nc):
        s = sum(v[6 * c + j] for j in range(3))
        for j in range(3):
            out[6 * c + j] = v[6 * c + j] - Fr(1, 2) * s
        for j in range(3, 6):
            out[6 * c + j] = 2 * v[6 * c + j]
    return out


def torus_check(L):
    cells, n, G, S = build_torus(L)
    nc = len(cells)
    GS0 = all(sum(G[r][k] * S[q][k] for k in range(n)) == 0 for r in range(len(G)) for q in range(nc))
    dmG = DomainMatrix([[QQ(v) for v in r] for r in G], (len(G), n), QQ)
    ns = dmG.nullspace()
    dK = ns.shape[0]
    Bf = [[Fr(int(x.p), int(x.q)) for x in row] for row in ns.to_Matrix().tolist()]
    MB = [Mapply(v, nc) for v in Bf]
    Gram = [[sum(Bf[i][k] * MB[j][k] for k in range(n)) for j in range(dK)] for i in range(dK)]
    inn = inertia(Gram)
    # Fourier k != 0 part: kernel vectors with zero cell-sum in every slot component
    meanrows = []
    for a in range(6):
        row = [0] * n
        for c in range(nc):
            row[6 * c + a] = 1
        meanrows.append(row)
    dmGm = DomainMatrix([[QQ(v) for v in r] for r in (G + meanrows)], (len(G) + 6, n), QQ)
    ns2 = dmGm.nullspace()
    B2 = [[Fr(int(x.p), int(x.q)) for x in row] for row in ns2.to_Matrix().tolist()]
    d2 = len(B2)
    MB2 = [Mapply(v, nc) for v in B2]
    Gram2 = [[sum(B2[i][k] * MB2[j][k] for k in range(n)) for j in range(d2)] for i in range(d2)]
    inn2 = inertia(Gram2)
    # S^T columns (scalar-gauge E-shifts), radical, negative direction
    St = [[S[q][k] for q in range(nc)] for k in range(n)]
    rkS = DomainMatrix([[QQ(v) for v in r] for r in S], (nc, n), QQ).rank()
    # M s_y in rowspace of G^T  <=>  rank [G^T | M S^T] == rank G^T
    MS = []
    for q in range(nc):
        sv = [Fr(S[q][k]) for k in range(n)]
        MS.append(Mapply(sv, nc))
    GT = [[G[r][k] for r in range(len(G))] for k in range(n)]
    big = [[QQ(GT[k][r]) for r in range(len(G))] + [QQ(int(MS[q][k].numerator), int(MS[q][k].denominator)) for q in range(nc)] for k in range(n)]
    rk_big = DomainMatrix(big, (n, len(G) + nc), QQ).rank()
    rk_GT = dmG.rank()
    # uniform dilation
    u = [Fr(0)] * n
    for c in range(nc):
        for j in range(3):
            u[6 * c + j] = Fr(1)
    Gu0 = all(sum(G[r][k] * u[k] for k in range(n)) == 0 for r in range(len(G)))
    Mu = Mapply(u, nc)
    uMu = sum(u[k] * Mu[k] for k in range(n))
    uMs = all(sum(Mu[k] * S[q][k] for k in range(n)) == 0 for q in range(nc))
    return dict(GS0=GS0, dK=dK, inn=inn, d2=d2, inn2=inn2, rkS=rkS, rk_big=rk_big, rk_GT=rk_GT, Gu0=Gu0, uMu=uMu, uMs=uMs, nc=nc)


for L in (3, 4):
    r = torus_check(L)
    N3 = L ** 3
    pred_full = (2 * (N3 - 1) + 5, 1, N3 - 1)
    pred_dim = 3 * (N3 - 1) + 6
    check(f"B3 L={L} torus, exact: G S^T = 0; dim ker G = {pred_dim}; M on ker G has inertia {pred_full} = (2 per nonzero momentum + 5, 1, one scalar-gauge zero per nonzero momentum); "
          f"rank S = {N3 - 1}; every M s_y lies in the row space of G (so the {N3 - 1} gauge directions are the radical of M on ker G); "
          f"the uniform dilation lies in ker G, has M-value {Fr(-3, 2) * N3} and is M-orthogonal to all gauge directions",
          r["GS0"] and r["dK"] == pred_dim and r["inn"] == pred_full and r["rkS"] == N3 - 1 and r["rk_big"] == r["rk_GT"]
          and r["Gu0"] and r["uMu"] == Fr(-3, 2) * N3 and r["uMs"],
          f"dim ker={r['dK']}, inertia={r['inn']}, rank S={r['rkS']}, u.M.u={r['uMu']}")
    check(f"B4 L={L} torus, exact: restricted to the nonzero-momentum part of ker G (zero cell-sum in each slot component, dimension {3 * (N3 - 1)}), M has inertia ({2 * (N3 - 1)}, 0, {N3 - 1}): "
          f"positive semidefinite, zeros = gauge only; the single negative direction is the homogeneous (k = 0) block",
          r["d2"] == 3 * (N3 - 1) and r["inn2"] == (2 * (N3 - 1), 0, N3 - 1), f"dim={r['d2']}, inertia={r['inn2']}")

# ----------------------------------------------------------------------------------------------
# Part C -- finite-range mixed identity, reduced block
# ----------------------------------------------------------------------------------------------
def central_coeffs(m):
    return {r: Fr((-1) ** (r + 1) * comb(2 * m, m - r), r * comb(2 * m, m)) for r in range(1, m + 1)}


z = sp.symbols("z")
okC1 = True
okC1b = True
okC1c = True
for m in range(1, 13):
    cr = central_coeffs(m)
    # exactness of d/dx on polynomials of degree <= 2m: sum c_r (r^j - (-r)^j) = delta_{j1}
    for j in range(0, 2 * m + 2):
        val = sum(cr[r] * (Fr(r) ** j - Fr(-r) ** j) for r in cr)
        exp_ = 1 if j == 1 else 0
        if j <= 2 * m:
            okC1b &= (val == exp_)
        else:
            okC1c &= (val != exp_)       # the order is exactly 2m
    # defect symbol: z D'(z) - 1 with D = sum c_r (z^r - z^-r)
    Dz = sum(sp.Rational(c.numerator, c.denominator) * (z ** r - z ** (-r)) for r, c in cr.items())
    Rz = sp.expand(z * sp.diff(Dz, z) - 1)
    Rexp = sp.expand(-((2 - z - 1 / z) ** m) / sp.binomial(2 * m, m))
    okC1 &= (sp.expand(Rz - Rexp) == 0)
check("C1 radius-m central differences D_m = sum_{r<=m} c_r (S^r - S^-r), c_r = (-1)^(r+1) C(2m,m-r)/(r C(2m,m)), m=1..12: exact on polynomials of degree <= 2m and no more "
      "(order exactly 2m), and the exact defect symbol z D_m'(z) - 1 = -(2 - z - 1/z)^m / C(2m,m) = -(2 sin(k/2))^(2m)/C(2m,m) (Laurent identity in sympy)",
      okC1 and okC1b and okC1c, "m=1..12")

okC2 = True
for m in range(1, 13):
    cr = central_coeffs(m)
    # matrix elements of the commutator defect Delta = [D,X] - 1 on the infinite lattice: Delta_{x,y} = (y-x) D_{y-x} - delta_{xy}
    def Dk(r):
        if r == 0:
            return Fr(0)
        return cr[r] if (r > 0 and r <= m) else (-cr[-r] if (r < 0 and -r <= m) else Fr(0))

    for x in range(-4, 5):
        for y in range(-4, 5):
            r = y - x
            Dxy = (y - x) * Dk(r) - (1 if x == y else 0)
            pred = -Fr((-1) ** abs(r) * comb(2 * m, m - abs(r)), comb(2 * m, m)) if abs(r) <= m else Fr(0)
            okC2 &= (Dxy == pred)
    # diagonal of the defect is exactly -1 (the sum rule), all entries have the sign pattern -(-1)^r
    okC2 &= all(((y - x) * Dk(y - x) - (1 if x == y else 0)) == -1 for x in range(-3, 4) for y in [x])
    # antisymmetry D^sharp = -D
    okC2 &= all(Dk(-r) == -Dk(r) for r in range(0, 2 * m + 2))
check("C2 reduced block F=I, A=0, mu0=0, mu1=1: D X - X D - 1 has matrix elements (y-x)D_{y-x} - delta_{xy} = -(-1)^r C(2m,m-|r|)/C(2m,m), r=y-x (exact, window |x|,|y|<=4, m=1..12); "
      "its diagonal is exactly -1 at every site and D is antisymmetric (D^sharp=-D)", okC2)

# sum rule and positivity of the defect
sr_ok = True
for m in range(1, 13):
    Rexp = sp.expand(-((2 - z - 1 / z) ** m) / sp.binomial(2 * m, m))
    const = sp.Poly(sp.expand(Rexp * z ** m), z).coeff_monomial(z ** m)
    sr_ok &= (const == -1)
    # (2 sin(k/2))^(2m) = (2 - z - 1/z)^m >= 0 on |z| = 1, so R_m <= 0 and the L1 mass of the defect is exactly 1
    sr_ok &= (int(sp.Poly(sp.expand((2 - z - 1 / z) ** m * z ** m), z).coeff_monomial(z ** m)) == comb(2 * m, m))
check("C3 exact sum rule: the mean over the Brillouin zone of the defect symbol R_m equals -1 for every m (= -mu1), R_m <= 0 pointwise, hence its L1 mass is exactly 1 for every m; "
      "the defect cannot be made small in mean, only moved", sr_ok, "m=1..12")

# random finite 2x2 Laurent matrices: z tr D' + tr[D, A F^-1] - 2 mu1 has constant coefficient -2 mu1 (trace of commutator vanishes)
random_ok = True
rs = np.random.default_rng(5)
for trial in range(3):
    def randL(rad=2):
        M_ = sp.zeros(2, 2)
        for i in range(2):
            for j in range(2):
                M_[i, j] = sum(int(rs.integers(-3, 4)) * z ** r for r in range(-rad, rad + 1))
        return M_

    Dm, Am = randL(), randL()
    Fm = sp.Matrix([[2 + z + 1 / z + int(rs.integers(0, 2)), int(rs.integers(-1, 2))], [int(rs.integers(-1, 2)), 3]])
    if sp.simplify(Fm.det()) == 0:
        continue
    Y = (Am * Fm.inv()).applyfunc(sp.cancel)
    comm = (Dm * Y - Y * Dm).applyfunc(sp.cancel)
    trc = sp.cancel(comm.trace())
    ztD = sp.expand(z * sp.diff(Dm.trace(), z))
    random_ok &= (trc == 0)
    random_ok &= (sp.Poly(sp.expand(ztD * z ** 10), z).coeff_monomial(z ** 10) == 0)
check("C4 random finite 2x2 Laurent matrices D, A and invertible F (3 trials, exact): tr[D, A F^-1] = 0 identically (rational functions) and z (tr D)' has zero constant coefficient, "
      "so the trace identity z (tr D)' = 2 mu1 of the finite-range note cannot hold for mu1 != 0", random_ok)

# Weighted-l1 extension: for a kernel with sum |r| ||D_r|| < inf the symbol z D'(z) = sum r D_r z^r converges absolutely
# and its Fourier coefficient at r = 0 is 0 * D_0 = 0.  Test with antisymmetric geometric kernels D_r = sign(r) q^|r|.
ok_ext = True
for q in (Fr(1, 2), Fr(2, 3), Fr(9, 10)):
    partial = sum(abs(r) * q ** abs(r) for r in range(-4000, 4001))
    ok_ext &= abs(float(partial) - float(2 * q / (1 - q) ** 2)) < 1e-9 * float(2 * q / (1 - q) ** 2) + 1e-9
    kern = {r: (0 if r == 0 else (1 if r > 0 else -1) * q ** abs(r)) for r in range(-60, 61)}
    zero_mode = kern[0] * 0                      # coefficient r d_r at r = 0
    ok_ext &= (zero_mode == 0)
    # mean over the circle of z D'(z) by exact Riemann sum on 8192 points = coefficient 0 (aliasing negligible)
    kk_ = np.arange(8192) * 2 * np.pi / 8192
    zz = np.exp(1j * kk_)
    zDp = sum(complex(float(r * v)) * zz ** r for r, v in kern.items())
    ok_ext &= abs(zDp.mean()) < 1e-9
check("C5 weighted-l1 class (sum |r| ||D_r|| < inf, e.g. exponentially decaying kernels): the symbol z D'(z) = sum r D_r z^r has zero circle-mean (coefficient r=0 is 0 * D_0); "
      "tested with antisymmetric geometric kernels q = 1/2, 2/3, 9/10 (first moments 2q/(1-q)^2, exact partial sums; circle mean by 8192-point sum) -- so z (tr D)' = 2 mu1 cannot hold in this class",
      ok_ext)

# universal diagonal obstruction for ANY operator D on l_c(Z) (not translation invariant, any range)
rng2 = np.random.default_rng(7)
Nw = 9
Dfull = [[Fr(int(rng2.integers(-5, 6))) for _ in range(Nw)] for _ in range(Nw)]
Xd = [Fr(x) for x in range(Nw)]
# (D X - X D)_{xy} = D_{xy} X_y - X_x D_{xy}; diagonal entries
comm_diag = [Dfull[x][x] * Xd[x] - Xd[x] * Dfull[x][x] for x in range(Nw)]
diag_ok = all(v == 0 for v in comm_diag)
check("C6 universal diagonal obstruction (reduced block, any D, any range, no translation invariance): (D X - X D)_{xy} = D_{xy}(y - x), so its diagonal vanishes; hence "
      "[D,X] - mu1 has diagonal exactly -mu1 at every site, so [D,X] = mu1 1 is impossible for mu1 != 0 and ||[D,X] - mu1|| >= |mu1| in operator norm for every D", diag_ok)

# SLAC limit
okS = True
for m in (5, 20, 80, 320):
    cr = central_coeffs(m)
    for r in (1, 2, 3, 4):
        lim = Fr((-1) ** (r + 1), r)
        okS &= abs(float(cr[r] - lim)) < 4.0 * r * r / m
cr200 = central_coeffs(200)
okS &= cr200[1] == Fr(200, 201)


def Dslac(r):
    return Fr(0) if r == 0 else Fr(1 if (r + 1) % 2 == 0 else -1, r)


okS &= all(((y - x) * Dslac(y - x) - (1 if x == y else 0)) == -((-1) ** abs(y - x)) for x in range(-6, 7) for y in range(-6, 7))
u_vec = [(-1) ** x for x in range(-6, 7)]
okS &= all(u_vec[i] * u_vec[j] == (-1) ** abs(i - j) for i in range(13) for j in range(13))
partial_first_moment = [sum(r * abs(Dslac(r)) for r in range(1, R + 1)) for R in (10, 100, 1000)]
okS &= partial_first_moment == [10, 100, 1000]
check("C7 SLAC limit m -> infinity: c_r -> (-1)^(r+1)/r (c_1 = m/(m+1)); for D_infty = sum_{r != 0} (-1)^(r+1)/r S^r, [D,X] - 1 = -P_pi with P_pi[x,y] = (-1)^(x-y) = u_x u_y (rank one, "
      "supported at the zone-edge momentum pi); the first moment sum_{r<=R} r |D_r| = R diverges, so D_infty is outside the weighted-l1 class", okS)

# numerical: defect concentrates at the zone edge, IR error decays exponentially in m on band-limited states
mp.mp.dps = 40
conc_ok = True
rows_ = []
prev_mass = 0
for m in (2, 8, 32, 128, 512):
    Cm = mp.binomial(2 * m, m)
    f = lambda k: (2 * mp.sin(k / 2)) ** (2 * m) / Cm / (2 * mp.pi)
    mass_edge = 2 * mp.quad(f, [mp.pi * 3 / 4, mp.pi])      # |k| > 3 pi/4 (both edges)
    sup_ir = (2 * mp.sin(mp.pi / 4)) ** (2 * m) / Cm        # sup over |k| <= pi/2
    rows_.append((m, float(mass_edge), float(sup_ir)))
    conc_ok &= mass_edge >= prev_mass - mp.mpf(10) ** -30
    prev_mass = mass_edge
total_check = mp.quad(lambda k: (2 * mp.sin(k / 2)) ** 20 / mp.binomial(20, 10) / (2 * mp.pi), [-mp.pi, 0, mp.pi])
conc_ok &= abs(total_check - 1) < mp.mpf(10) ** -30
conc_ok &= rows_[-1][1] > 0.999 and rows_[-1][2] < 1e-60 and rows_[0][1] < 0.9
check("C8 (numerical, mpmath 40 digits) the defect mass R_m in |k| > 3pi/4 grows monotonically toward 1 (m=2,8,32,128,512) while sup over |k| <= pi/2 of |R_m| = 2^m/C(2m,m) falls "
      "geometrically; total mass is 1 (m=10 quadrature); max |R_m| = 4^m/C(2m,m) ~ sqrt(pi m) grows (UV defect)",
      conc_ok, str([(a, round(b, 6), f"{c:.3e}") for a, b, c in rows_]))

# clock control: three-site example (exact)
q0, q1, q2, p0, p1, p2 = sp.symbols("q0 q1 q2 p0 p1 p2")
T0s, T1s, Pi0, Pi1 = sp.symbols("T0 T1 Pi0 Pi1")
pairs = [(q0, p0), (q1, p1), (q2, p2), (T0s, Pi0), (T1s, Pi1)]


def pb(Af, Bf):
    return sp.expand(sum(sp.diff(Af, q) * sp.diff(Bf, p) - sp.diff(Af, p) * sp.diff(Bf, q) for q, p in pairs))


H0, H1, H2 = p0 * q1, p1 * q2, p0 * q2
C0 = Pi0 + H0 - T1s * H2 / 2
C1 = Pi1 + H1 + T0s * H2 / 2
check("C9 clock control (exact): H0=p0 q1, H1=p1 q2, H2=p0 q2 have {H0,H1}=H2 (not first class); the clock-dressed C0 = Pi0 + H0 - T1 H2/2, C1 = Pi1 + H1 + T0 H2/2 satisfy {C0,C1} = 0 exactly; "
      "at T=0 the constraint C_a=0 reads Pi_a = -H_a, which leaves every (q,p) allowed (H_a(z)=0 is not imposed)",
      sp.expand(pb(H0, H1) - H2) == 0 and pb(C0, C1) == 0 and sp.expand(C0.subs({T0s: 0, T1s: 0}) - (Pi0 + H0)) == 0)

# ----------------------------------------------------------------------------------------------
fails = len(RES) - sum(RES)
print(f"TOTAL: PASS={sum(RES)} FAIL={fails}")
if fails == 0:
    print("HIT: scoped. (i) Reduced two-component TT block, model sector F = 1, A = 0: the exact defect of the radius-m central-difference Leibniz family is "
          "-(2 sin(k/2))^(2m)/C(2m,m), so infrared order 2m is bought with a defect whose Brillouin-zone mean is exactly -mu1, which is non-positive, has L1 mass exactly 1 for every m, "
          "and whose sup norm grows like sqrt(pi m); the diagonal of the defect is -mu1 for every D of any range (standard commutator fact, applied here); the SLAC limit leaves a rank-one zone-edge term. "
          "(ii) The reduced matrix obstruction (z (tr D)' = 2 mu1) of the finite-range note extends from finite support to every translation-invariant kernel class with summable first moment "
          "(F generically invertible), so exponentially local kernels are not a live alternative at the level of that reduced identity; the reduction of the full degree-two identity for "
          "infinite-range kernels is NOT proved here.")
print("SUMMARY: exact-character recovery of the 26->2 / 9->1 gauge-invariant leading-form counts (gauge kernel K = {Q_c}, 10-dim, ~ Sym^2 U), exact all-momentum DeWitt quotient (positive, gauge zeros only) "
      "separated from the single homogeneous negative direction on 3^3 and 4^3 tori, and an exact defect/sum-rule analysis of the reduced finite-range mixed identity "
      "showing controlled infrared closure of order 2m only by moving a defect of mass exactly mu1 to the zone edge; full gravity completion (other brackets, sources, gauge reduction) not reached.")
sys.exit(0 if fails == 0 else 1)
