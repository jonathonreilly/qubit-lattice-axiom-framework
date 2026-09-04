"""
T205 - Seeley-DeWitt coefficients b1,b2 for a diagonal metric g(x0), computed
from the raw Christoffel/Riemann definitions (explicit loops, no einsum
gymnastics), then VALIDATED against the hand-derived conformal values
b1 = 1/4, b2 = 1/8 (T200).

  (4 pi s)^2 K_2(s)/Vol_2 = 1 + b1 x + b2 x^2 + ... ,  x = s kappa^2
  b1 = [int sqrt(g) R/6]_2 / (Vol_2 kappa^2)
  b2 = [int sqrt(g) a2 ]_2 / (Vol_2 kappa^4)
  a2 = (1/360)(5R^2 - 2 Ric^2 + 2 Riem^2)     [ int lap R = 0 on the torus ]
"""
import numpy as np

def curv(gd, dgd, ddgd):
    """gd,dgd,ddgd : (N,4) diag(g), d0 diag(g), d0d0 diag(g).
       returns R, Ric2, Riem2, sqrtg   (each length N)"""
    N = gd.shape[0]
    g = np.zeros((N, 4, 4)); dg = np.zeros((N, 4, 4)); ddg = np.zeros((N, 4, 4))
    for a in range(4):
        g[:, a, a] = gd[:, a]; dg[:, a, a] = dgd[:, a]; ddg[:, a, a] = ddgd[:, a]
    gi = np.linalg.inv(g)
    dgi = -np.einsum('nab,nbc,ncd->nad', gi, dg, gi)
    D  = np.zeros((N, 4, 4, 4))          # D[mu,r,s] = d_mu g_{rs}
    D[:, 0] = dg
    DD = np.zeros((N, 4, 4, 4))          # DD[r,s] = d_0 d_0 g_{rs} (only mu=nu=0)
    DD = ddg
    Gam  = np.zeros((N, 4, 4, 4))        # Gam[l,m,v]
    dGam = np.zeros((N, 4, 4, 4, 4))     # dGam[mu,l,m,v]; only mu=0 nonzero
    for l in range(4):
        for m in range(4):
            for v in range(4):
                acc = np.zeros(N); dacc = np.zeros(N)
                for r in range(4):
                    comb  = D[:, m, r, v] + D[:, v, r, m] - D[:, r, m, v]
                    acc  += gi[:, l, r]*comb
                    dcomb = (DD[:, r, v] if m == 0 else 0.0) \
                          + (DD[:, r, m] if v == 0 else 0.0) \
                          - (DD[:, m, v] if r == 0 else 0.0)
                    dacc += dgi[:, l, r]*comb + gi[:, l, r]*dcomb
                Gam[:, l, m, v] = 0.5*acc
                dGam[:, 0, l, m, v] = 0.5*dacc
    Riem = np.zeros((N, 4, 4, 4, 4))     # Riem[r,s,m,v] = R^r_{s m v}
    for r in range(4):
        for s in range(4):
            for m in range(4):
                for v in range(4):
                    val = dGam[:, m, r, v, s] - dGam[:, v, r, m, s]
                    for l in range(4):
                        val = val + Gam[:, r, m, l]*Gam[:, l, v, s] \
                                  - Gam[:, r, v, l]*Gam[:, l, m, s]
                    Riem[:, r, s, m, v] = val
    Ric = np.einsum('nmsmv->nsv', Riem)
    R   = np.einsum('nsv,nsv->n', gi, Ric)
    Ric2 = np.einsum('nab,ncd,nac,nbd->n', gi, gi, Ric, Ric)
    Rlow = np.einsum('nae,nesmv->nasmv', g, Riem)          # R_{a s m v}
    Riem2 = np.einsum('nasmv,nap,nsq,nmr,nvw,npqrw->n',
                      Rlow, gi, gi, gi, gi, Rlow)
    return R, Ric2, Riem2, np.sqrt(np.linalg.det(g))

def coeffs(chan, L, n, h=0.05, N=4096):
    kap = 2*np.pi*n/L; t = np.arange(N)*L/N; dt = L/N
    def build(eps):
        psi, dpsi, ddpsi = np.cos(kap*t), -kap*np.sin(kap*t), -kap**2*np.cos(kap*t)
        gd = np.ones((N, 4)); dgd = np.zeros((N, 4)); ddgd = np.zeros((N, 4))
        for a, sgn in chan.items():
            gd[:, a] += sgn*eps*psi; dgd[:, a] = sgn*eps*dpsi; ddgd[:, a] = sgn*eps*ddpsi
        R, Ric2, Riem2, sg = curv(gd, dgd, ddgd)
        a2 = (5*R*R - 2*Ric2 + 2*Riem2)/360.0
        return np.array([np.sum(sg)*dt, np.sum(sg*R/6.0)*dt, np.sum(sg*a2)*dt])
    f = {e: build(e*h) for e in (-2, -1, 0, 1, 2)}
    d2 = (-f[2] + 16*f[1] - 30*f[0] + 16*f[-1] - f[-2])/(12*h*h)
    V2, A1, A2 = 0.5*d2                       # eps^2 Taylor coefficients (per column)
    return V2, A1/(V2*kap**2), A2/(V2*kap**4)

if __name__ == "__main__":
    L, n = 64, 2
    cases = {
        "conformal   diag(+1,+1,+1,+1)": {0: 1, 1: 1, 2: 1, 3: 1},
        "traceless   diag(+1,-1, 0, 0)": {0: 1, 1: -1},
        "traceless TT diag(0,+1,-1, 0)": {1: 1, 2: -1},
        "traceless    diag(+1,0,0,-1)":  {0: 1, 3: -1},
    }
    print(f"{'channel':32s} {'Vol2/L^4':>12s} {'b1':>12s} {'b2':>12s}   |b2|/b1")
    for name, ch in cases.items():
        V2, b1, b2 = coeffs(ch, L, n)
        print(f"{name:32s} {V2/L:12.6f} {b1:12.6f} {b2:12.6f}   {abs(b2)/abs(b1):8.4f}")
    print("\nVALIDATION - conformal must give Vol2/L^4 = 0.5, b1 = 0.25, b2 = 0.125")
    V2, b1, b2 = coeffs(cases["conformal   diag(+1,+1,+1,+1)"], L, n)
    print(f"  err: {abs(V2/L-0.5):.3e}  {abs(b1-0.25):.3e}  {abs(b2-0.125):.3e}")
