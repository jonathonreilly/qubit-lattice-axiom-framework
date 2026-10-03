"""Focused re-test of the displacement z-statistic for m=0.6, g=0.03 sharp site cuts (several seeds), and the same
statistic computed with the first record's state taken directly from |y> (sanity of conditioning)."""
import sys, numpy as np
from core1d import step, packet, Registrar
from check_markov import kernel_moments
M, j0, w0, T, B = 2048, 700, 20.0, 600, 600
m, K0, g = 0.6, 0.3, 0.03
d, sd, q = kernel_moments(m, T)
allz = []
for seed in [int(s) for s in sys.argv[1].split(",")]:
    rng = np.random.default_rng(seed)
    a0, b0 = packet(M, m, K0, w0, j0)
    a = np.repeat(a0[None], B, 0); b = np.repeat(b0[None], B, 0)
    reg = Registrar(B, M, g, kind="gauss", sig=0.0, rng=rng, x0_cells=j0)
    for t in range(1, T + 1):
        a, b = step(a, b, m); a, b = reg.apply(a, b, t)
    z = []
    for tr in reg.tracks:
        tt = np.array([p[0] for p in tr[1:]]); ys = np.array([p[1] for p in tr[1:]])
        c = np.where(np.isclose(ys % 1.0, 0.0), 1.0, -1.0)
        for i in range(ys.size - 1):
            n = int(tt[i + 1] - tt[i]); z.append((c[i] * (ys[i + 1] - ys[i]) - d[n]) / sd[n])
    z = np.array(z); allz.append(z)
    print(f"seed {seed}: {z.size} segments, z mean {z.mean():+.4f} +- {1/np.sqrt(z.size):.4f}, var {z.var():.3f}")
z = np.concatenate(allz)
print(f"pooled: {z.size} segments, z mean {z.mean():+.4f} +- {1/np.sqrt(z.size):.4f}")
