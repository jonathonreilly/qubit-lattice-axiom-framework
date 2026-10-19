"""G-invariant polynomials (degree <= 4) in the order-parameter components, by orbit sums over B3.
Fields (real copies R/I of complex components):
  l-sector: mR, mI in 3M (sym off-diagonal), nR, nI in 3M' (antisym)           -> 12 variables
  nu-sector: DR, DI diagonal (A1+E), pR, pI in 3M                                -> 12 variables
B3 acts by M -> g M g^T on each component matrix: a signed permutation of the 24 variables."""
import itertools, numpy as np, scipy.sparse as sp
from t4_core import B3, act
PAIRS = [(0, 1), (0, 2), (1, 2)]
def to_mat(typ, x):
    M = np.zeros((3, 3), dtype=np.result_type(x, float))
    if typ == 'D': M[np.arange(3), np.arange(3)] = x
    for k, (i, j) in enumerate(PAIRS):
        if typ == 'S': M[i, j] = M[j, i] = x[k]
        if typ == 'A': M[i, j] = x[k]; M[j, i] = -x[k]
    return M
def from_mat(typ, M):
    if typ == 'D': return np.diag(M).copy()
    return np.array([M[i, j] for (i, j) in PAIRS])
FIELDS = [('mR', 'S', 'l'), ('mI', 'S', 'l'), ('nR', 'A', 'l'), ('nI', 'A', 'l'),
          ('DR', 'D', 'n'), ('DI', 'D', 'n'), ('pR', 'S', 'n'), ('pI', 'S', 'n')]
NV = 3 * len(FIELDS)
SECTOR = np.array([0 if f[2] == 'l' else 1 for f in FIELDS for _ in range(3)])
IL = np.where(SECTOR == 0)[0]; IN = np.where(SECTOR == 1)[0]
def rep24(g):
    A = np.zeros((NV, NV))
    for v in range(NV):
        z = np.zeros(NV); z[v] = 1; A[:, v] = apply(g, z)
    return A
def apply(g, z):
    out = np.zeros(NV, dtype=np.result_type(z, float))
    for f, (nm, typ, sec) in enumerate(FIELDS):
        out[3 * f:3 * f + 3] = from_mat(typ, act(g, to_mat(typ, z[3 * f:3 * f + 3])))
    return out
REPS = [rep24(g) for g in B3]
PERM = []
for A in REPS:   # signed permutation: (A z)_v = s_v z_{pi(v)}
    pi = np.argmax(np.abs(A), axis=1); s = A[np.arange(NV), pi]
    assert np.allclose(np.abs(A).sum(1), 1); PERM.append((pi, s))
def zmat(z):
    """z (24) -> (Ml-part, Mnu-part) complex matrices (l without A1)."""
    m = to_mat('S', z[0:3] + 1j * z[3:6]) + to_mat('A', z[6:9] + 1j * z[9:12])
    n = to_mat('D', z[12:15] + 1j * z[15:18]) + to_mat('S', z[18:21] + 1j * z[21:24])
    return m, n
def zfrom(Ml_noA1, Mn):
    z = np.zeros(NV)
    for f, (nm, typ, sec) in enumerate(FIELDS):
        M = Ml_noA1 if sec == 'l' else Mn
        if typ == 'S': K = M - np.diag(np.diag(M)); K = (K + K.T) / 2
        elif typ == 'A': K = (M - M.T) / 2
        else: K = np.diag(np.diag(M))
        part = K.real if nm.endswith('R') else K.imag
        z[3 * f:3 * f + 3] = from_mat(typ, part)
    return z

def invariants(maxdeg=4):
    """orbit-sum basis. returns list of dicts {sorted index tuple: coeff}, bidegree list."""
    seen = set(); invs = []; bideg = []
    for d in range(1, maxdeg + 1):
        for mono in itertools.combinations_with_replacement(range(NV), d):
            if mono in seen: continue
            orb = {}
            for pi, s in PERM:
                # mono(Az) = prod_v (s_v z_pi(v))
                new = tuple(sorted(pi[v] for v in mono)); sg = np.prod([s[v] for v in mono])
                orb[new] = orb.get(new, 0) + sg
            seen.update(orb.keys())
            orb = {k: c / len(PERM) for k, c in orb.items() if abs(c) > 1e-9}
            if orb:
                invs.append(orb); nl = sum(SECTOR[v] == 0 for v in mono); bideg.append((nl, d - nl))
    return invs, bideg

class Poly:
    """sum_k c_k I_k as a flat monomial list with value/grad/hess."""
    def __init__(self, invs, coeffs):
        idx = []; w = []
        for I, c in zip(invs, coeffs):
            if c == 0: continue
            for mono, a in I.items():
                idx.append(list(mono) + [NV] * (4 - len(mono))); w.append(c * a)
        self.idx = np.array(idx, int).reshape(-1, 4); self.w = np.array(w)
    def val(self, z):
        ze = np.append(z, 1.0); return float(self.w @ np.prod(ze[self.idx], 1))
    def grad(self, z):
        ze = np.append(z, 1.0); Z = ze[self.idx]; g = np.zeros(NV + 1)
        for p in range(4):
            others = np.prod(np.delete(Z, p, 1), 1); np.add.at(g, self.idx[:, p], self.w * others)
        return g[:NV]
    def hess(self, z):
        ze = np.append(z, 1.0); Z = ze[self.idx]; H = np.zeros((NV + 1, NV + 1))
        for p in range(4):
            for q in range(4):
                if p == q: continue
                keep = [r for r in range(4) if r not in (p, q)]
                others = np.prod(Z[:, keep], 1); np.add.at(H, (self.idx[:, p], self.idx[:, q]), self.w * others)
        return H[:NV, :NV]

def inv_values(invs, Zs):
    """values of each invariant at points Zs (N x 24) -> (N x K)."""
    out = np.zeros((len(Zs), len(invs)))
    Ze = np.hstack([Zs, np.ones((len(Zs), 1))])
    for k, I in enumerate(invs):
        idx = np.array([list(m) + [NV] * (4 - len(m)) for m in I]); c = np.array(list(I.values()))
        out[:, k] = np.prod(Ze[:, idx], 2) @ c
    return out
def u1_rotate(Z, al, an):
    """U(1)_l x U(1)_nu: rotate (R,I) copies of every complex component."""
    Z = Z.copy(); al = np.reshape(np.asarray(al, float), (-1, 1)); an = np.reshape(np.asarray(an, float), (-1, 1))
    for (a, b, ang) in [(0, 3, al), (6, 9, al), (12, 15, an), (18, 21, an)]:
        R, I = Z[:, a:a + 3].copy(), Z[:, b:b + 3].copy()
        Z[:, a:a + 3] = np.cos(ang) * R - np.sin(ang) * I; Z[:, b:b + 3] = np.sin(ang) * R + np.cos(ang) * I
    return Z
