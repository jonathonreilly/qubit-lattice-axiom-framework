"""E9: frequency and size of FORCED signalling (no rule at all keeps A's 3-tick history law
independent of B's tick choices).  Plaquette toy, A's three ticks fixed, B chooses its
tick-0 and tick-1 gates (2 x 2 = 4 setting pairs), tick 2 fixed.

Measure: minimal total L1 violation of the NS-A rows (= sum over the 3 non-reference
setting pairs and all A-histories of |law difference|), minimised over all rules with
C (Born odds every tick) and one-site moves.

Usage: python3 e9_forced_scan.py <ntrials> <seed> <moves: tick|lattice> [real]
"""
import sys
import time
import numpy as np
import os
METHOD = os.environ.get('LPMETHOD', 'highs-ipm')
from mtlp import (Model, history_lp, haar_unitary, rand_state, block_unitary,
                  ring_adj, tick_support_adj)

ntr = int(sys.argv[1]); seed = int(sys.argv[2]); moves = sys.argv[3]
real = len(sys.argv) > 4 and sys.argv[4] == 'real'
rng = np.random.default_rng(seed)
T = 3
EVEN = [[0, 1], [2, 3]]
ODD = [[1, 2], [3, 0]]


def gate():
    if real:
        th = rng.uniform(0, 2 * np.pi)
        return np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]], complex)
    return haar_unitary(2, rng)


def tick(k):
    blocks = EVEN if k % 2 == 0 else ODD
    return block_unitary(4, blocks, [gate(), gate()])


t0 = time.time()
vals = []
bslack = [0.0]
for tr in range(ntr):
    if real:
        psi0 = rng.normal(size=16).astype(complex); psi0 /= np.linalg.norm(psi0)
    else:
        psi0 = rand_state(16, rng)
    UA = [[tick(k)] for k in range(T)]
    UB = [[tick(0), tick(0)], [tick(1), tick(1)], [tick(2)]]
    if moves == 'lattice':
        movA = [ring_adj(4)] * T; movB = [ring_adj(4)] * T
    else:
        movA = [tick_support_adj(UA[k][0]) for k in range(T)]
        movB = [tick_support_adj(UB[k][0]) for k in range(T)]
    m = Model(psi0, UA, UB, movA, movB)
    lp, idx = history_lp(m, ns=True, caus=True)
    r = lp.solve(soft={'NSA': 1.0, 'BORN': 1e4}, method=METHOD)
    if r.status == 0:
        vals.append(r.slack_by_tag['NSA'])
        bslack.append(r.slack_by_tag['BORN'])
    else:
        vals.append(np.nan)
vals = np.array(vals)
pos = vals[vals > 1e-4]
print('   sorted NS-A min violations (top 12):', np.round(np.sort(vals[~np.isnan(vals)])[::-1][:12], 5).tolist(), '; count in (1e-7,1e-4]:', int(((vals > 1e-7) & (vals <= 1e-4)).sum()))
print(f"[{METHOD}] moves={moves} real={real} seed={seed}: forced signalling in {len(pos)}/{ntr} instances; "
      f"max min-violation {np.nanmax(vals):.4e}; median of positives {np.median(pos) if len(pos) else 0:.3e}; "
      f"solver failures {np.isnan(vals).sum()}; max Born slack {max(bslack):.1e}  ({time.time()-t0:.1f}s)")
