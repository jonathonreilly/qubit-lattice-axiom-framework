"""F5-T3': Kubo-Bastin DC conductivity of the dissipative Wilson walker with an energy-selective (T=0, mu=0) sink."""
import numpy as np
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]], complex); sz = np.array([[1, 0], [0, -1]], complex)
SIG = np.array([sx, sy, sz])

def sigma_xx(N, gam_fun):
    k1 = 2*np.pi*(np.arange(N)+0.5)/N
    K = np.stack(np.meshgrid(k1, k1, k1, indexing='ij'), -1).reshape(-1, 3)
    out_tot, out_light = 0.0, 0.0
    for chunk in np.array_split(np.arange(K.shape[0]), 8):
        k = K[chunk]
        h = np.einsum('nj,jab->nab', np.sin(k), SIG)
        vx = np.cos(k[:, 0])[:, None, None] * sx
        G = gam_fun(k)
        GR = np.linalg.inv(-h + 0.5j*G[:, None, None]*np.eye(2))
        ImG = (GR - np.conj(np.swapaxes(GR, -1, -2))) / 2j
        val = np.trace(vx @ ImG @ vx @ ImG, axis1=-2, axis2=-1).real / np.pi
        out_tot += val.sum()
        light = np.linalg.norm(np.where(k > np.pi, k - 2*np.pi, k), axis=1) < 0.5
        out_light += val[light].sum()
    return out_tot / K.shape[0], out_light / K.shape[0]

ff = lambda k: (1 - np.cos(k)).sum(-1)
for p in (1, 2, 4):
    for N in (32, 48, 64):
        s, sl = sigma_xx(N, lambda k, p=p: ff(k)**p)
        print(f"p={p} N={N}: sigma_xx = {s:.5e} e^2/(hbar a); light-node region (|k|<0.5) share = {sl:.3e}")
for eta in (1e-1, 1e-2, 1e-3):
    s, sl = sigma_xx(48, lambda k, eta=eta: eta*np.ones(k.shape[0]))
    print(f"control Hermitian walker + eta={eta:g}: sigma_xx = {s:.5e}")
