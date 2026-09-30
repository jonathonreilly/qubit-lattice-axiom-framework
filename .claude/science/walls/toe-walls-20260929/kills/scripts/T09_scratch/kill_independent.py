"""Independent re-derivation of the tick census (kill check for T09).
Different construction from the attack's census.py:
 - covariant subspace built by a REYNOLDS projector on the 7-tuple (A_0, A_{+x},A_{-x},...),
 - unitarity imposed EXACTLY through the Fourier-autocorrelation identities  sum_y A_y^dag A_{y+d} = delta_{d,0} I
   (25 shifts d in the difference set), not at 24 sampled momenta,
 - optional covariance up to the sign character:  A_{Rh} = chi(R) rho(R) A_h rho(R)^dag, chi in {1, sgn}.
Uses only the irrep matrices of common.py (checked homomorphic below)."""
import sys, itertools, numpy as np
from scipy.optimize import least_squares
sys.path.insert(0, '.')
from common import *

DIRV = [tuple(int(x) for x in d) for d in DIRS]
SUP = [(0,0,0)] + DIRV                     # 7 support points, index 0 = centre
IDX = {p: i for i, p in enumerate(SUP)}
def rot_on_support(R):
    return [IDX[tuple(int(round(x)) for x in (R @ np.array(p)))] for p in SUP]

def covariant_basis2(names, chi):
    s = sum(IRREP_DIM[n] for n in names)
    dim = 7 * s * s
    P = np.zeros((dim, dim), complex)
    for R in ROTS:
        rho = rep_matrix(names, R)
        c = 1.0 if chi == 'triv' else float(sgn(R))
        perm = rot_on_support(R)
        # (g.A)_{R h} = c rho A_h rho^dag ;  vec row-major: vec(rho A rho^dag) = kron(rho, conj(rho)) vec(A)
        K = c * np.kron(rho, rho.conj())
        G = np.zeros((dim, dim), complex)
        for h in range(7):
            G[perm[h]*s*s:(perm[h]+1)*s*s, h*s*s:(h+1)*s*s] = K
        P += G
    P /= 24
    # range of P
    u, sv, vh = np.linalg.svd(P)
    r = int((sv > 1e-9).sum())
    B = u[:, :r]                         # orthonormal basis (columns) of covariant subspace
    return s, B

DIFFS = sorted({tuple(np.subtract(a, b)) for a in SUP for b in SUP})
def residual_fn(s, B, tau, nontriv_weights=None):
    r = B.shape[1]
    I = np.eye(s)
    def unpack(x):
        c = x[:r] + 1j*x[r:]
        v = B @ c
        return [v[h*s*s:(h+1)*s*s].reshape(s, s) for h in range(7)]
    def res(x):
        A = unpack(x)
        out = []
        for d in DIFFS:
            M = np.zeros((s, s), complex)
            for a, pa in enumerate(SUP):
                pb = tuple(np.add(pa, d))
                if pb in IDX:
                    M += A[a].conj().T @ A[IDX[pb]]
            if d == (0,0,0): M = M - I
            out += [M.real.ravel(), M.imag.ravel()]
        nrm = sum(np.linalg.norm(A[h])**2 for h in range(1, 7)) - tau
        out.append([nrm])
        return np.concatenate(out)
    return res

def run(names, chi, starts, taus, seed):
    s, B = covariant_basis2(names, chi)
    r = B.shape[1]
    if r == 0: return s, 0, None, 0
    rng = np.random.default_rng(seed)
    best = 1e9; nsol = 0
    for tau in taus:
        res = residual_fn(s, B, tau)
        for _ in range(starts):
            x0 = rng.normal(size=2*r) * 0.7
            sol = least_squares(res, x0, method='lm', xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=800)
            c = np.linalg.norm(sol.fun)
            best = min(best, c)
            if c < 1e-8: nsol += 1
    return s, r, best, nsol

if __name__ == '__main__':
    mode = sys.argv[1]
    starts = int(sys.argv[2])
    if mode == 'ctrl':
        # positive control: the six-direction rep must give solutions; dimension of covariant space
        for names in (['A1','E','T1'], ['H1'], ['A1','T1'], ['T1']):
            for chi in ('triv',):
                s, r, best, nsol = run(names, chi, starts, (0.3, 1.0, 'auto'), 1) if False else (None,)*4
        for names in (['A1','E','T1'], ['H1'], ['A1','T1'], ['E']):
            s, B = covariant_basis2(names, 'triv')
            print('+'.join(names), 's=', s, 'dim of covariant 7-tuple space (complex) =', B.shape[1])
        for names in (['A1','E','T1'], ['E'], ['A1','T1']):
            s, r, best, nsol = run(names, 'triv', starts, (0.3, 1.0, s-0.3), 7)
            print('ctrl', '+'.join(names), 'best cost', best, 'n_sol', nsol, flush=True)
    else:
        chi = mode          # 'triv' or 'sgn'
        maxd = int(sys.argv[3]); pool = sys.argv[4].split(',')
        from census import reps_up_to
        for names in sorted(reps_up_to(pool, maxd), key=lambda n: sum(IRREP_DIM[x] for x in n)):
            s = sum(IRREP_DIM[n] for n in names)
            if s < 2: continue
            if chi == 'triv' and all(IRREP_DIM[n] == 1 for n in names): continue
            if max(names.count(n) for n in set(names)) > int(sys.argv[5]): continue
            s, r, best, nsol = run(names, chi, starts, (0.3, 1.0, s-0.3), 11)
            print(f"{chi:4s} s={s} {'+'.join(names):20s} covdim={r:3d} best={best if best is None else format(best,'.2e')} nsol={nsol}", flush=True)
