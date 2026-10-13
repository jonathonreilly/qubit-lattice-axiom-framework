"""Shared machinery for R19-23: the R19-19 invariant kernel space (same construction, same seed),
the linearized Einstein-Hilbert kernel, and the full 10x10 quadratic symbol Q(omega, q) = s*K_EH - eps*Pi.
Conventions follow r1919_gauge.py: p_mu = (omega, q) lower, contracts the kernel's upper indices;
gauge directions h_{mu nu} = p_mu xi_nu + p_nu xi_mu; rows use e:e = 2.
Normalization: s is fixed so that for a TT e (e:e = 2) at q along z, e.(s K_EH).e = omega^2 - q^2.
Then the TT pole is omega^2 = q^2 + eps * e.Pi.e (R9-9: (M^2/2)(omega^2-q^2) = Pi, eps = 2/M^2 = 16 pi at a = l_P)."""
import numpy as np, itertools
rng = np.random.default_rng(7)
D = 4
eta = np.diag([-1., 1, 1, 1])
G = []
for p in itertools.permutations(range(3)):
    for s in itertools.product([1, -1], repeat=3):
        for tsgn in (1, -1):
            M = np.zeros((4, 4)); M[0, 0] = tsgn
            for i in range(3): M[1+i, 1+p[i]] = s[i]
            G.append(M)
def act(R, T):
    for ax in range(T.ndim):
        T = np.moveaxis(np.tensordot(R, T, axes=([1], [ax])), 0, ax)
    return T
def symB(T):
    T = (T + T.transpose(1,0,2,3,4,5))/2; T = (T + T.transpose(0,1,3,2,4,5))/2
    T = (T + T.transpose(2,3,0,1,4,5))/2; T = (T + T.transpose(0,1,2,3,5,4))/2
    return T
def symA(T):
    T = (T + T.transpose(1,0,2,3))/2; T = (T + T.transpose(0,1,3,2))/2
    T = (T + T.transpose(2,3,0,1))/2
    return T
def reyn(T, sym):
    T = sym(T); out = np.zeros_like(T)
    for R in G: out += act(R, T)
    return out/len(G)
def basis(shape, sym, nsamp):
    Ts = [reyn(rng.normal(size=shape), sym).ravel() for _ in range(nsamp)]
    M = np.array(Ts); u, s, vt = np.linalg.svd(M, full_matrices=False)
    r = int((s > 1e-10*s[0]).sum())
    return vt[:r].reshape((r,)+shape), s
Bb, _ = basis((D,)*6, symB, 60)
Ab, _ = basis((D,)*4, symA, 30)

def EH():
    B = np.zeros((4,)*6)
    for m, n, r, s_, A, Bi in itertools.product(range(4), repeat=6):
        pA = eta[A]; pB = eta[Bi]
        val = 0.5*(eta[m, r]*eta[n, s_] + eta[m, s_]*eta[n, r])*eta[A, Bi]
        val -= 0.5*(pA[m]*pB[r]*eta[n, s_] + pA[m]*pB[s_]*eta[n, r] + pA[n]*pB[r]*eta[m, s_] + pA[n]*pB[s_]*eta[m, r])
        val += pA[m]*pB[n]*eta[r, s_] + pA[r]*pB[s_]*eta[m, n]
        val -= eta[m, n]*eta[r, s_]*eta[A, Bi]
        B[m, n, r, s_, A, Bi] = val
    return symB(B)
Beh = EH()

# symmetric basis of h_{mu nu}: E_a with E_a:E_b = delta_ab (orthonormal in Frobenius)
PAIRS = [(m, n) for m in range(4) for n in range(m, 4)]
EB = []
for (m, n) in PAIRS:
    E = np.zeros((4, 4))
    if m == n: E[m, m] = 1.
    else: E[m, n] = E[n, m] = 1/np.sqrt(2)
    EB.append(E)
EB = np.array(EB)
NAMES = ['h%d%d' % pq for pq in PAIRS]

def kernel(A, B, p):
    return A + np.einsum('mnrsab,a,b->mnrs', B, p, p)
def mat(K):
    return np.einsum('aij,ijkl,bkl->ab', EB, K, EB)

r2 = np.sqrt(2)
def emb(e3):
    e = np.zeros((4, 4)); e[1:, 1:] = e3; return e
Eg = emb(np.diag([1., -1, 0])); T2 = np.zeros((3, 3)); T2[0, 1] = T2[1, 0] = 1; T2 = emb(T2)
a3 = np.array([1, -1, 0])/r2; b3 = np.array([0, 0, 1.])
F1 = emb(np.outer(a3, a3)-np.outer(b3, b3)); F2 = emb(np.outer(a3, b3)+np.outer(b3, a3))
z3 = np.array([0, 0, 1.]); fd3 = np.array([1, 1, 0])/r2
t4 = np.array([1., 0, 0, 0])
NAMED = [('Eg', z3, Eg), ('T2g', z3, T2), ('face1', fd3, F1), ('face2', fd3, F2)]

# normalization s
_p = np.array([0.3, 0, 0, 0.7])
_v = np.einsum('ij,ijkl,kl->', Eg, kernel(0*Ab[0], Beh, _p), Eg)
s_EH = (0.3**2 - 0.7**2)/_v

def rows(A, B):
    out = []
    for nm, n, e in NAMED:
        ct = np.einsum('ij,kl,ijklab,a,b->', e, e, B, t4, t4)
        nn = np.concatenate([[0.], n])
        cs = np.einsum('ij,kl,ijklab,a,b->', e, e, B, nn, nn)
        out.append(ct + cs)
    out += [np.einsum('ij,kl,ijkl->', Eg, Eg, A), np.einsum('ij,kl,ijkl->', T2, T2, A)]
    return np.array(out)

def wardA(A, nus): return A[:, nus].ravel()
def wardB(B, nus):
    C = B.copy()
    C = (C + C.transpose(4,1,2,3,0,5) + C.transpose(5,1,2,3,4,0))/3
    C = (C + C.transpose(0,1,2,3,5,4))/2
    C = (C + C.transpose(4,1,2,3,0,5) + C.transpose(5,1,2,3,4,0))/3
    return C[:, nus].ravel()
def nullspace(M, tol=1e-9):
    if M.shape[0] == 0: return np.eye(M.shape[1])
    u, s, vt = np.linalg.svd(M)
    r = int((s > tol*max(s[0], 1e-300)).sum())
    return vt[r:].T
# Ward-allowed subspaces
NB_full = nullspace(np.array([wardB(B, [0,1,2,3]) for B in Bb]).T)
NB_sp = nullspace(np.array([wardB(B, [1,2,3]) for B in Bb]).T)
NA_sp = nullspace(np.array([wardA(A, [1,2,3]) for A in Ab]).T)
def combA(th): return np.tensordot(th, Ab, 1)
def combB(th): return np.tensordot(th, Bb, 1)

def Qmat(A, B, omega, qvec, eps):
    p = np.concatenate([[omega], qvec])
    return s_EH*mat(kernel(0*A, Beh, p)) - eps*mat(kernel(A, B, p))
def Qparts(A, B, qvec, eps):
    """Q(omega) = Q0 + omega Q1 + omega^2 Q2 exactly (degree <= 2)."""
    Q0 = Qmat(A, B, 0., qvec, eps)
    Qp = Qmat(A, B, 1., qvec, eps); Qm = Qmat(A, B, -1., qvec, eps)
    Q1 = (Qp - Qm)/2; Q2 = (Qp + Qm)/2 - Q0
    return Q0, Q1, Q2
def gauge_dirs(omega, qvec):
    p = np.concatenate([[omega], qvec]); out = []
    for nu in range(4):
        xi = np.zeros(4); xi[nu] = 1.
        h = np.outer(p, xi) + np.outer(xi, p)
        out.append(np.einsum('aij,ij->a', EB, h))
    return np.array(out).T   # 10 x 4
def vec(h): return np.einsum('aij,ij->a', EB, h)
