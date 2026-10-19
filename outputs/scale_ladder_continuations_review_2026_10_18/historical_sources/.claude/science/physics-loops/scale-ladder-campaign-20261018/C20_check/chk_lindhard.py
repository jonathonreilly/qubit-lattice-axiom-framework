"""Independent Lindhard / channel check (C20 claim B).
Own code: vectorized static Lindhard per site, chi_ab(q) = (1/Nk) sum_k sum_nm (f_n(k)-f_m(k+q))/(e_m(k+q)-e_n(k))
<nk|O_a|m k+q><m k+q|O_b|nk>, O_a Frobenius-orthonormal Hermitian; own O_h projectors (A2 character = parity of the
axis permutation); finite-difference grand-potential check chi = -d^2 Omega/dh^2; T and grid scan."""
import sys, itertools, time
import numpy as np
from scipy.special import expit
from chk_common import load, bloch_fn

Mdl, X, Mm, seeds = load()
loc0 = Mdl['loc0']
bl = Mdl['blocks_from'](Mdl['H0'](-1.0, 0.2) + 0.05 * X)
Hk = bloch_fn(bl)
kst = Mdl['kst']; Q = Mdl['Q']
mu = np.linalg.eigvalsh(Hk(kst[None]))[0, 0]
print('mu = E_N =', mu)

# site-0 signed-permutation matrices of the dressed rotations / inversions
def smat(Ps):
    P, s = Ps; M = np.zeros((12, 12))
    for b, j in enumerate(loc0): M[loc0.index(P[j]), b] = (-1.0) ** s[j]
    return M
SR = [smat(g) for g in Mdl['rots']]; SI = [smat(g) for g in Mdl['invs']]
ROTS = Mdl['ROTS']

def a2char(Rm):
    p = [int(np.nonzero(Rm[i])[0][0]) for i in range(3)]
    inv = sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j]); return (-1) ** inv
def classO(Rm):
    tr = int(round(np.trace(Rm)))
    return {3: 'E', 0: 'C3', 1: 'C4'}.get(tr, 'C2' if np.allclose(np.abs(np.diag(Rm)), 1) else "C2'")
CH = {'A1': dict(E=1, C3=1, C2=1, C4=1, **{"C2'": 1}), 'A2': dict(E=1, C3=1, C2=1, C4=-1, **{"C2'": -1}),
      'E': dict(E=2, C3=-1, C2=2, C4=0, **{"C2'": 0}), 'T1': dict(E=3, C3=0, C2=-1, C4=1, **{"C2'": -1}),
      'T2': dict(E=3, C3=0, C2=-1, C4=-1, **{"C2'": 1})}
# sanity: A2 char from axis-permutation parity agrees with table
assert all(a2char(R_) == CH['A2'][classO(R_)] for R_ in ROTS)

# standard Hermitian orthonormal basis of 12x12 matrices, as vectors in R^144
basis = []
for i in range(12):
    for j in range(i, 12):
        B = np.zeros((12, 12), complex)
        if i == j: B[i, i] = 1
        else: B[i, j] = B[j, i] = 2 ** -0.5
        basis.append(B)
for i in range(12):
    for j in range(i + 1, 12):
        B = np.zeros((12, 12), complex); B[i, j] = 1j * 2 ** -0.5; B[j, i] = -1j * 2 ** -0.5; basis.append(B)
Bm = np.array(basis)
def to_vec(O): return np.einsum('aij,ij->a', Bm.conj(), O).real
def proj_op(name, par):
    ch = CH[name]; d = ch['E']
    P = np.zeros((144, 144))
    for k in range(24):
        c = ch[classO(ROTS[k])]
        for S, sgn in ((SR[k], 1), (SI[k], par)):
            D = np.array([to_vec(S @ B @ S.T) for B in Bm]).T
            P += sgn * c * D
    return P * d / 48
idv = to_vec(np.eye(12)) / np.sqrt(12)
Pt = np.eye(144) - np.outer(idv, idv)
sectors = {}
for nm in CH:
    for par, lab in ((1, 'g'), (-1, 'u')):
        P = proj_op(nm, par); w, V = np.linalg.eigh((P + P.T) / 2); Vs = V[:, w > 0.5]
        sectors[nm + lab] = Vs
print('multiplicities x dim:', {k: v.shape[1] for k, v in sectors.items()}, 'sum', sum(v.shape[1] for v in sectors.values()))

def chi_sector(Vs, qv, N, T, off, traceless=True):
    """Lindhard chi restricted to span(Vs) (columns: R^144 vectors); returns the restricted matrix."""
    if traceless:
        Vs = Pt @ Vs; u, s, _ = np.linalg.svd(Vs, full_matrices=False); Vs = u[:, s > 1e-8]
    Os = np.tensordot(Vs.T, Bm, 1)                       # (m,12,12)
    g = np.arange(N) * 2 * np.pi / N - np.pi
    K = np.array(list(itertools.product(g, g, g))) + off
    chi = np.zeros((Os.shape[0],) * 2, complex)
    for c0 in range(0, len(K), 2048):
        Kc = K[c0:c0 + 2048]
        e1, v1 = np.linalg.eigh(Hk(Kc)); e2, v2 = np.linalg.eigh(Hk(Kc + qv))
        f1 = expit(-(e1 - mu) / T); f2 = expit(-(e2 - mu) / T)
        de = e2[:, None, :] - e1[:, :, None]; df = f1[:, :, None] - f2[:, None, :]
        deg = np.abs(de) < 1e-10
        W = np.where(deg, (f1 * (1 - f1) / T)[:, :, None] * np.ones_like(de), df / np.where(deg, 1, de))
        M = np.einsum('kin,aij,kjm->aknm', v1.conj(), Os, v2)
        chi += np.einsum('aknm,knm,bknm->ab', M, W, M.conj())
    chi /= len(K)
    return (chi + chi.conj().T).real / 2, Vs

def top(name, qv, N, T, off, traceless=True):
    c, Vs = chi_sector(sectors[name], qv, N, T, off, traceless)
    w, V = np.linalg.eigh(c); return w[-1], Vs @ V[:, -1]

# 1) reproduce at the runner's setting (no O_h symmetrization here: raw grid)
t0 = time.time()
for lab, qv, names in (('q=0', np.zeros(3), ['A1u', 'T1u', 'T1g', 'A1g']), ('Q', Q, ['T2u', 'T2g', 'A2u', 'A2g'])):
    print(lab, {n: round(top(n, qv, 12, 0.01, 0.037)[0], 4) for n in names})
cA1g_full = top('A1g', np.zeros(3), 12, 0.01, 0.037, traceless=False)[0]
print('A1g including the trace (charge) channel:', round(cA1g_full, 4), f'({time.time()-t0:.0f}s)')

# 2) finite-difference grand potential check on the leading vectors
def Omega(Hfun, N, T, off):
    g = np.arange(N) * 2 * np.pi / N - np.pi
    K = np.array(list(itertools.product(g, g, g))) + off
    e = np.linalg.eigvalsh(Hfun(K)); x = -(e - mu) / T
    return -T * np.sum(np.logaddexp(0, x)) / len(K)
for lab, name, qv in (('q=0', 'A1u', None), ('Q', 'A2u', Q), ('Q', 'T2u', Q)):
    lam, vec = top(name, np.zeros(3) if qv is None else qv, 12, 0.01, 0.037)
    O = np.tensordot(vec, Bm, 1)
    def H_h(h):
        if qv is None: return lambda K: Hk(K) + h * O
        return lambda K: np.block([[Hk(K), np.broadcast_to(h * O, (len(K), 12, 12))],
                                   [np.broadcast_to(h * O, (len(K), 12, 12)), Hk(K + qv)]])
    fac = 1.0 if qv is None else 0.5     # folded 24x24 over the full zone counts each pair twice
    h = 2e-3
    Om = [fac * Omega(H_h(x), 12, 0.01, 0.037) for x in (-h, 0, h)]
    print(f'{lab} {name}: Lindhard {lam:.4f}  vs  -Omega\'\' = {-(Om[0]-2*Om[1]+Om[2])/h**2:.4f}')

# 3) robustness scan
print('scan: (N, T, offset) -> chi(A1u,0), chi(T1u,0), chi(T2u,Q), chi(A2u,Q)')
for N, T, off in ((12, 0.02, 0.037), (12, 0.01, 0.0), (16, 0.01, 0.021), (16, 0.005, 0.021), (20, 0.005, 0.013),
                  (24, 0.005, 0.009), (24, 0.0025, 0.009), (28, 0.0025, 0.005), (12, 0.05, 0.037), (16, 0.1, 0.02)):
    t0 = time.time()
    r = [top('A1u', np.zeros(3), N, T, off)[0], top('T1u', np.zeros(3), N, T, off)[0],
         top('T2u', Q, N, T, off)[0], top('A2u', Q, N, T, off)[0]]
    print(N, T, off, np.round(r, 4), f'({time.time()-t0:.0f}s)', flush=True)
