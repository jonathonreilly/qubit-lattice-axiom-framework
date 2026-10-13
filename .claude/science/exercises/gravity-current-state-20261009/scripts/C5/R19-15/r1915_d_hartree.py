"""R19-15 (d): numerical check that the O(lambda) (Hartree) shear Hessian vanishes when the unstrained
PHYSICAL mass is held fixed. NN scalar, E_g flow (as r1915_d_loops.py). m_b^2 = m_p^2 - (lambda/2) G(0; m_p) exactly
solved self-consistently at h=0: m_p^2 = m_b^2 + (lambda/2) G(0; m_p) (one-loop tadpole)."""
import numpy as np, sys
def disp(kx, ky, kz, m):
    return np.sqrt(m*m + 6 - 2*np.cos(kx) - 2*np.cos(ky) - 2*np.cos(kz))

def flowE(kx, ky, t, nst=20):
    F = lambda y: 0.5*np.sin(y)
    def one(x, s):
        h = s/nst
        for _ in range(nst):
            a = F(x); b = F(x + 0.5*h*a); c = F(x + 0.5*h*b); d = F(x + h*c)
            x = x + h*(a + 2*b + 2*c + d)/6
        return x
    return one(kx, t), one(ky, -t)

def flowT(kx, ky, t, nst=20):
    F = lambda y: 0.5*np.sin(y)
    h = t/nst; x, y = kx.copy(), ky.copy()
    for _ in range(nst):
        a1, a2 = F(y), F(x)
        b1, b2 = F(y + 0.5*h*a2), F(x + 0.5*h*a1)
        c1, c2 = F(y + 0.5*h*b2), F(x + 0.5*h*b1)
        d1, d2 = F(y + h*c2), F(x + h*c1)
        x, y = x + h*(a1 + 2*b1 + 2*c1 + d1)/6, y + h*(a2 + 2*b2 + 2*c2 + d2)/6
    return x, y

def eps_t(N, m, t, chan):
    k = 2*np.pi*np.arange(N)/N
    KX, KY, KZ = np.meshgrid(k, k, k, indexing='ij')
    if t != 0.0:
        KX, KY = (flowE if chan == 'E' else flowT)(KX, KY, t)
    return disp(KX, KY, KZ, m)

N = 28
def EG(m2, t):
    m = np.sqrt(m2); e = eps_t(N, m, t, 'E'); return 0.5*e.mean(), (1/(2*e)).mean()
def hess(f, d=0.02):
    return (f(d) - 2*f(0.0) + f(-d))/d**2
mp = 1.0
mu0 = hess(lambda t: EG(mp**2, t)[0])
print('mu_E one loop at m_p=1: %+.9e' % mu0)
for lam in (0.04, 0.02, 0.01):
    G0 = EG(mp**2, 0.0)[1]
    mb2 = mp**2 - 0.5*lam*G0
    tot = lambda t: (lambda E, G: E + lam/8*G*G)(*EG(mb2, t))
    bare = lambda t: (lambda E, G: E + lam/8*G*G)(*EG(mp**2, t))
    hp = hess(tot); hb = hess(bare)
    print('lambda=%.3f  fixed physical mass: mu - mu0 = %+.4e (ratio to lambda^2 %+.4e)   bare m=m_p: mu - mu0 = %+.4e (/lambda %+.4e)' % (lam, hp - mu0, (hp - mu0)/lam**2, hb - mu0, (hb - mu0)/lam))
