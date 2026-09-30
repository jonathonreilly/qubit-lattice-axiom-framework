"""T09 Test 1: census of nontrivial exactly-covariant radius-1 unitary ticks on Z^3, C^s per site.
For each representation (multiset of irreps of 2O / O) find whether a unitary tick with pinned
nonzero neighbour norm exists (random-start Levenberg-Marquardt)."""
import sys, itertools, json, time
import numpy as np
from scipy.optimize import least_squares
from common import *

rng = np.random.default_rng(20260929)
KS = rng.uniform(-np.pi, np.pi, size=(24, 3))

def setup(names):
    s, b0, bN = covariant_basis(names)
    n0, nN = len(b0), len(bN)
    K = len(KS)
    B = np.zeros((n0 + nN, K, s, s), complex)
    for j, b in enumerate(b0):
        B[j] = b[None]
    for j, d in enumerate(bN):
        for di, v in enumerate(DIRS):
            ph = np.exp(1j * (KS @ v))
            B[n0 + j] += ph[:, None, None] * d[di][None]
    G = np.zeros((nN, nN), complex)
    for a, da in enumerate(bN):
        for b, db in enumerate(bN):
            G[a, b] = sum(np.trace(da[di].conj().T @ db[di]) for di in range(6))
    return s, n0, nN, B, G

def solve(names, tau, n_starts, seed=0):
    s, n0, nN, B, G = setup(names)
    if nN == 0:
        return s, n0, nN, None, None, None
    nb = n0 + nN
    r = np.random.default_rng(seed)
    I = np.eye(s)
    def res(x):
        c = x[:nb] + 1j * x[nb:]
        U = np.einsum('j,jkab->kab', c, B)
        R = np.einsum('kba,kbc->kac', U.conj(), U) - I[None]
        cn = c[n0:]
        nrm = np.real(cn.conj() @ G @ cn) - tau
        return np.concatenate([R.real.ravel(), R.imag.ravel(), [nrm]])
    best = (1e9, None)
    nsol = 0
    for t in range(n_starts):
        x0 = r.normal(size=2 * nb) * 0.7
        sol = least_squares(res, x0, method='lm', xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=1500)
        cost = np.linalg.norm(sol.fun)
        if cost < best[0]:
            best = (cost, sol.x)
        if cost < 1e-9:
            nsol += 1
    return s, n0, nN, best[0], best[1], nsol

def reps_up_to(pool, maxdim):
    out = []
    def rec(start, cur, dim):
        if cur:
            out.append(list(cur))
        for i in range(start, len(pool)):
            d = IRREP_DIM[pool[i]]
            if dim + d <= maxdim:
                cur.append(pool[i]); rec(i, cur, dim + d); cur.pop()
    rec(0, [], 0)
    return out

if __name__ == '__main__':
    n_starts = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    results = []
    maxint = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    maxspin = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    reps = [('int', r) for r in reps_up_to(INT_IRREPS, maxint)] + [('spin', r) for r in reps_up_to(SPIN_IRREPS, maxspin)]
    # prune: reps made only of 1-dim irreps are covered by the exact cross-term lemma (U = a + 2pC(k), p=0);
    # skip irreps repeated more than twice
    def keep(t):
        names = t[1]
        if all(IRREP_DIM[n] == 1 for n in names):
            return False
        return max(names.count(n) for n in set(names)) <= 2
    reps = [t for t in reps if keep(t)]
    reps.sort(key=lambda t: sum(IRREP_DIM[n] for n in t[1]))
    if len(sys.argv) > 4:
        only = sys.argv[4].split(',')
        reps = [t for t in reps if '+'.join(t[1]) in only]
    print(len(reps), 'representations')
    t0 = time.time()
    for kind, names in reps:
        s = sum(IRREP_DIM[n] for n in names)
        row = {'kind': kind, 'rep': names, 's': s}
        found = False
        for tau in (0.3, 1.0, max(0.5, s - 0.3)):
            out = solve(names, tau, n_starts, seed=hash(tuple(names)) % 1000)
            s_, n0, nN, cost, x, nsol = out
            row['n0'] = n0; row['nN'] = nN
            if cost is None:
                row.setdefault('tau', {})[str(tau)] = None
                continue
            row.setdefault('tau', {})[str(tau)] = {'best_cost': float(cost), 'n_solutions': int(nsol)}
            if cost < 1e-9:
                found = True
        row['nontrivial_found'] = found
        results.append(row)
        print(f"{kind:4s} s={s} {'+'.join(names):18s} dimA0={row.get('n0')} dimAz={row.get('nN')} nontrivial={found}  "
              + ' '.join(f"tau{t}:{(v or {}).get('best_cost', float('nan')):.1e}/{(v or {}).get('n_solutions', 0)}" for t, v in row['tau'].items()), flush=True)
    json.dump(results, open(f'census_results_{maxint}_{maxspin}.json', 'w'), indent=1)
    print('elapsed', time.time() - t0)
