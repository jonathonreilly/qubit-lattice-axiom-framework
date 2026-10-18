#!/usr/bin/env python3
"""R5 T2: code-natural fixed exponent patterns vs the charged-fermion masses and CKM, with random controls.

m_{f,i} = Lambda_f * eps^{p_i}, p a fixed pattern (light -> heavy). Chebyshev fit in log space.
Masses: the HIER-2 recalled sets (MZ, GUT, MIX). CKM recalled.
"""
import numpy as np

SETS = {
    'MZ':  dict(u=1.27e-3, c=0.619, t=171.7, d=2.90e-3, s=0.055, b=2.89,
                e=0.48657e-3, mu=0.102718, tau=1.74624),
    'GUT': dict(u=0.48e-3, c=0.235, t=74.0, d=1.14e-3, s=0.022, b=1.00,
                e=0.469652e-3, mu=0.0991466, tau=1.68558),
    'MIX': dict(u=2.16e-3, c=1.27, t=172.69, d=4.67e-3, s=0.0934, b=4.18,
                e=0.511e-3, mu=0.1057, tau=1.777),
}
SECT = [('u', 'c', 't'), ('d', 's', 'b'), ('e', 'mu', 'tau')]
PAT = {'LIN': (3, 2, 1), 'CAT2': (4, 2, 1), 'CAT3': (9, 3, 1), 'ODD': (5, 3, 1)}
CKM = dict(us=0.225, cb=0.041, ub=0.0037)
S = -np.exp(np.linspace(np.log(1e-3), np.log(12.0), 2500))  # s = ln eps in [-12, -1e-3]


def sector_err(x, p, s):
    """x: (..., 3) log masses light->heavy; p pattern; s: (k,) grid. returns (..., k) half-ranges."""
    r = x[..., None, :] - np.asarray(p)[None, :] * s[:, None]  # (..., k, 3)
    return (r.max(-1) - r.min(-1)) / 2


def model_A(X):
    """X: (..., 3 sectors, 3) -> best max-dev over patterns with shared eps; returns (dev, pattern, s)."""
    best = None
    for name, p in PAT.items():
        e = np.stack([sector_err(X[..., f, :], p, S) for f in range(3)], -1).max(-1)  # (..., k)
        k = e.argmin(-1)
        d = np.take_along_axis(e, k[..., None], -1)[..., 0]
        if best is None:
            best = (d, np.full(d.shape, name, object), S[k])
        else:
            m = d < best[0]
            best = (np.where(m, d, best[0]), np.where(m, name, best[1]), np.where(m, S[k], best[2]))
    return best


def model_B(X):
    """each sector its own pattern and eps."""
    per = []
    for f in range(3):
        dmin = None
        for p in PAT.values():
            d = sector_err(X[..., f, :], p, S).min(-1)
            dmin = d if dmin is None else np.minimum(dmin, d)
        per.append(dmin)
    return np.max(np.stack(per, -1), -1)


def ckm_fit(p, s_fixed=None):
    t = np.log([CKM['us'], CKM['cb'], CKM['ub']])
    a = np.array([p[0] - p[1], p[1] - p[2], p[0] - p[2]], float)
    if s_fixed is None:
        dev = np.abs(a[None, :] * S[:, None] - t[None, :]).max(1)
        k = dev.argmin()
        return np.exp(dev[k]), np.exp(S[k])
    return np.exp(np.abs(a * s_fixed - t).max()), np.exp(s_fixed)


rng = np.random.default_rng(20261018)
NR = 2000
print('patterns (light->heavy):', PAT)
print('shape statistic R = ln(m1/m3)/ln(m2/m3); pattern R:', {k: (p[0]-p[2])/(p[1]-p[2]) for k, p in PAT.items()})
for name, m in SETS.items():
    X = np.log(np.array([[m[k] for k in sec] for sec in SECT]))
    R = [(X[f, 0] - X[f, 2]) / (X[f, 1] - X[f, 2]) for f in range(3)]
    dA, pA, sA = model_A(X)
    dB = model_B(X)
    print(f'\n=== {name}: observed R (up, down, lep) = ' + ', '.join(f'{r:.2f}' for r in R))
    print(f'  model A (one pattern, one eps, 3 scales; 4 cont. params): best {pA} eps={np.exp(sA):.4f} max factor x{np.exp(dA):.2f}')
    for pn, p in PAT.items():
        e = np.stack([sector_err(X[f], p, S) for f in range(3)], -1).max(-1)
        k = e.argmin()
        fct, epsc = ckm_fit(p)
        fct2, _ = ckm_fit(p, S[k])
        print(f'    {pn:5s}: mass x{np.exp(e[k]):.2f} at eps={np.exp(S[k]):.4f};  CKM (FN reading) best x{fct:.2f} at eps={epsc:.3f}; '
              f'CKM at mass eps x{fct2:.2f}')
    print(f'  model B (pattern and eps per sector; 6 cont. params): max factor x{np.exp(dB):.2f}')
    # random controls
    heavy = X[:, 2]
    # C1: two lighter masses log-uniform over 6 decades below the heaviest
    u = np.sort(rng.uniform(np.log(1e-6), 0, size=(NR, 3, 2)), -1)
    X1 = np.concatenate([heavy[None, :, None] + u, np.broadcast_to(heavy[None, :, None], (NR, 3, 1))], -1)
    # C2: keep lightest and heaviest, middle log-uniform between them (tests shape only)
    lo = X[:, 0]
    mid = lo[None, :] + rng.uniform(0, 1, size=(NR, 3)) * (heavy - lo)[None, :]
    X2 = np.stack([np.broadcast_to(lo, (NR, 3)), mid, np.broadcast_to(heavy, (NR, 3))], -1)
    for cname, XR in (('C1 six-decade', X1), ('C2 span-matched', X2)):
        rA = np.concatenate([model_A(XR[i:i+100])[0] for i in range(0, NR, 100)])
        rB = np.concatenate([model_B(XR[i:i+100]) for i in range(0, NR, 100)])
        print(f'  control {cname}: model A  frac<=x3 {np.mean(rA <= np.log(3)):.3f}, p(F_rand <= F_data) = {np.mean(rA <= dA + 1e-12):.3f};'
              f'  model B frac<=x3 {np.mean(rB <= np.log(3)):.3f}, p = {np.mean(rB <= dB + 1e-12):.3f}')
# CKM random control: random magnitudes log-uniform, ordered |V13| < |V23| < |V12| < 1, over 4 decades
t = np.sort(rng.uniform(np.log(1e-4), 0, size=(NR, 3)), 1)  # ub < cb < us
a_menu = {k: np.array([p[0]-p[1], p[1]-p[2], p[0]-p[2]], float) for k, p in PAT.items()}
best = np.full(NR, np.inf)
for k, a in a_menu.items():
    tt = t[:, [2, 1, 0]]  # us, cb, ub
    dev = np.concatenate([np.abs(a[None, None, :] * S[None, :, None] - tt[i:i+100, None, :]).max(2).min(1) for i in range(0, NR, 100)])
    best = np.minimum(best, dev)
dat = min(np.log(ckm_fit(p)[0]) for p in PAT.values())
print(f'\nCKM random control (log-uniform ordered magnitudes over 4 decades): frac within x3 = {np.mean(best <= np.log(3)):.3f}; '
      f'p(F_rand <= F_data={np.exp(dat):.2f}) = {np.mean(best <= dat + 1e-12):.3f}')
