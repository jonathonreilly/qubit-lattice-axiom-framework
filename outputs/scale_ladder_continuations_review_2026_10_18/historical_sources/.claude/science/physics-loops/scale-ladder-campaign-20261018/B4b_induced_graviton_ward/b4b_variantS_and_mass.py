"""B4b companion: (i) mass robustness of the 'D'-vertex symbol findings; (ii) the 'S' vertex
(mom = sin(Pbar/2), used by the isotropy and TT-stiffness-positive runners) on the runners' own grids.

Checks
  MR1-3  Ward violation, E/T2 split and [110] TT-pencil birefringence persist for m in {0.5, 1.0} (N=12)
  S1     'S' vertex kernel depends on the Brillouin-zone window (not a periodic lattice kernel)
  S2     'D' vertex control: window independent
  S3     'S' kernel lattice Ward residual on runner grids is O(1) relative to the TT stiffness signal
"""
import sys
import os
import itertools
import numpy as np
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stag_kernel import Pi_tensor, grid, symbol_from_T6, quad

results = []


def check(name, ok, detail=''):
    results.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name + ('  [' + detail + ']' if detail else ''), flush=True)


def _job(args):
    K, N, m, var, shift = args
    Pg = grid(N)
    if shift:
        Pg = Pg.copy()
        Pg[:, 2] = np.where(Pg[:, 2] < 0, Pg[:, 2] + 2 * np.pi, Pg[:, 2])   # window [0,2pi) in y
    return Pi_tensor(np.array(K, float), N, m, var, Pgrid=Pg).real


def eval_many(jobs):
    with Pool(4) as pool:
        return pool.map(_job, jobs)


dirs = [tuple(np.eye(4)[a]) for a in range(4)] + [tuple(np.eye(4)[a] + np.eye(4)[b]) for a, b in itertools.combinations(range(4), 2)]
eps = (0.05, 0.1)


def symbol_T6(N, m):
    Ks = [np.zeros(4)] + [e * np.array(u) for u in dirs for e in eps]
    vals = eval_many([(tuple(K), N, m, 'D', False) for K in Ks])
    P0 = vals[0]
    M2 = {}
    i = 1
    for u in dirs:
        M2[u] = (4 * (vals[i] - P0) / eps[0] ** 2 - (vals[i + 1] - P0) / eps[1] ** 2) / 3.0
        i += 2
    T6 = np.zeros((4,) * 6)
    E = np.eye(4)
    for a in range(4):
        T6[..., a, a] = M2[tuple(E[a])]
    for a, b in itertools.combinations(range(4), 2):
        off = 0.5 * (M2[tuple(E[a] + E[b])] - M2[tuple(E[a])] - M2[tuple(E[b])])
        T6[..., a, b] = off
        T6[..., b, a] = off
    return T6


def tt_pencil(T6, n):
    n = np.array(n, float)
    n /= np.linalg.norm(n)
    kt = np.array([1, 0, 0, 0.])
    ks = np.concatenate([[0], n])
    Pn = np.eye(3) - np.outer(n, n)
    pols = []
    for a in range(3):
        for b in range(a, 3):
            h = (np.outer(np.eye(3)[a], np.eye(3)[b]) + np.outer(np.eye(3)[b], np.eye(3)[a])) / 2
            x = Pn @ h @ Pn
            pols.append((x - np.trace(x) / 2 * Pn).ravel())
    U, _, _ = np.linalg.svd(np.array(pols).T)
    tt = []
    for i in range(2):
        h4 = np.zeros((4, 4))
        h4[1:, 1:] = U[:, i].reshape(3, 3)
        tt.append(h4)
    A = np.array([[quad(symbol_from_T6(T6, kt), x, y).real for y in tt] for x in tt])
    B = np.array([[quad(symbol_from_T6(T6, ks), x, y).real for y in tt] for x in tt])
    return np.sort(np.linalg.eigvals(np.linalg.solve(A, B)).real)


print('== MR: mass robustness of the D-vertex symbol (N=12)')
hT = np.zeros((4, 4)); hT[2, 3] = hT[3, 2] = 1 / np.sqrt(2)
hE = np.diag([0, 0, 1, -1.]) / np.sqrt(2)
rng = np.random.default_rng(11)
ks_rand = [v / np.linalg.norm(v) for v in rng.normal(size=(10, 4))]
for m in (0.5, 1.0):
    T6 = symbol_T6(12, m)
    wr = max(np.abs(np.einsum('m,mnrs->nrs', k, symbol_from_T6(T6, k))).max() / np.abs(symbol_from_T6(T6, k)).max()
             for k in ks_rand)
    Mx = symbol_from_T6(T6, np.array([0, 1, 0, 0.]))
    eot = quad(Mx, hE).real / quad(Mx, hT).real
    c110 = tt_pencil(T6, [1, 1, 0])
    c111 = tt_pencil(T6, [1, 1, 1])
    print('   m=%.1f: Ward ratio %.3f; E/T2 %.4f; TT c^2 [110] %s; [111] %s'
          % (m, wr, eot, ', '.join('%.5f' % c for c in c110), ', '.join('%.5f' % c for c in c111)))
    check('MR m=%.1f leading-symbol Ward violation O(1) (>1e-2)' % m, wr > 1e-2, '%.3f' % wr)
    check('MR m=%.1f E/T2 split nonzero (>1e-3)' % m, abs(eot - 1) > 1e-3, '%.4f' % eot)
    check('MR m=%.1f raw-kernel [110] TT-pencil split nonzero (>1e-5) and |c^2-1| nonzero' % m,
          abs(c110[1] - c110[0]) > 1e-5 and abs(c110 - 1).max() > 1e-4,
          'split %.2e' % (c110[1] - c110[0]))

print('== S: sin(Pbar/2) vertex on the runners\' grids (m=0.7)')
m = 0.7
for N in (6, 8):
    K = [0, 2 * np.pi / N, 0, 0]
    a0, aK, b0, bK, d0, dK, e0, eK = eval_many([((0, 0, 0, 0), N, m, 'S', False), (tuple(K), N, m, 'S', False),
                                                ((0, 0, 0, 0), N, m, 'S', True), (tuple(K), N, m, 'S', True),
                                                ((0, 0, 0, 0), N, m, 'D', False), (tuple(K), N, m, 'D', False),
                                                ((0, 0, 0, 0), N, m, 'D', True), (tuple(K), N, m, 'D', True)])
    winS = np.abs((aK - a0) - (bK - b0)).max() / np.abs(aK - a0).max()
    winD = np.abs((dK - d0) - (eK - e0)).max() / np.abs(dK - d0).max()
    k0 = 2 * np.pi / N
    ph = 2 * np.sin(k0 / 2)
    sigS = abs(quad(aK - a0, hT))
    LS = np.abs(ph * (aK - a0)[1]).max()
    sigD = abs(quad(dK - d0, hT))
    LD = np.abs(ph * (dK - d0)[1]).max()
    print('   N=%d: window dependence S %.2e, D %.2e;  Ward residual/TT signal: S %.3f, D %.3f' % (N, winS, winD, LS / sigS, LD / sigD))
    check('S1 N=%d sin(Pbar/2)-vertex kernel changes with BZ window choice (>1e-3 relative)' % N, winS > 1e-3, '%.2e' % winS)
    check('S2 N=%d sin(Pbar)-vertex control is window independent (<1e-10)' % N, winD < 1e-10, '%.1e' % winD)
    check('S3 N=%d sin(Pbar/2)-vertex lattice Ward residual is O(1) of the TT signal (>0.05)' % N, LS / sigS > 0.05,
          '%.3f' % (LS / sigS))

n_pass = sum(ok for _, ok in results)
print('TOTAL: PASS=%d FAIL=%d' % (n_pass, len(results) - n_pass))
