#!/usr/bin/env python3
"""Aggregate sim.c CSV rows: mean, block-based SE, jackknife Q. Author: Claude Sonnet 5.5."""
import sys, csv, math, collections, json
import numpy as np

COLS = ['sum_a1', 'sum_aopp', 'sum_aorth', 'sum_adiag', 'sum_s', 'sum_m2', 'sum_m4']


def load(files):
    G = collections.defaultdict(list)
    for fn in files:
        for row in csv.reader(open(fn)):
            if not row:
                continue
            key = (row[0], float(row[1]), float(row[2]), float(row[3]), int(row[4]))
            n = int(row[6])
            vals = [float(x) for x in row[7:14]]
            G[key].append((n, vals))
    return G


def summarize(G):
    out = {}
    for key, blocks in G.items():
        n = np.array([b[0] for b in blocks], float)
        V = np.array([b[1] for b in blocks], float)  # nblk x 7
        B = len(blocks)
        means_blk = V / n[:, None]
        tot = V.sum(0) / n.sum()
        se = means_blk.std(0, ddof=1) / math.sqrt(B)
        # Q = <m4>/<m2>^2 with jackknife
        def Qof(idx):
            m2 = V[idx, 5].sum() / n[idx].sum()
            m4 = V[idx, 6].sum() / n[idx].sum()
            return m4 / (m2 * m2) if m2 > 0 else float('nan')
        allidx = np.arange(B)
        Q = Qof(allidx)
        jk = np.array([Qof(np.delete(allidx, i)) for i in range(B)])
        Qse = math.sqrt((B - 1) / B * ((jk - jk.mean()) ** 2).sum())
        out[key] = dict(n=int(n.sum()), a1=tot[0], a1_se=se[0], aopp=tot[1], aopp_se=se[1], aorth=tot[2],
                        adiag=tot[3], adiag_se=se[3], s=tot[4], s_se=se[4], m2=tot[5], m2_se=se[5], Q=Q, Q_se=Qse)
    return out


if __name__ == '__main__':
    S = summarize(load(sys.argv[1:]))
    for key in sorted(S):
        d = S[key]
        print(key, ' '.join(f'{k}={v:.6g}' if isinstance(v, float) else f'{k}={v}' for k, v in d.items()))
