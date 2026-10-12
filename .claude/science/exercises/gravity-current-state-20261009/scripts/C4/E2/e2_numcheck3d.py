"""E2: brute-force check of the 2+1D large-N coefficients (QED3: 64/(5 pi^2 N); GN-Yukawa: 16/(15 pi^2 N)).
2x2 Euclidean gammas (Pauli), mediator ~ c^2 G_mn / K_G (QED3, Feynman-like in G) or 1/K_G (GN scalar),
shell integral over S^2 of the exact integrand, linear-in-p part by finite differences.
Usage: python e2_numcheck3d.py
"""
import numpy as np

g = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]  # x, y, t
nth, nph = 200, 128
xt, wt = np.polynomial.legendre.leggauss(nth); th = (xt + 1) * np.pi / 2; wt = wt * np.pi / 2
ph = np.arange(nph) * 2 * np.pi / nph
TH, PH = np.meshgrid(th, ph, indexing='ij')
W = (wt[:, None] * np.full(nph, 2 * np.pi / nph)[None, :] * np.sin(TH)).ravel()
K = np.stack([np.sin(TH) * np.cos(PH), np.sin(TH) * np.sin(PH), np.cos(TH)], -1).reshape(-1, 3)
G3 = np.array(g)


def sigma(p, c, kind):
    G = np.array([1 / c ** 2, 1 / c ** 2, 1.0])
    KG = np.sqrt(K[:, 2] ** 2 + c ** 2 * (K[:, :2] ** 2).sum(1))
    q = p[None, :] - K
    q2 = (q ** 2).sum(1)
    Sq = np.einsum('na,aij->nij', -1j * q, G3) / q2[:, None, None]   # fermion propagator, speed 1
    out = np.zeros((2, 2), complex)
    if kind == 'qed3':
        for m in range(3):
            coef = W * c ** 2 * G[m] / KG
            out += -(g[m] @ np.einsum('n,nij->ij', coef, Sq) @ g[m])   # Sigma' = int gamma S gamma D (sign as 4D)
        out = -out  # restore: Sigma' = + int gamma_m S gamma_n D_mn
    else:
        out = -np.einsum('n,nij->ij', W / KG, Sq)                      # Yukawa: Sigma' = - y^2 int S D
    return out / (2 * np.pi) ** 3


def flow(c, kind, h=1e-4):
    r = {}
    for nm, idx in (('t', 2), ('s', 0)):
        e = np.zeros(3); e[idx] = h
        d = (sigma(e, c, kind) - sigma(-e, c, kind)) / (2 * h)
        r[nm] = (np.trace(g[idx] @ d) / (2j)).real
    return r['s'] - r['t'], r


if __name__ == "__main__":
    for kind, kappa, A in (('qed3', 4 / (5 * np.pi ** 2), 16), ('gn', 2 / (15 * np.pi ** 2), 8)):
        d0, r0 = flow(1.0, kind)
        print(f"{kind}: c=1 isotropic coefficient A_t = {r0['t']:.6e} (expect 1/(6 pi^2) = {1/(6*np.pi**2):.6e}), anisotropy {d0:.1e}")
        for c in (0.99, 1.01):
            dv, _ = flow(c, kind)
            print(f"   c = {c}: dv/dL per unit A = {dv:+.6e}; kappa (c-1) = {kappa*(c-1):+.6e}; ratio {dv/(kappa*(c-1)):.4f}"
                  f"  -> exponent x{A}/N = {kappa*A:.4f}/N")
