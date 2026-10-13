"""R18-5: sensitivity of UD's Xi to the O(q^2) placement prescription (midpoint G(k) vs leg-average (G(k-q/2)+G(k+q/2))/2),
direct finite-q evaluation on a uniform grid, m = 0.3 (resolved), D1(1.4,0.3) and D1(0.916719,0.559627)."""
import numpy as np, sys
sys.path.insert(0, '.')
from content3 import D1q
from xiud import Gvec
def brute2(law, m, name, pol, N, presc, shifts=(1, 2, 4), Nc=4):
    kk = (np.arange(N) + 0.5)*2*np.pi/N - np.pi
    S, Sp, Spp, W, Wp, Wpp = law.tables(kk)
    def chi(n):
        acc = 0.0
        for ix in range(N):
            Sx, Spx, Wpx = S[ix], Sp[ix], Wp[ix]
            Sy, Spy, Wpy = S[:, None], Sp[:, None], Wp[:, None]
            Mz = m + W[ix] + W[:, None] + W[None, :]
            c = [Sx + 0*Mz, Sy + 0*Mz, S[None, :] + 0*Mz, Mz]; E2 = sum(x*x for x in c)
            px = Sx*Spx + Mz*Wpx; py = Sy*Spy + Mz*Wpy
            G = Gvec(name, pol, Sx, Sy, Spx, Spy, Wpx, Wpy, Mz, px, py, c, E2)
            if presc == 'avg' and n > 0:
                G = [0.5*(np.roll(g, n, axis=1) + np.roll(g, -n, axis=1)) for g in G]
            ca = [np.roll(x, n, axis=1) for x in c]; cb = [np.roll(x, -n, axis=1) for x in c]
            Ea = np.sqrt(sum(x*x for x in ca)); Eb = np.sqrt(sum(x*x for x in cb))
            G2 = sum(a*a for a in G); caG = sum(a*b for a, b in zip(ca, G)); cbG = sum(a*b for a, b in zip(cb, G)); cab = sum(a*b for a, b in zip(ca, cb))
            t = (Nc/4)*(G2*(1 + cab/(Ea*Eb)) - 2*caG*cbG/(Ea*Eb))
            acc += float(np.mean(2*t/(Ea + Eb)))
        return acc/N
    c0 = chi(0); d = []
    for n in shifts:
        q = 4*np.pi*n/N; d.append(-(chi(n) - c0)/q**2)
    r1 = (4*d[0] - d[1])/3; r2 = (4*d[1] - d[2])/3
    return (16*r1 - r2)/15
for (b, r) in ((1.4, 0.3), (0.916719, 0.559627)):
    law = D1q(b, r)
    for pol in ('T2g', 'Eg'):
        for N in (96, 128):
            am = brute2(law, 0.3, 'UD', pol, N, 'mid'); aa = brute2(law, 0.3, 'UD', pol, N, 'avg')
            print('D1(%.4f,%.4f) m=0.3 UD %s N=%d: alpha(mid) %+.6e alpha(avg) %+.6e  diff %+.3e' % (b, r, pol, N, am, aa, aa - am), flush=True)
