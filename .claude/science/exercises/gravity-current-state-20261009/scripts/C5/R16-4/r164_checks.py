#!/usr/bin/env python3
"""
C5 R16-4: set A, route E1 -- does any late-time observable remember the initial state?
Every number in R16-4_report.md is printed here. Run: OMP_NUM_THREADS=2 python3 r164_checks.py > r164_checks.out

Model (stated before any run): R13-6's linearized preferred-frame E1 model, repaired gain P-r13b
  F = exp(-k^2 l^2/2) F_t(w),  F_t = (1 - 4 i w tau)(1 - i w tau)^-4,  f(t) = e^{-x} x^2 (4 - x)/(2 tau), x = t/tau,
per frame mode k (Omega = c|k|), TT channel (R15-2: only TT has the cone pole; S/V constraint channels carry no free data).
Metric noise kernel K = f * J0(Omega .)  (the gain is the stated bandwidth regulator for hdot: K(0) = K'(0) = 0).
Initial-state class G(n_b, k_c): product Gaussian states, per normal mode excess energy <= n_b quanta(-equivalent),
for |k| <= k_c; vacuum start elsewhere.  Sections:
 [1] Lambda(n): worst excess second moment of an energy-bounded Gaussian mode, relative to vacuum
 [2] TT free data: exact energy memory (Monte Carlo of the E1 TT mode with record noise)
 [3] J0 tail: a record-current perturbation reaches h through K; amplitude ~ t^-1/2, energy ~ 1/t
 [4] Domination lemma on a random passive network: excess <= Lambda * (vacuum internal part), decay e^{-Gamma_min t}
 [5] Near-cone budget: initial TT energy vs rho_Lambda; thresholds; record's own occupation per mode
 [6] Lab observables: GW-background effect at n_b = 1; meter excess threshold
 [7] PPN-type: <h^2> and noise-fluid term from initial TT data
 [8] R15-2's initial-memory term B: decay of Psi_1 for the repaired gain (matter at t0; outside the class)
 [9] Double-pulsar drag: state independence at linear order; bath-friction size
 [10] E2 aside: fraction of initial TT energy left at t_H under drag-allowed friction
Subtractions: [1],[4] the vacuum (steady-state) second moments; [2] the vacuum-start mean energy; [3] none (positive
envelopes); [5]-[7] none (positive energies/variances) except the record's own content where stated; [8] Psi_1(inf) = 0
(exact; printed); [9] none; [10] none.
"""
import math, numpy as np
from scipy import special, integrate, optimize

np.random.seed(16004)
hbar = 1.054571817e-34; c = 2.99792458e8; G = 6.67430e-11; kB = 1.380649e-23
lP = math.sqrt(G*hbar/c**3)
tH = 4.35e17                      # s (RECALLED, as R11-5/R13-6)
rho_crit = 8.5e-27*c**2           # J/m^3 (RECALLED, as R11-5/R13-6)
rho_L = 0.69*rho_crit
H0 = 1/tH*0.957                   # s^-1 (RECALLED ~2.2e-18)

def sec(s): print("\n" + s)

# ---------------------------------------------------------------- [1]
sec("[1] Lambda(n) = sup lambda_max(V_vac^-1/2 M0 V_vac^-1/2), M0 = V + m m^T - V_vac, single mode, excess energy <= n quanta")
print("    subtraction: the vacuum second moments V_vac = I/2")
def lam_state(nth, r, phi, ax, ay):
    S = np.diag([math.exp(2*r), math.exp(-2*r)])
    R = np.array([[math.cos(phi), -math.sin(phi)], [math.sin(phi), math.cos(phi)]])
    V = (nth + 0.5)*R @ S @ R.T
    m = math.sqrt(2)*np.array([ax, ay])
    M0 = V + np.outer(m, m) - 0.5*np.eye(2)
    E = (nth + 0.5)*math.cosh(2*r) - 0.5 + ax*ax + ay*ay
    return np.linalg.eigvalsh(2*M0).max(), E
for n in [1e-6, 1e-2, 1.0, 1e2]:
    best = 0.0
    for _ in range(20000):
        w = np.random.dirichlet([1, 1, 1])*n     # split excess energy among thermal / squeeze / displacement (approx.)
        nth = w[0]
        # choose r so that (nth+1/2)cosh2r - 1/2 - nth = w[1]
        r = 0.5*math.acosh((w[1] + nth + 0.5)/(nth + 0.5))
        a = math.sqrt(max(w[2], 0)); ph = np.random.uniform(0, 2*math.pi)
        lmax, E = lam_state(nth, r, np.random.uniform(0, math.pi), a*math.cos(ph), a*math.sin(ph))
        if E <= n*(1 + 1e-9): best = max(best, lmax)
    formula = 2*n + 2*math.sqrt(n*(n + 1))
    lpure, _ = lam_state(0, math.asinh(math.sqrt(n)), 0, 0, 0)
    print(f"    n = {n:.0e}: sampled sup = {best:.6e}; pure squeeze sinh^2 r = n gives {lpure:.6e}; formula 2n+2sqrt(n(n+1)) = {formula:.6e}; thermal 2n = {2*n:.1e}; displaced 4n = {4*n:.1e}")
print("    correlated multimode (collective squeeze over N modes, per-mode excess n = 1): lambda_max = e^{2r}-1, sinh^2 r = N n")
for N in [1, 10, 1000]:
    r = math.asinh(math.sqrt(N*1.0)); print(f"      N = {N}: lambda_max = {math.exp(2*r)-1:.3e}  (=> per-mode bounds need product states; else Lambda grows ~4N n)")

# ---------------------------------------------------------------- kernels
tau = 0.2                          # units 1/Omega
def f_gain(t):
    x = np.asarray(t)/tau
    return np.where(x >= 0, np.exp(-x)*x**2*(4 - x)/(2*tau), 0.0)
fm0 = integrate.quad(lambda t: float(f_gain(t)), 0, 60*tau)[0]
fm1 = integrate.quad(lambda t: t*float(f_gain(t)), 0, 60*tau)[0]
def K_of_t(t, deriv=False):
    # K(t) = int_0^t f(s) J0(t-s) ds ; K'(t) = f(t) J0(0) - int_0^t f(s) J1(t-s) ds  (boundary term f(t): ref_R15-2 item 5)
    up = min(t, 60*tau)
    if deriv:
        return float(f_gain(t)) - integrate.quad(lambda s: float(f_gain(s))*special.j1(t - s), 0, up, limit=200)[0]
    return integrate.quad(lambda s: float(f_gain(s))*special.j0(t - s), 0, up, limit=200)[0]

# ---------------------------------------------------------------- [2]
sec("[2] TT free data in E1 (Omega = 1, tau = 0.2): <E(t)>_state - <E(t)>_vac vs the initial excess (subtraction: vacuum-start mean energy)")
print(f"    gain moments: int f = {fm0:.12f}, int t f = {fm1:.2e} (zero first moment, P-r13b)")
dt = 0.01; Tmax = 400.0; ns = int(Tmax/dt)
tg = np.arange(ns)*dt
# K = f * J0 by direct discrete convolution on the whole grid (f supported on [0, 60 tau])
fg = f_gain(tg[:int(60*tau/dt)])
J0g = special.j0(tg); J1g = special.j1(tg)
Kfull = np.convolve(fg, J0g)[:ns]*dt
Kpfull = f_gain(tg) - np.convolve(fg, J1g)[:ns]*dt   # K' = f(t) J0(0) - f * J1  (boundary term per ref_R15-2 item 5)
for tchk in [10.0, 300.0]:
    i = int(tchk/dt)
    print(f"    check K({tchk}) grid = {Kfull[i]:.6e} vs quadrature {K_of_t(tchk):.6e};  K'({tchk}) grid = {Kpfull[i]:.6e} vs {K_of_t(tchk, True):.6e}")
print(f"    K(0) = {Kfull[0]:.1e}, K'(0) = {Kpfull[0]:.1e} (gain makes hdot regular; vR13-6:27-31 white-noise term absent)")
samples = [20.0, 100.0, 399.0]
npaths = 8000; chunk = 250
Svar = 0.5                       # white record noise, two-sided density 1/2 (R13-6 convention)
sig0 = 1.0                       # thermal-like initial TT data: h0, v0 ~ N(0, sig0^2) => initial mean energy sig0^2
A0 = 1.0                         # displaced: h0 = A0 => initial energy A0^2/2
res = {s: {"vac": [], "th": [], "dis": [], "cross": []} for s in samples}
for c0 in range(0, npaths, chunk):
    xi = np.random.randn(chunk, ns)*math.sqrt(Svar/dt)
    h0 = np.random.randn(chunk)*sig0; v0 = np.random.randn(chunk)*sig0
    for s in samples:
        i = int(s/dt)
        kk = Kfull[i::-1][:i+1]; kp = Kpfull[i::-1][:i+1]
        hn = xi[:, :i+1] @ kk*dt; hdn = xi[:, :i+1] @ kp*dt
        Evac = 0.5*(hn**2 + hdn**2)
        hf = h0*math.cos(s) + v0*math.sin(s); vf = -h0*math.sin(s) + v0*math.cos(s)
        Eth = 0.5*((hn + hf)**2 + (hdn + vf)**2)
        hd = A0*math.cos(s); vd = -A0*math.sin(s)
        Edis = 0.5*((hn + hd)**2 + (hdn + vd)**2)
        res[s]["vac"].append(Evac); res[s]["th"].append(Eth); res[s]["dis"].append(Edis)
        res[s]["cross"].append(hn*hf + hdn*vf)
for s in samples:
    ev = np.concatenate(res[s]["vac"]); et = np.concatenate(res[s]["th"]); ed = np.concatenate(res[s]["dis"]); cr = np.concatenate(res[s]["cross"])
    se = lambda a: a.std()/math.sqrt(len(a))
    i = int(s/dt); Eth_vac = 0.5*Svar*np.sum(Kfull[:i+1]**2 + Kpfull[:i+1]**2)*dt
    print(f"    t = {s:6.1f}: <E>_vac = {ev.mean():.4f} +- {se(ev):.4f} (exact (1/4) int_0^t (K^2+K'^2) = {Eth_vac:.4f}; grows ~ log t); "
          f"thermal-vac = {et.mean()-ev.mean():.4f} +- {se(et-ev):.4f} (initial excess {sig0**2:.4f}); "
          f"displaced-vac = {ed.mean()-ev.mean():.4f} +- {se(ed-ev):.4f} (initial {A0**2/2:.4f}); <cross> = {cr.mean():.4f} +- {se(cr):.4f}")
print("    => the excess is the initial free-wave energy, unchanged at every t (no attractor in the TT free-data sector)")

# ---------------------------------------------------------------- [3]
sec("[3] J0 tail: a unit record-current pulse at t0 reaches h as K(t)/sqrt(2) (subtraction: none; positive envelopes)")
for t in [10.0, 100.0, 1000.0, 10000.0]:
    Kt = K_of_t(t); Kpt = K_of_t(t, True)
    print(f"    t = {t:8.0f}: t*(K^2 + K'^2) = {t*(Kt**2 + Kpt**2):.5f} (-> 2/pi = {2/math.pi:.5f}); amplitude*sqrt(t) = {math.sqrt(t*(Kt**2+Kpt**2)):.5f}")
Ft1 = abs((1 - 4j*tau)/(1 - 1j*tau)**4)**2
print(f"    limit (2/pi)|F_t(Omega)|^2 = {2/math.pi*Ft1:.5f} (|F_t(Omega tau = {tau})|^2 = {Ft1:.4f}): the J0 tail carries the cone gain")
print("    => pulse energy in h decays as |F|^2 (1/pi)/(Omega t): the record-current sector has a t^-1/2 (amplitude) attractor")
print("    contrast: a perturbation of h(t0), hdot(t0) (or of the classical post-filter state) is a free wave: energy constant ([2])")
for name, k in [("k = 1/(1 um)", 1e6), ("k = 1/(4e-10 m)", 2.5e9), ("k = 1/AU", 1/1.496e11), ("k = 1/(1 kpc)", 1/3.086e19)]:
    W = c*k
    print(f"      {name}: Omega t_H = {W*tH:.2e}; relative pulse energy left at t_H ~ (2/pi)/(Omega t_H) = {(2/math.pi)/(W*tH):.1e}")

# ---------------------------------------------------------------- [4]
sec("[4] Domination lemma on random passive linear networks (subtraction: the steady-state = vacuum second moments)")
def rand_passive(nm, rng):
    # complex amplitudes a: da/dt = (-i H - L^dag L/2) a + ...; quadrature form A (2nm x 2nm)
    Hm = rng.normal(size=(nm, nm)) + 1j*rng.normal(size=(nm, nm)); Hm = (Hm + Hm.conj().T)/2
    L = rng.normal(size=(1, nm))*0.3 + 1j*rng.normal(size=(1, nm))*0.3
    Ac = -1j*Hm - 0.5*L.conj().T @ L
    # real representation for x = (Re a, Im a)*sqrt(2)
    A = np.block([[Ac.real, -Ac.imag], [Ac.imag, Ac.real]])
    return A
rng = np.random.default_rng(7)
worst = 0.0; worst_mean = 0.0; rates = []
for trial in range(200):
    nm = 4; A = rand_passive(nm, rng)
    Gmin = -np.linalg.eigvals(A).real.max(); rates.append(Gmin)
    Vss = 0.5*np.eye(2*nm)               # passive network, vacuum input: steady state = vacuum
    # product Gaussian initial state, each mode excess <= n_b = 0.5 quanta
    nb = 0.5; blocks = []; m0 = []
    for j in range(nm):
        w = rng.dirichlet([1, 1, 1])*nb; nth = w[0]
        r = 0.5*math.acosh((w[1] + nth + 0.5)/(nth + 0.5)); phi = rng.uniform(0, math.pi)
        Rm = np.array([[math.cos(phi), -math.sin(phi)], [math.sin(phi), math.cos(phi)]])
        blocks.append((nth + 0.5)*Rm @ np.diag([math.exp(2*r), math.exp(-2*r)]) @ Rm.T)
        a = math.sqrt(w[2]); ph = rng.uniform(0, 2*math.pi); m0.append(math.sqrt(2)*np.array([a*math.cos(ph), a*math.sin(ph)]))
    V0 = np.zeros((2*nm, 2*nm)); mm = np.zeros(2*nm)
    for j in range(nm):
        idx = [j, j + nm]
        V0[np.ix_(idx, idx)] = blocks[j]; mm[idx] = m0[j]
    D0 = V0 - Vss                         # covariance excess: block-diagonal for product states
    Lam = 2*nb + 2*math.sqrt(nb*(nb + 1))
    from scipy.linalg import expm
    for t in [0.0, 1.0, 5.0]:
        Phi = expm(A*t)
        cvec = rng.normal(size=2*nm)
        ct = Phi.T @ cvec
        exc = ct @ D0 @ ct; vac = ct @ Vss @ ct
        worst = max(worst, exc/(Lam*vac))
        worst_mean = max(worst_mean, (ct @ mm)**2/(4*nb*vac))
print(f"    200 random 4-mode passive networks, product Gaussian states with per-mode excess <= 0.5 quanta, 3 times each:")
print(f"    covariance part: max [c_t^T (V0 - V_ss) c_t] / [Lambda(0.5) c_t^T V_ss c_t] = {worst:.4f} (<= 1 required); Lambda(0.5) = {2*0.5+2*math.sqrt(0.75):.4f}")
print(f"    mean part: max (c_t . m0)^2 / [4 n_b c_t^T V_ss c_t] = {worst_mean:.4f}  (can exceed 1: coherent displacements add across modes;")
print(f"      bound is (c.m)^2 <= (sum_j 4|alpha_j|^2) c^T V_ss c = 4 x (total displaced quanta) x vacuum; enters only first moments and mode-diagonal energies)")
print(f"    and c_t^T V_ss c_t = |Phi(t)^T c|^2/2 decays as e^(-2 Gamma_min t): Gamma_min over the sample in [{min(rates):.3f}, {max(rates):.3f}]")

# ---------------------------------------------------------------- [5]
sec("[5] near-cone budget: initial TT energy (2 polarizations, n_b quanta per mode for |k| <= k_c) vs rho_Lambda (subtraction: none)")
print(f"    rho_Lambda = {rho_L:.3e} J/m^3 ; rho_init = n_b hbar c k_c^4/(4 pi^2) (exact for the class edge; conserved at linear order, [2])")
def rho_init(nb, kc): return nb*hbar*c*kc**4/(4*math.pi**2)
print("    (a) k_c = 1/l (modes the strict gain sees):")
for l in [4e-10, 2e-9, 1e-8, 1e-6, 5e-6]:
    kc = 1/l
    print(f"      l = {l:.0e} m: rho_init(n_b=1)/rho_L = {rho_init(1, kc)/rho_L:.2e};  threshold n_b* = {rho_L/rho_init(1, kc):.2e} quanta/mode")
print("    (b) k_c = 1/(c tau_c), c tau_c in R14-2's window [lower(l), 1.49e-3 m] (vR14-2:7):")
for ctc in [1.2e-4, 5.2e-4, 1.49e-3]:
    kc = 1/ctc
    print(f"      c tau_c = {ctc:.2e} m: rho_init(n_b=1)/rho_L = {rho_init(1, kc)/rho_L:.2e};  threshold n_b* = {rho_L/rho_init(1, kc):.2e}")
kcs = (4*math.pi**2*rho_L/(hbar*c))**0.25
print(f"    (c) one quantum per mode in every TT mode with k <= k_c* = {kcs:.3e} m^-1 (wavelength 2pi/k_c* = {2*math.pi/kcs*1e3:.3f} mm) already equals rho_Lambda")
Ts = (15*rho_L*(hbar*c)**3/math.pi**2)**0.25/kB
print(f"    (d) thermal (Planck occupation) TT state: rho = (pi^2/15)(kT)^4/(hbar c)^3 = rho_Lambda at T* = {Ts:.2f} K")
rho_cmb = math.pi**2/15*(kB*2.7255)**4/(hbar*c)**3
print(f"        (check: photon-like rho at 2.7255 K = {rho_cmb:.3e} J/m^3)")
print("    (f) classical (Rayleigh-Jeans) thermal TT state, k_B T per mode per polarization up to k_c = 1/l: rho = k_B T k_c^3/(3 pi^2)")
for l in [4e-10, 1e-8, 1e-6, 5e-6]:
    TRJ = 3*math.pi**2*rho_L*l**3/kB
    print(f"      l = {l:.0e} m: rho = rho_Lambda at T_RJ* = {TRJ:.2e} K;  at T = 2.7255 K rho/rho_L = {kB*2.7255/(l**3)/(3*math.pi**2)/rho_L:.1e}")
print("    (e) record's own TT occupation per mode at t_H (R15-2 TT normalization; leading-log weight 1/4 refereed, finite constant NOT: ref_R15-2 item 5):")
gE = 0.5772156649
for k in [1e3, 1e6, 1e8]:
    W = c*k; Lp = math.log(W*tH)
    print(f"      k = {k:.0e} m^-1: n_rec = eps |F|^2 (ln(Omega t_H) + O(1))/(2 pi) = {Lp/(2*math.pi):.2f} eps |F|^2 (+- ~0.5 from the unrefereed constant; L = {Lp:.1f})")
print("        strict-variant eps (R15-2 out:50-53, endpoints uncertain at O(1/L) per ref_R15-2: 4.7e-16, 6.3e-11, 3.6e-8, 2.1e-5 at l = 1e-8, 2e-7, 1e-6, 5e-6 m) => n_rec(k ~ 1/l) ~ 12 eps e^-1:")
for l, eps in [(1e-8, 4.7e-16), (2e-7, 6.3e-11), (1e-6, 3.6e-8), (5e-6, 2.1e-5)]:
    W = c/l; Lp = math.log(W*tH)
    print(f"          l = {l:.0e}: n_rec(1/l) = {eps*math.exp(-1)*Lp/(2*math.pi):.1e} quanta/mode, vs threshold n_b*(k_c = 1/l) = {rho_L/rho_init(1, 1/l):.1e}")

# ---------------------------------------------------------------- [6]
sec("[6] lab observables (subtraction: none)")
def Omega_GW(nb, f):
    w = 2*math.pi*f
    drho_dlnw = nb*hbar*w**4/(math.pi**2*c**3)
    return drho_dlnw/rho_crit
for f in [1e-4, 1e-3, 1e2]:
    Og = Omega_GW(1, f)
    Sh = 3*H0**2/(2*math.pi**2)*Og/f**3             # one-sided strain PSD (RECALLED relation)
    Lsep = 0.376                                       # LPF test-mass separation (RECALLED)
    Sa = ((2*math.pi*f)**2*Lsep/2)**2*Sh
    print(f"    n_b = 1 TT background at f = {f:.0e} Hz: Omega_GW = {Og:.2e}; sqrt(S_h) = {math.sqrt(Sh):.2e}/sqrt(Hz); LPF-like tidal sqrt(S_a) = {math.sqrt(Sa):.2e} m s^-2/sqrt(Hz) vs 1.74e-15")
mCs = 132.905*1.66054e-27
for l in [4e-10, 1e-6, 5e-6]:
    kc = 1/l; h2 = 16*lP**2*kc**2/math.pi
    for v in [1e-2, 1.0]:
        rate = (mCs*v**2/hbar)**2*h2*(l/c)          # (m v^2/hbar)^2 <h^2> x correlation time l/c  (TT couples to slow matter via h_ij T^ij ~ m v^i v^j)
        if v == 1e-2: print(f"    Cs-133 dephasing from n_b = 1 TT background, k_c = 1/l = {kc:.1e}: (m v^2/hbar)^2 <h^2> (l/c) = {rate:.1e} s^-1 at v = 1 cm/s; x70 s = {rate*70:.1e} (vs O(1) loss)")
print("    meter sector: excess decoherence functional <= Lambda(n_b) x vacuum prediction (domination, [4]); vacuum prediction")
print("    <= 1e-9 of the comparator (R6-4's smallest margin, inherited via vR11-5:12 / R13-6:344) => below comparator iff Lambda < 1e9:")
nstar = optimize.brentq(lambda n: 2*n + 2*math.sqrt(n*(n+1)) - 1e9, 1, 1e12)
print(f"      Lambda(n_b) = 1e9 at n_b = {nstar:.3e} quanta per meter mode")

# ---------------------------------------------------------------- [7]
sec("[7] PPN-type: initial TT data at second order (subtraction: none)")
for l in [4e-10, 1e-6, 5e-6]:
    kc = 1/l
    h2 = 16*lP**2*kc**2/math.pi
    print(f"    n_b = 1, k_c = 1/l = {kc:.1e}: <h_ij h_ij>_init = 16 n_b lP^2 k_c^2/pi = {h2:.2e} (R15-2's record value <= 1.4e-49); "
          f"fluid term 1.6e-33 rho_init/rho_crit = {1.6e-33*rho_init(1, kc)/rho_crit:.1e} vs alpha2 < 1.6e-9")

# ---------------------------------------------------------------- [8]
sec("[8] R15-2's initial-memory term B for matter present at t0 (outside the class; subtraction: Psi_1(inf) = 0, printed)")
taur = 1.0
psi = lambda s: integrate.quad(lambda t: math.exp(-t)*t**2*(4 - t)/2, s, np.inf)[0]   # f in units tau = 1
Psi1_inf = integrate.quad(lambda s: psi(s), 0, 80)[0]
print(f"    (units tau = 1) Psi_1(inf) = int_0^inf psi = int t f = {Psi1_inf:.2e}")
for s in [10, 20, 40]:
    tail = integrate.quad(lambda u: psi(u), s, 80)[0]
    print(f"    s = {s} tau: psi(s) = {psi(s):.2e}; Psi_1(s) - Psi_1(inf) = {-tail:.2e}")
print("    => B decays like s^3 e^{-s/tau}; at tau <= 5 ps it is gone within ~ 1e-10 s of t0")

# ---------------------------------------------------------------- [9]
sec("[9] double-pulsar drag (subtraction: none)")
print("    linear order: the self-force is the odd part of the body's own mean response (Lemma D, vR13-6:3-7); initial data")
print("    add a body-independent homogeneous solution, so Gamma is state-independent (proved in report §3.5)")
M = 1.3*1.989e30; rg = G*M/c**2
for rho in [rho_L, 1e3*rho_L]:
    Gam = rho*math.pi*rg**2*4/(M*c)
    print(f"    bath-friction upper estimate (geometric cross-section pi (GM/c^2)^2, momentum transfer x4): rho = {rho/rho_L:.0e} rho_L -> Gamma <= {Gam:.1e} s^-1 vs 6.1e-21")

# ---------------------------------------------------------------- [10]
sec("[10] E2 aside (outside the setting): fraction of initial TT energy left at t_H, energy damping e^{-gamma t}")
for g in [0.016, 0.024, 0.032, 0.047]:
    print(f"    gamma = {g} H0: e^(-gamma t_H) = {math.exp(-g*0.957*1.0):.3f}  (H0 t_H ~ 0.96 with the RECALLED t_H)")
print("\nend")
