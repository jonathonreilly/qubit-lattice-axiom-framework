"""R6-3 (a): Siegel shell densities C*_t of the LRL reciprocal lattice.
L7 = diag(sqrt7,1,1,1)Z^4 (rho = 1/sqrt7).  Reciprocal (Minkowski pairing): G = 2pi diag(1/sqrt7,1,1,1) m,
G^2 = c t, c = (2pi)^2/7, t = Q*(m) = -m0^2 + 7(m1^2+m2^2+m3^2)  (form <-1,7,7,7>, det -343).
Haar-average of the Bragg comb on shell t:  E_g sum_{G in shell t} f(gG) = C*_t int f delta(q^2 - c t) d^4q.
Siegel (class number one; recalled): C*_t = c rho* prod_p alpha_p(t),  rho* = sqrt7/(2pi)^4.
alpha_p for p not dividing 14t: 1 - chi(p)/p^2, chi = (-7/.) ; p | t, p odd != 7: (1-chi/p^2) sum_{i<=v} (chi/p)^i ;
p = 2, 7: exact count mod p^r.
Cross-check against direct counting of reciprocal vectors in the lattice frame (|m0| <= K)."""
import numpy as np, time
t0 = time.time()
c = (2*np.pi)**2/7; rhostar = np.sqrt(7)/(2*np.pi)**4
L2chi = 1.151925470544491   # L(2, (-7/.)), as used in R4-1

def chi(p):
    if p == 2: return 1
    if p == 7: return 0
    return 1 if pow(p % 7, 3, 7) == 1 else -1   # (p/7) = (-7/p) for odd p

def factor(n):
    n = abs(n); f = {}; d = 2
    while d*d <= n:
        while n % d == 0: f[d] = f.get(d, 0)+1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0)+1
    return f

def alpha_local(p, t, r):
    N = p**r
    x = np.arange(N, dtype=np.int64)
    h0 = np.bincount((-x*x) % N, minlength=N).astype(float)
    h1 = np.bincount((7*x*x) % N, minlength=N).astype(float)
    F = np.fft.rfft
    conv = np.fft.irfft(F(h0)*F(h1)**3, n=N)
    return conv[t % N]/N**3

_cache = {}
def alpha_2_7(p, t):
    v = factor(t).get(p, 0)
    r = v + (5 if p == 2 else 3)
    key = (p, t % p**r, r)
    if key not in _cache:
        a1 = alpha_local(p, t, r); a2 = alpha_local(p, t, r+1)
        assert abs(a1-a2) < 1e-9*max(1, a1), (p, t, a1, a2)
        _cache[key] = a2
    return _cache[key]

prod_good = 1/(L2chi*(1 - chi(2)/4.0))   # prod over p not dividing 14 of (1 - chi(p)/p^2)

def Cstar(t):
    f = factor(t)
    val = c*rhostar*prod_good*alpha_2_7(2, t)*alpha_2_7(7, t)
    for p, v in f.items():
        if p in (2, 7): continue
        x = chi(p)/p
        val *= sum(x**i for i in range(v+1))
    return val

if __name__ == '__main__':
    ts = [t for t in range(-60, 61) if t != 0]
    C = {t: Cstar(t) for t in ts}
    print("c = %.6f, rho* = %.6e, c*rho* = %.6e (mean of C*_t)" % (c, rhostar, c*rhostar))
    print("represented? t: C*_t")
    print("  timelike: ", " ".join("%d:%.5f" % (t, C[t]) for t in range(-1, -21, -1)))
    print("  spacelike:", " ".join("%d:%.5f" % (t, C[t]) for t in range(1, 21)))
    # cross-check by direct counting: r3 via convolution
    K = 3000
    Nmax = (60 + K*K)//7 + 2
    r1 = np.zeros(Nmax+1); s = np.arange(0, int(np.sqrt(Nmax))+1)
    np.add.at(r1, s*s, 2); r1[0] = 1
    n2 = 1 << int(np.ceil(np.log2(3*(Nmax+1))))
    R = np.fft.rfft(r1, n2); r3 = np.rint(np.fft.irfft(R**3, n2)[:Nmax+1])
    print("count check (|m0| <= K = %d): ratio = count / (C*_t * mu_t(|q0|<=Q))" % K)
    Q = 2*np.pi*K/np.sqrt(7)
    for t in (-1, -2, -3, -4, -7, -8, -14, -49, 3, 5, 6, 7, 10, 14, 21, 28):
        m0 = np.arange(-K, K+1)
        num = t + m0*m0
        ok = (num >= 0) & (num % 7 == 0)
        cnt = r3[(num[ok]//7)].sum()
        M = c*t; mm = abs(M)
        if t < 0:
            mu = 2*np.pi*(Q*np.sqrt(Q*Q-mm) - mm*np.log((np.sqrt(Q*Q-mm)+Q)/np.sqrt(mm)))
        else:
            mu = 2*np.pi*(Q*np.sqrt(Q*Q+mm) + mm*np.log((Q+np.sqrt(Q*Q+mm))/np.sqrt(mm)))
        print("  t=%4d  count=%10d  C*=%.6f  ratio=%.4f" % (t, cnt, C[t], cnt/(C[t]*mu) if C[t] > 0 else np.nan))
    print("mean C*_t over 1<=|t|<=60: %.6e (c rho* = %.6e)" % (np.mean([C[t] for t in ts]), c*rhostar))
    np.save('r63_Cstar.npy', np.array([[t, Cstar(t)] for t in range(-4000, 4001) if t != 0]))
    print("elapsed %.1f s" % (time.time()-t0))
