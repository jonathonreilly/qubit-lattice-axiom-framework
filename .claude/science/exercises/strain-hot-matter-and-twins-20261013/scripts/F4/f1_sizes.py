"""F1 (c): sizes of the SF additive-mass strain channel through SM history and in today's matter.
Mapping = R19-34's (copied from r1934_sizes.py, itself from r1931_sizes.py part C; ESTIMATE: quarks t, b, c with C_F g_s^2, g_s^2 ~ 0.3
at the lattice scale, RECALLED; electrons e^2 ~ 0.1; nucleons sigma-term weight ~13 light-quark units; one Dirac edge for all species).
Canonical reading (conditional, PRICE_NOTE:22): m_g^2 a^2 = 16 pi mu_SF,  mu_SF = <psibar psi> a^3 x coupling x d^2(dm)/dt^2 (SF units t);
R19-34 enters c_h = d^2(dm)/dh^2 (H-cov) with mu_SF = c_h/4; here c_h := 4 Hess_t (identical formula).  Bound lines as R19-21/31/34:
|m_g| < H (history; r1921_history.py:14-15), LVK 1.92e-23 eV (vacuum, propagation), 100 Hz GW energy 4.1e-13 eV (in-medium; needs F2).
Sun: mean density 1.41 g/cm^3 (n_N ~ 8.4e29 /m^3), core 150 g/cm^3 (n_N ~ 9e31 /m^3), RECALLED; electrons taken at the nucleon density
as R19-34 did for the Earth (an overestimate by ~1.2-2 in n_e, i.e. <= 1.4 in |m_g|)."""
import numpy as np
MP = 1.22089e19; gs2 = 0.3
def Ha2(T, gs=106.75): return (8*np.pi/3)*(np.pi**2/30)*gs*(T/MP)**4
quarks = {'t': 172.69, 'b': 4.18, 'c': 1.27}
def ppbar(m, T):
    k = np.linspace(1e-4, 60*T + 10*m, 200001); E = np.sqrt(k*k + m*m)
    return 4*np.trapezoid(k*k/(2*np.pi**2)*m/E/(np.exp(np.minimum(E/T, 700)) + 1), k)
rows = (('H-cov R19-34 root (control)', -0.040475/4), ('SF B1 root D1(0.909103708,0.555604226)', 2.42401e-2))
import sys
for a in sys.argv[1:]:
    lab, v = a.rsplit('=', 1)
    rows = rows + ((lab, float(v)),)
lP = 1.616e-35; EP_eV = MP*1e9
for lab, Ht in rows:
    c = 4*Ht
    print('%s: Hess_t = %+.6e e^2  (c_h = 4 Hess_t = %+.6e)' % (lab, Ht, c))
    for T in (150.0, 100.0, 50.0, 10.0, 1.0):
        mu = sum(3*ppbar(m, T)/MP**3*(4/3)*gs2*c/4 for m in quarks.values())
        gs_ = 106.75 if T > 90 else 86.25
        print('   T = %6.1f GeV: mu_SF = %+.3e  m_g^2/H^2 = %+.3e' % (T, mu, 16*np.pi*mu/Ha2(T, gs_)))
    for where, n in (('IGM n ~ 0.25 /m^3', 0.25), ('Sun mean n ~ 8.4e29 /m^3', 8.4e29), ('Earth n ~ 3.3e30 /m^3', 3.3e30), ('Sun core n ~ 9e31 /m^3', 9e31)):
        na3 = n*lP**3
        for who, w in (('electrons', 0.1), ('nucleons', 13*(4/3)*gs2)):
            mg2a2 = 16*np.pi*na3*w*abs(c)/4
            print('   today %-26s %-9s |m_g| = %.2e eV' % (where, who, np.sqrt(mg2a2)*EP_eV))
    worst = 0
    for T in (150.0, 100.0, 50.0, 10.0, 1.0):
        mu = sum(3*ppbar(m, T)/MP**3*(4/3)*gs2*c/4 for m in quarks.values()); gs_ = 106.75 if T > 90 else 86.25
        worst = max(worst, abs(16*np.pi*mu/Ha2(T, gs_)))
    mE = np.sqrt(16*np.pi*3.3e30*lP**3*13*(4/3)*gs2*abs(c)/4)*EP_eV
    print('   tuning to the lines: history %.1e ; Earth (vs 4.1e-13 eV) %.1e' % (1/worst, (4.1e-13/mE)**2))
