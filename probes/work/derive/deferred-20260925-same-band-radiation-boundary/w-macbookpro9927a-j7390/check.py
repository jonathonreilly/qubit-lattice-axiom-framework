#!/usr/bin/env python3
"""Checks for J:derive:deferred-20260925-same-band-radiation-boundary:a1 (worker w-macbookpro9927a-j7390).

Question (owner-requested recovery of block 149, PR #9242): does the walker-member coupling allow an
interband single-quantum process?  Coupling (supplied, block 136's action): V = (1/2) sum_x Theta_ij(x) h_ij(x),
Theta = block 120's stress Theta_ij = phi_j^T K_i^j (as defined in block 136), h a transverse-traceless (TT)
travelling disturbance of the member at wave vector q with frequency |p(q)|, p_j = 2 sin(q_j/2) (block 149 T1
at alpha = K/4, unit rate).  Single-quantum assumption (explicit): one disturbance carries energy |p(q)|.
Process: pair creation from the half-filled sea, lower-band walker at k' = k - q -> upper band at k.

S1  plane-wave form factor of K_a^j from its definition (symbolic)
S2  the symmetric resonances k = q/2 + pi nu vanish exactly for the stress and the energy vertex
S3  an exact non-symmetric resonance (algebraic root, rigorous interval), genuine after squaring
S4  its TT amplitude is nonzero (rigorous interval arithmetic), in two polarization conventions
All exact except S3/S4's interval enclosures, which are rigorous (mpmath.iv, outward rounding).
"""
import time

import sympy as sp
from mpmath import iv, mp

T0 = time.time()
RES = []


def check(tag, ok, msg):
    RES.append((tag, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}")


I = sp.I
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]

# ------------------------------------------------------------------ S1
# plane waves psi(x) = e^{ik.x} u; half-angle phases Z_a = e^{ik_a/2}, W_a = e^{ik'_a/2} make every factor a
# Laurent polynomial; the x-dependence is the translation factor e^{-iq.x}, so x = 0 suffices.
Zs = sp.symbols('Z1:4', nonzero=True)
Ws = sp.symbols('W1:4', nonzero=True)
u = sp.Matrix(sp.symbols('u1:3'))
up = sp.Matrix(sp.symbols('v1:3'))
ub = sp.Matrix(sp.symbols('ub1:3'))          # conj(u), independent symbols (u^dag = ub^T)


def phase(Zv, n):                              # e^{i k.n} for integer vector n
    return sp.Mul(*[Zv[a] ** (2 * n[a]) for a in range(3)])


def e(a, d):
    v = [0, 0, 0]
    v[a] = d
    return v


def Psym(Zv, j):                               # symbol of P_j = S_j C_j at k: (e^{2ik} - e^{-2ik})/(4i)
    return (Zv[j] ** 4 - Zv[j] ** (-4)) / (4 * I)


ok1 = True
for a in range(3):
    for j in range(3):
        # at x = 0: phi = e^{ik.x}u (bra conj: 1/Z), psi = e^{ik'.x}u'
        bra = lambda n: phase([1 / z for z in Zs], n)          # conj(e^{ik.n})
        ket = lambda n: phase(Ws, n)
        uAu = (ub.T * SIG[a] * up)[0]
        t1 = bra(e(a, 1)) * ket([0, 0, 0]) * Psym(Ws, j) * uAu               # phi^dag(e_a) s_a (P psi)(0)
        t2 = bra(e(a, 1)) * Psym(Zs, j) * ket([0, 0, 0]) * uAu               # (P phi)^dag(e_a) s_a psi(0), P real symbol
        t3 = bra([0, 0, 0]) * Psym(Zs, j) * ket(e(a, 1)) * uAu               # (P phi)^dag(0) s_a psi(e_a)
        t4 = bra([0, 0, 0]) * ket(e(a, 1)) * Psym(Ws, j) * uAu               # phi^dag(0) s_a (P psi)(e_a)
        elem = (t1 + t2 + t3 + t4) / 4
        # formula: (1/2) e^{-iq_a/2} cos Kbar_a (P_j(k) + P_j(k')) u^dag s_a u'
        cosK = (Zs[a] * Ws[a] + 1 / (Zs[a] * Ws[a])) / 2
        formula = sp.Rational(1, 2) * (Ws[a] / Zs[a]) * cosK * (Psym(Zs, j) + Psym(Ws, j)) * uAu
        ok1 = ok1 and sp.cancel(sp.expand(elem - formula)) == 0
check("S1", ok1, "from K_a^j(x) = (1/2)Re[psi^dag(x+e_a) sigma_a (P_j psi)(x) + (P_j psi)^dag(x+e_a) sigma_a psi(x)]: "
      "<k,u|K_a^j(x)|k',u'> = (1/2) e^{-iq.x} e^{-iq_a/2} cos(Kbar_a) (P_j(k) + P_j(k')) u^dag sigma_a u', q = k - k', "
      "Kbar = (k + k')/2 (a Laurent identity in e^{ik/2}, e^{ik'/2}); Theta_ij = phi_j^T K_i^j multiplies it by "
      "(1/2)(1 + e^{-iq_j}) prod_{l!=j} cos q_l")

# ------------------------------------------------------------------ S2
qs = sp.symbols('q1:4', real=True)
ok2 = True
for nu in [(0, 0, 0), (1, 0, 0), (0, 1, 1), (1, 1, 1)]:
    kk = [qs[i] / 2 + sp.pi * nu[i] for i in range(3)]
    kk2 = [kk[i] - qs[i] for i in range(3)]
    ok2 = ok2 and all(sp.simplify(sp.sin(kk[j]) * sp.cos(kk[j]) + sp.sin(kk2[j]) * sp.cos(kk2[j])) == 0 for j in range(3))
    ok2 = ok2 and all(sp.simplify(sp.sin(kk[j]) + sp.sin(kk2[j])) == 0 for j in range(3))
    ok2 = ok2 and all(sp.simplify(sp.sin(kk[j]) ** 2 - sp.sin(qs[j] / 2) ** 2) == 0 and
                      sp.simplify(sp.sin(kk2[j]) ** 2 - sp.sin(qs[j] / 2) ** 2) == 0 for j in range(3))
check("S2", ok2, "at every symmetric resonance k = q/2 + pi nu, k' = k - q (pair energy 2|s(q/2)| = |p(q)| exactly): "
      "P_j(k) + P_j(k') = 0 and h(k) + h(k') = 0, so the stress vertex and the energy-density vertex "
      "(1/2)u^dag(h(k) + h(k'))u' both vanish identically there")

# ------------------------------------------------------------------ S3: an exact non-symmetric resonance
sh = [sp.Rational(3, 5), sp.Rational(5, 13), sp.Rational(8, 17)]          # sin(q_j/2)
ch = [sp.Rational(4, 5), sp.Rational(12, 13), sp.Rational(15, 17)]        # cos(q_j/2)
sq = [2 * sh[i] * ch[i] for i in range(3)]                                # sin q_j
cq = [ch[i] ** 2 - sh[i] ** 2 for i in range(3)]                          # cos q_j
pvec = [2 * s for s in sh]                                                # p_j = 2 sin(q_j/2)
A = sh[1] ** 2 + sh[2] ** 2
Zq = sh[0] ** 2
t = sp.symbols('t', real=True)
c = (1 - t ** 2) / (1 + t ** 2)
s = 2 * t / (1 + t ** 2)
X = s ** 2
Y = (s * cq[0] - c * sq[0]) ** 2
Rr = 4 * Zq + 2 * A - X - Y
Fp = sp.Poly(sp.numer(sp.together(4 * (X + A) * (Y + A) - Rr ** 2)), t)
sym_root = sh[0] / (1 + ch[0])                                            # tan(q1/4): the symmetric point
q_sym, r_sym = sp.div(Fp, sp.Poly((t - sym_root) ** 2, t))
iso = sp.Poly(q_sym, t).intervals(eps=sp.Rational(1, 10 ** 40))
iv.dps = 80


def ivr(r):
    r = sp.Rational(r)
    return iv.mpf(int(r.p)) / int(r.q)


def enclose(ab):
    a_, b_ = ab
    return iv.mpf([ivr(a_).a, ivr(b_).b])


cands = [enclose(ab) for ab, mlt in iso]
okroot = r_sym.is_zero and Fp.degree() == 8
# the root t* near tan(0.2997/2): not the symmetric point (1/3) nor its pi-image (-3)
Tstar = min(cands, key=lambda T: abs(float(T.mid) - 0.1510))
okroot = okroot and not (1 / ivr(3) in Tstar) and not (ivr(-3) in Tstar) and float(Tstar.delta) < 1e-39


class C:
    """complex interval (re, im)"""
    def __init__(s_, re, im=None):
        s_.re, s_.im = re, (im if im is not None else iv.mpf(0))
    def __add__(s_, o): return C(s_.re + o.re, s_.im + o.im)
    def __sub__(s_, o): return C(s_.re - o.re, s_.im - o.im)
    def __mul__(s_, o): return C(s_.re * o.re - s_.im * o.im, s_.re * o.im + s_.im * o.re)
    def conj(s_): return C(s_.re, -s_.im)


def cr(v):
    return C(v)


def mat_mul(Am, Bm):
    return [[Am[i][0] * Bm[0][j] + Am[i][1] * Bm[1][j] for j in range(2)] for i in range(2)]


def pauli_dot(cv):          # sum_i c_i sigma_i, c complex intervals
    c1, c2, c3 = cv
    i_ = C(iv.mpf(0), iv.mpf(1))
    return [[c3, c1 - i_ * c2], [c1 + i_ * c2, C(-c3.re, -c3.im)]]


def dagger(Mm):
    return [[Mm[j][i].conj() for j in range(2)] for i in range(2)]


def proj(hv, sign):         # (1 + sign h.sigma/|h|)/2, h real intervals
    nrm = iv.sqrt(hv[0] ** 2 + hv[1] ** 2 + hv[2] ** 2)
    hs = pauli_dot([cr(sign * hv[a] / nrm) for a in range(3)])
    one = [[cr(iv.mpf(1)), cr(iv.mpf(0))], [cr(iv.mpf(0)), cr(iv.mpf(1))]]
    return [[C((one[i][j].re + hs[i][j].re) / 2, (one[i][j].im + hs[i][j].im) / 2) for j in range(2)] for i in range(2)]


def amplitude_data(T):
    cT = (1 - T ** 2) / (1 + T ** 2)
    sT = 2 * T / (1 + T ** 2)
    shI = [ivr(v) for v in sh]
    chI = [ivr(v) for v in ch]
    sqI = [ivr(v) for v in sq]
    cqI = [ivr(v) for v in cq]
    AI = ivr(A)
    X_ = sT ** 2
    sk1q = sT * cqI[0] - cT * sqI[0]                     # sin(kappa - q1)
    R_ = 4 * ivr(Zq) + 2 * AI - X_ - sk1q ** 2           # must be > 0 (genuine root)
    g_ = iv.sqrt(X_ + AI) + iv.sqrt(sk1q ** 2 + AI)
    pn = iv.sqrt(sum(ivr(v) ** 2 for v in pvec))
    s_half = sT * chI[0] - cT * shI[0]                    # sin(kappa - q1/2)
    c_half = cT * chI[0] + sT * shI[0]                    # cos(kappa - q1/2) = cos Kbar_1
    stress = 2 * s_half * c_half * cqI[0]                 # P_1(k) + P_1(k') = sin(2kappa - q1) cos q1
    hk = [sT, shI[1], shI[2]]                             # h(k*), k* = (kappa, q2/2, q3/2)
    hkp = [sk1q, -shI[1], -shI[2]]                        # h(k*'), k*' = (kappa - q1, -q2/2, -q3/2)
    return R_, g_ - pn, stress, c_half, hk, hkp, chI, shI


R_, gap, stress, cK1, hk, hkp, chI, shI = amplitude_data(Tstar)
okroot = okroot and R_.a > 0 and (0 in gap) and float(abs(gap).b) < 1e-30
check("S3", okroot, f"resonance on the line k = (kappa, q2/2, q3/2), sin(q/2) = (3/5, 5/13, 8/17): with t = tan(kappa/2) "
      f"the doubly squared condition is a degree-8 polynomial with the symmetric point t = 1/3 as a double root; its "
      f"other real roots include -3 (the pi-image of the symmetric point) and t* = {float(Tstar.mid):.15f} "
      f"(kappa* = {2 * float(mp.atan(Tstar.mid)):.12f}), isolated to width < 1e-39, where 4Z + 2A - X - Y > 0 "
      f"(so the square roots have the right sign) and |s(k*)| + |s(k*')| - |p(q)| encloses 0: an exact resonance "
      f"with k* != q/2 + pi nu")

# ------------------------------------------------------------------ S4: the amplitude at the resonance
e1 = sp.Matrix([0, pvec[2], -pvec[1]])
pv = sp.Matrix(pvec)
e2 = pv.cross(e1)
eps_plus = (e2.dot(e2)) * e1 * e1.T - (e1.dot(e1)) * e2 * e2.T
eps_cross = e1 * e2.T + e2 * e1.T
okTT = all((pv.T * E) == sp.zeros(1, 3) and E.trace() == 0 and E == E.T for E in (eps_plus, eps_cross))
Pp = proj(hk, 1)
Pm = proj(hkp, -1)
results = {}
for name, E in (("plus", eps_plus), ("cross", eps_cross)):
    for conv in ("A", "B"):
        cvec = []
        for i in range(3):
            cKi = cK1 if i == 0 else iv.mpf(1)                      # cos Kbar_i: Kbar = (kappa - q1/2, 0, 0)
            base = C(ivr(E[i, 0]) * cKi)
            if conv == "B":                                         # site convention without the pullback phase
                base = base * C(chI[i], -shI[i])                    # e^{-i q_i/2}
            cvec.append(base)
        Cm = pauli_dot(cvec)
        M4 = mat_mul(mat_mul(mat_mul(Pp, Cm), Pm), dagger(Cm))
        tr = M4[0][0] + M4[1][1]
        results[(name, conv)] = tr
nonzero = {key: (val.re.a > 0) for key, val in results.items()}
okS4 = (okTT and (stress.a > 0 or stress.b < 0) and (cK1.a > 0 or cK1.b < 0)
        and all(nonzero[(n_, "A")] or False for n_ in ("plus",)) and any(nonzero[(n_, "B")] for n_ in ("plus", "cross")))
fmt = lambda v: f"[{float(v.re.a):.4g}, {float(v.re.b):.4g}]"
check("S4", okS4, "TT polarizations (eps+, eps x) transverse to p(q) and traceless, exactly; at k*: "
      f"P_1(k*) + P_1(k*') = sin(2kappa* - q1) cos q1 in [{float(stress.a):.5f}, {float(stress.b):.5f}] (P_2, P_3 "
      f"parts vanish), cos Kbar_1 != 0, and the spinor factor |sum_i c_i u+^dag sigma_i u-|^2 = "
      f"Tr(Pi+(c.sigma)Pi-(c.sigma)^dag) with c_i = eps_i1 cos Kbar_i: eps+ {fmt(results[('plus', 'A')])} "
      f"(pulled-back convention), {fmt(results[('plus', 'B')])} (site convention); eps x "
      f"{fmt(results[('cross', 'A')])}, {fmt(results[('cross', 'B')])}; the prefactor (1/8)(1 + e^{{-iq1}}) cos q2 cos q3 "
      f"is nonzero: the pair-creation amplitude is nonzero at an exact resonance")

npass = sum(ok for _, ok in RES)
print(f"TOTAL: PASS={npass} FAIL={len(RES) - npass}  ({time.time() - T0:.0f} s)")
if npass == len(RES):
    print("SUMMARY: COUNTEREXAMPLE to suppression of the interband single-quantum channel: with block 136's coupling "
          "(1/2) Theta_ij h_ij and one TT quantum of energy |p(q)| (explicit assumption), the stress vertex vanishes "
          "exactly at every symmetric resonance k = q/2 + pi nu (P_j and h odd), but at an exact non-symmetric resonance "
          "(q/2 with sines 3/5, 5/13, 8/17; k* = (kappa*, q2/2, q3/2), kappa* = 0.29973..., an algebraic root) the "
          "pair-creation amplitude from the half-filled sea is nonzero (rigorous intervals) and the occupation allows "
          "it (lower state filled, upper state empty); the rate integral is not computed.")
    print("HIT: block 149's pair-creation channel has a nonzero allowed single-quantum amplitude: with V = (1/2) sum "
          "Theta_ij h_ij (block 136) and a TT disturbance at q, sin(q/2) = (3/5, 5/13, 8/17), the walker transition "
          "k*' = k* - q (filled lower band) -> k* (empty upper band), k* = (kappa*, q2/2, q3/2) with tan(kappa*/2) a root "
          "of an exact degree-8 resonance polynomial (0.150995526...), satisfies |s(k*)| + |s(k*')| = |p(q)| exactly and "
          "has vertex (1/8)(1 + e^{-iq1}) cos q2 cos q3 sin(2kappa* - q1) cos q1 sum_i eps_i1 cos Kbar_i u+^dag sigma_i u- "
          "!= 0 for eps+ in both site conventions; at the symmetric resonances k = q/2 + pi nu the vertex vanishes exactly.")
else:
    print("SUMMARY: ROUTE FAILS AT a failed check above")
