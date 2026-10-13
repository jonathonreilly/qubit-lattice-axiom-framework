"""R19-27 (a): the thermal cross channel (R19-21's channel F) for the ISOTROPIC enthalpy, NN lattice scalar with on-site
(lambda/4!) phi^4 at O(lambda) (Hartree / first order), on V1 (H-cov dilation: same law at a new spacing, m and T physical).
Free energy at O(lambda): f = f_free + (lambda/8) G^2 + (dm2/2) G, G = G_vac + G_th; the vacuum tadpole is cancelled at the
lowest state.  The state(T)-dependent Planckian piece is the cross term
    f_x(n) = (lambda/4) G_vac(n) G_th(n) + (dm2(n)/2) G_th(n),
    G_vac = g_vac(m l)/l^2, g_vac(mu) = <1/(2 Omega)>;  G_th = g_th(m l, T l)/l^2, g_th = <1/(Omega (e^{Omega/tau} - 1))>.
Schemes:  per-site counterterm dm2 = -(lambda/2) g_vac(0)/l^2  (one number fixed in lattice units; tracks n)
          LI counterterm       dm2 = -(lambda/2) G_vac(n0)      (fixed in physical units, tuned at n0)
Enthalpy of the cross term, W_x = n d f_x/dn at fixed T, m (identity E1), by central differences in n.
Expected: LI: W_x -> (lambda/4) G_th n dG_vac/dn = (lambda/6) G_th G_vac (Planckian x T^2) at n0;
          per-site: only the mass-dependent (log) part of g_vac survives: W_x / W_x(LI) ~ (m l)^2 log.
"""
import numpy as np
out = []
def P(s): print(s, flush=True); out.append(s)
N = 96
k = (np.arange(N) + 0.5)*2*np.pi/N - np.pi
O2 = (4*np.sin(k/2)**2)
def means(mu, tau):
    gv = 0.0; gt = 0.0
    O23 = O2[None, :, None] + O2[None, None, :]
    for i in range(N):
        Om = np.sqrt(O2[i] + O23 + mu*mu)
        gv += (0.5/Om).sum()
        x = Om/tau
        gt += np.where(x < 700, 1.0/(Om*np.expm1(np.minimum(x, 700))), 0.0).sum()
    return gv/N**3, gt/N**3
gv00, _ = means(0.0, 1.0)
P('NN scalar, N = %d: g_vac(0) = <1/(2 Omega)> = %.6f (lattice units)' % (N, gv00))
lam = 1.0; dl = 2e-3
def fx(n, m, T, scheme, Gvac0):
    l = n**(-1/3); gv, gt = means(m*l, T*l)
    Gv, Gt = gv/l**2, gt/l**2
    dm2 = -(lam/2)*gv00/l**2 if scheme == 'site' else -(lam/2)*Gvac0
    return (lam/4)*Gv*Gt + 0.5*dm2*Gt, Gv, Gt
T = 0.1
P('T l0 = %.2f, lambda = 1, n0 = 1; W_x = d f_x / d ln n:' % T)
rows = []
for m in (0.4, 0.2, 0.1, 0.05):
    Gvac0 = means(m, T)[0]
    res = {}
    for sch in ('LI', 'site'):
        fp = fx(np.exp(dl), m, T, sch, Gvac0)[0]; fm = fx(np.exp(-dl), m, T, sch, Gvac0)[0]
        f0, Gv, Gt = fx(1.0, m, T, sch, Gvac0)
        res[sch] = (f0, (fp - fm)/(2*dl))
    pred = (lam/6)*Gt*gv00
    rows.append((m, res))
    P('  m l0 = %.2f: G_th = %.4e | LI: f_x %+.3e W_x %+.4e (pred (lam/6) G_th g_vac(0) = %+.4e) | per-site: f_x %+.3e W_x %+.3e | ratio %+.2e'
      % (m, Gt, res['LI'][0], res['LI'][1], pred, res['site'][0], res['site'][1], res['site'][1]/res['LI'][1]))
ms = np.array([r[0] for r in rows]); rat = np.array([abs(r[1]['site'][1]/r[1]['LI'][1]) for r in rows])
P('  log-log slope of |W_site/W_LI| vs m l: %.2f  (expected ~2, times a log)' % np.polyfit(np.log(ms), np.log(rat), 1)[0])
P('  (the per-site residual is the log running of the mass, (lambda/2)(g_vac(m l) - g_vac(0))/l^2 ~ lambda m^2 log(m l): EW-scale, LI-type;')
P('   zero under the full line of constant physics. Scale at l = l_P, T = T_c: LI W_x ~ (lambda/6)(T^2/12) g_vac(0) M_P^2.)')
MP = 1.22089e19; Tc = 159.5; rr = (np.pi**2/30)*106.75*Tc**4
Wli = (1/6)*(Tc**2/12)*gv00*MP**2
P('  LI scheme at T_c (lambda = 1, l = l_P, massless G_th = T^2/12): W_x = %.2e GeV^4 = %.1e rho_rad(T_c)' % (Wli, Wli/rr))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
