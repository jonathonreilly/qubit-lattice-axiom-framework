"""Direct check of the diagonal/independence closure used by E1's renewal model.

For d_x = eta_x + sum_y w_xy d_y, compare the actual feedback square with
the diagonal approximation sum_y w_xy^2 d_y^2 and retain the source-feedback
cross term.  A renewal closure needs both omitted contributions to be small.
"""

import sys
from math import sqrt

import numpy as np

from bd_core import bd4d_weights, csr_apply, evolve, sprinkle4d


def run(eps, T, nreal, seed):
    rng = np.random.default_rng(seed)
    bins = np.arange(3.0, T + 0.001, 1.0)
    rows = [[] for _ in bins[:-1]]
    for realization in range(nreal):
        points = sprinkle4d(1 / eps, T, rng)
        tau = np.sqrt(np.maximum(points[:, 0] ** 2 - (points[:, 1:] ** 2).sum(1), 0))
        targets = np.arange(len(points))
        indptr, indices, weights = bd4d_weights(points, targets, eps)
        phi = evolve(indptr, indices, weights, targets, np.ones(len(points)), tau < 3.0)
        dev = phi - 1
        eta = csr_apply(indptr, indices, weights, np.ones(len(points))) - 1

        feedback = np.zeros(len(points))
        diagonal = np.zeros(len(points))
        signed_sum = np.zeros(len(points))
        squared_sum = np.zeros(len(points))
        for a in range(len(points)):
            lo, hi = indptr[a], indptr[a + 1]
            ww = weights[lo:hi]
            yy = indices[lo:hi]
            feedback[a] = np.dot(ww, dev[yy])
            diagonal[a] = np.dot(ww * ww, dev[yy] * dev[yy])
            signed_sum[a] = ww.sum()
            squared_sum[a] = np.dot(ww, ww)

        for k in range(len(bins) - 1):
            mask = (tau >= bins[k]) & (tau < bins[k + 1])
            # d_x^2 = eta^2 + feedback^2 + 2 eta*feedback exactly.
            rows[k].append(
                np.column_stack(
                    [
                        dev[mask] ** 2,
                        eta[mask] ** 2,
                        feedback[mask] ** 2,
                        diagonal[mask],
                        2 * eta[mask] * feedback[mask],
                        signed_sum[mask],
                        squared_sum[mask],
                    ]
                )
            )
        print(f"finished eps={eps} realization={realization + 1}/{nreal} N={len(points)}", flush=True)

    print(f"== eps={eps} T={T} nreal={nreal} ==")
    print("bin n E[d2] E[eta2] E[fb2] E[diag] fb2/diag E[2eta*fb] E[sumw] E[sumw2]")
    for k in range(len(rows)):
        data = np.vstack(rows[k])
        means = data.mean(axis=0)
        print(
            f"[{bins[k]:.0f},{bins[k+1]:.0f}) {len(data):6d} "
            f"{means[0]:.6g} {means[1]:.6g} {means[2]:.6g} {means[3]:.6g} "
            f"{means[2]/means[3]:.6g} {means[4]:+.6g} {means[5]:.6g} {means[6]:.6g}"
        )


if __name__ == "__main__":
    run(float(sys.argv[1]) if len(sys.argv) > 1 else 0.2,
        float(sys.argv[2]) if len(sys.argv) > 2 else 10.0,
        int(sys.argv[3]) if len(sys.argv) > 3 else 12,
        int(sys.argv[4]) if len(sys.argv) > 4 else 20261009)
