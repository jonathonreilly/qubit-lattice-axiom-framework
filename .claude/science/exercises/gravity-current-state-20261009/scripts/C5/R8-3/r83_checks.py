#!/usr/bin/env python3
"""C5 R8-3 checks: relativistic completion of smeared CQ gravity.

Sections
 [1] Lemma V0: invariant hyperboloid measure grows without bound (frame cutoff Lambda).
 [2] Lemma J: a jump of the form factor F at the null cone makes the retarded field
     of a monochromatic compact source log-divergent; continuous F stays finite.
 [3] e^{l^2 box} on timelike momenta: amplification exponents for physical processes.
 [4] gamma / Shapiro: Gaussian-smeared point mass, deflection and delay deficits.
 [5] Preferred-frame escape: order-of-magnitude vacuum photon production vs EBL.
 [6] GW170817 timing / emission factor for the preferred-frame causal smearing.
All numbers are printed; OMP threads limited by the caller.
"""
import math
import mpmath as mp
import numpy as np
from scipy import integrate, special

mp.mp.dps = 30
hbar = 1.054571817e-34
c = 2.99792458e8
G = 6.67430e-11
eV = 1.602176634e-19
hbarc_eVm = hbar * c / eV          # 1.97327e-7 eV m
lP2 = G * hbar / c**3             # Planck length squared

print("[1] Lemma V0: invariant measure of the shell p^2 = -s (s=1) inside |p|<Lambda")
for Lam in [1e1, 1e2, 1e3, 1e4]:
    # int_{|p|<Lam} d^3p / (2 E),  E = sqrt(p^2 + 1)
    N = math.pi * (Lam * math.sqrt(Lam**2 + 1) - math.asinh(Lam))
    print(f"    Lambda={Lam:8.0e}  N={N:.6e}  N/Lambda^2={N/Lam**2:.6f}")
# disjoint boosted copies of E={a<=p0<=b, pz>=0} on the s=1 shell: rapidities
a, b = 1.0, 2.0
eta = [0.0]
for _ in range(5):
    # need a*cosh(eta_next) > b*exp(eta_prev)
    target = b * math.exp(eta[-1]) / a
    eta.append(math.acosh(target) + 1e-9)
print("    rapidities giving pairwise-disjoint boosted copies:", [round(x, 4) for x in eta])
print("    => invariant measure >= sum of equal positive masses = infinite")

print()
print("[2] Lemma J: field of a monochromatic point source, w0=1, r=3, smooth cutoff K=40")
w0, r, K = mp.mpf(1), mp.mpf(3), mp.mpf(40)


def integrand(k, eps):
    d = k**2 - w0**2
    return k * mp.sin(k * r) * mp.e**(-(k / K)**2) * (d + 1j * eps) / (d**2 + eps**2)


def I_range(lo, hi, eps):
    pts = [lo, hi] if hi != mp.inf else [lo, lo + 1, lo + 5, mp.inf]
    return mp.quad(lambda k: integrand(k, eps), pts, maxdegree=10)


def F_smooth(k):
    # continuous at the null cone: F=1 for spacelike (k>w0), exp(-(w0^2-k^2)/mu^2) timelike
    s = w0**2 - k**2
    return mp.e**(-s / mp.mpf('0.05')) if s > 0 else mp.mpf(1)


for eps in [mp.mpf('1e-2'), mp.mpf('1e-4'), mp.mpf('1e-6'), mp.mpf('1e-8'), mp.mpf('1e-10')]:
    # jump: keep only spacelike k > w0 (F=0 timelike, F=1 spacelike)
    Ij = mp.quad(lambda k: integrand(k, eps), [w0, w0 + eps**0.5, w0 + 1, w0 + 5, mp.inf], maxdegree=10)
    # full retarded (F=1 everywhere)
    If = mp.quad(lambda k: integrand(k, eps), [0, w0 - 1e-3, w0 - eps**0.5, w0, w0 + eps**0.5, w0 + 1e-3, w0 + 5, mp.inf], maxdegree=10)
    # continuous F
    Ic = mp.quad(lambda k: F_smooth(k) * integrand(k, eps), [0, w0 - 0.3, w0 - eps**0.5, w0, w0 + eps**0.5, w0 + 1e-3, w0 + 5, mp.inf], maxdegree=10)
    print(f"    eps={float(eps):.0e}  jump: Re={float(Ij.real):+.5f} Im={float(Ij.imag):+.5f}"
          f" | full: Re={float(If.real):+.5f} Im={float(If.imag):+.5f}"
          f" | continuous F: Re={float(Ic.real):+.5f} Im={float(Ic.imag):+.5f}")
print(f"    predicted jump-log slope dRe/dln(1/eps) = +sin(w0 r)/2 * e^-(w0/K)^2 = {float(mp.sin(w0*r)/2*mp.e**(-(w0/K)**2)):+.5f}")
print("    observed slope from eps=1e-8 -> 1e-10:", f"{(0.70048-0.37574)/math.log(100):+.5f}")

print()
print("[3] e^{l^2 box}: |F|^2 = exp(2 l^2 s) at timelike s = (DeltaE/hbar c)^2")
procs = [("thermal IR photon pair, 0.05 eV", 0.05), ("optical transition, 2 eV", 2.0),
         ("K-shell X-ray, 10 keV", 1e4), ("e+e- threshold, 1.022 MeV", 1.022e6),
         ("nuclear gamma (Co-60), 1.17 MeV", 1.17e6)]
for ell in [1e-10, 4e-10, 1e-8, 1e-6, 5e-6]:
    row = []
    for name, E in procs:
        x = ell * E / hbarc_eVm
        row.append(f"{2*x*x:.3e}")
    print(f"    l={ell:.0e} m  exponents 2 l^2 s:", ", ".join(row))
print("    (processes:", "; ".join(p[0] for p in procs), ")")
Ethr = hbarc_eVm / 5e-6
print(f"    at l=5e-6 m the exponent exceeds 1 for DeltaE > hbar c/(sqrt2 l) = {Ethr/math.sqrt(2):.4f} eV")
# vacuum norm of e^{l^2 box} T at a point: int ds s^2 e^{2 l^2 s} diverges
for S in [10, 30, 100]:
    val = integrate.quad(lambda s: s**2 * math.exp(2 * s - 2 * S), 0, S)[0]
    print(f"    int_0^S ds s^2 e^(2 s) (l=1 units), S={S}: log10 = {math.log10(val) + 2*S/math.log(10):.1f}")

print()
print("[4] gamma and Shapiro for a Gaussian-smeared point mass (sigma = l per axis)")


def phi_smeared(rr, sig=1.0):  # units GM=1
    return -special.erf(rr / (math.sqrt(2) * sig)) / rr


def defl_ratio(bb, sig=1.0):
    # alpha = 2/c^2 int dPhi/db dz ; compare to point mass 2 * 2/b
    def dphidb(z):
        rr = math.hypot(bb, z)
        x = rr / (math.sqrt(2) * sig)
        dphidr = special.erf(x) / rr**2 - (2 / math.sqrt(math.pi)) * math.exp(-x * x) / (math.sqrt(2) * sig * rr)
        return dphidr * bb / rr
    val = 2 * integrate.quad(dphidb, 0, np.inf, limit=400)[0]
    return val / (2.0 / bb)


for bb in [1, 2, 3, 5, 8]:
    num = defl_ratio(bb)
    pred = 1 - math.exp(-bb**2 / 2)
    print(f"    b={bb} l: deflection/GR numeric={num:.10f}  1-exp(-b^2/2l^2)={pred:.10f}")
for bb in [3, 5, 8]:
    d = integrate.quad(lambda z: special.erfc(math.hypot(bb, z) / math.sqrt(2)) / math.hypot(bb, z), 0, np.inf, limit=400)[0]
    print(f"    b={bb} l: Shapiro excess int erfc/r dz (units GM/c^3 * 2) = {2*d:.3e}  (vs log term ~ 2 ln(4 r1 r2/b^2) ~ 50)")
Rsun = 6.957e8
for ell in [4e-10, 5e-6]:
    print(f"    Sun limb, l={ell:.0e}: exponent -b^2/(2 l^2) = {-(Rsun**2)/(2*ell**2):.3e}  => deficit 0 to any precision")

print()
print("[5] Preferred-frame escape: vacuum photon production, order of magnitude (SUGGESTED)")
tH = 4.35e17                      # s, ~ 1/H0 (recalled)
I_EBL = 6e-8                      # W m^-2 sr^-1, total EBL ~ 50-80 nW m^-2 sr^-1 (recalled)
u_EBL = 4 * math.pi * I_EBL / c
print(f"    u_EBL ~ 4 pi I/c = {u_EBL:.2e} J/m^3 (comparator, recalled)")
for Ap in [1e-4, 1e-2, 1.0]:
    for ell in [1e-10, 1e-9, 1e-8]:
        Edot = Ap * hbar * c**2 * lP2 / ell**7
        u = Edot * tH
        print(f"    A'={Ap:.0e} l={ell:.0e} m: Edot={Edot:.2e} W/m^3, u(t_H)={u:.2e} J/m^3, ratio to EBL={u/u_EBL:.1e}")
    lmin = (Ap * hbar * c**2 * lP2 * tH / u_EBL)**(1 / 7)
    print(f"    A'={Ap:.0e}: l_min (u_inj < u_EBL, tau=l/c) = {lmin:.2e} m; photon energy hbar c/l = {hbarc_eVm/lmin:.1f} eV")
print("    general tau: Edot ~ A' hbar c^2 lP^2 /(l^3 (c tau)^4) -> constrains l^3 tau^4")

print()
print("[6] Preferred-frame causal smearing C(w)=(1-i w tau)^-n, tau=l/c, n=2: GW emission factor")
for ell in [4e-10, 5e-6]:
    tau = ell / c
    for f in [100.0, 1000.0]:
        w = 2 * math.pi * f
        one_minus = -math.expm1(-(w * ell / c)**2 / 2 - math.log1p((w * tau)**2))
        Fmag = 1 - one_minus
        lag = 2 * tau
        print(f"    l={ell:.0e} f={f:.0f} Hz: 1-|F|={one_minus:.2e}, group lag ~ n tau = {lag:.2e} s (GW170817 window 1.74 s)")

print()
print("[7] Covariant Lemma K: K = D0 + cN^2 |F|^2 PJ/s^2 with PJ*D0' >= 1/4, D0 = D0'|F|^2  => K >= cN |F|^2/|s|")
rng = np.random.default_rng(83)
worst = np.inf
for _ in range(20000):
    s = rng.choice([-1, 1]) * 10**rng.uniform(-6, 6)      # timelike (+) or spacelike (-)
    F = 10**rng.uniform(-3, 0)
    cN = 10**rng.uniform(-2, 2)
    PJ = 10**rng.uniform(-8, 8)
    D0p = (1 / (4 * PJ)) * (1 + 10**rng.uniform(-6, 3))   # on or above the trade-off
    K = D0p * F**2 + cN**2 * F**2 * PJ / s**2
    worst = min(worst, K / (cN * F**2 / abs(s)))
print(f"    min K/(cN|F|^2/|s|) over 20000 draws (timelike and spacelike s) = {worst:.6f}")

print()
print("[9] Preferred-frame null-cone regulator mu (SUGGESTED, order of magnitude)")
rho_c = 8.5e-27 * c**2     # J/m^3, critical density (recalled)
OmGW = 1e-6                # N_eff-type bound on a GW background (recalled, order)
for Cgw in [1e-4, 1e-2, 1.0]:
    for ell in [1e-8, 5e-6]:
        # GW pumping per volume ~ Cgw * hbar c mu^2 / l^3 ; require * t_H < OmGW rho_c
        mu2max = OmGW * rho_c * ell**3 / (Cgw * hbar * c * tH)
        kopt = 2 * math.pi / 5e-7          # optical wavenumber for a log estimate
        logf = math.log(kopt**2 / mu2max)
        print(f"    Cgw={Cgw:.0e} l={ell:.0e}: mu^2 < {mu2max:.2e} m^-2 (1/mu > {1/math.sqrt(mu2max):.2e} m); null-cone log ln(k_opt^2/mu^2) = {logf:.0f}")
