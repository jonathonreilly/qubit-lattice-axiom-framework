#!/usr/bin/env python3
"""h5b: POST-HOC diagnostic (written after h5's B3 FAILED; not a criterion change). Separates the noise floor of d(M)
at small y from its scaling: slope of |arg det M| vs y (predicted 3, noise-free), and slope of d vs y on y >= 0.04."""
import numpy as np, time, resource
from scipy.linalg import expm
rng = np.random.default_rng(7)
def rand_su(N):
    H = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N)); Y = (H - H.conj().T) / 2
    Y -= np.trace(Y) / N * np.eye(N); return Y / np.linalg.norm(Y)
def Pi(Z):
    N = Z.shape[0]; A = (Z - Z.conj().T) / 2; return A - np.trace(A) / N * np.eye(N)
def dM(M):
    N = M.shape[0]; X = np.zeros((N, N), complex)
    for it in range(400):
        G = Pi(expm(-X) @ M); X = X + G
        if np.linalg.norm(G) < 1e-15: break
    trP = np.sum(np.linalg.svd(M, compute_uv=False))
    return (trP - np.real(np.trace(expm(-X) @ M))) / N
t0 = time.time(); YS = np.array([0.02, 0.04, 0.08, 0.16, 0.32]); sa, sd, sd2, cmax = [], [], [], 0.0
for s in range(50):
    dirs = [rand_su(3) for _ in range(8)]; us = rng.uniform(0.2, 1.0, 8)
    al, ds = [], []
    for y in YS:
        M = sum(expm(y * u * D) for D, u in zip(dirs, us)) / 8
        al.append(abs(np.angle(np.linalg.det(M)))); ds.append(dM(M))
        cmax = max(cmax, al[-1] / y ** 3) if y <= 0.05 else cmax
    al, ds = np.array(al), np.array(ds)
    sa.append(np.polyfit(np.log(YS[:4]), np.log(al[:4]), 1)[0])
    if np.all(ds[1:4] > 0): sd.append(np.polyfit(np.log(YS[1:4]), np.log(ds[1:4]), 1)[0])
    if np.all(ds[2:] > 0): sd2.append(np.polyfit(np.log(YS[2:]), np.log(ds[2:]), 1)[0])
print(f"|alpha| slope (y=0.02..0.16): median {np.median(sa):.3f}, range {min(sa):.3f}..{max(sa):.3f}; max |alpha|/y^3 at y<=0.04: {cmax:.3f}")
print(f"d slope (y=0.04..0.16): median {np.median(sd):.3f} (n={len(sd)}), range {min(sd):.2f}..{max(sd):.2f}")
print(f"d slope (y=0.08..0.32): median {np.median(sd2):.3f} (n={len(sd2)}), range {min(sd2):.2f}..{max(sd2):.2f}")
print(f"time {time.time()-t0:.1f} s; peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576:.0f} MB")
