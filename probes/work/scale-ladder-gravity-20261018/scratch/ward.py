"""Lattice Ward identity for the P1 scalar's stress on the Kuhn complex (b=0).
W(k1,k2,xi) = first variation of S_phi[phi_bar(k1), phi(k2)] under vertex displacement xi e^{iq.x}, q=k1-k2,
field values held at vertices. Continuum: W = i q_mu T^{mu nu} xi_nu = 0 when both legs are on shell."""
import numpy as np, contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    from fem import SIMPLICES
def W(k1, k2, xi):
    q = k1 - k2; tot = 0j
    for vs in SIMPLICES:
        E = np.array([vs[i] - vs[0] for i in range(1, 5)], float)
        G = E @ E.T; Gi = np.linalg.inv(G); sq = np.sqrt(np.linalg.det(G))
        ph2 = np.array([np.exp(1j*k2@v) for v in vs]); ph1 = np.array([np.exp(-1j*k1@v) for v in vs])
        d2 = ph2[1:] - ph2[0]; d1 = ph1[1:] - ph1[0]
        X = d1 @ Gi @ d2
        # d/dG of sq*X/24 :  sq/24 * ( 1/2 Gi X - Gi d2 d1^T Gi )   (symmetrised)
        P = np.outer(Gi @ d2, Gi @ d1); P = 0.5*(P + P.T)
        Psi = sq/24*(0.5*Gi*X - P)
        xs = np.array([xi*np.exp(1j*q@v) for v in vs])           # displacement at each vertex
        dE = xs[1:] - xs[0]
        dG = E @ dE.T + dE @ E.T
        tot += np.sum(Psi*dG)
    return tot
def shell(ks):
    return 1j*2*np.arcsinh(np.sqrt(np.sum(4*np.sin(ks/2)**2))/2)
rng = np.random.default_rng(2)
print("on-shell legs (lattice shell), |W| / (|q| |k|^2 |xi|) as legs scale down:")
for trial in range(3):
    n1 = rng.standard_normal(3); n2 = rng.standard_normal(3); xi = rng.standard_normal(4)
    for s in (0.4, 0.2, 0.1, 0.05):
        k1s, k2s = s*n1/np.linalg.norm(n1), s*0.7*n2/np.linalg.norm(n2)
        k1 = np.array([*k1s, shell(k1s)]); k2 = np.array([*k2s, shell(k2s)])
        w = W(k1, k2, xi); q = k1 - k2
        # off-shell control: same spatial momenta, time components scaled
        k2o = np.array([*k2s, 1.2*shell(k2s)]); wo = W(k1, k2o, xi)
        print(f"  trial {trial} s={s:.2f}: on-shell |W|={abs(w):.2e} (ratio {abs(w)/(s**3):.3e}/s^3)  off-shell control |W|={abs(wo):.2e}")
