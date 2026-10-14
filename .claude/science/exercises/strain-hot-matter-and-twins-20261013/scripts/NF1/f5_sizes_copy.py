"""F5 (b)/(c) arithmetic: residual strain channels after P-R19-34a, against F2's rows (C5_F2_report.md:95-106), and the
knock-on onto the R18-9 root's vacuum rows.  Mapping = F1's (f1_sizes.py / f1_envscale.py, canonical reading, conditional,
PRICE_NOTE:22; SM mapping an ESTIMATE): mu_SF = sum <psibar psi> a^3 x coupling x Hess_t; F1's channel has mu_rho = 2.424e-21
eV^2 m^3/kg (f1_envscale.out:1) for Hess_t = 2.42401e-2 and the nucleon weight 13 light-quark units x C_F g_s^2.
Each residual is expressed as a ratio R to F1's channel for the same matter, then mu_rho(residual) = R x 2.424e-21.
Inputs computed here: z''_t (f5_mult_*.out), e_m, d dm along nn (f5_nn_*.out).  RECALLED inputs are marked."""
import numpy as np, sys
MP = 1.22089e19                      # GeV, a = 1/M_P (non-reduced), as F1/R19-34
HESS = 2.42401e-2                    # F1 B1, e^2 units, SF
MU_F1 = 2.424e-21                    # F1 mu_rho (eV^2 m^3/kg), nucleon-dominated
EARTH, PTA, GAL = 1.5e-29, 8e-24, 2.7e-19     # F2 rows 1, 7, 5
zpp = float(sys.argv[1]) if len(sys.argv) > 1 else -4.6e-3    # z''_t per e^2 (f5_mult)
print('F1 channel: Hess_t %+.4e e^2, mu_rho %.3e, Earth row ratio %.2e' % (HESS, MU_F1, MU_F1/EARTH))
print('\n(b) residual channels after the rule (ratio R to F1 channel, mu_rho = R x %.3e; Earth row 1.5e-29):' % MU_F1)
# (i) multiplicative: per nucleon sum_q m_q <N|qbar q|N> (RECALLED: sigma_piN ~ 0.045, sigma_s ~ 0.04 GeV; heavy c,b,t each
#     (2/27)(m_N - sigma_piN - sigma_s) by the trace anomaly) against 13 light-quark units of <qbar q> for F1's channel
mN = 0.9383; spi, ss = 0.045, 0.040
heavy = 3*(2/27)*(mN - spi - ss)
mqq = spi + ss + heavy
R_i_N = (mqq/MP)*abs(zpp)/(13*HESS)
R_i_e = (0.000511/MP)*abs(zpp)/HESS
print('  (i) multiplicative m_f z\'\' <psibar psi>: z\'\'_t = %+.2e e^2 (SF, off-shell estimate); sum_q m_q<qbar q>_N = %.3f GeV'
      % (zpp, mqq))
print('      nucleons R = %.2e -> mu_rho %.1e (Earth row ratio %.1e);  electrons R = %.2e' % (R_i_N, R_i_N*MU_F1, R_i_N*MU_F1/EARTH, R_i_e))
# speed/kinetic rows of matter (not fixed by the rule; P-R19-31c territory): <p^2/E> of quarks in a nucleon ~ 0.3 GeV (ESTIMATE)
for kpp in (0.01, 0.1, 1.0):
    R = (0.3/MP)*kpp/(13*HESS)
    print('  (i\') matter speed rows, kappa\'\'_t = %.2f e^2 (bracket, not computed): R = %.1e -> mu_rho %.1e (Earth ratio %.1e)' % (kpp, R, R*MU_F1, R*MU_F1/EARTH))
# (ii) Pauli/clover term from F3's dressing: energy per fully polarized electron in B: 8|a| (m_e l_P) mu_B B per unit t^2 (F3 sec 4)
muB, B = 5.788e-5, 5e-5               # eV/T, Earth field 50 microtesla (RECALLED)
for a in (0.0141, 1.0):
    num = 8*a*(0.000511/MP)*muB*B      # eV
    den = 0.1*HESS*MP*1e9              # eV: F1 channel per electron (e^2 = 0.1)
    print('  (ii) Pauli term, dressing |a| = %.4f, fully polarized electrons in 50 uT: R <= %.1e' % (a, num/den))
# (iii) photon: Ward => no mass at any strain (proved for the generalized-link law at every t); medium EM energy x kappa_gamma''
for kg in (1e-3, 1e-1):
    R = (2.2e-3/MP)*kg/(13*0.4*HESS)   # nuclear Coulomb ~2.2 MeV/nucleon (Fe, RECALLED semi-empirical a_C = 0.711 MeV)
    print('  (iii) photon kinetic strain response x nuclear Coulomb energy, kappa_g\'\' = %.0e: R = %.1e -> mu_rho %.1e' % (kg, R, R*MU_F1))
# (iv) Higgs-sector channels (R19-21, count once): matter shifts v; Wilson c1 slope.  |m_g| IGM 1.42e-9 eV (vR19-21 item 4),
#      Earth ~5 MeV (Wilson) / 0.02 eV (even part) (rR19-21:211, suggested)
rho_igm, rho_e = 0.0224*1.878e-29*1e3, 5500.0          # kg/m^3 (r1921_history.py:72)
for lab, mg, rho in (('IGM, Wilson c1 (vR19-21 item 4, arithmetic confirmed)', 1.42e-9, rho_igm),
                     ('Earth, Wilson c1 (rR19-21:211, suggested)', 5e6, rho_e), ('Earth, even part (rR19-21:211, suggested)', 0.02, rho_e)):
    mur = mg**2/rho
    print('  (iv) %-52s |m_g| %.2e eV -> mu_rho %.1e : Earth row x%.1e, Galaxy/IGM row x%.1e' % (lab, mg, mur, mur/EARTH, mur/GAL))
# hot era, multiplicative channel (top-dominated), F1's thermal mapping
gs2 = 0.3
def Ha2(T, gs=106.75): return (8*np.pi/3)*(np.pi**2/30)*gs*(T/MP)**4
quarks = {'t': 172.69, 'b': 4.18, 'c': 1.27}
def ppbar(m, T):
    k = np.linspace(1e-4, 60*T + 10*m, 200001); E = np.sqrt(k*k + m*m)
    return 4*np.trapezoid(k*k/(2*np.pi**2)*m/E/(np.exp(np.minimum(E/T, 700)) + 1), k)
print('\n  hot era (F1 mapping; quarks t, b, c; C_F g_s^2):')
for T in (150.0, 100.0, 10.0, 1.0):
    gs_ = 106.75 if T > 90 else 86.25
    muF1 = sum(3*ppbar(m, T)/MP**3*(4/3)*gs2*HESS for m in quarks.values())
    mumu = sum(3*ppbar(m, T)/MP**3*(4/3)*gs2*(m/MP)*zpp for m in quarks.values())
    print('    T = %5.0f GeV: F1 channel m_g^2/H^2 %+.2e ; multiplicative residual %+.2e' % (T, 16*np.pi*muF1/Ha2(T, gs_), 16*np.pi*mumu/Ha2(T, gs_)))
