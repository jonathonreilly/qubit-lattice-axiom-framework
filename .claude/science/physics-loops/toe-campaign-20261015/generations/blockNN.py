"""Block-coin walks restricted to nearest-site hops: |v_out - v_in - 2n|_inf <= 1."""
import sys, itertools, numpy as np
from scipy.linalg import null_space
from scipy.optimize import least_squares
import coinfast as CF
rep = sys.argv[1]; ntrial = int(sys.argv[2]); delta = float(sys.argv[3]) if len(sys.argv) > 3 else 0.05
d, N, J, K, pairs, nz = CF.build(rep)
import coinrep as CR
S = [tuple(v) for v in CR.stencil('cube')]
corners = [np.array(v) for v in itertools.product((0, 1), repeat=3)]
rows = []
for i, n in enumerate(S):
    for a, vo in enumerate(corners):
        for b, vi in enumerate(corners):
            if np.abs(vo - vi - 2 * np.array(n)).max() > 1:
                rows.append(K[i, a, b, :])
M = np.array(rows)
Z = null_space(M) if len(rows) else np.eye(J)
print(rep, 'family dim', J, '-> nearest-site family dim', Z.shape[1], flush=True)
K2 = np.einsum('nabj,jm->nabm', K, Z); J2 = Z.shape[1]
fun, jac, unpack = CF.make(d, N, J2, K2, pairs, nz, delta)
rng = np.random.default_rng(0); best = 1e9; hits = 0
for t in range(ntrial):
    r = least_squares(fun, rng.normal(size=2 * J2) * rng.choice([0.3, 1.0]), jac=jac, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=5000)
    res = np.linalg.norm(r.fun); best = min(best, res)
    A = unpack(r.x); mov = sum(np.sum(np.abs(A[i]) ** 2) for i in nz)
    print(f'trial {t}: residual {res:.2e} moving weight {mov:.3f}' + ('  HIT' if res < 1e-10 else ''), flush=True)
    if res < 1e-10: hits += 1; np.save(f'blockNN_{rep}_hit{t}.npy', A)
print(rep, 'nearest-site moving unitary solutions', hits, '/', ntrial, 'best residual', best)
