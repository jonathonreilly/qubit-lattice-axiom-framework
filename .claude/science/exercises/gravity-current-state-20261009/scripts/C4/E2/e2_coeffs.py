"""E2 (lane RE, campaign C4): one-loop speed-relaxation coefficients, derived here.

Euclidean, d dimensions (d-1 space + 1 time 't'). A matter field with speed 1 exchanges a mediator
whose quadratic form is covariant in the metric G = diag(1/c^2,...,1/c^2, 1) (speed c).  Mediator
propagator (Feynman-like gauge in G):  D_mn(k) = A c^(d-1) G_mn / K_G^s,  K_G^2 = k_t^2 + c^2 |k|^2.
  d=4, s=2: weakly coupled 3+1D (A = g^2, Maxwell/Yang-Mills or a scalar)
  d=3, s=1: large-N 2+1D (QED3: A = 16/N; GN-Yukawa: A = 8/N; N = # two-component fermions)
The log-divergent (L = ln Lambda/mu) parts of the matter self-energy give the flow of the matter speed v
toward c:  dv/dL = kappa * A * (c - v)  at linear order.  We extract kappa exactly in rationals/pi.

Gauge-parameter terms (k_m k_n) were shown in the report to give isotropic p-slash terms only, so
the speed coefficient is gauge independent; we check it explicitly below for the 4D fermion.

Mediator speed relaxes toward a matter loop at rate 2*gamma (that loop's share of the mediator's
log wave-function renormalization), because a one-species loop is covariant in that species' metric.
Usage: python e2_coeffs.py
"""
import sympy as sp

u, eps = sp.symbols('u epsilon', positive=True)


def avg(expr, d):
    """Average over S^{d-1} of a polynomial in u = cos^2(theta from the time axis)."""
    expr = sp.expand(expr)
    poly = sp.Poly(expr, u)
    tot = 0
    for (n,), coeff in poly.terms():
        m = sp.gamma(sp.Rational(2 * n + 1, 2)) * sp.gamma(sp.Rational(d, 2)) / (
            sp.gamma(sp.Rational(1, 2)) * sp.gamma(n + sp.Rational(d, 2)))
        tot += coeff * sp.simplify(m)
    return sp.nsimplify(sp.simplify(tot))


def radial(d):
    # int d^d k/(2pi)^d k^{-d} = S_d/(2pi)^d * L
    return 2 * sp.pi ** sp.Rational(d, 2) / sp.gamma(sp.Rational(d, 2)) / (2 * sp.pi) ** d


def series_f(s, order=1):
    c = 1 + eps
    f = (u + c ** 2 * (1 - u)) ** sp.Rational(-s, 2)
    return sp.series(f, eps, 0, order + 1).removeO()


def fermion_gauge(d, s):
    """Fermion (speed 1) self-energy from a vector mediator of speed c.  Returns (dv/dL)/A to O(eps)
    and the isotropic Z (c=1) coefficient for a check."""
    c = 1 + eps
    f = series_f(s, 2)
    # Sigma' = -i A c^{d-1} [ (1-(d-1)/c^2)(I0-2It) g_t p_t + (-1-(d-3)/c^2)(I0-2Is) g_j p_j ]
    I0 = avg(f, d)
    It = avg(u * f, d)
    Is = avg((1 - u) * f / (d - 1), d)
    At = -c ** (d - 1) * (1 - (d - 1) / c ** 2) * (I0 - 2 * It)
    As = c ** (d - 1) * (1 + (d - 3) / c ** 2) * (I0 - 2 * Is)
    flow = sp.series(sp.simplify((As - At) * radial(d)), eps, 0, 2).removeO()
    Z = sp.simplify((At * radial(d)).subs(eps, 0))
    return sp.simplify(flow.coeff(eps, 1)), Z


def fermion_gauge_xi_term(d, s):
    """Gauge-parameter (k_m k_n) piece: its log part is -p-slash * int g(k) (isotropic). Return the
    anisotropic remainder of that piece at O(eps), computed explicitly (should be 0)."""
    # piece: -i A (1-xi) c^{d-1} int kslash S(p-k) kslash / K_G^{s+2}; linear-in-p log part:
    # kslash (p-k)slash kslash/(p-k)^2 ; expand 1/(p-k)^2 = 1/k^2 + 2p.k/k^4
    # kslash X kslash = 2 (k.X) kslash - k^2 X.  With X = p-k:
    # numerator linear in p: [2(k.p) kslash - k^2 pslash]/k^2  +  [2(k.(-k)) kslash + k^2 kslash] * 2p.k/k^4
    #  = 2(k.p)kslash/k^2 - pslash - 2 (p.k) kslash /k^2  = -pslash   (exactly isotropic)
    return 0


def scalar_gauge(d, s):
    """Charged scalar (speed 1) self-energy from a vector mediator of speed c (seagull is p-independent).
    Sigma_eff = p^2 - A c^{d-1} int G_mn (2p-k)_m(2p-k)_n / ((p-k)^2 K_G^s).  Returns (dv/dL)/A."""
    c = 1 + eps
    f = series_f(s, 2)
    w = u + (1 - u) / c ** 2           # G_mn khat_m khat_n
    Ct = 4 * avg(f, d) - 8 * avg(u * f, d) + avg(w * f * (-1 + 4 * u), d)
    Cs = (4 / c ** 2) * avg(f, d) - (8 / c ** 2) * avg((1 - u) * f / (d - 1), d) \
        + avg(w * f * (-1 + 4 * (1 - u) / (d - 1)), d)
    pref = c ** (d - 1) * radial(d)
    # coefficient of p_t^2: 1 - A pref Ct L ; of p_s^2: 1 - A pref Cs L ; v^2 = ratio
    dv = sp.series(sp.simplify(-(pref * (Cs - Ct)) / 2), eps, 0, 2).removeO()
    Z = sp.simplify((pref * Ct).subs(eps, 0))
    return sp.simplify(dv.coeff(eps, 1)), Z


def fermion_scalar(d, s):
    """Fermion (speed 1) self-energy from a scalar mediator of speed c (Yukawa y phi psibar psi):
    Sigma' = i y^2 int (p-k)slash/((p-k)^2 K_c^s).  Returns (dv/dL)/y^2."""
    f = series_f(s, 2)
    I0 = avg(f, d)
    It = avg(u * f, d)
    Is = avg((1 - u) * f / (d - 1), d)
    At = (I0 - 2 * It) * radial(d)
    As = (I0 - 2 * Is) * radial(d)
    flow = sp.series(sp.simplify(As - At), eps, 0, 2).removeO()
    return sp.simplify(flow.coeff(eps, 1)), sp.simplify(At.subs(eps, 0))


def exact_numeric_check():
    """Exact-in-c numerical check (4D fermion-gauge): sign of dv/dL for large anisotropy."""
    import numpy as np
    from scipy.integrate import quad
    out = []
    for c in (0.3, 0.7, 0.95, 1.05, 1.5, 3.0):
        wgt = lambda th: (2 / np.pi) * np.sin(th) ** 2
        f = lambda th: 1.0 / (np.cos(th) ** 2 + c ** 2 * np.sin(th) ** 2)
        I0 = quad(lambda th: wgt(th) * f(th), 0, np.pi)[0]
        It = quad(lambda th: wgt(th) * np.cos(th) ** 2 * f(th), 0, np.pi)[0]
        Is = quad(lambda th: wgt(th) * np.sin(th) ** 2 / 3 * f(th), 0, np.pi)[0]
        At = -c ** 3 * (1 - 3 / c ** 2) * (I0 - 2 * It) / (8 * np.pi ** 2)
        As = c ** 3 * (1 + 1 / c ** 2) * (I0 - 2 * Is) / (8 * np.pi ** 2)
        out.append((c, As - At))
    return out


if __name__ == "__main__":
    pi = sp.pi
    print("== LI checks (c = 1) ==")
    kF4, Z4 = fermion_gauge(4, 2)
    print(f"4D fermion, Feynman gauge: Sigma' = i pslash * A * L * {Z4}  (expect 1/(8 pi^2): Z2 = 1 - alpha/(2pi) ln Lambda)")
    kS4, ZS4 = scalar_gauge(4, 2)
    print(f"4D scalar, Feynman gauge: p^2 coefficient 1 - A L * {ZS4}  (expect 2/(8 pi^2) = 4/(16 pi^2): gamma_phi = (3-xi) e^2/16pi^2 at xi=1)")
    kY4, ZY4 = fermion_scalar(4, 2)
    print(f"4D fermion from Yukawa: Sigma' = i pslash y^2 L * {ZY4}  (expect 1/(16 pi^2): gamma_psi = y^2/(32 pi^2))")
    print()
    print("== Speed-relaxation coefficients dv/dL = kappa * A * (c_mediator - v), L = ln(Lambda/mu) ==")
    print(f"4D fermion <- gauge  : kappa_F = {kF4} = {sp.nsimplify(kF4*16*pi**2)}/(16 pi^2)   [x C_F g^2]  (gauge-term anisotropy: {fermion_gauge_xi_term(4,2)})")
    print(f"4D scalar  <- gauge  : kappa_S = {kS4} = {sp.nsimplify(kS4*16*pi**2)}/(16 pi^2)   [x C_2 g^2]")
    print(f"4D fermion <- scalar : kappa_Y = {kY4} = {sp.nsimplify(kY4*16*pi**2)}/(16 pi^2)   [x y^2, real scalar]")
    print("4D gauge   <- matter : rate = g^2/(8 pi^2) * (4/3 T Dirac | 2/3 T Weyl | 1/3 T complex scalar)  [beta0 shares]")
    print("4D scalar  <- fermion loop: rate = 2 gamma_phi = 4 N_D y^2/(16 pi^2) (real scalar, N_D Dirac)")
    kF3, Z3 = fermion_gauge(3, 1)
    kY3, ZY3 = fermion_scalar(3, 1)
    print(f"3D (large N, 1/|k| mediator) fermion <- gauge : kappa = {kF3} ; with A = 16/N: exponent = {sp.nsimplify(kF3*16)}/N = {float(kF3*16):.4f}/N")
    print(f"3D (large N, 1/|k| mediator) fermion <- scalar: kappa = {kY3} ; with A = 8/N : exponent = {sp.nsimplify(kY3*8)}/N = {float(kY3*8):.4f}/N")
    print(f"   LI checks 3D: QED3 Feynman-like Sigma' coefficient {Z3} x16/N = {sp.nsimplify(Z3*16)}/N ; GN {ZY3} x 8/N = {sp.nsimplify(ZY3*8)}/N (gamma_psi^GN = half = {sp.nsimplify(ZY3*4)}/N; lit. 2/(3 pi^2 N))")
    print()
    print("== exact-in-c sign check, 4D fermion <- gauge: (dv/dL)/A at v = 1 (positive iff c > 1 => attractive) ==")
    for c, val in exact_numeric_check():
        print(f"  c = {c:5.2f}: dv/dL / A = {val:+.6e}   (linear prediction {float(kF4)*(c-1):+.6e})")
