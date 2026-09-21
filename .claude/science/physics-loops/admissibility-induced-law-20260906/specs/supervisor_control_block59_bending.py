"""Block 59 control (supervisor-run; floating point; evidence, not proof): how a ray bends and a slow body falls when bonds have rates of their own.

(a) Three dimensions, the walk with the qubit as coin, NO rest energy, bond amplitudes c_b = (phi_x phi_y)^(1 + beta) with phi = exp(u/2),
    u = g z: beta = 0 is block 54's product form (lengths locked at 1); beta = 1 is l = wbar/w (wbar = 1).  A positive-energy packet moves along x;
    the part of its displacement along z that is odd in g is compared with a cloud of rays of E = c(z) eps(k) and between the two clauses.
(b) A line with an ON-SITE rest energy timed by the site rate, H = w m sigma_x + sigma_z D with the hops timed by c = w^(1 + beta): a packet at
    rest falls at -c^2 dlog w whatever beta (note T4): the fall of a slow body does not tell the two clauses apart; the bending of a ray does."""
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply

SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]


def cloud(g, beta, start, sig, kvec, t_end, centre_z, n=20000, steps=600, seed=59):
    rng = np.random.default_rng(seed)
    dx = sig * rng.standard_normal((n, 3)); dk = rng.standard_normal((n, 3)) / (2 * sig)
    x = start[None, :] + np.concatenate([dx, -dx, dx, -dx]); k = kvec[None, :] + np.concatenate([dk, dk, -dk, -dk])
    x0 = x.mean(axis=0)

    def f(x, k):
        s, co = np.sin(k), np.cos(k)
        e = np.sqrt((s * s).sum(axis=1))
        c = np.exp((1 + beta) * g * (x[:, 2] - centre_z))
        vel = (c / e)[:, None] * s * co
        force = np.zeros_like(k); force[:, 2] = -e * c * (1 + beta) * g
        return vel, force

    h = t_end / steps
    for _ in range(steps):
        a1, b1 = f(x, k); a2, b2 = f(x + h / 2 * a1, k + h / 2 * b1); a3, b3 = f(x + h / 2 * a2, k + h / 2 * b2); a4, b4 = f(x + h * a3, k + h * b3)
        x = x + h * (a1 + 2 * a2 + 2 * a3 + a4) / 6; k = k + h * (b1 + 2 * b2 + 2 * b3 + b4) / 6
    return (x.mean(axis=0) - x0)[2]


def bending(side, k0, g, t_end, sig, beta):
    idx = np.arange(side ** 3).reshape(side, side, side)
    pos = np.stack(np.meshgrid(*[np.arange(side, dtype=float)] * 3, indexing="ij"))
    centre = side / 2.0
    kvec = np.array([k0, 0.0, 0.0])
    start = np.array([centre - 0.5 * t_end * np.cos(k0), centre, centre])
    out = {}
    for sign in (+1, -1):
        amp_site = np.exp(0.5 * (1 + beta) * sign * g * (pos[2] - centre))
        rows, cols, vals = [], [], []
        for j in range(3):
            lo = [slice(None)] * 3; hi = [slice(None)] * 3
            lo[j] = slice(0, side - 1); hi[j] = slice(1, side)
            xa, xb = idx[tuple(lo)].ravel(), idx[tuple(hi)].ravel()
            amp = (amp_site[tuple(lo)] * amp_site[tuple(hi)]).ravel()
            for s1 in range(2):
                for s2 in range(2):
                    cc = SIG[j][s1, s2]
                    if cc == 0:
                        continue
                    rows += [2 * xb + s1, 2 * xa + s1]; cols += [2 * xa + s2, 2 * xb + s2]; vals += [0.5j * amp * cc, -0.5j * amp * cc]
        n = 2 * idx.size
        ham = coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(n, n)).tocsr()
        d = pos - start[:, None, None, None]
        env = np.exp(-(d ** 2).sum(axis=0) / (4 * sig ** 2)) * np.exp(1j * k0 * d[0])
        spinor = np.array([1.0, 1.0]) / np.sqrt(2)                          # content along +x
        comp = [np.fft.fftn(env * spinor[0]), np.fft.fftn(env * spinor[1])]
        kk = 2 * np.pi * np.fft.fftfreq(side)
        kx, ky, kz = np.meshgrid(kk, kk, kk, indexing="ij")
        sx, sy, sz = np.sin(kx), np.sin(ky), np.sin(kz)
        e = np.sqrt(sx * sx + sy * sy + sz * sz); e[e == 0] = 1.0
        nx, ny, nz = sx / e, sy / e, sz / e
        upc = 0.5 * ((1 + nz) * comp[0] + (nx - 1j * ny) * comp[1]); dnc = 0.5 * ((nx + 1j * ny) * comp[0] + (1 - nz) * comp[1])
        psi = np.zeros(n, complex); psi[0::2] = np.fft.ifftn(upc).ravel(); psi[1::2] = np.fft.ifftn(dnc).ravel(); psi /= np.linalg.norm(psi)
        p0 = (np.abs(psi[0::2]) ** 2 + np.abs(psi[1::2]) ** 2).reshape(side, side, side)
        z0 = (p0 * pos[2]).sum()
        out_t = expm_multiply(-1j * ham * t_end, psi)
        p = (np.abs(out_t[0::2]) ** 2 + np.abs(out_t[1::2]) ** 2).reshape(side, side, side)
        mean0 = np.array([(p0 * pos[j]).sum() for j in range(3)])
        out[sign] = ((p * pos[2]).sum() / p.sum() - z0, cloud(sign * g, beta, mean0, sig, kvec, t_end, centre))
    return 0.5 * (out[1][0] - out[-1][0]), 0.5 * (out[1][1] - out[-1][1])


def slow_fall(beta, g=0.002, m=0.4, t_end=100.0, n_sites=3000, sig=40.0):
    z = np.arange(n_sites, dtype=float)
    w = np.exp(g * (z - n_sites / 2)); c = w ** (1 + beta)
    rows, cols, vals = [], [], []
    for s1, s2 in ((0, 1), (1, 0)):
        rows.append(2 * np.arange(n_sites) + s1); cols.append(2 * np.arange(n_sites) + s2); vals.append(w * m + 0j)
    amp = np.sqrt(c[1:] * c[:-1])
    up, dn = np.arange(1, n_sites), np.arange(0, n_sites - 1)
    for s, cc in ((0, 1.0), (1, -1.0)):
        rows.append(2 * up + s); cols.append(2 * dn + s); vals.append(0.5j * amp * cc)
        rows.append(2 * dn + s); cols.append(2 * up + s); vals.append(-0.5j * amp * cc)
    ham = coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(2 * n_sites, 2 * n_sites)).tocsr()
    k = 2 * np.pi * np.fft.fftfreq(n_sites)
    gk = np.exp(-(k ** 2) * sig ** 2) * np.exp(-1j * k * n_sites / 2)
    e = np.sqrt(m * m + np.sin(k) ** 2)
    upc, dnc = e + np.sin(k), m * np.ones_like(k); nrm = np.sqrt(upc ** 2 + dnc ** 2)
    psi = np.stack([np.fft.ifft(gk * upc / nrm), np.fft.ifft(gk * dnc / nrm)], axis=1).reshape(-1); psi /= np.linalg.norm(psi)
    p0 = (np.abs(psi) ** 2).reshape(n_sites, 2).sum(axis=1)
    out = expm_multiply(-1j * ham * t_end, psi)
    p = (np.abs(out) ** 2).reshape(n_sites, 2).sum(axis=1)
    return (p * z).sum() / p.sum() - (p0 * z).sum()


if __name__ == "__main__":
    g, t_end = 0.004, 30.0
    print(f"(a) a ray crossing the gradient, 64^3 box, wave vector 0.5 along x, packet width 5, g = {g}, T = {t_end}: the part of the z-displacement odd in g")
    res = {}
    for beta in (0.0, 1.0):
        walk, rays = bending(64, 0.5, g, t_end, 5.0, beta)
        res[beta] = walk
        print(f"    beta = {beta:.0f} ({'lengths locked at 1: c = w' if beta == 0 else 'l = wbar/w: c = w^2/wbar'}): walk {walk:+.4f}; cloud of rays with E = c eps: {rays:+.4f}; walk over cloud {walk / rays:.4f}")
    print(f"    bending with l = wbar/w over bending with locked lengths: {res[1.0] / res[0.0]:.4f} (note T4: 2 at first order in g)")
    print("(b) a slow body on a line, rest energy 0.4 timed by the SITE rate, hops timed by c = w^(1 + beta), g = 0.002, T = 100: fall of the packet")
    falls = {beta: slow_fall(beta) for beta in (0.0, 1.0)}
    print(f"    beta = 0: {falls[0.0]:+.4f}; beta = 1: {falls[1.0]:+.4f}; ratio {falls[1.0] / falls[0.0]:.4f} (note T4: 1 at first order; -g T^2/2 = {-0.5 * 0.002 * 100 ** 2:+.4f})")
