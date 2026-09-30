"""Independent re-implementation (does not import the attacker's code).
Question: how many records does a scorer need to separate formation-order odds from static odds?
Attack claim: ~1.3e4 coding-set records ('chi2 excess 16') and 'cheaper question ... at about 10^4 records'.
Checks: (1) is 'chi2 excess 16' a 4-sigma separation for the chi2/df~90 calibration statistic? (2) paired log-score N for 4 sigma
with the true formation order known; (3) what an order-blind scorer (final snapshot only) can do."""
import numpy as np
rng = np.random.default_rng(31337)
L = 4; N = L**3; M = 20000
P_, Q_, R_ = 3.0, 1.0, 2.0
PHI = np.array([[P_ if s == t else (Q_ if s//2 == t//2 else R_) for t in range(6)] for s in range(6)])
coords = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
idx = {c: i for i, c in enumerate(coords)}
nbrs = [[idx[(x+dx, y+dy, z+dz)] for dx, dy, dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
         if 0 <= x+dx < L and 0 <= y+dy < L and 0 <= z+dz < L] for (x, y, z) in coords]
par = np.array([(x+y+z) % 2 for (x, y, z) in coords])

def rule(vals_nb):  # vals_nb: (M, k) recorded neighbour values, -1 = unrecorded -> (M,6)
    w = np.ones((vals_nb.shape[0], 6))
    for k in range(vals_nb.shape[1]):
        v = vals_nb[:, k]
        f = np.where((v >= 0)[:, None], PHI[:, np.maximum(v, 0)].T, 1.0)
        w = w * f
    return w / w.sum(1, keepdims=True)

vals = -np.ones((M, N), dtype=int)
ppred = np.zeros((M, N, 6))              # predictive odds at the site, by SITE
order = rng.permuted(np.tile(np.arange(N), (M, 1)), axis=1)
m = np.arange(M)
for t in range(N):
    x = order[:, t]
    # gather neighbours: pad to 6 with -1
    nbv = -np.ones((M, 6), dtype=int)
    for xi in range(N):
        sel = np.where(x == xi)[0]
        if len(sel):
            for k, y in enumerate(nbrs[xi]):
                nbv[sel, k] = vals[sel, y]
    p = rule(nbv)
    u = rng.random(M)[:, None]
    s = (u > np.cumsum(p, 1)).sum(1).clip(0, 5)
    vals[m, x] = s
    ppred[m, x, :] = p
# static conditional on all final neighbour values, at even sites
ev = np.where(par == 0)[0]
qstat = np.zeros((M, N, 6))
for xi in ev:
    nbv = -np.ones((M, 6), dtype=int)
    for k, y in enumerate(nbrs[xi]):
        nbv[:, k] = vals[:, y]
    qstat[:, xi, :] = rule(nbv)
# per-record log score difference d = log ppred(x) - log qstat(x)  (formation-with-order minus static)
d = np.log(ppred[m[:, None], ev[None, :], vals[:, ev]]) - np.log(qstat[m[:, None], ev[None, :], vals[:, ev]])
d = d.reshape(-1)
mu, sd = d.mean(), d.std()
print(f"records (even sites) = {d.size}; mean log-score gain of formation-with-order over static = {mu:.3e} nats/record, sd = {sd:.3f}")
print(f"paired-score N for 4 sigma (order KNOWN): {16*sd**2/mu**2:.0f} records")
# KL estimate & chi2-excess relation
print(f"  (2*mean gain = {2*mu:.3e} ~ chi2 excess per record; attack measured 1.186e-3)")
# (1) sd of chi2 with df=90: 4-sigma needs lambda solving lambda = 4*sqrt(2*(df+2*lambda))
df = 90
lam = 0.0
for _ in range(100): lam = 4*np.sqrt(2*(df+2*lam))
print(f"non-central chi2 (df={df}) 4-sigma needs excess ~{lam:.0f}, not 16 => N ~ {lam/1.186e-3:.0f} records for the omnibus calibration statistic")
# (3) order-blind: an observer with only the final snapshot cannot form ppred at all.  Compare with a random imposed order.
rank = np.argsort(rng.random((M, N)), axis=1).argsort(axis=1)
imp = np.zeros((M, N, 6))
for xi in ev:
    nbv = -np.ones((M, 6), dtype=int)
    for k, y in enumerate(nbrs[xi]):
        nbv[:, k] = np.where(rank[:, y] < rank[:, xi], vals[:, y], -1)
    imp[:, xi, :] = rule(nbv)
d2 = np.log(imp[m[:, None], ev[None, :], vals[:, ev]]) - np.log(qstat[m[:, None], ev[None, :], vals[:, ev]])
d2 = d2.reshape(-1)
print(f"IMPOSED random order (order unknown, guessed) vs static: mean gain {d2.mean():.3e}, sd {d2.std():.3f} nats/record")
d3 = np.log(ppred[m[:, None], ev[None, :], vals[:, ev]]) - np.log(imp[m[:, None], ev[None, :], vals[:, ev]])
print(f"true order vs guessed random order: mean gain {d3.mean():.3e}, sd {d3.std():.3f} => N(4 sigma) = {16*d3.var()/d3.mean()**2:.0f}")
print("Note: guessed order = right law family, wrong order; population of orders is exactly what T01 leaves open.")
