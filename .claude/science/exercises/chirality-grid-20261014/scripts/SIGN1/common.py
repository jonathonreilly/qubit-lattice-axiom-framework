"""SIGN-1 common objects: Spin(10) 16 via real Cl(9) gammas, Majorana conversion, X2 vertex bilinears B^a.
Conventions: complex modes m = s*16 + alpha (s = walker spin, alpha = Spin(10) 16 index), 32 modes per vertex.
Majoranas p = tau*n + m, psi = (g1 + i g2)/2, i.e. psi = U gamma with U = (1/2)[I, iI].
A bilinear gamma^T K gamma (K antisymmetric) is the operator; Hermitian iff K = (i/2) a with a real antisymmetric.
"""
import numpy as np, itertools

I2 = np.eye(2); X = np.array([[0., 1], [1, 0]]); Z = np.diag([1., -1]); E = np.array([[0., 1], [-1, 0]])  # E = i sigma_y
SY = np.array([[0, -1j], [1j, 0]])

def kron(*ms):
    out = np.array([[1.0]])
    for m in ms: out = np.kron(out, m)
    return out

def cl9_gammas():
    """9 mutually anticommuting real symmetric 16x16 matrices squaring to 1 (Pauli strings, even # of E)."""
    lab = {"I": I2, "X": X, "Z": Z, "E": E}
    cands = []
    for s in itertools.product("IXZE", repeat=4):
        if s.count("E") % 2 == 0 and s != ("I",) * 4:
            cands.append(kron(*[lab[c] for c in s]))
    n = len(cands)
    anti = np.array([[np.allclose(cands[i] @ cands[j], -cands[j] @ cands[i]) for j in range(n)] for i in range(n)])
    best = []
    def bt(cl, start):
        nonlocal best
        if len(cl) > len(best): best = list(cl)
        if len(best) == 9: return True
        for j in range(start, n):
            if all(anti[j, c] for c in cl):
                cl.append(j)
                if bt(cl, j + 1): return True
                cl.pop()
        return False
    bt([], 0)
    G = [cands[i] for i in best]
    assert len(G) == 9
    for a in range(9):
        assert np.allclose(G[a], G[a].T) and np.allclose(G[a] @ G[a], np.eye(16))
        for b in range(a):
            assert np.allclose(G[a] @ G[b] + G[b] @ G[a], 0)
    return G

G9 = cl9_gammas()
N10 = [g.astype(complex) for g in G9] + [1j * np.eye(16)]          # N^a, a = 1..10 (index 0..9)

def spin10_gens():
    """anti-Hermitian generators on the 16: Gamma^a Gamma^b (a<b<=9) and i Gamma^a; labelled by planes (a,b), b=9 is direction 10."""
    gens = {}
    for a in range(9):
        for b in range(a + 1, 9):
            gens[(a, b)] = (G9[a] @ G9[b]).astype(complex)
        gens[(a, 9)] = 1j * G9[a]
    return gens

def realify(M):
    """real 2n x 2n matrix of a complex-linear map psi -> M psi acting on gamma (tau-major ordering)."""
    return np.block([[M.real, -M.imag], [M.imag, M.real]])

def antireal(M):
    """real matrix O with Theta gamma Theta^-1 = O gamma for the antiunitary Theta psi Theta^-1 = M psi."""
    return np.block([[M.real, -M.imag], [-M.imag, -M.real]])

def Umat(n):
    return 0.5 * np.hstack([np.eye(n), 1j * np.eye(n)])

def pairing_K(M):
    """psi^T M psi (M antisymmetric, n x n)  ->  gamma^T K gamma."""
    n = M.shape[0]; U = Umat(n)
    K = U.T @ M @ U
    return 0.5 * (K - K.T)

def density_K(h):
    """psi^dag h psi  ->  gamma^T K gamma + const (antisymmetric part only)."""
    n = h.shape[0]; U = Umat(n)
    K = U.conj().T @ h @ U
    return 0.5 * (K - K.T)

def vertex_B():
    """K matrices (64x64 complex antisymmetric) of B^a = psi^T (i sigma_y x N^a) psi on one vertex (32 modes)."""
    return [pairing_K(np.kron(1j * SY, Na)) for Na in N10]

def alt_s(X_, Y_, idx):
    """6-term symmetrised antisymmetriser at quadruples idx (S,4), i<j<k<l."""
    i, j, k, l = idx.T
    return (X_[i, j] * Y_[k, l] - X_[i, k] * Y_[j, l] + X_[i, l] * Y_[j, k]
            + Y_[i, j] * X_[k, l] - Y_[i, k] * X_[j, l] + Y_[i, l] * X_[j, k])
