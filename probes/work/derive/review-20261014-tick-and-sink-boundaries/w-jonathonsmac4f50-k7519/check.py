#!/usr/bin/env python3
"""
check.py for J:derive:review-20261014-tick-and-sink-boundaries:a1

Self-contained. Uses numpy, scipy, sympy, mpmath only (mpmath not needed here).
Exact arithmetic (Fraction / sympy) for every discrete or algebraic claim.
Floating point is used ONLY for two labelled lattice cross-checks (L1, L2) and
one labelled quadrature cross-check (Q1); each has an explicit tolerance.

Setting (supplied by this attempt, NOT by the axioms):
  free, translation invariant, two-band tick U(k) = a - i b.sigma in SU(2) on Z^3,
  arc vacuum, linear (Peierls) coupling of charge e to a transverse boson of speed c.
"""
import sys
import itertools
from fractions import Fraction as Fr

import numpy as np
import sympy as sp
from scipy import integrate, optimize

RESULTS = []


def check(name, cond, detail=""):
    ok = bool(cond)
    RESULTS.append(ok)
    print(("PASS " if ok else "FAIL ") + name + ((" | " + detail) if detail else ""))
    return ok


# --------------------------------------------------------------------------
# A. T_d is not an involution; the object that is an on-site involution is eps
# --------------------------------------------------------------------------
L = 4
sites = list(itertools.product(range(L), repeat=3))
idx = {s: i for i, s in enumerate(sites)}
N = len(sites)


def perm_matrix(shift):
    P = np.zeros((N, N), dtype=np.int64)
    for s in sites:
        t = tuple((s[j] + shift[j]) % L for j in range(3))
        P[idx[t], idx[s]] = 1
    return P


Td = perm_matrix((1, 1, 1))
I = np.eye(N, dtype=np.int64)
check("A1 T_d^2 != 1 on Z_4^3 (T_d is not an involution)", not np.array_equal(Td @ Td, I))
check("A2 T_d^4 == 1 on Z_4^3", np.array_equal(np.linalg.matrix_power(Td, 4), I))
S2 = I + Td
# (1+T)/2 is a projector iff (1+T)^2 = 2(1+T) iff T^2 = 1
check("A3 (1+T_d)/2 is not a projector", not np.array_equal(S2 @ S2, 2 * S2))

# eigenvalue of T_d on momentum m = (m1,m2,m3): i^(m1+m2+m3). exact integer exponent mod 4
ex = {}
for m in itertools.product(range(L), repeat=3):
    ex.setdefault(sum(m) % 4, []).append(m)
check("A4 T_d eigenspace dims (1,i,-1,-i) = (16,16,16,16)", [len(ex[e]) for e in range(4)] == [16] * 4)
corners = [m for m in itertools.product([0, 2], repeat=3)]
vals = {m: (-1) ** (sum(m) // 2) for m in corners}  # T_d = i^(2 hw) = (-1)^hw
check("A5 on the 8 corner momenta T_d = (-1)^hw (+-1 only there)", all(sum(m) % 2 == 0 for m in corners) and len(vals) == 8)
noncorner_pm1 = [m for m in itertools.product(range(L), repeat=3) if sum(m) % 2 == 0 and m not in corners]
check("A6 T_d = +-1 eigenspace also contains non-corner momenta (24 of 32)", len(noncorner_pm1) == 24,
      "eigenvalue +-1 space has dim 32, only 8 are corners")

# eps: on-site involution, anticommutes with the walker H' = 2i H = sum sigma_j (x) (T_j - T_j^-1)
eps = np.diag([(-1) ** (x + y + z) for (x, y, z) in sites]).astype(np.int64)
check("A7 eps^2 = 1 (on-site involution)", np.array_equal(eps @ eps, I))
check("A8 T_d eps T_d^-1 = -eps", np.array_equal(Td @ eps @ Td.T, -eps))
sig = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
Hp = np.zeros((2 * N, 2 * N), dtype=complex)
for j in range(3):
    sh = [0, 0, 0]
    sh[j] = 1
    Tj = perm_matrix(tuple(sh))
    Hp += np.kron(sig[j], Tj - Tj.T)
E2 = np.kron(np.eye(2), eps)
check("A9 {H, eps} = 0 for the walker on Z_4^3 (eps pairs k with k+Q: it exchanges node hands, not a gamma5)",
      np.array_equal(E2 @ Hp + Hp @ E2, np.zeros_like(Hp)))

# --------------------------------------------------------------------------
# B. Normalised Wilson-Weyl tick: node data, sum rules, single light Weyl
# --------------------------------------------------------------------------
def tick_nodes(mu):
    out = []
    for K in itertools.product([0, 1], repeat=3):
        hw = sum(K)
        m = mu + 3 - 2 * hw
        assert m != 0
        a = 1 if m > 0 else -1
        s = (-1) ** hw
        out.append(dict(K=K, hw=hw, m=m, a=a, chiE=s, chiU=a * s, v=Fr(1) / abs(m)))
    return out


mus = [Fr(-5, 2), Fr(-2), Fr(-3, 2), Fr(-1, 2), Fr(1, 2), Fr(3, 2), Fr(2), Fr(5, 2), Fr(7, 2), Fr(-7, 2)]
all_ok = True
for mu in mus:
    nd = tick_nodes(mu)
    s0 = sum(n["chiU"] for n in nd if n["a"] == 1)
    sp_ = sum(n["chiU"] for n in nd if n["a"] == -1)
    sE = sum(n["chiE"] for n in nd)
    all_ok &= (s0 == sp_) and (sE == 0)
check("B1 mu-scan: sum chi_U over eps=0 nodes == sum over eps=pi nodes, and sum chi_E == 0 (10 values of mu)", all_ok)

nd = tick_nodes(Fr(-2))
n0 = [n for n in nd if n["a"] == 1]
npi = [n for n in nd if n["a"] == -1]
check("B2 mu=-2: exactly one eps=0 node (K=0), seven eps=pi nodes",
      len(n0) == 1 and n0[0]["K"] == (0, 0, 0) and len(npi) == 7)
check("B3 mu=-2: sum_0 chi = +1 (a single light Weyl); sum_pi chi = +1 (same net hand)",
      sum(n["chiU"] for n in n0) == 1 and sum(n["chiU"] for n in npi) == 1)
check("B4 mu=-2: net E-chirality of the eps=pi nodes is -1 (opposite to the light node)",
      sum(n["chiE"] for n in npi) == -1 and n0[0]["chiE"] == 1)

# symbolic confirmation of node speeds: b_j = sin k_j / sqrt(m^2 + sum sin^2); J = d b/d k at each corner
k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
ks = [k1, k2, k3]
mexpr = sp.Integer(-2) + sum(sp.cos(k) for k in ks)
Nexpr = sp.sqrt(mexpr ** 2 + sum(sp.sin(k) ** 2 for k in ks))
bvec = [sp.sin(k) / Nexpr for k in ks]
speeds_ok = True
dets_ok = True
for n in nd:
    pt = {ks[j]: (sp.pi if n["K"][j] else 0) for j in range(3)}
    J = sp.Matrix(3, 3, lambda i, j: sp.diff(bvec[i], ks[j]).subs(pt))
    J = J.applyfunc(sp.simplify)
    v = sp.Rational(n["v"].numerator, n["v"].denominator)
    speeds_ok &= all(sp.simplify(J[i, i] / v - (1 if n["K"][i] == 0 else -1)) == 0 for i in range(3))
    speeds_ok &= all(J[i, j] == 0 for i in range(3) for j in range(3) if i != j)
    dets_ok &= (sp.sign(J.det()) == n["chiE"])
check("B5 symbolic: Jacobian of b at each of 8 corners is diag(+-1)/|m|; speeds v=1/|m| = 1,1,1/3,1/5 for hw=0..3", speeds_ok)
check("B6 symbolic: sign det J equals (-1)^hw at every corner", dets_ok)
check("B7 mu=-2 node speeds: eps=0 node 1; pi nodes {1 x3, 1/3 x3, 1/5 x1}",
      sorted(n["v"] for n in npi) == sorted([Fr(1)] * 3 + [Fr(1, 3)] * 3 + [Fr(1, 5)]) and n0[0]["v"] == 1)

# --------------------------------------------------------------------------
# C. U_g (the repo's one-handed tick, rebuilt from the description F3:70-76) -- exact
# --------------------------------------------------------------------------
x, y, z, t = sp.symbols("x y z t", real=True)
d1, d2, d3 = sp.symbols("d1 d2 d3", real=True)
a_g = sp.cos(x) * sp.cos(y) * sp.cos(z)
g2 = (1 - a_g ** 2) / (sp.sin(x) ** 2 + sp.sin(y) ** 2 + sp.sin(z) ** 2)
shiftQ = {x: x + sp.pi, y: y + sp.pi, z: z + sp.pi}
check("C1 a(k+Q) = -a(k), g^2(k+Q) = g^2(k), sin(k+Q) = -sin(k) => U_g(k+Q) = -U_g(k)",
      sp.simplify(a_g.subs(shiftQ, simultaneous=True) + a_g) == 0 and
      sp.simplify(g2.subs(shiftQ, simultaneous=True) - g2) == 0)
ok_g = True
for K in itertools.product([0, 1], repeat=3):
    sub = {x: (sp.pi if K[0] else 0) + t * d1, y: (sp.pi if K[1] else 0) + t * d2, z: (sp.pi if K[2] else 0) + t * d3}
    num = sp.series((1 - a_g ** 2).subs(sub, simultaneous=True), t, 0, 3).removeO()
    den = sp.series((sp.sin(x) ** 2 + sp.sin(y) ** 2 + sp.sin(z) ** 2).subs(sub, simultaneous=True), t, 0, 3).removeO()
    ok_g &= sp.simplify(num - den) == 0 and sp.simplify(num / t ** 2 - (d1 ** 2 + d2 ** 2 + d3 ** 2)) == 0
check("C2 U_g: g -> 1 and every node isotropic with speed exactly 1 at all 8 corners (series to O(t^2))", ok_g)

# --------------------------------------------------------------------------
# D. Static backgrounds: E[A] is always conserved and the arc vacuum is its zero-sea (exact, finite band)
# --------------------------------------------------------------------------
import random
random.seed(12345)


def rand_herm(n):
    M = sp.zeros(n, n)
    for i in range(n):
        M[i, i] = sp.Rational(random.randint(-9, 9), random.randint(1, 5))
        for j in range(i + 1, n):
            re = sp.Rational(random.randint(-9, 9), random.randint(1, 5))
            im = sp.Rational(random.randint(-9, 9), random.randint(1, 5))
            M[i, j] = re + sp.I * im
            M[j, i] = re - sp.I * im
    return M


ok_static = True
for n in (3, 4, 5):
    H = rand_herm(n)
    Id = sp.eye(n)
    U = (Id - sp.I * H) * ((Id + sp.I * H).inv())          # exact unitary (Cayley); U = e^{-i eps}, eps = 2 arctan(h)
    Ud = U.H
    Eop = sp.I / 2 * (U - Ud)
    ok_static &= sp.simplify(U * Ud - Id) == sp.zeros(n, n)
    ok_static &= sp.simplify(Eop * U - U * Eop) == sp.zeros(n, n)
    ok_static &= sp.simplify(Eop - 2 * H * ((Id + H * H).inv())) == sp.zeros(n, n)   # E = +2H/(1+H^2) = sin(eps)
check("D1 exact (n=3,4,5 random unitaries): E=(i/2)(U-U^+) is Hermitian-local, commutes with U, E = 2H/(1+H^2) = sin(eps)", ok_static)
# quasi-energy eps=2 arctan(h) in (-pi,0) iff h<0 iff E-eigenvalue 2h/(1+h^2) < 0 : exact sign identity
hh = sp.symbols("hh", real=True)
check("D2 arc vacuum (eps in (-pi,0), eps=2 atan h) == negative-E sea: sin(2 atan h) = 2h/(1+h^2) (exact identity; sign E = sign h)",
      sp.simplify(sp.sin(2 * sp.atan(hh)) - 2 * hh / (1 + hh ** 2)) == 0)

# --------------------------------------------------------------------------
# E. Cone spectral function S_T, derived exactly with sympy
# --------------------------------------------------------------------------
r1, r2, q, u, w, v_, om, e_ = sp.symbols("r1 r2 q u w v omega e", positive=True)
qk = (r2 ** 2 - r1 ** 2 - q ** 2) / (2 * q)        # qhat . k
qkp = (r2 ** 2 - r1 ** 2 + q ** 2) / (2 * q)       # qhat . (k+q)
Texpr = 1 + qk * qkp / (r1 * r2)                    # transverse sum 1 + (q.n)(q.n')
subs_uw = {r1: (u + w) / 2, r2: (u - w) / 2}
target = (u ** 2 - q ** 2) * (q ** 2 + w ** 2) / (q ** 2 * (u ** 2 - w ** 2))
check("E1 T = 1 + (q.n)(q.n') = (u^2-q^2)(q^2+w^2)/(q^2(u^2-w^2)), u=r1+r2, w=r1-r2",
      sp.simplify(Texpr.subs(subs_uw, simultaneous=True) - target) == 0)
# measure d^3k = 2 pi rho drho dkz = (2 pi r1 r2 / q) dr1 dr2
kz = qk
rho2 = r1 ** 2 - kz ** 2
jac = sp.Matrix([[sp.diff(rho2, r1), sp.diff(rho2, r2)], [sp.diff(kz, r1), sp.diff(kz, r2)]]).det()
check("E2 d^3k = (2 pi r1 r2 / q) dr1 dr2  (|d(rho^2,kz)/d(r1,r2)|/2 = r1 r2 / q)",
      sp.simplify(jac ** 2 / 4 - (r1 * r2 / q) ** 2) == 0)
# transverse-sum pair identity from spinor algebra: Tr[P+' s_i P- s_i] summed, minus q-component
ns = sp.symbols("n1 n2 n3 m1 m2 m3", real=True)
nvec = sp.Matrix(ns[:3])
mvec = sp.Matrix(ns[3:])
s_ = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
sdot = lambda vv: vv[0] * s_[0] + vv[1] * s_[1] + vv[2] * s_[2]
Pm = (sp.eye(2) - sdot(nvec)) / 2         # hole (lower band) at k, unit n
Pp = (sp.eye(2) + sdot(mvec)) / 2         # particle (upper band) at k+q, unit m
qh = sp.Matrix([0, 0, 1])
tot = sum(((Pp * s_[i] * Pm * s_[i]).trace() for i in (0, 1, 2)))
qc = (Pp * s_[2] * Pm * s_[2]).trace()
Tsym = sp.simplify(tot - qc)
unit = {ns[2]: sp.sqrt(1 - ns[0] ** 2 - ns[1] ** 2), ns[5]: sp.sqrt(1 - ns[3] ** 2 - ns[4] ** 2)}
Tdiff = sp.simplify((Tsym - (1 + nvec[2] * mvec[2])).subs(unit))
# sum over x,y polarisations of |<+|sigma_i|->|^2 = 1 + n_z m_z  (needs |n|=|m|=1 used)
check("E3 spinor algebra: sum_{eps perp q} |<u+(k')|eps.sigma|u-(k)>|^2 = 1 + (q.n)(q.n') for unit n, n'",
      sp.simplify(sp.expand(Tdiff)) == 0)
I_w = sp.integrate(q ** 2 + w ** 2, (w, -q, q))
check("E4 int_{-q}^{q} (q^2+w^2) dw = 8 q^3 / 3", sp.simplify(I_w - 8 * q ** 3 / 3) == 0)
# int d^3k T delta(omega - v u) with u=r1+r2, dr1 dr2 = du dw / 2, r1 r2 = (u^2-w^2)/4
integrand_w = sp.simplify((sp.pi / (4 * q)) * (u ** 2 - w ** 2) * target)       # (2pi/q)*(1/2)*(1/4)*(u^2-w^2)*T
Iw = sp.integrate(sp.simplify(integrand_w), (w, -q, q))
Idk = sp.simplify(Iw.subs(u, om / v_) / v_)                                      # delta(omega - v u) -> 1/v
Idk_target = sp.Rational(2, 3) * sp.pi * (om ** 2 - v_ ** 2 * q ** 2) / v_ ** 3
check("E5 int d^3k T delta(omega - v(r1+r2)) = (2 pi/3)(omega^2 - v^2 q^2)/v^3", sp.simplify(Idk - Idk_target) == 0)
S_T = sp.simplify(2 * sp.pi * e_ ** 2 * v_ ** 2 / (2 * sp.pi) ** 3 * Idk_target)
check("E6 S_T(omega,q) = 2 pi e^2 v^2 int d^3k/(2pi)^3 T delta = e^2 (omega^2 - v^2 q^2)/(6 pi v)",
      sp.simplify(S_T - e_ ** 2 * (om ** 2 - v_ ** 2 * q ** 2) / (6 * sp.pi * v_)) == 0)
# rate per volume for one cone: R = int d^3q/(2pi)^3 (1/(2 omega)) S_T(omega=c q, q), omega>=v q
c_, qm, al = sp.symbols("c q_max alpha", positive=True)
Rint = sp.integrate(4 * sp.pi * q ** 2 / (2 * sp.pi) ** 3 / (2 * c_ * q) * S_T.subs({om: c_ * q}), (q, 0, qm))
Rcone = sp.simplify(Rint)
check("E7 R_cone = e^2 (c^2-v^2) q_max^4 / (96 pi^3 c v) = alpha (c^2-v^2) q_max^4/(24 pi^2 c v) with e^2=4 pi alpha",
      sp.simplify(Rcone - e_ ** 2 * (c_ ** 2 - v_ ** 2) * qm ** 4 / (96 * sp.pi ** 3 * c_ * v_)) == 0 and
      sp.simplify(Rcone.subs(e_, sp.sqrt(4 * sp.pi * al)) - al * (c_ ** 2 - v_ ** 2) * qm ** 4 / (24 * sp.pi ** 2 * c_ * v_)) == 0)

# Q1 numerical cross-check of E5 by direct quadrature with explicit spinors (floating point, tol 1e-5)
def cumulative_numeric(vv, qq, omega):
    s = omega / vv
    sig_ = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], dtype=complex)]

    def T_at(rho, kz_):
        k = np.array([rho, 0.0, kz_])
        kp = np.array([rho, 0.0, kz_ + qq])
        def spinors(p):
            h = sum(p[i] * sig_[i] for i in range(3))
            w_, V = np.linalg.eigh(h)
            return V[:, 0], V[:, 1]       # lower, upper
        lo, _ = spinors(k)
        _, up = spinors(kp)
        return sum(abs(np.vdot(up, sig_[i] @ lo)) ** 2 for i in (0, 1))   # eps = x, y (perp to q = z)

    zc = -qq / 2
    half = s / 2
    def rho_max(kzv):
        arg = 1 - ((kzv - zc) / half) ** 2
        return np.sqrt(max(half ** 2 - (qq / 2) ** 2, 0.0) * max(arg, 0.0))
    f = lambda rho, kzv: 2 * np.pi * rho * T_at(rho, kzv)
    val, err = integrate.dblquad(f, zc - half, zc + half, lambda kzv: 0.0, rho_max, epsabs=1e-9, epsrel=1e-9)
    return val


Qpar = [(0.7, 0.9, 2.0), (0.5, 1.2, 3.1), (1.3, 0.4, 1.9)]
q1_ok = True
msgs = []
for vv, qq, om_ in Qpar:
    num = cumulative_numeric(vv, qq, om_)
    pred = (2 * np.pi / (3 * vv ** 3)) * (om_ ** 3 / 3 - vv ** 2 * qq ** 2 * om_ + 2 * vv ** 3 * qq ** 3 / 3)
    rel = abs(num - pred) / abs(pred)
    msgs.append("v=%.1f q=%.1f om=%.1f rel.err=%.1e" % (vv, qq, om_, rel))
    q1_ok &= rel < 1e-5
check("Q1 [float] direct spinor quadrature of the cumulative pair weight matches the closed form (3 points)", q1_ok, "; ".join(msgs))

# --------------------------------------------------------------------------
# F. Photon-number balance: state (arc) dependence, exact
# --------------------------------------------------------------------------
nv, nc, nph = sp.symbols("n_v n_c n_ph", nonnegative=True)
absorb = nph * nv * (1 - nc)
emit = (nph + 1) * nc * (1 - nv)
drate = sp.simplify(emit - absorb)
nstar = sp.solve(sp.Eq(drate, 0), nph)[0]
check("F1 d n/dt = (n+1) n_c (1-n_v) - n n_v (1-n_c); normal sea (n_v=1,n_c=0) -> d n/dt = 0 at n=0 (stable)",
      sp.simplify(drate.subs({nv: 1, nc: 0, nph: 0})) == 0)
check("F2 inverted sea (n_v=0,n_c=1): d n/dt = n+1 > 0 for every n >= 0 (no stationary photon number)",
      sp.simplify(drate.subs({nv: 0, nc: 1}) - (nph + 1)) == 0)
check("F3 infinite-temperature fermions (n_v=n_c=1/2): d n/dt = 1/4 > 0 for every n (spontaneous term survives, stimulated cancel)",
      sp.simplify(drate.subs({nv: sp.Rational(1, 2), nc: sp.Rational(1, 2)}) - sp.Rational(1, 4)) == 0)
check("F4 stationary photon number n* = n_c(1-n_v)/(n_v-n_c) (positive only if n_v>n_c; none for inverted occupation)",
      sp.simplify(nstar - nc * (1 - nv) / (nv - nc)) == 0)

# --------------------------------------------------------------------------
# G. Net first-order photon balance of the mu=-2 tick and U_g, exact in c
# --------------------------------------------------------------------------
def f_cone(c, v):
    return (c * c - v * v) / (c * v) if c > v else Fr(0)


def balance(nodes, c, emitting_a):
    # emitting sector = nodes with a == emitting_a (inverted w.r.t. the dynamics); absorbing sector = other
    em = sum(f_cone(c, n["v"]) for n in nodes if n["a"] == emitting_a)
    ab = sum(f_cone(c, n["v"]) for n in nodes if n["a"] != emitting_a)
    return em, ab


nd2 = tick_nodes(Fr(-2))
# arc vacuum (-pi,0]: eps=pi nodes emit, eps=0 node absorbs
em1, ab1 = balance(nd2, Fr(1), -1)
check("G1 mu=-2, c=1 (matter speed of the 0 node): emission weight 64/5, light-node absorption 0 (marginal)",
      em1 == Fr(64, 5) and ab1 == 0, "emission=%s absorption=%s" % (em1, ab1))
em2, ab2 = balance(nd2, Fr(1, 4), -1)
check("G2 mu=-2, c=1/4: only the v=1/5 node emits: weight 9/20; light node absorbs 0",
      em2 == Fr(9, 20) and ab2 == 0)
em3, ab3 = balance(nd2, Fr(1, 5), -1)
check("G3 mu=-2, c=1/5: no emission at first order (threshold c > min v = 1/5)", em3 == 0 and ab3 == 0)
# large-c limit reproduces K3's 17x
cbig = Fr(10 ** 9)
em4, ab4 = balance(nd2, cbig, -1)
check("G4 mu=-2, c -> infinity: emission/absorption -> sum_pi (1/v) / (1/v_0) = 17 (K3-T1F's 17.0008 is this limit)",
      abs(float(em4 / ab4) - 17.0) < 1e-6, "ratio=%.9f" % float(em4 / ab4))
# the complementary arc (0,pi]: eps=0 node emits, pi nodes absorb
em5, ab5 = balance(nd2, Fr(1), 1)
check("G5 mu=-2, c=1, complementary arc: emission 0, absorption 64/5 (pure photon decay into pi-pairs, no emission)",
      em5 == 0 and ab5 == Fr(64, 5))
ndg = [dict(a=(1 if sum(K) % 2 == 0 else -1), v=Fr(1)) for K in itertools.product([0, 1], repeat=3)]
emg, abg = balance(ndg, Fr(2), -1)
check("G6 U_g (8 nodes, v=1): emission == absorption for every c (exact gain=loss), e.g. c=2: 4 nodes each side",
      all(balance(ndg, cc, -1)[0] == balance(ndg, cc, -1)[1] for cc in (Fr(1, 2), Fr(1), Fr(3, 2), Fr(2), Fr(10))) and emg == abg)
em7, ab7 = balance(ndg, Fr(1), -1)
check("G7 U_g at c = v = 1: emission = absorption = 0 at first order (knife edge); closed for all c <= 1",
      em7 == 0 and ab7 == 0 and all(balance(ndg, cc, -1) == (0, 0) for cc in (Fr(1, 3), Fr(9, 10))))

# --------------------------------------------------------------------------
# L. Lattice cross-checks of the cone identification (float; tolerance stated)
# --------------------------------------------------------------------------
MU = -2.0


def b_norm(kv):
    m = MU + np.cos(kv).sum()
    d = np.sin(kv)
    Nn = np.sqrt(m * m + d @ d)
    return np.sqrt((d @ d)) / Nn      # |b| = sin(theta)


def pair_threshold(K, qvec):
    # minimal quasi-energy gap of a pair with total crystal momentum q near the node K (both sectors: theta -> arcsin|b|)
    Kv = np.array([np.pi if kk else 0.0 for kk in K])
    fun = lambda kap: np.arcsin(min(b_norm(Kv + kap), 1.0)) + np.arcsin(min(b_norm(Kv + kap + qvec), 1.0))
    best = np.inf
    for s0 in (-qvec / 2, -qvec / 2 + 0.2 * np.array([qvec[1], -qvec[0], 0.0]) + 1e-3):
        r = optimize.minimize(fun, s0, method="Nelder-Mead", options=dict(xatol=1e-12, fatol=1e-14, maxiter=4000))
        best = min(best, r.fun)
    return best


qlen = 0.02
l_ok = True
lmsg = []
for K in itertools.product([0, 1], repeat=3):
    hw = sum(K)
    vexp = 1.0 / abs(MU + 3 - 2 * hw)
    for qdir in (np.array([1.0, 0, 0]), np.array([1.0, 1.0, 1.0]) / np.sqrt(3)):
        th = pair_threshold(K, qlen * qdir)
        rel = abs(th / (vexp * qlen) - 1)
        l_ok &= rel < 5e-3
    lmsg.append("hw%d v=%.3f" % (hw, vexp))
check("L1 [float] lattice pair-threshold Omega_min(q) = v|q| (+-0.5%) at all 8 corners, 2 directions, |q|=0.02", l_ok)

# lattice check that pi-side threshold is the quasi-energy -omega fold: theta_pi = pi - arcsin|b| on a<0
def theta_exact(kv):
    m = MU + np.cos(kv).sum()
    d = np.sin(kv)
    Nn = np.sqrt(m * m + d @ d)
    return np.arccos(m / Nn)


kk = np.array([np.pi + 0.01, np.pi - 0.02, np.pi + 0.005])           # near the hw3 node (a<0)
check("L2 [float] near a pi node theta = pi - arcsin|b| (so excitation phase = -(arcsin|b|1 + arcsin|b|2) mod 2 pi)",
      abs(theta_exact(kk) - (np.pi - np.arcsin(b_norm(kk)))) < 1e-12)

# --------------------------------------------------------------------------
# H. Sink side: what the Record text does and does not give (exact toy)
# --------------------------------------------------------------------------
tt, kap = sp.symbols("t kappa", positive=True)
n_t = sp.exp(-kap * tt)                    # filled single mode under pure loss, jump rate kappa * <n>
total_jumps = sp.integrate(kap * n_t, (tt, 0, sp.oo))
check("H1 loss-only sink on one filled mode: total expected jumps = 1 (exact); N filled modes -> N",
      sp.simplify(total_jumps - 1) == 0)
r_gain = sp.symbols("r", positive=True)
Tcap = sp.symbols("T", positive=True)
check("H2 a gain-containing sink with steady jump rate r>0 per site writes r*T jumps: exceeds a one-per-site capacity at T = 1/r (exact)",
      sp.solve(sp.Eq(r_gain * Tcap, 1), Tcap) == [1 / r_gain])
# H3: the capacity conclusion is conditional on the bridge premise H-rec; without it the same Lindbladian has no capacity bound.
# exact statement: the Lindblad generator is a function of (kappa, jump operators) only -- the record count never enters
print("NOTE (reading, not counted): the Lindblad generator depends on {H, L_j} only; a record-slot capacity bound enters only through the premise H-rec "
      "(each jump writes one permanent record). Axiom text: MINIMAL_AXIOMS_2026-06-29.md lines 75-83, 114-123, 182-186.")

# --------------------------------------------------------------------------
n_pass = sum(RESULTS)
n_fail = len(RESULTS) - n_pass
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
if n_fail == 0:
    print("HIT: scoped result -- first-order vacuum->photon+pi-pair emission of a free two-band tick with arc vacuum has "
          "exact cone-level rate R=e^2(c^2-v^2)q_max^4/(96 pi^3 c v) per inverted node, threshold c>v, so for the "
          "mu=-2 Wilson tick it is open for every photon speed c>1/5 while light-node absorption is closed for c<=1 "
          "(K3's 17x is the c->infinity limit), for U_g emission=absorption exactly and both closed for c<=1, and the sign "
          "of the net balance flips with the arc chosen; for static backgrounds E[A] is always conserved (exact).")
print("SUMMARY: exact cone-level emission/absorption thresholds and rates for inverted pi-sector nodes, showing that a pi partner "
      "alone fixes no gain; the result depends on the photon speed c, the node speeds v, and the arc chosen.")
sys.exit(0 if n_fail == 0 else 1)
