AUDIT_INPUT_PATHS = ('docs/TWO_LAYER_CUBE_TICK_HAS_EXACT_SO4_AND_NO_CORNER_SU4_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Ruleset C commutant test: two fermion modes per site, CL-1 cube tick, face phase -1, no copy mass.

Computes, exactly (linear algebra on the 16 modes of one 2x2x2 cell, Bloch form):
  (1) the K-independent cell-local commutant of the free two-layer tick, number-conserving and pairing parts,
      and its Lie algebra;
  (2) whether any operator on corner labels (X x 1_layer) commutes with the tick, exactly or at the Dirac
      point to first order, and what survives the lattice rotations;
  (3) the same for other hop-phase choices with product -1 around every face, plus controls.
Supplied model; finite diagnostic; no physical identification.
"""
import itertools, signal, sys
import numpy as np

AUDIT_TIMEOUT_SEC = 60
signal.signal(signal.SIGALRM, lambda *a: (print('TIMEOUT'), sys.exit(1)))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
np.random.seed(20261022)
PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"{'PASS' if ok else 'FAIL'}: {name}" + (f"  [{detail}]" if detail else ''))


CORN = list(itertools.product([0, 1], repeat=3))
IDX = {c: i for i, c in enumerate(CORN)}
E3 = np.eye(3, dtype=int)
EPSC = np.diag([(-1.0) ** sum(c) for c in CORN])          # corner parity (sublattice sign)
ISY = np.array([[0, 1], [-1, 0]], dtype=complex)            # i sigma_y on the layer bit


def eta_perm(perm, gauge=None, q=(0, 0, 0)):
    """Staggered phases with axis order perm (product -1 on every face), times a site gauge and a uniform
    holonomy q per axis; all such choices have face product -1."""
    def eta(i, p):
        j = perm.index(i)
        s = (-1) ** sum(p[perm[k]] for k in range(j))
        g = 1.0 if gauge is None else gauge[tuple(np.add(p, E3[i]) % 2)] * np.conj(gauge[tuple(np.array(p) % 2)])
        return s * g * np.exp(1j * q[i])
    return eta


def terms(anchor, eta):
    T = []
    for c in CORN:
        p = np.array(anchor) + np.array(c)
        for i in range(3):
            if c[i] == 0:
                qq = p + E3[i]
                amp = eta(i, tuple(p)) / np.sqrt(3)
                d = qq // 2 - p // 2
                a, b = IDX[tuple(qq % 2)], IDX[tuple(p % 2)]
                T += [(a, b, amp, d), (b, a, np.conj(amp), -d)]
    return T


def Rmat(T, K, order=None):
    R = np.zeros((8, 8), complex)
    for a, b, amp, d in T:
        R[a, b] += amp * np.exp(1j * np.dot(K, d))
    return R


class Tick:
    def __init__(self, eta, eps=0.37, mu=0.0):
        self.Te, self.To, self.eps, self.mu = terms((0, 0, 0), eta), terms((1, 1, 1), eta), eps, mu

    def U(self, K):
        e, m = self.eps, self.mu
        Re, Ro = Rmat(self.Te, K), Rmat(self.To, K)
        from scipy.linalg import expm
        return expm(1j * (e + m / 2) * Ro) @ expm(-1j * (e - m / 2) * Re)

    def taylor(self):
        """U(k) = 1 + sum_i k_i a_i + sum_ij k_i k_j b_ij + ... at k = 0 (face phase -1: R^2 = 1)."""
        e = self.eps
        Re = Rmat(self.Te, np.zeros(3))
        right = np.cos(e) * np.eye(8) - 1j * np.sin(e) * Re
        a = [sum(1j * d[i] * amp * np.outer(E8[a_], E8[b_]) for a_, b_, amp, d in self.To) for i in range(3)]
        b = [[sum(-d[i] * d[j] / 2 * amp * np.outer(E8[a_], E8[b_]) for a_, b_, amp, d in self.To)
              for j in range(3)] for i in range(3)]
        A = [1j * np.sin(e) * x @ right for x in a]
        B = [[1j * np.sin(e) * x @ right for x in row] for row in b]
        return A, B


E8 = np.eye(8)


def nullspace(M, tol=1e-9):
    """Null space of a stacked system; M is a matrix or a list of row blocks (reduced block by block by QR,
    so memory stays at a few n x n)."""
    blocks = [M] if isinstance(M, np.ndarray) else M  # list or generator of blocks
    R = None
    for Bk in blocks:
        S = Bk if R is None else np.vstack([R, Bk])
        if S.shape[0] < S.shape[1]:
            S = np.vstack([S, np.zeros((S.shape[1] - S.shape[0], S.shape[1]), S.dtype)])
        R = np.linalg.qr(S, mode='r')
    _, s, Vh = np.linalg.svd(R)
    return Vh[s < tol * max(1.0, s[0])].conj()


def commutant(mats):
    n = mats[0].shape[0]
    I = np.eye(n)
    N = nullspace(np.kron(I, X) - np.kron(X.T, I) for X in mats)
    return [v.reshape(n, n, order='F') for v in N]


def transpose_perm(n):
    P = np.zeros((n * n, n * n))
    for a in range(n):
        for b in range(n):
            P[a + n * b, b + n * a] = 1
    return P


def pairings(Uf, Ks, n):
    I = np.eye(n * n)
    N = nullspace([np.kron(Uf(-K), Uf(K)) - I for K in Ks] + [I + transpose_perm(n)])
    return [v.reshape(n, n, order='F') for v in N]


def bdg(A=None, D=None, n=16):
    A = np.zeros((n, n)) if A is None else A
    D = np.zeros((n, n)) if D is None else D
    return np.block([[A, D], [D.conj().T, -A.T]])


def herm_basis(alg):
    out = []
    for X in alg:
        for Y in (X + X.conj().T, 1j * (X - X.conj().T)):
            out.append(Y)
    V = np.array([np.concatenate([y.real.ravel(), y.imag.ravel()]) for y in out]).T
    Q, s, _ = np.linalg.svd(V, full_matrices=False)
    Q = Q[:, s > 1e-9 * s[0]]
    m = int(np.sqrt(V.shape[0] // 2))
    return [(Q[:m * m, k] + 1j * Q[m * m:, k]).reshape(m, m) for k in range(Q.shape[1])]


def lie(gens):
    """Real Lie algebra spanned by hermitian gens (as i*gens): dim, closure, center, derived, rank, ideals."""
    m = gens[0].shape[0]
    V = np.array([np.concatenate([g.real.ravel(), g.imag.ravel()]) for g in gens]).T
    Q, s, _ = np.linalg.svd(V, full_matrices=False)
    Q = Q[:, s > 1e-9 * s[0]]
    B = [(Q[:m * m, k] + 1j * Q[m * m:, k]).reshape(m, m) * 1j for k in range(Q.shape[1])]
    n = len(B)
    co = lambda X: Q.T @ np.concatenate([(-1j * X).real.ravel(), (-1j * X).imag.ravel()])
    ad = np.zeros((n, n, n))
    res = 0.0
    for i in range(n):
        for j in range(n):
            C = B[i] @ B[j] - B[j] @ B[i]
            c = co(C)
            res = max(res, np.linalg.norm(C - sum(c[k] * B[k] for k in range(n))))
            ad[i][:, j] = c
    Mc = [ad[:, :, j].T for j in range(n)]  # rows: sum_i x_i ad_i[:, j]
    centre = len(nullspace(Mc, 1e-8)) if n else 0
    derived = np.linalg.matrix_rank(np.hstack([ad[i] for i in range(n)]), 1e-8)
    x = np.random.randn(n)
    adx = np.tensordot(x, ad, 1)
    rank = n - np.linalg.matrix_rank(adx, 1e-8)
    # simple ideals: eigenspaces of a generic symmetric element of the commutant of ad on [g,g]
    U_, s_, _ = np.linalg.svd(np.hstack([ad[i] for i in range(n)]))
    Dd = U_[:, :derived]
    adD = [Dd.T @ ad[i] @ Dd for i in range(n)]
    I = np.eye(derived)
    if derived == 0:
        return dict(dim=n, closure=res, centre=centre, derived=0, rank=rank, ideals=[])
    Cm = nullspace((np.kron(I, a) - np.kron(a.T, I) for a in adD), 1e-8)
    Y = sum(np.random.randn() * v.reshape(derived, derived, order='F').real for v in Cm)
    w = np.sort(np.linalg.eigvalsh(Y + Y.T))
    ideals, cur = [], 1
    for k in range(1, len(w)):
        if abs(w[k] - w[k - 1]) < 1e-6:
            cur += 1
        else:
            ideals.append(cur)
            cur = 1
    if derived:
        ideals.append(cur)
    return dict(dim=n, closure=res, centre=centre, derived=derived, rank=rank, ideals=sorted(ideals))


def name(L):
    simple = {3: 'su(2)', 8: 'su(3)', 10: 'so(5)', 15: 'su(4)'}
    parts = [simple.get(d, f'?{d}') for d in L['ideals']] + ['u(1)'] * L['centre']
    return '+'.join(parts) if parts else '0'


def randK(n):
    return [np.random.uniform(-np.pi, np.pi, 3) for _ in range(n)]


KS = randK(10)
KS += [-K for K in KS]
KF = randK(5)
STD = Tick(eta_perm((0, 1, 2)))

# ---------------- A. the supplied tick ----------------
print('A. supplied tick: Z^3, two tilings by 2x2x2 cubes offset (1,1,1), face phase -1, eps=0.37, mu=0, no copy mass')
eta0 = eta_perm((0, 1, 2))
fmax = 0.0
for p in itertools.product(range(2), repeat=3):
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        ph = eta0(i, p) * eta0(j, tuple(np.add(p, E3[i]))) * np.conj(eta0(i, tuple(np.add(p, E3[j])))) * np.conj(eta0(j, p))
        fmax = max(fmax, abs(ph + 1))
check('A1 phases multiply to -1 around every unit face (all 24 face classes of the period-2 lattice)', fmax < 1e-12)
r2 = max(np.abs(Rmat(t, K) @ Rmat(t, K) - np.eye(8)).max() for K in KF for t in (STD.Te, STD.To))
check('A2 even and odd cube hops are reflections, R^2 = 1 (Bloch form, generic K)', r2 < 1e-12, f'{r2:.1e}')
un = max(np.abs(STD.U(K) @ STD.U(K).conj().T - np.eye(8)).max() for K in KF)
check('A3 one-layer tick U(K) unitary', un < 1e-12)
w0 = np.angle(np.linalg.eigvals(STD.U(np.zeros(3))))
wR = np.sort(np.abs(np.angle(np.linalg.eigvals(STD.U(np.pi * np.ones(3))))))
check('A4 U(0) = 1 (all 8 bands light at K = 0); at K = R = pi(1,1,1) all 8 at |w| = 2 eps',
      np.abs(w0).max() < 1e-12 and np.abs(wR - 2 * 0.37).max() < 1e-10)
degs = []
for K in KF[:3]:
    w = np.angle(np.linalg.eigvals(STD.U(K)))
    degs.append(sorted(np.unique(np.round(w, 8), return_counts=True)[1].tolist()))
check('A5 generic K: two quasi-energies +-w(K), each 4-fold', all(d == [4, 4] for d in degs), str(degs[0]))

# ---------------- B. exact commutant ----------------
print('B. exact K-independent cell-local commutant')
U2 = lambda K, t=STD: np.kron(t.U(K), np.eye(2))
c1 = [len(commutant([STD.U(K)])), len(commutant([STD.U(np.zeros(3))])), len(commutant([STD.U(np.pi * np.ones(3))]))]
print(f'   single-K commutant dims, one layer (generic, K=0, K=R): {c1}; two layers: {[4 * c for c in c1]}')
check('B1 a single momentum fixes nothing: dims 32 / 64 / 32 are band degeneracies (U(0) = 1)', c1 == [32, 64, 32])
stab = [len(commutant([STD.U(K) for K in KS[:n]])) for n in (1, 2, 3, 4, 5, 6, 10)]
print(f'   one-layer intersection dims for nK = 1,2,3,4,5,6,10: {stab}')
A1 = commutant([STD.U(K) for K in KS])
check('B2 one layer: K-independent commutant = scalars (dim 1); corner parity eps is NOT in it',
      len(A1) == 1 and np.abs(EPSC @ STD.U(KF[0]) - STD.U(KF[0]) @ EPSC).max() > 0.1)
A2 = commutant([U2(K) for K in KS])
known = [np.kron(E8, Y) for Y in [np.eye(2), np.array([[0, 1], [1, 0]]), np.diag([1., -1]), np.array([[0, -1j], [1j, 0]])]]
kc = max(np.abs(X @ U2(K) - U2(K) @ X).max() for X in known for K in KF)
check('B3 two layers: number-conserving commutant = 1_8 x M_2(C) (dim 4, layer U(2))',
      len(A2) == 4 and kc < 1e-12, f'dim {len(A2)}')
D2 = pairings(U2, KS, 16)
D1 = pairings(STD.U, KS, 8)
Dt = np.kron(EPSC, ISY)
ov = abs(np.vdot(Dt, D2[0])) / np.linalg.norm(Dt) / np.linalg.norm(D2[0]) if D2 else 0
check('B4 pairing commutant: none for one layer; exactly one for two layers, Delta = eps x i sigma_y '
      '(staggered on-site layer-singlet pair)', len(D1) == 0 and len(D2) == 1 and abs(ov - 1) < 1e-9)
gens = [bdg(A=h) for h in herm_basis(A2)] + [bdg(D=D2[0]), bdg(D=1j * D2[0])]
W = lambda K: np.block([[U2(K).conj().T, np.zeros((16, 16))], [np.zeros((16, 16)), U2(-K).T]])
err = max(np.abs(g @ W(K) - W(K) @ g).max() for g in gens for K in KF)
check('B5 all 6 BdG generators commute with the Nambu tick at 5 fresh K', err < 1e-10, f'{err:.1e}')
L = lie(gens)
print(f'   exact algebra: dim {L["dim"]}, centre {L["centre"]}, derived {L["derived"]}, rank {L["rank"]}, '
      f'simple ideals {L["ideals"]} -> {name(L)}')
check('B6 exact internal Lie algebra = su(2)_layer + su(2)_pair = so(4) (dim 6, rank 2, no centre); '
      'fermion number is the Cartan of su(2)_pair', L['dim'] == 6 and L['ideals'] == [3, 3] and L['centre'] == 0
      and L['rank'] == 2 and L['closure'] < 1e-10)
check('B7 no su(4) inside: dim 6 < 15 and every simple ideal is su(2)', L['dim'] < 15)
# site Fock content under so(4): 4 states = (2,1) + (1,2)
cd = lambda k: np.kron(np.kron(np.eye(2 ** k), np.array([[0, 0], [1, 0]])), np.eye(2 ** (1 - k)))
Z = np.diag([1, -1])
c1d, c2d = cd(0), np.kron(Z, np.array([[0, 0], [1, 0]]))
Sl = [c1d @ c2d.conj().T + c2d @ c1d.conj().T, (c1d.conj().T @ c1d - c2d.conj().T @ c2d)]
Sp = [c1d @ c2d + (c1d @ c2d).conj().T, (c1d.conj().T @ c1d + c2d.conj().T @ c2d) - np.eye(4)]
casL = sum(np.linalg.matrix_power(X, 2) for X in Sl)
casP = sum(np.linalg.matrix_power(X, 2) for X in Sp)
P_even = np.diag([1, 0, 0, 1.]); P_odd = np.eye(4) - P_even
check('B8 one site (two modes, 4 states): odd sector = layer doublet, even sector = pair doublet, '
      'i.e. (2,1)+(1,2) of so(4); site parity grades the two spinors',
      np.abs(P_even @ casL).max() < 1e-12 and np.abs(P_odd @ casP).max() < 1e-12
      and np.trace(P_odd @ casL) > 0 and np.trace(P_even @ casP) > 0)

# ---------------- C. corner labels ----------------
print('C. corner-label operators X x 1_layer, exact and at the Dirac point')
check('C1 exact: the only corner-label operator commuting with the tick is X = 1 (no su(n), n >= 2, on corners)',
      len(A1) == 1)
A, Bt = STD.taylor()
num = max(np.abs(STD.U(1e-6 * E3[i]) - np.eye(8) - 1e-6 * A[i]).max() for i in range(3))
check('C2 Taylor coefficients of U at K = 0 match finite differences', num < 1e-10, f'{num:.1e}')
E1 = commutant(A)
E2c = commutant(A + [Bt[i][j] + Bt[j][i] for i in range(3) for j in range(3)])
g5 = A[0] @ A[1] @ A[2]
g5 = g5 / np.sqrt(abs(np.trace(g5 @ g5) / 8))
E1h = [h for h in herm_basis(E1)]
L1 = lie(E1h)
print(f'   one layer, Dirac (first) order: dim {len(E1)} -> {name(L1)}; second order: dim {len(E2c)}')
check('C3 first order at K = 0, one layer: corner algebra = chiral copy u(2)+u(2) (dim 8); largest simple '
      'factor su(2), so no su(4) on corners even emergently', len(E1) == 8 and L1['ideals'] == [3, 3]
      and L1['centre'] == 2)
check('C4 second order breaks it to the exact scalars (dim 1)', len(E2c) == 1)
cen = commutant(A + E1)  # centre of the first-order algebra
Gam = [X - np.trace(X) / 8 * np.eye(8) for X in herm_basis(cen)]
Gam = max(Gam, key=np.linalg.norm)
Gam = Gam / np.sqrt(abs(np.trace(Gam @ Gam)) / 8)
gok = np.abs(Gam @ Gam - np.eye(8)).max() < 1e-9 and abs(np.trace(Gam)) < 1e-9
gdiag = np.abs(Gam - np.diag(np.diag(Gam))).max()
check('C5 first-order centre = span{1, Gamma}, Gamma a traceless involution (emergent chirality); '
      'Gamma is not a corner-label diagonal (corner parity eps does not commute with the Dirac terms)',
      len(cen) == 2 and gok and gdiag > 0.1 and max(np.abs(EPSC @ a - a @ EPSC).max() for a in A) > 0.1)
# two layers, Dirac order
A2t = [np.kron(a, np.eye(2)) for a in A]
E1two = commutant(A2t)
L1two = lie(herm_basis(E1two))
print(f'   two layers, Dirac order: dim {len(E1two)} -> {name(L1two)} (acts on copy x layer)')
check('C6 two layers, first order: u(4)+u(4) (dim 32) on copy x layer; this su(4) is emergent and needs the '
      'layer bit, not the three axes', len(E1two) == 32 and L1two['ideals'] == [15, 15])
E2two = commutant(A2t + [np.kron(Bt[i][j] + Bt[j][i], np.eye(2)) for i in range(3) for j in range(3)])
check('C7 two layers, second order: back to the exact layer M_2 (dim 4)', len(E2two) == 4)

# rotations: find S_g = G P_g with S U(K) S^-1 = U(gK + delta)
print('C8-. lattice rotations about an even-cube centre (with site gauge and possible K shift)')
def rot_op(g, tick):
    t = (1 - g @ np.ones(3, dtype=int)) // 2
    def P(K):
        M = np.zeros((8, 8), complex)
        gK = g @ K
        for c in CORN:
            v = g @ np.array(c) + t
            M[IDX[tuple(v % 2)], IDX[c]] = np.exp(1j * np.dot(gK, v // 2))
        return M
    for dl in itertools.product([0, np.pi], repeat=3):
        rows = []
        for K in KS[:6]:
            Am = P(K) @ tick.U(K) @ P(K).conj().T
            Bm = tick.U(g @ K + np.array(dl))
            for a in range(8):
                for b in range(8):
                    r = np.zeros(8, complex)
                    r[a] += Am[a, b]
                    r[b] -= Bm[a, b]
                    rows.append(r)
        N = nullspace(np.array(rows))
        if len(N):
            G = np.diag(N[0] / N[0][np.argmax(abs(N[0]))])
            G = G / np.abs(np.diag(G)).max()
            return np.array(dl), (lambda K, G=G: G @ P(K))
    return None, None

g4 = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
g3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
rots = {}
for nm, g in [('C4z', g4), ('C3', g3)]:
    dl, S = rot_op(g, STD)
    ok = S is not None and max(np.abs(S(K) @ STD.U(K) @ S(K).conj().T - STD.U(g @ K + dl)).max() for K in KF) < 1e-10 \
        and max(np.abs(S(K) @ S(K).conj().T - np.eye(8)).max() for K in KF) < 1e-10
    check(f'C8 {nm} is a symmetry with a cell-periodic site gauge, K -> gK + {[int(x) for x in np.round(dl / np.pi)]} pi', ok)
    rots[nm] = (dl, S)
both0 = all(np.abs(rots[k][0]).max() == 0 for k in rots)
check('C9 rotations fix K = 0, so they act on the light corner states there', both0)
S0 = [rots[k][1](np.zeros(3)) for k in rots]
rcom1 = commutant(A + S0)
rcom2 = commutant(A2t + [np.kron(s, np.eye(2)) for s in S0])
Lr = lie(herm_basis(rcom2))
print(f'   Dirac-order algebra commuting with C4z, C3: one layer dim {len(rcom1)}, two layers dim {len(rcom2)} -> {name(Lr)}')
gin = abs(np.linalg.matrix_rank(np.array([X.ravel() for X in rcom1] + [Gam.ravel()]), 1e-8) - 2) == 0
check('C10 rotations act on the copy factor: one layer keeps only span{1, Gamma} (dim 2); two layers keep '
      'u(2)+u(2) = layer x {1, Gamma} (dim 8): no su(4) commutes with tick and rotations',
      len(rcom1) == 2 and gin and len(rcom2) == 8 and 15 not in Lr['ideals'])

# ---------------- D. hop-phase choices and controls ----------------
print('D. other hop-phase choices with product -1 on every face; controls')
res = []
for perm in itertools.permutations(range(3)):
    gauge = {c: np.exp(2j * np.pi * np.random.rand()) for c in CORN}
    t = Tick(eta_perm(perm, gauge))
    u2 = lambda K, t=t: np.kron(t.U(K), np.eye(2))
    res.append((len(commutant([t.U(K) for K in KS])), len(commutant([u2(K) for K in KS])), len(pairings(u2, KS, 16))))
check('D1 all 6 axis orders x random cell-periodic site gauges: (1, 4, 1) = scalars, layer U(2), one pairing',
      all(r == (1, 4, 1) for r in res), str(res[0]))
q = np.random.uniform(-np.pi, np.pi, 3)
tq = Tick(eta_perm((0, 1, 2), q=q))
u2q = lambda K: np.kron(tq.U(K), np.eye(2))
nq = len(commutant([u2q(K) for K in KS]))
pq = len(pairings(u2q, KS, 16))
# e^{iq} per hop = site gauge e^{i q.p}, p = 2R + c: cell part diag(e^{i q.c}) and a K shift by 2q
err_q = 1e9
for sg in (1, -1):
    Gc = np.kron(np.diag([np.exp(sg * 1j * np.dot(q, c)) for c in CORN]), np.eye(2))
    Dq = Gc @ Dt @ Gc.T
    for st in (4, -4):
        err_q = min(err_q, max(np.abs(u2q(K) @ Dq @ u2q(-K + st * q).T - Dq).max() for K in KF))
check('D2 uniform complex phases e^{iq_i} (face product still -1): layer U(2) kept; the pair is conserved '
      'at total cell momentum 4q (a site-gauge image), so the algebra is still so(4)', nq == 4 and pq == 0
      and err_q < 1e-10, f'{err_q:.1e}')
tm = Tick(eta0, mu=0.2)
um = lambda K: np.kron(tm.U(K), np.eye(2))
check('D3 control, copy-free mass angle mu = 0.2: (1, 4, pairings %d)' % len(pairings(um, KS, 16)),
      len(commutant([tm.U(K) for K in KS])) == 1 and len(commutant([um(K) for K in KS])) == 4)
t0 = Tick(lambda i, p: 1.0)
u20 = lambda K: np.kron(t0.U(K), np.eye(2))
z1, z2, zp = len(commutant([t0.U(K) for K in KS])), len(commutant([u20(K) for K in KS])), len(pairings(u20, KS, 16))
check('D4 control, face product +1 (R not a reflection): (%d, %d, %d); no su(4) either' % (z1, z2, zp),
      z2 < 15)
for e in (0.11, 1.2):
    te = Tick(eta0, eps=e)
    ue = lambda K, te=te: np.kron(te.U(K), np.eye(2))
    check(f'D5 step eps = {e}: same (4 number-conserving, 1 pairing)', len(commutant([ue(K) for K in KS])) == 4
          and len(pairings(ue, KS, 16)) == 1)

tp = Tick(eta0, eps=np.pi / 2)
up = lambda K: np.kron(tp.U(K), np.eye(2))
n1p = commutant([tp.U(K) for K in KS])
n2p, p2p = commutant([up(K) for K in KS]), pairings(up, KS, 16)
Lp = lie([bdg(A=h) for h in herm_basis(n2p)] + [bdg(D=d) for d in p2p] + [bdg(D=1j * d) for d in p2p])
print(f'   step pi/2 (U = R_o R_e): one layer dim {len(n1p)}, two layers {len(n2p)} + {len(p2p)} pairings -> {name(Lp)}')
check('D6 only at the special step eps = pi/2 does corner parity eps join (one layer span{1, eps}, as in the '
      'block-tick note); still no su(4) and the corner algebra is abelian', len(n1p) == 2 and
      np.abs(EPSC @ tp.U(KF[0]) - tp.U(KF[0]) @ EPSC).max() < 1e-12 and 15 not in Lp['ideals'])
print('E. N identical layers (N modes per site): the internal algebra comes from the layer count, not the corners')
dimsN = {}
for N in (1, 3):
    uN = lambda K, N=N: np.kron(STD.U(K), np.eye(N))
    KN = KS[:6] + [-K for K in KS[:6]]
    aN, pN = commutant([uN(K) for K in KN]), pairings(uN, KN, 8 * N)
    gN = [bdg(A=h, n=8 * N) for h in herm_basis(aN)] + [bdg(D=d, n=8 * N) for d in pN] + \
         [bdg(D=1j * d, n=8 * N) for d in pN]
    LN = lie(gN)
    dimsN[N] = (len(aN), len(pN), LN['dim'], LN['ideals'], LN['centre'])
    print(f'   N = {N}: number-conserving {len(aN)}, pairings {len(pN)}, algebra dim {LN["dim"]} -> {name(LN)}')
check('E1 N = 1: u(1); N = 2: so(4) (B6); N = 3: 1_8 x M_3 plus eps x (antisym 3x3) = so(6) = su(4), simple, '
      'dim 15: an exact su(4) appears only by supplying three layers, acting on the layer index',
      dimsN[1][:3] == (1, 0, 1) and dimsN[3][:4] == (9, 3, 15, [15]))
print('VERDICT: exact internal algebra of the free two-layer tick = so(4) = su(2)_layer + su(2)_pair; '
      'no su(4) on corner labels (exact or at the Dirac point); Ruleset C as stated (C1+C2) is dead; an exact su(4) needs N = 3 layers (so(2N)), i.e. a supplied count.')
print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
