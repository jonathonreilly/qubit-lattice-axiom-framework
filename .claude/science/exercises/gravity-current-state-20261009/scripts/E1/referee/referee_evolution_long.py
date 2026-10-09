"""Longer independent-seed replication of the E1 4D explicit recurrence.

The purpose is limited: check whether the finite-epsilon growth persists past
the worker's last window centres, and expose realization-to-realization spread.
It is not an extrapolation to physical epsilon.
"""

import sys
from math import sqrt

import numpy as np

from bd_core import bd4d_weights, csr_apply, evolve, sprinkle4d


eps = float(sys.argv[1]) if len(sys.argv) > 1 else 0.2
T = float(sys.argv[2]) if len(sys.argv) > 2 else 13.5
nreal = int(sys.argv[3]) if len(sys.argv) > 3 else 12
seed = int(sys.argv[4]) if len(sys.argv) > 4 else 812810
lam = 0.8
tcs = np.arange(4.5, 10.51, 1.0)
rng = np.random.default_rng(seed)
opened = {tc: [] for tc in tcs}
closed = {tc: [] for tc in tcs}

for realization in range(nreal):
    points = sprinkle4d(1 / eps, T, rng)
    tau = np.sqrt(np.maximum(points[:, 0] ** 2 - (points[:, 1:] ** 2).sum(1), 0))
    targets = np.arange(len(points))
    indptr, indices, weights = bd4d_weights(points, targets, eps)
    phi = evolve(indptr, indices, weights, targets, np.ones(len(points)), tau < 3.0)
    d_open = csr_apply(indptr, indices, weights, np.ones(len(points))) - 1
    d_closed = phi - 1
    radius = np.sqrt((points[:, 1:] ** 2).sum(1))
    current = []
    for tc in tcs:
        dt = points[:, 0] - tc
        select = (np.abs(dt) < 2.5 * lam) & (radius < 2.5 * lam) & (tau >= 3.0)
        wt = np.exp(-(dt[select] ** 2 + radius[select] ** 2) / (2 * lam**2))
        opened[tc].append(np.dot(wt, d_open[select]) / wt.sum())
        closed[tc].append(np.dot(wt, d_closed[select]) / wt.sum())
        current.append(closed[tc][-1])
    print(
        f"realization={realization + 1:02d} N={len(points)} closed="
        + " ".join(f"{value:+.5g}" for value in current),
        flush=True,
    )

print(f"== eps={eps} T={T} nreal={nreal} lambda={lam} ==")
log_rms = []
for tc in tcs:
    oo = np.asarray(opened[tc])
    cc = np.asarray(closed[tc])
    rms_o = sqrt(np.mean(oo**2))
    rms_c = sqrt(np.mean(cc**2))
    log_rms.append(np.log(rms_c))
    print(
        f"tc={tc:4.1f} open_rms={rms_o:.6g} closed_rms={rms_c:.6g} "
        f"closed_median_abs={np.median(np.abs(cc)):.6g} "
        f"closed_q25_q75=({np.quantile(cc,.25):+.6g},{np.quantile(cc,.75):+.6g})"
    )

exp_fit = np.polyfit(tcs, log_rms, 1)
pow_fit = np.polyfit(np.log(tcs), log_rms, 1)
exp_rss = np.sum((log_rms - np.polyval(exp_fit, tcs)) ** 2)
pow_rss = np.sum((log_rms - np.polyval(pow_fit, np.log(tcs))) ** 2)
print(f"exp_rate={exp_fit[0]:.6g} logRSS={exp_rss:.6g}")
print(f"power={pow_fit[0]:.6g} logRSS={pow_rss:.6g}")
