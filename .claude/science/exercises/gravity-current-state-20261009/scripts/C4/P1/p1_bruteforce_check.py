"""Independent brute-force checks (no elliptic reduction, no integration by parts):
 (a) naive fermion with symbol sin p: flow the momentum grid with RK4 and finite-difference E_vac(eps) = <-2 omega_n(Phi^-1 p)>;
 (b) metric-coupled scalar / photon option B: finite differences of <1/2 sqrt(M^2 + e^-eps Kx^2 + e^eps Ky^2 + Kz^2)>;
 (c) KG flow F(m) the same way (V3 method).  Midpoint grids L=64 and 96 (m=0.5, smooth integrands)."""
import numpy as np
def flow_inv(k, e, f, n=60):
    x = k.copy(); h = 1.0/n
    for _ in range(n):
        a1 = -e*f(x); a2 = -e*f(x+h/2*a1); a3 = -e*f(x+h/2*a2); a4 = -e*f(x+h*a3)
        x = x + h/6*(a1+2*a2+2*a3+a4)
    return x
def hess(E, de=0.02):
    v = {e: E(e) for e in [-de, -de/2, 0, de/2, de]}
    D = lambda e: (v[e]+v[-e]-2*v[0])/e**2
    return (4*D(de/2)-D(de))/3
for L in [64, 96]:
    k = 2*np.pi*(np.arange(L)+0.5)/L
    m = 0.5
    fN = lambda x: 0.5*np.sin(x)          # RN norm: velocity 1/2 hhat f, f = sin p
    def EN(e):
        qx = flow_inv(k, e, fN); qy = flow_inv(k, -e, fN)
        X, Y, Z = np.meshgrid(qx, qy, k, indexing='ij')
        return (-2*np.sqrt(m*m + np.sin(X)**2 + np.sin(Y)**2 + np.sin(Z)**2)).mean()
    def EK(e):
        qx = flow_inv(k, e, fN); qy = flow_inv(k, -e, fN)
        X, Y, Z = np.meshgrid(qx, qy, k, indexing='ij')
        return (0.5*np.sqrt(m*m + 4*np.sin(X/2)**2 + 4*np.sin(Y/2)**2 + 4*np.sin(Z/2)**2)).mean()
    X, Y, Z = np.meshgrid(k, k, k, indexing='ij')
    KX2, KY2, KZ2 = 4*np.sin(X/2)**2, 4*np.sin(Y/2)**2, 4*np.sin(Z/2)**2
    EB = lambda e, M: (0.5*np.sqrt(M*M + np.exp(-e)*KX2 + np.exp(e)*KY2 + KZ2)).mean()
    print(f'L={L}: naive(sin p) G(0.5) = {hess(EN):+.8e}   [p1_mu_species: +9.909285e-02]')
    print(f'       KG flow   F(0.5) = {hess(EK):+.8e}   [p1_mu_species: +2.467156e-03]')
    print(f'       metric F_B(0.5) = {hess(lambda e: EB(e, 0.5)):+.8e}   [+3.504308e-01];  2F_B(0) photon B = {2*hess(lambda e: EB(e, 0.0)):+.6e} [+7.117213e-01]')
