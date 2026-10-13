#!/usr/bin/env python3
"""R16-14 (C5 round 16, item 14): set A, noise-fed PPN test for E1 and E2.
Every number in the report comes from this file's output.  OMP_NUM_THREADS=2; runtime ~1 min.
Subtraction rule: each section prints what is subtracted.
"""
import numpy as np, mpmath as mp, sympy as sp
from scipy import special, integrate
np.set_printoptions(precision=4)
rng = np.random.default_rng(16014)

# ---------------- constants (SI; RECALLED unless stated) ----------------
G = 6.674e-11; c = 2.99792458e8; hbar = 1.054571817e-34
Msun = 1.989e30; Rsun = 6.957e8; AU = 1.496e11
H0 = 67.7e3 / 3.0857e22                     # s^-1 (Planck-like, RECALLED)
rho_crit = 3 * H0**2 / (8 * np.pi * G); rho_L = 0.69 * rho_crit
tH = 1 / H0
w_cmb = 369.8e3                              # solar CMB speed (Planck 2018, via vR11-5 web check)
lP2 = hbar * G / c**3
print("[0] constants: H0 = %.4e s^-1, rho_crit = %.4e kg/m^3, rho_L = %.4e kg/m^3, l_P^2 = %.3e m^2" % (H0, rho_crit, rho_L, lP2))
# Bounds (RECALLED, as the item states): |alpha1| < 1e-5, |alpha2| < 2e-9, |gamma-1| < 2.3e-5;
# |beta-1| < 8e-5 (Will 2014, perihelion; RECALLED); Mercury anomalous perihelion |dw/dt| < 0.003"/cy (Pitjeva-Pitjev, RECALLED)
B_a1, B_a2, B_g, B_b = 1e-5, 2e-9, 2.3e-5, 8e-5
B_a2_sun = 4e-7                              # solar-spin alpha2 (Will 2014, RECALLED; via vR11-5)
gam_max = 0.047 * H0                          # E2 drag-allowed range 0.016-0.047 H0 (vR14-2:3)
ctau_max = 1.49e-3                            # E1/E2 tau_c drag ceiling (R14-2:168-176; vR14-2:7)
ell_min, ell_max = 4e-10, 5e-6               # R6-4 conservative window (vR6-4:7)
print("    bounds: alpha1 %.0e, alpha2 %.0e (solar spin %.0e), gamma-1 %.1e, beta-1 %.0e; E2 gamma <= %.3e s^-1; c tau_c <= %.2e m" % (B_a1, B_a2, B_a2_sun, B_g, B_b, gam_max, ctau_max))

# ---------------- [1] E1 repaired gain: Taylor coefficients ----------------
x = sp.symbols('x', real=True)
Ft = (1 - 4*sp.I*x) * (1 - sp.I*x)**(-4)
ser = sp.series(Ft, x, 0, 7).removeO()
print("\n[1] E1 repaired gain F_t(x) = (1-4ix)(1-ix)^-4, x = omega tau (subtraction: 1)")
print("    series:", sp.expand(ser))
coef = [sp.nsimplify(sp.expand(ser).coeff(x, n)) for n in range(7)]
print("    coefficients x^0..x^6:", coef)

# ---------------- [2] exact mean potential of a moving Gaussian body, E1 ----------------
# units G = M = a = 1 (a = Gaussian width), c irrelevant (Newtonian mean field, omega = k.u)
# dPhi(r,theta) = -(1/pi) int_0^inf dk int_-1^1 dmu rho~(k) (K-1) J0(k r sin th sqrt(1-mu^2)) exp(i k r mu cos th)
# (prefactor: -4 pi G (2pi)/(2pi)^3 = -1/pi)
kk, wk = np.polynomial.legendre.leggauss(1600); kmax = 12.0
kq = 0.5 * kmax * (kk + 1); wq = 0.5 * kmax * wk
mu, wmu = np.polynomial.legendre.leggauss(400)
def potential(r, th, Kfun):
    K, MU = np.meshgrid(kq, mu, indexing='ij')
    integrand = np.exp(-K**2 / 2) * Kfun(K, MU) * special.j0(K * r * np.sin(th) * np.sqrt(1 - MU**2)) * np.exp(1j * K * r * MU * np.cos(th))
    return (-(1 / np.pi) * np.einsum('i,j,ij->', wq, wmu, integrand)).real
def Phi_G(r):  # Gaussian-body potential, G = M = a = 1
    return -special.erf(r / np.sqrt(2)) / r
s = 0.05      # s = u tau / a
FtN = lambda X: (1 - 4j * X) / (1 - 1j * X)**4
Kfun_E1 = lambda K, MU: FtN(s * K * MU) - 1.0
# check the plain potential first
print("\n[2] E1: exact mean potential of a moving Gaussian body (u along z; s = u tau/a = %.2f); subtraction: the GR (F = 1) potential" % s)
print("    quadrature check, F = 1: Phi(3, 0.7) = %.8f vs -erf/r = %.8f" % (potential(3.0, 0.7, lambda K, MU: np.ones_like(K)), Phi_G(3.0)))
def dz_n(f, R, th, n, h=1e-2):
    z0, x0 = R * np.cos(th), R * np.sin(th)
    F = lambda z: f(np.hypot(x0, z))
    if n == 2: return (F(z0 + h) - 2 * F(z0) + F(z0 - h)) / h**2
    if n == 3: return (F(z0 + 2*h) - 2 * F(z0 + h) + 2 * F(z0 - h) - F(z0 - 2*h)) / (2 * h**3)
for (R, th) in [(2.0, 0.3), (4.0, 0.0), (4.0, 1.2), (8.0, 0.0), (8.0, 0.9)]:
    num = potential(R, th, Kfun_E1)
    pred_even = -6 * s**2 * dz_n(Phi_G, R, th, 2)
    pred_odd = -20 * s**3 * dz_n(Phi_G, R, th, 3)
    print("    r=%.0f th=%.1f: dPhi = %+.4e; prediction -6s^2 (u.grad)^2 Phi - 20 s^3 (u.grad)^3 Phi = %+.4e (even %+.3e, odd %+.3e); r*dPhi = %+.2e"
          % (R, th, num, pred_even + pred_odd, pred_even, pred_odd, R * num))
rr = np.array([4.0, 6.0, 8.0, 10.0]); vals = np.array([abs(potential(R, 0.0, Kfun_E1)) for R in rr])
print("    on-axis falloff slope d ln|dPhi|/d ln r (r = 4..10): %s  -> 1/r^3 (quadrupole-type), no 1/r (PPN) term" % np.round(np.diff(np.log(vals)) / np.diff(np.log(rr)), 3))

# ---------------- [3] E2 friction: frame dipole ----------------
# K_gamma - K_R with omega = k u mu (c = 1): 1/(k^2(1-u^2 mu^2) - i g k u mu) - 1/(k^2(1-u^2 mu^2))
uu, gg = 0.01, 1e-3
def Kfun_E2(K, MU):
    d0 = K**2 * (1 - uu**2 * MU**2)
    return K**2 * (1 / (d0 - 1j * gg * K * uu * MU) - 1 / d0)   # multiply by k^2 because potential() divides by nothing: see below
# potential() integrates rho~ * Kfun with measure dk dmu (k^2 dk/k^2 already absorbed: K-1 multiplies 1/k^2 * k^2) -> pass k^2 * deltaK
print("\n[3] E2-h friction: exact mean potential of a moving Gaussian body (u = %.2f c, gamma = %.0e c/a); subtraction: the undamped (gamma = 0) potential" % (uu, gg))
for (R, th) in [(3.0, 0.3), (6.0, 0.0), (6.0, 1.0), (9.0, 0.5)]:
    p1, p2 = potential(R, th, Kfun_E2), potential(R, np.pi - th, Kfun_E2)
    odd, even = (p1 - p2) / 2, (p1 + p2) / 2
    pred = 0.5 * gg * uu * np.cos(th)        # (G M gamma / 2 c^2)(u . x^), point-mass form
    print("    r=%.0f th=%.1f: odd part = %+.5e vs frame dipole (G M gamma/2c^2) u cos th = %+.5e (ratio %.4f); even part = %+.4e"
          % (R, th, odd, pred, odd / pred, even))
print("    even part ~ constant gamma u/2 = %.2e (k -> 0 region k < gamma u/c, i.e. r > c^2/(gamma u)): a constant potential, no force;" % (gg * uu / 2))
print("    in SI c^2/(gamma w) = %.1e m at gamma = 0.047 H0, beyond the Hubble radius" % (c**2 / (0.047 * H0 * w_cmb)))

# ---------------- [4] homogeneous spheroid: index symbols and the alpha2-hat map ----------------
def Aidx(a):
    a = np.asarray(a, float); out = []
    for i in range(3):
        f = lambda t: 1 / ((a[i]**2 + t) * np.sqrt(np.prod(a**2 + t)))
        out.append(np.prod(a) * integrate.quad(f, 0, np.inf, limit=400, epsabs=1e-14, epsrel=1e-12)[0])
    return np.array(out)
eta = 1e-4; eps_i = np.array([eta / 3, eta / 3, -2 * eta / 3]); a_i = 1 + eps_i
A = Aidx(a_i)
print("\n[4] homogeneous ellipsoid a_i = 1 + eps_i (volume-preserving, eps = %s): A_i - 2/3 = %s; prediction -(4/5) eps_i = %s"
      % (eps_i, A - 2/3, -0.8 * eps_i))
# anisotropic parts: gain self-energy E_d = 3 tau^2 * 2 pi G rho M sum A_i u_i^2; alpha2 self-energy (a2/2c^2) sum W_ii u_i^2, W_ii = -(2pi/5) G rho M A_i a_i^2
dAn = (A - 2/3); dAI = A * a_i**2 - (2/3)
K_map = (6 * np.pi * (-0.8)) / ((-(2*np.pi/5) / 2) * (np.polyfit(eps_i, dAI, 1)[0]))
print("    d(A_i a_i^2)/d eps_i = %.4f (prediction 8/15 = %.4f); alpha2_eff = K (c tau / R)^2 with K = %.3f (analytic 45)"
      % (np.polyfit(eps_i, dAI, 1)[0], 8/15, K_map))

# ---------------- [5] effective alpha, gamma tables at the test scales ----------------
print("\n[5] O(G) frame terms mapped to effective PPN parameters at each test's scale (subtraction: GR's boosted linear field)")
tests = [("solar spin (alpha2, r = R_sun)", Rsun, w_cmb, None),
         ("pulsar spin (alpha2-hat, r = 12 km)", 1.2e4, 3.0e5, None),
         ("PSR J1738+0333 orbit (alpha1-hat, a = 1.74e9 m)", 1.74e9, 3.0e5, 3.5e5),
         ("planetary/LLR (alpha1, r = 1 AU)", AU, w_cmb, 2.98e4)]
for ctau, lab in [(ell_max, "E1 strict tau = l/c (l = 5e-6 m)"), (ctau_max, "E1/E2 tau_c ceiling (c tau_c = 1.49e-3 m)")]:
    print("  gain term (both routes; repaired gain P-r13b), %s:" % lab)
    for name, r, wv, vorb in tests:
        if vorb is None:
            val = 45 * (ctau / r)**2; bnd = B_a2_sun if 'solar' in name else B_a2
        else:
            val = 6 * (ctau / r)**2 * (wv / vorb); bnd = B_a1
        print("    %-48s effective = %.2e  bound %.0e  margin %.1f decades" % (name, val, bnd, np.log10(bnd / val)))
print("  E2 friction (gamma = 0.047 H0 = %.2e s^-1):" % gam_max)
for name, r, wv, vorb in tests:
    if vorb is None:
        val = (gam_max * r / c)**2        # even (gamma^2) part; the odd frame dipole gives no torque on a reflection-symmetric body (proved)
        bnd = B_a2_sun if 'solar' in name else B_a2
        print("    %-48s even part (gamma r/c)^2 = %.2e  bound %.0e  margin %.1f decades" % (name, val, bnd, np.log10(bnd / val)))
    else:
        val = gam_max * r / (2 * vorb); bnd = B_a1
        print("    %-48s frame dipole gamma r/(2 v) = %.2e  bound %.0e  margin %.1f decades" % (name, val, bnd, np.log10(bnd / val)))
# gamma_PPN: Cassini; E1 temporal gain at impact parameter b >= R_sun, E2 frame dipole along a 1 AU path vs Shapiro log
b = Rsun; Lpath = AU; shap_log = np.log(4 * AU * 8.4 * AU / b**2)
g_E1 = 6 * (5e-12 * w_cmb / b)**2
g_E2 = gam_max * w_cmb * Lpath / (2 * c**2) / shap_log
print("  gamma_PPN (Cassini, |gamma-1| < %.1e): E1 gain (6 (tau_c w/b)^2, b = R_sun) = %.1e; E2 frame dipole/Shapiro log = %.1e; spatial smearing exp(-b^2/2l^2) = 0"
      % (B_g, g_E1, g_E2))

# ---------------- [6] beta: linear record metric vs GR completion; perihelion by exact orbit integration ----------------
mp.mp.dps = 30
def apsidal_shift(beta, gamma, m=1, rp=800, ra=1200):
    m, rp, ra, beta, gamma = mp.mpf(m), mp.mpf(rp), mp.mpf(ra), mp.mpf(beta), mp.mpf(gamma)
    A = lambda r: 1 - 2*m/r + 2*beta*(m/r)**2
    B = lambda r: 1 + 2*gamma*m/r
    # B r^2 (E^2/A - 1) = L^2 at both turning points -> solve for E^2, L^2
    M = mp.matrix([[B(rp)*rp**2/A(rp), -1], [B(ra)*ra**2/A(ra), -1]]); v = mp.matrix([B(rp)*rp**2, B(ra)*ra**2])
    E2, L2 = mp.lu_solve(M, v)
    Q = lambda r: (B(r) * r**4 / L2) * (E2 / A(r) - 1) - r**2      # (dr/dphi)^2
    f = lambda chi: ((ra - rp) / 2 * mp.sin(chi)) / mp.sqrt(abs(Q((rp + ra) / 2 - (ra - rp) / 2 * mp.cos(chi))))
    return 2 * mp.quad(f, [0, mp.pi]) - 2 * mp.pi
a_, e_ = 1000, 0.2
gr_pred = 6 * mp.pi / (a_ * (1 - e_**2))
s11 = apsidal_shift(1, 1); s01 = apsidal_shift(0, 1)
print("\n[6] beta (static spherical, isotropic coords; subtraction: 2 pi). Orbit a = 1000 m, e = 0.2:")
print("    beta=1,gamma=1 (GR / completion N): shift = %.6e; (2+2g-b)/3 * 6 pi m/(a(1-e^2)) = %.6e" % (s11, gr_pred))
print("    beta=0,gamma=1 (metric linear in records of T): shift = %.6e; ratio to GR = %.5f (PPN predicts 4/3 = %.5f)" % (s01, s01 / s11, 4/3))
merc_GR = 42.98
print("    Mercury: GR 42.98\"/cy; linear record metric gives %.2f\"/cy, excess %.2f\"/cy vs |anomaly| < 0.003\"/cy (RECALLED): ruled out by %.1f decades; beta-1 = -1 vs |beta-1| < 8e-5"
      % (merc_GR * float(s01 / s11), merc_GR * float(s01 / s11 - 1), np.log10(merc_GR * float(s01 / s11 - 1) / 0.003)))

# literal linear-coupling reading (R13-6 E1-H1: matter feels h only through (1/2) h_mn T^mn, h linear in records of T):
eU, ev = sp.symbols('U v', positive=True); bet, gm = sp.symbols('beta gamma')
L_ppn = -sp.sqrt(1 - 2*eU + 2*bet*eU**2 - (1 + 2*gm*eU)*ev**2)
L_lin = -sp.sqrt(1 - ev**2) + eU*(1 + ev**2)/sp.sqrt(1 - ev**2)       # (1/2) h_mn u^m u^n / u^0 with h_00 = h_ii = 2U
def coeffs(L):
    t = sp.symbols('t'); ser = sp.series(L.subs({eU: t**2*eU, ev: t*ev}), t, 0, 5).removeO()
    return sp.expand(ser.coeff(t, 4))
c_ppn, c_lin = coeffs(L_ppn), coeffs(L_lin)
sol = sp.solve([sp.Eq(c_ppn.coeff(eU, 1).coeff(ev, 2), c_lin.coeff(eU, 1).coeff(ev, 2)),
                sp.Eq(c_ppn.coeff(eU, 2).coeff(ev, 0), c_lin.coeff(eU, 2).coeff(ev, 0))], [bet, gm], dict=True)
print("    1PN test-mass Lagrangian, O(eps^4) part: geodesic PPN %s ; linear coupling %s -> effective %s" % (c_ppn, c_lin, sol))
s05 = apsidal_shift(0.5, 1)
print("    beta=1/2,gamma=1 (linear coupling): shift = %.6e; ratio to GR = %.5f (PPN 7/6 = %.5f); Mercury %.2f\"/cy, excess %.2f\"/cy (%.1f decades over 0.003\"/cy)"
      % (s05, s05 / s11, 7/6, merc_GR * float(s05 / s11), merc_GR * float(s05 / s11 - 1), np.log10(merc_GR * float(s05 / s11 - 1) / 0.003)))

# ---------------- [7] noise medium: perihelion and alpha from a uniform gravitating medium ----------------
aM, eM, MM = 5.791e10, 0.2056, Msun
def harmonic_shift(kappa_rel):   # Newtonian orbit (GM = 1, a = 1, e = eM) plus attractive dV = kappa r^2/2; returns shift per orbit
    rp, ra = 1 - mp.mpf(eM), 1 + mp.mpf(eM)
    V = lambda r: -1 / r + kappa_rel * r**2 / 2
    # E, L from turning points: E = V(r) + L^2/(2 r^2) at rp and ra
    L2 = 2 * (V(ra) - V(rp)) / (1 / rp**2 - 1 / ra**2); E = V(rp) + L2 / (2 * rp**2)
    f = lambda chi: (mp.sqrt(L2) * (ra - rp) / 2 * mp.sin(chi)) / (((rp + ra)/2 - (ra - rp)/2 * mp.cos(chi))**2 *
        mp.sqrt(abs(2 * (E - V((rp + ra)/2 - (ra - rp)/2 * mp.cos(chi))) - L2 / ((rp + ra)/2 - (ra - rp)/2 * mp.cos(chi))**2)))
    return 2 * mp.quad(f, [0, mp.pi]) - 2 * mp.pi
kap = mp.mpf('1e-8')
num = harmonic_shift(kap); pred = -3 * mp.pi * kap * mp.sqrt(1 - eM**2)
print("\n[7] uniform medium (active density rho_act = rho + 3p) in Mercury's orbit; subtraction: 2 pi (Newtonian closed orbit)")
print("    check: dV = kappa r^2/2, kappa = 1e-8 GM/a^3: shift = %.6e vs -3 pi kappa a^3 sqrt(1-e^2)/GM = %.6e" % (num, pred))
coefM = 4 * np.pi**2 * aM**3 * np.sqrt(1 - eM**2) / MM           # |shift| per orbit per (kg/m^3)
orb_cy = 36525 / 87.969; bound_rad_orbit = 0.003 / 206264.806 / orb_cy
rho_act_max = bound_rad_orbit / coefM
print("    |dw| = 4 pi^2 rho_act a^3 sqrt(1-e^2)/M = %.3e rad/orbit per kg/m^3; bound %.2e rad/orbit -> |rho_act| < %.2e kg/m^3 = %.2e rho_L"
      % (coefM, bound_rad_orbit, rho_act_max, rho_act_max / rho_L))
print("    in-window medium (budget: rho_n <= rho_L, radiation-like rho_act = 2 rho_n): |dw| = %.2e rad/orbit, margin %.1f decades"
      % (coefM * 2 * rho_L, np.log10(bound_rad_orbit / (coefM * 2 * rho_L))))
# constraint-channel field energy (R15-2 |u1| = hbar I_F /(32 pi^1.5 l^3 tau), I_F = 21/32), as kg/m^3
def u1(ell, ctau): return hbar * (21 / 32) / (32 * np.pi**1.5 * ell**3 * (ctau / c)) / c**2
print("    constraint-channel |u1|/rho_L (recheck of R15-2 table) and Mercury test with |rho_act| <= 6|u1| (S+V, both signs, p = u/3):")
for ell in [4e-10, 1e-9, 1e-8, 3e-8, 1e-7, 1e-6, 5e-6]:
    for ctau, lab in [(ell, "strict"), (ctau_max, "tau_c ceiling")]:
        val = u1(ell, ctau)
        print("      l = %.0e m, %-13s |u1| = %.2e rho_L; 6|u1| vs Mercury: %s (ratio %.1e)" % (ell, lab, val / rho_L, "pass" if 6 * val < rho_act_max else "FAIL", 6 * val / rho_act_max))
# relic TT data (R16-4's G(1,1/l) witness; excluded by the item's datum h_TT = 0): Mercury test on 2*Delta rho (radiation, rho+3p = 2 rho)
print("    relic free TT data, one quantum per mode to k = 1/l (R16-4 witness; the item fixes h_TT = 0): Mercury test on rho_act = 2 hbar c/(4 pi^2 l^4)/c^2")
for ell in [4e-10, 1e-8, 2e-8, 1e-7, 1e-6, 5e-6]:
    dr = hbar * c / (4 * np.pi**2 * ell**4) / c**2
    print("      l = %.0e m: Delta rho = %.2e rho_L; 2 Delta rho / Mercury bound = %.1e -> %s" % (ell, dr / rho_L, 2 * dr / rho_act_max, "FAIL" if 2 * dr > rho_act_max else "pass"))
# alpha_eff of the medium ~ 3 rho_act / rhobar(r)
for name, r, M in [("J1738 orbit", 1.74e9, 1.65 * Msun), ("1 AU", AU, Msun), ("Sun (solar spin)", Rsun, Msun), ("NS spin", 1.2e4, 1.4 * Msun)]:
    rb = 3 * M / (4 * np.pi * r**3)
    print("    medium alpha_eff ~ 3 rho_act/rhobar at %-17s: in-window (rho_act = 2 rho_L) %.1e; worst case 6|u1|(4e-10 m, strict) %.1e"
          % (name, 3 * 2 * rho_L / rb, 3 * 6 * u1(4e-10, 4e-10) / rb))

# ---------------- [8] O(<h^2>) no-derivative dressing: constant-H model ----------------
print("\n[8] O(<h^2>) terms with no derivative on the noise = constant-H problem: Phi(A x), A = sqrt(1 + H) (subtraction: Phi(x))")
def sym_tt(n, sig, kap):
    Hs = rng.normal(size=(n // 2, 3, 3)); Hs = np.concatenate([Hs, -Hs]); Hs = (Hs + np.transpose(Hs, (0, 2, 1))) / 2   # antithetic pairs
    Hs -= np.trace(Hs, axis1=1, axis2=2)[:, None, None] * np.eye(3) / 3
    W = np.diag([1.0, 1.0, np.sqrt(1 + kap)])            # anisotropic weight along e_z (the frame velocity in the body frame)
    return sig * W @ Hs @ W
def dress(kap, n=200000, sig=1e-3):
    Hs = sym_tt(n, sig, kap); h2 = np.mean(np.einsum('nij,nij->n', Hs, Hs))
    th = np.linspace(0, np.pi, 7); out = []
    for t in th:
        xv = np.array([np.sin(t), 0, np.cos(t)])
        Hx = Hs @ xv; Ax = xv + 0.5 * Hx - 0.125 * np.einsum('nij,nj->ni', Hs, Hx)
        out.append(np.mean(-1 / np.linalg.norm(Ax, axis=1)) + 1.0)
    P2 = 0.5 * (3 * np.cos(th)**2 - 1); cfit = np.polyfit(P2, np.array(out) / h2, 1)
    return cfit, h2
c_iso, h2i = dress(0.0); c_an, h2a = dress(0.5)
print("    isotropic TT-like H: dPhi/<H_ij H_ij> = %.4f + %.4f P2(cos th)  (per 1/r)" % (c_iso[1], c_iso[0]))
print("    anisotropic (kappa = 0.5): dPhi/<H_ij H_ij> = %.4f + %.4f P2(cos th); d c2/d kappa = %.3f" % (c_an[1], c_an[0], (c_an[0] - c_iso[0]) / 0.5))
h2max = 1.4e-49
print("    => alpha2_eff <= |d c2/d kappa| * kappa_max * <h^2> / (w/c)^2 with kappa_max = 10 (w/c)^2: %.1e (<h^2> <= %.1e, R15-2 out [7]) vs %.0e"
      % (abs((c_an[0] - c_iso[0]) / 0.5) * 10 * h2max, h2max, B_a2))

# ---------------- [9] stochastic metric: timing residuals and perihelion random walk ----------------
print("\n[9] stochastic (zero-mean) noise: timing and perihelion; subtraction: none (variances)")
kpc = 3.0857e19
def shapiro_var(ell, ctau, L=kpc):
    tau = ctau / c
    def inner(om):
        q = max(om / c, 1 / L)
        Ftt = abs((1 - 4j * om * tau) / (1 - 1j * om * tau)**4)**2
        return Ftt * special.exp1(q**2 * ell**2) / (4 * np.pi)
    I = integrate.quad(inner, 0, 50 / tau, limit=400, points=[1 / tau])[0] / (2 * np.pi) * 2   # both signs of omega
    return (4 / c**2) * L * (2 * np.pi * hbar * G / c**4) * c**4 * I / c**4 * c**0
for ell, ctau in [(4e-10, 4e-10), (4e-10, ctau_max), (5e-6, 5e-6)]:
    v = shapiro_var(ell, ctau) * 10      # x10 envelope for the V channel and S-block correlations
    print("    S(+V) channel Shapiro-type delay per pulse, L = 1 kpc, l = %.0e m, c tau = %.1e m: sigma_t = %.1e s (PTA residuals ~1e-7 s, RECALLED)" % (ell, ctau, np.sqrt(v)))
for f in [1e-9, 1 / 3.156e7]:
    k = 2 * np.pi * f / c
    drho = hbar * c / (2 * np.pi**3) * k**4 * (np.log(c * k * tH) + 1)       # eps = 1, |F| = 1 at k << 1/l (upper envelope)
    Om = drho / (rho_crit * c**2); hc = np.sqrt(3 * H0**2 * Om / (2 * np.pi**2 * f**2))
    print("    TT record noise at f = %.1e Hz: Omega_GW = %.1e, h_c = %.1e (NANOGrav 15-yr h_c ~ 2.4e-15 at 1/yr, RECALLED)" % (f, Om, hc))
T10 = 10 * 3.156e7
for name, M, R in [("Earth", 5.97e24, 6.371e6), ("pulsar", 1.4 * Msun, 1.2e4), ("Mercury", 3.30e23, 2.44e6)]:
    Sa = 2 * np.pi * hbar * G / (M * 4 / 3 * np.pi * R**3)          # body-averaged acceleration noise (two-sided, |F| = 1)
    dx = np.sqrt(Sa * T10**3 / 3); print("    %-8s acceleration noise S_a = %.1e m^2 s^-3; 10-yr position walk %.1e m -> timing %.1e s" % (name, Sa, dx, dx / c))
Sa_M = 2 * np.pi * hbar * G / (3.30e23 * 4 / 3 * np.pi * 2.44e6**3); Tcy = 3.156e9
print("    Mercury perihelion random walk over a century: sigma_v/v = %.1e rad (bound %.1e rad/cy)" % (np.sqrt(Sa_M * Tcy) / 4.79e4, 0.003 / 206264.806))

# ---------------- [10] E2-only second-order items ----------------
print("\n[10] E2-only: sink medium, friction on U^2, local sink deposition (subtraction: undamped GR)")
print("    FRW sink rho_s = (gamma/3H) rho_GW <= %.3f rho_GW <= %.3f rho_L in window -> Mercury margin %.1f decades"
      % (gam_max / (3 * H0), gam_max / (3 * H0), np.log10(rho_act_max / (gam_max / (3 * H0) * rho_L))))
Usun = 3 * G * Msun**2 / (5 * Rsun)          # uniform-sphere |U| (order of magnitude; real Sun ~2x)
Gam_sun = 2 * gam_max * Usun / (3 * Msun * c**2); P_dep = Gam_sun * Msun * w_cmb**2
print("    solar self-drag Gamma = %.1e s^-1; power into the sink %.1e W; mass-equivalent over t_H %.1e kg (= %.1e M_sun), spread along a %.1e m path"
      % (Gam_sun, P_dep, P_dep * tH / c**2, P_dep * tH / c**2 / Msun, w_cmb * tH))
print("    friction on the O(G^2) U^2 term: relative gamma w r/(2c^2) at 1 AU = %.1e (beta shift), at R_sun %.1e" % (gam_max * w_cmb * AU / (2 * c**2), gam_max * w_cmb * Rsun / (2 * c**2)))
print("    E1 gain on the U^2 term: 6 (tau_c w / r)^2 at R_sun = %.1e" % (6 * (ctau_max / c * w_cmb / Rsun)**2))
