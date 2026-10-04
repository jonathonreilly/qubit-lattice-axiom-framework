"""A50 t2_search: continuous (non-Clifford) covariant product dressings, searched by least squares.
argv: group (O, T, D2, C2z), window (axis = v + 6 links + 6 far corners; full = 27 places + far
corners), target (none | T | all), number of starts.
Residual vector: non-scalar parts of every per-site word for the T-junctions (and corners when
target = all), plus, for a target, theta~ + 1 for those junctions (theta~ = link phase * prod tr(W)/2).
Falsification test of lemma F'': under O no start may reach zero residual with target T.
Control: under {1, C2z} the same search must reach zero with theta = -1.
"""
import signal, sys, time
import numpy as np
from collections import Counter
from scipy.optimize import least_squares
from a50lib import *
signal.alarm(285)
gname, wname, target = sys.argv[1], sys.argv[2], sys.argv[3]
NST = int(sys.argv[4]) if len(sys.argv) > 4 else 20
G = GRP[gname]
WIN = AXSITES if wname == 'axis' else WFAR
NONLEG = [x for x in WIN if x not in LEGLINK]
import zlib; rng = np.random.default_rng(zlib.crc32((gname + wname + target).encode()))

# fast transport map; seeding structure in build_hops order
FH = FastHops(G, WIN)
struct = [(o, S, stab_type(S) if kind(o) != 1 else ('link', None)) for (o, S) in FH.struct]
npar = sum(1 if kind(o) == 1 or st[0] != 'triv' else 3 for (o, S, st) in struct)

def seeds_of(p, branches):
    out = []; q = 0
    for (o, S, st), br in zip(struct, branches):
        if kind(o) == 1:
            e = np.zeros(3); e[link_axis(o)] = p[q]; out.append(su2_exp(e)); q += 1
        elif st[0] == 'triv':
            out.append(su2_exp(p[q:q + 3])); q += 3
        else:
            n = st[1]
            if st[0] == 'so2' or br == 0:
                out.append(su2_exp(p[q] * n))
            else:
                b1 = np.cross(n, [1, 0, 0] if abs(n[0]) < 0.9 else [0, 1, 0]); b1 /= np.linalg.norm(b1)
                b2 = np.cross(n, b1)
                out.append(nsig(np.cos(p[q]) * b1 + np.sin(p[q]) * b2))
            q += 1
    return np.array(out)

TRI_USE = T_TRI if target != 'all' else TRIPLES
def dag(A):
    return np.conj(np.swapaxes(A, -1, -2))
def evaluate(seeds):
    A, L = FH.arrays(seeds)
    K = [kron6(L[h]) for h in range(6)]
    res = []; th = {}
    for tri in TRI_USE:
        i, j, k = tri
        W = dag(A[i]) @ A[j] @ dag(A[k]) @ A[i] @ dag(A[j]) @ A[k]
        lam = (W[:, 0, 0] + W[:, 1, 1]) / 2
        D = (W - lam[:, None, None] * I2).reshape(-1)
        T1 = K[i] @ K[j].conj().T @ K[k]; T2 = K[k] @ K[j].conj().T @ K[i]
        c, rL = phase_fit(T1, T2)
        res.append(np.concatenate([D.real, D.imag, [rL]]))
        th[tri] = c * np.prod(lam)
    return np.concatenate(res), th

# consistency of the fast map with build_hops (random seeds)
_br = [0] * len(struct); _p = rng.uniform(-3, 3, size=npar); _sd = seeds_of(_p, _br)
_it = iter(list(_sd)); _h = build_hops(G, WIN, lambda o, S: next(_it))
_A, _L = FH.arrays(_sd)
_d = max(np.abs(_A[i, n] - _h[i].get(x, I2)).max() for i in range(6) for n, x in enumerate(FH.nonleg))
_d = max(_d, max(np.abs(_L[i][m] - _h[i].get(LEGLINK[m], I2)).max() for i in range(6) for m in range(6)))
print("fast map vs build_hops: max diff %.1e" % _d)

def fun(p, branches):
    r, th = evaluate(seeds_of(p, branches))
    if target in ('T', 'all'):
        t = np.array([th[tri] + 1 for tri in TRI_USE])
        r = np.concatenate([r, t.real, t.imag])
    return r

print("group %s, window %s (%d places), target %s, %d params, %d starts"
      % (gname, wname, len(WIN), target, npar, NST))
t0 = time.time(); summary = Counter(); best = np.inf; zero_thetas = Counter(); ex = None
for s in range(NST):
    if time.time() - t0 > 240:
        print("   time cap reached after %d starts" % s); break
    branches = [rng.integers(2) for _ in struct]
    p0 = rng.uniform(-np.pi, np.pi, size=npar)
    sol = least_squares(fun, p0, args=(branches,), method='lm', xtol=1e-15, ftol=1e-15, max_nfev=40 * npar)
    r, th = evaluate(seeds_of(sol.x, branches))
    if s < 2: print('   start %d: nfev %d, status %d, cost %.2e, %.1f s' % (s, sol.nfev, sol.status, sol.cost, time.time() - t0))
    rmax = np.abs(r).max()
    best = min(best, np.linalg.norm(fun(sol.x, branches)))
    if rmax < 1e-8:
        pat = tuple(sorted(Counter(complex(np.round(th[t].real, 5), np.round(th[t].imag, 5)) for t in TRI_USE).items(),
                           key=lambda z: z[0].real))
        zero_thetas[pat] += 1
        if ex is None and any(np.round(th[t].real, 5) == -1 for t in T_TRI if t in th):
            ex = (s, {NAMES[t[0]] + NAMES[t[1]] + NAMES[t[2]]: np.round(th[t], 4) for t in TRI_USE})
        summary['scalar at optimum'] += 1
    else:
        summary['not scalar'] += 1
print("   outcomes: %s" % dict(summary))
print("   smallest final residual norm (incl. target terms): %.3e" % best)
print("   theta patterns at scalar optima (over %s): %s" % ('T-junctions' if target != 'all' else 'all 20', dict(zero_thetas)))
if ex is not None:
    print("   example with a -1 T-junction (start %d): %s" % ex)
print("   wall %.1f s" % (time.time() - t0))
print("done")
