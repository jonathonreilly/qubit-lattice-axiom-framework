"""TOR-1 RP kernel entries on the Lx = 4 torus (PREREG section 4 + F2): W-matched point-orbit witnesses (K2c V2), hard crossing
weight delta = 0.6, beta_g = 0, link reflection.  Crossing integration: plane A by lat2d Duffy cells (phi_0 = 0), plane B by the
same cells, the Polyakov variable chi_0 by the trapezoid rule.
usage: python3 tor1_kernel.py pool.npz Lt n nw ops [pairs=upper|sub:SEED:NSUB]   (ops comma list: chi,mod,O,vec0,W,PG)
writes pool_..._L{n}_{nw}_{ops}.npz with log-entries per op."""
import sys, time
import numpy as np
from tor1_geom import *
fn, Lt, n, nw, ops = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5].split(',')
pairs_mode = sys.argv[6] if len(sys.argv) > 6 else 'upper'
S = Torus(4, Lt); T = Lt // 2; t00 = time.time()
z = np.load(fn); U = [{'x': z['ux'][i], 't': z['ut'][i]} for i in range(len(z['ux']))]; k = len(U)
if 'chi' in ops:
    M = TorusMeasure(S, '11112', Ns=4, sk=-1, ntor=96, nloop=1024); M.ntor1 = 24; M.use_spline()


def logs(op, A):
    if op == 'chi': return M.logrho(A)
    if op == 'mod':
        l1, g1 = vec_logdet(S, A, 0.0, 1); l2, g2 = vec_logdet(S, A, 0.0, 2); return 2 * l1.real + 0.5 * l2.real + 0j
    if op == 'O': return vec_logdet(S, A, 0.05, 1)[0]
    if op == 'vec0': return vec_logdet(S, A, 0.0, 1)[0]
    if op == 'W': return wilson_logdet(S, A, 0.05)
    if op == 'PG': return np.zeros(len(A), complex)


if pairs_mode == 'upper':
    pairs = [(a, b) for a in range(k) for b in range(a, k)]
else:
    md, sd, ns = pairs_mode.split(':'); rs = np.random.default_rng(int(sd)); sub = set()
    while len(sub) < int(ns):
        a_, b_ = sorted(int(v) for v in rs.choice(k, 2, replace=False)); sub.add((a_, b_))
    pairs = sorted(sub) + [(i, i) for i in range(k)]
    if md == 'rev': pairs = [(b_, a_) for (a_, b_) in sorted(sub)]
    if md == 'fix': pairs = [(0, 5), (0, 0), (5, 5)]          # F7 reduced plane-refinement subset (fixed before running)
CH = {'chi': 64, 'mod': 128, 'O': 128, 'vec0': 128, 'W': 256, 'PG': 4096}
L = {op: np.full((k, k), np.nan + 0j) for op in ops}; Q = {'gmin': np.inf, 'Qmax': 0, 'maxF': 0.0}
print(f"# TOR-1 kernel pool={fn} Lx=4 Lt={Lt} k={k} level (n={n}, nw={nw}) ops={ops} pairs={pairs_mode} ({len(pairs)} entries)", flush=True)
for i, (a, b) in enumerate(pairs):
    A, w = entry_fields(S, U[a], U[b], n, nw)
    F = (A @ S.Pm.T + np.pi) % (2 * np.pi) - np.pi; Q['maxF'] = max(Q['maxF'], np.abs(F).max())
    Q['Qmax'] = max(Q['Qmax'], int(np.abs(np.round(F.sum(1) / (2 * np.pi))).max()))
    for op in ops:
        ls = [logs(op, A[c:c + CH[op]]) for c in range(0, len(A), CH[op])]; l = np.concatenate(ls)
        lm = l.real.max(); L[op][a, b] = lm + np.log(np.sum(w * np.exp(l - lm)) + 0j)
    if i % 5 == 0 or i == len(pairs) - 1:
        print(f"  entry {i+1}/{len(pairs)} ({a},{b}) nodes {len(w)} [{time.time()-t00:.0f}s]", flush=True)
print(f"node checks: max|F| over all nodes {Q['maxF']:.4f} (hard support 0.6, bulk margin 0.55); max |Q| {Q['Qmax']}")
out = fn.replace('.npz', f'_L{n}_{nw}_{"-".join(ops)}_{pairs_mode.replace(":", "")}.npz')
np.savez(out, pairs=np.array(pairs), **{op: L[op] for op in ops})
print(f"saved {out} done [{time.time()-t00:.0f}s]")
