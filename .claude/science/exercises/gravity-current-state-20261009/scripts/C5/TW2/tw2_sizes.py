"""TW-2 (c), (d), (e): needed splittings and the leak's sizes on F2's rows (F1/NF-1 mapping) and on F6's clock row.
Inputs (argv, from tw2_conv_*.out, per e^2, SF units): Lpp_Eg = A'' - B'' (Eg), Lpp_tet = A'' - B'' (tet), Lp_tet = A' - B' (tet), zpp = A''.
Light twin of a pair (l, h): m = (m_h + m_l)/2, sigma = (m_h - m_l)/2; dm_l(t) = m_l [A] + sigma [A - B];  heavy: dm_h = m_h [A] - sigma [A - B].
Mapping (F1/NF-1, CONDITIONAL canonical TT-pole reading, PRICE_NOTE:22, a = 1/M_P with G = a^2; SM mapping an ESTIMATE, as f1_sizes.py:1-6):
  F1's channel: nucleon weight 13 light-quark units x C_F g_s^2 x Hess_F1 (2.42401e-2 M_P) -> mu_rho = 2.424e-21 eV^2 m^3/kg (Earth row x1.62e8).
  Leak: nucleon weight W_N = sum_q <N|qbar q|N> (+-sigma_q) [light +, heavy -]; R = (W_N/M_P) Lpp / (13 Hess_F1); mu_rho = R x 2.424e-21.
  <N|qbar q|N> (RECALLED/ESTIMATE): u, d: 6.6 each (sigma_piN = 45 MeV, m_hat = 3.42 MeV); s: sigma_s/m_s = 0.040/0.0934;
  heavy Q: (2/27)(m_N - sigma_piN - sigma_s)/m_Q (trace anomaly), also for the vector-like partners.
Clock row (F6, f6_drift.py; pre-registered: NANOGrav 15-yr A = 2.4e-15, gamma = 13/3; bound |d ln(m_p/m_e)/dt| < 3.6e-17 /yr):
  Hessian part: d ln(m_p/m_e)/dQ_E x drift(Q_E), drift 7.67e-30 .. 1.02e-28 /yr (f6_drift.out);
  linear part (new): d ln(m_p/m_e)/dt_tet x slope of ONE orthonormal traceless component (t_tet = -h_E2/sqrt 2), computed here.
Couplings at the lattice scale (ESTIMATE, F1's): electrons e^2 = 0.1; quarks C_F g_s^2 = 0.4."""
import numpy as np, sys
Lpp_Eg, Lpp_tet, Lp_tet, zpp = (float(v) for v in sys.argv[1:5])
MP = 1.22089e19; HESS = 2.42401e-2; MU_F1 = 2.424e-21
ROWS = (('Earth crossing (row 1)', 1.5e-29), ('detector ground (row 2)', 1e-29), ('PTA (row 7, suggested)', 8e-24),
        ('Galaxy+IGM (row 5)', 2.7e-19), ('binary pulsar (row 8, toy forecast)', 2e-43))
me, mmu, mtau = 0.000511, 0.10566, 1.77686
mu_, md, ms, mc, mb, mt = 0.00216, 0.00467, 0.0934, 1.27, 4.18, 172.69
mN, spiN, ss = 0.9383, 0.045, 0.040
def qq(m):           # heavy-quark nucleon content
    return (2/27)*(mN - spiN - ss)/m
print('(c) needed taste splittings sigma = (m_heavy - m_light)/2 (RECALLED PDG masses, GeV), and sigma a = sigma/M_P:')
def pairs(mVLq, mVLl, mnup):
    return {'(e, mu)': (me, mmu), '(nu_e, nu_mu)': (0.0, 0.0), '(u, c)': (mu_, mc), '(d, s)': (md, ms),
            '(tau, tau\')': (mtau, mVLl), '(t, t\')': (mt, mVLq), '(b, b\')': (mb, mVLq), '(nu_tau, nu\')': (0.0, mnup)}
for k, (ml, mh) in pairs(1500.0, 1000.0, 50.0).items():
    sg = (mh - ml)/2
    print('   %-14s m_l %.4g  m_h %.4g  sigma %.4g GeV  sigma a %.2e  sigma/m_l %s' % (k, ml, mh, sg, sg/MP, ('%.3g' % (sg/ml)) if ml > 0 else '-'))
print('   (third-family partners: vector-like quark 1.5 TeV, lepton 1.0 TeV, nu\' 50 GeV > M_Z/2 as placeholders; LHC/LEP limits RECALLED)')


def W_N(mVLq):
    P = pairs(mVLq, 1000.0, 50.0)
    ql = {'(u, c)': (6.6, qq(mc)), '(d, s)': (6.6, ss/ms), '(t, t\')': (qq(mt), qq(mVLq)), '(b, b\')': (qq(mb), qq(mVLq))}
    tot = 0.0; parts = {}
    for k, (nl, nh) in ql.items():
        ml, mh = P[k]; sg = (mh - ml)/2
        parts[k] = sg*(nl - nh); tot += parts[k]
    return tot, parts


for mVL in (1000.0, 1500.0, 3000.0):
    tot, parts = W_N(mVL)
    print('   nucleon leak weight W_N (m_VLq = %.0f GeV) = %.3f GeV: %s' % (mVL, tot, ', '.join('%s %+.3f' % kv for kv in parts.items())))
WN, _ = W_N(1500.0)
mq_weight = spiN + ss + 3*(2/27)*(mN - spiN - ss)          # NF-1's multiplicative weight sum m_q <qbar q>
print('   compare: NF-1 multiplicative weight sum_q m_q<qbar q>_N = %.3f GeV (x z\'\'); F1 additive weight 13 x M_P' % mq_weight)

print('\n(d) Hessian leak on F2\'s rows (nucleons; R = (W_N/M_P) Lpp/(13 Hess_F1)):')
for lab, Lpp in (('Eg  (B1 under D4[001])', Lpp_Eg), ('tet (A1 under D4[001])', Lpp_tet)):
    R = (WN/MP)*abs(Lpp)/(13*HESS); mu = R*MU_F1
    print('   %s: Lpp = %+.4e e^2 -> R %.2e, mu_rho %.2e eV^2 m^3/kg (%s sign)' % (lab, Lpp, R, mu, 'massive' if Lpp*WN > 0 else 'tachyonic'))
    print('      ' + ' ; '.join('%s x%.1e' % (nm, mu/b) for nm, b in ROWS))
Re = (mmu - me)/2/MP*abs(Lpp_Eg)/HESS; mu_e = Re*MU_F1*(5.0e-10/3.6e-9)**2
print('   electrons (pair (e, mu), F1 electron weight e^2 at n_e = n_N, f1_sizes.out): mu_rho %.2e (Earth row x%.1e)' % (mu_e, mu_e/1.5e-29))
# hot era (F1 thermal mapping; quarks with their pair splittings)
gs2 = 0.3
def Ha2(T, gs=106.75): return (8*np.pi/3)*(np.pi**2/30)*gs*(T/MP)**4
def ppbar(m, T):
    k = np.linspace(1e-4, 60*T + 10*m, 200001); E = np.sqrt(k*k + m*m)
    return 4*np.trapezoid(k*k/(2*np.pi**2)*m/E/(np.exp(np.minimum(E/T, 700)) + 1), k)
print('   hot era (F1 mapping, quark pairs (u,c),(d,s),(b,b\'),(t,t\'); light +sigma, heavy -sigma):')
for T in (150.0, 100.0, 10.0, 1.0):
    gs_ = 106.75 if T > 90 else 86.25
    mu = 0.0
    for (ml, mh) in ((mu_, mc), (md, ms), (mb, 1500.0), (mt, 1500.0)):
        sg = (mh - ml)/2
        mu += 3*(ppbar(ml, T) - ppbar(mh, T))/MP**3*(4/3)*gs2*(sg/MP)*Lpp_Eg
    print('      T = %5.0f GeV: m_g^2/H^2 %+.2e' % (T, 16*np.pi*mu/Ha2(T, gs_)))

print('\n(d) clock row (F6 estimator; bound 3.6e-17 /yr):')
dlnme = 0.5*0.1*Lpp_Eg*(mmu - me)/2/me + 0.5*0.1*zpp
dlnmp = 0.5*0.4*Lpp_Eg*WN/mN
dQ = (7.670e-30, 1.023e-28)
print('   Hessian (Eg): d ln m_e/dQ_E %+.3e (leak + NF-1 multiplicative), d ln m_p/dQ_E %+.3e -> d ln(m_p/m_e)/dQ_E %+.3e' % (dlnme, dlnmp, dlnmp - dlnme))
print('      rate %.1e .. %.1e /yr -> x%.1e .. x%.1e of the clock row' % (abs(dlnmp - dlnme)*dQ[0], abs(dlnmp - dlnme)*dQ[1],
                                                                       abs(dlnmp - dlnme)*dQ[0]/3.6e-17, abs(dlnmp - dlnme)*dQ[1]/3.6e-17))
# linear: single-component slope under the NANOGrav background (f6_drift.py spectrum, C instead of C^2)
A_, gam = 2.4e-15, 13/3
alpha_ = (3 - gam)/2
def comp_slope(fmin, Tobs, fmax=50.0, nf=4000, nt=801):
    f = np.exp(np.linspace(np.log(fmin), np.log(fmax), nf)); hc2 = (A_*f**alpha_)**2; S = 0.4*hc2/f; lnf = np.log(f)
    def integ(y, mask=None):
        if mask is not None:
            y = np.where(mask, y, 0.0)
        return float(np.sum(0.5*(y[1:] + y[:-1])*np.diff(lnf)))
    tau = np.linspace(-Tobs/2, Tobs/2, nt); dg = np.linspace(0, Tobs, nt)
    Cg = np.array([integ(S*f*np.cos(2*np.pi*f*dd)) for dd in dg])
    C = np.interp(np.abs(tau[:, None] - tau[None, :]), dg, Cg)
    wts = np.full(nt, tau[1] - tau[0]); wts[0] *= 0.5; wts[-1] *= 0.5
    slope = np.sqrt((wts[:, None]*wts[None, :]*tau[:, None]*tau[None, :]*C).sum())*12/Tobs**3
    hdot = np.sqrt(integ((2*np.pi*f)**2*S*f, f < 1/Tobs))
    return np.sqrt(integ(S*f)), slope, hdot
for lab, me_on in (('leptons+quarks', 1), ):
    dlnme1 = 0.1*Lp_tet*(mmu - me)/2/me
    for mVL in (1000.0, 1500.0, 3000.0):
        wn, _ = W_N(mVL)
        dlnmp1 = 0.4*Lp_tet*wn/mN
        print('   linear (tet, along the splitting axis), m_VLq = %4.0f GeV: d ln m_e/dt %+.3f, d ln m_p/dt %+.3f -> d ln(m_p/m_e)/dt_tet %+.3f'
              % (mVL, dlnme1, dlnmp1, dlnmp1 - dlnme1))
    k1 = abs(0.4*Lp_tet*W_N(1500.0)[0]/mN - dlnme1)/np.sqrt(2)
    for fmin_yr in (16.0, 30.0):
        for Tobs in (10.0, 5.0):
            sa, sl, hd = comp_slope(1/fmin_yr, Tobs)
            print('      f_min 1/(%2.0f yr), T_obs %4.1f yr: sigma_a %.3e, LS slope of one component %.3e /yr, rms hdot(f<1/T) %.3e /yr -> rate %.1e .. %.1e /yr = x%.1f .. x%.1f of the clock row (m_VLq 1.5 TeV)'
                  % (fmin_yr, Tobs, sa, sl, hd, k1*sl, k1*hd, k1*sl/3.6e-17, k1*hd/3.6e-17))
    for nm, kk in (('electron side alone', abs(dlnme1)/np.sqrt(2)), ('proton side alone (1.5 TeV)', abs(0.4*Lp_tet*W_N(1500.0)[0]/mN)/np.sqrt(2))):
        sa, sl, hd = comp_slope(1/16.0, 10.0)
        print('      %s: x%.1f of the clock row (f_min 1/16 yr, T_obs 10 yr, LS slope)' % (nm, kk*sl/3.6e-17))

print('\n(e) a grid-scale third-family twin (no light 4th family): m_b\' a = s, sigma = s M_P/2; Earth row via <bbar b>_N:')
for sa_ in (1e-8, 1e-6, 1e-4, 1e-2, 0.3):
    wb = qq(mb)*sa_*MP/2
    R = (wb/MP)*abs(Lpp_Eg)/(13*HESS)
    dl = 0.5*0.4*Lpp_Eg*wb/mN*dQ[0]/3.6e-17
    print('   m_b\' a = %.0e (m_b\' = %.1e GeV): Earth row x%.1e ; clock (Hessian) x%.1e ; clock (linear, b only) x%.1e'
          % (sa_, sa_*MP, R*MU_F1/1.5e-29, dl, 0.4*abs(Lp_tet)*wb/mN/np.sqrt(2)*comp_slope(1/16.0, 10.0)[1]/3.6e-17))
