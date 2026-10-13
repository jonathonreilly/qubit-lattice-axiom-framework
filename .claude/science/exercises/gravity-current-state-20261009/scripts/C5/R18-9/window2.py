import sys, numpy as np, lib9 as L
from scipy.optimize import fsolve
from photon import photonGw
from zz import mu_E
D = np.load('photres2_N160_parsed.npy'); D = D[D[:, 1] == 1.0]; D = D[np.argsort(D[:, 0])]
fits = [np.polyfit(D[:, 0], D[:, j], len(D) - 1) for j in range(2, 8)]
def phot(bg, a):
    c = [np.polyval(f, bg) for f in fits]; law = photonGw(bg, np.pi - bg); g, f = law.samples(1 << 14)
    return np.array([c[0] + c[1]*a + c[2]*a*a, c[3] + c[4]*a + c[5]*a*a, 2*mu_E(g, f, 1e-3)])
m = 0.01; x = np.array([2.9435, 0.915, 0.5587, -0.176])
print('nodes', D[:, 0])
for bs, fr in [(3.1, 1.0), (3.0, 1.0), (2.9, 1.0), (2.8, 1.0), (2.6, 1.0), (2.4, 1.0), (2.2, 1.0), (2.0, 1.0), (1.5, 1.0), (1.0, 1.0), (1.0, 0.02), (0.5, 0.02)]:
    S = L.scal(bs, fr, m)
    def rows(x):
        bg, bf, r, a = x; F = L.dirac(bf, r, m=m); V = phot(bg, a); t = L.NS*S[:3] + L.ND*F[:3] + L.NV*V
        return np.array([t[0], t[1], t[2], L.ND*F[3]])
    sol, info, ier, msg = fsolve(rows, x, full_output=True, epsfcn=1e-10)
    print('scalar G_w(%.2f, fr=%.2f) muE_s %+.4e -> b_g* %.5f b_f %.5f r %.5f a %+.5f | max|rows| %.1e | r<=1/sqrt3 %s' % (bs, fr, S[2], *sol, np.abs(rows(sol)).max(), sol[2] <= 1/np.sqrt(3)), flush=True)
    if ier == 1: x = sol
