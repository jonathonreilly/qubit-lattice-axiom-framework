"""F3 (a)/(b): enumerate the admissible dressing generators G(k) (hermitian 4x4, trig polynomials on a stencil, cubic covariant)
and split them by P, T, C parity and by triviality ([G, H] = 0 identically).  Real-linear algebra on sampled values.
Also checks that cubic/P/T/C are symmetries of the undressed root H(k) (D1 root edge)."""
import numpy as np, itertools, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'arch'))
from f3_dirac import *
from dirac import D1

L = D1(0.909103708, 0.555604226)
def Hroot(k):            # k (..., 3)
    c = [L.S(k[..., j]) for j in range(3)]
    M = L.W(k[..., 0]) + L.W(k[..., 1]) + L.W(k[..., 2])
    return H_of(c, M)

rng = np.random.default_rng(7)
K = rng.uniform(-np.pi, np.pi, (40, 3))
Hk = Hroot(K)
R3 = [rot90(a) for a in range(3)]; SR = [spin90(a) for a in range(3)]
print('symmetry checks of the undressed root H(k) at 40 random k:')
for a in range(3):
    print('  cubic rot90 axis %d: max|H(Rk) - S H S^dag| = %.1e' % (a, np.abs(Hroot(K @ R3[a].T) - SR[a] @ Hk @ SR[a].conj().T).max()))
print('  P: max|H(-k) - beta H beta| = %.1e' % np.abs(Hroot(-K) - beta @ Hk @ beta).max())
print('  T: max|U_T H^* U_T^dag - H(-k)| = %.1e' % np.abs(U_T @ Hk.conj() @ U_T.conj().T - Hroot(-K)).max())
print('  C: max|U_C H^* U_C^dag + H(-k)| = %.1e' % np.abs(U_C @ Hk.conj() @ U_C.conj().T + Hroot(-K)).max())
print('  U_T U_T^* = %s ; U_C U_C^* = %s (x identity)' % (np.round((U_T @ U_T.conj())[0, 0], 6), np.round((U_C @ U_C.conj())[0, 0], 6)))

MB = herm_basis()

def stencil(kind):
    pts = set()
    for n in itertools.product((-2, -1, 0, 1, 2), repeat=3):
        n2 = sum(x*x for x in n); ninf = max(abs(x) for x in n)
        if kind == 'S19' and n2 <= 2: pts.add(n)
        if kind == 'S27' and ninf <= 1: pts.add(n)
        if kind == 'S33' and (ninf <= 1 or (n2 == 4)): pts.add(n)
    half = [n for n in pts if n > (0, 0, 0)]
    return sorted(half)

def funcs(kind):
    """real scalar functions: 1, cos(k.n), sin(k.n) for n in the half stencil."""
    F = [('1', lambda k: np.ones(k.shape[:-1]))]
    for n in stencil(kind):
        nn = np.array(n, float)
        F.append(('cos%s' % (n,), (lambda nn: lambda k: np.cos(k @ nn))(nn)))
        F.append(('sin%s' % (n,), (lambda nn: lambda k: np.sin(k @ nn))(nn)))
    return F

def ev(G, k):
    """G = list of (coef, fidx, midx) evaluated at k -> (..., 4, 4)."""
    return G(k)

def vec(vals):
    return np.concatenate([vals.real.ravel(), vals.imag.ravel()])

def analyse(kind, Kp):
    F = funcs(kind); nb = len(F)*len(MB)
    basis = [(fi, mi) for fi in range(len(F)) for mi in range(len(MB))]
    def Gval(i, k):
        fi, mi = basis[i]
        return np.multiply.outer(F[fi][1](k), MB[mi][1])
    ops = {
        'R0': lambda i, k: SR[0] @ Gval(i, k @ R3[0]) @ SR[0].conj().T,      # (R.G)(k) = S G(R^-1 k) S^dag ; R^-1 k = k @ R (orthogonal)
        'R1': lambda i, k: SR[1] @ Gval(i, k @ R3[1]) @ SR[1].conj().T,
        'R2': lambda i, k: SR[2] @ Gval(i, k @ R3[2]) @ SR[2].conj().T,
        'P': lambda i, k: beta @ Gval(i, -k) @ beta,
        'T': lambda i, k: -U_T @ Gval(i, -k).conj() @ U_T.conj().T,
        'C': lambda i, k: -U_C @ Gval(i, -k).conj() @ U_C.conj().T,
    }
    B = np.stack([vec(Gval(i, Kp)) for i in range(nb)], 1)
    A = {}
    for nm, op in ops.items():
        Bg = np.stack([vec(op(i, Kp)) for i in range(nb)], 1)
        X, res, rk, _ = np.linalg.lstsq(B, Bg, rcond=None)
        A[nm] = X
        assert np.abs(B @ X - Bg).max() < 1e-9, nm
    rkB = np.linalg.matrix_rank(B, 1e-9)
    def null(Mat, tol=1e-9):
        u, s, vt = np.linalg.svd(Mat)
        r = (s > tol*max(1, s[0])).sum()
        return vt[r:].T
    I = np.eye(nb)
    cub = null(np.vstack([A['R0'] - I, A['R1'] - I, A['R2'] - I]))
    # commutator map G -> [G, H] at samples
    Hs = Hroot(Kp)
    Cm = np.stack([vec(Gval(i, Kp) @ Hs - Hs @ Gval(i, Kp)) for i in range(nb)], 1)
    def dimfix(Vsub, extra=()):
        mats = [ (A[e] - I) @ Vsub for e in extra ] if extra else []
        if mats:
            W = Vsub @ null(np.vstack(mats))
        else:
            W = Vsub
        if W.shape[1] == 0:
            return W, 0, 0
        # independent functions (B W) and nontrivial part (rank of commutator image)
        rf = np.linalg.matrix_rank(B @ W, 1e-8) if W.shape[1] else 0
        rc = np.linalg.matrix_rank(Cm @ W, 1e-8) if W.shape[1] else 0
        return W, rf, rc
    print('\n[%s] stencil half-size %d -> %d real basis functions x matrices (rank %d)' % (kind, len(stencil(kind)), nb, rkB))
    W, rf, rc = dimfix(cub)
    print('  cubic-covariant hermitian generators: dim %d (nontrivial, i.e. rank of G -> [G,H]: %d)' % (rf, rc))
    # parity sectors inside the cubic-covariant space
    for sP in (+1, -1):
        for sT in (+1, -1):
            for sC in (+1, -1):
                mats = [A['R0'] - I, A['R1'] - I, A['R2'] - I, A['P'] - sP*I, A['T'] - sT*I, A['C'] - sC*I]
                Wp = null(np.vstack(mats))
                if Wp.shape[1] == 0:
                    rf2 = rc2 = 0
                else:
                    rf2 = np.linalg.matrix_rank(B @ Wp, 1e-8); rc2 = np.linalg.matrix_rank(Cm @ Wp, 1e-8)
                # beta-commutant (literal-reading admissible: [G, beta] = 0)
                Bc = np.stack([vec(Gval(i, Kp) @ beta - beta @ Gval(i, Kp)) for i in range(nb)], 1)
                Wl = Wp @ null(Bc @ Wp) if Wp.shape[1] else Wp
                rl = np.linalg.matrix_rank(Cm @ Wl, 1e-8) if Wl.shape[1] else 0
                print('    P%+d T%+d C%+d : dim %2d, nontrivial %2d ; of which [G,beta]=0 (literal branch) nontrivial %2d'
                      % (sP, sT, sC, rf2, rc2, rl))
    # identify the fully symmetric nontrivial sector with gamma.f candidates
    mats = [A['R0'] - I, A['R1'] - I, A['R2'] - I, A['P'] - I, A['T'] - I, A['C'] - I]
    Wsym = null(np.vstack(mats))
    ib_alpha = [[mi for mi, (nm, _) in enumerate(MB) if nm == 'i beta alpha_' + a][0] for a in 'xyz']
    def cand(fn):
        return vec(sum(np.multiply.outer(fn(Kp, j), MB[ib_alpha[j]][1]) for j in range(3)))
    def fvec(name):
        if name == 'G1': return lambda k, j: np.sin(k[..., j])
        if name == 'G2': return lambda k, j: np.sin(k[..., j])*(np.cos(k[..., (j+1) % 3]) + np.cos(k[..., (j+2) % 3]))
        if name == 'G3': return lambda k, j: np.sin(k[..., j])*np.cos(k[..., (j+1) % 3])*np.cos(k[..., (j+2) % 3])
        if name == 'G4': return lambda k, j: np.sin(2*k[..., j])
    names = ['G1', 'G2'] + (['G3'] if kind in ('S27', 'S33') else []) + (['G4'] if kind == 'S33' else [])
    # commutator images of the symmetric sector vs of the candidates
    imgS = Cm @ Wsym
    rS = np.linalg.matrix_rank(imgS, 1e-8)
    candC = []
    for nm in names:
        fn = fvec(nm)
        Gc = sum(np.multiply.outer(fn(Kp, j), MB[ib_alpha[j]][1]) for j in range(3))
        candC.append(vec(Gc @ Hs - Hs @ Gc))
    candC = np.stack(candC, 1)
    rboth = np.linalg.matrix_rank(np.hstack([imgS, candC]), 1e-8)
    print('  fully symmetric nontrivial sector: dim %d ; candidates %s (i beta alpha_j f_j = -gamma_j f_j) span rank %d ; joint rank %d'
          % (rS, names, np.linalg.matrix_rank(candC, 1e-8), rboth))

Kp = rng.uniform(-np.pi, np.pi, (48, 3))
for kind in ('S19', 'S27', 'S33'):
    analyse(kind, Kp)
