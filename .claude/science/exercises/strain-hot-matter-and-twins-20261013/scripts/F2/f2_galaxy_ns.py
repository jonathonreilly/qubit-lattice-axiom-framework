"""F2 cases (ii) Sun / Galaxy / IGM, (iii) binary pulsars, (v) static potentials (conditional).
All bounds expressed on mu_rho = |m_g^2|/rho [eV^2 m^3/kg] (m^2 proportional to density, non-relativistic matter).

(ii-a) LVK dispersion (GWTC-4.0 m_g <= 1.92e-23 eV, LIGO-P2500066 as cited in vR19-21:26): int m^2 dl <= m_LVK^2 D_0,
       column = IGM (n_b (1+z)^3-weighted, D_0 ~ 1.5 Gpc) + Milky Way (N_H ~ 1e21 cm^-2) + host (~1e21 cm^-2).  Both branches.
(ii-b) GW170817 speed (ApJL 848 L13: GRB 1.74 s after GW; emission lag <= 10 s assumed there): c dt = mu_rho Sigma /(2 (hbar w)^2).
(ii-c) PTA band (branch M): a medium with m(n) > omega is evanescent; the Earth sits in the Local Bubble (n ~ 0.005 cm^-3,
       ~100 pc). Observed nHz common process with HD correlation (NANOGrav 15-yr ApJL 951 L8, ~3 sigma HD; EPTA, PPTA, CPTA)
       down to f_min ~ 1/(16 yr) -> m(n_LB) <= omega_min ~ 8.2e-24 eV (Wu et al. 2023 arXiv:2310.07469 vacuum version).
(ii-d) Sun: no detected event's path crossed the Sun (expected number ~ N_events x 5.4e-6) -> no bound.
(iii)  Binary pulsar (branch M): reciprocity -- far-zone amplitude = int Psi_in tau_ij; the medium mass term screens Psi_in inside
       each star.  Born: 1 - s = (mu_rho/(hbar c)^2) <|Phi_N|>/(4 pi G), <|Phi_N|> = 2|W|/M (mass-averaged potential).
       Circular binary: matter stress and field stress each carry half the oscillating TT source -> amplitude x (1+s)/2,
       power x ~ 1 - (1 - s).  Double pulsar: Pb-dot/GR agrees to 1.3e-4 (95%; Kramer et al. 2021 PRX 11 041050).
       Hard-sphere limit (m R >> 1): exact static exterior/interior matching, s computed.
(v)    Static potential, CONDITIONAL on trace/scalar content of the stiffness (not supplied by the E_g Hessian):
       same Born formula for the Sun's Psi -> Cassini |gamma - 1| < 2.3e-5.
"""
import numpy as np
from f2_common import MU_RHO_PLACEHOLDER, hbarc, hbar, m_u, G, Msun, Mpc, c_light, yr

P = MU_RHO_PLACEHOLDER
print('placeholder mu_rho = %.3e eV^2 m^3/kg' % P)

print('\n(ii-a) LVK GWTC-4.0 dispersion, column-density version')
mL = 1.92e-23; D0 = 1.5e3 * Mpc
SigIGM = 0.253 * 1.5 * D0 * m_u          # kg/m^2 (rough (1+z)^3 weighting factor 1.5)
SigMW = 1e25 * m_u; SigHost = 1e25 * m_u
Sig = SigIGM + SigMW + SigHost
mu_b = mL**2 * D0 / Sig
print('  Sigma: IGM %.2e + MW %.2e + host %.2e = %.2e kg/m^2' % (SigIGM, SigMW, SigHost, Sig))
print('  mu_rho <= %.2e  (|m_g| at IGM mean %.2e eV; at ISM 1/cc %.2e eV); placeholder/bound = %.2e'
      % (mu_b, np.sqrt(mu_b * 0.253 * m_u), np.sqrt(mu_b * 1e6 * m_u), P / mu_b))
print('  placeholder path-averaged |m_g| = sqrt(mu Sigma / D0) = %.2e eV vs 1.92e-23' % np.sqrt(P * Sig / D0))

print('\n(ii-b) GW170817 arrival time')
Sig817 = (0.253 * 40 * Mpc + 8e24) * m_u
w100 = 2 * np.pi * hbar * 100
mu_t = 2 * w100**2 * c_light * 10.0 / Sig817
print('  Sigma(NGC 4993 path) = %.2e kg/m^2; mu_rho <= %.2e (weak); placeholder delay at 100 Hz = %.2e s'
      % (Sig817, mu_t, P * Sig817 / (2 * w100**2) / c_light))
mu_d817 = (9.51e-22)**2 * 40 * Mpc / Sig817
print('  GW170817 dispersion (9.51e-22 eV at 40 Mpc) on the extragalactic+MW column: mu_rho <= %.2e (weak)' % mu_d817)

print('\n(ii-c) PTA band, branch M (Local Bubble)')
wmin = 8.2e-24
for nLB in (1e3, 5e3, 1e5):
    rho = nLB * m_u
    mu_p = wmin**2 / rho
    m_ph = np.sqrt(P * rho)
    kap = np.sqrt(max(m_ph**2 - wmin**2, 0)) / hbarc
    print('  n = %.0e /m3: bound mu_rho <= %.2e; placeholder |m_g| = %.2e eV (x%.1f omega_min), kappa*100pc = %.2e; placeholder/bound = %.1e'
          % (nLB, mu_p, m_ph, m_ph / wmin, kap * 100 * 3.0857e16, P / mu_p))
f_cut = np.sqrt(P * 5e3 * m_u) / (2 * np.pi * hbar)
print('  placeholder: nHz GWs below f = %.2e Hz (= 1/%.1f yr) evanescent in Local-Bubble gas' % (f_cut, 1 / f_cut / yr))
# heliosphere check: m ~ 1/r, int m dr from 0.01 AU to 100 AU
AU = 1.496e11
m1 = np.sqrt(P * 5e6 * m_u)
print('  heliosphere (solar wind 5/cc at 1 AU, n ~ r^-2): int m dr/hbarc over 0.01-100 AU = %.2e (thin)' % (m1 * AU * np.log(1e4) / hbarc))

print('\n(iii) binary pulsar screening')
GMc2 = G * Msun / c_light**2
M_ns, R_ns = 1.3, 12e3
C = M_ns * GMc2 / R_ns
phi_avg = 1.5 * G * M_ns * Msun / R_ns     # n = 1 polytrope: |W| = (3/4) GM^2/R -> <|Phi|> = 1.5 GM/R
x = 1.3e-4
mu_ns = x * 4 * np.pi * G / phi_avg * hbarc**2
rho_c = 3 * M_ns * Msun / (4 * np.pi * R_ns**3)
print('  NS: M = %.1f Msun, R = %.0f km, compactness %.3f, <|Phi|>/c^2 = %.3f, mean rho = %.2e kg/m3' % (M_ns, R_ns / 1e3, C, phi_avg / c_light**2, rho_c))
print('  Born: 1 - s = mu_rho <|Phi|>/(4 pi G (hbar c)^2);  |1 - s| <= 1.3e-4  ->  mu_rho <= %.2e eV^2 m^3/kg' % mu_ns)
print('        equivalently |m_g| at mean NS density <= %.2e eV (m R = %.3f); at 5500 kg/m3 <= %.2e eV'
      % (np.sqrt(mu_ns * rho_c), np.sqrt(mu_ns * rho_c) * R_ns / hbarc, np.sqrt(mu_ns * 5500)))
mR = np.sqrt(P * rho_c) * R_ns / hbarc
# exact uniform sphere, static: inside Psi = A sinh(m r)/r, outside 1 - b/r; mass-weighted mean of Psi
def s_uniform(mR):
    if mR < 1e-3:
        return 1 - 0.4 * mR**2
    # matching: Psi(R) = A sinh(mR)/R = 1 - b/R ; Psi'(R): A (m cosh - sinh/R)/R = b/R^2
    # -> A = 1/(m cosh(mR))  (exterior derivative condition gives Psi(R) = tanh(mR)/(mR))
    # mass-weighted mean: (3/R^3) int_0^R A sinh(m r)/r r^2 dr = 3 A (mR cosh mR - sinh mR)/(m^2 R^3)
    if mR > 300:
        return 3 * (mR - 1) / mR**3   # s = 3(mR - tanh mR)/(mR)^3
    A_over = 1 / np.cosh(mR)
    return 3 * A_over * (mR * np.cosh(mR) - np.sinh(mR)) / mR**3
for mr in (1e-2, 0.1, 1, 10, 100, mR):
    s = s_uniform(mr)
    print('  uniform sphere m R = %.3e: s = %.4e -> power factor ((1+s)/2)^2 = %.4f' % (mr, s, ((1 + s) / 2)**2))
print('  placeholder at NS density: |m_g| = %.2e eV, m R = %.2e -> Pb-dot changed by ~%.0f%% (matter coupling screened; self-field O(C) corrections not computed)'
      % (np.sqrt(P * rho_c), mR, 100 * (1 - ((1 + s_uniform(mR)) / 2)**2)))
print('  placeholder/bound = %.1e' % (P / mu_ns))

print('\n(v) static potential (CONDITIONAL on trace content)')
phi_sun = 3 * G * Msun / 6.957e8      # n = 3 polytrope |W| = 1.5 GM^2/R
mu_v = 2.3e-5 * 4 * np.pi * G / phi_sun * hbarc**2
print('  Sun <|Phi|>/c^2 = %.2e; Cassini |gamma-1| < 2.3e-5 -> mu_rho <= %.2e (if the stiffness screens Psi); placeholder/bound = %.1e'
      % (phi_sun / c_light**2, mu_v, P / mu_v))
print('  placeholder in the Sun: |m_g| (mean rho 1410) = %.2e eV, m R_sun = %.2e (hard sphere if trace content exists)'
      % (np.sqrt(P * 1410), np.sqrt(P * 1410) * 6.957e8 / hbarc))
