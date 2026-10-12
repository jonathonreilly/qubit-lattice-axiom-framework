#!/usr/bin/env python3
"""C5 R12-7 checks: route E2, classical metric records with frame friction on GWs, G = g/(s + i gamma w).

Units: c = 1 inside dimensionless sections; SI where stated.  s = w^2 - k^2 (frame), retarded G_g = 1/(k^2 - w^2 - i g w).
Sections
 [1] causality: poles in the lower half w-plane for every real k; position-space kernel (telegraph) support,
     static limit int G dt = 1/(4 pi r); boosted-frame stability (Im w' <= 0) for boosts up to 0.999
 [2] c_T: phase/group/front velocity; GW170817 lag; gamma_max from c_T
 [3] binary pulsar: radiated power at the source with damped G, exact integral, relative change vs gamma/Omega
 [4] standard sirens: d_L^GW/d_L^EM = exp(gamma t_lb(z)/2); Lu et al. beta = gamma/c; GW170817 EM distance; Xi_0 map
 [5] static limit and moving sources: exact Newton at w=0; frame-dipole term if friction acted on the scalar sector;
     TT-only order; PPN-alpha comparison numbers; self-drag (scalar-sector friction) for Sun / neutron star
 [6] explicit causal meter bank per frame mode: Lorentzian QND elements (Gamma_i log-spaced, lambda_i ~ Gamma_i^1/2),
     each record filtered by its own causal Lorentzian; excess factor X(u) = P D/(|F|^2/4); profiles; both finite with G_g
 [7] two-tone element stationarity (time-domain Monte Carlo of the classical record-noise part)
 [8] Lamb-string sink: classical field mode attached to a semi-infinite string: exact Ohmic friction, energy bookkeeping
 [9] sink and cosmology: Hawking-fluid mean free path for rho <= rho_crit; Ohmic-bath steady state in FRW;
     stationary near-cone record content with L_g = ln(2w/g) (R11-5 formula) -> epsilon needed
Subtraction: none in every section (positive integrands/spectral densities), except [5] (rest-frame static kernel).
"""
import math
import numpy as np
from scipy import integrate, special

rng = np.random.default_rng(20261012)
c = 2.99792458e8; G = 6.67430e-11; hbar = 1.054571817e-34
Mpc = 3.0857e22; H0 = 2.2e-18          # s^-1 (as R12-4; 67.9 km/s/Mpc)
Gyr = 3.156e16
c_over_Mpc = c / Mpc

# ------------------------------------------------------------------ [1]
print("[1] causality and stability of the damped TT propagator 1/(k^2 - w^2 - i g w)")
worst_im = -np.inf
for g in [1e-3, 1.0, 10.0]:
    for k in np.concatenate([np.logspace(-6, 3, 400), [g / 2]]):
        roots = np.roots([1.0, 1j * g, -k * k])     # w^2 + i g w - k^2 = 0
        worst_im = max(worst_im, roots.imag.max())
print(f"    max Im(w) over poles, k in [1e-6,1e3], g in {{1e-3,1,10}}: {worst_im:.3e} (<= 0: analytic in upper half-plane -> retarded/causal)")
# position space: G(t,r) = e^{-gt/2}[delta(t-r)/(4 pi r) + theta(t-r) (g/2) I1(g tau/2)/(4 pi tau)], tau = sqrt(t^2-r^2)
g = 1.0
for r in [0.1, 1.0, 5.0]:
    def f(t, r=r):
        x = g * math.sqrt(max(t * t - r * r, 0.0)) / 2
        ratio = 0.5 if x < 1e-8 else special.i1e(x) / x          # I1(x)/x with I1 = i1e * e^x
        return math.exp(-g * t / 2 + x) * (g * g / 4) * ratio / (4 * math.pi)
    tail = integrate.quad(f, r, r + 50, limit=400)[0] + integrate.quad(f, r + 50, r + 5e5, limit=2000)[0]
    delta_part = math.exp(-g * r / 2) / (4 * math.pi * r)
    print(f"    r={r}: int_0^inf G dt = delta part {delta_part:.6f} + tail {tail:.6f} = {delta_part+tail:.6f} ; 1/(4 pi r) = {1/(4*math.pi*r):.6f}")
# direct check that the kernel solves the damped equation: compare with numerical inverse transform at one (t,r)
def G_num(t, r, g, K=4000.0, n=400001):
    # G(t,r) = (1/(2 pi^2 r)) int_0^inf k sin(kr) e^{-gt/2} sin(sqrt(k^2-g^2/4) t)/sqrt(k^2-g^2/4) dk   (retarded, smooth part only checked away from cone)
    k = np.linspace(1e-9, K, n)
    om = np.sqrt((k * k - g * g / 4).astype(complex))     # overdamped modes k < g/2 included (sin(i x)/(i) = sinh)
    integrand = (k * np.sin(k * r) * np.exp(-g * t / 2) * (np.sin(om * t) / om).real) * np.exp(-(k / K) ** 2 * 50)
    return np.trapezoid(integrand, k) / (2 * math.pi ** 2 * r)
for (t, r) in [(0.5, 1.0), (3.0, 1.0), (6.0, 2.0)]:
    tau2 = t * t - r * r
    an = 0.0 if tau2 <= 0 else math.exp(-g * t / 2) * (g / 2) * special.i1(g * math.sqrt(tau2) / 2) / (4 * math.pi * math.sqrt(tau2))
    print(f"    (t,r)=({t},{r}): inverse-transform G = {G_num(t, r, g):+.5f}  analytic tail = {an:+.5f}  ({'outside' if tau2<=0 else 'inside'} the cone)")
# boosted frames: dispersion in rest frame w^2 + i g w - |k|^2 = 0, with w = Gb(w' + v k'_x), k_x = Gb(k'_x + v w')
worst = -np.inf
for v in [0.1, 0.5, 0.9, 0.999]:
    Gb = 1 / math.sqrt(1 - v * v)
    for _ in range(4000):
        kp = rng.normal(size=3) * 10 ** rng.uniform(-4, 3)
        kpx, kperp2 = kp[0], kp[1] ** 2 + kp[2] ** 2
        # (Gb(w'+v kx'))^2 + i g Gb (w' + v kx') - Gb^2 (kx' + v w')^2 - kperp2 = 0 -> quadratic in w'
        a2 = Gb ** 2 * (1 - v * v)
        a1 = Gb ** 2 * (2 * v * kpx - 2 * v * kpx) + 1j * g * Gb
        a0 = Gb ** 2 * (v * v * kpx ** 2 - kpx ** 2) + 1j * g * Gb * v * kpx - kperp2
        roots = np.roots([a2, a1, a0])
        worst = max(worst, roots.imag.max())
print(f"    boosted frames v up to 0.999, 16000 random real k': max Im(w') = {worst:.3e} (<= 0: no growing mode in any frame)")

# ------------------------------------------------------------------ [2]
print("\n[2] c_T: dispersion w^2 + i g w = c^2 k^2 for real w")
D170817 = 40 * Mpc
for gam in [H0, 3 * H0, 60 * H0]:
    w = 2 * math.pi * 100
    kk = (w / c) * np.sqrt(1 + 1j * gam / w)
    vph = w / kk.real
    dw = 1e-6 * w
    k2 = ((w + dw) / c) * np.sqrt(1 + 1j * gam / (w + dw))
    vg = dw / (k2.real - kk.real)
    print(f"    gamma={gam/H0:5.1f} H0, 100 Hz: (v_ph-c)/c = -g^2/8w^2 = {-gam**2/(8*w*w):+.2e}; (v_g-c)/c = +{gam**2/(8*w*w):.2e} (analytic; below double precision numerically); front velocity = c")
w = 2 * math.pi * 100
print(f"    GW170817 lag over 40 Mpc at gamma=H0: {D170817/c*H0**2/(8*w*w):.1e} s vs 1.74 s; |dv/c| bound 3e-15 -> gamma_max(c_T) = {math.sqrt(8*3e-15)*w:.2e} s^-1 = {math.sqrt(8*3e-15)*w/H0:.1e} H0")

# ------------------------------------------------------------------ [3]
print("\n[3] radiated power at the source: P(g)/P(0) = int k^2 dk A(k) ImG(Om,k) / (pi Om A(Om)/2), A = exp(-k^2 a^2)")
def power_ratio(gam_over_Om, aOm):
    Om = 1.0; gg = gam_over_Om
    W = min(1e3 * gg * Om, 0.5 * Om * Om)
    def fu(u):
        k = math.sqrt(Om * Om + u)
        return 0.5 * k * math.exp(-(k * aOm) ** 2) * gg * Om / (u * u + (gg * Om) ** 2)
    def fth(th):
        u = gg * Om * math.tan(th)
        k = math.sqrt(Om * Om + u)
        return 0.5 * k * math.exp(-(k * aOm) ** 2)
    th = math.atan(W / (gg * Om))
    val = integrate.quad(fth, -th, th, limit=800)[0]
    val += integrate.quad(fu, -Om * Om, -W, limit=800)[0]
    val += integrate.quad(fu, W, 10 / aOm ** 2, limit=2000, points=[1.0, 10.0, 100.0])[0]
    return val / (math.pi * Om * math.exp(-aOm ** 2) / 2)
for gr in [1e-1, 1e-2, 1e-4, 1e-6]:
    for aOm in [1e-3, 1e-1]:
        r = power_ratio(gr, aOm)
        print(f"    g/Om={gr:.0e}, a*Om={aOm:.0e}: P(g)/P(0) - 1 = {r-1:+.3e}")
const_check = [(gr, (1/2)*math.sqrt(1+math.sqrt(1+gr*gr))/math.sqrt(2) ) for gr in [1e-1, 1e-2]]
for gr, rez in const_check:
    print(f"    constant A: exact (pi/2) Re sqrt(Om^2 + i g Om) -> ratio = {2*rez:.10f} at g/Om={gr:.0e} (1 + g^2/8Om^2 = {1+gr*gr/8:.10f})")
for name, Pb, tol in [("Hulse-Taylor B1913+16", 27906.98, 1.6e-3), ("double pulsar J0737-3039", 8834.53, 1.3e-4)]:
    Om_gw = 2 * 2 * math.pi / Pb
    print(f"    {name}: Omega_GW = {Om_gw:.3e} s^-1; gamma/Omega at gamma=H0 = {H0/Om_gw:.1e}; fractional power change <~ (gamma/Omega) = {H0/Om_gw:.1e} vs test precision {tol:.1e}")

# ------------------------------------------------------------------ [4]
print("\n[4] standard sirens: amplitude ~ e^{-gamma t_prop/2}; d_L^GW = d_L^EM exp(gamma t_lb(z)/2) (friction in cosmic time)")
H0kms = H0 * Mpc / 1e3
Om_m = 0.31
def t_lb(z):
    f = lambda zz: 1.0 / ((1 + zz) * math.sqrt(Om_m * (1 + zz) ** 3 + 1 - Om_m))
    return integrate.quad(f, 0, z)[0] / H0
print(f"    H0 = {H0kms:.1f} km/s/Mpc; Lu et al. beta (energy rate, h ~ e^(-beta D/2)) = gamma/c: at gamma=H0 beta = {H0/c_over_Mpc:.2e} Mpc^-1 vs 95% bound 6.75e-4 -> gamma_max = {6.75e-4*c_over_Mpc/H0:.2f} H0")
print(f"    GW170817-only bound (Lu et al. Table I) beta < 1.408e-2 Mpc^-1 -> gamma_max = {1.408e-2*c_over_Mpc/H0:.0f} H0")
for gam_H in [1.0, 3.0]:
    gam = gam_H * H0
    row = []
    for z in [0.0098, 0.1, 0.3, 0.5, 1.0, 3.0, 20.0]:
        row.append(f"z={z}: {math.exp(gam*t_lb(z)/2):.4f}")
    print(f"    gamma={gam_H} H0: d_L^GW/d_L^EM  " + "; ".join(row))
print("    comparator: GWTC-3 dark sirens Xi_0 = 1.2 +- 0.7 (flat prior, 68%; Mancarella et al., web snippet); Xi_0 ~ ratio at z>>1")

# ------------------------------------------------------------------ [5]
print("\n[5] static limit and moving sources")
print("    G(w=0,k) = 1/k^2 exactly for every gamma (friction term ~ w): Newtonian static limit unchanged [exact]")
for name, r, wv in [("1 AU, w=370 km/s", 1.496e11, 3.7e5), ("binary-pulsar orbit 1e9 m", 1e9, 3.7e5), ("Galaxy 10 kpc, 300 km/s", 3.086e20, 3e5)]:
    eps_s = H0 * wv * r / (2 * c * c)
    print(f"    {name}: IF friction acted on the scalar potential, frame-dipole correction gamma w r/(2c^2) = {eps_s:.1e} (gamma=H0)")
w_cmb = 369.82e3
print(f"    TT-only friction (E2 as specified): moving-source TT field is O(w^2/c^2) = {(w_cmb/c)**2:.1e} of U; friction alters it by gamma w r/c^2:")
print(f"      effective PPN-type term at 1 AU ~ {(w_cmb/c)**2*H0*w_cmb*1.496e11/c**2:.1e} U  vs alpha_2-type bound 1.6e-9 x (w/c)^2 = {1.6e-9*(w_cmb/c)**2:.1e} U")
for name, Uratio in [("Sun", 0.6 * 2.12e-6), ("neutron star", 0.15)]:
    rate = 2 * H0 * Uratio / 3
    print(f"    scalar-sector friction would give self-drag rate (2 gamma |U|/3Mc^2) for {name}: {rate:.1e} s^-1 (dv/v over t_H = {rate*4.35e17:.1e}); TT-only: O((w/c)^4) smaller")

# ------------------------------------------------------------------ [6]
print("\n[6] explicit causal near-cone meter bank, one frame mode (u = w - c|k| in units of the band edge delta = 1)")
# identity check
for x in [1e-6, 1e-2, 1.0, 1e2]:
    val = integrate.quad(lambda y: math.exp(0.5 * y) / (x + math.exp(y)), -80, 80, limit=800)[0] / math.pi
    print(f"    synthesis identity: (1/pi) int t^-1/2/(x+t) dt = {val:.6f} vs 1/sqrt(x) = {x**-0.5:.6f}")
b = 1e-8                          # plays the role of gamma*w/(2c|k|) (relative linewidth floor)
Gam = np.logspace(math.log10(2 * b), 0, 8 * 8 + 1)     # 8 per decade, 2b .. 1
lam = np.sqrt(Gam)                # element strength ~ Gamma^1/2 (positive synthesis weights)
cw = lam.copy()                   # each record filtered by its own causal Lorentzian, weight c_i = lam_i
us = np.concatenate([-np.logspace(-10, 0.5, 300)[::-1], np.logspace(-10, 0.5, 300)])
X = []; Pe = []; Dv = []
for u in us:
    chi = 1.0 / (Gam / 2 - 1j * u)                     # causal Lorentzian response of element i
    F = np.sum(cw * lam * chi ** 2)                     # total gain (record filtered by chi again)
    P = np.sum(cw ** 2 * np.abs(chi) ** 2) / 2          # record noise (shot noise 1/2 filtered)
    D = np.sum(lam ** 2 * np.abs(chi) ** 2) / 2         # backaction on matter (each element saturated)
    X.append(P * D / (abs(F) ** 2 / 4)); Pe.append(P / abs(F) ** 2); Dv.append(D)
X = np.array(X); Pe = np.array(Pe); Dv = np.array(Dv)
print(f"    bank: {len(Gam)} elements, Gamma in [{Gam[0]:.0e}, 1], lambda_i = c_i = Gamma_i^1/2; excess X = P D/(|F|^2/4): min {X.min():.3f} max {X.max():.3f} (>= 1 is H-T; bounded)")
sel = (np.abs(us) > 1e-6) & (np.abs(us) < 1e-2)
slopeP = np.polyfit(np.log(np.abs(us[sel])), np.log(Pe[sel]), 1)[0]
slopeD = np.polyfit(np.log(np.abs(us[sel])), np.log(Dv[sel]), 1)[0]
print(f"    inside the band (1e-6<|u|<1e-2): d ln P_eff/d ln|u| = {slopeP:.3f} (target +1), d ln D/d ln|u| = {slopeD:.3f} (target -1)")
print(f"    at the cone (u=0): P_eff = {Pe[np.argmin(np.abs(us))]:.3e}, D = {Dv[np.argmin(np.abs(us))]:.3e} (both finite: floor set by Gamma_min ~ 2b)")
# with damped G: M = |G|^2 P_eff, |G|^2 ~ 1/(4 (u^2 + b^2)) in the same units (s ~ 2u, g w ~ 2b)
def bank_integrals(bb):
    Gm = np.logspace(math.log10(2 * bb), 0, int(8 * math.log10(1 / (2 * bb))) + 1)
    lm = np.sqrt(Gm)
    def PeD(u):
        chi = 1.0 / (Gm / 2 - 1j * u)
        F = np.sum(lm * lm * chi ** 2); P = np.sum(lm ** 2 * np.abs(chi) ** 2) / 2
        return P / abs(F) ** 2, P
    uu = np.logspace(math.log10(bb) - 4, 0, 4000)
    vals = np.array([PeD(u) for u in uu])
    M = vals[:, 0] / (uu ** 2 + bb ** 2); Dd = vals[:, 1]
    IM = 2 * np.trapezoid(M * uu, np.log(uu)); ID = 2 * np.trapezoid(Dd * uu, np.log(uu))
    return IM, ID, 2 * math.log(1 / bb)
for bb in [1e-4, 1e-8, 1e-12]:
    IM, ID, L2 = bank_integrals(bb)
    print(f"    b={bb:.0e}: int M du = {IM:.2f}, int D du = {ID:.2f}, 2 ln(1/b) = {L2:.1f}  (both finite, both ~ L; product/L^2 = {IM*ID/L2**2:.3f})")

# ------------------------------------------------------------------ [7]
print("\n[7] two-tone element: J(t) = cos(Om t) n_c(t) + sin(Om t) n_s(t), n_c, n_s iid stationary -> J stationary")
Om = 5.0; dt = 0.01; Nt = 2 ** 17; nreal = 200
a = math.exp(-dt)
# vectorised OU via lfilter
from scipy.signal import lfilter
lag = 37
for t_abs in [1000, 1000 + 31]:
    prods = []
    for _ in range(16000):
        wn = rng.normal(size=(2, 1100))
        ncs = lfilter([math.sqrt(1 - a * a)], [1, -a], wn, axis=1)
        tt = np.arange(1100) * dt
        J = np.cos(Om * tt) * ncs[0] + np.sin(Om * tt) * ncs[1]
        prods.append(J[t_abs] * J[t_abs - lag])
    print(f"    absolute time index {t_abs}: <J(t)J(t-{lag}dt)> = {np.mean(prods):+.4f} +- {np.std(prods)/math.sqrt(len(prods)):.4f};"
          f" stationary prediction e^(-lag dt) cos(Om lag dt) = {math.exp(-lag*dt)*math.cos(Om*lag*dt):+.4f}")

# ------------------------------------------------------------------ [8]
print("\n[8] Lamb-string sink: mode q (mass m=1, freq Om) attached to a semi-infinite string (impedance Z): friction g = Z/m")
def lamb(Z, Om=1.0, L=600.0, N=12000, T=60.0):
    dx = L / N; v = 1.0; mu = Z / v; tension = Z * v      # string: density mu, tension tau, impedance sqrt(mu tau) = Z
    dtt = 0.5 * dx / v
    y = np.zeros(N + 1); yd = np.zeros(N + 1)
    q = 0.0; qd = 1.0          # start with velocity, no initial kink in the string
    Es = []; Eq = []; ts = []; flux = 0.0; Fl = []
    nsteps = int(T / dtt)
    for n in range(nsteps):
        # string end attached: y[0] = q
        y[0] = q
        lapl = np.zeros(N + 1); lapl[1:-1] = (y[2:] - 2 * y[1:-1] + y[:-2]) / dx ** 2
        ydd = (tension / mu) * lapl
        # force on q from string: tension * dy/dx at x=0
        fq = tension * (y[1] - y[0]) / dx
        qdd = -Om * Om * q + fq
        flux += -fq * qd * dtt          # work done by the mode on the string
        qd += qdd * dtt; q += qd * dtt
        yd[1:-1] += ydd[1:-1] * dtt; y[1:-1] += yd[1:-1] * dtt
        yd[0] = qd
        if n % 200 == 0:
            Eq.append(0.5 * qd * qd + 0.5 * Om * Om * q * q)
            Es.append(np.sum(0.5 * mu * yd[1:-1] ** 2) * dx + np.sum(0.5 * tension * np.diff(y) ** 2 / dx))
            ts.append(n * dtt); Fl.append(flux)
    return np.array(ts), np.array(Eq), np.array(Es), np.array(Fl)
for Z in [0.05, 0.1]:
    ts, Eq, Es, Fl = lamb(Z)
    m = (ts > 5) & (ts < 50)
    rate = -np.polyfit(ts[m], np.log(Eq[m]), 1)[0]
    print(f"    Z={Z}: fitted energy decay rate of the mode = {rate:.4f} (Ohmic prediction g = Z/m = {Z:.4f}); "
          f"mode energy lost {Eq[0]-Eq[-1]:.4f} vs work delivered into the string {Fl[-1]:.4f} (mismatch {abs(Eq[0]-Eq[-1]-Fl[-1])/(Eq[0]):.1e}); string-energy estimator {Es[-1]:.4f}")

# ------------------------------------------------------------------ [9]
print("\n[9] sink and cosmology")
rho_crit = 8.5e-27                     # kg/m^3 (RECALLED, ~ H0=68)
rho_L = 0.69 * rho_crit * c ** 2       # J/m^3
for gam_H in [1.0, 3.0]:
    eta = gam_H * H0 * c ** 2 / (16 * math.pi * G)
    lmfp = 3 * eta / (rho_crit * c)
    print(f"    Hawking viscous fluid with gamma = {gam_H} H0: eta = gamma c^2/(16 pi G) = {eta:.2e} Pa s; kinetic estimate eta ~ rho c l/3 with rho <= rho_crit -> l_mfp >= {lmfp:.1e} m = {lmfp/Mpc:.0f} Mpc"
          f" (>> lambda_GW ~ 3e6 m at 100 Hz and >> ell: hydrodynamic damping not available)")
print("    Ohmic bath (oscillators at rest in the frame, no gradient energy) -> pressureless sink: rho_s' + 3H rho_s = gamma rho_GW -> steady rho_s = (gamma/3H) rho_GW")
for ell in [1e-8, 2e-7, 1e-6, 5e-6]:
    w = c / ell
    Lg = math.log(2 * w / H0)
    rhoGW_eps1 = Lg * hbar * c / (math.pi ** 3 * ell ** 4)       # R11-5 form rho_GW ~ eps L hbar c/(pi^3 l^4), O(1) weights (suggested)
    eps_need = rho_L / (rhoGW_eps1 * (1 + 1.0 / 3))              # GW content + sink at gamma = H0 (gamma/3H = 1/3)
    print(f"    ell={ell:.0e} m: L_g = ln(2w/H0) = {Lg:.1f}; rho_GW(eps=1) = {rhoGW_eps1:.2e} J/m^3 = {rhoGW_eps1/rho_L:.1e} rho_L; (GW+sink) < rho_L needs eps < {eps_need:.1e}")
for gam_H in [1e-10, 1e-2, 1.0, 3.0]:
    print(f"    gamma = {gam_H:.0e} H0: L_g at ell = 1e-6 m = {math.log(2*c/1e-6/(gam_H*H0)):.1f}")

# ------------------------------------------------------------------ [10]
print("\n[10] lab kernels and the TT projector")
for (wl, ell) in [(1e3, 5e-6), (1e-3, 4e-10)]:
    ck = c / ell
    x = H0 * wl / ck ** 2
    print(f"    lab w={wl:.0e} s^-1, ck=c/ell={ck:.1e} s^-1: gamma w/(ck)^2 = {x:.1e}; |G_g|^2/|G_R|^2 - 1 ~ -(gamma w/s)^2 = {-x*x:.1e} (subtraction: undamped kernel)")
# TT projector non-locality: D_ij = delta_i1 delta_j1 f(r), f supported in r<1; (Lambda^TT D)_11 outside the support
N = 96; Lbox = 24.0
xs = (np.arange(N) - N // 2) * (Lbox / N)
X3, Y3, Z3 = np.meshgrid(xs, xs, xs, indexing='ij')
R = np.sqrt(X3 ** 2 + Y3 ** 2 + Z3 ** 2)
f = np.where(R < 1, (1 - R ** 2) ** 3, 0.0)
kx = 2 * np.pi * np.fft.fftfreq(N, d=Lbox / N)
KX, KY, KZ = np.meshgrid(kx, kx, kx, indexing='ij')
K2 = KX ** 2 + KY ** 2 + KZ ** 2; K2[0, 0, 0] = 1.0
fk = np.fft.fftn(np.fft.ifftshift(f))
P11 = 1 - KX * KX / K2
# Lambda^TT_{11,11} = P11 P11 - 1/2 P11 P11 = 1/2 P11^2 for D = e1 e1 f
TT11 = np.real(np.fft.fftshift(np.fft.ifftn(0.5 * P11 ** 2 * fk)))
i0 = N // 2
for rr in [2.0, 3.0, 5.0]:
    j = i0 + int(round(rr / (Lbox / N)))
    print(f"    D=e1e1 f(r), f=0 for r>1: (Lambda^TT D)_11 at (0,{rr},0) = {TT11[i0, j, i0]:+.3e}, at ({rr},0,0) = {TT11[j, i0, i0]:+.3e}; f(0)={f[i0,i0,i0]:.1f}"
          f"  (nonzero outside the support: the TT projection is instantaneous and non-local)")

# ------------------------------------------------------------------ [11]
print("\n[11] sink fluctuation noise: if the Ohmic sink carried zero-point (FDT) noise S = 2 gamma hbar w into h,")
print("     each near-cone mode would hold int |G_g|^2 S ds/(2pi) ~ hbar w/2 independent of gamma -> rho ~ hbar c/(16 pi^2 ell^4)")
ws = 1.0; gg = 1e-6
s_ = np.concatenate([-np.logspace(-14, 1, 20001)[::-1], np.logspace(-14, 1, 20001)])
Gm2 = 1.0 / (s_ ** 2 + (gg * ws) ** 2)
val = np.trapezoid(Gm2 * 2 * gg * ws, s_) / (2 * math.pi)
print(f"    check: int |G_g|^2 (2 g w) ds/(2 pi) = {val:.4f} (-> 1/2 x [units hbar w per unit s-measure], gamma-independent)")
for ell in [1e-8, 2e-7, 1e-6, 5e-6]:
    rho_zp = hbar * c / (16 * math.pi ** 2 * ell ** 4)
    print(f"    ell={ell:.0e} m: rho_zp = {rho_zp:.2e} J/m^3 = {rho_zp/rho_L:.1e} rho_L  (a noisy quantum sink breaks the epsilon budget; a classical T=0 outgoing-only sink adds none)")
