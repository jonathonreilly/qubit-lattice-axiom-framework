"""TW-2 (a): the minimal taste-splitting term family on NF-1's staggered edge (s = SymS(0.909103708), r = 0, continuous time).

Reduced-zone (offset) basis of nf1_alg.py: H(k)[n, n'] = <k + pi n| H |k + pi n'>, k unfolded; Gamma_j, Gamma_eps from nf1_gammas.npy,
dictionary U (nf1_dict.npy): U Gamma_j U^dag = alpha_j x 1_2, U Gamma_eps U^dag = beta x 1_2 (taste factor = second tensor slot).
A k-independent 8x8 matrix M times a scalar symbol g(k) is a legal (single-valued, local) staggered operator iff the folding rule
P_m [g(k) M] P_m = g(k + pi m) M holds for all m in {0,1}^3 (P_m = offset permutation n -> n xor m = multiplication by (-1)^{m.x}).
Checks (all printed):
 1. Folding-sign classes: for each sign character chi_c(m) = (-1)^{c.m} the space of M with P_m M P_m = chi_c(m) M (dimension 8 each).
 2. Taste-split MASS family: M in that class with {M, Gamma_j} = 0 (j = 1,2,3) and [M, Gamma_eps] = 0  (dictionary: beta x B, B in M_2).
    Taste-nonsinglet mass beta x (n.tau) needs c != 0; minimal symbol g with g(k + pi m) = (-1)^{c.m} g(k), g(0) != 0:
    c = (1,1,0) -> g = cos k1 cos k2 (face-diagonal hop, range sqrt 2), etc.  Reports dim and the dictionary image (which tau).
 3. Twisted (eps-odd) family: {M, Gamma_eps} = 0, {M, Gamma_j} = 0 (dictionary i beta g5 x B).  Reports which c carries the singlet and
    which the triplet (the eps-odd hop option of TESTS 'TW-2 (a)').
 4. Position space (L = 8): the face-diagonal operator O_12 = cos k1 cos k2 M_(110); hermitian, range, sublattice, translation-by-2,
    commutation with the shifts S_1, S_2, S_3 and with eps; spectrum of h + m eps + sigma O_12 at the corners = |m +- sigma|.
 5. Cubic rotations (L = 4): search the staggered representation chi(x) -> f(x) chi(R^-1 x), f a 2-periodic sign field, for C4[001],
    C2[100], C2[110], C3[111]; then the action on O_12, O_23, O_31 (does any proper rotation keep a taste-split mass invariant?).
"""
import numpy as np, sys, os, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'flat'))
from sublum import SymS
from f3_dirac import alpha, beta, g5
BF = 0.909103708
A = SymS(BF)
G4 = np.load(os.path.join(HERE, 'nf1_gammas.npy')); Ud = np.load(os.path.join(HERE, 'nf1_dict.npy'))
Gam, Geps = G4[:3], G4[3]
bits = [((i >> 0) & 1, (i >> 1) & 1, (i >> 2) & 1) for i in range(8)]
idx = lambda n: n[0] + 2*n[1] + 4*n[2]
def P(m):
    Pm = np.zeros((8, 8))
    for n in bits:
        Pm[idx(n), idx(tuple((a + b) % 2 for a, b in zip(n, m)))] = 1.0
    return Pm
Ms = [tuple(b) for b in bits]
print('1. P_111 == Gamma_eps: %s' % np.allclose(P((1, 1, 1)), Geps))
tau = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1., -1.]).astype(complex)]
I2 = np.eye(2)


def nullspace(rows, tol=1e-10):
    Aq = np.array(rows)
    u, s, vh = np.linalg.svd(Aq)
    r = int((s > tol).sum())
    return vh[r:].conj()


def solve_class(c, eps_comm):
    """M (8x8 complex) with P_m M P_m = (-1)^{c.m} M, {M, Gamma_j} = 0, [M, Geps] = 0 (eps_comm=True) or {M, Geps} = 0."""
    rows = []
    E = [np.zeros(64) for _ in range(64)]
    for i in range(64):
        E[i] = np.zeros(64); E[i][i] = 1
    def lin(op):
        # op: function M -> 8x8; build its 64x64 matrix acting on vec(M)
        return np.array([op(E[i].reshape(8, 8)).ravel() for i in range(64)]).T
    for m in Ms:
        sg = (-1)**(c[0]*m[0] + c[1]*m[1] + c[2]*m[2])
        Pm = P(m)
        rows += list(lin(lambda X: Pm @ X @ Pm - sg*X))
    for j in range(3):
        rows += list(lin(lambda X, j=j: Gam[j] @ X + X @ Gam[j]))
    if eps_comm:
        rows += list(lin(lambda X: Geps @ X - X @ Geps))
    else:
        rows += list(lin(lambda X: Geps @ X + X @ Geps))
    ns = nullspace(rows)
    return [v.reshape(8, 8) for v in ns]


CLN, CLM = [], []
_gens = [alpha[0], alpha[1], alpha[2], beta]; _gn = ['a1', 'a2', 'a3', 'b']
for _r in range(5):
    for _sub in itertools.combinations(range(4), _r):
        _X = np.eye(4, dtype=complex)
        for _s in _sub:
            _X = _X @ _gens[_s]
        CLN.append('.'.join(_gn[_s] for _s in _sub) or '1'); CLM.append(_X)
TAU = [I2] + tau


def dict_image(M):
    """full decomposition of U M U^dag in (16 Clifford monomials of alpha_j, beta) x (1, tau_1, tau_2, tau_3) of the dictionary frame."""
    X = Ud @ M @ Ud.conj().T
    out = {}
    rec = np.zeros_like(X)
    for cn, C in zip(CLN, CLM):
        for tn, T in zip(('1', 't1', 't2', 't3'), TAU):
            B = np.kron(C, T)
            coef = np.trace(B.conj().T @ X)/8
            rec += coef*B
            if abs(coef) > 1e-9:
                out['%s(x)%s' % (cn, tn)] = complex(np.round(coef, 6))
    return out, np.abs(rec - X).max()


def herm_norm(M):
    for ph in (1, 1j):
        if np.allclose(ph*M, (ph*M).conj().T, atol=1e-12):
            M = ph*M; break
    return M/np.sqrt(np.trace(M @ M).real/8)


print('1b. dictionary images of the offset permutations P_m (= multiplication by (-1)^{m.x}):')
for m in Ms:
    print('   m=%s: %s' % (''.join(map(str, m)), dict_image(P(m))[0]))
print('2. taste-split MASS family ({M, Gamma_j} = 0, [M, Geps] = 0) by folding class c (symbol sign (-1)^{c.m}):')
MASS = {}
for c in Ms:
    sol = solve_class(c, True)
    line = '   c=%s: dim %d' % (''.join(map(str, c)), len(sol))
    if sol:
        M = herm_norm(sol[0])
        im, res = dict_image(M)
        MASS[c] = M
        line += ' ; M^2 = 1: %s ; hermitian %s ; dictionary image %s (resid %.1e)' % (np.allclose(M @ M, np.eye(8)), np.allclose(M, M.conj().T),
                                                                                 {k: np.round(v, 6) for k, v in im.items()}, res)
    print(line)
print('   minimal symbols: c=000 -> 1 (on-site eps: the singlet mass); c=110 -> cos k1 cos k2; c=011 -> cos k2 cos k3; c=101 -> cos k1 cos k3')
print('3. twisted (eps-odd) family ({M, Gamma_j} = 0, {M, Geps} = 0):')
TW = {}
for c in Ms:
    sol = solve_class(c, False)
    line = '   c=%s: dim %d' % (''.join(map(str, c)), len(sol))
    if sol:
        M = herm_norm(sol[0])
        im, res = dict_image(M)
        TW[c] = M
        line += ' ; dictionary image %s' % ({k: np.round(v, 6) for k, v in im.items()})
    print(line)
print('   minimal symbols: c=001 -> cos k3 (NN hop along 3); c=111 -> cos k1 cos k2 cos k3 (body diagonal)')
np.save(os.path.join(HERE, 'tw2_mass_ops.npy'), np.array([MASS[(1, 1, 0)], MASS[(0, 1, 1)], MASS[(1, 0, 1)]]))

# ---- 4. position space ----
def gsym(c, k):
    out = 1.0
    for j in range(3):
        if c[j]:
            out = out*np.cos(k[j])
    return out


def pos_op(c, M, L):
    """O[x,y] = sum_d M[d,0] (-1)^{d.x} G(x - y), G = kernel of the minimal symbol (consistent with the folding rule)."""
    V = L**3
    X = np.array(np.unravel_index(np.arange(V), (L, L, L))).T
    k1 = 2*np.pi*np.arange(L)/L
    KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')
    gk = gsym(c, (KX, KY, KZ))
    Gr = np.real(np.fft.ifftn(gk))              # G(r) = (1/V) sum_k g(k) e^{ikr}
    D = (X[:, None, :] - X[None, :, :]) % L
    Gxy = Gr[D[..., 0], D[..., 1], D[..., 2]]
    cx = np.zeros(V, complex)
    for d in Ms:
        cx += M[idx(d), 0]*(-1.0)**(X @ np.array(d))
    return cx[:, None]*Gxy, X


sys.path.insert(0, HERE)
import importlib.util
spec = importlib.util.spec_from_file_location('nf1alg_pos', os.path.join(HERE, 'nf1_alg.py'))
# reuse nf1_alg's dense staggered h builder without rerunning its prints: copy of pos_space (t = 0, no links)
def pos_h(L):
    k1 = 2*np.pi*np.arange(L)/L
    ker = np.fft.ifft(A.s(k1))
    V = L**3
    X = np.array(np.unravel_index(np.arange(V), (L, L, L))).T
    eta = [np.ones(V), (-1.0)**X[:, 0], (-1.0)**(X[:, 0] + X[:, 1])]
    H = np.zeros((V, V), complex)
    for j in range(3):
        for r in range(1, L):
            Y = X.copy(); Y[:, j] = (Y[:, j] + r) % L
            H[np.arange(V), np.ravel_multi_index(Y.T, (L, L, L))] += eta[j]*ker[r]
    return H, X


L = 8
H0, X = pos_h(L)
V = L**3
eps = (-1.0)**X.sum(1)
def shift(j, zeta):
    Y = X.copy(); Y[:, j] = (Y[:, j] + 1) % L
    S = np.zeros((V, V)); S[np.arange(V), np.ravel_multi_index(Y.T, (L, L, L))] = zeta
    return S
S1 = shift(0, (-1.0)**(X[:, 1] + X[:, 2])); S2 = shift(1, (-1.0)**X[:, 2]); S3 = shift(2, np.ones(V))
T2 = [shift(j, np.ones(V)) for j in range(3)]
print('4. position space L=%d: shifts commute with h: %.1e %.1e %.1e' % (L, *[np.abs(S @ H0 - H0 @ S).max() for S in (S1, S2, S3)]))
for c, nm in (((1, 1, 0), 'O_12'), ((0, 1, 1), 'O_23'), ((1, 0, 1), 'O_31')):
    O, _ = pos_op(c, MASS[c], L)
    Dd = (X[None, :, :] - X[:, None, :] + L//2) % L - L//2
    nz = np.abs(O) > 1e-12
    hops = sorted(set(tuple(v) for v in Dd[nz]))
    sameSL = np.abs(O[(eps[:, None]*eps[None, :]) < 0]).max()
    tr2 = max(np.abs(Tm @ Tm @ O - O @ Tm @ Tm).max() for Tm in T2)
    com = ['%+.0f' % (0 if np.abs(S @ O - O @ S).max() < 1e-12 else (-1 if np.abs(S @ O + O @ S).max() < 1e-12 else np.nan)) for S in (S1, S2, S3)]
    print('   %s: hermitian %.1e ; hop vectors %s ; opposite-sublattice weight %.1e ; [T_j^2, O] %.1e ; commutes(0)/anticommutes(-1) with S1,S2,S3: %s ; [eps,O] %.1e ; {h,O} %.1e'
          % (nm, np.abs(O - O.conj().T).max(), hops, sameSL, tr2, com, np.abs(eps[:, None]*O - O*eps[None, :]).max(),
             np.abs(H0 @ O + O @ H0).max()))
    if c == (1, 1, 0):
        O12 = O
for (m, sg) in ((0.05, 0.03), (0.05, 0.05)):
    Ht = H0 + m*np.diag(eps) + sg*O12
    ev = np.sort(np.abs(np.linalg.eigvalsh(Ht)))[:16]
    print('   h + %.2f eps + %.2f O_12: lowest |E| = %s  (expect |m - sigma| x4, |m + sigma| x4 at the corners)' % (m, sg, np.round(ev[:10], 6)))

# ---- 5. cubic rotations on L = 4 ----
L = 4
H4, X4 = pos_h(L); V4 = L**3
def rot_perm(R):
    Y = (X4 @ R.T) % L
    return np.ravel_multi_index(Y.T, (L, L, L))
rots = {'C4[001]': np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]), 'C2[100]': np.diag([1, -1, -1]),
        'C2[110]': np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]]), 'C3[111]': np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])}
Os = {nm: pos_op(c, MASS[c], L)[0] for c, nm in (((1, 1, 0), 'O_12'), ((0, 1, 1), 'O_23'), ((1, 0, 1), 'O_31'))}
eps4 = (-1.0)**X4.sum(1)
print('5. cubic rotations (L = 4), Q: chi(x) -> f(x) chi(R^-1 x), f 2-periodic sign field; Q h Q^dag = h:')
for nm, R in rots.items():
    pr = rot_perm(R)                                   # site x -> R x
    Pm = np.zeros((V4, V4)); Pm[pr, np.arange(V4)] = 1.0   # |x> -> |R x>
    found = []
    for fb in itertools.product((1, -1), repeat=7):
        F = np.array((1,) + fb)
        f = F[(X4[:, 0] % 2) + 2*(X4[:, 1] % 2) + 4*(X4[:, 2] % 2)]
        Q = np.diag(f) @ Pm
        if np.abs(Q @ H4 @ Q.T - H4).max() < 1e-10:
            found.append(Q)
        elif np.abs(Q @ H4 @ Q.T + H4).max() < 1e-10:
            pass
    acts = []
    if found:
        Q = found[0]
        for on, O in Os.items():
            img = Q @ O @ Q.T
            hit = [('%s%s' % ('+' if np.abs(img - O2).max() < 1e-10 else '-', n2)) for n2, O2 in Os.items()
                   if np.abs(img - O2).max() < 1e-10 or np.abs(img + O2).max() < 1e-10]
            acts.append('%s -> %s' % (on, hit if hit else 'other'))
        acts.append('eps -> %s' % ('+eps' if np.abs(Q @ np.diag(eps4) @ Q.T - np.diag(eps4)).max() < 1e-12 else '-eps'))
    print('   %s: %d sign fields found; action: %s' % (nm, len(found), '; '.join(acts)))
