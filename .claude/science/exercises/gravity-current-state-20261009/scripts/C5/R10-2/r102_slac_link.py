# R10-2 part 2. (a) Whole-zone SLAC slices 1/(th^2+c), th in (-pi,pi]: link-RP Hankel [G(1+i+j)]
# and site-RP [G(i+j)] over the c range of the 4D zone (c = |k_spatial|^2 + m^2 in [m^2, 3pi^2+m^2)).
# (b) Lemma C sign check: the link kernel for lam<0 near th=pi is a DIP; the site kernel is a PEAK.
import mpmath as mp
mp.mp.dps = 50
def G_of(F, tmax):
    return [mp.quad(lambda t: F(t)*mp.cos(n*t), [0, mp.pi/2, mp.pi])/mp.pi for n in range(tmax+1)]
def eigs(M):
    E = mp.eigsy(mp.matrix(M), eigvals_only=True)
    E = sorted([E[i] for i in range(len(E))]); return E[0], E[-1]
N = 14
for c in ['0.0025', '0.25', '1.0', '5.0', '15.0', '29.86']:
    cc = mp.mpf(c)
    G = G_of(lambda t: 1/(t**2+cc), 2*N+3)
    res = []
    for n in [2, 6, 10, 14]:
        L1 = [[G[1+i+j] for j in range(n+1)] for i in range(n+1)]
        H0 = [[G[i+j] for j in range(n+1)] for i in range(n+1)]
        lo1, hi1 = eigs(L1); lo0, hi0 = eigs(H0)
        res.append('N=%d link %s site %s' % (n, mp.nstr(lo1/hi1, 3), mp.nstr(lo0/hi0, 3)))
    print('SLAC c=%s: ' % c + ' | '.join(res))
# kernel shapes near pi (lam = -0.99)
lam = mp.mpf('-0.99')
for phi in ['0', '0.02', '0.1', '0.3']:
    th = mp.pi + mp.mpf(phi)
    site = (1-lam**2)/(1-2*lam*mp.cos(th)+lam**2)
    link = 2*mp.re(mp.e**(1j*th)/(1-lam*mp.e**(1j*th)))
    print('lam=-0.99 phi=%s  site kernel P=%s   link kernel 2Re e^{ith}/(1-lam e^{ith})=%s' % (phi, mp.nstr(site, 6), mp.nstr(link, 6)))
