#!/usr/bin/env python3
"""Corrigendum packet for PR #8180 (block 35, the gravity node's kernel under the formation reading): the checks behind ATTEMPT.md.

Objects (block 35's declared objects with block 34's transform; PR #8180 at 7c844adf, PR #8178 at its head):
  theta_{t+1} = P theta_t + xi_t on the periodic L x L level plane, (P theta)_(i,j) = (theta_(i,j) + theta_(i-1,j) + theta_(i,j-1))/3 (the runner's
  shift_matrix; the control's np.roll), xi i.i.d. of variance sigma^2 = 1 per site (sigma^2 scales out); phi(k) = (1 + e^{ik1} + e^{ik2})/3,
  u = |phi|^2, e_k(x) = e^{ik.x}; block 34's transform theta^_k = L^{-1} sum_x e^{-ik.x} theta_x; the runner's exact covariance recursion
  Sigma_{t+1} = P Sigma_t P^T + I (Sigma_0 = 0) and Sigma_{t,t+s} := [Cov(theta_{x,t}, theta_{x',t+s})]_{x,x'} = Sigma_t (P^s)^T.
T1 (exact, in Q(sqrt3, i), which holds every character value on L = 3, 4):
  T1a  P^T e_k = phi e_k and P e_k = conj(phi) e_k for every k;
  T1b  block 34's transform: (P theta)^_k = conj(phi) theta^_k (the stated '(P theta)^_k = phi theta^_k' fails on every mode with phi non-real);
       the +ik transform sum e^{ik.x} theta_x has multiplier phi;
  T1c  the runner's own Sigma_{t,t+s}: e_k^H Sigma_{t,t+s} e_k = phi^s e_k^H Sigma_t e_k and L^{-2} e_k^H Sigma_t e_k = (1 - u^t)/(1 - u): so with
       block 34's transform and Cov(X, Y) = E[X conj Y] (the pairing of the note's executed observable), Cov(theta^_k(t), theta^_k(t+s)) =
       phi^s Var theta^_k(t) holds as displayed; the conjugate pairing gives conj(phi)^s; they differ exactly where phi^s is not real (counted);
  T1d  (I - P P^T) phi^s e_k = (1 - u)(P^T)^s e_k: the stationary operator C_s = (I - PP^T)^{-1}(P^T)^s has eigenvalue phi^s/(1 - u) on e_k;
  T1e  the transform of the forward space-time correlation c(r) = Cov(theta_{0,t}, theta_{r,t+s}): sum_r e^{-ik.r} c(r) = conj(phi)^s (1 - u^t)/(1 - u);
  T1f  convention-free: with c = cos(k.x), s = sin(k.x): c'Sc + s'Ss = Re(phi^s) W and c'Ss - s'Sc = Im(phi^s) W (S = Sigma_{t,t+s},
       W = c'Sigma_t c + s'Sigma_t s); cosine characters alone give Re(phi^s) = Re(conj(phi)^s) (the runner's B2 cannot see the conjugation).
T3 (symbolic; one labelled numerical cross-check):
  T3a  E(K) = 3(|1 - phi(k) e^{iw}|^2 + 1 - u(k)), k = (K1 - K3, K2 - K3), w = K3;
  T3b  the formation law on Z^3, theta(X) = (1/3) sum_a theta(X - e_a) + xi(X), has symbol 1 - conj(phi(k)) e^{-iw}: S_F = sigma^2/|1 - phi e^{iw}|^2,
       hence E = 3 sigma^2/S_F + 3(1 - u) exactly;
  T3c  the runner's D2 test (a non-vanishing mixed derivative of the logarithm) returns 'not a product' for BOTH kernels, in the lattice frame
       and in the level frame (exact algebraic values at an algebraic point, minimal polynomials);
  T3d  the comparator in the (k, tau) representation: G(tau) = z^tau/(6y) (tau >= 0), conj(z)^|tau|/(6y) (tau <= 0), z = conj(phi)/(1 + y),
       y = sqrt(1 - u), solves (6 - 3 phi S+ - 3 conj(phi) S-) G = delta_0 exactly; |z|^2 = (1 - y)/(1 + y);
  T3e  the phase identity: G^(k, tau)/C^_tau(k) = y/(6 sigma^2 (1 + y)^|tau|) > 0 (same phase conj(phi)^tau for both kernels);
  T3f  the rates per level: -log|phi| = -(1/2) log(1 - y^2) = y^2/2 + O(y^4), -log|z| = artanh y = y + O(y^3); y^2 = k'Mk + O(|k|^4);
  T3g  (numerical, 30 digits, labelled) the Fourier integral (1/2pi) int e^{iw tau}/E(k, w) dw against T3d's G at one k, tau = -2..3.
"""
import itertools
import sys
import time
from fractions import Fraction as F

import sympy as sp

FAILS = []
T0 = time.time()


def check(label, ok, detail):
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {detail}")
    if not ok:
        FAILS.append(label)


# ------------------------------------------------------------------------------------------------ exact arithmetic in Q(sqrt3, i)
class Q3:
    """(a + b sqrt3) + i (c + d sqrt3), a..d Fractions."""

    __slots__ = ("a", "b", "c", "d")

    def __init__(self, a=0, b=0, c=0, d=0):
        self.a, self.b, self.c, self.d = F(a), F(b), F(c), F(d)

    def __add__(self, o):
        o = q3(o)
        return Q3(self.a + o.a, self.b + o.b, self.c + o.c, self.d + o.d)

    __radd__ = __add__

    def __neg__(self):
        return Q3(-self.a, -self.b, -self.c, -self.d)

    def __sub__(self, o):
        return self + (-q3(o))

    def __rsub__(self, o):
        return q3(o) - self

    def __mul__(self, o):
        o = q3(o)

        def m(p, q, r, s):  # (p + q sqrt3)(r + s sqrt3)
            return (p * r + 3 * q * s, p * s + q * r)
        xx, yy = m(self.a, self.b, o.a, o.b), m(self.c, self.d, o.c, o.d)
        xy, yx = m(self.a, self.b, o.c, o.d), m(self.c, self.d, o.a, o.b)
        return Q3(xx[0] - yy[0], xx[1] - yy[1], xy[0] + yx[0], xy[1] + yx[1])

    __rmul__ = __mul__

    def __pow__(self, n):
        r = Q3(1)
        for _ in range(n):
            r = r * self
        return r

    def conj(self):
        return Q3(self.a, self.b, -self.c, -self.d)

    def re(self):
        return Q3(self.a, self.b)

    def im(self):
        return Q3(self.c, self.d)

    def is_real(self):
        return self.c == 0 and self.d == 0

    def __eq__(self, o):
        o = q3(o)
        return (self.a, self.b, self.c, self.d) == (o.a, o.b, o.c, o.d)

    def __hash__(self):
        return hash((self.a, self.b, self.c, self.d))

    def __repr__(self):
        return f"({self.a}+{self.b}r3)+i({self.c}+{self.d}r3)"


def q3(x):
    return x if isinstance(x, Q3) else Q3(x)


def root_of_unity(L):
    return {3: Q3(F(-1, 2), 0, 0, F(1, 2)), 4: Q3(0, 0, 1, 0)}[L]


def matvec(A, v):
    return [sum((A[i][j] * v[j] for j in range(len(v)) if A[i][j] != 0), Q3()) for i in range(len(A))]


def dot(u, v):  # u^T v (no conjugation)
    return sum((a * b for a, b in zip(u, v)), Q3())


def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][l] * B[l][j] for l in range(m)) for j in range(p)] for i in range(n)]


def transpose(A):
    return [list(r) for r in zip(*A)]


def torus(L):
    sites = list(itertools.product(range(L), repeat=2))
    idx = {x: i for i, x in enumerate(sites)}
    N = L * L
    P = [[F(0)] * N for _ in range(N)]
    for (i, j) in sites:
        for (a, b) in ((i, j), ((i - 1) % L, j), (i, (j - 1) % L)):
            P[idx[(i, j)]][idx[(a, b)]] += F(1, 3)
    w = root_of_unity(L)
    pw = [w ** m for m in range(L)]
    modes = {}
    for n in itertools.product(range(L), repeat=2):
        e = [pw[(n[0] * x[0] + n[1] * x[1]) % L] for x in sites]
        ph = (1 + pw[n[0]] + pw[n[1]]) * Q3(F(1, 3))
        modes[n] = (e, ph)
    return sites, idx, P, modes


# ================================================================================================ T1
def section_T1():
    print("=" * 110)
    print("T1  the conventions of the space-time covariance, exact on the tori L = 3, 4 (the runner's own recursion)")
    res = {}
    ok_a = ok_b = ok_c = ok_d = ok_e = ok_f = True
    for L in (3, 4):
        sites, idx, P, modes = torus(L)
        N = L * L
        PT = transpose(P)
        # T1a / T1b
        th = [Q3(F((7 * i + 3) % 11 - 5, 1 + (i % 4))) for i in range(N)]   # a generic rational field
        Pth = matvec(P, th)
        nonreal_modes = b34_fail = 0
        for n, (e, ph) in modes.items():
            ok_a &= matvec(PT, e) == [ph * v for v in e] and matvec(P, e) == [ph.conj() * v for v in e]
            ebar = [v.conj() for v in e]
            hat = dot(ebar, th) * Q3(F(1, L))            # block 34: theta^_k = L^{-1} sum e^{-ik.x} theta_x
            hatP = dot(ebar, Pth) * Q3(F(1, L))
            chk = dot(e, th) * Q3(F(1, L))               # the +ik transform
            chkP = dot(e, Pth) * Q3(F(1, L))
            ok_b &= hatP == ph.conj() * hat and chkP == ph * chk
            if n != (0, 0) and not ph.is_real():
                nonreal_modes += 1
                b34_fail += int(not (hatP == ph * hat))
        # the runner's recursion
        T = 6 if L == 3 else 4
        I = [[F(int(i == j)) for j in range(N)] for i in range(N)]
        Ps = [I]
        for s in range(1, 4):
            Ps.append(matmul(Ps[-1], P))
        PsT = [transpose(M) for M in Ps]
        Sig = [[F(0)] * N for _ in range(N)]
        differ = pairs = 0
        for t in range(1, T + 1):
            Sig = [[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(matmul(matmul(P, Sig), PT), I)]
            cross = {s: matmul(Sig, PsT[s]) for s in range(1, 4)}
            ones = [Q3(1)] * N
            for s in range(1, 4):   # the zero mode: 1' Sigma_{t,t+s} 1 / N^2 = t/N (sigma^2 = 1)
                ok_c &= dot(ones, matvec(cross[s], ones)) == Q3(F(t, 1) * N)
            for n, (e, ph) in modes.items():
                if n == (0, 0):
                    continue
                ebar = [v.conj() for v in e]
                u = (ph * ph.conj()).a
                V = dot(ebar, matvec(Sig, e))             # = L^2 Var theta^_k(t)
                ok_c &= V == Q3(N * (1 - u ** t) / (1 - u))
                cvec, svec = [v.re() for v in e], [v.im() for v in e]
                W = dot(cvec, matvec(Sig, cvec)) + dot(svec, matvec(Sig, svec))
                for s in range(1, 4):
                    S = cross[s]
                    lhs = dot(ebar, matvec(S, e))           # e^H Sigma_{t,t+s} e = L^2 E[theta^_k(t) conj theta^_k(t+s)]
                    ok_c &= lhs == (ph ** s) * V
                    conj_pair = dot(e, matvec(S, ebar))     # = L^2 E[conj theta^_k(t) theta^_k(t+s)]
                    ok_c &= conj_pair == (ph.conj() ** s) * V
                    if t == 1:
                        pairs += 1
                        differ += int(not (ph ** s).is_real())
                        # T1d: the stationary operator's eigen-relation (independent of t)
                        PPT_e = matvec(P, matvec(PT, [(ph ** s) * v for v in e]))
                        lhs_d = [(ph ** s) * v - x for v, x in zip(e, PPT_e)]
                        rhs_d = [Q3(1 - u) * x for x in matvec(PsT[s], e)]
                        ok_d &= lhs_d == rhs_d
                    # T1e: the transform of the forward correlation c(r) = [Sigma_{t,t+s}]_{0, r}
                    row0 = S[idx[(0, 0)]]
                    tr = sum((Q3(row0[idx[r]]) * ebar[idx[r]] for r in sites), Q3())
                    ok_e &= tr == (ph.conj() ** s) * Q3((1 - u ** t) / (1 - u))
                    # T1f: the real sine-cosine identities, and the cosine-only ratio's blindness
                    cc = dot(cvec, matvec(S, cvec)) + dot(svec, matvec(S, svec))
                    cs = dot(cvec, matvec(S, svec)) - dot(svec, matvec(S, cvec))
                    ok_f &= cc == (ph ** s).re() * W and cs == (ph ** s).im() * W
                    ok_f &= (ph ** s).re() == (ph.conj() ** s).re()
        res[L] = dict(nonreal_modes=nonreal_modes, b34_fail=b34_fail, differ=differ, pairs=pairs, modes=N - 1)
    r3, r4 = res[3], res[4]
    check("T1a", ok_a, "on L = 3, 4, every character e_k(x) = e^{ik.x} has P^T e_k = phi(k) e_k and P e_k = conj(phi(k)) e_k, exactly in Q(sqrt3, i)")
    check("T1b", ok_b and r3["b34_fail"] == r3["nonreal_modes"] and r4["b34_fail"] == r4["nonreal_modes"],
          f"block 34's transform theta^_k = L^-1 sum e^(-ik.x) theta_x has (P theta)^_k = conj(phi) theta^_k for a generic rational field, so "
          f"block 34 T1.1's '(P theta)^_k = phi(k) theta^_k' fails on every nonzero mode with phi non-real ({r3['nonreal_modes']} of {r3['modes']} "
          f"on L = 3, {r4['nonreal_modes']} of {r4['modes']} on L = 4); the +ik transform sum e^(ik.x) theta_x has multiplier phi")
    check("T1c", ok_c, f"with the runner's own exact Sigma_t and Sigma_(t,t+s) = Sigma_t (P^s)^T (t <= 6 on L = 3, t <= 4 on L = 4, s = 1, 2, 3): "
          f"L^-2 e^H Sigma_t e = (1 - u^t)/(1 - u), and e^H Sigma_(t,t+s) e = phi^s e^H Sigma_t e, i.e. Cov(theta^_k(t), theta^_k(t+s)) = "
          f"E[theta^_k(t) conj theta^_k(t+s)] = phi^s Var theta^_k(t) as block 35 displays it, while the conjugate pairing "
          f"E[conj theta^_k(t) theta^_k(t+s)] gives conj(phi)^s Var; the two differ on {r3['differ']} of {r3['pairs']} (mode, s) pairs on L = 3 "
          f"and {r4['differ']} of {r4['pairs']} on L = 4 (exactly those with phi^s not real); the plane average: t/L^2")
    check("T1d", ok_d, "(I - P P^T) phi^s e_k = (1 - u)(P^T)^s e_k for every nonzero mode and s = 1, 2, 3: the stationary operator "
          "C_s = sigma^2 (I - P P^T)^{-1} (P^T)^s = lim Sigma_(t,t+s) has eigenvalue sigma^2 phi(k)^s/(1 - u) on e^{ik.x}")
    check("T1e", ok_e, "the transform of the forward space-time correlation c(r) = Cov(theta_(0,t), theta_(r,t+s)): sum_r e^(-ik.r) c(r) = "
          "conj(phi)^s (1 - u^t)/(1 - u) exactly: read as the Fourier coefficient of the correlation in the forward displacement, the kernel "
          "carries conj(phi)^s, the conjugate of the display")
    check("T1f", ok_f, "convention-free form, exact: with the real characters c = cos(k.x), s = sin(k.x), c'Sc + s'Ss = Re(phi^s) W and "
          "c'Ss - s'Sc = Im(phi^s) W (S = Sigma_(t,t+s), W = c'Sigma_t c + s'Sigma_t s): the covariance of the cosine amplitude at level t with "
          "the sine amplitude at level t+s fixes the sign of Im(phi^s); cosine characters alone see Re(phi^s) = Re(conj(phi)^s), which is why "
          "the runner's B2 passed under either reading")
    return res


# ================================================================================================ T3
def exact_nonzero(val):
    x = sp.Symbol("x")
    mp = sp.minimal_polynomial(val, x)
    return mp != x, mp


def section_T3():
    print("=" * 110)
    print("T3  the product-structure claim is representation-dependent; what separates the kernels")
    K1, K2, K3, k1, k2, w = sp.symbols("K1 K2 K3 k1 k2 w", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    sub = {K1: k1 + w, K2: k2 + w, K3: w}
    u = sp.expand(sp.expand_complex(phi * sp.conjugate(phi)))
    E = sum(2 * (1 - sp.cos(K)) for K in (K1, K2, K3))
    absq = sp.expand_complex((1 - phi * sp.exp(sp.I * w)) * sp.conjugate(1 - phi * sp.exp(sp.I * w)))
    ident = sp.simplify(sp.expand(sp.expand_trig(E.subs(sub) - 3 * (absq + 1 - u)))) == 0
    check("T3a", ident, "E(K) = 3(|1 - phi(k) e^{iw}|^2 + 1 - u(k)) exactly, k = (K1 - K3, K2 - K3), w = K3 (the level planes X1 + X2 + X3 = const, "
          "in-plane coordinates (X1, X2), predecessors X - e_a)")
    # T3b: the formation law's symbol on Z^3 in the lattice frame
    symb = sp.Rational(1, 3) * sum(sp.exp(-sp.I * K) for K in (K1, K2, K3))
    ok_b = sp.simplify(sp.expand(symb.subs(sub) - sp.exp(-sp.I * w) * sp.conjugate(phi))) == 0
    D_lat = sp.expand_complex((1 - sp.Rational(1, 3) * sum(sp.exp(sp.I * K) for K in (K1, K2, K3))) *
                              sp.conjugate(1 - sp.Rational(1, 3) * sum(sp.exp(sp.I * K) for K in (K1, K2, K3))))
    ok_b &= sp.simplify(sp.expand(sp.expand_trig(D_lat.subs(sub) - absq))) == 0
    ok_b &= sp.simplify(sp.expand(sp.expand_trig(E - 3 * D_lat - 3 * (1 - u.subs({k1: K1 - K3, k2: K2 - K3}))))) == 0
    check("T3b", ok_b, "the formation law on Z^3, theta(X) = (1/3) sum_a theta(X - e_a) + xi(X), has symbol 1 - (1/3) sum_a e^{-iK_a} = 1 - conj(phi(k)) e^{-iw}, "
          "so its space-time spectral density is S_F = sigma^2/|1 - (1/3) sum_a e^{iK_a}|^2 = sigma^2/|1 - phi(k) e^{iw}|^2, and E = 3 sigma^2/S_F + 3(1 - u(k)) exactly")
    # T3c: the runner's D2 test applied to both kernels, exactly, in both frames
    out = []
    ok_c = True
    pt_lat = {K1: sp.pi / 2, K2: sp.pi / 3, K3: sp.pi / 6}
    pt_lev = {k1: sp.pi / 3, k2: sp.pi / 6, w: sp.pi / 2}
    for name, f, a, b, pt in (("log E, lattice (K1,K3)", E, K1, K3, pt_lat), ("log S_F, lattice (K1,K3)", D_lat, K1, K3, pt_lat),
                              ("log E, level (k1,w)", E.subs(sub), k1, w, pt_lev), ("log S_F, level (k1,w)", absq, k1, w, pt_lev)):
        num = f * sp.diff(f, a, b) - sp.diff(f, a) * sp.diff(f, b)     # f^2 * d2 log f / da db
        val = sp.nsimplify(sp.radsimp(sp.expand(sp.expand_trig(num.subs(pt)))))
        nz, mp = exact_nonzero(val)
        ok_c &= nz
        out.append(f"{name}: f^2 d2(log f) = {val} (min. poly {mp})")
    check("T3c", ok_c, "the runner's D2 test (a non-vanishing mixed derivative of the logarithm) returns 'not a product' for the comparator AND for the "
          "formation kernel, in the lattice frame at K = (pi/2, pi/3, pi/6) and in the level frame at (k1, k2, w) = (pi/3, pi/6, pi/2) (exact algebraic "
          "values, nonzero by their minimal polynomials; S_F enters through f = 1/S_F up to sigma^2, same mixed derivative up to sign): " + "; ".join(out))
    # T3d: the comparator in the (k, tau) representation, exactly
    p, q, y = sp.symbols("p q y")          # p = phi, q = conj(phi), y = sqrt(1 - p q)
    rel = y ** 2 - (1 - p * q)

    def red(expr):
        num = sp.numer(sp.together(sp.expand(expr)))
        return sp.rem(sp.expand(num), rel, y) == 0
    z, zb = q / (1 + y), p / (1 + y)
    A = 1 / (6 * y)

    def G(tau):
        return A * z ** tau if tau >= 0 else A * zb ** (-tau)
    ok_d = all(red(6 * G(t) - 3 * p * G(t + 1) - 3 * q * G(t - 1) - (1 if t == 0 else 0)) for t in range(-4, 5))
    ok_d &= red(p * z ** 2 - 2 * z + q) and red(q * zb ** 2 - 2 * zb + p)
    ok_d &= red(z * zb - (1 - y) / (1 + y))
    zp = (1 + y) / p
    ok_d &= red(p * zp ** 2 - 2 * zp + q)
    check("T3d", ok_d, "with E(k, w) = 6 - 3 phi e^{iw} - 3 conj(phi) e^{-iw}, the sequence G(tau) = z^tau/(6y) (tau >= 0), conj(z)^|tau|/(6y) (tau <= 0), "
          "z = conj(phi)/(1 + y), y = sqrt(1 - u), solves 6G(tau) - 3 phi G(tau+1) - 3 conj(phi) G(tau-1) = delta_(tau,0) exactly (tau = -4..4; the "
          "tau != 0 equations reduce to phi z^2 - 2z + conj(phi) = 0); the other root is (1 + y)/phi; |z|^2 = (1 - y)/(1 + y) < 1: the comparator in "
          "the (k, tau) representation is a plane factor 1/(6y) times a propagator z^|tau| (conjugated for tau < 0)")
    # T3e: the phase identity
    s2 = sp.Symbol("sigma2", positive=True)
    ok_e = True
    for tau in range(0, 6):
        C_hat = s2 * q ** tau / y ** 2                       # the formation kernel's transform (T1e, stationary: V = sigma^2/(1 - u) = sigma^2/y^2)
        ok_e &= red(G(tau) / C_hat - y / (6 * s2 * (1 + y) ** tau))
    check("T3e", ok_e, "the phase identity: for tau = 0..5, G^(k, tau)/C^_tau(k) = y/(6 sigma^2 (1 + y)^tau), real and positive, where C^_tau(k) = sigma^2 "
          "conj(phi)^tau/(1 - u) is the formation kernel's transform in the same convention (T1e): both kernels carry the same phase conj(phi(k))^tau, "
          "so the drift along the (1,1,1) axis is common to both and does not separate them")
    # T3f: the rates
    Y = sp.Symbol("Y", positive=True)
    rF = sp.series(-sp.log(1 - Y ** 2) / 2, Y, 0, 6).removeO()
    rC = sp.series(sp.log((1 + Y) / (1 - Y)) / 2, Y, 0, 6).removeO()
    rA = sp.series(sp.atanh(Y), Y, 0, 6).removeO()
    ok_f = sp.expand(rF - (Y ** 2 / 2 + Y ** 4 / 4)) == 0 and sp.expand(rC - (Y + Y ** 3 / 3 + Y ** 5 / 5)) == 0 and sp.expand(rC - rA) == 0
    # -log|z| = -(1/2) log|z|^2 = (1/2) log((1 + y)/(1 - y)) by T3d; -log|phi| = -(1/2) log u = -(1/2) log(1 - y^2)
    eps, a, b = sp.symbols("epsilon a b", real=True)
    uab = u.subs({k1: eps * a, k2: eps * b})
    ser = sp.series(1 - uab, eps, 0, 4).removeO()
    ok_f &= sp.simplify(ser - eps ** 2 * (2 * a ** 2 - 2 * a * b + 2 * b ** 2) / 9) == 0
    check("T3f", ok_f, "per level the formation propagator decays at rate -log|phi| = -(1/2) log(1 - y^2) = y^2/2 + y^4/4 + O(y^6), the comparator's at "
          "-log|z| = (1/2) log((1 + y)/(1 - y)) = artanh y = y + y^3/3 + y^5/5 + O(y^7), with y^2 = 1 - u(k) = k'Mk + O(|k|^4), M = (1/9)[[2,-1],[-1,2]] "
          "(series in epsilon for k = epsilon (a, b)): rates of order |k|^2 (diffusive) against |k| (elliptic); plane factors sigma^2/y^2 against 1/(6y)")
    # T3g: numerical cross-check of the transform's sign convention (labelled)
    import mpmath as mpm
    mpm.mp.dps = 30
    kv = (mpm.mpf("0.7"), mpm.mpf("-0.4"))
    phv = (1 + mpm.exp(1j * kv[0]) + mpm.exp(1j * kv[1])) / 3
    yv = mpm.sqrt(1 - abs(phv) ** 2)
    zv = mpm.conj(phv) / (1 + yv)

    def Ew(wv):
        return 6 - 2 * (mpm.cos(kv[0] + wv) + mpm.cos(kv[1] + wv) + mpm.cos(wv))

    def Gnum(tau):
        return mpm.quad(lambda wv: mpm.exp(1j * wv * tau) / Ew(wv), [-mpm.pi, mpm.pi]) / (2 * mpm.pi)

    errs = []
    for tau in range(-2, 4):
        ref = zv ** tau / (6 * yv) if tau >= 0 else mpm.conj(zv) ** (-tau) / (6 * yv)
        errs.append(abs(Gnum(tau) - ref))
    err = max(errs)
    check("T3g", err < mpm.mpf(10) ** (-20), f"(numerical, 30 digits, labelled) at k = (0.7, -0.4): (1/2pi) int e^(i w tau)/E(k, w) dw equals T3d's G(tau) "
          f"for tau = -2..3 to {mpm.nstr(err, 3)}; |z| = {mpm.nstr(abs(zv), 10)} against |phi| = {mpm.nstr(abs(phv), 10)}")


def main():
    res = section_T1()
    section_T3()
    print("=" * 110)
    print(f"runtime {time.time() - T0:.0f}s")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} ({FAILS})")
        return 0
    r3, r4 = res[3], res[4]
    core = ("corrigendum for PR #8180: T1's display Cov(theta^_k(t), theta^_k(t+s)) = phi^s Var holds exactly with block 34's transform "
            "L^-1 sum e^(-ik.x) theta_x and the pairing E[X conj Y] of the note's own executed observable, and C_s = sigma^2 (I - PP*)^-1 P*^s "
            "has eigenvalue sigma^2 phi^s/(1 - u) on e^(ik.x); the proof's line theta^_k(t+s) = phi^s theta^_k(t) + noise is false in that transform "
            "(the multiplier is conj(phi), as in block 34 T1.1, same slip); in the conjugate readings (the +ik transform with E[X conj Y], or the "
            "Fourier coefficient of the forward correlation) the kernel is conj(phi)^s/(1 - u); all readings agree exactly where phi^s is real "
            f"({r3['pairs'] - r3['differ']} of {r3['pairs']} (mode, s) pairs on L = 3, {r4['pairs'] - r4['differ']} of {r4['pairs']} on L = 4); "
            "convention-free: c'Sc + s'Ss = Re(phi^s) W, c'Ss - s'Sc = Im(phi^s) W. T3/D2: the mixed-derivative test calls both kernels "
            "non-products (lattice and level frames); in (k, tau) both are a positive plane factor times the same phase conj(phi)^tau times "
            "exp(-|tau| rho), rho_F = -(1/2) log(1 - y^2) ~ y^2/2 against rho_C = artanh y ~ y, y = sqrt(1 - u); "
            "G^/C^ = y/(6 sigma^2 (1 + y)^|tau|); E = 3 sigma^2/S_F + 3(1 - u)")
    print("SUMMARY: PROVED (ATTEMPT.md S1-S9; finite facts CHECKED here) " + core)
    print("HIT: " + core)
    return 0


if __name__ == "__main__":
    sys.exit(main())
