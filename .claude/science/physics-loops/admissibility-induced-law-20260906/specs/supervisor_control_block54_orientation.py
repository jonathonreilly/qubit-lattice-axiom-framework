"""Block 54 control (supervisor-run; floating point; evidence, not proof): the clocked walk in three dimensions, by orientation.

H_w = sqrt(w) [sum_j sigma_j (x) D_j] sqrt(w) on an open box, w = exp(g (r - centre).ghat).  A positive-energy Gaussian packet of wave vector
k0 along `move` is evolved with +g and with -g; half the difference of the mean positions along ghat is the part of the motion that is odd in the
gradient (the fall).  The same is done for a cloud of rays with the energy function E = w(r) eps(k), eps = sqrt(sum_j sin^2 k_j), and the central
ray's law  dv_j/dt = -w^2 cos(2 k_j) d_j u + 2 (v.grad u) v_j  is quoted next to both.
Also reported: the direction of the content <sigma> against the direction of the velocity <i[H_w, r]> at the start and at the end (the content
follows the direction of travel through the turn).
usage: supervisor_control_block54_orientation.py            (runs the fixed list below)"""
import time

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply

SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]


def cloud(g, gdir, centre, start, sig, kvec, t_end, n=20000, steps=600, seed=54):
    rng = np.random.default_rng(seed)
    dx = sig * rng.standard_normal((n, 3))
    dk = rng.standard_normal((n, 3)) / (2 * sig)
    x = start[None, :] + np.concatenate([dx, -dx, dx, -dx])
    k = kvec[None, :] + np.concatenate([dk, dk, -dk, -dk])
    x0 = x.mean(axis=0)

    def f(x, k):
        s, c = np.sin(k), np.cos(k)
        e = np.sqrt((s * s).sum(axis=1))
        w = np.exp(g * ((x - centre[None, :]) @ gdir))
        return (w / e)[:, None] * s * c, -(e * w * g)[:, None] * gdir[None, :]

    h = t_end / steps
    for _ in range(steps):
        a1, b1 = f(x, k)
        a2, b2 = f(x + 0.5 * h * a1, k + 0.5 * h * b1)
        a3, b3 = f(x + 0.5 * h * a2, k + 0.5 * h * b2)
        a4, b4 = f(x + h * a3, k + h * b3)
        x = x + h * (a1 + 2 * a2 + 2 * a3 + a4) / 6
        k = k + h * (b1 + 2 * b2 + 2 * b3 + b4) / 6
    return x.mean(axis=0) - x0


def content_and_velocity(psi, sw, side):
    a = psi.reshape(side, side, side, 2)
    content = np.array([np.real(np.einsum("xyzs,st,xyzt->", a.conj(), SIG[j], a)) for j in range(3)])
    vel = np.zeros(3)
    for j in range(3):
        lo = [slice(None)] * 3; hi = [slice(None)] * 3
        lo[j] = slice(0, side - 1); hi[j] = slice(1, side)
        amp = sw[tuple(lo)] * sw[tuple(hi)]
        vel[j] = np.real(np.einsum("xyz,xyzs,st,xyzt->", amp, a[tuple(hi)].conj(), SIG[j], a[tuple(lo)]))
    return content / np.linalg.norm(content), vel


def one(side, k0, g, t_end, sig, move, gdir):
    move = np.array(move, float) / np.linalg.norm(move)
    gdir = np.array(gdir, float) / np.linalg.norm(gdir)
    idx = np.arange(side ** 3).reshape(side, side, side)
    pos = np.stack(np.meshgrid(*[np.arange(side, dtype=float)] * 3, indexing="ij"))
    centre = np.array([side / 2.0] * 3)
    kvec = k0 * move
    s0, c0 = np.sin(kvec), np.cos(kvec)
    e0 = np.sqrt((s0 * s0).sum())
    v0 = s0 * c0 / e0
    start = centre - v0 * (0.5 * t_end)
    rel = pos - centre[:, None, None, None]
    out = {}
    for sign in (+1, -1):
        u = sign * g * (rel[0] * gdir[0] + rel[1] * gdir[1] + rel[2] * gdir[2])
        sw = np.exp(0.5 * u)
        rows, cols, vals = [], [], []
        for j in range(3):
            lo = [slice(None)] * 3; hi = [slice(None)] * 3
            lo[j] = slice(0, side - 1); hi[j] = slice(1, side)
            xa, xb = idx[tuple(lo)].ravel(), idx[tuple(hi)].ravel()
            amp = (sw[tuple(lo)] * sw[tuple(hi)]).ravel()
            for s1 in range(2):
                for s2 in range(2):
                    c = SIG[j][s1, s2]
                    if c == 0:
                        continue
                    rows += [2 * xb + s1, 2 * xa + s1]; cols += [2 * xa + s2, 2 * xb + s2]; vals += [0.5j * amp * c, -0.5j * amp * c]
        n = 2 * idx.size
        ham = coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(n, n)).tocsr()
        _, vecs = np.linalg.eigh(sum(s0[j] * SIG[j] for j in range(3)))
        spinor = vecs[:, 1]
        d = pos - start[:, None, None, None]
        env = np.exp(-(d ** 2).sum(axis=0) / (4 * sig ** 2)) * np.exp(1j * (d[0] * kvec[0] + d[1] * kvec[1] + d[2] * kvec[2]))
        comp = [np.fft.fftn(env * spinor[0]), np.fft.fftn(env * spinor[1])]
        kk = 2 * np.pi * np.fft.fftfreq(side)
        kx, ky, kz = np.meshgrid(kk, kk, kk, indexing="ij")
        sx, sy, sz = np.sin(kx), np.sin(ky), np.sin(kz)
        e = np.sqrt(sx * sx + sy * sy + sz * sz); e[e == 0] = 1.0
        nx, ny, nz = sx / e, sy / e, sz / e                                   # projector on the positive-energy branch: (1 + n.sigma)/2
        upc = 0.5 * ((1 + nz) * comp[0] + (nx - 1j * ny) * comp[1])
        dnc = 0.5 * ((nx + 1j * ny) * comp[0] + (1 - nz) * comp[1])
        psi = np.zeros(n, complex)
        psi[0::2] = np.fft.ifftn(upc).ravel(); psi[1::2] = np.fft.ifftn(dnc).ravel()
        psi /= np.linalg.norm(psi)
        p0 = (np.abs(psi[0::2]) ** 2 + np.abs(psi[1::2]) ** 2).reshape(side, side, side)
        mean0 = np.array([(p0 * pos[j]).sum() for j in range(3)])
        psi_t = expm_multiply(-1j * ham * t_end, psi)
        p = (np.abs(psi_t[0::2]) ** 2 + np.abs(psi_t[1::2]) ** 2).reshape(side, side, side)
        mean = np.array([(p * pos[j]).sum() for j in range(3)]) / p.sum()
        edge = p[:2].sum() + p[-2:].sum() + p[:, :2].sum() + p[:, -2:].sum() + p[:, :, :2].sum() + p[:, :, -2:].sum()
        cont0, vel0 = content_and_velocity(psi, sw, side)
        cont1, vel1 = content_and_velocity(psi_t, sw, side)
        out[sign] = ((mean - mean0) @ gdir, cloud(sign * g, gdir, centre, mean0, sig, kvec, t_end) @ gdir, edge, cont0, vel0, cont1, vel1)
    walk = 0.5 * (out[1][0] - out[-1][0])
    rays = 0.5 * (out[1][1] - out[-1][1])
    law = (-(np.cos(2 * kvec) * gdir * gdir).sum() + 2 * (v0 @ gdir) ** 2) * 0.5 * g * t_end ** 2
    _, _, edge, cont0, vel0, cont1, vel1 = out[1]
    ang = lambda a, b: float(np.degrees(np.arccos(np.clip(a @ b / np.linalg.norm(a) / np.linalg.norm(b), -1, 1))))
    return walk, rays, law, edge, ang(vel0, vel1), ang(cont0, cont1), ang(cont1, vel1)


if __name__ == "__main__":
    cases = [((1, 0, 0), (0, 0, 1)), ((1, 1, 0), (0, 0, 1)), ((1, -1, 0), (1, 1, 1)), ((1, 1, -2), (1, 1, 1)), ((2, 1, 0), (1, -2, 3))]
    for side, k0, sig in ((68, 0.5, 5.0), (80, 0.25, 7.0)):
        g, t_end = 0.004, 30.0
        print(f"box {side}^3, wave vector {k0}, packet width {sig}, g = {g}, T = {t_end}; long-wavelength fall -g T^2/2 = {-0.5 * g * t_end ** 2:+.4f}")
        for move, gdir in cases:
            t0 = time.time()
            walk, rays, law, edge, turn_v, turn_c, gap = one(side, k0, g, t_end, sig, move, gdir)
            print(f"    motion along {move}, gradient along {gdir}: fall of the walk {walk:+.4f}; of the cloud of rays {rays:+.4f}; walk over cloud {walk / rays:.4f}; central ray's law {law:+.4f} | the velocity turned by {turn_v:.2f} degrees, the content by {turn_c:.2f}, final angle between them {gap:.2f} | weight near the walls {edge:.0e} | {time.time() - t0:.0f} s")
