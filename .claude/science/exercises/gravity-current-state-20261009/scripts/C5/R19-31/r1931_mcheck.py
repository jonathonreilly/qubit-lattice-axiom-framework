"""R19-31 check: (i) the gap between the ON-SHELL soft self-energy's strain Hessian and the (S_loc)-CW coefficient 3 G_gam'' is O(e^2 m^2)
(so the g^2 T^2 cancellation is exact up to O(g^2 m^2) = O(g^4 T^2) when m ~ m_th ~ gT); (ii) the massless-limit (S_loc) residue
coefficient K/T^4 = (sum_i d2kappa_ii/dh2) * <n p_i^2/eps>_{m=0}/T^4, <n p_i^2/eps> = pi^2 T^4/90 (u_i = p_i/l_i makes it h-independent).
Imports the functions of r1931_sqed_cross.py by exec of its definitions (same folder)."""
import numpy as np, time
src = open(__file__.replace('r1931_mcheck.py', 'r1931_sqed_cross.py')).read().split('# ---- (1)')[0]
t0 = time.time()
for mm in (0.2, 0.1, 0.05):
    g = {}; exec(src.replace('m = 0.1      #', 'm = %r      #' % mm), g)
    d = g['d']; S, C, kap = {}, {}, {}
    for h in (-d, 0.0, d):
        S[h] = g['Sig_time'](h, 1j*mm*(1 - 1e-7)); C[h] = 3*g['G_gam'](h)
        S0 = g['Sig_time'](h, 0.0); kap[h] = []
        for i in range(3):
            rr = []
            for p in (0.15, 0.3):
                pv = [0.0, 0.0, 0.0]; pv[i] = p
                Op = np.sqrt(g['Om2'](h, *[np.array(x) for x in pv]))
                rr.append(float((g['Sig_static'](h, pv) - S0 - (g['Sig_time'](h, Op) - S0))/Op**2))
            kap[h].append((rr[0]*0.3**2 - rr[1]*0.15**2)/(0.3**2 - 0.15**2))
    hs = lambda f: (f[d] - 2*f[0.0] + f[-d])/d**2
    k2 = [(kap[d][i] - 2*kap[0.0][i] + kap[-d][i])/d**2 for i in range(3)]
    print('m=%.2f: d2Sigma_os(rest)/dh2 %+.6e  3G_gam\'\' %+.6e  gap %+.3e (gap/m^2 %+.3f) | kappa0 %+.5f  d2kappa_ii %s  sum %+.4f -> K/T^4 (H-cov, m->0 gas) %+.4f per e^2'
          % (mm, hs(S), hs(C), hs(S) - hs(C), (hs(S) - hs(C))/mm**2, kap[0.0][0], ['%+.4f' % x for x in k2], sum(k2), sum(k2)*np.pi**2/90), flush=True)
print('time %.0f s' % (time.time() - t0))
