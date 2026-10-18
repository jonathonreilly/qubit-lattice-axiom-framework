"""COL-1 check 4: floating-token SU(3) structure WITH LINKS and a Gauss law on Z^1 (one qubit per site).

Token at z (19 qubits), offsets:
  0,1,2 : 1 1 0                marker
  3-5   : q   quark colour (one-hot) or empty       -> 3   of SU(3)_z
  6     : 0
  7-9   : p   antiquark colour (one-hot) or empty   -> 3bar of SU(3)_z     (q,p: at most one present)
  10    : 0
  11-13 : A   colour of the z-end of link z->z+19   -> 3bar of SU(3)_z
  14    : 0
  15-17 : B   colour of the far end of that link    -> 3   of SU(3)_{z+19}  (A,B: both empty or both one-hot)
  18    : 0
V(z) = token pattern valid at z.   Pi_x = V(x) AND V(x-19).
G_x^a = Pi_x [ T(q_x) + Tbar(p_x) + Tbar(A_x) + T(B_{x-19}) ] Pi_x      (gauge point at every site x)
H = sum over links  { m [q or p present] + e [link occupied]  +  w (K_x + K_x^dag) },
K_x = Pi_{x+19} [q_x,p_x,A_x,B_x,q_{x+19},p_{x+19} empty] -> sum_{a,b} |q_x=a, A_x=a, B_x=b, p_{x+19}=b>
       (creates quark at x, flux x->x+19, antiquark at x+19; both ends colour singlets).
"""
import sys, itertools, numpy as np, scipy.sparse as sp
from su3common import T, Tbar, F
from parse_lemma import satisfiable, colour_blind, onehot_or_empty

TOK = 19
OFF = dict(q=3, p=7, A=11, B=15)
REP = dict(q=T, p=Tbar, A=Tbar, B=T)

# ---------- predicates as constraint lists (positions are integers) ----------
def V(z):
    cons = [((z, z + 1, z + 2), {(1, 1, 0)})]
    m = set()
    for q in onehot_or_empty(3):
        for p in onehot_or_empty(3):
            if sum(q) + sum(p) <= 1:
                m.add(q + (0,) + p + (0,))
    cons.append((tuple(range(z + 3, z + 11)), m))
    l = set()
    for A in onehot_or_empty(3):
        for B in onehot_or_empty(3):
            if sum(A) == sum(B):
                l.add(A + (0,) + B + (0,))
    cons.append((tuple(range(z + 11, z + 19)), l))
    return cons

def Pi(x):
    return V(x) + V(x - TOK)

def groups(x):
    """register groups acted on by G_x, with their rep"""
    return [(tuple(range(x + OFF['q'], x + OFF['q'] + 3)), 'q'),
            (tuple(range(x + OFF['p'], x + OFF['p'] + 3)), 'p'),
            (tuple(range(x + OFF['A'], x + OFF['A'] + 3)), 'A'),
            (tuple(range(x - TOK + OFF['B'], x - TOK + OFF['B'] + 3)), 'B')]

def support(x):
    s = set()
    for pos, _ in Pi(x):
        s.update(pos)
    return s

print("=== (i) parse lemma, exact, all relative offsets with overlapping supports")
S0 = support(0)
compatible, bad_blind = [], []
for d in range(-2 * TOK - 2, 2 * TOK + 3):
    if d == 0:
        continue
    if not (S0 & support(d)):
        continue
    if satisfiable(Pi(0) + Pi(d)):
        compatible.append(d)
        # P2: Pi_d blind to G_0's moves and Pi_0 blind to G_d's moves
        for g, _ in groups(0):
            if not colour_blind(g, Pi(d)):
                bad_blind.append((d, 'Pi_d vs G_0', g))
        for g, _ in groups(d):
            if not colour_blind(g, Pi(0)):
                bad_blind.append((d, 'Pi_0 vs G_d', g))
own = [g for g, _ in groups(0) if not colour_blind(g, Pi(0))]
shared = [(d, set(sum([list(g) for g, _ in groups(0)], [])) & set(sum([list(g) for g, _ in groups(d)], [])))
          for d in compatible]
print("  support size of G_x: %d qubits; overlapping offsets with jointly satisfiable Pi: %s" % (len(S0), compatible))
print("  P2 failures (must be none): %s; own-register blindness failures: %s" % (bad_blind, own))
print("  qubits acted on (quantumly) by both G_0 and G_d for compatible d: %s" % [(d, sorted(s)) for d, s in shared])

# ---------- (ii) bit-level operators on the constrained subspace of a ring with 2 tokens, all offsets ----------
sys.stdout.flush()
L = 2 * TOK
def token_bits(q, p, A, B):
    return [1, 1, 0] + list(q) + [0] + list(p) + [0] + list(A) + [0] + list(B) + [0]

mat_states = [(q, p) for q in onehot_or_empty(3) for p in onehot_or_empty(3) if sum(q) + sum(p) <= 1]
lnk_states = [(A, B) for A in onehot_or_empty(3) for B in onehot_or_empty(3) if sum(A) == sum(B)]
basis = []
for off in range(TOK):
    for (q1, p1), (A1, B1), (q2, p2), (A2, B2) in itertools.product(mat_states, lnk_states, mat_states, lnk_states):
        bitsl = token_bits(q1, p1, A1, B1) + token_bits(q2, p2, A2, B2)
        s = 0
        for k, b in enumerate(bitsl):
            if b:
                s |= 1 << ((k + off) % L)
        basis.append(s)
basis = np.array(sorted(set(basis)), dtype=np.int64)
Nb = len(basis)
print("=== (ii) ring L=%d, 2 tokens, all %d offsets: constrained subspace dim %d" % (L, TOK, Nb))
one = np.int64(1)

def B_(k):
    return (basis >> np.int64(k % L)) & 1

def Vvec(z):
    ok = (B_(z) == 1) & (B_(z + 1) == 1) & (B_(z + 2) == 0)
    sq = B_(z + 3) + B_(z + 4) + B_(z + 5); sp_ = B_(z + 7) + B_(z + 8) + B_(z + 9)
    ok &= (sq + sp_ <= 1) & (B_(z + 6) == 0) & (B_(z + 10) == 0)
    sA = B_(z + 11) + B_(z + 12) + B_(z + 13); sB = B_(z + 15) + B_(z + 16) + B_(z + 17)
    ok &= (sA <= 1) & (sA == sB) & (B_(z + 14) == 0) & (B_(z + 18) == 0)
    return ok

Vv = {z: Vvec(z) for z in range(L)}
Piv = {x: Vv[x] & Vv[(x - TOK) % L] for x in range(L)}
lookup = lambda t: np.searchsorted(basis, t)

def in_basis(t):
    i = np.searchsorted(basis, t)
    i = np.minimum(i, Nb - 1)
    return basis[i] == t

leak = [0]
def assemble(rows, cols, vals):
    if not rows:
        return sp.csr_matrix((Nb, Nb), dtype=complex)
    t = np.concatenate(rows); c = np.concatenate(cols); v = np.concatenate(vals)
    ok = in_basis(t)
    leak[0] += int((~ok).sum())
    return sp.csr_matrix((v[ok], (lookup(t[ok]), c[ok])), shape=(Nb, Nb), dtype=complex)

def Gops(x):
    act = np.nonzero(Piv[x])[0]
    out = []
    for a in range(8):
        rows, cols, vals = [], [], []
        for g, kind in groups(x):
            occ = np.stack([B_(k)[act] for k in g], axis=1)
            has = occ.sum(axis=1) == 1
            src = act[has]; j = occ[has].argmax(axis=1)
            M = REP[kind][a]
            for i in range(3):
                amp = M[i, j]
                nz = np.abs(amp) > 0
                pos_j = np.array([g[jj] % L for jj in range(3)])[j[nz]]
                tgt = (basis[src[nz]] & ~(one << pos_j)) | (one << np.int64(g[i] % L))
                rows.append(tgt); cols.append(src[nz]); vals.append(amp[nz])
        out.append(assemble(rows, cols, vals))
    return out

def Kop(x):
    y = x + TOK
    grp = lambda o, base: [base + o + k for k in range(3)]
    gq, gpx, gA, gB = grp(3, x), grp(7, x), grp(11, x), grp(15, x)
    gqy, gpy = grp(3, y), grp(7, y)
    ok = Piv[y % L].copy()
    for g in (gq, gpx, gA, gB, gqy, gpy):
        for k in g:
            ok &= B_(k) == 0
    src = np.nonzero(ok)[0]
    rows, cols, vals = [], [], []
    for a in range(3):
        for b in range(3):
            add = (one << np.int64(gq[a] % L)) | (one << np.int64(gA[a] % L)) | (one << np.int64(gB[b] % L)) | (one << np.int64(gpy[b] % L))
            rows.append(basis[src] | add); cols.append(src); vals.append(np.ones(len(src)))
    return assemble(rows, cols, vals)

def mx(m):
    m = sp.csr_matrix(m)
    return float(np.abs(m.data).max()) if m.nnz else 0.0

G = {x: Gops(x) for x in range(L)}
rel = 0.0
for x in (0, 5):
    for a in range(8):
        for b in range(a + 1, 8):
            lhs = G[x][a] @ G[x][b] - G[x][b] @ G[x][a]
            rhs = sum(1j * F[a, b, c] * G[x][c] for c in range(8) if abs(F[a, b, c]) > 0)
            rel = max(rel, mx(lhs - rhs))
cross = 0.0
for y in range(1, L):
    for a in range(8):
        for b in range(8):
            cross = max(cross, mx(G[0][a] @ G[y][b] - G[y][b] @ G[0][a]))
rot = ((basis << one) | (basis >> np.int64(L - 1))) & ((one << np.int64(L)) - 1)
perm = lookup(rot)
assert np.all(basis[perm] == rot)
Tm = sp.csr_matrix((np.ones(Nb), (perm, np.arange(Nb))), shape=(Nb, Nb))
cov = max(mx(Tm @ G[x][a] @ Tm.T - G[(x + 1) % L][a]) for x in range(L) for a in range(8))
m_, e_, w_ = 0.7, 0.3, 1.0
dm = np.zeros(Nb); de = np.zeros(Nb)
for x in range(L):
    v = Vv[x]
    dm += m_ * v * sum(B_(x + k) for k in (3, 4, 5, 7, 8, 9))
    de += e_ * v * sum(B_(x + k) for k in (11, 12, 13))
K = sum(Kop(x) for x in range(L))
H = sp.diags(dm + de).astype(complex) + w_ * (K + K.conj().T)
gi = max(mx(H @ G[y][a] - G[y][a] @ H) for y in range(L) for a in range(8))
covH = mx(Tm @ H @ Tm.T - H)
print("  su(3) relation err %.1e | max cross commutator over y,a,b %.1e | translation covariance err (all x,a) %.1e" % (rel, cross, cov))
print("  leakage of G/H out of the constrained subspace: %d | max |[H,G_y^a]| %.1e | |T H T^dag - H| %.1e | nnz(K) %d"
      % (leak[0], gi, covH, K.nnz))
offs = np.full(Nb, -1)
for o in range(TOK - 1, -1, -1):
    offs[Vv[o]] = o
o0 = np.nonzero(offs == 0)[0]; on = np.nonzero(offs != 0)[0]
C = sum(g @ g for x in range(L) for g in G[x])
C0 = C[o0][:, o0].toarray(); H0 = H[o0][:, o0].toarray()
print("  offset sectors: %d; offset-0 sector dim %d; H couples different offset sectors: %.1e"
      % (len(set(offs.tolist())), len(o0), mx(H[o0][:, on])))
w, U = np.linalg.eigh(C0)
phys = U[:, w < 1e-9]
Hp = phys.conj().T @ H0 @ phys
ev = np.linalg.eigvalsh(Hp)
print("  Gauss-law physical subspace dim (offset 0): %d ; max |H_phys| %.3f ; spectrum of H on it: %s"
      % (phys.shape[1], np.abs(Hp).max(), np.round(ev, 4).tolist()))
qn = sum(B_(x + k) for x in (0, TOK) for k in (3, 4, 5))[o0]
wq = np.real(np.einsum('ik,i,ik->k', phys.conj(), qn, phys))
print("  max quark number among physical basis vectors: %.3f (states with a quark obey the Gauss law with flux)" % wq.max())
