"""E2: independent numerical check of the 4D speed-relaxation coefficients (kappa_F, kappa_S).
Brute force: explicit 4x4 Euclidean gamma matrices, exact (p-k)^2 (no hand expansion), shell integral
of the one-loop self-energy over the unit 3-sphere (the log coefficient of a degree -4 homogeneous
integrand), linear-in-p part by symmetric finite differences, Feynman-like gauge in the mediator metric
plus a general-xi term to confirm gauge independence of the speed.
Usage: python e2_numcheck.py
"""
import numpy as np

s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex)
Z2 = np.zeros((2, 2)); I2 = np.eye(2)
g = [np.block([[Z2, -1j * s], [1j * s, Z2]]) for s in (s1, s2, s3)] + [np.block([[Z2, I2], [I2, Z2]])]  # x,y,z,t
for a in range(4):
    for b in range(4):
        assert np.allclose(g[a] @ g[b] + g[b] @ g[a], 2 * (a == b) * np.eye(4))


def slash(v):
    return sum(v[i] * g[i] for i in range(4))


# quadrature on S^3: k = (sin th * n(alpha,phi), cos th); weight sin^2 th * sin alpha
nth, nal, nph = 48, 32, 32
xt, wt = np.polynomial.legendre.leggauss(nth); th = (xt + 1) * np.pi / 2; wt = wt * np.pi / 2
xa, wa = np.polynomial.legendre.leggauss(nal); al = (xa + 1) * np.pi / 2; wa = wa * np.pi / 2
ph = np.arange(nph) * 2 * np.pi / nph; wp = np.full(nph, 2 * np.pi / nph)
TH, AL, PH = np.meshgrid(th, al, ph, indexing='ij')
W = (wt[:, None, None] * wa[None, :, None] * wp[None, None, :]) * np.sin(TH) ** 2 * np.sin(AL)
K = np.stack([np.sin(TH) * np.sin(AL) * np.cos(PH), np.sin(TH) * np.sin(AL) * np.sin(PH),
              np.sin(TH) * np.cos(AL), np.cos(TH)], -1).reshape(-1, 4)
W = W.reshape(-1)
assert abs(W.sum() - 2 * np.pi ** 2) < 1e-10


def sigma_fermion(p, c, xi=1.0):
    """Shell integrand sum: Sigma'(p)/(A L) for fermion speed 1, vector mediator speed c."""
    G = np.diag([1 / c ** 2] * 3 + [1.0])
    KG2 = K[:, 3] ** 2 + c ** 2 * (K[:, :3] ** 2).sum(1)
    q = p[None, :] - K
    q2 = (q ** 2).sum(1)
    out = np.zeros((4, 4), complex)
    # Feynman-in-G part: gamma_m S gamma_n G_mn
    for m in range(4):
        coef = W * c ** 3 * G[m, m] / (KG2 * q2)
        Sq = np.einsum('n,nij->ij', coef, np.einsum('na,aij->nij', -1j * q, np.array(g)))
        out += g[m] @ Sq @ g[m]
    # (1 - xi) gauge piece: - kslash S kslash / K_G^2  (lower-index k_m)
    if xi != 1.0:
        coef = -(1 - xi) * W * c ** 3 / (KG2 ** 2 * q2)
        for n in range(len(W)):
            ks = slash(K[n]); out += coef[n] * ks @ (-1j * slash(q[n])) @ ks
    return out / (2 * np.pi) ** 4


def lin_coeffs(c, xi=1.0, h=1e-4):
    res = {}
    for name, idx in (('t', 3), ('s', 0)):
        e = np.zeros(4); e[idx] = h
        d = (sigma_fermion(e, c, xi) - sigma_fermion(-e, c, xi)) / (2 * h)
        res[name] = np.trace(g[idx] @ d).real if False else (np.trace(g[idx] @ d) / (4j)).real
    return res['s'] - res['t'], res


def sigma_scalar(p, c):
    G = np.diag([1 / c ** 2] * 3 + [1.0])
    KG2 = K[:, 3] ** 2 + c ** 2 * (K[:, :3] ** 2).sum(1)
    q = p[None, :] - K
    q2 = (q ** 2).sum(1)
    v = 2 * p[None, :] - K
    num = (v ** 2 * np.diag(G)[None, :]).sum(1)
    return -(W * c ** 3 * num / (KG2 * q2)).sum() / (2 * np.pi) ** 4


def scalar_coeffs(c, h=1e-3):
    out = {}
    for name, idx in (('t', 3), ('s', 0)):
        e = np.zeros(4); e[idx] = h
        d2 = (sigma_scalar(e, c) + sigma_scalar(-e, c) - 2 * sigma_scalar(np.zeros(4), c)) / (2 * h ** 2)
        out[name] = d2
    # p_t^2 (1 + Ct), p_s^2 (1 + Cs): v^2 = (1+Cs)/(1+Ct) -> dv/dL = (Cs - Ct)/2
    return (out['s'] - out['t']) / 2, out


if __name__ == "__main__":
    kF = 1 / (3 * np.pi ** 2); kS = 1 / (4 * np.pi ** 2)
    d0, r0 = lin_coeffs(1.0)
    print(f"c=1 LI check fermion: A_t = {r0['t']:.6e}, A_s = {r0['s']:.6e}, expect 1/(8pi^2) = {1/(8*np.pi**2):.6e}")
    for c in (0.99, 1.01, 1.1):
        dv, r = lin_coeffs(c)
        print(f"fermion <- gauge, c = {c}: dv/dL / A = {dv:+.6e} ; kappa_F*(c-1) = {kF*(c-1):+.6e} ; ratio {dv/(kF*(c-1)):.4f}")
    for xi in (0.0, 3.0):
        dv, r = lin_coeffs(1.01, xi=xi)
        print(f"  gauge xi = {xi}: dv/dL / A = {dv:+.6e}  (xi=1 value above; isotropic parts A_t = {r['t']:.4e})")
    s0, rs = scalar_coeffs(1.0)
    print(f"c=1 LI check scalar: p^2 log coefficient = {rs['t']:.6e} (expect -1/(4pi^2) = {-1/(4*np.pi**2):.6e})")
    for c in (0.99, 1.01):
        dv, r = scalar_coeffs(c)
        print(f"scalar  <- gauge, c = {c}: dv/dL / A = {dv:+.6e} ; kappa_S*(c-1) = {kS*(c-1):+.6e} ; ratio {dv/(kS*(c-1)):.4f}")
