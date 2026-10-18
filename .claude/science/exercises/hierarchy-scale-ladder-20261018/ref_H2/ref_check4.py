#!/usr/bin/env python3
"""Referee check 4: per-band closest approach to the band centre, b_k = min_q |E_k(q) - mean| (k = 9..16,
upper half), for multi-charge L1 directions with masses; grid |q_i| <= 3 eps (25^3) + refinement per band.
Orders from eps = 0.01 -> 0.005. Gives the distinct true-gap orders per direction."""
import sys
sys.argv = ['orders_group.py', 'A1-A1']
sys.path.insert(0, '/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/hier/H2/scripts')
import numpy as np
import orders_group as og
from scipy.optimize import minimize
H0b = np.zeros((3, 16, 16), complex)
for s in og.NODES:
    i = og.NID[s]
    for j in range(3): H0b[j, 2*i:2*i+2, 2*i:2*i+2] = ((-1)**s[j]) * og.PAU[j]
def band_min(H, R, n=25):
    xs = np.linspace(-R, R, n); best = np.full(16, np.inf); arg = [None]*16
    for x in xs:
        Q = np.array(np.meshgrid([x], xs, xs, indexing='ij')).reshape(3, -1).T
        e = np.abs(np.linalg.eigvalsh(np.einsum('pj,jab->pab', Q, H0b) + H[None]))
        for k in range(8, 16):
            i = np.argmin(e[:, k])
            if e[i, k] < best[k]: best[k] = e[i, k]; arg[k] = Q[i]
    out = []
    for k in range(8, 16):
        f = lambda q, k=k: abs(np.linalg.eigvalsh(np.einsum('j,jab->ab', q, H0b) + H)[k])
        r = minimize(f, arg[k], method='Nelder-Mead', options=dict(xatol=1e-16, fatol=1e-20, maxiter=3000))
        out.append(min(best[k], r.fun))
    return np.array(out)
keys = list(og.REPS.keys())
for ki, key in enumerate(keys):
    if key[0] != 'hw1': continue
    mats = og.REPS[key]
    for li, (order, phi) in enumerate(og.fixed_lines(mats)):
        tch = [np.allclose(mats[og.GID[(ti, og.oidx(np.eye(3, dtype=int)))]] @ phi, phi) or
               np.allclose(mats[og.GID[(ti, og.oidx(np.eye(3, dtype=int)))]] @ phi, -phi) for ti in range(8)]
        if all(tch): continue   # single-charge: done exactly in check 2
        rng = np.random.default_rng(1000 * ki + 17 * li + 0)
        fs = og.f_eval(og.generic_maps(mats, rng), mats, phi)
        fs = [f / np.linalg.norm(f) if np.linalg.norm(f) > 1e-10 else 0 * f for f in fs]
        bs = []
        for eps in (0.01, 0.005):
            H = sum((eps**(n+1)) * fs[n] for n in range(7)); H = H - np.trace(H).real / 16 * np.eye(16)
            bs.append(band_min(H, 3 * eps))
        ords = []
        for a, b in zip(*bs):
            ords.append('0' if (a < 1e-12 or b < 1e-13) else f"{np.log(a/b)/np.log(2):.1f}")
        print(f"hw1 {key[1]:<4} dir{li}: upper-band closest-approach orders {ords}  (b_k at eps=0.01: {np.array2string(bs[0], precision=1)})")
        sys.stdout.flush()
