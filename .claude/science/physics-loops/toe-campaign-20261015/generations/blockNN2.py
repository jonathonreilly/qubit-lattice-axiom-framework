"""Nearest-site block walks, now requiring dispersion: tr W(k) or tr W(k)^2 must depend on k."""
import sys, itertools, numpy as np
from scipy.linalg import null_space
from scipy.optimize import least_squares
import coinfast as CF, coinrep as CR
rep = sys.argv[1]; ntrial = int(sys.argv[2]); delta = float(sys.argv[3]) if len(sys.argv) > 3 else 0.05
NN = (sys.argv[4] == 'nn') if len(sys.argv) > 4 else True
d, N, J, K, pairs, nz = CF.build(rep)
S = [tuple(v) for v in CR.stencil('cube')]; sidx = {n: i for i, n in enumerate(S)}
corners = [np.array(v) for v in itertools.product((0, 1), repeat=3)]
if NN:
    rows = [K[i, a, b, :] for i, n in enumerate(S) for a, vo in enumerate(corners) for b, vi in enumerate(corners)
            if np.abs(vo - vi - 2 * np.array(n)).max() > 1]
    Z = null_space(np.array(rows))
else:
    Z = np.eye(J)
K2 = np.einsum('nabj,jm->nabm', K, Z); J2 = Z.shape[1]
fun0, jac0, unpack = CF.make(d, N, J2, K2, pairs, nz, 0.0)
diffs2 = sorted({tuple(np.array(a) + np.array(b)) for a in S for b in S})
def disp(A):
    t1 = sum(abs(np.trace(A[i])) ** 2 for i in nz)
    t2 = 0.0
    for m in diffs2:
        if m == (0, 0, 0): continue
        acc = 0
        for i, n in enumerate(S):
            n2 = tuple(np.array(m) - np.array(n))
            if n2 in sidx: acc = acc + np.trace(A[i] @ A[sidx[n2]])
        t2 += abs(acc) ** 2
    return t1 + t2
def fun(x):
    A = unpack(x)
    return np.concatenate([fun0(x), [10 * max(0.0, delta - disp(A))]])
print(rep, 'nearest-site' if NN else 'cell', 'family dim', J2, flush=True)
rng = np.random.default_rng(1); hits = 0; best = 1e9
for t in range(ntrial):
    r = least_squares(fun, rng.normal(size=2 * J2) * rng.choice([0.3, 1.0]), xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
    res = np.linalg.norm(r.fun); best = min(best, res); A = unpack(r.x)
    print(f'trial {t}: residual {res:.2e} dispersion measure {disp(A):.3f}' + ('  HIT' if res < 1e-10 else ''), flush=True)
    if res < 1e-10: hits += 1; np.save(f'blockNN2_{rep}_{"nn" if NN else "cell"}_hit{t}.npy', A)
print(rep, 'dispersive unitary solutions', hits, '/', ntrial, 'best residual', best)
