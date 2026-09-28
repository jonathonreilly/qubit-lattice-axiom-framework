"""The curvature member's exterior on the cubic lattice and the first-order ray turn.

Exact sections (sympy, rational arithmetic) and two labelled floating-point controls.
Setting: block 110 (landed) T1 with the lattice unit-source potential G in place of 1/(4 pi r).
At first order in the charges, chi - 1 = Q G, 1 - N = P G and the rays' index is n = 1 + (3Q + P) G
= 1 + (3a + p) 4 pi G with a = Q/4pi, p = P/4pi (block 110's normalisation).
"""
import sys, time
import sympy as sp

T0 = time.time()
FAILS = []
def want(ok, label):
    print(("PASS " if ok else "FAIL ") + label, flush=True)
    if not ok:
        FAILS.append(label)

x, y, z = sp.symbols('x y z', real=True)
X = (x, y, z)
r = sp.sqrt(x**2 + y**2 + z**2)
S4 = x**4 + y**4 + z**4
def D(f, n): return sum(sp.diff(f, v, n) for v in X)
def lap(f): return D(f, 2)
def zero(e): return sp.simplify(sp.together(sp.expand(e))) == 0

# ---------------------------------------------------------------------------------------------
# A. The lattice unit-source potential: G = G0 + G1 + G2 + G3 + O(r^-9)
# ---------------------------------------------------------------------------------------------
print("== A. lattice Green function expansion (exact)")
k1, k2, k3 = sp.symbols('k1 k2 k3', real=True)
sigma = sum(2 * (1 - sp.cos(k)) for k in (k1, k2, k3))
ser = sp.series(2 * (1 - sp.cos(k1)), k1, 0, 10).removeO()
want(sp.expand(ser - (k1**2 - k1**4 / 12 + k1**6 / 360 - k1**8 / 20160)) == 0,
     "A1 symbol of -Laplacian per axis: 2(1-cos k) = k^2 - k^4/12 + k^6/360 - k^8/20160 + O(k^10)")
# Taylor form of the lattice Laplacian: sum_i f(x+e_i)+f(x-e_i)-2f(x) = Lap f + D4/12 + D6/360 + D8/20160 + ...
h = sp.Symbol('h')
f_test = sp.Function('f')
taylor = sp.series(f_test(h) + f_test(-h) - 2 * f_test(0), h, 0, 10).removeO()
want(all(sp.simplify(taylor.coeff(h, n) - (2 * sp.Subs(sp.Derivative(f_test(h), (h, n)), h, 0) / sp.factorial(n) if n % 2 == 0 else 0)) == 0
         for n in range(1, 10)), "A2 lattice Laplacian = sum over axes of 2 d^(2n)/(2n)! (Taylor)")
# homogeneous inverse-power Fourier transforms (standard): FT[1/k^2]=1/(4 pi r), FT[1/k^4]=-r/(8 pi), FT[1/k^6]=r^3/(96 pi), FT[1/k^8]=-r^5/(2880 pi)
want(zero(lap(r) - 2 / r) and zero(lap(r**3) - 12 * r) and zero(lap(r**5) - 30 * r**3) and zero(lap(1 / r)),
     "A3 Lap r = 2/r, Lap r^3 = 12 r, Lap r^5 = 30 r^3, Lap 1/r = 0 off the origin (so (-Lap)^m of the four kernels is delta)")
G0 = 1 / (4 * sp.pi * r)
# 1/sigma = 1/k^2 + B/k^4 + B^2/k^6 + B^3/k^8, B = S_4/12 - S_6/360 + S_8/20160 (S_m = sum k_i^m); k_i^m -> (-i d_i)^m
G1 = -D(r, 4) / (96 * sp.pi)
G2 = -D(r, 6) / (2880 * sp.pi) + D(D(r**3, 4), 4) / (13824 * sp.pi)
G3 = -D(r, 8) / (161280 * sp.pi) + D(D(r**3, 6), 4) / (207360 * sp.pi) - D(D(D(r**5, 4), 4), 4) / (4976640 * sp.pi)
want(zero(G1 - (5 * S4 - 3 * r**4) / (32 * sp.pi * r**7)), "A4 G1 = (5(x^4+y^4+z^4) - 3 r^4)/(32 pi r^7)")
P2 = sp.expand(sp.simplify(G2 * sp.pi * r**13))
P2_expected = (sp.Rational(23, 128) * (x**8 + y**8 + z**8)
               - sp.Rational(61, 32) * (x**6 * (y**2 + z**2) + y**6 * (x**2 + z**2) + z**6 * (x**2 + y**2))
               + sp.Rational(621, 128) * (x**4 * y**4 + x**4 * z**4 + y**4 * z**4)
               - sp.Rational(57, 32) * x**2 * y**2 * z**2 * (x**2 + y**2 + z**2))
want(sp.expand(P2 - P2_expected) == 0, "A5 G2 = P8(x)/(pi r^13), P8 = 23/128 S8 - 61/32 sum x^6 y^2 + 621/128 sum x^4 y^4 - 57/32 x^2y^2z^2 r^2")
want(zero(lap(G1) + D(G0, 4) / 12), "A6 order r^-5 of the lattice Laplace equation: Lap G1 + D4 G0/12 = 0")
want(zero(lap(G2) + D(G1, 4) / 12 + D(G0, 6) / 360), "A7 order r^-7: Lap G2 + D4 G1/12 + D6 G0/360 = 0")
want(zero(sp.expand(sp.simplify((lap(G3) + D(G2, 4) / 12 + D(G1, 6) / 360 + D(G0, 8) / 20160) * r**21))),
     "A8 order r^-9: Lap G3 + D4 G2/12 + D6 G1/360 + D8 G0/20160 = 0")
# uniqueness of G1: a cubic-invariant, even, degree -3 homogeneous harmonic is h2(x)/r^5 with h2 a cubic-invariant harmonic quadratic
a_ = sp.Symbol('a_')
want(sp.solve(sp.Eq(lap(a_ * (x**2 + y**2 + z**2)), 0), a_) == [0],
     "A9 the only cubic-invariant quadratic form is a r^2, harmonic only for a = 0: G1 is fixed by A6 and cubic symmetry")
# spherical (l = 0) averages of the corrections vanish: sphere moments <x^a y^b z^c> = (a-1)!!(b-1)!!(c-1)!!/(n+1)!! (all even)
def sphere_avg(poly):
    P = sp.Poly(sp.expand(poly), x, y, z); tot = 0
    for (a, b_, c), co in P.terms():
        if a % 2 or b_ % 2 or c % 2: continue
        n = a + b_ + c
        tot += co * sp.factorial2(a - 1) * sp.factorial2(b_ - 1) * sp.factorial2(c - 1) / sp.factorial2(n + 1)
    return sp.nsimplify(tot)
P3 = sp.expand(sp.simplify(G3 * sp.pi * r**19))
want(sphere_avg(5 * S4 - 3 * (x**2 + y**2 + z**2)**2) == 0 and sphere_avg(P2) == 0 and sphere_avg(P3) == 0,
     "A10 G1 r^3, G2 r^5, G3 r^7 have zero average over the sphere (no l = 0 part)")
h4 = 5 * S4 - 3 * (x**2 + y**2 + z**2)**2
want(sphere_avg(P2 * h4) != 0 and sphere_avg(P3 * h4) == 0,
     "A11 l-content: G2 r^5 has an l = 4 part, G3 r^7 has none (the l <= 2k-2 parts of the k-th symbol term are polynomials, so G_k carries only l >= 2k)")
print("   [A took %.0f s]" % (time.time() - T0), flush=True)

# ---------------------------------------------------------------------------------------------
# B. The exterior fields at first order (exact)
# ---------------------------------------------------------------------------------------------
print("== B. first-order exterior: chi - 1 = Q G, 1 - N = P G; relative anisotropy of G")
rel = sp.simplify(G1 / G0)          # (5 S4/r^4 - 3)/(8 r^2)
at = lambda e, pt: sp.simplify(e.subs(dict(zip(X, pt))))
s_ = sp.Symbol('s', positive=True)
want(at(rel, (s_, 0, 0)) == 1 / (4 * s_**2) and at(rel, (s_, s_, 0)) == -1 / (32 * s_**2) and at(rel, (s_, s_, s_)) == -1 / (18 * s_**2),
     "B1 G1/G0 at (s,0,0), (s,s,0), (s,s,s): +1/(4 s^2), -1/(32 s^2), -1/(18 s^2)")
# in terms of r: axis +1/(4r^2); face (r^2 = 2s^2) -1/(16r^2); body (r^2 = 3s^2) -1/(6r^2)
print("   in terms of r: axis +1/(4 r^2), face diagonal -1/(16 r^2), body diagonal -1/(6 r^2) (same for chi-1 and 1-N at first order)")

# ---------------------------------------------------------------------------------------------
# C. The first-order turn: Theta = grad_b of the line integral of (n - 1) along the unperturbed ray
# ---------------------------------------------------------------------------------------------
print("== C. first-order turn corrections (exact)")
b = sp.Symbol('b', positive=True); phi = sp.Symbol('phi', real=True); zz = sp.Symbol('zz', real=True)
def lineint(num, m, t, beta):
    """int_{-inf}^{inf} num(b beta + zz t)/(b^2 + zz^2)^(m/2) dzz for orthonormal t, beta; exact Beta integrals."""
    sub = {x: b * beta[0] + zz * t[0], y: b * beta[1] + zz * t[1], z: b * beta[2] + zz * t[2]}
    P = sp.Poly(sp.expand(num.subs(sub, simultaneous=True)), zz); tot = 0
    for (k,), c in P.terms():
        if k % 2: continue
        j = k // 2
        tot += c * b**(2 * j + 1 - m) * sp.gamma(sp.Rational(2 * j + 1, 2)) * sp.gamma(sp.Rational(m - 2 * j - 1, 2)) / sp.gamma(sp.Rational(m, 2))
    return sp.simplify(tot)
N1 = sp.expand((5 * S4 - 3 * (x**2 + y**2 + z**2)**2) / 8)      # 4 pi G1 = N1/r^7
N2 = sp.expand(4 * P2)                                          # 4 pi G2 = N2/r^13
w = sp.Symbol('w')
def fourier(f):
    g = sp.expand(sp.simplify(f).subs({sp.cos(phi): (w + 1 / w) / 2, sp.sin(phi): (w - 1 / w) / (2 * sp.I)}))
    Pw = sp.Poly(sp.expand(g * w**16), w); cf = {k - 16: c for (k,), c in Pw.terms()}; out = {}
    for k in sorted(set(abs(k) for k in cf)):
        A = cf.get(k, 0); Bm = cf.get(-k, 0)
        if k == 0:
            if sp.simplify(A) != 0: out['1'] = sp.nsimplify(sp.simplify(A))
            continue
        cc = sp.nsimplify(sp.simplify(A + Bm)); ss = sp.nsimplify(sp.simplify(sp.I * (A - Bm)))
        if cc != 0: out['cos%d' % k] = cc
        if ss != 0: out['sin%d' % k] = ss
    return out
v = lambda *c: sp.Matrix(c)
dirs = {
    'axis e3': (v(0, 0, 1), v(sp.cos(phi), sp.sin(phi), 0)),
    'face (1,1,0)/sqrt2': (v(1, 1, 0) / sp.sqrt(2), sp.cos(phi) * v(0, 0, 1) + sp.sin(phi) * v(1, -1, 0) / sp.sqrt(2)),
    'body (1,1,1)/sqrt3': (v(1, 1, 1) / sp.sqrt(3), sp.cos(phi) * v(1, -1, 0) / sp.sqrt(2) + sp.sin(phi) * v(1, 1, -2) / sp.sqrt(6)),
}
expect1 = {'axis e3': {'cos4': sp.Rational(1, 6)},
           'face (1,1,0)/sqrt2': {'cos2': sp.Rational(-1, 12), 'cos4': sp.Rational(1, 8)},
           'body (1,1,1)/sqrt3': {}}
expect2 = {'axis e3': {'cos4': sp.Rational(3, 20), 'cos8': sp.Rational(5, 24)},
           'face (1,1,0)/sqrt2': {'cos4': sp.Rational(19, 192), 'cos6': sp.Rational(-1, 10), 'cos8': sp.Rational(15, 128)},
           'body (1,1,1)/sqrt3': {'cos6': sp.Rational(-4, 135)}}
f1 = lambda t, be: sp.Rational(1, 4) * sum(ti**4 for ti in t) + sum(t[i]**2 * be[i]**2 for i in range(3)) \
    + sp.Rational(2, 3) * sum(bi**4 for bi in be) - sp.Rational(3, 4)
# continuum part: grad_b of int dz/r is -2 beta/b
want(sp.simplify(sp.integrate(b / (b**2 + zz**2)**sp.Rational(3, 2), (zz, -sp.oo, sp.oo)) - 2 / b) == 0,
     "C0 continuum: int b/r^3 dz = 2/b, the turn 2(3a+p)/b toward the body (block 110 T4, first order)")
for name, (t, be) in dirs.items():
    Psi1 = lineint(N1, 7, t, be); Psi2 = lineint(N2, 13, t, be)
    F1 = sp.simplify(Psi1 * b**2); F2 = sp.simplify(Psi2 * b**4)
    want(sp.simplify(F1 - f1(t, be)) == 0, f"C1 {name}: b^2 int 4pi G1 dz = f1(t,beta) = (1/4)S4(t) + sum t_i^2 beta_i^2 + (2/3)S4(beta) - 3/4")
    got1, got2 = fourier(F1), fourier(F2)
    want(got1 == expect1[name], f"C2 {name}: f1 = {expect1[name] or 0} (Fourier in phi)")
    want(got2 == expect2[name], f"C3 {name}: f2 = b^4 int 4pi G2 dz = {expect2[name]}")
# generic orthonormal pairs: the f1 formula
for t, be in [(v(1, 2, 2) / 3, v(2, 1, -2) / 3), (v(1, 2, 2) / 3, v(2, -2, 1) / 3), (v(2, 3, 6) / 7, v(3, -6, 2) / 7), (v(2, 3, 6) / 7, v(6, 2, -3) / 7)]:
    want(sp.simplify(lineint(N1, 7, t, be) * b**2 - f1(t, be)) == 0, f"C4 generic t={list(t)}, beta={list(be)}: f1 formula holds")
# azimuthal average of f1 is zero for every unit t: circle moments <b_i b_j> = P_ij/2, <b_i^4> = 3 P_ii^2/8, P = I - t t
t1_, t2_, t3_ = sp.symbols('t1 t2 t3', real=True)
tt = [t1_, t2_, t3_]
avgS4b = sum(sp.Rational(3, 8) * (1 - ti**2)**2 for ti in tt)
avgmix = sum(ti**2 * (1 - ti**2) / 2 for ti in tt)
avgf1 = sp.Rational(1, 4) * sum(ti**4 for ti in tt) + avgmix + sp.Rational(2, 3) * avgS4b - sp.Rational(3, 4)
want(sp.simplify(avgf1.subs(t3_**2, 1 - t1_**2 - t2_**2)) == 0 or sp.expand(sp.expand(avgf1).subs(t3_, sp.sqrt(1 - t1_**2 - t2_**2))) == 0,
     "C5 <f1>_phi = 0 for every ray direction t (circle moments)")
# zonal lemma behind the all-orders statement: int_{-1}^{1} P_l(u)(1-u^2)^(k-1) du = 0 for l > 2k-2
u = sp.Symbol('u')
want(all(sp.integrate(sp.legendre(l, u) * (1 - u**2)**(k - 1), (u, -1, 1)) == 0 for k in range(1, 6) for l in range(2 * k, 2 * k + 9, 2)),
     "C6 int P_l(u)(1-u^2)^(k-1) du = 0 for l >= 2k (checked k = 1..5, l = 2k..2k+8)")
# order comparison with the continuum second-order turn at equal charges a = p = M/2
M = sp.Symbol('M', positive=True)
nu1 = 3 * (M / 2) + M / 2; nu2 = 3 * (M / 2)**2 + 3 * (M / 2)**2 + (M / 2)**2
ratio = sp.simplify((nu1 / (3 * b**3)) / (sp.pi * (nu2 + nu1**2 / 2) / b**2))
want(sp.simplify(ratio - 8 / (45 * sp.pi * M * b)) == 0,
     "C7 axis, phi=0: lattice b^-3 term / continuum second-order term = 8/(45 pi M b) at a = p = M/2")
print("   [A-C took %.0f s]" % (time.time() - T0), flush=True)

# ---------------------------------------------------------------------------------------------
# D. FLOATING POINT control 1: exact lattice Green function values (Bessel integral, mpmath 40 digits)
# ---------------------------------------------------------------------------------------------
print("== D. FLOATING POINT: lattice G from G(x) = int_0^inf e^{-6t} I_x1(2t) I_x2(2t) I_x3(2t) dt")
import mpmath as mp
mp.mp.dps = 40
def Gex(n1, n2, n3):
    f = lambda t: mp.besseli(n1, 2 * t) * mp.besseli(n2, 2 * t) * mp.besseli(n3, 2 * t) * mp.e**(-6 * t)
    return mp.quad(f, [0, 1, 5, 20, 80, 320, 1280, mp.inf])
g0123 = sp.lambdify(X, G0 + G1 + sp.simplify(G2) + sp.simplify(G3), 'mpmath')
watson = mp.sqrt(6) / (192 * mp.pi**3) * mp.gamma(mp.mpf(1) / 24) * mp.gamma(mp.mpf(5) / 24) * mp.gamma(mp.mpf(7) / 24) * mp.gamma(mp.mpf(11) / 24)
g00 = Gex(0, 0, 0)
want(abs(g00 - watson) < mp.mpf('1e-17'), "D1 G(0) = sqrt6/(192 pi^3) Gamma(1/24)Gamma(5/24)Gamma(7/24)Gamma(11/24) = %s (Watson); quadrature differs by %s" % (mp.nstr(watson, 20), mp.nstr(g00 - watson, 3)))
for name, pts in [("axis", [(16, 0, 0), (24, 0, 0)]), ("face", [(16, 16, 0), (24, 24, 0)]),
                  ("body", [(16, 16, 16), (24, 24, 24)]), ("generic", [(32, 16, 0), (48, 24, 0)])]:
    scaled = []
    for p in pts:
        pr = [mp.mpf(q) for q in p]; rr = mp.sqrt(sum(q * q for q in pr))
        scaled.append((Gex(*p) - g0123(*pr)) * rr**9)
    ok = abs(scaled[0] - scaled[1]) < mp.mpf('0.35') * abs(scaled[1]) + mp.mpf('0.05')
    want(ok, f"D2 {name}: (G - G0 - G1 - G2 - G3) r^9 = {mp.nstr(scaled[0], 5)}, {mp.nstr(scaled[1], 5)} (bounded: remainder is O(r^-9))")

# ---------------------------------------------------------------------------------------------
# E. FLOATING POINT control 2: direct rays of H = c|k|, c = 1/n, n = 1 + eps 4 pi (G0 + G1)
# ---------------------------------------------------------------------------------------------
print("== E. FLOATING POINT: integrated rays vs the first-order turn (inward 2/b + 2 f1/b^3, sideways f1'/b^3)")
import numpy as np
from scipy.integrate import solve_ivp, quad
eps = 1e-6; L = 400.0
def n1(p):
    rr = np.sqrt(p @ p); return 1 / rr + (5 * np.sum(p**4) - 3 * rr**4) / (8 * rr**7)
def grad_n1(p, hh=1e-5):
    return np.array([(n1(p + hh * e) - n1(p - hh * e)) / (2 * hh) for e in np.eye(3)])
def ray_turn(t, be, bb):
    t = np.array(t, float); be = np.array(be, float); x0 = bb * be - L * t
    def rhs(_, Y):
        p, k = Y[:3], Y[3:]; nn = 1 + eps * n1(p); c = 1 / nn; kn = np.linalg.norm(k)
        gc = -eps * grad_n1(p) / nn**2
        return np.concatenate([c * k / kn, -kn * gc])
    ev = lambda _, Y: (Y[:3] @ t) - L; ev.terminal = True
    sol = solve_ivp(rhs, [0, 3 * L], np.concatenate([x0, t]), method='DOP853', rtol=1e-12, atol=1e-14, events=ev)
    k = sol.y[3:, -1]; dk = k / np.linalg.norm(k) - t
    return dk / eps
def born_turn(t, be, bb):
    t = np.array(t, float); be = np.array(be, float)
    comp = [quad(lambda s: grad_n1(bb * be + s * t)[i], -L, L, limit=400, epsabs=1e-13)[0] for i in range(3)]
    return np.array(comp)
for name, t, be, ph in [("axis phi=0", (0, 0, 1), (1, 0, 0), 0.0), ("axis phi=pi/8", (0, 0, 1), (np.cos(np.pi / 8), np.sin(np.pi / 8), 0), np.pi / 8),
                        ("body phi=0.3", tuple(np.ones(3) / np.sqrt(3)), tuple(np.cos(0.3) * np.array([1, -1, 0]) / np.sqrt(2) + np.sin(0.3) * np.array([1, 1, -2]) / np.sqrt(6)), 0.3)]:
    bb = 2.5
    th = ray_turn(t, be, bb); bn = born_turn(t, be, bb)
    tv = np.array(t, float); bev = np.array(be, float); phat = np.cross(tv, bev)
    # finite-L continuum part of the Born turn: -(2/b) L/sqrt(L^2+b^2) along beta; lattice part integrates to its infinite value within 1e-9 at L = 400
    fin = 2 / bb * L / np.sqrt(L**2 + bb**2)
    if name.startswith("axis"):
        f1v = np.cos(4 * ph) / 6; f1p = -4 * np.sin(4 * ph) / 6
    else:
        f1v = 0.0; f1p = 0.0
    inward_pred = fin + 2 * f1v / bb**3; side_pred = f1p / bb**3
    ok = np.linalg.norm(th - bn) < 1e-5 and abs(-(bn @ bev) - inward_pred) < 1e-8 and abs(bn @ phat - side_pred) < 1e-8
    want(ok, f"E1 {name}, b={bb}: ray inward {-(th @ bev):.9f} sideways {th @ phat:.3e}; Born inward {-(bn @ bev):.9f} (pred {inward_pred:.9f}) sideways {bn @ phat:.3e} (pred {side_pred:.3e})")

print("   [total %.0f s]" % (time.time() - T0))
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + FAILS[0]); sys.exit(1)
print("SUMMARY: PROVED (given the standard asymptotic expansion of the simple-cubic lattice Green function, derived term by term and checked) "
      "at first order in the charges the member's exterior is chi-1 = QG, 1-N = PG with G = 1/(4 pi r) + (5 sum x_i^4 - 3 r^4)/(32 pi r^7) + O(r^-5); "
      "the rays' turn is (3a+p)[2/b + 2 f1/b^3 + 4 f2/b^5 + ...] toward the body plus (3a+p)[f1'/b^3 + f2'/b^5 + ...] sideways, "
      "f1 = (1/4) sum t_i^4 + sum t_i^2 beta_i^2 + (2/3) sum beta_i^4 - 3/4; axis f1 = cos(4 phi)/6, face diagonal -cos(2phi)/12 + cos(4phi)/8, "
      "body diagonal f1 = 0 and f2 = -(4/135) cos(6 phi); the azimuthal average of every correction vanishes")
print("HIT: first direction-dependent term of the member's first-order ray turn on the cubic lattice is O(b^-3): "
      "(3a+p)(2 f1 inward, f1' sideways)/b^3 with f1 = (1/4)S4(t) + sum t_i^2 beta_i^2 + (2/3)S4(beta) - 3/4; "
      "along an axis inward (3a+p)cos(4phi)/(3b^3), sideways -(2/3)(3a+p)sin(4phi)/b^3; zero along the body diagonal, "
      "whose first anisotropy is -(16/135)(3a+p)cos(6phi)/b^5 inward, (8/45)(3a+p)sin(6phi)/b^5 sideways; "
      "no b^-2, b^-4 terms and zero azimuthal average at every order (point source at a site or cubic-symmetric content)")
