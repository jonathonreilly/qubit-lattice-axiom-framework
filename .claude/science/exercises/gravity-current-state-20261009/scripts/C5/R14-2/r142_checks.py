"""C5 R14-2 checks: set A, start time (E1) against GW friction (E2) with the self-drag fixed.
Sections
 [1] E2-h self-drag formula: exact quadrature with the full damped propagator vs Gamma = 2 gamma |U|/(3 M c^2)
 [2] double pulsar: per-star E2-h drag rates (uniform, n=1 polytrope, GR binding-energy proxy), mass-weighted Gamma_eff,
     bound on gamma/H0
 [3] orbital mapping by direct integration: linear drag on absolute velocities (unequal Gamma_A, Gamma_B, CM velocity V,
     e = 0.088) and cubic drag |u|^2 u; Pdot_b/P_b vs -3 Gamma_eff and -3 Gamma_3 v_eff^2
 [4] repair of the E2 drag 'the same way': zero-integral (superohmic) friction kernel gamma(w) = g0 w^2/(w^2+wc^2):
     moments, passivity, poles in rest and boosted frames, exact polytrope drag vs speed, orbit-averaged double-pulsar
     bound on wc; friction left in the LIGO band and on near-cone record modes
 [5] the gain's residual drag (P-r13b, shared by E1 and E2) with the CMB velocity included in the orbit average
 [6] near-cone budget on equal terms: E2 single-port factor e^{-g t/2} J0; Var h finite-age (E1) vs stationary damped (E2);
     T_eq = e^{-gamma_E}/gamma; eps tables (strict tau = l/c); tau_c variant thresholds for E1 and E2 (with sink)
 [7] standard sirens at the drag-allowed gamma
Subtractions (TESTS rule): none except where a section prints one (all integrands are positive energies, rates or
spectral densities; the drag is the odd-in-omega part, the even part exerts no force on a symmetric body).
"""
import math
import numpy as np
from scipy import integrate, special
from scipy.integrate import solve_ivp

c = 2.99792458e8; G = 6.67430e-11; hbar = 1.054571817e-34
Ms = 1.98847e30
H0 = 2.2e-18                      # s^-1 (as R12-7: 67.9 km/s/Mpc)
tH = 4.35e17                      # s (as R11-5 / R13-6)
rho_crit = 8.5e-27*c**2           # J/m^3 (RECALLED, as R11-5)
rho_L = 0.69*rho_crit
Mpc = 3.0857e22

# double pulsar (comparators: 1.3e-4 at 95% web-checked abstract arXiv:2112.06795; masses, Pb, PdotGR RECALLED Kramer et al. 2021)
mA, mB = 1.338185*Ms, 1.248868*Ms
Pb = 8834.535                     # s
PdotGR = 1.2478e-12
frac = 1.3e-4
Gam_lim = frac*PdotGR/Pb/3.0      # Pdot_b/P_b = -3 Gamma_eff
Mtot = mA + mB
a_orb = (G*Mtot*Pb**2/(4*math.pi**2))**(1/3)
w_rel = 2*math.pi*a_orb/Pb
wA, wB = mB/Mtot*w_rel, mA/Mtot*w_rel
V_cmb = 3.70e5                    # m/s: solar CMB speed (RECALLED 369.8 km/s); J0737's peculiar velocity wrt the Sun is small (RECALLED)

# ------------------------------------------------------------------ [1]
print("[1] E2-h self-drag: G_gamma = 1/(k^2 - w^2/c^2 - i gamma w/c^2), source moving at v (w = k.v)")
print("    F = -4 pi G int d^3k/(2pi)^3 k Im[k^2 G] |rho~|^2/k^2 ; first order: Gamma = 2 gamma |U|/(3 M c^2)")
# scaled units c = 1, Gaussian body rho~ = M exp(-k^2 a^2/2), a = 1, 4 pi G M -> 1
def drag_exact_gauss(gam, v, a=1.0):
    def inner(k):
        f = lambda mu: (k*mu)*(k*k/(k*k - (k*mu*v)**2 - 1j*gam*(k*mu*v))).imag
        return integrate.quad(f, -1, 1, limit=200)[0]*math.exp(-(k*a)**2)/k**2*k**2
    val = integrate.quad(inner, 0, 10/a, limit=400)[0]/(2*math.pi)**2
    return val/v                  # Gamma / (4 pi G M) in scaled units
for gam, v in [(1e-3, 1e-2), (1e-4, 1e-3), (1e-2, 1e-1)]:
    ex = drag_exact_gauss(gam, v)
    twoU_over_4piGM2 = 1/(2*math.pi**2)*math.sqrt(math.pi)/2      # 2|U|/(4 pi G M^2) = (1/2pi^2) int e^{-k^2} dk
    first = 2*gam*(twoU_over_4piGM2/2)/3                          # 2 gamma |U|/(3 M) per (4 pi G M)
    print(f"    gamma={gam:.0e}, v={v:.0e} (c=1, a=1): exact Gamma = {ex:.6e}, 2 gamma|U|/(3Mc^2) = {first:.6e}, ratio = {ex/first:.6f}")
print("    subtraction: none (odd part of the response only)")

# ------------------------------------------------------------------ [2]
print("\n[2] double pulsar J0737-3039A/B: E2-h drag per star and the bound on gamma")
print(f"    Pb = {Pb} s, |Pdot_GR| = {PdotGR:.4e}, agreement {frac:.1e} (95%) -> Gamma_eff < {Gam_lim:.3e} s^-1")
print(f"    a = {a_orb:.3e} m, relative orbital speed {w_rel/1e3:.0f} km/s (A {wA/1e3:.0f}, B {wB/1e3:.0f} km/s)")
def U_over_Mc2(M, R, model):
    beta = G*M/(R*c*c)
    if model == "uniform":   return 0.6*beta
    if model == "polytrope": return 0.75*beta
    if model == "LP-BE":     return 0.6*beta/(1 - 0.5*beta)   # Lattimer-Prakash binding-energy fit (RECALLED), strong-field proxy
rows = []
for R in [11e3, 12e3, 13e3]:
    for model in ["uniform", "polytrope", "LP-BE"]:
        uA, uB = U_over_Mc2(mA, R, model), U_over_Mc2(mB, R, model)
        gA, gB = 2*uA/3, 2*uB/3           # Gamma_i / gamma
        geff = (gA*mB + gB*mA)/Mtot
        gmax = Gam_lim/geff/H0
        rows.append(gmax)
        print(f"    R={R/1e3:.0f} km, {model:9s}: |U|/Mc^2 A={uA:.4f} B={uB:.4f}; Gamma_A/gamma={gA:.4f}, Gamma_B/gamma={gB:.4f}, Gamma_eff/gamma={geff:.4f}"
              f" -> gamma < {gmax:.4f} H0 ; at gamma=H0: Pdot_b/P_b = {-3*geff*H0:.2e} s^-1 (allowed {3*Gam_lim:.2e})")
print(f"    range over these structure models: gamma_max = {min(rows):.3f} - {max(rows):.3f} H0")
mu2 = mA*mB/Mtot**2
print(f"    companion-field (frame-dipole) term: dPhi_2 = (G m_2 gamma/2c^2)(v_2.rhat) -> orbit-averaged dE/|E| = +2 gamma (m_A m_B/M^2) w_rel^2/c^2 = {2*mu2*(w_rel/c)**2:.2e} gamma"
      f" (anti-drag; vs self-drag 2 Gamma_eff ~ 0.13-0.17 gamma): negligible")
print("    subtraction: none")

# ------------------------------------------------------------------ [3]
print("\n[3] orbital mapping by direct integration (G = 1, a = 1, m_A + m_B = 1; drag on absolute velocities u_i = V + w_i)")
qA, qB = mA/Mtot, mB/Mtot
def run(GA, GB, V, ecc, law, norb=40, G3=None):
    # initial relative orbit at pericentre, CM moving at V
    r0 = (1 - ecc); vrel = math.sqrt((1 + ecc)/(1 - ecc))
    xA = np.array([ qB*r0, 0, 0]); xB = np.array([-qA*r0, 0, 0])
    vA = np.array([0,  qB*vrel, 0]) + V; vB = np.array([0, -qA*vrel, 0]) + V
    def rhs(t, y):
        xa, xb, va, vb = y[0:3], y[3:6], y[6:9], y[9:12]
        d = xb - xa; r = np.linalg.norm(d)
        fa = qB*d/r**3; fb = -qA*d/r**3
        if law == "lin":
            fa = fa - GA*va; fb = fb - GB*vb
        else:
            fa = fa - G3*np.dot(va, va)*va; fb = fb - G3*np.dot(vb, vb)*vb
        return np.concatenate([va, vb, fa, fb])
    def aorb(y):
        xa, xb, va, vb = y[0:3], y[3:6], y[6:9], y[9:12]
        r = np.linalg.norm(xb - xa); vr = va - vb
        E = 0.5*qA*qB*np.dot(vr, vr) - qA*qB/r
        return -qA*qB/(2*E)
    P0 = 2*math.pi
    y0 = np.concatenate([xA, xB, vA, vB])
    sol = solve_ivp(rhs, [0, norb*P0], y0, method="DOP853", rtol=1e-12, atol=1e-14, dense_output=False, t_eval=[0, norb*P0])
    a0, a1 = aorb(sol.y[:, 0]), aorb(sol.y[:, -1])
    return 1.5*(a1 - a0)/a0/(norb*P0)      # Pdot/P
for GA, GB, V, ecc in [(1e-5, 1e-5, [0, 0, 0], 0.0), (1e-5, 1e-5, [0.3, 0.2, 0.1], 0.088), (1.2e-5, 0.8e-5, [0.3, 0.2, 0.1], 0.088)]:
    pp = run(GA, GB, np.array(V, float), ecc, "lin")
    geff = (GA*qB + GB*qA)
    print(f"    linear: Gamma_A={GA:.1e}, Gamma_B={GB:.1e}, V={V}, e={ecc}: Pdot/P = {pp:.4e}; -3 Gamma_eff (mass-weighted) = {-3*geff:.4e}; ratio {pp/(-3*geff):.4f}")
for V, ecc in [([0.0, 0.0, 0.0], 0.0), ([0.8, 0.0, 0.0], 0.0), ([0.0, 0.0, 0.8], 0.0), ([0.8, 0.0, 0.0], 0.088)]:
    G3 = 1e-5
    pp = run(None, None, np.array(V, float), ecc, "cub", G3=G3)
    Vv = np.array(V); Vpar2 = Vv[0]**2 + Vv[1]**2
    # prediction for circular orbits: Gamma_eq = G3 * sum m_i w_i^2 (V^2 + V_par^2 + w_i^2) / sum m_i w_i^2
    w_a, w_b = qB*1.0, qA*1.0
    num = qA*w_a**2*(Vv@Vv + Vpar2 + w_a**2) + qB*w_b**2*(Vv@Vv + Vpar2 + w_b**2)
    den = qA*w_a**2 + qB*w_b**2
    print(f"    cubic F = -m G3 |u|^2 u, V={V}, e={ecc}: Pdot/P = {pp:.4e}; -3 G3 <V^2+V_par^2+w^2>_m = {-3*G3*num/den:.4e}; ratio {pp/(-3*G3*num/den):.4f}")
print("    => Pdot_b/P_b = -3 Gamma_eff for linear drag (any V, small e; unequal Gamma mass-weighted);"
      " cubic drag: Gamma_eq = Gamma_3 (V^2 + V_par^2 + w^2): the CMB velocity enters")

# ------------------------------------------------------------------ [4]
print("\n[4] repair 'the same way': friction memory kernel with zero integral, K(t) = g0[delta(t) - wc e^{-wc t}] theta(t)")
print("    gamma(w) = int K e^{iwt} dt = g0 (-i w)/(wc - i w);  Re gamma = g0 w^2/(w^2 + wc^2) >= 0 (passive); gamma(0) = 0")
wc_ = 2.0
Kint = 1.0 - integrate.quad(lambda t: wc_*math.exp(-wc_*t), 0, 50)[0]
print(f"    zeroth moment of K (wc=2): {Kint:.1e}; min Re gamma over w in [-1e3,1e3]: "
      f"{min((1*(-1j*w)/(wc_-1j*w)).real for w in np.linspace(-1e3,1e3,20001)):.1e}")
# poles of D(w,k) = (k^2 - w^2 - i w gamma(w)) (wc - i w) in the rest frame (c = 1)
def roots_rest(k, g0, wc):
    # (k^2 - w^2)(wc - i w) - i w * g0 (-i w) = (k^2 - w^2)(wc - i w) - g0 w^2
    # = i w^3 - (wc + g0) w^2 - i k^2 w + k^2 wc
    return np.roots([1j, -(wc + g0), -1j*k*k, k*k*wc])
mx = -1e9
for g0 in [1e-3, 1e-1, 10.0]:
    for wc in [1e-2, 1.0, 1e2]:
        for k in np.logspace(-4, 4, 81):
            mx = max(mx, max(r.imag for r in roots_rest(k, g0, wc)))
print(f"    rest frame: max Im w over k in [1e-4,1e4], g0 in {{1e-3,0.1,10}}, wc in {{1e-2,1,1e2}}: {mx:.2e} (<= 0: no growth)")
rng = np.random.default_rng(1402)
mxb = -1e9
for _ in range(6000):
    beta = rng.uniform(0, 0.999); Gm = 1/math.sqrt(1 - beta*beta)
    kp = rng.normal(size=3)*10**rng.uniform(-3, 3)
    g0 = 10**rng.uniform(-3, 1); wc = 10**rng.uniform(-2, 2)
    # rest-frame w = Gm (w' + beta k'_x), k_x = Gm (k'_x + beta w'), k_perp = k'_perp ; s = k^2 - w^2 = k'^2 - w'^2
    # (k'^2 - w'^2)(wc - i w) - g0 w^2 = 0, with w = Gm(w' + beta kx'): cubic in w'
    kk = kp@kp; A = Gm; B = Gm*beta*kp[0]
    # (kk - w'^2)(wc - i(A w' + B)) - g0 (A w' + B)^2
    p1 = np.array([-1.0, 0.0, kk])                 # kk - w'^2
    p2 = np.array([-1j*A, wc - 1j*B])               # wc - i(A w' + B)
    p3 = g0*np.array([A*A, 2*A*B, B*B])
    poly = np.polysub(np.polymul(p1, p2), p3)
    mxb = max(mxb, max(r.imag for r in np.roots(poly)))
print(f"    boosted frames (6000 random beta<0.999, k', g0, wc): max Im w' = {mxb:.2e} (<= 0 within rounding: no growing mode)")

# exact drag for an n=1 polytrope moving at speed u, first order in gamma (w^2/c^2 << k^2 at these speeds)
def rho_t(k, M, R):
    x = k*R
    return np.where(x < 1e-6, M, M*math.pi**2*np.sin(x)/(x*(math.pi**2 - x*x) + 1e-300))
def rho_t_safe(k, M, R):
    x = np.asarray(k*R, float)
    out = np.empty_like(x)
    near = np.abs(x - math.pi) < 1e-6
    small = x < 1e-8
    reg = ~(near | small)
    out[reg] = M*math.pi**2*np.sin(x[reg])/(x[reg]*(math.pi**2 - x[reg]**2))
    out[near] = M*math.pi**2*(-1.0)/(math.pi*(-2*math.pi))      # limit sin(x)/(pi^2-x^2) -> 1/(2 pi) at x = pi
    out[small] = M
    return out
def Gamma_of_u(u, M, R, g0, wc):
    # Gamma(u) = (4 pi G/(M c^2)) (1/4pi^2) int dk |rho~|^2 int dmu mu^2 Re gamma(k u mu)/g0 * g0
    ks = np.logspace(math.log10(1e-4/R), math.log10(400/R), 6000)
    if wc == 0:
        inner = np.full_like(ks, 2/3)
    else:
        a = ks*u/wc
        inner = np.where(a < 1e-3, 2*a*a/5, 2*(1/3 - (1 - np.arctan(a)/np.maximum(a, 1e-300))/np.maximum(a*a, 1e-300)))
    integrand = rho_t_safe(ks, M, R)**2*inner
    val = np.trapezoid(integrand*ks, np.log(ks))
    return 4*math.pi*G/(M*c*c)/(4*math.pi**2)*val*g0
R = 12e3
ohm = Gamma_of_u(3e5, mA, R, 1.0, 0)
print(f"    check: ohmic polytrope Gamma/gamma (quadrature) = {ohm:.5f}; 2|U|/(3Mc^2) with |U| = 3GM^2/(4R): {2*0.75*G*mA/(R*c*c)/3:.5f}")
def Gamma_eq_orbit(Gfun_A, Gfun_B, V, inplane=True, nphi=720):
    # circular relative orbit in the x-y plane; V in plane (along x) or normal (z); Gamma_eq = sum m <Gamma(|u|) u.w> / sum m w^2
    Vv = np.array([V, 0, 0]) if inplane else np.array([0, 0, V])
    num = 0.0; den = mA*wA**2 + mB*wB**2
    for ph in np.linspace(0, 2*math.pi, nphi, endpoint=False):
        e = np.array([-math.sin(ph), math.cos(ph), 0])
        for m, w, Gf, sgn in [(mA, wA, Gfun_A, 1), (mB, wB, Gfun_B, -1)]:
            wv = sgn*w*e; u = Vv + wv; un = np.linalg.norm(u)
            num += m*Gf(un)*(u@wv)/nphi
    return num/den
print("    double pulsar, n=1 polytropes R = 12 km, V_CMB = 370 km/s in the orbital plane (worst case):")
for wc in [0, 30.0, 100.0, 300.0, 1e3, 3e3]:
    GA_ = lambda u, wc=wc: Gamma_of_u(u, mA, R, H0, wc)
    GB_ = lambda u, wc=wc: Gamma_of_u(u, mB, R, H0, wc)
    us = np.linspace(1e3, 1.2e6, 120)
    tabA = np.array([GA_(u) for u in us]); tabB = np.array([GB_(u) for u in us])
    fA = lambda u: np.interp(u, us, tabA); fB = lambda u: np.interp(u, us, tabB)
    ge = Gamma_eq_orbit(fA, fB, V_cmb, True, 360)
    ge_n = Gamma_eq_orbit(fA, fB, V_cmb, False, 360)
    print(f"      wc = {wc:7.0f} rad/s: Gamma_eq(g0 = H0) = {ge:.2e} s^-1 (V normal to plane {ge_n:.2e}); bound {Gam_lim:.2e} -> g0 < {Gam_lim/ge*H0/H0:.3g} H0")
fl = lambda f, wc: (2*math.pi*f)**2/((2*math.pi*f)**2 + wc**2)
for wc in [300.0, 1e3]:
    print(f"    wc = {wc:.0f}: friction left in the LIGO band gamma(w)/g0 = {fl(20, wc):.3f} (20 Hz), {fl(100, wc):.3f} (100 Hz), {fl(1000, wc):.3f} (1 kHz);"
          f" on near-cone record modes w = c/l >= 6e13 rad/s: 1 - gamma/g0 <= {(wc/6e13)**2:.0e}")
print("    subtraction: none")

# ------------------------------------------------------------------ [5]
print("\n[5] the gain's residual drag after P-r13b (shared by E1 and E2): cubic term, orbit-averaged with the CMB velocity")
def grad2_int(M, R):
    rr = np.linspace(1e-6, R, 200001)
    shape = np.sin(np.pi*rr/R)/(np.pi*rr/R)
    rhoc = M/np.trapezoid(4*np.pi*rr**2*shape, rr)
    drho = np.gradient(rhoc*shape, rr)
    return np.trapezoid(4*np.pi*rr**2*drho**2, rr)
c3 = 20.0
IA, IB = grad2_int(mA, R), grad2_int(mB, R)
def G3_of(tau, M, I1):   # Gamma(u) = G3 u^2 with G3 = (4 pi G/M) c3 tau^3 I1/5
    return 4*math.pi*G/M*c3*tau**3*I1/5
for tau, lab in [(5e-6/c, "strict tau = l/c, l = 5e-6 m"), (7.9e-12, "R13-6's tau_c ceiling 7.9e-12 s (v = 300 km/s)")]:
    gA3, gB3 = G3_of(tau, mA, IA), G3_of(tau, mB, IB)
    ge = Gamma_eq_orbit(lambda u: gA3*u*u, lambda u: gB3*u*u, V_cmb, True)
    ge0 = Gamma_eq_orbit(lambda u: gA3*u*u, lambda u: gB3*u*u, 0.0, True)
    print(f"    {lab}: Gamma_eq = {ge:.2e} s^-1 with V_CMB in plane ({ge0:.2e} with V = 0); bound {Gam_lim:.2e}")
# tau_c ceiling with the CMB velocity
gA1, gB1 = G3_of(1.0, mA, IA), G3_of(1.0, mB, IB)
ge1 = Gamma_eq_orbit(lambda u: gA1*u*u, lambda u: gB1*u*u, V_cmb, True)
ge1n = Gamma_eq_orbit(lambda u: gA1*u*u, lambda u: gB1*u*u, V_cmb, False)
tmax = (Gam_lim/ge1)**(1/3); tmaxn = (Gam_lim/ge1n)**(1/3)
print(f"    tau_c ceiling (first moment zero, n = 4, smooth polytropes): tau_c < {tmax:.2e} s (c tau_c < {c*tmax:.2e} m), V in plane;"
      f" {tmaxn:.2e} s (c tau_c < {c*tmaxn:.2e} m), V normal; R13-6 quoted 7.9e-12 s (2.4e-3 m) at v = 300 km/s without the CM term")
print("    subtraction: none")

# ------------------------------------------------------------------ [6]
print("\n[6] near-cone record budget on equal terms")
print("    (a) E2 single-port causal factor: H_g(w) = (W^2 - w^2 - i g w)^(-1/2) <-> theta(t) e^{-g t/2} J0(W' t), W' = sqrt(W^2 - g^2/4)")
W, g = 1.0, 0.1
Wp = math.sqrt(W*W - g*g/4)
for w in [0.3, 0.97, 1.0, 1.5]:
    p = -1j*w + 1e-12
    num = integrate.quad(lambda t: (math.exp(-g*t/2)*special.j0(Wp*t)*np.exp(-p*t)).real, 0, 600, limit=4000)[0] \
        + 1j*integrate.quad(lambda t: (math.exp(-g*t/2)*special.j0(Wp*t)*np.exp(-p*t)).imag, 0, 600, limit=4000)[0]
    ex = (W*W - w*w - 1j*g*w)**-0.5
    ex = ex if ex.real >= 0 else -ex
    print(f"      w={w}: Laplace of e^(-gt/2)J0 = {num:.6f}; (W^2-w^2-igw)^(-1/2) = {ex:.6f}")
r = np.roots([-1, -1j*g, W*W])
print(f"      branch points (zeros of W^2 - w^2 - i g w): {r[0]:.4f}, {r[1]:.4f} (both Im < 0: H_g and 1/H_g analytic in the UHP, outer)")
print("    (b) Var h per mode (W = 1): E1 finite age 1/2 int_0^T J0^2 vs E2 stationary 1/2 int_0^inf e^{-g t} J0(W' t)^2 dt")
def var_E1(T):
    pts = np.linspace(0, T, int(T/5) + 2)
    return 0.5*sum(integrate.quad(lambda t: special.j0(t)**2, a, b, limit=50)[0] for a, b in zip(pts[:-1], pts[1:]))
def var_E2(gg):
    Wp_ = math.sqrt(1 - gg*gg/4)
    Tm = 40/gg
    pts = np.linspace(0, Tm, int(Tm/5) + 2)
    return 0.5*sum(integrate.quad(lambda t: math.exp(-gg*t)*special.j0(Wp_*t)**2, a, b, limit=50)[0] for a, b in zip(pts[:-1], pts[1:]))
for gg in [1e-2, 1e-3, 3e-4]:
    v2 = var_E2(gg); Teq = math.exp(-np.euler_gamma)/gg
    v1 = var_E1(Teq)
    print(f"      g = {gg:.0e}: E2 Var h = {v2:.6f}; E1 Var h at T_eq = e^(-gamma_E)/g = {Teq:.4g}: {v1:.6f}; asymptote ln(8/g)/(2pi) = {math.log(8/gg)/(2*math.pi):.6f}")
print("      => same log slope; E2 at friction g carries E1's record content at age T_eq = 0.561/g (subtraction: none)")
print("    (c) strict tau = l/c, eps needed for rho_GW (+ sink) < rho_L, R11-5 normalization (O(1) tensor weights, Isaacson; suggested)")
print("        E1: L = ln(eps c t_H/l); E2 (stationary, history >> 1/gamma): L = ln(eps c T_eq/l), T_eq = 0.561/gamma, times (1 + gamma/3H0)")
def eps_need(l, T, sink):
    eps = 1.0
    for _ in range(60):
        L = math.log(max(eps, 1e-300)*c*T/l)
        eps = rho_L*math.pi**3*l**4/(L*hbar*c*sink)
    return eps, L
print("        l [m]   | E1 (t_H)          | E2 gamma=0.03 H0  | E2 gamma=0.045 H0 | E2 gamma=H0 (drag-excluded unless repaired) | E2 R12-7 form ln(2c/(l H0))")
for l in [1e-8, 2e-7, 1e-6, 5e-6]:
    e1 = eps_need(l, tH, 1.0)
    outs = []
    for gH in [0.03, 0.045, 1.0, 7.0]:
        gm = gH*H0
        outs.append(eps_need(l, math.exp(-np.euler_gamma)/gm, 1 + gH/3))
    Lg = math.log(2*c/l/H0); er = rho_L*math.pi**3*l**4/(Lg*hbar*c*(4/3))
    print(f"        {l:.0e} | {e1[0]:.2e} (L={e1[1]:.1f}) | {outs[0][0]:.2e} (L={outs[0][1]:.1f}) | {outs[1][0]:.2e} (L={outs[1][1]:.1f}) | {outs[2][0]:.2e} (L={outs[2][1]:.1f})"
              f"                    | {er:.1e} (L={Lg:.1f}) | E2 superohmic g0=7 H0 (wc=1e3): {outs[3][0]:.2e} (L={outs[3][1]:.1f})")
print("    (d) tau_c variant (eps = 1, gain (1 - 4ix)(1 - ix)^-4, x = w tau_c): rho_log with ln(c k T); E2: T = T_eq and sink factor")
n = 4
Ft2 = lambda x: (1 + n*n*x*x)/(1 + x*x)**n
def rho_log(l, ctc, T):
    f = lambda lk: (lambda k: k**4*math.exp(-(k*l)**2)*Ft2(k*ctc)*max(math.log(c*k*T), 0.0))(math.exp(lk))
    v = integrate.quad(f, math.log(1e-6/ctc), math.log(30/l), limit=400)[0]
    return hbar*c/math.pi**3*2*v
def rho_qs(l, ctc, xmax=0.5):
    def inner(k):
        a = k*ctc
        gfun = lambda ly: (lambda y: y**3/(1-(y/a)**2)*Ft2(y))(math.exp(ly))
        return a**-3*integrate.quad(gfun, math.log(1e-8), math.log(xmax*a), limit=400)[0]
    f = lambda lk: (lambda k: k**4*math.exp(-(k*l)**2)*inner(k))(math.exp(lk))
    v = integrate.quad(f, math.log(1e-6/ctc), math.log(30/l), limit=200)[0]
    return hbar*c/math.pi**3*2*v
def solve(fun, lo, hi):
    for _ in range(60):
        mid = math.sqrt(lo*hi)
        if fun(mid) > rho_L: lo = mid
        else: hi = mid
    return hi
for l in [4e-10, 1e-8, 1e-6, 5e-6]:
    t1 = solve(lambda x: rho_log(l, x, tH) + rho_qs(l, x), 20*l, 1e4)
    res = [f"E1: c tau_c > {t1:.2e} m"]
    for gH in [0.03, 1.0, 7.0]:
        gm = gH*H0; Teq = math.exp(-np.euler_gamma)/gm
        t2 = solve(lambda x: (rho_log(l, x, Teq) + rho_qs(l, x))*(1 + gH/3), 20*l, 1e4)
        res.append(f"E2 gamma={gH} H0: c tau_c > {t2:.2e} m")
    print(f"      l = {l:.0e} m: " + "; ".join(res) + f"; drag ceiling (section [5], V in plane) c tau_c < {c*tmax:.2e} m")
print("    subtraction: none (positive energy densities)")

# ------------------------------------------------------------------ [7]
print("\n[7] standard sirens at the drag-allowed gamma: d_L^GW/d_L^EM = exp(gamma t_lb/2)")
Om_m = 0.31
def t_lb(z):
    f = lambda zz: 1.0/((1 + zz)*math.sqrt(Om_m*(1 + zz)**3 + 1 - Om_m))
    return integrate.quad(f, 0, z)[0]/H0
for gH in [0.03, 0.045]:
    print(f"    gamma = {gH} H0: " + "; ".join(f"z={z}: {math.exp(gH*H0*t_lb(z)/2):.4f}" for z in [0.0098, 0.1, 0.5, 1.0, 20.0])
          + f"; Lu et al. beta = gamma/c = {gH*H0/(c/Mpc):.1e} Mpc^-1 (bound 6.75e-4, fixed-distance benchmark)")
print(f"    damping time 2/gamma at 0.03 H0 = {2/(0.03*H0)/tH:.0f} t_H; record-content equivalence age T_eq = {math.exp(-np.euler_gamma)/(0.03*H0)/tH:.1f} t_H")
print("    subtraction: none")

# ------------------------------------------------------------------ [6e] (appended)
print("\n[6e] E2 stationary content with the eps profile e(s) = (s^2 + eps^2)/(s^2 + eps) (R13-6 [2], delta = sqrt(eps)), near cone, W = 1")
print("     Var_E2(g) = (1/4pi) int_{-S}^{S} e(s) ds / sqrt(s^2 + g^2)  (s = W^2 - w^2 ~ 2(W - w)); secular part = coefficient of ln(1/g)")
def var_e2(gg, eps, S=1.0):
    f = lambda s: ((s*s + eps*eps)/(s*s + eps))/math.sqrt(s*s + gg*gg)
    pts = sorted(set([0.0, gg, eps*eps, eps, math.sqrt(eps), S]))
    pts = [p for p in pts if p <= S]
    return 2*sum(integrate.quad(f, a, b, limit=400)[0] for a, b in zip(pts[:-1], pts[1:]))/(4*math.pi)
for eps in [1e-2, 1e-3]:
    vals = [(gg, var_e2(gg, eps)) for gg in [1e-6, 1e-7, 1e-8, 1e-9]]
    slope = (vals[-1][1] - vals[0][1])/math.log(1e3)
    # decomposition: secular eps*ln(eps/g)/(2pi) + forced remainder
    rem = [v - eps*math.log(eps/gg)/(2*math.pi) for gg, v in vals]
    rem_nolog = [v - eps*math.log(1/gg)/(2*math.pi) for gg, v in vals]
    print(f"     eps={eps:.0e}: Var(g=1e-6..1e-9) = " + ", ".join(f"{v:.6f}" for _, v in vals) + f"; d Var/d ln(1/g) = {slope:.3e} (eps/2pi = {eps/(2*math.pi):.3e})")
    print(f"       remainder after eps ln(eps/g)/2pi: " + ", ".join(f"{r:.5f}" for r in rem) + f"  (forced part ~ ln(1/eps)/(4pi) = {math.log(1/eps)/(4*math.pi):.5f})")
print("     => secular slope eps/(2pi) per ln(1/g), the same coefficient as E1 per ln T; the constant equals the forced part ln(1/eps)/(4pi) to O(eps ln eps),"
      " so whether eps sits inside the log is a convention at that order; the forced part is the same in E1 and E2. subtraction: none")

# ------------------------------------------------------------------ [6f] (appended)
print("\n[6f] where the tau_c window closes once the CMB velocity is in the orbit average (E1; E2 at 0.03 H0 differs by < 1%)")
for l in [1e-9, 2e-9, 3e-9, 5e-9]:
    t1 = solve(lambda x: rho_log(l, x, tH) + rho_qs(l, x), 20*l, 1e4)
    print(f"      l = {l:.0e} m: lower end c tau_c > {t1:.2e} m vs drag ceiling {c*tmax:.2e} m (V in plane) / {c*tmaxn:.2e} m (V normal): {'open' if t1 < c*tmax else ('open only if V normal' if t1 < c*tmaxn else 'closed')}")
print("    subtraction: none")
