"""C4b core: the B21_check Fourier-kernel bracket engine (../B21_check/kb.py, imported unchanged) extended by one
complex two-component spinor half-density chi (slots c0, c1) and its conjugate chibar (slots d0, d1).

Bracket: {chi_al(x), chibar_be(y)} = -i delta_al,be delta(x - y), i.e.
    {F, G} = -i sum_al (dF/dchi_al dG/dchibar_al - dF/dchibar_al dG/dchi_al),
so {chibar A chi, chibar B chi} = -i chibar [A, B] chi (the bilinear algebra is the same for Grassmann fields, B15 T0;
every functional below is bilinear in chi, so statistics play no role).  Evolution chi' = {chi, H} = -i h chi.

Real bilinears (sigma_0 = 1, sigma_1..3 Pauli):
    S_mu    = chibar sigma_mu chi                                   (n = S_0, spin s_c = S_c)
    J_{j,mu}= (i/2)(chibar sigma_mu d_j chi - d_j chibar sigma_mu chi) = -Re chibar sigma_mu p_j chi.
The walker's long-wavelength frame coupling (block 62: H = 1/2 sum {E^j.sigma, S_j}, S_j -> p_j) with lapse N is
    C_f[N] = int chibar 1/2{N E_a^j sigma_a, p_j} chi = - int N E_aj J_{j,a}.
"""
from __future__ import annotations
import os, sys, itertools, time
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B21_check"))
import sympy as sp
from sympy.polys.matrices import DomainMatrix
import kb
from kb import jet, Dk, h, Pt, functional, fadd, pb, eqs_of, restrict, sqrtgR_12, COMP, Q

I = sp.I
for _a in range(2):
    kb.DYN[f"c{_a}"] = (f"d{_a}", -I)
    kb.DYN[f"d{_a}"] = (f"c{_a}", I)

R3 = range(3)
CH = [jet("c0"), jet("c1")]
CB = [jet("d0"), jet("d1")]
SIG = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
XI = [jet(f"x{k}") for k in R3]
ETA = [jet(f"y{k}") for k in R3]
N, M = jet("N"), jet("M")
TH = [jet(f"t{k}") for k in R3]          # rotation-angle field (antisymmetric frame part), external
EPS = lambda i, j, k: sp.LeviCivita(i, j, k)


def S(mu, A=None):
    m = SIG[mu] if A is None else A
    return sp.expand(sum(CB[a] * m[a, b] * CH[b] for a in range(2) for b in range(2)))


def J(j, mu, A=None):
    m = SIG[mu] if A is None else A
    return sp.expand(I / 2 * sum(m[a, b] * (CB[a] * Dk(CH[b], j) - Dk(CB[a], j) * CH[b]) for a in range(2) for b in range(2)))


Sv = [S(mu) for mu in range(4)]
Jv = [[J(j, mu) for mu in range(4)] for j in R3]


def walker(Lp, E, v=1):
    """-v int Lp E_aj J_{j,a}; E is a 3x3 matrix of expressions E[a, j] = E_a^j."""
    return sp.expand(-v * Lp * sum(E[a, j] * Jv[j][a + 1] for a in R3 for j in R3))


def Hmat():
    return sp.Matrix(3, 3, lambda i, j: h(i, j))


def frame_sym(a=1, order=2):
    """symmetric section E = (delta + a h)^(-1/2) to the stated order in h."""
    H = Hmat()
    E = sp.eye(3) - a * H / 2
    if order >= 2:
        E += sp.Rational(3, 8) * a ** 2 * H * H
    return E.applyfunc(sp.expand)


def kosmann(xi, lam=1, spin=sp.Rational(-1, 4)):
    """lam int chibar i(xi.d + div xi/2 + (i/4) curl xi . sigma) chi  =  lam int (xi_k J_{k,0} - 1/4 curl xi . s)."""
    curl = [sum(EPS(c, k, j) * Dk(xi[j], k) for k in R3 for j in R3) for c in R3]
    return sp.expand(lam * (sum(xi[k] * Jv[k][0] for k in R3) + spin * sum(curl[c] * Sv[c + 1] for c in R3)))


# ------------------------------------------------------------------ gravity (re-written from chk_b21 definitions)
def G1d(xi):
    return sp.expand(sum(Pt(i, j) * (Dk(xi[j], i) + Dk(xi[i], j)) for i in R3 for j in R3))


def Lie_h(xi, i, j):
    return sum(xi[k] * Dk(h(i, j), k) + h(k, j) * Dk(xi[k], i) + h(i, k) * Dk(xi[k], j) for k in R3)


def G2Lie(xi):
    return sp.expand(sum(Pt(i, j) * Lie_h(xi, i, j) for i in R3 for j in R3))


trP = sum(Pt(k, k) for k in R3)
trPP = sp.expand(sum(Pt(i, j) * Pt(j, i) for i in R3 for j in R3))
trh = sum(h(k, k) for k in R3)


def kin0(al, b):
    return sp.expand((trPP + b * trP ** 2) / (4 * al))


def lb(a, b_):
    return [sp.expand(sum(a[k] * Dk(b_[i], k) - b_[k] * Dk(a[i], k) for k in R3)) for i in R3]


def lapse(xi, S1, S2, L_=None):
    L_ = N if L_ is None else L_
    return sp.expand(S1 * sum(xi[i] * Dk(L_, i) for i in R3) + S2 * L_ * sum(Dk(xi[i], i) for i in R3))


z0 = [sp.expand(N * Dk(M, i) - M * Dk(N, i)) for i in R3]


# ------------------------------------------------------------------ field counting / filters
def ftyp(f):
    if f[0] == "h":
        return "h"
    if f[0] == "P":
        return "P"
    if f[0] == "c" or f[0] == "d":
        return "f"
    if f[0] == "x":
        return "x"
    if f[0] == "y":
        return "y"
    if f[0] == "t":
        return "t"
    return f


def pat(**cnt):
    want = {k: v for k, v in cnt.items() if v}

    def k(fields):
        c = defaultdict(int)
        for x in fields:
            c[ftyp(x)] += 1
        return dict(c) == want
    return k


def any_of(*ks):
    return lambda f: any(k(f) for k in ks)


# ------------------------------------------------------------------ equations
def eqs_ri(F, keep=None):
    out = []
    for e in eqs_of(F, keep):
        e = sp.expand(e)
        re, im = sp.expand(sp.re(e)), sp.expand(sp.im(e))
        if re != 0:
            out.append(re)
        if im != 0:
            out.append(im)
    return out


def solve_lin(eqs, unk):
    """exact linear solve over QQ via DomainMatrix: returns (rank, consistent, nullity, particular/unique solution or None,
    rref matrix).  Coefficients must be rational numbers."""
    A, rhs = sp.linear_eq_to_matrix(eqs, unk)
    Ad = DomainMatrix.from_Matrix(A).convert_to(sp.QQ)
    Aug = DomainMatrix.from_Matrix(A.row_join(rhs)).convert_to(sp.QQ)
    rk, rka = Ad.rank(), Aug.rank()
    return rk, rk == rka, len(unk) - rk, A, rhs


def is_zero(F):
    return eqs_ri(F) == []


RES = {"pass": 0, "fail": 0}
T0 = time.time()


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} [{time.time() - T0:.0f}s] {msg}", flush=True)


def total():
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}  ({time.time() - T0:.0f}s)", flush=True)
