#!/usr/bin/env python3
"""Exact checks of Lemma 14.10 and of the identity and sizes in Lemma 14.16.
Run: OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 nice -n 10 python3 ft_virial.py
All integrals by deterministic quadrature. No fit, no random numbers.
"""
import numpy as np
from scipy.optimize import brentq
from scipy.special import ive

# ---------------------------------------------------------------------------
# A. Lemma 14.10 on SU(2), one free link in the exponential chart.
# U = exp(i v.sigma), Haar = sin^2|v|/|v|^2 d^3v on |v| <= pi.
# S_eff(v) = -beta c Tr-part - log J; radial reduction, E[v.grad S_eff] must be 3.
print("A. SU(2) one link, exponential chart: E[v.grad S_eff] = 3 exactly (J vanishes at the cut locus)")
r, wr = np.polynomial.legendre.leggauss(4000)
r = 0.5 * np.pi * (r + 1.0)
wr = 0.5 * np.pi * wr
for y in [1.0, 5.0, 40.0]:
    # density in r: sin^2 r exp(2 y cos r) (colour-symmetric slice: weight y Tr h = 2 y cos r)
    dens = np.sin(r) ** 2 * np.exp(2 * y * (np.cos(r) - 1.0))
    # S_eff in 3D coordinates: -2 y cos r - 2 log(sin r / r); r d/dr of it:
    rdS = 2 * y * r * np.sin(r) - 2 * (r * np.cos(r) / np.sin(r) - 1.0)
    val = np.sum(wr * dens * rdS) / np.sum(wr * dens)
    print(f"   y={y:5.1f}  E[v.grad S_eff] = {val:.12f}")

# B. Lemma 14.10 with a periodic chart, U(1): boundary term is real and tiny.
print("B. U(1) one angle on (-pi,pi): E[phi dS/dphi] = 1 - boundary, boundary = 2 pi e^{-S(pi)}/Z")
phi, wp = np.polynomial.legendre.leggauss(4000)
phi = np.pi * phi
wp = np.pi * wp
for b in [1.0, 5.0, 20.0]:
    S = b * (1 - np.cos(phi))
    Z = np.sum(wp * np.exp(-S))
    val = np.sum(wp * np.exp(-S) * phi * b * np.sin(phi)) / Z
    bd = 2 * np.pi * np.exp(-2 * b) / Z
    print(f"   b={b:5.1f}  E={val:.12f}  1-boundary={1 - bd:.12f}")


# ---------------------------------------------------------------------------
# C. Exact coefficient: SU(2) chain of n links with product W, class angle theta.
# rho_n(theta) = sum_l (2l+1) lam_l^n chi_l(theta), lam_l = I_{2l+1}(beta)/I_1(beta) (ratio to l=0)
# T_n(theta) = -d/dbeta log rho_n. Classical a_n(theta) = n (1 - cos(theta/n)).
# Claim of Text 14: T_n(theta) - T_n(0) = a_n(theta) (1 + O(g^4)), no O(g^2).
def T_n(n, theta, beta, lmax=None, h=None):
    """-d/dbeta log rho_n by a high-order central difference on an exact character sum."""
    h = h or 1e-3 * beta
    lmax = lmax or int(60 + 12 * np.sqrt(beta * n))

    def logrho(b):
        idx = np.arange(0, 2 * lmax + 1)  # idx = 2l
        # exponentially scaled Bessel, log e^{-b} I_{2l+1}(b) = log ive
        lam = ive(idx + 1, b)
        chi = np.array([np.sin((i + 1) * theta) / np.sin(theta) if theta != 0 else i + 1.0 for i in idx])
        val = np.sum((idx + 1) * lam ** n * chi)
        # weight: c_l = e^{-b} I_{2l+1}(b) * 2/b up to the class normalisation; (2/b)^n is W independent
        return np.log(val) + n * np.log(2.0 / b)

    return -(
        -logrho(beta + 2 * h) + 8 * logrho(beta + h) - 8 * logrho(beta - h) + logrho(beta - 2 * h)
    ) / (12 * h)


print("C. SU(2) chain: R = (T_n(theta)-T_n(0))/a_n(theta); claim R - 1 = O(1/beta^2), no 1/beta term")
print("   n  theta   beta     R-1           beta^2 (R-1)   beta (R-1)")
for n in [2, 4, 8]:
    th = 0.4
    for beta in [20.0, 40.0, 80.0, 160.0]:
        a = n * (1 - np.cos(th / n))
        R = (T_n(n, th, beta) - T_n(n, 0.0, beta)) / a
        print(f"   {n}  {th:.2f}  {beta:6.1f}  {R-1:+.4e}  {beta**2*(R-1):+.4f}       {beta*(R-1):+.4f}")
# Two-link analytic value from I_2/I_1: T_2 = 2 - 2c + 3/(2 beta) - 3/(16 beta^2 c) + ..., so
# R-1 -> -(3/32)/beta^2 at small theta.
print("   two-link analytic small-theta prediction beta^2 (R-1) = -3/32 = -0.09375")
print("   compounding over levels: beta^2 (R-1) at beta=320, theta=0.4, n=2,4,...,64 (no running in 1D, so x_j is constant)")
print("   ", ", ".join(f"n={n}: {320.0**2*((T_n(n,0.4,320.0)-T_n(n,0.0,320.0))/(n*(1-np.cos(0.4/n)))-1):+.4f}" for n in [2,4,8,16,32,64]))


# ---------------------------------------------------------------------------
# D. Line-by-line test of the identity of Lemma 14.16 on an exact non-Gaussian model with no symmetry.
# Abelian chain: cells c=1,2,3 with a_c(theta_c) = k_c (1 - cos theta_c), constraint theta_1+theta_2+theta_3 = Th.
# Two coarse cells: c' = {1,2}, c'' = {3}. Fibre coordinates xi=(xi_1,xi_2), xi_1 assigned to c', xi_2 to c''.
# theta = theta_star + g E xi, E columns (1,-1,0), (0,1,-1): a linear chart, so J = 1, Q^reg = 0.
k = np.array([1.0, 1.7, 0.6])
E = np.array([[1.0, 0.0], [-1.0, 1.0], [0.0, -1.0]])
phi_c = np.array([1.0, 1.0, 0.0])  # phi'(c)
phi_b = np.array([1.0, 0.0])  # phi^'_b


def star(Th):
    def res(lam):
        return np.sum(np.arcsin(np.clip(lam / k, -1, 1))) - Th

    if Th == 0:
        return np.zeros(3)
    lam = brentq(res, -0.999 * k.min(), 0.999 * k.min())
    return np.arcsin(lam / k)


def run(x, Th, N=400, wid=12.0):
    g = x ** -0.5
    n, w = np.polynomial.legendre.leggauss(N)
    n = wid * n
    w = wid * w
    X1, X2 = np.meshgrid(n, n, indexing="ij")
    W2 = np.outer(w, w)
    xi = np.stack([X1, X2])  # 2,N,N

    def law(Th_):
        ts = star(Th_)
        th = ts[:, None, None] + g * np.einsum("ib,bnm->inm", E, xi)
        a = k[:, None, None] * (1 - np.cos(th))
        a0 = k * (1 - np.cos(ts))
        grad_star = k * np.sin(ts)  # d a_c/d theta_c at star
        S = x * (a.sum(0) - a0.sum())
        dens = np.exp(-S) * W2
        dens /= dens.sum()
        # d_b of S in xi: x g sum_c k_c sin(theta_c) E_cb
        dS = np.einsum("cb,cnm->bnm", E, x * g * k[:, None, None] * np.sin(th))
        # homogeneous pieces of x a_c o chart: P1, P2, P>=3, per cell
        eta = g * np.einsum("ib,bnm->inm", E, xi)  # theta - theta*
        P1 = x * grad_star[:, None, None] * eta
        Qcc = k * np.cos(ts)
        P2 = 0.5 * x * Qcc[:, None, None] * eta ** 2
        Pge3 = x * a - x * a0[:, None, None] - P1 - P2
        return dict(ts=ts, a=a, a0=a0, dens=dens, dS=dS, eta=eta, P1=P1, P2=P2, Pge3=Pge3, Qcc=Qcc, grad=grad_star)

    LW, L1 = law(Th), law(0.0)

    def exp(L, F):
        return float(np.sum(L["dens"] * F))

    # Lemma 14.10 weighted on each coordinate
    v1 = exp(LW, xi[0] * LW["dS"][0])
    v2 = exp(LW, xi[1] * LW["dS"][1])

    def G(L):
        # (grad_c,b xi_b) and (1/2) xi_b (Q_c xi)_b per cell and coordinate
        cur = 0.0
        for c in range(3):
            for b in range(2):
                gr = x * g * L["grad"][c] * E[c, b]  # coefficient of xi_b in P1_c
                Qxi = x * g * g * L["Qcc"][c] * E[c, b] * np.einsum("b,bnm->nm", E[c], xi)  # (Q_c xi)_b
                cur = cur + (phi_c[c] - phi_b[b]) * (gr * xi[b] + 0.5 * xi[b] * Qxi)
        # G^hi: sum_c phi'(c) P>=3_c - (1/2) sum_b phi^'_b xi_b d_b sum_c P>=3_c
        Psum = L["Pge3"].sum(0)
        # d_b P>=3 = d_b S - d_b(P1+P2) ; sum_c P1 has zero gradient at the critical point
        P12grad = []
        for b in range(2):
            t = 0.0
            for c in range(3):
                t = t + x * g * L["grad"][c] * E[c, b] + x * g * g * L["Qcc"][c] * E[c, b] * np.einsum("b,bnm->nm", E[c], xi)
            P12grad.append(t)
        hi = (phi_c[:, None, None] * L["Pge3"]).sum(0)
        for b in range(2):
            hi = hi - 0.5 * phi_b[b] * xi[b] * (L["dS"][b] - P12grad[b])
        return cur, hi

    GW = G(LW)
    G1 = G(L1)
    lhs = exp(LW, (phi_c[:, None, None] * x * LW["a"]).sum(0)) - exp(L1, (phi_c[:, None, None] * x * L1["a"]).sum(0))
    classical = x * float((phi_c * LW["a0"]).sum())
    cur = exp(LW, GW[0]) - exp(L1, G1[0])
    hi = exp(LW, GW[1]) - exp(L1, G1[1])
    crit = float(np.abs(np.einsum("c,cb->b", LW["grad"], E)).max())
    return lhs, classical, cur, hi, v1, v2, crit


print("D. Identity of Lemma 14.16 on the asymmetric exact chain (k = 1, 1.7, 0.6), Th = 0.5")
print("   x      LHS          classical    current      hi           defect     v1-1      v2-1     cur/(g^2 cl)  hi/(g^4 cl)")
for x in [20.0, 40.0, 80.0, 160.0, 320.0]:
    lhs, cl, cur, hi, v1, v2, crit = run(x, 0.5)
    g2 = 1 / x
    print(f"   {x:5.0f}  {lhs:+.6e}  {cl:+.6e}  {cur:+.4e}  {hi:+.4e}  {lhs-cl-cur-hi:+.1e}  {v1-1:+.1e}  {v2-1:+.1e}  {cur/(g2*cl):+.4f}      {hi/(g2*g2*cl):+.4f}")
print("   criticality of V*: |sum_c grad_c| =", run(40.0, 0.5)[6])
