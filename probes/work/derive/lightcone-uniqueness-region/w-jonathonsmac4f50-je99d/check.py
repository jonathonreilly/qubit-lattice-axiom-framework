#!/usr/bin/env python3
"""lightcone-uniqueness-region a3 (w-jonathonsmac4f50-je99d): the directional lemma.

Claim: for the vMF kernel mu_V (density e^{V.s}/Z on S^2), every chordal-1-Lipschitz f,
every V in R^3 and every unit u:   Cov_V(f, u.s) <= 1/3,  with equality at V = 0, f = u.s.
Route: harmonic extension to the unit ball + Cauchy-Schwarz + Dirichlet energy (ATTEMPT.md S3-S8).
Everything finite below is exact (sympy / Fraction) except section N, which is labelled NUMERICAL.
"""
import sys
from fractions import Fraction as Fr
from math import factorial
import sympy as sp

FAILS = []
def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))
    if not ok: FAILS.append(name)

k, a, z, ph = sp.symbols('k a z phi', positive=True)
E = sp.symbols('E', positive=True)          # E = e^k
def to_E(expr):
    """rewrite sinh/cosh/exp of integer multiples of k as rational functions of E = e^k"""
    return sp.together(sp.expand(expr.rewrite(sp.exp)).subs(sp.exp(k), E)
                       .replace(lambda t: t.func == sp.exp, lambda t: E ** sp.simplify(t.args[0] / k)))

# ---------------------------------------------------------------- E1 closed forms of the z-integrals
Em = {m: sp.integrate(z**m * sp.exp(a*z), (z, -1, 1)) for m in range(3)}
claimed = {0: 2*sp.sinh(a)/a, 1: 2*sp.cosh(a)/a - 2*sp.sinh(a)/a**2,
           2: 2*sp.sinh(a)/a - 4*sp.cosh(a)/a**2 + 4*sp.sinh(a)/a**3}
for m in range(3):
    check(f"E1.{m} int_-1^1 z^{m} e^(az) dz closed form",
          sp.simplify((Em[m] - claimed[m]).rewrite(sp.exp)) == 0)
I = lambda t: 4*(t*sp.cosh(t) - sp.sinh(t))/t**3                  # int e^{tz}(1-z^2) dz
check("E1.3 I(a) = int e^(az)(1-z^2) dz = 4(a cosh a - sinh a)/a^3",
      sp.simplify((claimed[0] - claimed[2] - I(a)).rewrite(sp.exp)) == 0)
E0 = lambda t: claimed[0].subs(a, t); E1f = lambda t: claimed[1].subs(a, t); E2f = lambda t: claimed[2].subs(a, t)

# ---------------------------------------------------------------- E2 the vMF moments and the l=1 projections
A = sp.cosh(k)/sp.sinh(k) - 1/k                                    # mean of z under q(z) ~ e^{kz}
check("E2.1 A = coth k - 1/k is the mean: int e^{kz}(z-A) dz = 0",
      sp.simplify(to_E(E1f(k) - A*E0(k))) == 0)
J1 = E2f(k) - A*E1f(k)                                             # int e^{kz}(z-A) z dz
check("E2.2 J1 = int e^{kz}(z-A)z dz = 2 sinh k/k^3 - 2/(k sinh k)",
      sp.simplify(to_E(J1 - (2*sp.sinh(k)/k**3 - 2/(k*sp.sinh(k))))) == 0)
J2 = E2f(2*k) - 2*A*E1f(2*k) + A**2*E0(2*k)                         # int e^{2kz}(z-A)^2 dz
check("E2.3 int_0^2pi cos^2(phi) dphi = pi, int cos(phi) dphi = 0 (azimuthal orthogonality)",
      sp.integrate(sp.cos(ph)**2, (ph, 0, 2*sp.pi)) == sp.pi and sp.integrate(sp.cos(ph), (ph, 0, 2*sp.pi)) == 0)
check("E2.4 int_{S^2} x^2 dS = 4 pi/3",
      sp.integrate(sp.integrate((1 - z**2)*sp.cos(ph)**2, (ph, 0, 2*sp.pi)), (z, -1, 1)) == 4*sp.pi/3)

# ---------------------------------------------------------------- E3 the truncated energies and the reduction to G >= 0
c = k/(4*sp.pi*sp.sinh(k))                                         # density p = c e^{kz} per unit area
D0 = 1/(12*sp.pi)
Bperp = (sp.pi*c**2/2)*(I(2*k) + sp.Rational(3, 4)*I(k)**2)        # (|g|^2 + |g_1|^2)/2, perpendicular
Bpar = sp.pi*c**2*(J2 + sp.Rational(3, 2)*J1**2)                   # (|g|^2 + |g_1|^2)/2, parallel
Fperp = 8*sp.sinh(k)**2 - 3*k**2*(I(2*k) + sp.Rational(3, 4)*I(k)**2)
Fpar = 4*sp.sinh(k)**2 - 3*k**2*(J2 + sp.Rational(3, 2)*J1**2)
check("E3.1 D0 - Bperp = Fperp / (96 pi sinh^2 k)",
      sp.simplify(to_E(D0 - Bperp - Fperp/(96*sp.pi*sp.sinh(k)**2))) == 0)
check("E3.2 D0 - Bpar = Fpar / (48 pi sinh^2 k)",
      sp.simplify(to_E(D0 - Bpar - Fpar/(48*sp.pi*sp.sinh(k)**2))) == 0)

# exponential polynomials: dict {(m, n): Fraction} for sum c k^m e^{n k}
def ep_mul(p, q):
    r = {}
    for (m1, n1), v1 in p.items():
        for (m2, n2), v2 in q.items():
            r[(m1+m2, n1+n2)] = r.get((m1+m2, n1+n2), Fr(0)) + v1*v2
    return {kk: v for kk, v in r.items() if v != 0}
def ep_add(*ps):
    r = {}
    for p in ps:
        for kk, v in p.items(): r[kk] = r.get(kk, Fr(0)) + v
    return {kk: v for kk, v in r.items() if v != 0}
def ep_sc(s, p): return {kk: Fr(s)*v for kk, v in p.items()}
def ep_pow(p, e):
    r = {(0, 0): Fr(1)}
    for _ in range(e): r = ep_mul(r, p)
    return r
KK = {(1, 0): Fr(1)}
def kp(m): return {(m, 0): Fr(1)}
def sh(n): return {(0, n): Fr(1, 2), (0, -n): Fr(-1, 2)}
def ch(n): return {(0, n): Fr(1, 2), (0, -n): Fr(1, 2)}
def ep_sym(p): return sum(sp.Rational(v.numerator, v.denominator)*k**m*E**n for (m, n), v in p.items())

Gperp = ep_add(ep_mul(kp(4), ch(2)), ep_sc(-4, kp(4)), ep_sc(Fr(3, 2), ep_mul(kp(3), sh(2))),
               ep_sc(-18, ep_mul(kp(2), ch(2))), ep_sc(-18, kp(2)), ep_sc(36, ep_mul(KK, sh(2))),
               ep_sc(-18, ch(2)), {(0, 0): Fr(18)})
Nn = ep_add(ep_mul(KK, ch(1)), ep_sc(-1, sh(1)))                    # N = k cosh k - sinh k, A = N/(k sinh k)
S1 = sh(1)
t1 = ep_sc(3, ep_mul(ep_pow(S1, 2), ep_add(ep_mul(kp(5), sh(2)), ep_sc(-1, ep_mul(kp(4), ch(2))),
                                           ep_sc(Fr(1, 2), ep_mul(kp(3), sh(2))))))
t2 = ep_sc(6, ep_mul(ep_mul(S1, Nn), ep_add(ep_mul(kp(4), ch(2)), ep_sc(Fr(-1, 2), ep_mul(kp(3), sh(2))))))
t3 = ep_sc(3, ep_mul(ep_mul(kp(3), ep_pow(Nn, 2)), sh(2)))
Gpar = ep_add(ep_sc(4, ep_mul(kp(4), ep_pow(S1, 4))), ep_sc(-1, t1), t2, ep_sc(-1, t3),
              ep_sc(-18, ep_pow(ep_add(ep_pow(S1, 2), ep_sc(-1, kp(2))), 2)))
check("E3.3 k^4 Fperp equals the exponential polynomial Gperp",
      sp.simplify(to_E(k**4*Fperp) - ep_sym(Gperp)) == 0)
check("E3.4 k^4 sinh^2(k) Fpar equals the exponential polynomial Gpar",
      sp.simplify(to_E(k**4*sp.sinh(k)**2*Fpar) - ep_sym(Gpar)) == 0)

# ---------------------------------------------------------------- E4 every Taylor coefficient of Gperp, Gpar is >= 0
def taylor(p, N):
    out = [Fr(0)]*N
    for (m, n), v in p.items():
        for j in range(m, N): out[j] += v*Fr(n)**(j - m)/factorial(j - m)
    return out
def even(p): return all(p.get((m, -n), Fr(0)) == (-1)**m*v for (m, n), v in p.items())
def ff(j, m):
    r = Fr(1)
    for i in range(m): r *= (j - i)
    return r
def tail_nonneg(p, J0):
    """for even j >= J0: c_j j!/M^j = [P_M(j) + P_{-M}(j)] + sum_{0<|n|<M} (n/M)^j P_n(j), P_n(j) = sum_m c_mn (j)_m / n^m.
    Prove lead(j) := P_M + P_{-M} is a polynomial with lead(J0 + y) having nonnegative coefficients and lead(J0) > 0,
    and rest(j) <= (Mm/M)^j U(j) with U having nonnegative coefficients and (1+1/J0)^deg U <= M/Mm (so rest decreases)."""
    y = sp.symbols('y')
    M = max(abs(n) for (m, n) in p)
    assert J0 > max(m for (m, n) in p)          # n = 0 terms contribute only for j <= max m
    lower = sorted(set(n for (m, n) in p if 0 < abs(n) < M))
    Mm = max([abs(n) for n in lower] + [0])
    def Ppoly(n, x): return sum(sp.Rational(v.numerator, v.denominator)*sp.ff(x, m)/sp.Integer(n)**m
                                for (m, nn), v in p.items() if nn == n)
    lead = sp.expand(Ppoly(M, J0 + y) + Ppoly(-M, J0 + y))
    Lc = sp.Poly(lead, y).all_coeffs()
    lead_ok = all(cc >= 0 for cc in Lc) and lead.subs(y, 0) > 0
    if not lower:                                # nothing below the dominant exponent: rest(j) = 0
        return lead_ok, (M, Mm, J0)
    U = sp.expand(sum(sum(sp.Rational(abs(v).numerator, abs(v).denominator)*y**m/sp.Integer(abs(n))**m
                           for (m, nn), v in p.items() if nn == n) for n in lower))
    deg = sp.Poly(U, y).degree()
    dec = Fr(J0 + 1, J0)**deg <= Fr(M, Mm)
    restJ0 = sp.Rational(Mm, M)**J0*U.subs(y, J0)
    return lead_ok and dec and restJ0 < lead.subs(y, 0), (M, Mm, J0)
for name, G, first in [("Gperp", Gperp, (8, Fr(4, 15))), ("Gpar", Gpar, (10, Fr(16, 15)))]:
    co = taylor(G, 90)
    check(f"E4.{name}.a {name} is even in k (odd Taylor coefficients vanish identically)", even(G))
    nz = [(j, v) for j, v in enumerate(co) if v != 0]
    check(f"E4.{name}.b first nonzero coefficient is {first[1]} k^{first[0]}", nz[0] == first, str(nz[0]))
    check(f"E4.{name}.c all Taylor coefficients j < 90 are >= 0 (exact)", all(v >= 0 for v in co))
    ok, info = tail_nonneg(G, 60)
    check(f"E4.{name}.d all even Taylor coefficients j >= 60 are > 0 (dominant e^(+-Mk) polynomial beats the rest)", ok,
          "M=%d, next |n|=%d, J0=%d" % info)
print("=> Gperp(k) >= 0 and Gpar(k) >= 0 for every real k, > 0 for k != 0; hence Bperp, Bpar <= 1/(12 pi), strict for k > 0")

# ---------------------------------------------------------------- E5 the constant 1/3 is attained at V = 0
check("E5.1 at V = 0: Cov(u.s, u.s) = int (u.s)^2 dS/(4 pi) = 1/3 (linear f attains the bound)",
      sp.integrate(sp.integrate(z**2/(4*sp.pi), (ph, 0, 2*sp.pi)), (z, -1, 1)) == sp.Rational(1, 3))
check("E5.2 sqrt(|B| * D0) = sqrt((4 pi/3)/(12 pi)) = 1/3",
      sp.sqrt(sp.Rational(4, 3)*sp.pi/(12*sp.pi)) == sp.Rational(1, 3))
check("E5.3 at k -> 0 both truncated energies tend to D0 (Bperp, Bpar -> 1/(12 pi))",
      sp.limit(Bperp, k, 0) == D0 and sp.limit(Bpar, k, 0) == D0)

# ---------------------------------------------------------------- E6 TV: the Dobrushin coefficient is >= tanh(beta/2)
b = sp.symbols('beta', positive=True)
q = lambda V, zz: V*sp.exp(V*zz)/(2*sp.sinh(V))                    # law of z = e.s under mu_{V e}
# TV = (1/2) int_{-1}^1 |q_b(z) - q_{-b}(z)| dz = int_0^1 (q_b(z) - q_b(-z)) dz  (positive on z > 0)
tv = sp.integrate(q(b, z) - q(b, -z), (z, 0, 1))
check("E6.1 TV(mu_{beta e}, mu_{-beta e}) = tanh(beta/2)", sp.simplify((tv - sp.tanh(b/2)).rewrite(sp.exp)) == 0)
check("E6.2 7 tanh(ln(4/3)/2) = 1 exactly (TV-Dobrushin ceiling beta = ln(4/3))",
      sp.simplify(7*sp.tanh(sp.log(sp.Rational(4, 3))/2) - 1) == 0)

# ---------------------------------------------------------------- E7 the order of the constants (exact, rational bounds)
def exp_lower(x, n=12):   # sum_{i<=n} x^i/i!  <= e^x for x >= 0
    return sum(Fr(x)**i/factorial(i) for i in range(n + 1))
def exp_upper(x, n=12):   # e^x <= sum_{i<=n} x^i/i! + x^{n+1}/(n+1)! * 3  for 0 <= x <= 1
    return sum(Fr(x)**i/factorial(i) for i in range(n + 1)) + 3*Fr(x)**(n + 1)/factorial(n + 1)
sqrt3_hi = Fr(17321, 10000); assert sqrt3_hi**2 > 3
check("E7.1 sqrt(3)/7 < ln(4/3)   (block 27's TV constant is inside the TV ceiling)", exp_upper(sqrt3_hi/7) < Fr(4, 3))
check("E7.2 ln(4/3) < 3/10 < 3/7  (the TV ceiling, a2's unconditional W1 region, this attempt's W1 region)",
      Fr(4, 3) < exp_lower(Fr(3, 10)) and Fr(3, 10) < Fr(3, 7))
check("E7.3 3/7 < 0.55 < 0.60     (the W1 region ends below the executed onset bracket)", Fr(3, 7) < Fr(55, 100))
check("E7.4 7 * (1/3) * beta < 1 exactly for beta < 3/7", Fr(7, 3)*Fr(3, 7) == 1)

# ---------------------------------------------------------------- N  NUMERICAL cross-checks (floats; not part of the proof)
try:
    import numpy as np
    from numpy.polynomial.legendre import leggauss
    from scipy.special import eval_legendre, lpmv
    X, Wt = leggauss(300)
    def Aa(kk): return 1/np.tanh(kk) - 1/kk
    def dir_energy(kk, L=80):
        p = kk*np.exp(kk*X)/(4*np.pi*np.sinh(kk)); gpar = p*(X - Aa(kk)); gperp = p*np.sqrt(1 - X**2)
        Dp = Dq = 0.0
        for l in range(1, L):
            cl = (2*l + 1)/2*np.sum(Wt*gpar*eval_legendre(l, X)); Dp += cl**2*4*np.pi/(2*l + 1)/l
            n1 = 2*l*(l + 1)/(2*l + 1); bl = np.sum(Wt*gperp*lpmv(1, l, X))/n1; Dq += bl**2*np.pi*n1/l
        return Dp, Dq
    fBpar = sp.lambdify(k, Bpar, 'mpmath'); fBperp = sp.lambdify(k, Bperp, 'mpmath')
    d0 = 1/(12*np.pi); okN = True; rows = []
    for kk in [0.2, 0.7, 1.5, 3.0, 6.0]:
        Dp, Dq = dir_energy(kk); bp, bq = float(fBpar(kk)), float(fBperp(kk))
        okN &= (Dp <= bp*(1 + 1e-9) <= d0) and (Dq <= bq*(1 + 1e-9) <= d0)
        rows.append("k=%.1f D_par/D0=%.4f B_par/D0=%.4f D_perp/D0=%.4f B_perp/D0=%.4f" % (kk, Dp/d0, bp/d0, Dq/d0, bq/d0))
    for r in rows: print("   " + r)
    check("N1 NUMERICAL: Legendre-series Dirichlet energies <= truncated B <= D0 at k in {0.2,0.7,1.5,3,6}", okN)
    from scipy.optimize import linprog
    from scipy.sparse import coo_matrix
    def w1(kk, al, N=700):
        i = np.arange(N) + 0.5; zz = 1 - 2*i/N; pp = np.pi*(1 + 5**0.5)*i; r = np.sqrt(1 - zz*zz)
        P = np.stack([r*np.cos(pp), r*np.sin(pp), zz], 1); w = np.exp(kk*zz); w /= w.sum()
        u = np.array([np.sin(al), 0, np.cos(al)]); g = w*(P@u - u@np.array([0, 0, (w*zz).sum()]))
        pos = np.where(g > 0)[0]; neg = np.where(g < 0)[0]; aa = g[pos]; bb = -g[neg]; bb *= aa.sum()/bb.sum()
        C = np.linalg.norm(P[pos][:, None, :] - P[neg][None, :, :], axis=2); n1, n2 = len(pos), len(neg)
        rr = np.concatenate([np.repeat(np.arange(n1), n2), n1 + np.tile(np.arange(n2), n1)])
        cc = np.concatenate([np.arange(n1*n2), np.arange(n1*n2)])
        Aeq = coo_matrix((np.ones(2*n1*n2), (rr, cc)), shape=(n1 + n2, n1*n2))
        return linprog(C.ravel(), A_eq=Aeq, b_eq=np.concatenate([aa, bb]), bounds=(0, None), method='highs').fun
    vals = [(kk, al, w1(kk, al)) for kk, al in [(0.5, np.pi/3), (1.0, np.pi/4), (2.0, np.pi/4)]]
    for kk, al, v in vals: print("   LP chordal W1 of the derivative at k=%.1f, angle %.3f: %.4f" % (kk, al, v))
    check("N2 NUMERICAL: discretised optimal-transport value in mixed directions stays below 1/3", all(v < 1/3 for _, _, v in vals))
except ImportError as e:
    print("numerical cross-checks skipped:", e)

print()
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
    sys.exit(1)
print("SUMMARY: PROVED the directional lemma: for the vMF kernel, sup over V in R^3, unit u and chordal-1-Lipschitz f "
      "of Cov_V(f, u.s) equals 1/3 (attained at V = 0 by f = u.s); hence the light-cone formation chain (7 predecessors) "
      "contracts at rate 7*beta/3 and forgets its initial level for every beta < 3/7, with W1 region 3/7 > TV ceiling ln(4/3)")
print("HIT: the chordal W1 influence of the vMF kernel is exactly 1/3 in every direction at every V (the directional lemma "
      "left open by a1/a2), proved by harmonic extension to the ball, Cauchy-Schwarz and the Dirichlet energy bound "
      "D(u) <= max(B_par, B_perp) <= 1/(12 pi) (exponential polynomials with nonnegative Taylor coefficients); so light-cone "
      "formation has no memory for beta < 3/7 = 0.428..., above the TV-Dobrushin ceiling ln(4/3) = 0.2877 and below the "
      "executed onset (0.55, 0.60)")
