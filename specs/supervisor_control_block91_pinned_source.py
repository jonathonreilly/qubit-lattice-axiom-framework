#!/usr/bin/env python3
"""Supervisor control for block 91 (disjoint machinery: floating point; evidence, not proof).

W1: the Ising ladder of the runner's family D in floating point: the response 2 beta N^-1 <|S_+^(k)|^2> times E_1(k) at t = 4 and 9/4
    (how far below the upper bound 1 the smallest instance sits).
W2: the response to a pinned source MODE BY MODE under light-cone formation on L^3 planes (my simulator of block 90, two copies with common
    random numbers, the second with a transverse source h at the origin added to the rule's argument, V = beta (S + h t1)); R^(k) E(k) by
    |k| shell against the window [m^2/<P_b>, 1] (and the weaker [m^2, 1]), m = the unperturbed copy's mean record direction and <P_b> the
    correlation s_par s'_par + (1/2) s_perp.s'_perp of a record with a displaced predecessor (time averages).
"""
import math
import sys

import numpy as np


def w1():
    print("W1: Ising ladder (4 rungs), response x E_1(k) (upper bound 1)")
    size = 4
    verts = [(x, b) for x in range(size) for b in (0, 1)]
    led = [((x, b), ((x + 1) % size, b)) for x in range(size) for b in (0, 1)] + [((x, 0), (x, 1)) for x in range(size)]
    import itertools
    for t in (4.0, 2.25):
        beta = math.log(t)
        Z = 0.0
        acc = np.zeros(size)
        for sv in itertools.product((1, -1), repeat=len(verts)):
            s = dict(zip(verts, sv))
            w = t ** sum(s[p] * s[q] for p, q in led)
            Z += w
            sp_ = np.array([(s[(x, 0)] + s[(x, 1)]) / 2 for x in range(size)])
            f = np.fft.fft(sp_)
            acc += w * np.abs(f) ** 2
        S = acc / Z / size
        row = []
        for n in (1, 2, 3):
            E1 = 2 - 2 * math.cos(2 * math.pi * n / size)
            row.append(f"k={n}pi/2: {2 * beta * S[n] * E1:.4f}")
        print(f"  t={t}: " + "; ".join(row))


def sample_sphere_exp(V, U, ph):
    kap = np.linalg.norm(V, axis=1)
    kap = np.where(kap < 1e-12, 1e-12, kap)
    uu = V / kap[:, None]
    w = np.clip(1.0 + np.log(U + (1.0 - U) * np.exp(-2.0 * kap)) / kap, -1.0, 1.0)
    a = np.where((np.abs(uu[:, 0]) < 0.9)[:, None], np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
    b1 = a - (a * uu).sum(1)[:, None] * uu
    b1 /= np.linalg.norm(b1, axis=1)[:, None]
    b2 = np.cross(uu, b1)
    r = np.sqrt(np.clip(1 - w * w, 0, 1))
    return w[:, None] * uu + r[:, None] * (np.cos(ph)[:, None] * b1 + np.sin(ph)[:, None] * b2)


def w2_run(L, beta, h, eps, T, T0, seed):
    """Both copies carry a uniform field eps along z at every site (V = beta (S + eps z)); the second also the source h along x at the origin.
    Fixed axes throughout: m_z = <mean s_z>, P_b = <s^x s^x' + s^z s^z'> on the bonds to displaced predecessors, R along x."""
    rng = np.random.default_rng(seed)
    N = L ** 3
    s0 = np.zeros((L, L, L, 3))
    s0[..., 2] = 1.0
    s1 = s0.copy()
    t1 = np.array([1.0, 0.0, 0.0])
    ez = np.array([0.0, 0.0, 1.0])
    acc = np.zeros((L, L, L))
    mzs = []
    pbs = []
    drift = []
    cnt = 0
    for t in range(T):
        U = rng.random(N)
        ph = 2 * np.pi * rng.random(N)
        prev = s0.copy()
        new = []
        for idx, s in enumerate((s0, s1)):
            S = s.copy()
            for ax in range(3):
                S += np.roll(s, 1, axis=ax) + np.roll(s, -1, axis=ax)
            V = beta * (S + eps * ez)
            if idx == 1:
                V[0, 0, 0] += beta * h * t1
            new.append(sample_sphere_exp(V.reshape(-1, 3), U, ph).reshape(L, L, L, 3))
        s0, s1 = new
        if t >= T0:
            acc += (s1 - s0) @ t1
            mvec = s0.mean(axis=(0, 1, 2))
            mzs.append(mvec[2])
            drift.append(abs(mvec[0]) / max(np.linalg.norm(mvec), 1e-12))
            pb = 0.0
            for ax in range(3):
                for sh in (1, -1):
                    nb = np.roll(prev, sh, axis=ax)
                    pb += np.mean(s0[..., 0] * nb[..., 0] + s0[..., 2] * nb[..., 2])
            pbs.append(pb / 6)
            cnt += 1
    R = acc / cnt / h
    R -= R.mean()
    Rk = np.real(np.fft.fftn(R))
    k = 2 * np.pi * np.fft.fftfreq(L)
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    E = 6 - 2 * (np.cos(kx) + np.cos(ky) + np.cos(kz))
    kk = np.sqrt(np.minimum(np.abs(kx), 2 * np.pi - np.abs(kx)) ** 2 + np.minimum(np.abs(ky), 2 * np.pi - np.abs(ky)) ** 2 + np.minimum(np.abs(kz), 2 * np.pi - np.abs(kz)) ** 2)
    mz = float(np.mean(mzs))
    pb = float(np.mean(pbs))
    rows = []
    for lo, hi in ((0.0, 0.5), (0.5, 1.0), (1.0, 1.5), (1.5, 2.2), (2.2, 3.2), (3.2, 6.0)):
        sel = (kk > 1e-9) & (kk >= lo) & (kk < hi)
        if sel.sum():
            meas = float(np.mean(Rk[sel] * E[sel]))
            low = float(np.mean(mz * mz / (pb + eps * mz / E[sel])))
            rows.append(f"[{lo},{hi}): {meas:.3f} vs lower {low:.3f}")
    print(f"  L={L} beta={beta} h={h} eps={eps} T={T}: m_z = {mz:.4f}, <P_b> = {pb:.4f}, m_z^2 = {mz*mz:.4f}, max drift |m_x|/|m| = {max(drift):.3f}; R^(k)E(k) by shell vs lower bound (upper 1): " + "; ".join(rows), flush=True)


def main():
    w1()
    print("W2: response to a pinned source mode by mode, with a small uniform field (window [m_z^2/(<P_b> + eps m_z/E(k)), 1] per mode)")
    for beta, h in ((1.0, 0.1), (2.0, 0.1), (2.0, 0.05), (3.0, 0.1), (3.0, 0.05), (3.0, 0.5)):
        w2_run(16, beta, h, 0.02, 3000, 1000, seed=91 + int(10 * beta))


if __name__ == "__main__":
    sys.exit(main())
