"""R19-34 (d): sizes of the Wilson psibar-psi strain channel on the ROOT's Dirac edge, through SM history and in today's matter.
Logic and SM mapping copied from R19-31's r1931_sizes.py part (C) (ESTIMATE: quarks t, b, c with C_F g_s^2, g_s^2 ~ 0.3 at the lattice
scale, RECALLED; electrons e^2 ~ 0.1; nucleons sigma-term weight ~13 light-quark units; one Dirac edge for all species, as the root uses);
canonical reading (conditional, PRICE_NOTE:22): m_g^2 a^2 = 16 pi mu_SF, mu_SF = mu_Hcov/4 (R19-31 sec. 1); bound line |m_g| < H, i.e.
16 pi |mu| < (H a)^2 (r1921_history.py:14-15). Coefficient: d2(dm)/dh2 per e^2 (H-cov):
  R18-9 root edge D1(0.909103708, 0.555604226) + Gph(2.9435): -0.040475 (r1934_root.out);  0+ root -0.040813;  naive Wilson r = 1: -0.06218.
Also: the m-linear (multiplicative) Hessian on the root edge z'' = -0.0717 per e^2 (r1934_onshell_check.out, slope of the on-shell Hessian
in m), which survives on chirally protected edges in kind (size there not computed; suggested same order)."""
import numpy as np
MP = 1.22089e19; gs2 = 0.3
def Ha2(T, gs=106.75): return (8*np.pi/3)*(np.pi**2/30)*gs*(T/MP)**4
quarks = {'t': 172.69, 'b': 4.18, 'c': 1.27}
def ppbar(m, T):
    k = np.linspace(1e-4, 60*T + 10*m, 200001); E = np.sqrt(k*k + m*m)
    return 4*np.trapezoid(k*k/(2*np.pi**2)*m/E/(np.exp(np.minimum(E/T, 700)) + 1), k)
for lab, c in (('naive Wilson r=1 (R19-31 control)', -0.0621), ('R18-9 root D1 + Gph', -0.040475), ('R19-11 0+ root D1 + Gph', -0.040813)):
    print('%s: d2dm/dh2 = %+.6f e^2' % (lab, c))
    for T in (150.0, 100.0, 50.0, 10.0, 1.0):
        mu = sum(3*ppbar(m, T)/MP**3*(4/3)*gs2*c/4 for m in quarks.values())
        gs_ = 106.75 if T > 90 else 86.25
        print('   T = %6.1f GeV: mu_SF = %+.3e  m_g^2/H^2 = %+.3e' % (T, mu, 16*np.pi*mu/Ha2(T, gs_)))
    lP = 1.616e-35; EP_eV = MP*1e9
    for where, n in (('IGM n ~ 0.25 /m^3', 0.25), ('Earth n ~ 3.3e30 /m^3', 3.3e30)):
        na3 = n*lP**3
        for who, w in (('electrons', 0.1), ('nucleons', 13*(4/3)*gs2)):
            mg2a2 = 16*np.pi*na3*w*abs(c)/4
            print('   today %-22s %-9s |m_g| = %.2e eV   (LVK 1.92e-23 eV; 100 Hz GW 4.1e-13 eV)' % (where, who, np.sqrt(mg2a2)*EP_eV))
c = -0.040475
print('\nTuning needed to bring the root-edge channel to the bound lines (|coefficient| allowed / actual):')
worst = 0
for T in (150.0, 100.0, 50.0, 10.0, 1.0):
    mu = sum(3*ppbar(m, T)/MP**3*(4/3)*gs2*c/4 for m in quarks.values()); gs_ = 106.75 if T > 90 else 86.25
    worst = max(worst, abs(16*np.pi*mu/Ha2(T, gs_)))
print('   history (|m_g| < H, worst T in list): %.1e' % (1/worst))
lP = 1.616e-35; EP_eV = MP*1e9
mE = np.sqrt(16*np.pi*3.3e30*lP**3*13*(4/3)*gs2*abs(c)/4)*EP_eV
print('   Earth (|m_g| below the 100 Hz GW energy 4.1e-13 eV): %.1e' % ((4.1e-13/mE)**2))
print('\nMultiplicative (m-linear) channel on the root edge, z\'\' = -0.0717 e^2: cross term <psibar psi>_th m_f z\'\' (top-dominated):')
for T in (150.0, 100.0, 50.0, 10.0, 1.0):
    mu = sum(3*ppbar(m, T)*(m/MP)/MP**3*(4/3)*gs2*(-0.0717)/4 for m in quarks.values()); gs_ = 106.75 if T > 90 else 86.25
    print('   T = %6.1f GeV: m_g^2/H^2 = %+.2e' % (T, 16*np.pi*mu/Ha2(T, gs_)))
