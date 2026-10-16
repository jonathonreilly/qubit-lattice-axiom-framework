"""Covariant unitary walks with an arbitrary coin representation of the binary cubic group.

U(k) = sum_n A_n e^{i k.n}, n in a stencil S (Chebyshev range 1 by default).
Covariance: A_{R n} = D(R) A_n D(R)^dagger for generators R of O with lifts D.
Unitarity: sum_n A_n A_{n-d}^dagger = delta_{d,0} I for every d in S - S.
Search: least squares from random starts with sum_{n != 0} ||A_n||^2 pinned to 1.
"""
import sys, itertools, numpy as np
from scipy.linalg import expm, null_space
from scipy.optimize import least_squares

def spin_mats(j):
    m = np.arange(j, -j - 1, -1); d = len(m)
    Jz = np.diag(m).astype(complex)
    Jp = np.zeros((d, d), complex)
    for i in range(1, d):
        Jp[i - 1, i] = np.sqrt(j * (j + 1) - m[i] * (m[i] + 1))
    Jx = (Jp + Jp.conj().T) / 2; Jy = (Jp - Jp.conj().T) / 2j
    return Jx, Jy, Jz

def rep(name):
    """Return list of (R, D) for the two quarter-turn generators."""
    Rz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]); Rx = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
    def lift(j):
        Jx, Jy, Jz = spin_mats(j)
        return [(Rz, expm(-1j * np.pi / 2 * Jz)), (Rx, expm(-1j * np.pi / 2 * Jx))]
    if name.startswith('block'):
        B = np.load('/tmp/claude-0/-home-user/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/walk/blockreps.npy')
        DZ, DX = B[int(name[5:])]
        return [(Rz, DZ.astype(complex)), (Rx, DX.astype(complex))]
    if name in ('E12+E52', 'E12+H', 'E12+E52+H'):
        from scipy.linalg import block_diag
        h = lift(0.5); out = []
        parts = {'E12': lambda k: h[k][1], 'E52': lambda k: -h[k][1], 'H': lambda k: lift(1.5)[k][1]}
        for k in range(2):
            out.append((h[k][0], block_diag(*[parts[p](k) for p in name.split('+')])))
        return out
    if name == 'spin1/2': return lift(0.5)
    if name == 'spin1/2-D2':
        Jx, Jy, Jz = spin_mats(0.5)
        Hz = np.diag([-1, -1, 1]); Hx = np.diag([1, -1, -1])
        return [(Hz, expm(-1j * np.pi * Jz)), (Hx, expm(-1j * np.pi * Jx))]
    if name == 'spin3/2': return lift(1.5)
    if name == 'spin1': return lift(1.0)
    if name == 'spin1+spin0':
        return [(R, np.block([[D, np.zeros((3, 1))], [np.zeros((1, 3)), np.ones((1, 1))]])) for R, D in lift(1.0)]
    if name == '2xspin1':
        return [(R, np.kron(np.eye(2), D)) for R, D in lift(1.0)]
    if name == '2xspin1/2':
        return [(R, np.kron(np.eye(2), D)) for R, D in lift(0.5)]
    if name == 'spin1/2+trivial-sign':  # spin1/2 (x) sign character of O (quarter turns -> -1)
        return [(R, -D) for R, D in lift(0.5)]
    if name == 'spin1/2(x)E':  # spin-1/2 tensor the 2-dim irrep E of O (factors through S3) = G' (4-dim)
        # E: quarter turns act as transpositions in the standard 2-dim rep of S3
        w = np.exp(2j * np.pi / 3)
        # realize S3 on C^2 via permutation rep of {x,y,z} restricted to sum-zero plane
        P = lambda perm: np.eye(3)[list(perm)]
        basis = np.array([[1, -1, 0], [1, 1, -2]], float).T; basis /= np.linalg.norm(basis, axis=0)
        def E_of(R):
            perm = np.abs(R)  # the axis permutation underlying R
            return basis.T @ perm @ basis
        return [(R, np.kron(E_of(R), D)) for R, D in lift(0.5)]
    raise ValueError(name)


def su2_lift(Q):
    """SU(2) element whose adjoint action is the SO(3) matrix Q."""
    from scipy.spatial.transform import Rotation
    rv = Rotation.from_matrix(Q).as_rotvec(); th = np.linalg.norm(rv)
    if th < 1e-12: return np.eye(2, dtype=complex)
    n = rv / th; sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1])
    return np.cos(th / 2) * np.eye(2) - 1j * np.sin(th / 2) * (n[0] * sx + n[1] * sy + n[2] * sz)

def perm_sign(R):
    P = np.abs(R); return int(round(np.linalg.det(P)))

def menu_rep(kind):
    Rz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]); Rx = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
    out = []
    for R in (Rz, Rx):
        sg = perm_sign(R)
        if kind == 'menu-trivial': Q = np.eye(3)
        elif kind == 'menu-sign': Q = np.diag([1, sg, sg]).astype(float)
        elif kind == 'menu-axis': Q = sg * np.abs(R).astype(float)
        elif kind == 'menu-full': Q = R.astype(float)
        out.append((R, su2_lift(Q)))
    return out

def stencil(kind):
    if kind == 'cube':
        return [np.array(v) for v in itertools.product((-1, 0, 1), repeat=3)]
    if kind == 'nn':
        return [np.zeros(3, int)] + [s * np.eye(3, dtype=int)[a] for a in range(3) for s in (1, -1)]
    raise ValueError(kind)

def setup(repname, kind):
    gens = menu_rep(repname) if repname.startswith('menu-') else rep(repname); d = gens[0][1].shape[0]
    S = stencil(kind); idx = {tuple(v): i for i, v in enumerate(S)}; N = len(S)
    nvar = N * d * d
    rows = []
    for R, D in gens:
        for i, n in enumerate(S):
            j = idx[tuple(R @ n)]
            # A_j - D A_i D^dag = 0  (linear in vec A, column-major vec)
            M = np.zeros((d * d, nvar), complex)
            M[:, j * d * d:(j + 1) * d * d] += np.eye(d * d)
            M[:, i * d * d:(i + 1) * d * d] -= np.kron(D.conj(), D)
            rows.append(M)
    K = null_space(np.vstack(rows))  # complex basis of covariant families
    diffs = sorted({tuple(a - b) for a in S for b in S})
    return d, S, idx, K, diffs

def make_residual(d, S, idx, K, diffs):
    N = len(S); zero = idx[(0, 0, 0)]
    pairs = []
    for dd in diffs:
        ii, jj = [], []
        for i, n in enumerate(S):
            m = tuple(np.array(n) - np.array(dd))
            if m in idx: ii.append(i); jj.append(idx[m])
        pairs.append((np.array(ii), np.array(jj), dd == (0, 0, 0)))
    nz = np.array([i for i in range(N) if i != zero]); I = np.eye(d)
    def res(x):
        p = x[:K.shape[1]] + 1j * x[K.shape[1]:]
        A = (K @ p).reshape(N, d, d).transpose(0, 2, 1)  # column-major blocks
        out = []
        for ii, jj, isz in pairs:
            acc = np.einsum('nab,ncb->ac', A[ii], A[jj].conj())
            if isz: acc = acc - I
            out.append(acc.real.ravel()); out.append(acc.imag.ravel())
        out.append(np.array([10.0 * max(0.0, 0.05 - np.sum(np.abs(A[nz]) ** 2))]))
        return np.concatenate(out)
    return res

if __name__ == '__main__':
    repname, kind, ntrial = sys.argv[1], sys.argv[2], int(sys.argv[3])
    d, S, idx, K, diffs = setup(repname, kind)
    print(repname, kind, 'coin dim', d, 'covariant family dim (complex)', K.shape[1], flush=True)
    resid = make_residual(d, S, idx, K, diffs); rng = np.random.default_rng(0); best = 1e9; hits = []
    for t in range(ntrial):
        x0 = rng.normal(size=2 * K.shape[1])
        r = least_squares(resid, x0, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=int(sys.argv[4]) if len(sys.argv) > 4 else 4000)
        res = np.linalg.norm(r.fun); best = min(best, res)
        if res < 1e-10: hits.append(r.x)
        print(f'    trial {t}: residual {res:.3e}  best {best:.3e}', flush=True)
    print(f'  moving unitary solutions: {len(hits)}/{ntrial}   best residual {best:.3e}', flush=True)
    np.save(f'hits_{repname.replace("/", "_")}_{kind}.npy', np.array(hits))
