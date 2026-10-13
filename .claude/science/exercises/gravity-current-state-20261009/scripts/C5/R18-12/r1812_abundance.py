"""C5 R18-12 (b)-(c): corner-class ground states (proof inputs), relic abundance vs T_RH, and the bounds.

(0) Proof input for Theorem C': every quantum of the G-world (G(1.4) scalar any m >= 0; photon R85 or plaquette 'std')
    obeys E(k) >= (2/pi)|k|_T, |k|_T = Euclidean norm of the wrapped momentum. Checked on a dense grid and on the
    1D profiles (separable: E >= (2/pi)|k|_T follows from h(k) >= (2/pi)|k| and d(q) >= (2/pi)|q| per component).
    For D1 the same bound fails at the corners (doublers W_pi = 0.095 < 2): listed.
(1) Freeze-in from a thermal SM-like bath below T_RH (no equilibrium: Gamma/H << 1 is checked in (3)):
      Y = int_0^{T_RH} gamma(T) / (s H T) dT,  gamma = production rate density.
    (a) pair production of D1 doublers:  gamma = g^2 (M T/2pi)^3 e^{-2M/T} <sigma v>,  <sigma v> = kappa alpha^2/M^2
    (b) single production of corner photons from >= 3 box quanta (threshold E_th = pi/a):
        gamma = kappa alpha^3 T^4 (E_th/T)^{3/2} e^{-E_th/T}  (generic Maxwell-Boltzmann threshold form)
    kappa scanned 1e-6 .. 1e2: T_RH,max moves only logarithmically.
    Bound used: Omega h^2 <= 0.12 (RECALLED Planck 2018) with Omega h^2 = 2.744e8 (M/GeV) Y (RECALLED s0, rho_c).
(2) T_RH >= 1/a: initial class abundance Y0 in [1e-4, 1e-1] (O(1) of the lattice modes); Omega h^2 that follows.
(3) Gamma/H for annihilation / conversion at T <= 1/a with sigma ~ alpha^2/M^2 and gravitational sigma ~ a^2.
(4) Observable (i): W7 far-field mass for a lab body containing relic gas at the local DM density (upper bound),
    and the relic gas's own velocity-dependent mass.  Observable (iv): lifetimes.
Conventions: a = l_P reading, 1/a = M_P = 1.2209e19 GeV; g* = 106.75; alpha = 1/40 at the Planck scale (RECALLED).
"""
import os, sys
os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r1812_laws import Matter, omega, photon_delta, PHOTONS, G14, WPI, wrap

lines = []
def pr(s=""):
    print(s, flush=True); lines.append(s)

MP = 1.2209e19; gs = 106.75; alpha = 1/40.0
OMEGA_MAX = 0.12; C_OM = 2.744e8

# (0)
pr("(0) lower bound E(k) >= (2/pi)|k|_T (proof input for the corner theorem)")
q = np.linspace(1e-6, np.pi, 200001)
h = np.sqrt(G14.g(q)); pr("   G(1.4): min_k h(k)/k on (0,pi] = %.6f  (2/pi = %.6f)" % ((h/q).min(), 2/np.pi))
for ph in ('R85', 'std'):
    d = PHOTONS[ph](q); pr("   photon %-3s: min_q d(q)/q on (0,pi] = %.6f;  d(pi) = %.6f" % (ph, (d/q).min(), PHOTONS[ph](np.pi)))
rng = np.random.default_rng(7)
K = rng.uniform(-np.pi, np.pi, size=(400000, 3)); KT = np.linalg.norm(wrap(K), axis=1)
for m in (0.0, 0.3):
    r = Matter('G', m).eps(K)/KT; pr("   G m=%.1f: min over 4e5 random k of eps/|k|_T = %.6f" % (m, r.min()))
for ph in ('R85', 'std'):
    r = omega(ph, K)/KT; pr("   photon %-3s: min over 4e5 random q of omega/|q|_T = %.6f" % (ph, r.min()))
r = Matter('D1', 0.0).eps(K)/KT; pr("   D1 m=0 (control): min eps/|k|_T = %.6f  (fails: doublers, W_pi = %.4f at |k|_T = pi)" % (r.min(), WPI))
for c, Kc in (("(pi,0,0)", [np.pi, 0, 0]), ("(pi,pi,0)", [np.pi, np.pi, 0]), ("(pi,pi,pi)", [np.pi]*3)):
    w = omega('R85', [Kc])[0]; dl = photon_delta('R85', [Kc])[0]
    pr("   corner photon %-10s omega = %.4f = (2/pi)|K|_T = %.4f ; Delta diag = %s ; Q_D/E per axis = %s"
       % (c, w, 2/np.pi*np.linalg.norm(Kc), np.round(dl, 4).tolist(), np.round(dl/w, 4).tolist()))
pr("")

# (1)
def H(T): return 1.66*np.sqrt(gs)*T**2/MP
def s(T): return 2*np.pi**2/45*gs*T**3
def Y_pair(TRH, M, kappa, g=4):
    f = lambda T: g**2*(M*T/(2*np.pi))**3*np.exp(-2*M/T)*kappa*alpha**2/M**2/(s(T)*H(T)*T)
    lo = TRH/200.0
    return quad(f, lo, TRH, limit=200, points=[TRH*0.5])[0]
def Y_single(TRH, Eth, kappa):
    f = lambda T: kappa*alpha**3*T**4*(Eth/T)**1.5*np.exp(-Eth/T)/(s(T)*H(T)*T)
    return quad(f, TRH/200.0, TRH, limit=200)[0]
def TRH_max(Yfun, M):
    Ymax = OMEGA_MAX/(C_OM*M)
    g = lambda lt: np.log(max(Yfun(10**lt), 1e-300)) - np.log(Ymax)
    return 10**brentq(g, 14.0, 19.5), Ymax

pr("(1) freeze-in relic abundance and T_RH,max from Omega h^2 <= 0.12")
Md = WPI*MP
pr("   (a) D1 doublers (Delta = 0, W7-inert, charge of the parent species): M = %.4f/a = %.3e GeV, pair threshold 2M" % (WPI, Md))
for kappa in (1e-6, 1e-3, 1.0, 1e2):
    Tm, Ymax = TRH_max(lambda T: Y_pair(T, Md, kappa), Md)
    pr("       kappa = %-6g: Y_max = %.2e ; T_RH,max = %.3e GeV  (2M/T_RH,max = %.1f)" % (kappa, Ymax, Tm, 2*Md/Tm))
for TRH in (1e15, 6.8e15, 1e16, 3e16, 1e17):
    Y = Y_pair(TRH, Md, 1.0); pr("       T_RH = %.1e GeV: Y = %.2e  Omega h^2 = %.2e" % (TRH, Y, C_OM*Md*Y))
Mc = 2.0*MP; Eth = np.pi*MP
pr("   (b) G-world corner photon (pi,0,0) (Delta_xx = -4/a, W7-carrying): M = 2/a = %.3e GeV, single-production threshold pi/a" % Mc)
for kappa in (1e-6, 1e-3, 1.0, 1e2):
    Tm, Ymax = TRH_max(lambda T: Y_single(T, Eth, kappa), Mc)
    pr("       kappa = %-6g: Y_max = %.2e ; T_RH,max = %.3e GeV  (E_th/T_RH,max = %.1f)" % (kappa, Ymax, Tm, Eth/Tm))
for TRH in (6.8e15, 1e17, 3e17, 1e18):
    Y = Y_single(TRH, Eth, 1.0); pr("       T_RH = %.1e GeV: Y = %.2e  Omega h^2 = %.2e" % (TRH, Y, C_OM*Mc*Y))
pr("       threshold bracket: any initial state with total K = (pi,0,0) has E >= (2/pi)|K|_T = 2/a = M (Theorem C' bound); E_th = M gives:")
for kappa in (1e-6, 1.0, 1e2):
    Tm, Ymax = TRH_max(lambda T: Y_single(T, Mc, kappa), Mc)
    pr("       kappa = %-6g, E_th = 2/a: T_RH,max = %.3e GeV" % (kappa, Tm))
Me = 1.5314*MP
pr("   (c) lightest grid-stable defect-carrying matter edge state of the D1+R85 world: M = 1.5314/a; threshold bracket [M, 2M]")
for Ef in (1.0, 2.0):
    Tm, Ymax = TRH_max(lambda T: Y_single(T, Ef*Me, 1.0), Me)
    pr("       E_th = %.0f M: T_RH,max = %.3e GeV" % (Ef, Tm))
TI = 0.418*1.6e16
pr("   RECALLED: r < 0.036 (BICEP/Keck 2021) gives V^1/4 < 1.6e16 GeV, so instant reheating gives T_RH <= %.2e GeV (g* = 106.75)." % TI)
pr("       At that T_RH: doubler Boltzmann exponent 2M/T = %.0f ; corner-photon E_th/T = %.0f." % (2*Md/TI, Eth/TI))
pr("")

# (2)
pr("(2) T_RH >= 1/a: class abundance frozen at its initial value Y0 (see (3)); Omega h^2 = 2.744e8 M Y0")
for Y0 in (1e-4, 1e-2, 1e-1):
    pr("   Y0 = %.0e: doublers Omega h^2 = %.1e ; corner photons Omega h^2 = %.1e  (bound 0.12)" % (Y0, C_OM*Md*Y0, C_OM*Mc*Y0))
pr("   largest allowed initial abundance: Y0 < %.1e (doublers), < %.1e (corner photons)" % (OMEGA_MAX/(C_OM*Md), OMEGA_MAX/(C_OM*Mc)))
pr("")

# (3)
pr("(3) Gamma/H at T <= 1/a for removal by annihilation or conversion (n_partner ~ 0.1 T^3, v ~ 1)")
for T in (1.0, 0.1, 0.01):
    TT = T*MP
    for name, M in (("doubler", Md), ("corner photon", Mc)):
        g_gauge = 0.1*TT**3*alpha**2/M**2/H(TT)
        g_grav = 0.1*TT**3*(1/MP**2)/H(TT)
        pr("   T = %.2f/a  %-13s: gauge sigma ~ alpha^2/M^2: Gamma/H = %.1e ; gravitational sigma ~ a^2: Gamma/H = %.1e" % (T, name, g_gauge, g_grav))
pr("")

# (4)
pr("(4) observables (i) and (iv)")
rho_dm = 0.4; rho_body = 4.0*5.61e23          # GeV/cm^3  (RECALLED local DM density; 4 g/cm^3 body)
f = rho_dm/rho_body; V = 1.23e-3
for qd in (2.0, 20.0):
    pr("   (i) lab body with relic gas at the full local DM density, |Q_D/E| = %4.0f: edge fraction f <= %.1e ; |dM/M| <= f |Q/E| V^2/2 = %.1e  (MICROSCOPE-type bound ~1e-15)" % (qd, f, f*qd*V**2/2))
pr("   (i') the relic gas itself (corner photons, along the corner axis): M(V) = M[1 - Q V^2/(2(E+Q))] with Q = -2E: dM/M = -V^2 = %.1e at V = %.2e" % (-V**2, V))
tau = 1/(alpha*MP)*6.58e-25
pr("   (iv) open edge decays: lifetime ~ a/alpha ~ %.1e s (no BBN/CMB injection); sector ground states: no decay at all." % tau)
open(os.path.splitext(os.path.abspath(__file__))[0] + ".out", "w").write("\n".join(lines) + "\n")
