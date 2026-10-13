"""F6 (b)-(c): assemble c_H = d2_t Sigma_H(P=0) a^2 (SF units, per real Higgs component, counterterm fixed at t = 0) from the checked
loop Hessians, convert to vev shifts, and read against the clock row (NANOGrav background, f6_drift.out) and F2's rows through the
Higgs-induced vacuum stiffness.  SM mapping = ESTIMATE (couplings RECALLED); a = l_P; |t| = |h_+| (reading, pheno T2).
Loop Hessians (lattice units; sources in comments)."""
import numpy as np
HG = {'R18-9': 2.43452e-3, '0+': 6.80969e-4}          # loop 1 per e^2 (f6_gauge.out:4-6,15)
HL = {'R18-9': -2.674816e-3, '0+': -2.721567e-3}      # d2_t G_s (f6_gauge.out:23-27)
HY = {}                                              # loop 3 per N_c y_t^2, filled from f6_yuk_*.out
import json, os
if os.path.exists('f6_hy.json'):
    HY = json.load(open('f6_hy.json'))
MP = 1.22089e19; mH = 125.1; v = 246.22; fN = 0.30           # GeV (RECALLED; M_P as rR19-21:71)
NC = 3
coup = {   # lattice-scale couplings, RECALLED (labelled ESTIMATE): g^2, g'^2, y_t, lam
    'Planck-scale SM (RECALLED)': (0.26, 0.21, 0.38, -0.013),
    'R19-31 gauge values, y_t=0.5, lam=0': (0.25, 0.20, 0.50, 0.0),
    'low-scale SM (bracket)': (0.42, 0.13, 0.94, 0.13),
}
conv_v = MP**2/(2*mH**2)                      # |delta v/v| per unit (c_H Q_E)
print('|delta v/v| = c_H M_P^2/(2 m_H^2) Q_E  ->  M_P^2/(2 m_H^2) = %.4e' % conv_v)
drift = {'LS slope, f_min 1/16yr, T_obs 10 yr (smallest)': 7.670e-30, 'LS slope, f_min 1/16yr, T_obs 5 yr': 2.074e-29,
         'rms dQ/dt f<1/(5yr), f_min 1/16yr': 5.920e-29, 'rms dQ/dt f<1/(5yr), f_min 1/30yr (largest)': 1.023e-28}   # f6_drift.out
bound = 3.6e-17           # |d ln(m_p/m_e)/dt| per yr (Lange et al. 2021, 1 sigma; TESTS F6)
kmu = abs(fN - 1.0)       # d ln(m_p/m_e)/d ln v (m_e ~ v; m_p ~ v^{f_N}), ESTIMATE
rho_conv = 5.60959e35*(1.97327e-7)**3   # kg/m^3 -> eV^4
muF2 = {'Earth crossing (F2 row 1; referee-confirmed for the massive sign)': 1.5e-29, 'Galaxy/IGM LVK column (F2 row 5)': 2.7e-19,
        'PTA (F2 row 7, massive sign, suggested)': 8e-24}
for root in ('R18-9', '0+'):
    for br, hy in HY.get(root, {}).items():
        for lab, (g2, gp2, yt, lam) in coup.items():
            Cg = 0.75*g2 + 0.25*gp2
            parts = (Cg*HG[root], NC*yt**2*hy, 6*lam*HL[root])
            cH = sum(parts)
            print('[%s | %s | %s] c_H = %+.4e  (gauge %+.3e, top %+.3e, quartic %+.3e)' % (root, br, lab, cH, *parts))
            dvv = cH*conv_v
            print('     delta v/v = %+.3e x Q_E   (sign: c_H > 0 raises the mass parameter, v falls)' % (-dvv))
            rates = [kmu*abs(dvv)*r for r in drift.values()]
            print('     clock |d ln(m_p/m_e)/dt| = %.2e .. %.2e /yr (4 drift estimators) -> x%.1e .. x%.1e over %.1e/yr'
                  % (min(rates), max(rates), min(rates)/bound, max(rates)/bound, bound))
            amin = np.sqrt(max(rates)/bound)
            print('     a needed to pass the clock row (clock rate ~ (l_P/a)^2): a >= %.1e l_P (smallest drift: %.1e l_P)' % (amin, np.sqrt(min(rates)/bound)))
            mur = 16*np.pi*fN*abs(cH)*rho_conv/(mH*1e9)**2
            sign = 'tachyonic' if cH > 0 else 'massive'
            mgE = np.sqrt(16*np.pi*fN*abs(cH)*5500*rho_conv/(mH*1e9)**2)
            print('     Higgs-induced vacuum stiffness in matter: mu_rho = 16 pi f_N |c_H|/m_H^2 = %.3e eV^2 m^3/kg (%s; a-independent); Earth |m_g| = %.2e eV'
                  % (mur, sign, mgE))
            print('        ' + '; '.join('%s x%.1e' % (k.split(' (')[0], mur/b) for k, b in muF2.items()))
            if lab.startswith('Planck'):
                lamstar = -(Cg*HG[root] + NC*yt**2*hy)/(6*HL[root])
                print('     coupling zero (U=1 pieces fixed): lam* = %+.3f at the lattice scale (SM lam(M_P) ~ -0.01, RECALLED)' % lamstar)
# fermion control (F1's channel, same clock estimator; F1 mapping e^2 = 0.1, nucleon weight 5.2 = 13 x C_F g_s^2 (rF1:248-251))
HF = 2.42401e-2
dme = 0.5*0.1*HF*MP/0.51099895e-3; dmN = 0.5*5.2*HF*MP/0.938272
print('control, fermion additive channel (F1, uncorrected): d ln m_e/dQ = %.3e, d ln m_N/dQ = %.3e -> d ln(m_p/m_e)/dQ = %.3e' % (dme, dmN, dmN - dme))
rates = [abs(dmN - dme)*r for r in drift.values()]
print('     clock: %.2e .. %.2e /yr -> x%.1e .. x%.1e  (panel/pheno expectation ~2e8, pheno_statement.md:181)' % (min(rates), max(rates), min(rates)/bound, max(rates)/bound))
# dressing: can F3's (G1, G2) dressing zero BOTH the fermion additive Hessian and c_H?  (Planck-scale couplings, R18-9 Y-a B1)
L1, L2 = -8.585830e-01, -1.502128e+00          # F3 fermion responses (f3_astar.out:1-2)
dY1, dY2 = -8.67699331e-01, 2.68378829e-01     # Yukawa responses (f6_yuk_a.out:7-8)
HF1 = 2.424011e-2
g2, gp2, yt, lam = coup['Planck-scale SM (RECALLED)']
cH0 = (0.75*g2 + 0.25*gp2)*HG['R18-9'] + NC*yt**2*HY['R18-9']['Y-a B1, U=1 (main)'] + 6*lam*HL['R18-9']
Amat = np.array([[2*L1, 2*L2], [NC*yt**2*2*dY1, NC*yt**2*2*dY2]]); rhs = -np.array([HF1, cH0])
sol = np.linalg.solve(Amat, rhs)
print('dressing: G1 alone zeroes c_H at a = %.4e (fermion zero at a* = 1.4116e-2); G1+G2 zero both at (a1, a2) = (%.4e, %.4e) -- a 2-number tuning'
      % (-cH0/(NC*yt**2*2*dY1), sol[0], sol[1]))
# tadpole channel (outside the pre-registered Sigma_H): delta v/v = -(1/2)(y_t/sqrt2) N_c (d2_t C) M_P^3/(m_H^2 v) Q_E
if os.path.exists('f6_tad.json'):
    TD = json.load(open('f6_tad.json'))
    print('TADPOLE channel (outside the pre-registered Sigma_H; vectorlike-Wilson Yukawa map m_f = y_f h/sqrt2 as rR19-21 BO):')
    for br, d2C in TD.items():
        for yt in (0.38, 0.94):
            dvv = 0.5*(yt/np.sqrt(2))*NC*abs(d2C)*MP**3/(mH**2*v)
            print('tadpole [%s, y_t = %.2f]: d2_t <psibar psi>_vac = %+.4e per field -> |delta v/v| = %.2e x Q_E; clock (smallest drift) x%.1e'
                  % (br, yt, d2C, dvv, kmu*dvv*7.670e-30/bound))
