#!/usr/bin/env python3
"""Deferred-science recovery, ledger (first pass): checks for ATTEMPT.md, worker w-macbookpro9927a-j2f0e (claude-opus-5-5).

Residual worked (review finding U7-R5, PR8593 block 63's deferred q-only symbol experiment W3; U7-R4, PR8592 block 62's
missing site-to-face transfer; open item 1 of the a-bond-placed-stress-for-the-walk a3 attempt): which local placements of
the walk's momentum current can source block 62's symmetric six-component member so that its static compatibility condition
(orthogonality to the relabelling directions) holds on every stationary state of the walk?

Objects as landed on origin/main (blocks 62, 63, 64, 73). (T_a psi)(x) = psi(x + e_a); S_a = (T_a - T_a^-1)/(2i);
C_a = (T_a + T_a^-1)/2; P_j = S_j C_j; H = sum_a sigma_a S_a. Site response Theta_a^j(x) = Re psi^dag(x) sigma_a (S_j psi)(x);
bond currents on the bond x -> x + e_a:  J_a^j = (1/2) Re[psi^dag(x+e_a) sigma_a (S_j psi)(x) + (S_j psi)^dag(x+e_a) sigma_a psi(x)]
and K_a^j = the same with P_j (block 73). Member in the site convention of a3 (block 62's member translated): relabelling
directions h_ij = -(d_i xi_j + d_j xi_i), d_a the forward difference. Everything below is exact: Gaussian rationals for the
lattice identities (plane waves with rational points e^{ik}), sympy for symbolic identities and determinants.
"""
from __future__ import annotations

import hashlib
import json
import random
import subprocess
import time
from fractions import Fraction as Fr

import sympy as sp

OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


# ----------------------------------------------------------------------------------------------------------------------
# Gaussian rationals and plane-wave states on Z^3


class G:
    __slots__ = ("r", "i")

    def __init__(self, r=0, i=0):
        self.r = r if isinstance(r, Fr) else Fr(r)
        self.i = i if isinstance(i, Fr) else Fr(i)

    def __add__(a, b):
        if not isinstance(b, G):
            b = G(b)
        return G(a.r + b.r, a.i + b.i)

    __radd__ = __add__

    def __sub__(a, b):
        if not isinstance(b, G):
            b = G(b)
        return G(a.r - b.r, a.i - b.i)

    def __rsub__(a, b):
        return G(b) - a

    def __mul__(a, b):
        if not isinstance(b, G):
            b = G(b)
        return G(a.r * b.r - a.i * b.i, a.r * b.i + a.i * b.r)

    __rmul__ = __mul__

    def __neg__(a):
        return G(-a.r, -a.i)

    def conj(a):
        return G(a.r, -a.i)

    def iszero(a):
        return a.r == 0 and a.i == 0

    def __eq__(a, b):
        if not isinstance(b, G):
            b = G(b)
        return a.r == b.r and a.i == b.i

    def __hash__(a):
        return hash((a.r, a.i))


I = G(0, 1)
MI2 = G(0, Fr(-1, 2))    # 1/(2i)
MI4 = G(0, Fr(-1, 4))    # 1/(4i)
E3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def sh(x, a, m=1):
    return tuple(x[b] + m * E3[a][b] for b in range(3))


class State:
    """psi(x) = sum_n chi_n prod_a z_{n,a}^{x_a}, |z| = 1 Gaussian rational (so z^-1 = conj z)."""

    def __init__(self, waves):
        self.waves = []
        for z, chi in waves:
            for zz in z:
                assert zz.r * zz.r + zz.i * zz.i == 1
            self.waves.append((z, chi, [dict() for _ in range(3)]))
        self.cache = {}

    def pw(self, n, a, m):
        z, _, pc = self.waves[n]
        d = pc[a]
        if m not in d:
            if m == 0:
                d[m] = G(1)
            elif m > 0:
                d[m] = self.pw(n, a, m - 1) * z[a]
            else:
                d[m] = self.pw(n, a, m + 1) * z[a].conj()
        return d[m]

    def psi(self, x):
        v = self.cache.get(x)
        if v is None:
            v0, v1 = G(0), G(0)
            for n, (z, chi, _) in enumerate(self.waves):
                f = self.pw(n, 0, x[0]) * self.pw(n, 1, x[1]) * self.pw(n, 2, x[2])
                v0 = v0 + f * chi[0]
                v1 = v1 + f * chi[1]
            v = (v0, v1)
            self.cache[x] = v
        return v


def vsub(u, v):
    return (u[0] - v[0], u[1] - v[1])


def vscale(c, u):
    return (c * u[0], c * u[1])


def sig(a, v):
    if a == 0:
        return (v[1], v[0])
    if a == 1:
        return (G(0, -1) * v[1], I * v[0])
    return (v[0], -v[1])


def dot(u, v):   # u^dag v
    return u[0].conj() * v[0] + u[1].conj() * v[1]


def Sop(st, j, x):
    return vscale(MI2, vsub(st.psi(sh(x, j, 1)), st.psi(sh(x, j, -1))))


def Pop(st, j, x):
    return vscale(MI4, vsub(st.psi(sh(x, j, 2)), st.psi(sh(x, j, -2))))


def Hpsi(st, x):
    acc = (G(0), G(0))
    for a in range(3):
        t = sig(a, Sop(st, a, x))
        acc = (acc[0] + t[0], acc[1] + t[1])
    return acc


def theta(st, a, j, x):
    return dot(st.psi(x), sig(a, Sop(st, j, x))).r


def cur(st, a, j, x, mom):
    y = sh(x, a)
    return (dot(st.psi(y), sig(a, mom(st, j, x))) + dot(mom(st, j, y), sig(a, st.psi(x)))).r / 2


def rho(st, x):
    return dot(st.psi(x), st.psi(x)).r


def box(r, c=(0, 0, 0)):
    return [(c[0] + u, c[1] + v, c[2] + w) for u in range(-r, r + 1) for v in range(-r, r + 1) for w in range(-r, r + 1)]


# rational points on the unit circle
def rp(c, s):
    assert c * c + s * s == 1
    return G(c, s)


F45 = rp(Fr(4, 5), Fr(3, 5))   # e^{i theta}, cos theta = 4/5, sin theta = 3/5
Fm45 = F45.conj()


def reflection_state(z2, z3, E_over_chi=None):
    """k = (pi/2 + theta, k2, k3), k' = (pi/2 - theta, k2, k3), same coin: psi = chi (e^{ik.x} + e^{ik'.x})."""
    z1, z1p = I * F45, I * Fm45
    s = (Fr(4, 5), z2.i, z3.i)
    return (z1, z2, z3), (z1p, z2, z3), s


def eigvec(s, E):
    """eigenvector of s.sigma with eigenvalue E (E^2 = |s|^2), (E + s3, s1 + i s2)."""
    return (G(E + s[2]), G(s[0], s[1]))


# ----------------------------------------------------------------------------------------------------------------------
# Family A: the axis reflection states, their responses, and the spanning lemma


def family_a() -> dict:
    res = {}
    data = [(rp(Fr(4, 5), Fr(3, 5)), G(1), Fr(1)), (G(1), rp(Fr(4, 5), Fr(3, 5)), Fr(1)), (G(1), G(1), Fr(4, 5))]
    bad = []
    states = []
    for z2, z3, E in data:
        k, kp, s = reflection_state(z2, z3)
        assert sum(x * x for x in s) == E * E
        chi = eigvec(s, E)
        st = State([(k, chi), (kp, chi)])
        states.append((st, s, E, (z2, z3)))
        for x in box(2):
            h = Hpsi(st, x)
            p = st.psi(x)
            if not (h[0] == E * p[0] and h[1] == E * p[1]):
                bad.append(("H", x))
            r = rho(st, x)
            cosk = (None, z2.r, z3.r)
            for a in range(3):
                for j in range(3):
                    if theta(st, a, j, x) != s[a] * s[j] * r / E:
                        bad.append(("Theta", x, a, j))
                    want = 0 if a == 0 else s[a] * s[j] * cosk[a] * r / E
                    if cur(st, a, j, x, Sop) != want:
                        bad.append(("J", x, a, j))
            for j in range(3):
                dv = sum(cur(st, a, j, x, Sop) - cur(st, a, j, sh(x, a, -1), Sop) for a in range(3))
                if dv != 0:
                    bad.append(("div", x, j))
    # the symmetric part of J is not conserved on the first state (its (1,2) entry varies along x1)
    st, s, E, _ = states[0]
    symdiv = [sum((cur(st, a, j, x, Sop) + cur(st, j, a, x, Sop)) / 2 - (cur(st, a, j, sh(x, a, -1), Sop)
                   + cur(st, j, a, sh(x, a, -1), Sop)) / 2 for a in range(3)) for x in box(1) for j in range(3)]
    check("A1", not bad and any(v != 0 for v in symdiv),
          "reflection states k=(pi/2+th,k2,k3), k'=(pi/2-th,k2,k3), cos th=4/5, one coin, s=(4/5,3/5,0),(4/5,0,3/5),(4/5,0,0): "
          "H psi=E psi at all 125 sites of [-2,2]^3; there Theta_a^j=s_a s_j rho/E, J_1^j=0, J_a^j=s_a s_j cos k_a rho/E (a=2,3) "
          f"for all 9 (a,j) (rho=|psi|^2); div J=0; div of sym(J) nonzero ({sum(v != 0 for v in symdiv)}/81 site-j on [-1,1]^3)")
    # spanning lemma, symbolic in c = cos(theta) (= s_1 of every reflection state), common factor 1/E dropped
    c = sp.symbols("c")
    pts = [(sp.Rational(4, 5), sp.Rational(3, 5)), (sp.Rational(3, 5), sp.Rational(4, 5)), (1, 0), (0, 1),
           (sp.Rational(-4, 5), sp.Rational(3, 5)), (sp.Rational(5, 13), sp.Rational(12, 13)), (sp.Rational(12, 13), sp.Rational(-5, 13))]
    samples = [(pts[0], pts[1]), (pts[1], pts[4]), (pts[5], pts[2]), (pts[2], pts[6]), (pts[0], pts[3]), (pts[6], pts[5])]
    rowsJ, rowsT = [], []
    for (c2, s2), (c3, s3) in samples:
        v = [c2 * s2, c3 * s3]
        u = [c, s2, s3]
        rowsJ.append([v[a] * u[j] for a in range(2) for j in range(3)])
        sv = [c, s2, s3]
        rowsT.append([sv[a] * sv[b] for a in range(3) for b in range(a, 3)])
    dJ = sp.factor(sp.Matrix(rowsJ).det())
    dT = sp.factor(sp.Matrix(rowsT).det())
    polyJ, polyT = sp.Poly(dJ, c), sp.Poly(dT, c)
    okJ = polyJ.is_monomial and polyJ.degree() == 2 and polyJ.LC() != 0
    okT = polyT.is_monomial and polyT.degree() == 4 and polyT.LC() != 0
    check("A2", okJ and okT,
          f"spanning at every axis q=(2th,0,0), cos th=c: six reflection pairs give det[J-parts in {{v1=0}}(x)C^3] = {polyJ.LC()} c^2 "
          f"and det[Theta-parts in Sym(3)] = {polyT.LC()} c^4: nonzero for every c != 0, so the S-currents span U(q)(x)C^3 "
          "(all conserved currents at q) and the site responses span Sym(3)")
    res["states"] = states
    return res


# ----------------------------------------------------------------------------------------------------------------------
# finitely supported fields and the three pairings


def fwd(f, a):
    """forward difference of a site field (dict), (d_a f)(x) = f(x+e_a) - f(x)"""
    out = {}
    for x, v in f.items():
        out[x] = out.get(x, 0) - v
        y = sh(x, a, -1)
        out[y] = out.get(y, 0) + v
    return {x: v for x, v in out.items() if v != 0}


def avg(f, a, back_only=False):
    out = {}
    for x, v in f.items():
        if back_only:   # (1/2)(1 + T_a^-1): (g)(x) = (f(x) + f(x - e_a))/2
            for y in (x, sh(x, a, 1)):
                out[y] = out.get(y, 0) + Fr(v) / 2
        else:           # C_a: (g)(x) = (f(x+e_a) + f(x-e_a))/2
            for y in (sh(x, a, -1), sh(x, a, 1)):
                out[y] = out.get(y, 0) + Fr(v) / 2
    return {x: v for x, v in out.items() if v != 0}


def phi_op(f, j):
    """phi_j = (1/2)(1 + T_j^-1) prod_{l != j} C_l, symbol (1 + e^{-i q_j})/2 prod cos q_l"""
    g = avg(f, j, back_only=True)
    for l in range(3):
        if l != j:
            g = avg(g, l)
    return g


def strain_of_relabelling(xi, phi):
    """W_a^j = (1/2) Phi_j[d_a xi_j + d_j xi_a]: the walker's strain B = -(1/2) Phi h for h = -(d_i xi_j + d_j xi_i)"""
    W = {}
    for a in range(3):
        for j in range(3):
            f = {}
            for part in (fwd(xi[j], a), fwd(xi[a], j)):
                for x, v in part.items():
                    f[x] = f.get(x, 0) + Fr(v) / 2
            if phi:
                f = phi_op(f, j)
            W[(a, j)] = {x: v for x, v in f.items() if v != 0}
    return W


def pairing(st, W, kind):
    tot = Fr(0)
    for (a, j), f in W.items():
        for x, v in f.items():
            if kind == "Theta":
                tot += v * theta(st, a, j, x)
            else:
                tot += v * cur(st, a, j, x, Sop if kind == "J" else Pop)
    return tot


def rand_xi(rng, r=1):
    return [{x: rng.randint(-3, 3) for x in box(r)} for _ in range(3)]


def superposition_E1():
    """five plane waves of energy 1 with rational sines; coins (1+s3, s1+i s2) times Gaussian-integer amplitudes"""
    waves = []
    spec = [((Fr(4, 5), Fr(3, 5)), (Fr(3, 5), Fr(4, 5)), (Fr(1), Fr(0)), G(1, 2)),
            ((Fr(3, 5), Fr(4, 5)), (Fr(-1), Fr(0)), (Fr(-4, 5), Fr(3, 5)), G(2, -1)),
            ((Fr(1), Fr(0)), (Fr(-4, 5), Fr(3, 5)), (Fr(3, 5), Fr(4, 5)), G(3)),
            ((Fr(-4, 5), Fr(3, 5)), (Fr(1), Fr(0)), (Fr(-3, 5), Fr(4, 5)), G(-1, 1)),
            ((Fr(-1), Fr(0)), (Fr(3, 5), Fr(4, 5)), (Fr(4, 5), Fr(3, 5)), G(2, 2))]
    for (c1, s1), (c2, s2), (c3, s3), amp in spec:
        z = (rp(c1, s1), rp(c2, s2), rp(c3, s3))
        assert s1 * s1 + s2 * s2 + s3 * s3 == 1
        chi = eigvec((s1, s2, s3), Fr(1))
        waves.append((z, (amp * chi[0], amp * chi[1])))
    return State(waves)


# ----------------------------------------------------------------------------------------------------------------------
# Family B: the site response - exact W3 and the transfer


def pauli(v):
    return sp.Matrix([[v[2], v[0] - sp.I * v[1]], [v[0] + sp.I * v[1], -v[2]]])


def family_b(fa: dict) -> None:
    # B1: W3 exactly at the rational axis q = (2 th, 0, 0), cos th = 4/5: reflection pairs have M = s/E, Theta^j = s_j s/E
    c = sp.Rational(4, 5)
    trip = {0: [(c, 0, 0), (c, sp.Rational(3, 5), 0), (c, 0, sp.Rational(3, 5))],
            1: [(c, sp.Rational(3, 5), 0), (c, sp.Rational(3, 5), sp.Rational(4, 5)), (c, sp.Rational(4, 5), 0)],
            2: [(c, 0, sp.Rational(3, 5)), (c, sp.Rational(4, 5), sp.Rational(3, 5)), (c, 0, sp.Rational(4, 5))]}
    dets = [sp.Matrix(trip[j]).det() for j in range(3)]
    check("B1", all(d != 0 for d in dets),
          "q-only symbol, axis q=(2th,0,0), cos th=4/5: for each j, three reflection pairs with rational sines and s_j != 0 have "
          f"independent Theta^j_a = s_j s_a/E (dets {', '.join(str(d) for d in dets)}): sum_a f_a Theta_a^j = 0 on them forces f=0 "
          "(complex f)")
    # B2: W3 at a generic rational q: the eight per-component pairs kbar_a in {0, pi/2}, both bands
    ct = [(sp.Rational(4, 5), sp.Rational(3, 5)), (sp.Rational(12, 13), sp.Rational(5, 13)), (sp.Rational(15, 17), sp.Rational(8, 17))]
    f = sp.symbols("f1:4")
    fs = pauli(f)
    eqs = []
    only0 = None
    for choice in range(8):
        s = [ct[a][0] if choice >> a & 1 else ct[a][1] for a in range(3)]
        s2 = [ct[a][0] if choice >> a & 1 else -ct[a][1] for a in range(3)]
        E2 = sum(x * x for x in s)
        X = E2 * fs + pauli(s2) * fs * pauli(s)
        Y = pauli(s2) * fs + fs * pauli(s)
        e = [sp.expand(x) for x in list(X) + list(Y)]
        if choice != 0:   # s + s' = 0 for the all-negation pair: its site response vanishes, no condition
            eqs += e
        if choice == 0:
            sub = {f[a]: ct[a][1] for a in range(3)}
            only0 = all(sp.simplify(x.subs(sub)) == 0 for x in e)
    A = sp.Matrix([[sp.expand(x).coeff(fv) for fv in f] for x in eqs])
    check("B2", A.rank() == 3 and only0,
          "q-only symbol, generic rational q (half-angles with sines 3/5, 5/13, 8/17): the seven per-component pairs "
          "(kbar_a in {0, pi/2}) with s + s' != 0, both bands, give P'(f.sigma)P = 0 as the linear system X = Y = 0 of rank 3: "
          "only f = 0; the all-negation pair (s + s' = 0, no site response) accepts block 62's symbol p = 2 sin(q/2)")
    # B3: the naive transfer eps = -h/2 fails on a reflection state; B4: on the species-0 axis pair everything passes
    st = fa["states"][0][0]
    xi = [{(0, 0, 0): 1}, {}, {}]
    W = strain_of_relabelling(xi, phi=False)
    v3 = pairing(st, W, "Theta")
    zN = (rp(Fr(4, 5), Fr(3, 5)), rp(Fr(3, 5), Fr(4, 5)), G(1))
    zNp = (rp(Fr(4, 5), Fr(-3, 5)), rp(Fr(3, 5), Fr(4, 5)), G(1))
    stN = State([(zN, eigvec((Fr(3, 5), Fr(4, 5), Fr(0)), Fr(1))), (zNp, eigvec((Fr(-3, 5), Fr(4, 5), Fr(0)), Fr(1)))])
    okN = all(Hpsi(stN, x)[0] == stN.psi(x)[0] and Hpsi(stN, x)[1] == stN.psi(x)[1] for x in box(2))
    fa["species0"] = stN
    rng = random.Random(7)
    passN = []
    for _ in range(3):
        xr = rand_xi(rng)
        Wn = strain_of_relabelling(xr, phi=False)
        passN.append((pairing(stN, Wn, "Theta"), pairing(stN, Wn, "J")))
    check("B3", v3 != 0 and okN and all(p == (0, 0) for p in passN),
          f"the site transfer eps = -h/2 on the reflection state s=(4/5,3/5,0), xi_1 = delta_0: pairing = {v3} != 0 "
          "(member compatibility violated); boundary: on the species-0 axis pair k=(th,k2,0), k'=(-th,k2,0) (H psi = psi) "
          "both Theta with this transfer and J with B = -h/2 pass for three random xi (pairings 0)")


# ----------------------------------------------------------------------------------------------------------------------
# Family C: the S-current (blocks 63/64)


def family_c(fa: dict, sup: State) -> None:
    st = fa["states"][0][0]
    xi = [{}, {(0, 0, 0): 1}, {}]
    Wn = strain_of_relabelling(xi, phi=False)
    naive = pairing(st, Wn, "J")
    cons = Fr(0)   # sum_x J_a^j (d_a xi_j): zero by conservation
    for a in range(3):
        for j in range(3):
            for x, v in fwd(xi[j], a).items():
                cons += v * cur(st, a, j, x, Sop)
    rng = random.Random(11)
    phis = [pairing(sup, strain_of_relabelling(rand_xi(rng), phi=True), "J") for _ in range(2)]
    check("C1", naive != 0 and cons == 0 and all(p != 0 for p in phis),
          f"S-current: on the reflection state, xi_2 = delta_0: sum J (d xi) = {cons} (conservation) but the symmetric "
          f"realisation B = -h/2 gives pairing {naive} != 0 (a3's transposed divergence); the phi-realisation of family D "
          f"also fails for J on the energy-1 superposition ({', '.join(str(p) for p in phis)})")


# ----------------------------------------------------------------------------------------------------------------------
# Family D: the two-step current (block 73): a transposed law and a compatible local realisation


def family_d(sup: State, fa: dict) -> None:
    k, kp, q = sp.symbols("k kp q", real=True)
    e1 = sp.sin(k - kp) * (sp.sin(2 * k) + sp.sin(2 * kp)) / 2 - sp.cos(k - kp) * (sp.sin(k) ** 2 - sp.sin(kp) ** 2)
    e2 = (1 + sp.exp(-sp.I * q)) / 2 * (sp.exp(sp.I * q) - 1) - sp.I * sp.sin(q)
    e3 = sp.exp(-sp.I * q / 2) * (sp.exp(sp.I * q) - 1) - sp.I * 2 * sp.sin(q / 2)
    zs = [sp.simplify(sp.expand(sp.expand_trig(e1))), sp.simplify(e2.rewrite(sp.exp)), sp.simplify(e3.rewrite(sp.exp))]
    check("D1", all(z == 0 for z in zs),
          "symbolic: sin q_j (P_j(k)+P_j(k')) = cos q_j (sin^2 k_j - sin^2 k'_j) (so sum_j sin q_j prod_{l!=j} cos q_l "
          "(P_j+P'_j) = prod cos q . (E^2 - E'^2)); phi_j D_j = i sin q_j (x prod_{l!=j} cos q_l); e^{-iq/2}(e^{iq}-1) = i p")
    # D0: the response of the couplings sigma_a (1/2){C_a[v], M_j} (M = S: block 64, M = P: block 73) to a bond field v
    rngv = random.Random(3)
    resp_bad = 0
    for M in (Sop, Pop):
        for a in range(3):
            for j in range(3):
                v = {x: Fr(rngv.randint(-2, 2)) for x in box(1)}

                def Cv(f, x, a=a, v=v):   # (C_a[v] f)(x) = (1/2)[v(x) f(x+e_a) + v(x-e_a) f(x-e_a)]
                    y, z = sh(x, a), sh(x, a, -1)
                    u, w = f(y), f(z)
                    return (G(v.get(x, 0) / 2) * u[0] + G(v.get(z, 0) / 2) * w[0],
                            G(v.get(x, 0) / 2) * u[1] + G(v.get(z, 0) / 2) * w[1])
                gC = {x: Cv(sup.psi, x) for x in box(6)}   # C_a[v] psi lives on [-2,2]^3; M_j reaches two further
                tmp = State.__new__(State)
                tmp.cache = dict(gC)
                tot = G(0)
                for x in box(4):
                    t1 = Cv(lambda y: M(sup, j, y), x)
                    t2 = M(tmp, j, x)
                    o = sig(a, ((t1[0] + t2[0]) * Fr(1, 2), (t1[1] + t2[1]) * Fr(1, 2)))
                    tot = tot + dot(sup.psi(x), o)
                want = sum((vv * cur(sup, a, j, x, M) for x, vv in v.items()), Fr(0))
                resp_bad += not (tot.i == 0 and tot.r == want)
    okH = all(Hpsi(sup, x)[0] == sup.psi(x)[0] and Hpsi(sup, x)[1] == sup.psi(x)[1] for x in box(2))
    check("D0", resp_bad == 0 and okH,
          "<psi| sigma_a (1/2){C_a[v], M_j} |psi> = sum_x v(x) (current)_a^j(x) exactly for random integer bond fields v on "
          "[-1,1]^3, all 9 (a,j), with M = S (block 64's coupling, current J) and M = P (block 73's, current K), on the "
          "energy-1 superposition (H psi = psi on [-2,2]^3)")
    bad, jbad, n = [], 0, 0
    for x in box(1):
        for a in range(3):
            tK, tJ = Fr(0), Fr(0)
            for j in range(3):
                ls = [l for l in range(3) if l != j]
                for sgn in (1, -1):
                    y0 = sh(x, j, sgn)
                    for u in (1, -1):
                        for w in (1, -1):
                            y = sh(sh(y0, ls[0], u), ls[1], w)
                            tK += sgn * cur(sup, a, j, y, Pop) / 4
                            tJ += sgn * cur(sup, a, j, y, Sop) / 4
            n += 1
            if tK != 0:
                bad.append((x, a))
            jbad += tJ != 0
        for j in range(3):
            if sum(cur(sup, a, j, x, Pop) - cur(sup, a, j, sh(x, a, -1), Pop) for a in range(3)) != 0:
                bad.append(("div", x, j))
    check("D2", okH and not bad and jbad > 0,
          "two-step current K on an exact energy-1 superposition of five plane waves (H psi = psi on [-2,2]^3): "
          f"sum_j prod_(l!=j) C_l [K_a^j(x+e_j) - K_a^j(x-e_j)] = 0 at all {n} (site, a) and div K = 0; the same transposed "
          f"combination of J is nonzero at {jbad}/{n}")
    rng = random.Random(5)
    vals = []
    for _ in range(3):
        xi = rand_xi(rng)
        vals.append((pairing(sup, strain_of_relabelling(xi, phi=True), "K"), pairing(sup, strain_of_relabelling(xi, phi=False), "K")))
    others = [fa["states"][i][0] for i in range(3)] + [fa["species0"]]
    extra = [pairing(st, strain_of_relabelling(rand_xi(rng), phi=True), "K") for st in others]
    check("D3", all(v[0] == 0 and v[1] != 0 for v in vals) and all(e == 0 for e in extra),
          "phi-realisation B_i^j = -(1/2) phi_j h_ij, phi_j = (1/2)(1 + T_j^-1) prod_(l!=j) C_l (phi_j = 1 at q = 0): the "
          "member's relabelling directions pair to exactly 0 with K for three random integer xi on [-1,1]^3 on the "
          "superposition, and for one each on the three reflection states and the species-0 pair; the symmetric realisation "
          f"B = -h/2 gives {', '.join(str(v[1]) for v in vals)}")
    # D4: block 62's static member: R_2's kernel at nonzero p is exactly the three relabelling directions
    hs = sp.symbols("h11 h22 h33 h12 h13 h23")
    h = sp.Matrix([[hs[0], hs[3], hs[4]], [hs[3], hs[1], hs[5]], [hs[4], hs[5], hs[2]]])
    ranks = []
    for pv in [(1, 0, 0), (1, 2, 2), (sp.Rational(2, 5), sp.Rational(1, 3), sp.Rational(-3, 7))]:
        p = sp.Matrix(pv)
        p2 = (p.T * p)[0]
        R2 = (-(p2 / 4) * (h.T * h).trace() + sp.Rational(1, 2) * ((h * p).T * (h * p))[0]
              - sp.Rational(1, 2) * (p.T * h * p)[0] * h.trace() + (p2 / 4) * h.trace() ** 2)
        Mq = sp.hessian(R2, hs)
        gauge = []
        for b in range(3):
            eta = sp.Matrix([1 if c == b else 0 for c in range(3)])
            g = p * eta.T + eta * p.T
            gauge.append(sp.Matrix([g[0, 0], g[1, 1], g[2, 2], g[0, 1], g[0, 2], g[1, 2]]))
        ranks.append((Mq.rank(), all((Mq * g).is_zero_matrix for g in gauge), sp.Matrix.hstack(*gauge).rank()))
    check("D4", all(r == (3, True, 3) for r in ranks),
          "block 62's R_2 static matrix at p = (1,0,0), (1,2,2), (2/5,1/3,-3/7): rank 3, kernel = the three relabelling "
          "directions p(x)eta + eta(x)p; a source orthogonal to them is solvable at that wave vector")


# ----------------------------------------------------------------------------------------------------------------------
# Family Q: sources (origin/main 0e6ad82850, frozen heads, the a3 attempt, batch-07 findings) and every status SHA256

MAIN = "0e6ad82850"
N62 = ("docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_"
       "SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md")
N63 = ("docs/ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_"
       "NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md")
N64 = ("docs/ADMISSIBILITY_RULE_BOND_STRAINS_AND_PLAQUETTE_CURLS_A_FIELD_ENERGY_PER_LOCAL_TICK_THAT_DOES_NOT_SEE_THE_COINS_AXES_"
       "IS_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md")
N73 = ("docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_"
       "CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md")
H8593 = "3b0ed2b08180bda9b2174f61edf57b8ac2e8a71d"
HERE = "probes/work/derive/deferred-20260924-ledger/w-macbookpro9927a-j2f0e/"
A3 = "probes/work/derive/a-bond-placed-stress-for-the-walk/w-jonathonsmac4f50-j1518/ATTEMPT.md"
QUOTES = [
    (MAIN, N62, "The site-centered frame response of T2 requires a declared transfer/interpolation to those face components. "
                "Its preservation of the divergence condition is not established here."),
    (MAIN, N63, "The stronger on-shell claim that no nonzero q-only divergence symbol can work for every pair remains a deferred "
                "author experiment, not a proved universal no-go."),
    (MAIN, N64, "On a closed lattice the uniform part of the current is not balanced by any curl"),
    (MAIN, N73, "on stationary states the left side vanishes, so `K` is divergence-free there."),
    (H8593, N63, "An exact version needs two equal-energy pairs with rational data and a common `q`; not constructed."),
    (None, A3, "**Not shown: that every realisation `R` fails.**"),
    (None, A3, "The spanning statement above, which would turn"),
]


def family_q() -> int:
    bad = []
    for ref, path, q in QUOTES:
        text = open(path).read() if ref is None else subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True,
                                                                    text=True).stdout
        if q not in text:
            bad.append(path[-40:])
    b = json.load(open("probes/work/deferred-science-20260924/batch-07.json"))
    f5 = next(x for x in b["findings"] if x["id"] == "U7-R5")["resolution"]
    f4 = next(x for x in b["findings"] if x["id"] == "U7-R4")["resolution"]
    if "defer q-only numerical no-go" not in f5 or "missing site-to-face transfer explicit" not in f4:
        bad.append("findings")
    st = json.load(open(HERE + "RECOVERY_STATUS.json"))
    allsrc = {(x["pr"], x["path"]): x for x in b["sources"]}
    for e in st["source_groups_inspected"]:
        m = allsrc[(e["pr"], e["path"])]
        data = subprocess.run(["git", "show", f"{m['head']}:{m['path']}"], capture_output=True).stdout
        if hashlib.sha256(data).hexdigest() != m["sha256"] or e["sha256"] != m["sha256"] or e["head"] != m["head"]:
            bad.append("status:" + e["path"].split("/")[-1])
    if not st["origin_main_sha"].startswith(MAIN):
        bad.append("main sha")
    n = len(st["source_groups_inspected"])
    check("Q", not bad, f"quotes from origin/main {MAIN} (blocks 62, 63, 64, 73), frozen head {H8593[:10]} (N1.5: 'An exact "
          "version needs two equal-energy pairs with rational data and a common q; not constructed'), a3's 'Not shown: that "
          f"every realisation R fails'; findings U7-R5/U7-R4; SHA256 of all {n} sources in RECOVERY_STATUS.json re-verified "
          f"from their frozen heads {'' if not bad else bad}")
    return n


def main() -> None:
    t0 = time.time()
    n = family_q()
    fa = family_a()
    family_b(fa)
    sup = superposition_E1()
    family_c(fa, sup)
    family_d(sup, fa)
    print("\n".join(OUT))
    print(f"TOTAL: PASS={len(OUT) - len(FAILS)} FAIL={len(FAILS)}  ({time.time() - t0:.1f}s)")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return
    print("SUMMARY: PARTIAL exact, for block 62's symmetric member and the walk H = sum sigma_a S_a (identity frame, first order, "
          "every stationary state): (1) at every axis q = (t,0,0), cos(t/2) != 0, stationary 'reflection' pairs make the site "
          "responses span Sym(3) and the S-currents span all conserved currents U(q)(x)C^3; hence no local site-to-face transfer "
          "and no local realisation B = R h with Lambda R(0) = 1 keeps the member compatible (they would be blind to uniform "
          "strain, resp. shear), and no q-only symbol serves every equal-energy pair (exact, rational witnesses; also at a "
          "generic rational q); (2) block 73's two-step current obeys the exact transposed law sum_j prod_(l!=j) C_l "
          "[K_a^j(x+e_j) - K_a^j(x-e_j)] = 0 on stationary states, and B_i^j = -(1/2) phi_j h_ij is a local realisation "
          "(exact for uniform fields) under which the member's compatibility holds on every stationary state. "
          f"{n} deferred sources inspected; first pass.")
    print("HIT: the walk's site response and the bond current of the momentum S_j cannot source block 62's symmetric member compatibly on all "
          "stationary states through any local transfer (both spans are full at every axis wave vector), while block 73's "
          "two-step current satisfies an exact transposed conservation law and admits an explicit local realisation "
          "B_i^j = -(1/2) phi_j h_ij that makes the member's compatibility exact on every stationary state")


if __name__ == "__main__":
    main()
