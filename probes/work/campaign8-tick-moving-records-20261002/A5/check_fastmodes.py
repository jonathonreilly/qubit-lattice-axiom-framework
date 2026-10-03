#!/usr/bin/env python3
"""Lane T check H: do grid-scale modes outrun low-energy light? Fixed-order conveyor step U=e^{-ikx sx}e^{-iky sy}e^{-ikz sz}.
Low-k speed is exactly 1 in every direction (w ~ |k|); per-tick neighbourhood = 8 body-diagonal sites (cube hull).
Group velocity from cos w = cx cy cz - sx sy sz:  grad w = -grad(cos w)/sin w. Scan a 3D k-grid for max |v|."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np
n = 81
g = np.linspace(-np.pi, np.pi, n)
kx, ky, kz = np.meshgrid(g, g, g, indexing='ij')
c = [np.cos(kx), np.cos(ky), np.cos(kz)]
s = [np.sin(kx), np.sin(ky), np.sin(kz)]
F = c[0]*c[1]*c[2] - s[0]*s[1]*s[2]
sw = np.sqrt(np.clip(1 - F**2, 0, None))
dF = [-s[0]*c[1]*c[2] - c[0]*s[1]*s[2], -c[0]*s[1]*c[2] - s[0]*c[1]*s[2], -c[0]*c[1]*s[2] - s[0]*s[1]*c[2]]
ok = sw > 1e-3
v = np.stack([-d[ok]/sw[ok] for d in dF])
speed = np.linalg.norm(v, axis=0)
i = np.argmax(speed)
print("max |v| over grid = %.4f at k/pi = %s, v = %s" % (speed[i], np.round(np.array([kx[ok][i], ky[ok][i], kz[ok][i]])/np.pi, 3), np.round(v[:, i], 4)))
print("max |v_x|+|v_y|+|v_z| = %.4f ; max over components |v_i| = %.4f (cube hull requires <= 1 per component)" % (np.max(np.abs(v).sum(0)), np.max(np.abs(v))))
print("fraction of grid points with |v| > 1: %.4f" % np.mean(speed > 1 + 1e-9))
