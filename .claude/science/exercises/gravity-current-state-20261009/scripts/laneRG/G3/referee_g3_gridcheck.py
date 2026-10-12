"""Order-of-limits check for the sawtooth-flow basketball table."""

import numpy as np
from scipy.stats import qmc


PI = np.pi
saw = lambda x: (x + PI) % (2 * PI) - PI


def flow(momentum, eps, nsteps=16):
    x = momentum[..., 0].copy()
    y = momentum[..., 1].copy()
    step = 1 / nsteps
    for _ in range(nsteps):
        xm = saw(x + 0.5 * step * eps * saw(y))
        ym = saw(y + 0.5 * step * eps * saw(x))
        x = saw(x + step * eps * saw(ym))
        y = saw(y + step * eps * saw(xm))
    out = momentum.copy()
    out[..., 0] = x
    out[..., 1] = y
    return out


def weight(momentum, slac):
    if slac:
        omega = np.sqrt(1 + np.sum(saw(momentum) ** 2, axis=-1))
    else:
        omega = np.sqrt(1 + 4 * np.sum(np.sin(momentum / 2) ** 2, axis=-1))
    return 1 / (omega.sum(axis=1) * np.prod(2 * omega, axis=1))


unit = qmc.Sobol(9, scramble=True, seed=77).random_base2(19)
eps = 0.04
for size in [15, 19, 31, 63, 127]:
    n123 = (np.floor(unit * size).astype(int) - (size - 1) // 2).reshape(-1, 3, 3)
    n4 = (-n123.sum(axis=1) + (size - 1) // 2) % size - (size - 1) // 2
    momenta = np.concatenate([2 * PI * n123 / size, (2 * PI * n4 / size)[:, None, :]], axis=1)
    normal = np.all(n123.sum(axis=1) + n4 == 0, axis=1)
    for slac in [False, True]:
        w0 = weight(momenta, slac)
        delta = 0.5 * (weight(flow(momenta, eps), slac) + weight(flow(momenta, -eps), slac)) - w0
        mu_n = -np.mean(np.where(normal, delta, 0.0)) / (12 * eps**2)
        mu_u = -np.mean(np.where(~normal, delta, 0.0)) / (12 * eps**2)
        print(size, "SLAC" if slac else "KG", f"mu_N={mu_n:+.6e}", f"mu_U={mu_u:+.6e}")
