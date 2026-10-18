#!/usr/bin/env python3
"""Referee check 3: the hw1 Eg dir2 direction (sv-orders [1]); is there a true gap at order eps^2?
Gap at the common Fermi level G = min_q min_k |E_k(q) - mean|, and direct band-centre gap, by a grid over
|q_i| <= 3 eps (41^3 points, vectorised) plus Nelder-Mead refinement; also the order-1-only Hamiltonian."""
import sys
sys.argv = ['orders_group.py', 'A1-A1']
sys.path.insert(0, '/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/hier/H2/scripts')
import numpy as np
import orders_group as og
from scipy.optimize import minimize
targets = [('hw1', 'Eg', 2), ('hw1', 'A1g', 0), ('hw1', 'B2g', 0)]
keys = list(og.REPS.keys())
H0b = np.zeros((3, 16, 16), complex)
for s in og.NODES:
    i = og.NID[s]
    for j in range(3): H0b[j, 2*i:2*i+2, 2*i:2*i+2] = ((-1)**s[j]) * og.PAU[j]
def grid_min(H, R, n=31, kind='fermi'):
    xs = np.linspace(-R, R, n); best = (np.inf, None)
    for x in xs:
        Q = np.array(np.meshgrid([x], xs, xs, indexing='ij')).reshape(3, -1).T
        A = np.einsum('pj,jab->pab', Q, H0b) + H[None]
        e = np.linalg.eigvalsh(A)
        v = np.min(np.abs(e), axis=1) if kind == 'fermi' else (e[:, 8] - e[:, 7]) / 2
        k = np.argmin(v)
        if v[k] < best[0]: best = (v[k], Q[k])
    f = (lambda q: np.min(np.abs(np.linalg.eigvalsh(np.einsum('j,jab->ab', q, H0b) + H)))) if kind == 'fermi' else \
        (lambda q: (lambda e: (e[8] - e[7]) / 2)(np.linalg.eigvalsh(np.einsum('j,jab->ab', q, H0b) + H)))
    r = minimize(f, best[1], method='Nelder-Mead', options=dict(xatol=1e-16, fatol=1e-20, maxiter=4000))
    return min(best[0], r.fun), r.x
for (kind, irr, li) in targets:
    ki = keys.index((kind, irr)); mats = og.REPS[(kind, irr)]
    phi = og.fixed_lines(mats)[li][1]
    rng = np.random.default_rng(1000 * ki + 17 * li + 0)
    fs = og.f_eval(og.generic_maps(mats, rng), mats, phi)
    fs = [f / np.linalg.norm(f) if np.linalg.norm(f) > 1e-10 else 0 * f for f in fs]
    print(f"== {kind} {irr} dir{li}: |Stab|={len(og.stab(mats, phi))} ||f_n||: {[round(float(np.linalg.norm(f)),3) for f in fs]}")
    for label, nmax in (('order-1 only', 1), ('orders 1-2', 2), ('all orders <=7', 7)):
        row = []
        for eps in (0.02, 0.01, 0.005):
            H = sum((eps**(n+1)) * fs[n] for n in range(nmax)); H = H - np.trace(H).real / 16 * np.eye(16)
            gF, qF = grid_min(H, 3 * eps, kind='fermi'); gD, _ = grid_min(H, 3 * eps, kind='direct')
            row.append((eps, gF, gD, np.linalg.norm(qF)))
        sl = lambda a, b: (np.log(a / b) / np.log(2)) if (a > 1e-13 and b > 1e-13) else float('nan')
        print(f"  {label:<15} " + "  ".join(f"eps={e}: Fermi-gap={gF:.2e} direct={gD:.2e} |q*|={qn:.1e}" for e, gF, gD, qn in row)
              + f"   slopes Fermi {sl(row[1][1], row[2][1]):.2f} direct {sl(row[1][2], row[2][2]):.2f}")
    eps = 0.01; H = sum((eps**(n+1)) * fs[n] for n in range(7)); H = H - np.trace(H).real / 16 * np.eye(16)
    print("  q=0 levels at eps=0.01:", np.array2string(np.linalg.eigvalsh(H), precision=2))
    sys.stdout.flush()
