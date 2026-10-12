"""P1: species sum rules for mu_E, order by order, with SM-like content, against the P0 level.
Coefficients from p1_coeffs.npz (p1_mu_species.py).  All flow-coupled, taste-singlet species are w * F(lam * m):
   real KG component (Higgs, each massive-vector polarisation, photon/gluon polarisation in option A): w=+1, lam=1
   staggered field (2 Dirac tastes, symbol 1/2 sin 2p): w=-1/2, lam=2;  per-Dirac proxy: w=-1/4, lam=2
   naive-dispersion boson (bosonic doublers):            w=+1/2, lam=2
so  sum_i mu_i = sum_n c_n sum_i w_i (lam_i m_i)^n  (+ c6L log), and the rules are
   R0: sum w = 0;  R2: sum w lam^2 m^2 = 0;  R4: sum w lam^4 m^4 = 0;  R6: sum w (lam m)^6 [c6L ln(lam m) + c6] = 0.
"""
import numpy as np
d = np.load('/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/P1/p1_coeffs.npz')
c0, c2, c4, c6L, c6 = [float(d[k]) for k in ['c0', 'c2', 'c4', 'c6L', 'c6']]
g0, b0 = float(d['g0']), float(d['b0'])
print(f'F coefficients: c0={c0:+.6e} c2={c2:+.6e} c4={c4:+.6e} c6L={c6L:+.6e} c6={c6:+.6e}')
print(f'non-universal lattice ratios: naive(sin p) G(0)/F(0) = {g0/c0:.6f};  metric scalar F_B(0)/F(0) = {b0/c0:.6f}; photon B/A = {b0/c0:.6f}')

print('\nper-species weights at each order, relative to one real KG component (flow coupling):')
print('  order n :   0        2        4        6 (x [c6L ln(lam m) + c6])')
for name, w, lam in [('real KG component', 1, 1), ('staggered field (2 Dirac)', -0.5, 2), ('per Dirac (proxy)', -0.25, 2),
                     ('per fermionic d.o.f.', -1/16, 2), ('naive field, 1/2 sin2p (8 Dirac)', -2, 2), ('naive-dispersion boson', 0.5, 2)]:
    print(f'  {name:32s}' + ''.join(f'{w*lam**n:+9.4f}' for n in [0, 2, 4, 6]))

# SM content after EWSB, unitary gauge.  Masses in GeV (PDG-like, quoted from memory).
bos = [('gluons (8x2 pol)', 16, 0.0), ('photon (2 pol)', 2, 0.0), ('W+- (2x3 pol)', 6, 80.377), ('Z (3 pol)', 3, 91.1876), ('Higgs', 1, 125.25)]
ferm = [('t', 3, 172.69), ('b', 3, 4.18), ('c', 3, 1.27), ('s', 3, 0.093), ('d', 3, 0.00467), ('u', 3, 0.00216),
        ('tau', 1, 1.77686), ('mu', 1, 0.105658), ('e', 1, 0.000511), ('nu (3, Dirac proxy)', 3, 5e-11)]
species = [(n, k*1.0, 1, m) for n, k, m in bos] + [(n, -0.25*k, 2, m) for n, k, m in ferm]

def moments(ainv):
    out = {}
    for n in [0, 2, 4]:
        out[n] = [w*(lam*m/ainv)**n for _, w, lam, m in species]
    out[6] = [w*(lam*m/ainv)**6*(c6L*np.log(lam*m/ainv) + c6) if m > 0 else 0.0 for _, w, lam, m in species]
    return out

print('\nSM content (unitary gauge; fermions as per-Dirac proxies of staggered fields; gauge bosons option A):')
W0 = sum(w for _, w, _, _ in species)
nB = sum(w for _, w, _, _ in species if w > 0); nF = -sum(w for _, w, _, _ in species if w < 0)
print(f'  R0: sum w = {nB:.3f} (bosons) - {nF:.3f} (fermions) = {W0:+.3f}  ->  sum c0 = {W0*c0:+.4e} per site = {W0:.2f} x natural')
print(f'      R0 would need {4*nB:.0f} Dirac fermions for these bosons, or {nF:.3f} bosonic KG components for these fermions')
print(f'      with Weyl neutrinos (1.5 Dirac): {nB - (nF - 0.75*0.25*0 - 0.375):+.3f}')
GeV2 = {n: sum(w*(lam*m)**n for _, w, lam, m in species) for n in [2, 4]}
B2 = sum(w*(lam*m)**2 for _, w, lam, m in species if w > 0); F2 = -sum(w*(lam*m)**2 for _, w, lam, m in species if w < 0)
B4 = sum(w*(lam*m)**4 for _, w, lam, m in species if w > 0); F4 = -sum(w*(lam*m)**4 for _, w, lam, m in species if w < 0)
print(f'  R2: sum w lam^2 m^2 = {B2:.1f} - {F2:.1f} = {GeV2[2]:+.1f} GeV^2  (relative {GeV2[2]/max(B2, F2):+.3f}; per Dirac weight -1 x m^2, per boson dof +1)')
print(f'  R4: sum w lam^4 m^4 = {B4:.4e} - {F4:.4e} = {GeV2[4]:+.4e} GeV^4  (= Pauli Str M^4 per d.o.f.; relative {GeV2[4]/max(B4, F4):+.3f})')

for label, ainv, target in [('framework a^-1 = M_Pl = 1.221e19 GeV; P0 bound 1.08e-104', 1.221e19, 1.08e-104),
                            ('refereed a^-1 = reduced M_Pl = 2.435e18 GeV; P0 bound 5.7e-99 x 1.2e-3 = 6.8e-102', 2.435e18, 6.84e-102)]:
    print(f'\n  {label}  (identification of normalisations = reading)')
    mo = moments(ainv)
    for n, cn in [(0, c0), (2, c2), (4, c4), (6, 1.0)]:
        terms = np.array(mo[n])*cn
        tot = terms.sum(); big = np.abs(terms).max()
        prec = target/big if big > 0 else np.inf
        print(f'    order {n}: residual sum = {tot:+.3e}; largest single term = {big:.3e}; '
              f'needed cancellation precision (target/largest) = {prec:.1e}; residual/target = {abs(tot)/target:.1e}')
    t8 = max(abs(w)*(lam*m/ainv)**8 for _, w, lam, m in species)*1e-3*40
    print(f'    order 8 estimate (|c8| ~ 1e-3 x ln): {t8:.1e} -> {"negligible" if t8 < target*1e-3 else "needed"}')

# pairings that solve every order identically
print('\nexact pairings (all orders): KG component of mass 2m  <->  2 staggered fields of mass m:'
      f'  F(2m) - 2*(1/2)F(2m) = 0;  naive-dispersion boson (m) <-> staggered field (m): 1/2F(2m) - 1/2F(2m) = 0')
print('IR d.o.f. per pair: KG pairing 1 boson vs 16 fermionic; naive-boson pairing 8 vs 8 (bosonic doublers, I3).')

# interactions: one-loop size estimate
print('\none-loop interaction estimate: delta mu ~ kappa (g^2/16 pi^2) c0, kappa = O(1) (suggested, not computed)')
for name, g2 in [('alpha_em(M_Pl)~1/40 (e^2=4pi alpha)', 4*np.pi/40), ('alpha_s(M_Pl)~1/45', 4*np.pi/45), ('y_t(M_Pl)~0.4', 0.16), ('lambda_H(M_Pl)~0.01', 0.01)]:
    e = g2/(16*np.pi**2)*c0
    print(f'  {name:36s}: g^2/16pi^2 = {g2/(16*np.pi**2):.1e} -> delta mu ~ {e:.1e} per species = {e/1.08e-104:.1e} x P0 bound;'
          f' loop orders of exact cancellation needed ~ {np.log(1.08e-104/c0)/np.log(g2/(16*np.pi**2)):.0f}')
# broken-SUSY residual
for MS in [1e3, 1e4]:
    r = abs(c2)*(MS/1.221e19)**2
    print(f'  exact pairing broken by splitting Delta m^2 ~ ({MS:.0e} GeV)^2: R2 residual ~ |c2| Delta(m^2 a^2) = {r:.1e} = {r/1.08e-104:.1e} x P0 bound')
mmax = np.sqrt(1.08e-104/abs(c2))*1.221e19
print(f'  R2 alone tolerates only |sum w Delta m^2| <= {mmax**2:.1e} GeV^2 (i.e. splittings sqrt = {mmax:.1e} GeV) summed over all species')
