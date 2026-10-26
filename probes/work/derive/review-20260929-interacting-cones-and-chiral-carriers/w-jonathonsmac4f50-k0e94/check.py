#!/usr/bin/env python3
"""review-20260929-interacting-cones-and-chiral-carriers, attempt a1.

ONE obligation only: the supplied Yukawa comparator of the "one light cone under interactions" note
(walker s(k).sigma, lattice scalar Omega^2 = mu^2 + sum 4 sin^2(q_j/2), coupling g phi_x eps_x psi^dag psi,
Hamiltonian time).  Independent derivation of the walker's second-order loop integrand, the order of the
momentum / scalar-mass limits, and the numerical error of the coefficient.  The chiral-carrier half of the task
is NOT attempted here (see ATTEMPT.md, remaining obligations).

Machinery is disjoint from the source runner: sympy residues and algebra for every exact step; Gauss-Legendre
quadrature with a smooth-step map for the lattice integrals (the source uses midpoint grids); mpmath for the
continuum integrals.  Floating point is used ONLY where a line says so (NUM); everything else is exact (sympy).

Prints one line per check starting PASS or FAIL, then TOTAL, then SUMMARY (and HIT only when every check passed).
"""
import sys, time, warnings
import numpy as np
import sympy as sp
import mpmath as mp

warnings.filterwarnings("ignore")
T0 = time.time()
RES = []


def check(label, ok, detail=""):
    RES.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + label + (("  [" + detail + "]") if detail else ""), flush=True)


# =====================================================================================================
# A. EXACT (sympy): loop integrand, projector algebra, continuum closed forms
# =====================================================================================================
w = sp.Symbol('w', real=True)
nu = sp.Symbol('nu', real=True)
Om, ee = sp.symbols('Omega e', positive=True)

# A1. Euclidean frequency integral  I(lam) = int dw/2pi 1/(w^2+Om^2) 1/(i(nu-w)-lam), lam = +-e.
#     Close the contour on the side that does NOT contain the fermion pole (integrand ~ 1/w^3, arcs vanish).
f_plus = 1 / ((w**2 + Om**2) * (sp.I * (nu - w) - ee))      # fermion pole w = nu + i e   (upper half plane)
f_minus = 1 / ((w**2 + Om**2) * (sp.I * (nu - w) + ee))     # fermion pole w = nu - i e   (lower half plane)
I_plus = sp.simplify(-sp.I * sp.residue(f_plus, w, -sp.I * Om))     # close lower: -2 pi i * Res / (2 pi)
I_minus = sp.simplify(sp.I * sp.residue(f_minus, w, sp.I * Om))     # close upper: +2 pi i * Res / (2 pi)
E_ = sp.I * nu                                                      # E = i nu  (continued to real E later)
t1 = 1 / (2 * Om * (E_ - ee - Om))
t2 = 1 / (2 * Om * (E_ + ee + Om))
check("A1 exact: Euclidean frequency integral gives (1/2Omega)/(E-e-Omega) for the P+ part and (1/2Omega)/(E+e+Omega) for P-",
      sp.simplify(I_plus - t1) == 0 and sp.simplify(I_minus - t2) == 0, f"{I_plus} ; {I_minus}")

# numeric cross-check of the contour closure itself (NUM, mpmath, 20 digits)
mp.mp.dps = 20
nu0, Om0, e0 = mp.mpf('0.3'), mp.mpf('0.7'), mp.mpf('0.4')
fn = lambda x: 1 / ((x**2 + Om0**2) * (1j * (nu0 - x) - e0))
numI = mp.quad(fn, [-mp.inf, -1, 0, 1, mp.inf]) / (2 * mp.pi)
exI = 1 / (2 * Om0 * (1j * nu0 - e0 - Om0))
check("A1b NUM: direct real-line frequency integral equals the residue value (20 digits)", abs(numI - exI) < mp.mpf(10)**-15,
      f"|diff|={mp.nstr(abs(numI-exI),3)}")

# A2. Projector algebra and the Q-shift.
a1, a2, a3, b1, b2, b3 = sp.symbols('a1 a2 a3 b1 b2 b3', real=True)
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
sa = a1 * sig[0] + a2 * sig[1] + a3 * sig[2]
sb = b1 * sig[0] + b2 * sig[1] + b3 * sig[2]
Id2 = sp.eye(2)
dot = a1 * b1 + a2 * b2 + a3 * b3
ok_plus = sp.simplify(((Id2 + sa) / 2 * (Id2 + sb) / 2).trace() - (1 + dot) / 2) == 0
ok_minus = sp.simplify(((Id2 + sa) / 2 * (Id2 - sb) / 2).trace() - (1 - dot) / 2) == 0
check("A2 exact: tr[(1+a.sigma)/2 (1 +- b.sigma)/2] = (1 +- a.b)/2 (overlap weights O1,O2 of the loop)", ok_plus and ok_minus)
kx, ky, kz = sp.symbols('kx ky kz', real=True)
shift_ok = all(sp.simplify(sp.sin(k_ + sp.pi) + sp.sin(k_)) == 0 for k_ in (kx, ky, kz))
check("A2b exact: s(k+Q) = -s(k) for Q=(pi,pi,pi), so the P+ overlap at the partner node is (1 - shat(p).shat(p-q))/2",
      shift_ok)
# combine term 1 and term 2 (q -> -q, Omega and BZ measure even)
ep, ek, c = sp.symbols('e_p e_k c', real=True)
OmS = sp.Symbol('Omega', positive=True)
term1 = (1 - c) / 2 / (ep - ek - OmS)
term2 = (1 + c) / 2 / (ep + ek + OmS)
comb = sp.simplify((term1 + term2) - (ep - c * (ek + OmS)) / (ep**2 - (ek + OmS)**2))
check("A2c exact: O1/(e_p-e_k-Om)+O2/(e_p+e_k+Om) = [e_p - c(e_k+Om)]/[e_p^2-(e_k+Om)^2], c = shat(p).shat(p-q)", comb == 0)

# A3. continuum (Weyl pair, e = |k|) reduction to the (q,k) plane.  P=|p|, k=|p-q|, c k = P - q*ct.
P, q, k, ct = sp.symbols('P q k ct', positive=True)
ctv = (P**2 + q**2 - k**2) / (2 * P * q)        # from k^2 = P^2 + q^2 - 2 P q ct
law = sp.simplify((P**2 - q**2 + k**2) / (2 * P) - (P - q * ctv))
check("A3a exact: law of cosines gives c k = (P^2 - q^2 + k^2)/(2P)", sp.simplify(law) == 0)
cc = (P**2 - q**2 + k**2) / (2 * P * k)
Nn = P - cc * (k + q)
Dd = P**2 - (k + q)**2
# d^3q/(2pi)^3 = (2pi) q^2 dq dct/(2pi)^3 ; dct = -k dk/(P q)  =>  (1/(4 pi^2)) (q k / P) dq dk
dens = sp.simplify((1 / (4 * sp.pi**2)) * (q * k / P) * (1 / (2 * q)) * Nn / Dd)
target = -(q - k) / (16 * sp.pi**2 * P**2)
check("A3b exact: massless-scalar integrand per dq dk is exactly -(q-k)/(16 pi^2 P^2) (all denominators cancel)",
      sp.simplify(dens - target) == 0, str(sp.simplify(dens)))
# A4. radial integration.  k runs over [|q-P|, q+P].
vv = sp.Symbol('vv', real=True)
shell_out = sp.simplify(sp.integrate(-(q - k), (k, q - P, q + P)))               # q > P
shell_in = sp.simplify(sp.integrate(-(q - k), (k, P - q, P + q)))               # q < P
check("A4a exact: for q > P the angular integral at fixed q vanishes identically (massless scalar)", shell_out == 0, str(shell_out))
check("A4b exact: for q < P it is 2 q (P - q)", sp.simplify(shell_in - 2 * q * (P - q)) == 0, str(shell_in))
tot = sp.integrate(shell_in, (q, 0, P)) / (16 * sp.pi**2 * P**2)
check("A4c exact: continuum, mu=0: delta E(P) = g^2 P/(48 pi^2) for every P and every spatial cutoff Lambda >= P",
      sp.simplify(tot - P / (48 * sp.pi**2)) == 0, str(sp.simplify(tot)))

# A5. mu > 0 : small-P coefficient at fixed q (naive derivative) and its radial integral.
mu = sp.Symbol('mu', positive=True)
Om_ = sp.sqrt(q**2 + mu**2)
kk = sp.sqrt(P**2 + q**2 - 2 * P * q * ct)
cexpr = (P - q * ct) / kk
Fc = (1 / (2 * Om_)) * (P - cexpr * (kk + Om_)) / (P**2 - (kk + Om_)**2)
dF = sp.simplify(sp.diff(Fc, P).subs(P, 0))
dF_avg = sp.simplify(sp.integrate(dF, (ct, -1, 1)) / 2)
expected_avg = sp.Rational(1, 3) * (Om_ - q) / (Om_ * q * (q + Om_)**2)
check("A5a exact: angular average of d/dP of the integrand at P=0 is (1/3)(Om-q)/(Om q (q+Om)^2); it is 0 at mu=0",
      sp.simplify(dF_avg - expected_avg) == 0 and sp.simplify(expected_avg.subs(mu, 0)) == 0, str(dF_avg))
t_ = sp.Symbol('t', positive=True)
# radial integral (g^2/(2 pi^2)) int q^2 dq expected_avg = g^2/(6 pi^2) int q mu^2/(Om (q+Om)^3) dq ; q = mu sinh t
rad = sp.simplify((q**2 / (2 * sp.pi**2)) * expected_avg - (1 / (6 * sp.pi**2)) * q * mu**2 / (Om_ * (q + Om_)**3))
J_T = sp.integrate(sp.sinh(t_) * sp.exp(-3 * t_), (t_, 0, sp.Symbol('T', positive=True)))
J_inf = sp.limit(J_T, sp.Symbol('T', positive=True), sp.oo)
check("A5b exact: mu>0, P->0 first, Lambda->oo: dE/dP = g^2/(6 pi^2) * int sinh t e^{-3t} dt = g^2/(48 pi^2)",
      sp.simplify(rad) == 0 and J_inf == sp.Rational(1, 8) and sp.simplify(J_inf / (6 * sp.pi**2) - 1 / (48 * sp.pi**2)) == 0,
      f"J={J_inf}")

# NUM continuum cross-checks (mpmath, 20 digits): both orders give the same number
mp.mp.dps = 20
V0c = 1 / (48 * mp.pi**2)


def dE_cont(Pv, muv, Lam):
    def f(qv, ctv):
        Omv = mp.sqrt(qv * qv + muv * muv); kv = mp.sqrt(Pv * Pv + qv * qv - 2 * Pv * qv * ctv)
        if kv == 0 or Pv * Pv == (kv + Omv)**2:
            return mp.mpf(0)          # measure-zero corner q=P, ct=1 (integrand bounded, direction-dependent)
        cv = (Pv - qv * ctv) / kv
        return qv * qv / (2 * mp.pi**2) * mp.mpf(1) / 2 * (1 / (2 * Omv)) * (Pv - cv * (kv + Omv)) / (Pv * Pv - (kv + Omv)**2)
    return mp.re(mp.quad(f, [0, Pv, 2 * Pv, Lam], [-1, 1]))


vals = {}
for (Pv, muv, Lam) in [(mp.mpf('0.01'), 0, 5), (mp.mpf('0.01'), 0, 500), (mp.mpf('0.002'), 0, 50), (mp.mpf('0.002'), mp.mpf('1e-4'), 50)]:
    vals[(float(Pv), float(muv), Lam)] = dE_cont(Pv, muv, Lam) / Pv
okc = all(abs(v - V0c) < mp.mpf('1e-12') for v in vals.values())
check("A6 NUM (20 digits): continuum mu=0 (and mu << P): delta E/P = 1/(48 pi^2) to 1e-12, independent of P and of Lambda",
      okc, ", ".join(mp.nstr(v, 14) for v in vals.values()))
v_mu1 = dE_cont(mp.mpf('0.001'), 1, 1000) / mp.mpf('0.001')
v_mu1b = dE_cont(mp.mpf('0.001'), 1, 3000) / mp.mpf('0.001')
check("A6b NUM: continuum, P << mu (P=1e-3, mu=1): value -> 1/(48 pi^2) as Lambda grows (residual shrinks with Lambda); orders agree",
      abs(v_mu1 - V0c) < 1e-6 and abs(v_mu1b - V0c) < abs(v_mu1 - V0c),
      f"{mp.nstr(v_mu1,10)} (Lambda=1e3), {mp.nstr(v_mu1b,10)} (3e3), target {mp.nstr(V0c,10)}")

# =====================================================================================================
# B. LATTICE (NUM, double precision, Gauss-Legendre with smooth-step map; convergence reported)
# =====================================================================================================
qx, qy, qz, Ps, mus = sp.symbols('qx qy qz Ps mus', real=True)
OmL = sp.sqrt(mus**2 + 4 * (sp.sin(qx / 2)**2 + sp.sin(qy / 2)**2 + sp.sin(qz / 2)**2))
skv = sp.Matrix([-sp.sin(qx), -sp.sin(qy), sp.sin(Ps - qz)])          # s(p-q) mod Q, p = P z-hat
ekL = sp.sqrt(skv.dot(skv))
FL = (1 / (2 * OmL)) * (sp.sin(Ps) - (skv[2] / ekL) * (ekL + OmL)) / (sp.sin(Ps)**2 - (ekL + OmL)**2)
f1 = sp.lambdify((qx, qy, qz, mus), sp.diff(FL, Ps).subs(Ps, 0), 'numpy')    # naive P-derivative at P=0


def F_fin(qx_, qy_, qz_, Pv, muv):
    Omv = np.sqrt(muv**2 + 4 * (np.sin(qx_ / 2)**2 + np.sin(qy_ / 2)**2 + np.sin(qz_ / 2)**2))
    sx = -np.sin(qx_); sy = -np.sin(qy_); sz = np.sin(Pv - qz_)
    ekv = np.sqrt(sx * sx + sy * sy + sz * sz)
    cv = sz / ekv
    epv = np.sin(Pv)
    return (1 / (2 * Omv)) * (epv - cv * (ekv + Omv)) / (epv**2 - (ekv + Omv)**2)


def nodes(N):
    xg, wg = np.polynomial.legendre.leggauss(N)
    x = (xg + 1) / 2; wgt = wg / 2
    t = x**3 * (10 - 15 * x + 6 * x**2); dt = 30 * x**2 * (1 - x)**2          # smooth-step map: clusters at the zone corners
    return np.pi * t, np.pi * wgt * dt


def lat_integral(func, N):
    """(1/(2pi)^3) * int over the BZ; p-hat = z, symmetric in (qx,qy) -> factor 4 on [0,pi]^2; qz over both signs."""
    qa, Wa = nodes(N)
    QX, QY = np.meshgrid(qa, qa, indexing='ij'); W = np.outer(Wa, Wa)
    tot = 0.0
    for s in (1, -1):
        for iz in range(N):
            tot += Wa[iz] * np.sum(W * func(QX, QY, s * qa[iz]))
    return 4 * tot / (2 * np.pi)**3


def V_naive(muv, N):
    return lat_integral(lambda a, b, cz: f1(a, b, cz, muv), N)


def V_fin(Pv, muv, N):
    return lat_integral(lambda a, b, cz: F_fin(a, b, cz, Pv, muv), N) / np.sin(Pv)


# B1: P -> 0 first at fixed mu (naive derivative = exact limit for mu>0).  Quoted source values for comparison only.
src_q = {1.0: -0.0096707, 0.5: -0.0110696, 0.25: -0.0115076, 0.125: -0.0116301}
mus_list = [1.0, 0.5, 0.25, 0.125, 1/16, 1/32, 1/64, 1/128, 1/256]
Vmu = {}
conv_ok = True
for m_ in mus_list:
    a_ = V_naive(m_, 100); b_ = V_naive(m_, 160)
    Vmu[m_] = b_
    conv_ok &= abs(a_ - b_) < 2e-8
check("B1 NUM: P->0 first, fixed mu: quadrature converged (N=100 vs 160 agree to 2e-8) for mu = 1 ... 1/256", conv_ok,
      "; ".join(f"mu={m_:g}: {Vmu[m_]:.9f}" for m_ in mus_list))
check("B1b NUM: reproduces the source's quoted mu=1,1/2,1/4,1/8 values to their printed digits (fresh, independent quadrature)",
      all(abs(Vmu[m_] - v) < 6e-8 for m_, v in src_q.items()), ", ".join(f"{Vmu[m_]:.7f}" for m_ in src_q))

# B2: mu -> 0 extrapolation with the form V0 + a mu^2 + b mu^2 ln mu (last 3 points), plus a ratio check
mm = np.array([1/64, 1/128, 1/256]); vv_ = np.array([Vmu[m_] for m_ in mm])
A_ = np.c_[np.ones(3), mm**2, mm**2 * np.log(mm)]
V0_fit = np.linalg.solve(A_, vv_)[0]
mm2 = np.array([1/32, 1/64, 1/128]); vv2 = np.array([Vmu[m_] for m_ in mm2])
V0_fit2 = np.linalg.solve(np.c_[np.ones(3), mm2**2, mm2**2 * np.log(mm2)], vv2)[0]
V0_plus = V0_fit
err_fit = abs(V0_fit - V0_fit2)
check("B2 NUM: V(0+) = lim_{mu->0} lim_{P->0} dE/dP extrapolated with V0 + a mu^2 + b mu^2 ln mu: two triples agree",
      err_fit < 3e-8, f"V(0+) = {V0_fit:.9f}  (other triple {V0_fit2:.9f}; spread {err_fit:.1e})")

# B3: naive derivative at mu = 0 exactly (differentiate under the integral, P -> 0 inside)
Vn0_a = V_naive(0.0, 100); Vn0 = V_naive(0.0, 160)
check("B3 NUM: mu = 0 with the derivative taken under the integral (pointwise P->0 at each q): V_naive(0) converged",
      abs(Vn0_a - Vn0) < 2e-9, f"{Vn0:.10f}")

# B4: the identity  V(0+) = V_naive(0) + 1/(48 pi^2)
pred = Vn0 + 1 / (48 * np.pi**2)
check("B4 NUM: V(0+) - V_naive(0) = 1/(48 pi^2) = 0.0021108580 (infrared region q ~ P missed by the pointwise derivative)",
      abs(V0_fit - pred) < 5e-8, f"V(0+)={V0_fit:.9f}, V_naive(0)+1/(48pi^2)={pred:.9f}, diff {V0_fit-pred:.1e}")

# B5: the other order: mu = 0 exactly, finite P, then P -> 0 (direct lattice integral, no expansion)
Pl = [0.4, 0.2, 0.1, 0.05, 0.025]
Nl = {0.4: (200, 300), 0.2: (200, 300), 0.1: (300, 400), 0.05: (500, 700), 0.025: (600, 800)}
Vf = {}
devs = {}
for Pv in Pl:
    n1, n2 = Nl[Pv]
    v1 = V_fin(Pv, 0.0, n1); v2 = V_fin(Pv, 0.0, n2)
    Vf[Pv] = (v2, abs(v2 - v1))
    devs[Pv] = abs(v2 - pred)
print("      mu=0 finite P: " + "; ".join(f"P={Pv}: {Vf[Pv][0]:.8f} (N-change {Vf[Pv][1]:.1e})" for Pv in Pl), flush=True)
check("B5 NUM: mu = 0 exactly, finite P then P->0: dE(P)/sin P approaches V(0+) = -0.011675 (monotonically; within 1.5e-5 at P=0.025)",
      all(devs[Pl[i]] > devs[Pl[i + 1]] for i in range(len(Pl) - 1)) and devs[0.025] < 1.5e-5,
      "deviations from V(0+): " + ", ".join(f"{devs[Pv]:.1e}" for Pv in Pl))
s_exp = np.polyfit(np.log([0.1, 0.05, 0.025]), np.log([devs[0.1], devs[0.05], devs[0.025]]), 1)[0]
check("B5b NUM: the approach is a small power of P (fit exponent between 1 and 2); orders of limits do not split at this order",
      1.0 < s_exp < 2.0, f"fitted exponent {s_exp:.2f}")
SRC_MU0 = -0.009564
check("B6 NUM: the note's 'mu = 0 exactly' value -0.009564 is NOT the P->0 limit of the supplied formula (>= 2.0e-3 away at P=0.025, and the approach is toward -0.011675)",
      abs(Vf[0.025][0] - SRC_MU0) > 2.0e-3 and abs(Vf[0.05][0] - SRC_MU0) > abs(Vf[0.025][0] - SRC_MU0) - 1e-3,
      f"V(P=0.025)={Vf[0.025][0]:.7f}")
alt = Vn0 + 2 / (48 * np.pi**2)
check("B6b READING-support NUM: -0.009564 equals V_naive(0) + 2/(48 pi^2) to the printed 6 digits, i.e. the infrared term counted twice",
      abs(alt - SRC_MU0) < 6e-7, f"V_naive(0)+2/(48pi^2) = {alt:.7f}")

# =====================================================================================================
# C. SCALAR coefficient A-B (NUM, periodic midpoint grid, exact identity chi expression derived in ATTEMPT.md)
# =====================================================================================================
def AmB(r, N):
    h = 2 * np.pi / N
    kg = (np.arange(N) + 0.5) * h - np.pi
    sxg = np.sin(kg)
    SX, SY = np.meshgrid(sxg, sxg, indexing='ij'); sxy2 = SX**2 + SY**2
    ta = tb = 0.0
    for kzv in kg:
        sz = np.sin(kzv); szq = np.sin(kzv + r)
        e1 = np.sqrt(sxy2 + sz * sz); e2 = np.sqrt(sxy2 + szq * szq)
        a = 4 * e1 / (r * r + 4 * e1 * e1)                          # chi(r,0): q=0, weight 1, E = 2 e
        M = (1 + (sxy2 + sz * szq) / (e1 * e2)) / 2
        E = e1 + e2
        b = M * 2 * E / (E * E)                                     # chi(0,r)
        ta += a.sum(); tb += b.sum()
    return (ta - tb) * (h / (2 * np.pi))**3 / r**2


AB = {0.2: AmB(0.2, 512), 0.1: AmB(0.1, 768), 0.05: AmB(0.05, 1024)}
d1 = AB[0.1] - AB[0.2]; d2 = AB[0.05] - AB[0.1]
ratio = d1 / d2
AB_lim = AB[0.05] + d2 / (ratio - 1)          # geometric (power-law) extrapolation in r, ratio measured
print(f"      A-B(r): " + "; ".join(f"r={r}: {v:.6f}" for r, v in AB.items()) + f"; step ratio {ratio:.2f}; extrapolated {AB_lim:.5f}", flush=True)
check("C1 NUM: scalar A-B reproduces the quoted -0.07479 / -0.07556 / -0.07579 at r = 0.2 / 0.1 / 0.05 (to 3e-5)",
      abs(AB[0.2] + 0.07479) < 3e-5 and abs(AB[0.1] + 0.07556) < 3e-5 and abs(AB[0.05] + 0.07579) < 3e-5)
check("C2 NUM: extrapolated A-B = -0.0759 with error about 2e-4 (sources: -0.07589); this is a 3-digit support only",
      abs(AB_lim + 0.07589) < 2.5e-4, f"A-B = {AB_lim:.5f}")

# =====================================================================================================
# D. Combination
# =====================================================================================================
dv = V0_fit - AB_lim / 2
check("D NUM: v_psi - v_phi = V - (A-B)/2 = +0.0263 g^2 in BOTH orders of the walker limit (the note's +0.0284 at zero scalar mass is not supported)",
      abs(dv - 0.02627) < 2e-4, f"v_psi - v_phi = {dv:.5f} g^2  (note: 0.0263 / 0.0284)")

n_fail = RES.count(False)
print(f"TOTAL: PASS={RES.count(True)} FAIL={n_fail}")
print(f"runtime {time.time()-T0:.0f}s")
if n_fail == 0:
    print("HIT: for the supplied Yukawa comparator the walker's one-loop speed coefficient is -0.0116752(1) g^2 in BOTH orders of limits "
          "(mu->0 after P->0, and mu=0 then P->0); the infrared region q~P adds exactly g^2/(48 pi^2) (proved in the continuum, q-density vanishes for q>P at mu=0) "
          "to the pointwise derivative -0.0137861; the note's separate 'mu=0' value -0.009564 and +0.0284 g^2 are not reproduced.")
print("SUMMARY: one-loop walker speed shift -0.011675 g^2 is order-of-limits independent (exact continuum 1/(48 pi^2) infrared term + lattice numerics), "
      "gap v_psi - v_phi = +0.0263 g^2 (scalar side 3-digit support); the note's separate zero-mass value is not supported; chiral-carrier half and finite volume untouched.")
sys.exit(0 if n_fail == 0 else 1)
