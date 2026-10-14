"""NF-1 (c) sizes: the staggered law's multiplicative strain channel, and the controls' additive channels, on F2's rows.
Mapping = F1/F5's (f1_envscale.py, f5_sizes.py; canonical TT-pole reading CONDITIONAL, PRICE_NOTE:22; a = 1/M_P with G = a^2 built in;
SM mapping an ESTIMATE): mu_rho(channel) = R x 2.424e-21 eV^2 m^3/kg, R = ratio of the channel's matter coefficient to F1's.
  additive channel with Hessian H (e^2, SF units):           R = |H| / 2.42401e-2
  multiplicative channel z'' (dm = 1/2 m z'' t^2 per e^2):    R = (sum_q m_q <qbar q>_N / M_P) |z''| / (13 x 2.42401e-2)   (nucleons; F5's)
F2 rows (worker table, refereed with corrections: TESTS:9290-9296): Earth crossing 1.5e-29 (positive-mass sign checked), detector ~1e-29,
PTA 8e-24 (suggested), Galaxy+IGM 2.7e-19, binary pulsar 2e-43 (toy forecast).
argv: zpp_staggered L_G1 Hess_epsWilson(r_c=0.05) Hess_epsWilson(r_c=0.3)"""
import sys
import numpy as np
MP = 1.22089e19; HESS = 2.42401e-2; MU_F1 = 2.424e-21
ROWS = (('Earth crossing (row 1)', 1.5e-29), ('detector ground (row 2)', 1e-29), ('PTA (row 7, suggested)', 8e-24),
        ('Galaxy+IGM (row 5)', 2.7e-19), ('binary pulsar (row 8, toy)', 2e-43))
zpp, LG1, HW1, HW3 = (float(v) for v in sys.argv[1:5])
mN = 0.9383; spi, ss = 0.045, 0.040; heavy = 3*(2/27)*(mN - spi - ss); mqq = spi + ss + heavy   # RECALLED inputs, as f5_sizes.py
def show(lab, R, sign):
    mu = R*MU_F1
    print('%-62s R %.2e  mu_rho %.2e  (%s sign)' % (lab, R, mu, sign))
    print('      ' + ' ; '.join('%s x%.1e' % (nm, mu/b) for nm, b in ROWS))
print('reference F1 Wilson root channel: Hess_t +2.42401e-2, mu_rho 2.424e-21: Earth row x%.2e' % (MU_F1/1.5e-29))
R = (mqq/MP)*abs(zpp)/(13*HESS)
show("(c) staggered multiplicative z'' = %+.3e e^2 (nucleons)" % zpp, R, 'massive' if zpp > 0 else 'tachyonic')
show("    same, electrons (m_e/M_P weight)", (0.000511/MP)*abs(zpp)/HESS, 'massive' if zpp > 0 else 'tachyonic')
print('\ncontrols (additive channel re-admitted when eps is broken), mapped like F1:')
for a in (0.0141, 0.1, 1.0):
    H = 2*a*LG1
    show('  G1 dressing a = %.4f: Hess_t = 2aL = %+.3e' % (a, H), abs(H)/HESS, 'tachyonic' if H < 0 else 'massive')
for rc, H in ((0.05, HW1), (0.3, HW3)):
    show('  eps-Wilson r_c = %.2f: Hess_t = %+.3e' % (rc, H), abs(H)/HESS, 'tachyonic' if H < 0 else 'massive')
print('  precision to pass the Earth row with an eps-breaking term: |Hess_t| <= %.1e e^2' % (HESS*1.5e-29/MU_F1))
# hot era, multiplicative channel (F5's thermal mapping; quarks t, b, c; C_F g_s^2), same formula as f5_sizes.py
gs2 = 0.3
def Ha2(T, gs=106.75): return (8*np.pi/3)*(np.pi**2/30)*gs*(T/MP)**4
quarks = {'t': 172.69, 'b': 4.18, 'c': 1.27}
def ppbar(m, T):
    k = np.linspace(1e-4, 60*T + 10*m, 200001); E = np.sqrt(k*k + m*m)
    return 4*np.trapezoid(k*k/(2*np.pi**2)*m/E/(np.exp(np.minimum(E/T, 700)) + 1), k)
print('\nhot era, staggered multiplicative residual (one taste populated per SM quark; x2 if twins are thermal):')
for T in (150.0, 100.0, 10.0, 1.0):
    gs_ = 106.75 if T > 90 else 86.25
    mumu = sum(3*ppbar(m, T)/MP**3*(4/3)*gs2*(m/MP)*zpp for m in quarks.values())
    print('    T = %5.0f GeV: m_g^2/H^2 %+.2e' % (T, 16*np.pi*mumu/Ha2(T, gs_)))
