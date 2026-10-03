#!/usr/bin/env python3
"""A19 check: censoring-free test of the exact Markov reduction for sharp site cuts, plus the massless control.

For each observed segment (record i -> record i+1, gap n), compare with the exact single-site kernel at that n:
  z1 = (c_i*Delta - d(n)) / sd(n),  z2 = (f - q(n)) / sqrt(q(n)(1-q(n)))   (f = sublattice changed)
Means of z1, z2 should be 0 within 1/sqrt(#segments); variances should be 1.  Conditioning on n removes the
window-censoring bias of raw per-segment means.  Also: gap distribution is Geometric(g) (registration chance per
tick is exactly g, state-independent).
Massless control (m = 0): any cut leaves a straight track at exactly 1 cell/tick (chirality never flips).
"""
import numpy as np
from core1d import step, packet, Registrar

M, j0, w0, T, B = 2048, 700, 20.0, 600, 300


def kernel_moments(m, nmax):
    a = np.zeros((1, 4 * nmax + 64), complex); b = np.zeros_like(a)
    Mk = a.shape[1]; c0 = Mk // 2
    a[0, c0] = 1
    x = np.arange(Mk) - c0
    d, s2, q = np.zeros(nmax + 1), np.zeros(nmax + 1), np.zeros(nmax + 1)
    for n in range(1, nmax + 1):
        a, b = step(a, b, m)
        pa, pb = np.abs(a[0]) ** 2, np.abs(b[0]) ** 2
        mean = np.dot(pa, x) + np.dot(pb, x + 0.5)
        d[n] = mean
        s2[n] = np.dot(pa, x ** 2) + np.dot(pb, (x + 0.5) ** 2) - mean ** 2
        q[n] = pb.sum()
    return d, np.sqrt(s2), q


if __name__ == "__main__":
    for m, K0, g in ((0.6, 0.3, 0.03), (0.6, 0.3, 0.1), (1.4, 0.8, 0.03), (0.15, 0.1, 0.05)):
        rng = np.random.default_rng(int(__import__("sys").argv[1]) if len(__import__("sys").argv) > 1 else 7)
        a0, b0 = packet(M, m, K0, w0, j0)
        a = np.repeat(a0[None], B, 0); b = np.repeat(b0[None], B, 0)
        reg = Registrar(B, M, g, kind="gauss", sig=0.0, rng=rng, x0_cells=j0)
        for t in range(1, T + 1):
            a, b = step(a, b, m)
            a, b = reg.apply(a, b, t)
        d, sd, q = kernel_moments(m, T)
        z1, z2, gaps = [], [], []
        for tr in reg.tracks:
            tt = np.array([p[0] for p in tr[1:]]); ys = np.array([p[1] for p in tr[1:]])
            if ys.size < 2:
                continue
            c = np.where(np.isclose(ys % 1.0, 0.0), 1.0, -1.0)
            for i in range(ys.size - 1):
                n = int(tt[i + 1] - tt[i])
                gaps.append(n)
                z1.append((c[i] * (ys[i + 1] - ys[i]) - d[n]) / sd[n])
                f = 1.0 if c[i + 1] != c[i] else 0.0
                if 0 < q[n] < 1:
                    z2.append((f - q[n]) / np.sqrt(q[n] * (1 - q[n])))
        z1, z2, gaps = map(np.array, (z1, z2, gaps))
        print(f"m={m} K0={K0} g={g}: {z1.size} segments; displacement z: mean {z1.mean():+.4f} +- {1/np.sqrt(z1.size):.4f}, "
              f"var {z1.var():.3f};  flip z: mean {z2.mean():+.4f} +- {1/np.sqrt(z2.size):.4f}, var {z2.var():.3f};  "
              f"mean gap {gaps.mean():.2f} (censored window; 1/g = {1/g:.1f})")

    # gap law: registration chance per tick is exactly g whatever the state -> P(gap = n) = g(1-g)^(n-1)
    rng = np.random.default_rng(1000 + (int(__import__("sys").argv[1]) if len(__import__("sys").argv) > 1 else 3))
    g, m = 0.2, 0.6
    a0, b0 = packet(M, m, 0.3, w0, j0)
    a = np.repeat(a0[None], B, 0); b = np.repeat(b0[None], B, 0)
    reg = Registrar(B, M, g, kind="gauss", sig=16.0, rng=rng, x0_cells=j0)
    for t in range(1, 301):
        a, b = step(a, b, m)
        a, b = reg.apply(a, b, t)
    first = np.array([tr[1][0] for tr in reg.tracks if len(tr) > 1])
    print(f"first-registration tick: mean {first.mean():.3f} +- {first.std()/np.sqrt(first.size):.3f} (geometric 1/g = {1/g:.3f}); "
          f"P(first = 1) = {np.mean(first == 1):.3f} (g = {g})")

    # massless control: m = 0, site cuts and coarse cuts, K0 = 0.3 (v = +1 exactly)
    for kw in (dict(kind="gauss", sig=0.0), dict(kind="block", s=2), dict(kind="gauss", sig=8.0)):
        rng = np.random.default_rng(5)
        a0, b0 = packet(M, 0.0, 0.3, w0, j0)
        a = np.repeat(a0[None], 50, 0); b = np.repeat(b0[None], 50, 0)
        reg = Registrar(50, M, 0.3, rng=rng, x0_cells=j0, **kw)
        for t in range(1, 301):
            a, b = step(a, b, 0.0)
            a, b = reg.apply(a, b, t)
        sl = []
        for tr in reg.tracks:
            tt = np.array([p[0] for p in tr[1:]], float); ys = np.array([p[1] for p in tr[1:]])
            if ys.size > 2:
                sl.append(np.polyfit(tt, ys, 1)[0])
        sl = np.array(sl)
        dev = max(np.abs(np.diff([p[1] - p[0] for p in tr[1:]])).max() for tr in reg.tracks if len(tr) > 3)
        print(f"massless m=0 cut={kw}: track slopes mean {sl.mean():.6f}, sd {sl.std():.2e}; "
              f"max change of (Y - t) along a track: {dev:.2e} cells")
