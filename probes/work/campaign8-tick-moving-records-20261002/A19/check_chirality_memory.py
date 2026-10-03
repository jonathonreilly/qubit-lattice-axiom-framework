"""A19: the sublattice bit of the k-th record carries the velocity memory under sharp site cuts.
EXACT claims: E[c_1] = <v(K)> of the packet (band identity |u+_R|^2 - |u+_L|^2 = v(K)); E[c_{k+1}] = r E[c_k],
r = exact direction correlation; so the mean velocity after k records is ~ v0 (1 - sin m) r^(k-1) (long gaps)."""
import numpy as np
from core1d import step, packet, vgroup, Registrar, plus_band, PI
from exact_sharp import sharp_stats
M, j0, w0, T, B = 2048, 700, 20.0, 400, 600
for m, K0, g in ((0.6, 0.3, 0.1), (0.3, 0.1, 0.1), (0.6, -0.5, 0.2)):
    rng = np.random.default_rng(31)
    a0, b0 = packet(M, m, K0, w0, j0)
    Kg = 2 * PI * np.arange(M) / M
    A = np.fft.fft(a0); Bv = np.fft.fft(b0); wt = np.abs(A) ** 2 + np.abs(Bv) ** 2; wt /= wt.sum()
    vbar = np.dot(wt, vgroup(Kg, m))
    a = np.repeat(a0[None], B, 0); b = np.repeat(b0[None], B, 0)
    reg = Registrar(B, M, g, kind="gauss", sig=0.0, rng=rng, x0_cells=j0)
    for t in range(1, T + 1):
        a, b = step(a, b, m); a, b = reg.apply(a, b, t)
    r = sharp_stats(m, g)["r"]
    Ec = []
    for k in range(1, 6):
        cs = [1.0 if np.isclose(tr[k][1] % 1.0, 0.0) else -1.0 for tr in reg.tracks if len(tr) > k]
        Ec.append((np.mean(cs), np.std(cs) / np.sqrt(len(cs))))
    print(f"m={m} K0={K0} g={g}: packet <v> = {vbar:+.4f} (v(K0) = {vgroup(K0, m):+.4f}); exact r = {r:+.4f}")
    print("   k   E[c_k] MC (s.e.)      prediction <v> r^(k-1)")
    for k, (e, se) in enumerate(Ec, 1):
        print(f"   {k}   {e:+.4f} ({se:.4f})      {vbar * r ** (k - 1):+.4f}")
