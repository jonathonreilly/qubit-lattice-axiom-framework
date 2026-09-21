"""Block 51 control (floating point; not the runner): the stationary creeping inflow towards a point sink when the viscous operator has cubic symmetry,
    0 = -d_i P + nu (Laplacian g_i) + nu_c (d_i^2 g_i)   (no sum in the last term),     div g = -S delta,
solved in Fourier space on a periodic grid (usage: supervisor_control_block51_cubic_inflow.py N rmin rmax sigma; the sink is smeared over sigma sites).  Output: the radial inflow times r^2, averaged over the sites with r in [rmin, rmax] within
15 degrees of an axis, of a face diagonal, of a body diagonal, as a function of eta = nu_c/nu.  eta = 0 is the isotropic potential flow.
The lattice streaming of the record gas gives, in local equilibrium, nu_lat (Laplacian g_i + d_i^2 g_i) with nu_lat = sqrt3/16, that is eta = 1
when collisions add nothing, and eta = nu_lat/(nu_lat + nu_coll) otherwise."""
import sys
import numpy as np

N = int(sys.argv[1]) if len(sys.argv) > 1 else 96
rmin, rmax = (float(sys.argv[2]), float(sys.argv[3])) if len(sys.argv) > 3 else (6.0, 10.0)
SIGMA = float(sys.argv[4]) if len(sys.argv) > 4 else 1.5
k1 = 2 * np.pi * np.fft.fftfreq(N)
KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing="ij")
K = [KX, KY, KZ]
k2 = KX ** 2 + KY ** 2 + KZ ** 2
k2[0, 0, 0] = 1.0
idx = np.indices((N, N, N))
rel = np.stack([(idx[a] + N // 2) % N - N // 2 for a in range(3)]).astype(float)
r = np.sqrt((rel ** 2).sum(axis=0)); r[0, 0, 0] = 1.0
rhat = rel / r
shell = (r >= rmin) & (r <= rmax)
classes = {"axis": [(1, 0, 0), (0, 1, 0), (0, 0, 1)], "face diagonal": [(1, 1, 0), (1, 0, 1), (0, 1, 1), (1, -1, 0), (1, 0, -1), (0, 1, -1)],
           "body diagonal": [(1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]}
cos15 = np.cos(np.radians(15.0))
print(f"grid {N}^3, shell r in [{rmin}, {rmax}]")
for eta in (0.0, 0.25, 0.5, 0.75, 1.0, 2.0):
    denom = [k2 + eta * K[i] ** 2 for i in range(3)]
    s = sum(K[i] ** 2 / denom[i] for i in range(3)); s[0, 0, 0] = 1.0
    phat = np.exp(-0.5 * SIGMA ** 2 * k2) / s                       # pressure for a unit sink smeared over SIGMA sites (removes the ringing of a sharp cubic cut-off)
    g = [np.real(np.fft.ifftn(-1j * K[i] * phat / denom[i])) for i in range(3)]
    gr = -(g[0] * rhat[0] + g[1] * rhat[1] + g[2] * rhat[2]) * r ** 2
    out = []
    for name, dirs in classes.items():
        sel = np.zeros((N, N, N), bool)
        for d in dirs:
            u = np.array(d, float); u /= np.linalg.norm(u)
            sel |= np.abs(rhat[0] * u[0] + rhat[1] * u[1] + rhat[2] * u[2]) > cos15
        sel &= shell
        out.append(gr[sel].mean())
    out = np.array(out); norm = abs(gr[shell].mean())
    print(f"eta = {eta:4.2f}: inflow r^2 over its shell mean: axis {abs(out[0]) / norm:.3f}, face diagonal {abs(out[1]) / norm:.3f}, body diagonal {abs(out[2]) / norm:.3f}; axis over body diagonal {out[0] / out[2]:.3f}")
