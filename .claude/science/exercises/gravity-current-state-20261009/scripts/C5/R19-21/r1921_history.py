"""R19-21 (a),(b),(d),(e): the shear mismatch Delta mu(T) = mu_state - mu_lowest on R19-11's 0+ root edges, by channel, against H(T),
plus today's matter channel. Lattice units (a = l_P, m a = m / M_P, M_P = 1.22089e19 GeV as R19-11).
Inputs (refereed, R19-11 + verdict; archived runner outputs rechecked identical):
  Wilson-Dirac per field (fitres_root0_dense.out): mu_E c1 +1.06932e-2, c2 +6.6e-3 ; mu_T2 c1 +2.73929e-3, c2 +2.19e-3
  twisted-mass Dirac per field (twfit.out):        mu_E c2 +8.5643e-3 ; mu_T2 c2 -3.8315e-6 (odd orders vanish)
  scalar edge per scalar: mu_E c2 -1.36080e-3, mu_T2 0 (Liouville S1);  vector edge per vector: mu_E c2 -2.99321e-3, mu_T2 0
Channels (derivations in the report, section 3.1):
  V  (vev shift):  Delta mu = sum_s n_s [c1_s m_s a (x - 1) + c2_s (m_s a)^2 (x^2 - 1)],  x = v(T)/v.
       T > T_c: x = 0. T < T_c: linear response dx = -(2/(v^2 m_H^2)) sum_s m_s^2 dF_s/dm^2 (valid for |dx| << 1; RECALLED SM inputs),
       dF/dm^2 = (g/2)<n_B/eps> per bosonic species with g real dof, = 2<n_F/eps> per Dirac field (4 dof).
  F  (thermal Higgs fluctuations x lattice sea; checked mechanism in r1921_nn_thermal.py):
       Delta mu = 4 <dphi_1^2>_th * sum_s n_s c2_s kappa_s a^2,   kappa_s = (m_s/v)^2,  <dphi^2>_th = <n_B/eps> per real component.
  Q  (thermal quasiparticles' own lattice shear): 0.206 (T a)^6 per massless bosonic dof (checked r1921_nn_thermal.py), counted once with C4 W2.
Bound for 'no tensor-mode mass/instability faster than H' (canonical reading, conditional): 16 pi |Delta mu| < (H a)^2,
  (H a)^2 = (8 pi/3)(pi^2/30) g*(T) (T a)^4 (radiation era, RECALLED g*)."""
import numpy as np
from scipy.integrate import quad
MP = 1.22089e19; v = 246.22; mH = 125.25
dirac = {'t': (172.69, 3), 'b': (4.18, 3), 'c': (1.27, 3), 's': (0.0934, 3), 'd': (0.00467, 3), 'u': (0.00216, 3),
         'tau': (1.77686, 1), 'mu': (0.10566, 1), 'e': (0.000511, 1)}                 # RECALLED (as R19-11)
bos = {'W': (80.377, 6), 'Z': (91.1876, 3), 'H': (mH, 1)}                            # real dof (unitary-gauge counting, for dx only)
scal = [mH, 80.377, 80.377, 91.1876]; vecs = [80.377, 80.377, 91.1876]               # R19-11 Feynman-gauge bookkeeping for the rows
C = {'W': {'E': (1.06932e-2, 6.6e-3), 'T': (2.73929e-3, 2.19e-3)}, 'tw': {'E': (0.0, 8.5643e-3), 'T': (0.0, -3.8315e-6)}}
cS = {'E': -1.36080e-3, 'T': 0.0}; cV = {'E': -2.99321e-3, 'T': 0.0}
S1 = sum(n*m for m, n in dirac.values())/MP; S2 = sum(n*m*m for m, n in dirac.values())/MP**2
S2s = sum(m*m for m in scal)/MP**2; S2v = sum(m*m for m in vecs)/MP**2
print('R19-11 sums reproduced: sum n m a = %.4e (4.395e-17), sum n (ma)^2 = %.4e (6.0e-34), scalar %.4e (2.48e-34), vector %.4e (1.42e-34)' % (S1, S2, S2s, S2v))
def R2(edge, r):   # sum_s n_s c2_s (m_s a)^2 for row r
    return C[edge][r][1]*S2 + cS[r]*S2s + cV[r]*S2v
def dmu_V(x, edge, r):
    return C[edge][r][0]*S1*(x - 1) + R2(edge, r)*(x*x - 1)
print('\n(a) symmetric phase (x = 0): Delta mu_vac = mu(m->0) - mu(m_SM)')
for edge in ('W', 'tw'):
    print('  %-7s  mu_E %+.4e   mu_T2 %+.4e' % ({'W': 'Wilson', 'tw': 'twisted'}[edge], dmu_V(0, edge, 'E'), dmu_V(0, edge, 'T')))
def Jb(m, T):   # <n_B/eps> in GeV^2 (continuum: T << 1/a)
    if m/T > 60: return 0.0
    f = lambda k: k*k/np.sqrt(k*k + m*m)/np.expm1(np.sqrt(k*k + m*m)/T)
    return quad(f, 0, 60*T + 10*m, limit=200)[0]/(2*np.pi**2)
def Jf(m, T):
    if m/T > 60: return 0.0
    f = lambda k: k*k/np.sqrt(k*k + m*m)/(np.exp(np.sqrt(k*k + m*m)/T) + 1)
    return quad(f, 0, 60*T + 10*m, limit=200)[0]/(2*np.pi**2)
def dx_lin(T):
    s = sum(m*m*(g/2)*Jb(m, T) for m, g in bos.values()) + sum(m*m*n*2*Jf(m, T) for m, n in dirac.values())
    return -2*s/(v*v*mH*mH)
def gstar(T):   # RECALLED step approximation
    for Tt, g in ((170, 106.75), (90, 96.25), (5, 86.25), (1.5, 75.75), (0.2, 61.75), (0.1, 17.25), (5e-4, 10.75)):
        if T > Tt: return g
    return 3.36
def Ha2(T): return (8*np.pi/3)*(np.pi**2/30)*gstar(T)*(T/MP)**4
Tc = 159.5   # RECALLED SM crossover temperature (lattice studies), used only as the switch point
print('\n(b) history: m_g^2/H^2 = 16 pi Delta mu/(H a)^2 by channel (sign: + massive, - tachyonic). x = v(T)/v.')
print('  T[GeV]     x        | V Wilson mu_E   V Wilson mu_T2 | V twisted mu_E  V twisted mu_T2 | F(tw c2) mu_E   F(tw c2) mu_T2   F(W c2) mu_T2 | Q (g* dof)')
for T in (1e16, 1e12, 1e8, 1e4, 1e3, 300, 170, 150, 100, 50, 20, 10, 5, 2, 1):
    if T > Tc: x = 0.0
    else: x = 1 + dx_lin(T)
    out = []
    for edge, r in (('W', 'E'), ('W', 'T'), ('tw', 'E'), ('tw', 'T')):
        out.append(16*np.pi*dmu_V(x, edge, r)/Ha2(T))
    # F channel: Higgs fluctuations; above Tc massless-ish with thermal mass^2 ~ 0.4 T^2 (RECALLED c_h), below Tc mass mH
    mfl = np.sqrt(0.4)*T if T > Tc else mH
    phi2 = Jb(mfl, T)/MP**2
    for edge, r in (('tw', 'E'), ('tw', 'T'), ('W', 'T')):
        R2r = R2(edge, r) if edge == 'tw' else C['W']['T'][1]*S2
        out.append(16*np.pi*4*phi2*R2r/(v/MP)**2/Ha2(T))
    Q = 16*np.pi*0.206*(T/MP)**6*gstar(T)/Ha2(T)
    print('  %-9.3g %-8.5f | %+.2e       %+.2e      | %+.2e       %+.2e      | %+.2e       %+.2e        %+.2e     | %+.1e' % ((T, x) + tuple(out) + (Q,)), flush=True)
print('  (x below T_c from linear response; it is crude within a factor ~2 near T_c, where the crossover is non-perturbative (RECALLED).)')
print('\n(d)/(e) today, matter channel: d v/v = -f_N rho/(v^2 m_H^2), f_N = 0.30 (RECALLED Higgs-nucleon coupling); omega(100 Hz) = 4.14e-13 eV;')
print('  GW graviton-mass bound m_g <~ 1.3e-23 eV (RECALLED, LVK dispersion). Positive Delta mu = massive, negative = tachyonic (sign = -sign(slope)).')
GeV4_per_gcm3 = 5.61e23*(1.973e-14)**3      # 1 g/cm^3 in GeV^4  (1 g = 5.61e23 GeV; 1 cm^-1 = 1.973e-14 GeV)
for name, rho in (('mean IGM baryons (Omega_b h^2 = 0.0224)', 0.0224*1.878e-29), ('galactic ISM, n_H ~ 1 cm^-3', 1.67e-24), ('Earth, 5.5 g/cm^3', 5.5)):
    dx = -0.30*rho*GeV4_per_gcm3/(v*v*mH*mH)
    for edge, r in (('W', 'E'), ('W', 'T'), ('tw', 'E'), ('tw', 'T')):
        d = C[edge][r][0]*S1*dx + R2(edge, r)*2*dx
        mg = np.sqrt(16*np.pi*abs(d))*MP*1e9
        print('  %-42s dv/v %+.2e  %-7s %-4s: Delta mu %+.2e -> |m_g| = %.2e eV (%s); |m_g|/omega_100Hz = %.1e; /bound = %.1e'
              % (name, dx, {'W': 'Wilson', 'tw': 'twisted'}[edge], 'mu_' + r, d, mg, 'massive' if d > 0 else 'tachyonic', mg/4.14e-13, mg/1.3e-23))
print('\n(e) mass-blind requirement: |sum_k c_k sum n (m a)^k (dx)| < (H a)^2/(16 pi)  ->  the slope combinations must vanish to:')
for name, T, dx in (('T_c (160 GeV, x: 1 -> 0)', 160.0, -1.0), ('1 GeV (dx linear response)', 1.0, dx_lin(1.0))):
    lim = Ha2(T)/(16*np.pi)
    print('  %-30s (Ha)^2/16pi = %.2e, dx = %.2e: |c1| < %.1e (vs 1.07e-2: tuning %.0e),  |c2| < %.1e (vs 8.6e-3: %.0e)'
          % (name, lim, dx, lim/(S1*abs(dx)), lim/(S1*abs(dx))/1.07e-2, lim/(2*S2*abs(dx)), lim/(2*S2*abs(dx))/8.6e-3))
dxI = -0.30*0.0224*1.878e-29*GeV4_per_gcm3/(v*v*mH*mH); limI = (1.3e-23*1e-9/MP)**2/(16*np.pi)
print('  %-30s (m_g,bound a)^2/16pi = %.2e, dx = %.2e: |c1| < %.1e (tuning %.0e), |c2| < %.1e (tuning %.0e)'
      % ('today, IGM (GW mass bound)', limI, dxI, limI/(S1*abs(dxI)), limI/(S1*abs(dxI))/1.07e-2, limI/(2*S2*abs(dxI)), limI/(2*S2*abs(dxI))/8.6e-3))
