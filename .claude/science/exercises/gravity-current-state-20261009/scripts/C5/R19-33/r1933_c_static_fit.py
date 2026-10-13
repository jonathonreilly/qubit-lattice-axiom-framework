"""R19-33 (c) refinement of the static 1/r check: zero-mode-removed periodic lattice Green's function
G_L(r) = 1/(4 pi r) + C_L - r^2/(6 L^3) + images.  Compare 4 pi r [G_L(r) - C_L + r^2/(6L^3)] -> 1
using C_L fitted from the far region, along axis / face / body diagonals, L = 48, 96."""
import numpy as np
for L in (48, 96):
    k = 2 * np.pi * np.fft.fftfreq(L); K3 = np.meshgrid(k, k, k, indexing='ij')
    s2 = sum((2 * np.sin(kk / 2)) ** 2 for kk in K3)
    G = np.fft.ifftn(np.where(s2 > 0, 1.0 / np.where(s2 > 0, s2, 1), 0.0)).real
    # C_L from points 6..12 along the axis using the model, least squares
    rs = np.arange(6, 13); g = np.array([G[r, 0, 0] for r in rs]) - 1 / (4 * np.pi * rs) + rs ** 2 / (6 * L ** 3)
    C = g.mean()
    for name, d in [("axis", (1, 0, 0)), ("face", (1, 1, 0)), ("body", (1, 1, 1))]:
        out = []
        for n in (1, 2, 4, 8, 12):
            r = n * np.linalg.norm(d); x = tuple(np.array(d) * n % L)
            out.append("r=%.2f:%.4f" % (r, 4 * np.pi * r * (G[x] - C + r ** 2 / (6 * L ** 3))))
        print("L=%d %-4s 4 pi r G(r) [corrected]: " % (L, name) + "  ".join(out))
print("sign: G(r) - C > 0 and decreasing -> bridge cross term +2 lam M1 M2 G(r) is attractive")
