"""Fast covariant-walk search with analytic Jacobian (any coin rep from coinrep.py).

Unknowns p in C^J parametrise A_n = sum_j K[n,:,:,j] p_j (covariant subspace).
Residuals: Re/Im of P_d = sum_{i - j = d} A_i A_j^dagger - delta_{d0} I, and a
lower-bound penalty w * max(0, delta - sum_{n != 0} ||A_n||^2).
"""
import sys, numpy as np
from scipy.optimize import least_squares
import coinrep as CR

def build(repname, kind='cube'):
    import os; kind = os.environ.get('STENCIL', kind)
    gens = CR.menu_rep(repname) if repname.startswith('menu-') else CR.rep(repname)
    d = gens[0][1].shape[0]
    S = CR.stencil(kind); idx = {tuple(v): i for i, v in enumerate(S)}; N = len(S)
    _, _, _, Kflat, diffs = CR.setup(repname, kind)
    J = Kflat.shape[1]
    K = Kflat.reshape(N, d * d, J).reshape(N, d, d, J, order='C')
    # Kflat was built with column-major vec of each block: undo that
    K = np.stack([Kflat[i * d * d:(i + 1) * d * d].reshape(d, d, J, order='F') for i in range(N)])
    pairs = []
    for dd in diffs:
        ii, jj = [], []
        for i, n in enumerate(S):
            m = tuple(np.array(n) - np.array(dd))
            if m in idx: ii.append(i); jj.append(idx[m])
        pairs.append((np.array(ii), np.array(jj), dd == (0, 0, 0)))
    zero = idx[(0, 0, 0)]; nz = np.array([i for i in range(N) if i != zero])
    return d, N, J, K, pairs, nz

def make(d, N, J, K, pairs, nz, delta=0.05, w=10.0):
    I = np.eye(d)
    def unpack(x):
        p = x[:J] + 1j * x[J:]
        return np.einsum('nabj,j->nab', K, p)
    def fun(x):
        A = unpack(x); out = []
        for ii, jj, isz in pairs:
            P = np.einsum('nab,ncb->ac', A[ii], A[jj].conj())
            if isz: P = P - I
            out += [P.real.ravel(), P.imag.ravel()]
        mov = np.sum(np.abs(A[nz]) ** 2)
        out.append(np.array([w * max(0.0, delta - mov)]))
        return np.concatenate(out)
    def jac(x):
        A = unpack(x); rows = []
        for ii, jj, isz in pairs:
            # dP/dp_m = sum K[i,:,:,m] A_j^dag ; dP/dconj(p_m) = sum A_i K[j,:,:,m]^dag
            T1 = np.einsum('nabm,ncb->acm', K[ii], A[jj].conj())
            T2 = np.einsum('nab,ncbm->acm', A[ii], K[jj].conj())
            dX = T1 + T2; dY = 1j * T1 - 1j * T2
            Dx = dX.reshape(d * d, J); Dy = dY.reshape(d * d, J)
            rows.append(np.hstack([Dx.real, Dy.real])); rows.append(np.hstack([Dx.imag, Dy.imag]))
        mov = np.sum(np.abs(A[nz]) ** 2)
        pen = np.zeros(2 * J)
        if mov < delta:
            # d mov / dx_m = 2 Re sum conj(A) K_m ; d/dy_m = 2 Re sum conj(A) i K_m
            g = np.einsum('nab,nabm->m', A[nz].conj(), K[nz])
            pen = -w * np.concatenate([2 * g.real, 2 * (1j * g).real])
        rows.append(pen[None, :])
        return np.vstack(rows)
    return fun, jac, unpack

if __name__ == '__main__':
    repname, ntrial = sys.argv[1], int(sys.argv[2]); delta = float(sys.argv[3]) if len(sys.argv) > 3 else 0.05
    d, N, J, K, pairs, nz = build(repname)
    fun, jac, unpack = make(d, N, J, K, pairs, nz, delta)
    # gradient check
    x = np.random.default_rng(9).normal(size=2 * J); e = 1e-6; Jn = np.zeros((fun(x).size, 2 * J))
    for m in range(2 * J):
        dx = np.zeros(2 * J); dx[m] = e; Jn[:, m] = (fun(x + dx) - fun(x - dx)) / (2 * e)
    print(repname, 'coin dim', d, 'family dim', J, ' jacobian check max err', np.abs(Jn - jac(x)).max(), flush=True)
    rng = np.random.default_rng(0); best = 1e9; hits = []
    for t in range(ntrial):
        r = least_squares(fun, rng.normal(size=2 * J) * rng.choice([0.3, 1.0]), jac=jac, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=5000)
        res = np.linalg.norm(r.fun); best = min(best, res)
        mov = np.sum(np.abs(unpack(r.x)[nz]) ** 2)
        if res < 1e-10: hits.append(r.x); print(f'  HIT trial {t}: residual {res:.2e} moving norm {mov:.4f}', flush=True)
    print(f'{repname}: moving unitary solutions {len(hits)}/{ntrial}, best residual {best:.3e}', flush=True)
    np.save(f'fast_hits_{repname.replace("/", "_")}.npy', np.array(hits))
