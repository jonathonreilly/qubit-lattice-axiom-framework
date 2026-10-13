"""R19-31 probe (b),(c): the grid cross term of lattice scalar QED (Z^3 x R, NN complex scalar mass m, charge e, noncompact U(1)
at O(e^2), Feynman gauge) under H-cov E_g strain l = (e^h, e^-h, 1), with and without (S_loc). Lattice units, results per e^2.
Exact O(e^2) identity used (proved in report sec. 2): the part of the two-loop free energy linear in thermal occupations is
   X(h) = sum_p (n_p/eps_p) [Sigma_os(p; h) - Sigma_ct]    (thermal scalars; complex: particle + antiparticle)
        + sum_k (n_k/Omega_k) Pi_os^T(k; h)                 (thermal photons, 2 transverse polarisations)
i.e. soft density x ON-SHELL VACUUM self-energy of the soft particle. Sigma_ct = mass counterterm fixed at h = 0 (law datum).
(S_loc), background-field (CW) form: subtract Phi x d^2/dh^2 [dE_vac/dPhi](h), Phi = <|phi|^2>_state = <n/eps>,
   E_vac(Phi; h) = 3 sum_q (1/2) sqrt(Omega_q^2 + 2 e^2 Phi) (Landau gauge: background gives UV photons m_A^2 = 2 e^2 Phi)
   => dE_vac/dPhi = 3 e^2 G_gam(h),  G_gam = <1/(2 Omega)>.
Checks: (1) Sigma(0;h) Feynman = 4 G_gam - G_s(m); on-shell rest Sigma_os(0) vs CW 3 G_gam (gauge-invariant comparison);
        (2) on-shell O(p^2) part via D_space(p) - D_time(p0 = Omega_p) (cancels the LI threshold log; exact for the analytic part);
        (3) T-scaling of fixed-subtraction cross term (T^2) and of the (S_loc) residue (T^4); (4) photon-thermal channel Pi_os^T ~ k^2."""
import numpy as np, time
t0 = time.time()
br = np.array([0, 0.0025, 0.005, 0.01, 0.02, 0.04, 0.08, 0.16, 0.32, 0.64, 1.28, 2.2, np.pi])
xg, wg = np.polynomial.legendre.leggauss(6)
nodes, wts = [], []
for a, b in zip(br[:-1], br[1:]):
    nodes += list(0.5*(b - a)*xg + 0.5*(b + a)); wts += list(0.5*(b - a)*wg)
nodes = np.array(nodes); wts = np.array(wts)
k1 = np.concatenate([-nodes[::-1], nodes]); w1 = np.concatenate([wts[::-1], wts])/(2*np.pi)
QX, QY, QZ = np.meshgrid(k1, k1, k1, indexing='ij', sparse=True)
W = w1[:, None, None]*w1[None, :, None]*w1[None, None, :]
def avg(x): return float((W*x).sum())
def ells(h): return (np.exp(h), np.exp(-h), 1.0)
def Om2(h, qx, qy, qz):
    l = ells(h); return 4*np.sin(qx/2)**2/l[0]**2 + 4*np.sin(qy/2)**2/l[1]**2 + 4*np.sin(qz/2)**2/l[2]**2
def nB(e, T): return 1.0/np.expm1(e/T)
m = 0.1      # scalar mass (regulator; symmetric-phase Higgs has m_th ~ g T anyway)
d = 0.02     # strain step for Hessians
def G_gam(h): return avg(0.5/np.sqrt(Om2(h, QX, QY, QZ)))
def G_s(h): return avg(0.5/np.sqrt(m*m + Om2(h, QX, QY, QZ)))
def Sig_static(h, p):          # Sigma(P = (0, p)) per e^2, Feynman gauge
    l = ells(h); O = np.sqrt(Om2(h, QX, QY, QZ)); ep = np.sqrt(m*m + Om2(h, QX + p[0], QY + p[1], QZ + p[2]))
    V2 = sum((2/l[i])**2*np.sin(p[i] + q/2)**2 for i, q in enumerate((QX, QY, QZ)))
    seag = G_gam(h)*(1 + sum(np.cos(pi) for pi in p))
    return seag - avg(1/(2*(ep + O)) + V2/(2*ep*O*(ep + O)))
def Sig_time(h, p0):           # Sigma(P = (p0, 0)) per e^2, Feynman gauge; p0 may be complex (analytic continuation)
    O = np.sqrt(Om2(h, QX, QY, QZ)); e = np.sqrt(m*m + O*O); c = O*O
    N = lambda q0: (2*p0 + q0)**2 + c
    I = N(1j*O)/(2*O*((p0 + 1j*O)**2 + e*e)) + N(-p0 + 1j*e)/(2*e*((1j*e - p0)**2 + O*O))
    return 4*G_gam(h) - float((W*I).sum().real)
# ---- (1) zero-momentum values and the CW identity
print('m = %.2f, d = %.3f. (1) Sigma at zero momentum per e^2:' % (m, d))
S00, Sos0, CW = {}, {}, {}
for h in (-d, 0.0, d):
    S00[h] = Sig_time(h, 0.0); Sos0[h] = Sig_time(h, 1j*m*(1 - 1e-7)); CW[h] = 3*G_gam(h)
    print('  h=%+.3f  Sigma(P=0) Feynman %.9f (4G_gam-G_s = %.9f)  Sigma_os(rest) %.9f   CW 3G_gam %.9f   os-CW %+.3e'
          % (h, S00[h], 4*G_gam(h) - G_s(h), Sos0[h], CW[h], Sos0[h] - CW[h]), flush=True)
hs = lambda f: (f[d] - 2*f[0.0] + f[-d])/d**2
print('  Hessians: d2Sigma(P=0)/dh2 %+.6e   d2Sigma_os(rest)/dh2 %+.6e   d2(CW)/dh2 = 3 G_gam\'\' %+.6e   [os - CW] %+.3e'
      % (hs(S00), hs(Sos0), hs(CW), hs(Sos0) - hs(CW)), flush=True)
Gg2 = hs({h: G_gam(h) for h in (-d, 0.0, d)})
# ---- (2) on-shell O(p^2): D_space(p) - D_time(Omega_p) = Sigma_os(p) - Sigma_os(0)
print('(2) on-shell momentum dependence per e^2: [Sigma_os(p e_i) - Sigma_os(0)]/p_hat^2, p_hat^2 = Omega_p(h)^2 (free on-shell eps^2 - m^2)')
kap = {}
for h in (-d, 0.0, d):
    kap[h] = []
    for i in range(3):
        vals = []
        for p in (0.15, 0.3):
            pv = [0.0, 0.0, 0.0]; pv[i] = p
            Op = np.sqrt(Om2(h, *[np.array(x) for x in pv]))
            r = (Sig_static(h, pv) - S00[h] - (Sig_time(h, Op) - S00[h]))/Op**2
            vals.append((p, float(r)))
        # extrapolate r(p) = r0 + r2 p^2 to p -> 0
        (pa, ra), (pb, rb) = vals; r0 = (ra*pb**2 - rb*pa**2)/(pb**2 - pa**2)
        kap[h].append(r0)
        print('  h=%+.3f axis %s: r(0.15) %+.6e  r(0.30) %+.6e  -> r0 %+.6e' % (h, 'xyz'[i], ra, rb, r0), flush=True)
k0 = kap[0.0][0]
print('  h=0: isotropic on-shell speed renormalisation of the charged scalar, kappa0 = %+.4e per e^2 (the D1-infinity speed counterterm absorbs it)' % k0)
k2 = [(kap[d][i] - 2*kap[0.0][i] + kap[-d][i])/d**2 for i in range(3)]
k1d = [(kap[d][i] - kap[-d][i])/(2*d) for i in range(3)]
print('  dkappa_ii/dh = %s   d2kappa_ii/dh2 = %s' % (['%+.3e' % x for x in k1d], ['%+.3e' % x for x in k2]), flush=True)
# ---- (3) thermal sums: fixed-subtraction cross term vs (S_loc) residue, T scaling
print('(3) thermal cross terms per e^2 (canonical reading not applied here): FIXED = Phi*d2Sigma_os(rest)/dh2 + K(T); (S_loc) residue = FIXED - Phi*d2(CW)/dh2')
print('    K(T) = d2/dh2 sum_p (n/eps)(h) [kappa_ii(h) - kappa0] p_hat_i^2  (speed counterterm at h=0 removes kappa0), p_hat_i^2 = 4 sin^2(p_i/2)/l_i^2')
print('    Debye-prescription residue (photon sea 2 transverse modes at m_D^2 subtracted instead): FIXED - m_D^2 G_gam\'\'')
print('   T       Phi=<n/eps>   FIXED cross      FIXED/T^2     (S_loc) residue   residue/T^4    Debye-presc. residue  /T^2')
for T in (0.2, 0.1, 0.05, 0.025):
    Phi = avg(nB(np.sqrt(m*m + Om2(0.0, QX, QY, QZ)), T)/np.sqrt(m*m + Om2(0.0, QX, QY, QZ)))
    Kh = {}
    for j, h in enumerate((-d, 0.0, d)):
        l = ells(h); e = np.sqrt(m*m + Om2(h, QX, QY, QZ)); w = nB(e, T)/e
        Kh[h] = sum((kap[h][i] - k0)*avg(w*4*np.sin(q/2)**2/l[i]**2) for i, q in enumerate((QX, QY, QZ)))
    K = hs(Kh)
    fixed = Phi*hs(Sos0) + K
    res = fixed - Phi*hs(CW)
    e = np.sqrt(m*m + Om2(0.0, QX, QY, QZ)); n = nB(e, T); mD2 = avg(2*n*(1 + n)/T)
    debres = fixed - mD2*Gg2
    print('  %.3f  %.5e  %+.5e  %+.5e  %+.5e  %+.4e  %+.5e  %+.4e' % (T, Phi, fixed, fixed/T**2, res, res/T**4, debres, debres/T**2), flush=True)
# ---- (4) photon-thermal channel: on-shell transverse vacuum polarisation per e^2 (scalar loop), D_space - D_time
print('(4) thermal photons: on-shell transverse Pi_os(k e_j, pol e_i) per e^2 via Pi_ii(0,k e_j) - Pi_ii(k0 = Omega_k, 0); Ward => O(k^2)')
def Pi_static(h, i, k):        # Pi_ii(K = (0, k)) per e^2, vacuum
    l = ells(h); Q = (QX, QY, QZ)
    e1 = np.sqrt(m*m + Om2(h, *Q)); e2 = np.sqrt(m*m + Om2(h, QX + k[0], QY + k[1], QZ + k[2]))
    V2 = (2/l[i])**2*np.sin(Q[i] + k[i]/2)**2
    return avg(np.cos(Q[i])/e1) - avg(V2/(2*e1*e2*(e1 + e2)))
def Pi_time(h, i, k0):
    l = ells(h); Q = (QX, QY, QZ); e = np.sqrt(m*m + Om2(h, *Q))
    V2 = (2/l[i])**2*np.sin(Q[i])**2
    return avg(np.cos(Q[i])/e) - avg(V2/(e*(k0*k0 + 4*e*e)))
lam = {}
for h in (-d, 0.0, d):
    lam[h] = {}
    print('  h=%+.3f  Pi_ii(0) (Ward, must be 0): %s' % (h, ' '.join('%+.1e' % Pi_static(h, i, (0, 0, 0)) for i in range(3))), flush=True)
    for (i, j) in ((0, 2), (0, 1), (1, 2), (1, 0), (2, 0), (2, 1)):
        vals = []
        for k in (0.15, 0.3):
            kv = [0.0, 0.0, 0.0]; kv[j] = k
            Ok = np.sqrt(Om2(h, *[np.array(x) for x in kv]))
            vals.append((k, float((Pi_static(h, i, kv) - Pi_time(h, i, Ok))/Ok**2)))
        (ka, ra), (kb, rb) = vals; r0 = (ra*kb**2 - rb*ka**2)/(kb**2 - ka**2)
        lam[h][(i, j)] = r0
    print('         Pi_os/k_hat^2 (pol,dir): ' + '  '.join('(%s,%s) %+.5e' % ('xyz'[i], 'xyz'[j], lam[h][(i, j)]) for (i, j) in lam[h]), flush=True)
l0 = lam[0.0][(0, 2)]
print('  h=0 photon on-shell speed renormalisation lambda0 = %+.4e per e^2 (absorbed by the photon speed counterterm at h=0)' % l0)
print('   T      photon-channel cross term (after h=0 speed counterterm)   /T^4')
for T in (0.2, 0.1, 0.05, 0.025):
    Ph = {}
    for h in (-d, 0.0, d):
        l = ells(h); Om = np.sqrt(Om2(h, QX, QY, QZ)); w = nB(Om, T)/Om
        tot = 0.0
        for (i, j), r in lam[h].items():   # sum over the 2 transverse pols of k along each axis: approximate the quadratic form by axis values
            tot += 0.5*(r - l0)*avg(w*4*np.sin((QX, QY, QZ)[j]/2)**2/l[j]**2)
        Ph[h] = tot
    print('  %.3f  %+.5e   %+.4e' % (T, hs(Ph), hs(Ph)/T**4), flush=True)
print('G_gam\'\' = %+.6e ; time %.0f s' % (Gg2, time.time() - t0))
