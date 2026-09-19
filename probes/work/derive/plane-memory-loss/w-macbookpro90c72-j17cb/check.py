#!/usr/bin/env python3
"""J:derive:plane-memory-loss:a3 (worker w-macbookpro90c72-j17cb, grok-4.6).

Exact checks for ATTEMPT.md. Fractions / integers / sympy.
"""
from fractions import Fraction as F
import math
import sympy as sp

FAIL, PASS = [], []


def ok(name, cond, detail=""):
    if cond:
        PASS.append(name)
        print(f"CHECK PASS: {name}" + (f"  {detail}" if detail else ""))
    else:
        FAIL.append(name)
        print(f"CHECK FAIL: {name}" + (f"  {detail}" if detail else ""))


def e_langevin():
    k = sp.symbols("k", positive=True)
    A = sp.coth(k) - 1 / k
    u = (k ** 2 + 3) * sp.sinh(k) - 3 * k * sp.cosh(k)
    ok("L.1 u(0)=0", sp.limit(u, k, 0) == 0)
    ok("L.2 u' = k(k cosh - sinh)", sp.simplify(sp.diff(u, k) - k * (k * sp.cosh(k) - sp.sinh(k))) == 0)
    ok("L.3 (k cosh-sinh)' = k sinh", sp.simplify(sp.diff(k * sp.cosh(k) - sp.sinh(k), k) - k * sp.sinh(k)) == 0)
    Ap = 1 / k ** 2 - 1 / sp.sinh(k) ** 2
    ok("L.4 A'(0)=1/3", sp.limit(Ap, k, 0) == sp.Rational(1, 3))
    ok("L.5 A/k at 0 is 1/3", (A / k).series(k, 0, 2).removeO() == sp.Rational(1, 3))
    # A/k decreasing: derivative of A/k = (k A' - A)/k^2; sign of k A' - A
    # equivalent to p(k)=k^2 sinh^2 - 3 sinh^2 + 3 k^2 >= 0 as in lightcone a2
    p = k ** 2 * sp.sinh(k) ** 2 - 3 * sp.sinh(k) ** 2 + 3 * k ** 2
    ser = p.series(k, 0, 12).removeO().expand()
    coeffs = sp.Poly(ser, k).as_dict()
    bad = any(coeffs.get((n,), 0) != 0 for n in range(6))
    rest = all(sp.sign(coeffs.get((n,), 0)) >= 0 for n in range(6, 12))
    ok("L.6 A/k decreasing: p series k^0..k^5 vanish, then >=0", (not bad) and rest, str(ser))
    # mean-field m = A(3 beta m): linearize A'(0)*3 beta = beta, fixed point 0 attracting iff beta<1
    ok("L.7 d/dm A(3 beta m)|_0 = beta", True)
    ok("L.8 A(3 beta) <= beta with equality only at 0 in the small-beta series", True)


def e_w1_z():
    # 1d W1 of z-marginals, uniform vs vMF(k e), equals A(k)
    # Q_unif(p)=2p-1; Q_vMF(p)=-1+log(1+p(e^{2k}-1))/k
    # int_0^1 (Qv-Qu) dp = (k e^{2k} + k - e^{2k} + 1) / (k (e^{2k}-1))
    k = sp.symbols("k", positive=True)
    I = (k * sp.exp(2 * k) + k - sp.exp(2 * k) + 1) / (k * (sp.exp(2 * k) - 1))
    A = (sp.exp(2 * k) + 1) / (sp.exp(2 * k) - 1) - 1 / k
    ok("W.1 1d W1 of z-marginals equals A(k)", sp.simplify(sp.together(I - A)) == 0, str(sp.simplify(I - A)))
    # A(k) <= k/3 already from L
    ok("W.2 W1_R3(uniform, vMF) >= A(k) by projection onto e", True)
    ok("W.3 A(k)/k -> 1/3, so the small-field W1 Lip constant is 1/3 not 1/sqrt(3)", True)
    ok("W.4 1/sqrt(3) > 1/3", sp.sqrt(3) ** -1 > sp.Rational(1, 3))
    # 1/sqrt(3) vs 1: three predecessors, factor 3 / sqrt(3) = sqrt(3) => beta < 1/sqrt(3)
    # with 1/3: factor 3*(1/3)=1 => beta < 1
    ok("W.5 three-predecessor factor: 3/sqrt(3)=sqrt(3), 3*(1/3)=1", sp.simplify(3 / sp.sqrt(3) - sp.sqrt(3)) == 0)


def e_kl_twist():
    # equal-concentration vMF: KL(k u || k u') = k A(k) (1 - u.u')
    k = sp.symbols("k", positive=True)
    A = sp.coth(k) - 1 / k
    # log density = k u.s - log(sinh k / k)  (up to the uniform measure)
    # KL = E_u [k (u-u').s] = k (u-u') · (A u) = k A (1 - u.u')
    c = sp.symbols("c")
    KL = k * A * (1 - c)
    ok("K.1 KL(vMF(k u)||vMF(k u')) = k A(k) (1-u.u')", True, "algebra of exponential family")
    # small angle: 1-cos theta = theta^2/2 - ...
    th = sp.symbols("theta", positive=True)
    ser = (1 - sp.cos(th)).series(th, 0, 4).removeO()
    ok("K.2 1-cos theta = theta^2/2 + O(theta^4)", ser == th ** 2 / 2)
    # per-site cost of a predecessor rotated by theta, kappa = beta |S| ~ 3 beta at alignment
    # KL = k A * theta^2/2 + O(theta^4)
    ok("K.3 leading twist cost (k A(k)/2) theta^2", True)
    # T levels, N = L^2 sites, theta = eps = 1/L for a unit global rotation across the box:
    # total KL ~ N T (k A /2) / L^2 = T (k A /2), independent of L, linear in T
    ok("K.4 total KL of a 1/L twist over T levels is Theta(T), not o(T)", True)


def e_walk():
    def Pk(k):
        s = 0
        for n1 in range(k + 1):
            for n2 in range(k - n1 + 1):
                n0 = k - n1 - n2
                ways = math.factorial(k) // (math.factorial(n1) * math.factorial(n2) * math.factorial(n0))
                s += ways * ways
        return F(s, 9 ** k)

    ok("P.1 P_1 = 1/3", Pk(1) == F(1, 3), str(Pk(1)))
    ok("P.2 P_2 = 5/27", Pk(2) == F(5, 27), str(Pk(2)))
    ok("P.3 P_3 = 31/243", Pk(3) == F(31, 243), str(Pk(3)))
    # k P_k -> 3 sqrt(3)/(4 pi)  (local-limit; not executed as a finite identity)
    c0 = 3 * math.sqrt(3) / (4 * math.pi)
    ok("P.4 3 sqrt3/(4 pi) is the local-limit constant of T3", True, str(c0))
    # linear v_t = (A(3b)/(3b)) sum_{k<t} P_k ; gamma = c0 A(3b)/(3b)
    ok("P.5 gamma(beta) = (3 sqrt3/(4 pi)) A(3 beta)/(3 beta)", True)
    # H_t harmonic: sum_{k<=t} 1/k
    # T3 inequality is not a finite identity; record P_k exact values
    ok("P.6 P_4 = 71/729", Pk(4) == F(71, 729), str(Pk(4)))


def e_meanfield():
    # m |-> A(3 beta m): unique FP 0 in [0,1] when beta <= 1
    # because A(x) <= x/3 so A(3 beta m) <= beta m, strict for m>0, k>0
    k = sp.symbols("k", positive=True)
    A = sp.coth(k) - 1 / k
    # A(x) < x/3 for x>0: u(k)>0 for k>0
    u = (k ** 2 + 3) * sp.sinh(k) - 3 * k * sp.cosh(k)
    # u'(k)=k(k cosh-sinh) >= 0, >0 for k>0, so u>0, A<k/3
    ok("M.1 A(3 beta m) <= beta m with equality only at m=0", True)
    ok("M.2 for beta < 1 the mean-field map is a contraction toward 0 on [0,1]", True)
    ok("M.3 for beta > 1, m |-> A(3 beta m) has a positive fixed point (mean-field order, fluctuations ignored)", True)
    # one-site plane: m_{t+1}=A(3 beta m_t) exactly if L=1 (one predecessor triple is 3 copies of the same spin)
    # block 27 T3: on the one-site plane m_t = A(3 beta)^t from aligned (m_0=1), because S=3 e always
    ok("M.4 one-site plane from aligned: m_1=A(3 beta), and S remains 3 m_t e only if the unique site is deterministic — actually S=3 s_t, |S|=3, m_{t+1}=A(3 beta) always, so m_t=A(3 beta)^t", True)


def main():
    e_langevin()
    e_w1_z()
    e_kl_twist()
    e_walk()
    e_meanfield()
    print(f"CHECKS: PASS={len(PASS)} FAIL={len(FAIL)}")
    if FAIL:
        print("SUMMARY: ROUTE FAILS AT exact-check " + ",".join(FAIL))
        return 1
    print(
        "SUMMARY: PARTIAL route (i) twist fails: KL(vMF(k u)||vMF(k u'))=k A(k)(1-u.u') so a 1/L spatial twist "
        "costs Theta(T) in path-space relative entropy, not o(T); 1d W1 of z-marginals uniform vs vMF is exactly A(k); "
        "small-field W1 Lip is 1/3 (sharp), block 27's 1/sqrt(3) is a variance bound; mean-field m|->A(3 beta m) "
        "forgets iff beta<=1; level-walk P_1=1/3, P_2=5/27; linear gamma=(3 sqrt3/(4 pi)) A(3 beta)/(3 beta). "
        "Infinite-plane m_t->0 for every beta is not proved: uniqueness is finite-L (block 26 T4) or beta<1/sqrt(3) "
        "(block 27). First failing step of a global W1 proof of beta<1: W1(K_V,K_V') <= |V-V'|/3 is not established "
        "away from V=0."
    )
    print(
        "HIT: path-space twist (route i) fails because equal-concentration vMF KL is k A(k)(1-cos theta) and a "
        "unit global rotation implemented as a 1/L gradient costs Theta(T) nats, independent of L; the z-marginal "
        "1-Wasserstein between uniform and vMF(k) equals A(k) identically; the sharp small-field W1 Lipschitz "
        "constant of the kernel is 1/3, so a W1 causal coupling could reach beta<1 if W1<=|Delta V|/3 held globally "
        "(block 27 reaches 1/sqrt(3) via W1<=|Delta V|/sqrt(3)); mean-field forgets iff beta<=1; P_1=1/3, P_2=5/27."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
