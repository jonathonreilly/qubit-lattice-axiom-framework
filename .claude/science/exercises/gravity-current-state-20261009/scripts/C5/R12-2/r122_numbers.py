"""R12-2 numbers: Lemma CR, creation geometry and noise, mixture estimator, EW kicks, isotropy.
Inputs RECALLED unless stated: H0 = 67.7 km/s/Mpc, Om = 0.31, Or = 9.1e-5, l_P = 1.616e-35 m,
M_P = 1.221e19 GeV, T0 = 2.35e-13 GeV, g*(EW) = 106.75, m_H = 125 GeV, v = 246 GeV.
"""
import itertools
import numpy as np
import sympy as sp
from scipy.integrate import quad

c = 2.998e8; lP = 1.616e-35; tP = 5.391e-44
H0 = 67.7e3 / 3.0857e22          # s^-1
Om, Orad = 0.31, 9.1e-5
OL = 1 - Om - Orad
E = lambda z: np.sqrt(Om * (1 + z) ** 3 + Orad * (1 + z) ** 4 + OL)
DC = lambda z: c / H0 * quad(lambda x: 1 / E(x), 0, z)[0]   # comoving distance, m

print('## (a) Lemma CR: fixed sites need |W| >= H R on a ball of proper radius R (cosmic slicing)')
for z in (0.5, 1.0, 1.6, 3.0, 1089.9):
    Rem = DC(z) / (1 + z)              # proper distance at emission
    HR = H0 * E(z) * Rem / c
    print(f'  z = {z:7.1f}: proper distance at emission {Rem/3.0857e22:9.2f} Mpc, H(z) R = {HR:7.3f}  (timelike fixed sites need < 1)')
Rlss = DC(1089.9)
print(f'  comoving distance to last scattering {Rlss/3.0857e22:.0f} Mpc; today H0*D = {H0*Rlss/c:.2f}')
print(f'  creation rate needed: 3H0 = {3*H0:.3e} /s per site = {3*H0*tP:.3e} per site per Planck time')

print('\n## (b) local Z^3-preserving insertion by dislocation climb: line density rho_L = 3H/(a v)')
for lab, H in (('today', H0), ('BBN (T~1 MeV, H~0.7/s RECALLED)', 0.7)):
    for v in (1.0, 1e-3):
        rhoL = 3 * H / (lP * v * c)
        print(f'  {lab}: climb speed {v:g} c -> line density {rhoL:.3e} m^-2, mean line spacing {rhoL**-0.5:.3e} m')

print('\n## (c) Poisson (Yule) insertion noise along a column; phase noise across a wavefront')
rng = np.random.default_rng(1)
N0, Ht, trials = 400, np.log(2.0), 4000
# Yule: each site independently splits at rate H; N(t) negative binomial
Ns = np.array([np.sum(rng.geometric(np.exp(-Ht), size=N0)) for _ in range(trials)])
print(f'  Yule MC: N0={N0}, e^Ht=2: mean {Ns.mean():.1f} (theory {N0*2:.0f}); var {Ns.var():.0f} (theory N0 e^Ht (e^Ht-1) = {N0*2*1:.0f})')
for z in (1.0, 4.0):
    Lem = DC(z) / (1 + z)
    N0c = Lem / lP
    dN = np.sqrt(N0c * (1 + z) * z)          # std of final column length (sites)
    dL = dN * lP
    print(f'  source z={z}: column at emission N0 = {N0c:.2e} sites; std of final length {dL:.2e} m '
          f'(sqrt(l_P D_C) = {np.sqrt(lP*DC(z)):.2e} m)')
    for lab, lam in (('radio 1 cm', 1e-2), ('optical 500 nm', 5e-7), ('X-ray 1 keV', 1.24e-9), ('gamma 1 GeV', 1.24e-15)):
        print(f'      {lab:15s}: phase std 2 pi dL/lambda = {2*np.pi*dL/lam:.2e} rad')
lam = 1.24e-9
print(f'  X-ray: per-column std must be < lambda/(2 pi l_P) = {lam/(2*np.pi*lP):.2e} sites; Poisson gives {np.sqrt(DC(1.0)/lP):.2e}'
      f' -> variance suppression needed {(lam/(2*np.pi*lP))**2/(DC(1.0)/lP):.2e} of Poisson')

print('\n## (d) equation-of-state rule H^2 = (rho+p)/(1+cs2) on mixtures (kappa/3 = 1)')
r = sp.symbols('rho1:4', positive=True); w = sp.symbols('w1:4', real=True)
S = sum((1 + wi) * ri for wi, ri in zip(w, r)); D2 = sum((1 + wi) ** 2 * ri for wi, ri in zip(w, r))
pdot_over_rhodot = sum(wi * (1 + wi) * ri for wi, ri in zip(w, r)) / S
est = sp.simplify(S / (1 + pdot_over_rhodot))
print('  estimator - S^2/sum(1+w)^2 rho =', sp.simplify(est - S ** 2 / D2), '(0 => estimator = S^2/D2 <= sum rho by Cauchy-Schwarz)')
Rgrid = np.logspace(-3, 3, 20001)
ratio = (4 / 3 + Rgrid) ** 2 / ((16 / 9 + Rgrid) * (1 + Rgrid))
i = np.argmin(ratio)
print(f'  radiation+dust: min estimator/true = {ratio[i]:.5f} at rho_m/rho_r = {Rgrid[i]:.3f}  (H low by {100*(1-np.sqrt(ratio[i])):.2f}%)')
for wD in (-0.95, -0.9, -0.75, -0.5, 0.0):
    rm, rD = 0.31, 0.69
    est = (rm + (1 + wD) * rD) ** 2 / (rm + (1 + wD) ** 2 * rD)
    print(f'  dust + DE(w={wD:+.2f}), Om=0.31: estimator/true today = {est/(rm+rD):.3f}')
# LCDM target under E-rule: S' = -3 S^2/rho_T  =>  rho_D' = 3 (rho_m - S)
us = np.linspace(np.log(1e-3), 0.0, 20001)
rhoT = Om * np.exp(-3 * us) + OL
rhom = Om * np.exp(-3 * us)
g = -3 * OL / (rhoT * rhom)                      # d(1/S - 1/rho_m)/du, smooth
dlt = np.concatenate(([0.0], np.cumsum(0.5 * (g[1:] + g[:-1]) * np.diff(us))))
Sv = rhom / (1 + rhom * dlt)
diff = rhom ** 2 * dlt / (1 + rhom * dlt)          # rho_m - S, exact rearrangement
rhoD_change = 3 * np.concatenate(([0.0], np.cumsum(0.5 * (diff[1:] + diff[:-1]) * np.diff(us))))
print(f'  LCDM target via E-rule (start S = rho_m at z=999): (rho+p)_D today = {Sv[-1]-rhom[-1]:.3f} rho_c0, '
      f'change in rho_D since z=999 = {rhoD_change[-1]:+.3f} rho_c0 (negative => needs rho_D,i >= {-rhoD_change[-1]:.3f} rho_c0 early)')

print('\n## (e) phase-transition sizes (inputs RECALLED)')
GeV4_rhoL = 0.69 * 8.096e-47 * 0.677 ** 2
dV = 125.0 ** 2 * 246.0 ** 2 / 8
T = 160.0; gs = 106.75
rho_r = np.pi ** 2 / 30 * gs * T ** 4
print(f'  rho_Lambda = {GeV4_rhoL:.3e} GeV^4; Delta V_EW = m_H^2 v^2/8 = {dV:.3e} GeV^4 = {dV/GeV4_rhoL:.2e} rho_Lambda')
print(f'  rho_r(T=160 GeV) = {rho_r:.3e} GeV^4; Delta/rho = {dV/rho_r:.3e}')
# R-law curvature kick X = -kappa Delta/3 ; |Omega_K| today
MP = 1.221e19; H0GeV = 6.582e-25 * H0
HT = np.sqrt(8 * np.pi * rho_r / 3) / MP
aT = 2.35e-13 / T * (3.91 / gs) ** (1 / 3)
OmK_T = dV / rho_r
OmK_0 = OmK_T * (aT * HT) ** 2 / (H0GeV) ** 2
print(f'  R-law kick: |Omega_K| at EW = {OmK_T:.2e}; grown to today |Omega_K0| = {OmK_0:.2e} (DESI DR2 10^3 Omega_K = 2.3 +- 1.1)')
print(f'  R-law closed-radiation freeze: a_max/a_T = sqrt(rho_r/Delta) = {np.sqrt(rho_r/dV):.1f} -> T_freeze ~ {T/np.sqrt(rho_r/dV):.1f} GeV')
Tf = (dV / (np.pi ** 2 / 30 * 90)) ** 0.25
print(f'  A/U rules mistuned by Delta_EW: freeze (or Lambda-domination) when rho_r ~ Delta: T ~ {Tf:.0f} GeV; '
      f'de Sitter branch H = {np.sqrt(8*np.pi*dV/3)/MP:.2e} GeV = 1/({6.582e-25/(np.sqrt(8*np.pi*dV/3)/MP):.2e} s)')

print('\n## (f) cubic covariance -> isotropic mean expansion tensor (Schur, O_h on symmetric rank 2)')
mats = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3))
        for i, j in enumerate(perm):
            M[i, j] = signs[i]
        mats.append(M)
A = rng.normal(size=(3, 3)); A = A + A.T
avg = sum(M @ A @ M.T for M in mats) / len(mats)
print(f'  |O_h| = {len(mats)}; group average of random symmetric A = trace/3 * I: residual {np.abs(avg - np.trace(A)/3*np.eye(3)).max():.1e}')

print('\n## (g) grid zero-point under the equation-of-state rule (R11-3 numbers, refereed CONFIRMED WITH CORRECTIONS)')
for lab, rp in (('L, m=1', 2.0683), ('G, m=1', 1.8492), ('NN, m=1', 1.3991)):
    H = np.sqrt(8 * np.pi / 3 * rp)   # Planck units, a = l_P, per real scalar, cs2 -> 0 bound
    print(f'  {lab}: (rho+p)_vac = {rp} /a^4 -> H >= sqrt(8 pi/3 (rho+p)/(1+cs2)) ~ {H/np.sqrt(2):.2f}-{H:.2f} / t_P per real scalar')
print('  finite-step U ratio Delta p/Delta rho in [-0.833, -0.175] across L-G (R11-3 referee finding 5): Delta(rho+p) != 0 for every profile')
