"""B26 checker: own construction of the 12-mode corner model (no import of any repo / campaign code).

Modes |v, c>, v in Z^3, c = {d, e} a perpendicular pair of unit directions (12 corners).
Edges: on-site {a,b}@v -- {a,f}@v (f perpendicular to a and b); link {a,b}@v -- {-a,b}@v+a.
Z2 fluxes: square (4 corners sharing one direction) = pi, octant triangle = 0, cube face plaquette = pi,
tube (2 links + 2 on-site edges around one link direction) = pi.  Translation-invariant gauge on the 36 edge types
(own GF(2) solver).  Gauge-dressed rotations G_R |v,c> = (-1)^{lam_R.v + tau_R(c)} |R v, R c> (own GF(2) solve).
Translation-invariant operators: dict a -> 12x12 block X_a (X|v,c> = sum_a |v+a> X_a|c>), Bloch X(k) = sum_a X_a e^{i k.a}.
Conjugation: (G X G^-1)_{R a} = (-1)^{lam.a} U_R X_a U_R^T,  U_R|c> = (-1)^{tau(c)} |R c>.
"""
import itertools
import numpy as np

DIRS = [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]
def dot(a, b): return sum(x*y for x, y in zip(a, b))
def neg(a): return tuple(-x for x in a)
def add(a, b): return tuple(x+y for x, y in zip(a, b))
CORN = sorted({frozenset((d, e)) for d in DIRS for e in DIRS if dot(d, e) == 0},
              key=lambda c: tuple(-x for x in add(*tuple(c))))
assert len(CORN) == 12
CI = {c: i for i, c in enumerate(CORN)}
FACE = np.array([add(*tuple(c)) for c in CORN])
ANTI = [CI[frozenset(neg(x) for x in c)] for c in CORN]
Z0 = (0, 0, 0)
def other(c, x): return [y for y in c if y != x][0]
def perp2(a, b): return [f for f in DIRS if dot(f, a) == 0 and dot(f, b) == 0]

# ---- edge types (canonical key: (i, j, shift) with the smaller of the two orientations)
def ekey(c1, c2, s):
    a = (CI[c1], CI[c2], tuple(s)); b = (CI[c2], CI[c1], neg(s)); return min(a, b)
ET = {}; ONSITE = []; LINK = []
for c in CORN:
    for x in c:
        y = other(c, x)
        for f in perp2(x, y):
            k = ekey(c, frozenset((x, f)), Z0)
            if k not in ET: ET[k] = len(ET); ONSITE.append(k)
        k = ekey(c, frozenset((neg(x), y)), x)
        if k not in ET: ET[k] = len(ET); LINK.append(k)
NT = len(ET); assert NT == 36 and len(ONSITE) == 24 and len(LINK) == 12

def gf2_solve(A, b):
    A = np.array(A, np.uint8) % 2; b = np.array(b, np.uint8) % 2
    m, n = A.shape; M = np.concatenate([A, b[:, None]], 1); piv = []; r = 0
    for col in range(n):
        nz = [i for i in range(r, m) if M[i, col]]
        if not nz: continue
        M[[r, nz[0]]] = M[[nz[0], r]]
        for i in range(m):
            if i != r and M[i, col]: M[i] ^= M[r]
        piv.append(col); r += 1
        if r == m: break
    if M[r:, n].any(): return None, r, None
    x = np.zeros(n, np.uint8)
    for i, col in enumerate(piv): x[col] = M[i, n]
    free = [j for j in range(n) if j not in piv]
    kern = []
    for f in free:
        v = np.zeros(n, np.uint8); v[f] = 1
        for i, col in enumerate(piv): v[col] = M[i, f]
        kern.append(v)
    return x, r, kern

def loop_row(seq):
    row = np.zeros(NT, np.uint8)
    for (c1, p1), (c2, p2) in zip(seq, seq[1:] + seq[:1]):
        row[ET[ekey(c1, c2, tuple(y - x for x, y in zip(p1, p2)))]] ^= 1
    return row
def ring(d):
    a0 = [f for f in DIRS if dot(f, d) == 0][0]; b0 = [f for f in DIRS if dot(f, d) == 0 and dot(f, a0) == 0][0]
    return [a0, b0, neg(a0), neg(b0)]
LOOPS = []   # (row, flux)
for d in DIRS:
    rg = ring(d)
    LOOPS.append((loop_row([(frozenset((d, r)), Z0) for r in rg]), 1))                 # square
    for i in range(4):
        p, q = rg[i], rg[(i + 1) % 4]
        LOOPS.append((loop_row([(frozenset((d, p)), Z0), (frozenset((neg(d), p)), d),
                                (frozenset((neg(d), q)), d), (frozenset((d, q)), Z0)]), 1))  # tube
for s in itertools.product((1, -1), repeat=3):
    x, y, z = (s[0],0,0), (0,s[1],0), (0,0,s[2])
    LOOPS.append((loop_row([(frozenset((x, y)), Z0), (frozenset((y, z)), Z0), (frozenset((z, x)), Z0)]), 0))  # triangle
for d in DIRS:
    for e in DIRS:
        if dot(d, e) != 0: continue
        LOOPS.append((loop_row([(frozenset((d, e)), Z0), (frozenset((neg(d), e)), d),
                                (frozenset((neg(d), neg(e))), add(d, e)), (frozenset((d, neg(e))), e)]), 1))  # plaquette
u, LOOP_RANK, _ = gf2_solve([r for r, _ in LOOPS], [f for _, f in LOOPS])
assert u is not None

# ---- rotations
def all_oh():
    out = []
    for p in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), int)
            for i in range(3): M[i, p[i]] = sg[i]
            out.append(M)
    return out
OH = all_oh(); ROT = [M for M in OH if round(np.linalg.det(M)) == 1]; assert len(ROT) == 24
def rd(M, d): return tuple(int(x) for x in M @ np.array(d))
def rc(M, c): return frozenset(rd(M, d) for d in c)
def chiA2(M):   # A2 of O = sign of the underlying permutation of axes (for proper rotations)
    p = [int(np.nonzero(M[i])[0][0]) for i in range(3)]
    return (-1) ** sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])

def psg(M):
    """(lam, tau) with u_e + u_{Me} = tau(c1) + tau(c2) + lam.s for all 36 edge types; returns solution and kernel dim."""
    A = []; b = []
    for (i1, i2, s), t in ET.items():
        row = np.zeros(15, np.uint8); row[:3] = np.array(s) % 2; row[3 + i1] ^= 1; row[3 + i2] ^= 1
        A.append(row); b.append(u[t] ^ u[ET[ekey(rc(M, CORN[i1]), rc(M, CORN[i2]), rd(M, s))]])
    x, r, kern = gf2_solve(A, b)
    return x, kern
PSG = []
for M in OH:
    x, kern = psg(M); assert x is not None
    PSG.append(dict(M=M, lam=x[:3].astype(int), tau=x[3:].astype(int), kdim=len(kern), kern=kern))
def Umat(g):
    U = np.zeros((12, 12))
    for c in CORN: U[CI[rc(g['M'], c)], CI[c]] = (-1.0) ** g['tau'][CI[c]]
    return U
for g in PSG: g['U'] = Umat(g); g['chi'] = chiA2(g['M']) if round(np.linalg.det(g['M'])) == 1 else None
PROPER = [g for g in PSG if round(np.linalg.det(g['M'])) == 1]

def conjG(g, X):
    """G X G^-1 for a block dict X."""
    Y = {}
    for a, B in X.items():
        Y[rd(g['M'], a)] = (-1.0) ** int(np.dot(g['lam'], a)) * g['U'] @ B @ g['U'].T
    return Y
def bl_eq(X, Y, s=1.0, tol=1e-10):
    keys = set(X) | set(Y)
    return all(np.abs(X.get(a, 0) - s * Y.get(a, 0)).max() < tol if (a in X or a in Y) else True for a in keys)
def bloch(X, k):
    k = np.asarray(k, float); out = np.zeros((12, 12), complex)
    for a, B in X.items(): out += B * np.exp(1j * np.dot(k, a))
    return out
def bloch_grad(X, k):
    k = np.asarray(k, float)
    return [sum(B * 1j * a[j] * np.exp(1j * np.dot(k, a)) for a, B in X.items()) for j in range(3)]
def mul(X, Y):
    Z = {}
    for a, A in X.items():
        for b, B in Y.items():
            c = add(a, b); Z[c] = Z.get(c, 0) + A @ B
    return {a: B for a, B in Z.items() if np.abs(B).max() > 1e-13}
def dag(X): return {neg(a): B.conj().T for a, B in X.items()}

# ---- Hamiltonian pieces in B18 sign convention (-t (-1)^u)
def ham(kind):
    X = {}
    for (i1, i2, s) in (ONSITE if kind == 'on' else LINK):
        amp = -(-1.0) ** u[ET[(i1, i2, s)]]
        X.setdefault(s, np.zeros((12, 12), complex))[i2, i1] += amp       # |v+s, c2><v, c1|
        X.setdefault(neg(s), np.zeros((12, 12), complex))[i1, i2] += amp
    return X
HON = ham('on'); HLINK = ham('link')
RL = {a: B / np.sqrt(2) for a, B in HLINK.items()}
LAM = np.zeros((12, 12), complex)
for sg in itertools.product((1, -1), repeat=3):
    x, y, z = (sg[0],0,0), (0,sg[1],0), (0,0,sg[2])
    cy = [frozenset((x, y)), frozenset((y, z)), frozenset((z, x))]
    if round(np.linalg.det(np.array([x, y, z]))) < 0: cy = cy[::-1]
    for a_ in range(3):
        q, r = cy[a_], cy[(a_ + 1) % 3]
        amp = 1j * (-1.0) ** u[ET[ekey(q, r, Z0)]]
        LAM[CI[r], CI[q]] += amp; LAM[CI[q], CI[r]] += np.conj(amp)
LAMX = {Z0: LAM}

# ---- S: |v,c> -> s_c |v + f_c, c>, s solved by orbit propagation from s_{c0} = +1
def orbit_solve(target_of, chi_fn, c0=0):
    """Generic monomial-letter construction: column c maps to target_of(c) = (row corner index, displacement)
    with coefficient z_c; solve z_{Rc} from z_c using covariance G X G^-1 = chi X.  Returns block dict or None."""
    z = {c0: 1.0 + 0j}; changed = True
    while changed:
        changed = False
        for g in PROPER:
            for c in list(z):
                i, a = target_of(c); Rc = CI[rc(g['M'], CORN[c])]
                # image of entry (i <- c, disp a): (Ri <- Rc, disp Ra) with sign (-1)^{lam.a + tau(c) + tau(i)}
                val = (-1.0) ** (int(np.dot(g['lam'], a)) + g['tau'][c] + g['tau'][i]) * z[c] / chi_fn(g)
                i2, a2 = target_of(Rc)
                if (CI[rc(g['M'], CORN[i])], rd(g['M'], a)) != (i2, a2): return None   # support not equivariant
                if Rc in z:
                    if abs(z[Rc] - val) > 1e-12: return None
                else: z[Rc] = val; changed = True
    X = {}
    for c, zc in z.items():
        i, a = target_of(c); X.setdefault(a, np.zeros((12, 12), complex))[i, c] += zc
    return X
c_xy = CI[frozenset(((1,0,0), (0,1,0)))]
S1 = orbit_solve(lambda c: (c, tuple(FACE[c])), lambda g: 1, c0=c_xy)
A0 = orbit_solve(lambda c: (ANTI[c], Z0), lambda g: g['chi'], c0=c_xy)
def Spow(p):
    return {tuple(p * FACE[c]): np.diag([(S1[tuple(FACE[c])][c, c]) ** p if j == c else 0 for j in range(12)]) for c in range(12)} if p else {Z0: np.eye(12, dtype=complex)}
def Spow(p):
    X = {}
    for c in range(12):
        a = tuple(int(x) for x in p * FACE[c]); B = X.setdefault(a, np.zeros((12, 12), complex))
        B[c, c] = S1[tuple(FACE[c])][c, c] ** p
    return X
def Sk(k, p=1):
    s = np.array([S1[tuple(FACE[c])][c, c] for c in range(12)])
    return np.diag(s ** p * np.exp(1j * p * FACE @ np.asarray(k, float)))
A0m = A0[Z0]
RTX = mul(mul({Z0: A0m}, RL), {Z0: A0m.conj().T})

# ---- eigen-projectors of the on-site pieces (ascending eigenvalue)
def eproj(M):
    w, V = np.linalg.eigh(M); ls = sorted(set(np.round(w, 6)))
    return ls, [V[:, np.abs(w - l) < 1e-6] @ V[:, np.abs(w - l) < 1e-6].conj().T for l in ls]
HON0 = bloch(HON, np.zeros(3))
HEV, PH = eproj(HON0); LEV, PL = eproj(LAM)
PHASE = [1, 1j, -1, -1j]
def onH(a, b): return PH[0] + PHASE[a] * PH[1] + PHASE[b] * PH[2]
def onL(a, b, c): return PL[0] + PHASE[a] * PL[1] + PHASE[b] * PL[2] + PHASE[c] * PL[3]
PC = {f"H{a}{b}": onH(a, b) for a in range(4) for b in range(4)}
PC.update({f"L{a}{b}{c}": onL(a, b, c) for a in range(4) for b in range(4) for c in range(4)})
def eigsp(M, lam):
    w, V = np.linalg.eigh(M); return V[:, np.abs(w - lam) < 1e-6]
DPM = eigsp(HON0, 2.0)
DP = DPM @ eigsp(DPM.conj().T @ LAM @ DPM, -2 * np.sqrt(2))
DM = DPM @ eigsp(DPM.conj().T @ LAM @ DPM, 2 * np.sqrt(2))

# ---- symmetric on-site algebra (commutant of all U_R, proper rotations)
def onsite_algebra():
    rows = []
    for g in PROPER:
        U = g['U']
        rows.append(np.kron(U, U) - np.eye(144))          # vec(U B U^T) = (U kron U) vec(B) (row-major)
    A = np.vstack(rows); _, sv, Vh = np.linalg.svd(A)
    return [v.reshape(12, 12) for v in Vh[np.sum(sv > 1e-9):].conj()]
ONB = onsite_algebra()
def rand_onsite_unitary(rng):
    H = sum(rng.normal() * B + rng.normal() * 1j * B for B in ONB); H = (H + H.conj().T) / 2
    w, V = np.linalg.eigh(H); return V @ np.diag(np.exp(1j * w * 3.0)) @ V.conj().T

def wrap(x): return np.angle(np.exp(1j * np.asarray(x)))
