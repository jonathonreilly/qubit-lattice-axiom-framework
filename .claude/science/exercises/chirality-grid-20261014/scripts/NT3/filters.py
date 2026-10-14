"""Filters of PREREG.md (normalised so that <f^2>_BZ = 1 on the infinite lattice for local filters)."""
import numpy as np

def _norm1d(fun, N=1 << 14):
    k = 2 * np.pi * np.arange(N) / N
    return np.sqrt((fun(k) ** 2).mean())

F1D = {
    "F_lo": lambda k: (1 - np.cos(k)) * (1 + 0.6 * np.cos(k)) / 2,
    "F_star": lambda k: (1 - np.cos(k)) / 2,
    "F_hi": lambda k: ((1 - np.cos(k)) / 2) ** 2,
}
NORM1D = {n: _norm1d(f) for n, f in F1D.items()}

def ring_fvals(name, L):
    if name == "C0":
        return {m: 1.0 for m in range(L)}
    if name == "C1":
        return {m: (0.0 if m == 0 else 1.0) for m in range(L)}
    f = F1D[name]
    return {m: float(f(2 * np.pi * m / L)) / NORM1D[name] for m in range(L)}

def f_NN3(p):
    return (1 - np.cos(p).sum(0)) / 2

def f_F13(p):
    s2, c2 = np.sin(p / 2) ** 2, np.cos(p / 2) ** 2
    return 1 - (s2[0] * c2[1] * c2[2] + s2[1] * c2[0] * c2[2] + s2[2] * c2[0] * c2[1])

def _norm3d(fun, N=64):
    k = 2 * np.pi * np.arange(N) / N
    acc = 0.0
    for kx in k:
        p = np.stack(np.meshgrid(np.array([kx]), k, k, indexing="ij"))
        acc += (fun(p) ** 2).sum()
    return np.sqrt(acc / N ** 3)

F3D = {"f_NN": f_NN3, "f_F1": f_F13}
NORM3D = {n: _norm3d(f) for n, f in F3D.items()}

def cube_fvals(name):
    out = {}
    for i in range(8):
        p = np.pi * np.array([(i >> 0) & 1, (i >> 1) & 1, (i >> 2) & 1], float).reshape(3, 1)
        out[i] = float(F3D[name](p)[0]) / NORM3D[name]
    return out
