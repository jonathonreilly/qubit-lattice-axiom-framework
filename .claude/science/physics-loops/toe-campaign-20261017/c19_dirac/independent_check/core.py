"""Independent core for the C19 check (corner fermion, Dirac pair).  Written from the note's text;
graph/gauge ideas follow the C18 check, re-implemented here.

Conventions (mine):
  vertex (n, c), c = sorted pair of perpendicular direction indices (12 per site)
  translation-covariant operator given by blocks m[sh][c2, c1] = coefficient of c^dag_{n+sh,c2} c_{n,c1}
  times a phase e^{i P.n} (P = 0 or Q = (pi,pi,pi)), phase referenced to the SOURCE site n.
  Bloch states |k, a> = N^-1/2 sum_n e^{i k.n} a_c c^dag_{n,c}; then
     h(k)        = sum_sh m[sh] e^{-i k.sh}                      (P = 0, k -> k)
     B_{k->k+Q}  = sum_sh m[sh] e^{-i (k+Q).sh}                  (P = Q)
  Unitary symmetry g: c_{n,c} -> sigma_g(n,c) c_{g n, g c}, sigma = eta(c) (-1)^{s.n};
  operator matrix A[i,j] -> A'[g i, g j] = sigma_i sigma_j A[i,j].
"""
import itertools
import numpy as np

DV = [np.array(v) for v in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))]
def didx(v):
    v = tuple(int(round(x)) for x in v)
    for i, w in enumerate(DV):
        if tuple(w) == v: return i
    raise KeyError(v)
CORN = [(i, j) for i, j in itertools.combinations(range(6), 2) if DV[i] @ DV[j] == 0]
CI = {c: k for k, c in enumerate(CORN)}
def cn(i, j): return CI[tuple(sorted((i, j)))]
NEG = [1, 0, 3, 2, 5, 4]

def nb(c):
    """graph neighbours of (0,c): (c2, shift, kind)"""
    i, j = CORN[c]; out = []
    for a, b in ((i, j), (j, i)):
        for f in range(6):
            if f not in (a, b, NEG[a], NEG[b]):
                out.append((cn(a, f), (0, 0, 0), 'o'))
        out.append((cn(NEG[a], b), tuple(DV[a]), 'l'))
    return out

ET = []; EK = {}
for c in range(12):
    for c2, sh, kd in nb(c):
        if (c, c2, sh) in EK: continue
        EK[(c, c2, sh)] = EK[(c2, c, tuple(-x for x in sh))] = len(ET); ET.append((c, c2, sh, kd))
NT = len(ET); assert NT == 36

def etype(v1, v2):
    (n1, c1), (n2, c2) = v1, v2
    return EK[(c1, c2, tuple(b - a for a, b in zip(n1, n2)))]

# ---------- cycles (brute force 3- and 4-cycles through cell 0), classified
def cycles():
    found = {}
    for c0 in range(12):
        st = ((0, 0, 0), c0); stack = [[st]]
        while stack:
            p = stack.pop()
            n, c = p[-1]
            for c2, sh, _ in nb(c):
                w = (tuple(a + b for a, b in zip(n, sh)), c2)
                if w == st and len(p) >= 3:
                    key = frozenset(frozenset((p[i], p[(i+1) % len(p)])) for i in range(len(p)))
                    found.setdefault(key, list(p))
                elif w not in p and len(p) < 4:
                    stack.append(p + [w])
    out = []
    for cy in found.values():
        kinds = [ET[etype(cy[i], cy[(i+1) % len(cy)])][3] for i in range(len(cy))]
        nl = kinds.count('l'); ns = len({v[0] for v in cy})
        if len(cy) == 3 and nl == 0: cl = 'triangle'
        elif len(cy) == 4 and nl == 0:
            com = set(CORN[cy[0][1]])
            for v in cy: com &= set(CORN[v[1]])
            cl = 'square' if com else 'tt'
        elif len(cy) == 4 and nl == 4 and ns == 4: cl = 'plaquette'
        elif len(cy) == 4 and nl == 2 and ns == 2: cl = 'tube'
        else: cl = 'other'
        out.append((cy, cl))
    return out
CYC = cycles()

def gf2(rows, rhs, n):
    piv = {}
    for r, b in zip(rows, rhs):
        x = r | (b << n)
        while x & ((1 << n) - 1):
            p = (x & ((1 << n) - 1)).bit_length() - 1
            if p in piv: x ^= piv[p]
            else: piv[p] = x; break
        else:
            if x: return None
    ps = sorted(piv)
    for p in ps:
        for q in ps:
            if q != p and (piv[q] >> p) & 1: piv[q] ^= piv[p]
    sol = [0] * n
    for p in ps: sol[p] = (piv[p] >> n) & 1
    return sol

def gauge(F):
    rows, rhs = [], []
    for cy, cl in CYC:
        x = 0
        for i in range(len(cy)): x ^= 1 << etype(cy[i], cy[(i+1) % len(cy)])
        rows.append(x); rhs.append(0 if cl == 'tt' else F[cl])
    s = gf2(rows, rhs, NT)
    return None if s is None else np.array(s)

FLUX = dict(square=1, triangle=0, plaquette=1, tube=1)
U = gauge(FLUX)

# ---------- point group (proper rotations) and inversion
ROTS = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = sg[i]
        if round(np.linalg.det(M)) == 1: ROTS.append(M)
INV = -np.eye(3, dtype=int)
def rc(R, c):
    i, j = CORN[c]; return cn(didx(R @ DV[i]), didx(R @ DV[j]))
def w1(R):
    p = [didx(R @ DV[i]) for i in range(6)]; s = 0; seen = [0] * 6
    for i in range(6):
        if not seen[i]:
            L = 0; j = i
            while not seen[j]: seen[j] = 1; j = p[j]; L += 1
            s += L - 1
    return s % 2
W1 = [w1(R) for R in ROTS]

def psg(R, u=U):
    rows, rhs = [], []
    for j, (c1, c2, sh, kd) in enumerate(ET):
        Rsh = tuple(int(x) for x in R @ np.array(sh))
        jR = EK[(rc(R, c1), rc(R, c2), Rsh)]
        x = (1 << c1) ^ (1 << c2)
        for a in range(3):
            if sh[a] % 2: x ^= 1 << (12 + a)
        rows.append(x); rhs.append(int(u[jR] ^ u[j]))
    sol = gf2(rows, rhs, 15)
    if sol is None: return None
    return np.array([(-1) ** sol[c] for c in range(12)]), np.array(sol[12:15])

PSG = [psg(R) for R in ROTS]
PSGI = psg(INV)
def Wm(R, eta):
    W = np.zeros((12, 12))
    for c in range(12): W[rc(R, c), c] = eta[c]
    return W
WR = [Wm(R, e) for R, (e, s) in zip(ROTS, PSG)]
WI = Wm(INV, PSGI[0])

# ---------- translation-covariant operators as dicts sh -> 12x12
def act(R, eta, s, m, chi=1.0):
    out = {}
    for sh, M in m.items():
        Rsh = tuple(int(x) for x in R @ np.array(sh))
        Wt = Wm(R, eta)
        out[Rsh] = out.get(Rsh, 0) + chi * (-1.0) ** (s @ np.array(sh)) * (Wt @ M @ Wt.T)
    return out

def hop(t1, t2, u=U):
    m = {}
    for j, (c1, c2, sh, kd) in enumerate(ET):
        z = -(t1 if kd == 'o' else t2) * (-1.0) ** u[j]
        nsh = tuple(-x for x in sh)
        m.setdefault(sh, np.zeros((12, 12), complex))[c2, c1] += z
        m.setdefault(nsh, np.zeros((12, 12), complex))[c1, c2] += z
    return m

def addm(*ms, coeffs=None):
    out = {}
    coeffs = coeffs or [1.0] * len(ms)
    for a, m in zip(coeffs, ms):
        for sh, M in m.items(): out[sh] = out.get(sh, 0) + a * M
    return out

def bloch(m, k):
    k = np.asarray(k, float); H = np.zeros((12, 12), complex)
    for sh, M in m.items(): H += M * np.exp(-1j * k @ np.array(sh))
    return H
def bloch_batch(m, ks):
    ks = np.atleast_2d(ks); H = np.zeros((len(ks), 12, 12), complex)
    for sh, M in m.items(): H += M[None] * np.exp(-1j * ks @ np.array(sh))[:, None, None]
    return H
Q = np.array([np.pi] * 3)
def fold(h, mst, k):
    """24x24 folded Bloch H in basis (k, k+Q); mst = staggered blocks (phase at source)."""
    A = bloch(h, k); Bq = bloch(h, k + Q)
    Bkq = bloch(mst, k + Q)        # k -> k+Q
    Bqk = bloch(mst, k + 2 * Q)    # k+Q -> k
    return np.block([[A, Bqk], [Bkq, Bq]])
def fold_batch(h, mst, ks):
    ks = np.atleast_2d(ks)
    A = bloch_batch(h, ks); Bq = bloch_batch(h, ks + Q)
    Bkq = bloch_batch(mst, ks + Q); Bqk = bloch_batch(mst, ks + 2 * Q)
    top = np.concatenate([A, Bqk], axis=2); bot = np.concatenate([Bkq, Bq], axis=2)
    return np.concatenate([top, bot], axis=1)

# ---------- 2O and characters
def q2su(q):
    a, b, c, d = q; return np.array([[a+1j*b, c+1j*d], [-c+1j*d, a-1j*b]])
QS = []
for i in range(4):
    for s_ in (1, -1):
        v = [0]*4; v[i] = s_; QS.append(v)
for sg in itertools.product((1, -1), repeat=4): QS.append([x/2 for x in sg])
for i, j in itertools.combinations(range(4), 2):
    for si, sj in itertools.product((1, -1), repeat=2):
        v = [0]*4; v[i], v[j] = si/np.sqrt(2), sj/np.sqrt(2); QS.append(v)
G2 = [q2su(q) for q in QS]
PA = [np.array([[0,1],[1,0]]), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]])]
def so3(Uu): return np.rint(np.array([[0.5*np.real(np.trace(PA[i]@Uu@PA[j]@Uu.conj().T)) for j in range(3)] for i in range(3)])).astype(int)
def rid(R): return [k for k, S in enumerate(ROTS) if (S == R).all()][0]
PROJ = [rid(so3(g)) for g in G2]
def gid(Uu): return [k for k, V in enumerate(G2) if np.allclose(Uu, V)][0]
MUL = [[gid(G2[a] @ G2[b]) for b in range(48)] for a in range(48)]
SEC = [PROJ.index(r) for r in range(24)]

def lift(D, elems=None):
    """D: list of 24 matrices (projective rep of O with +-1 multipliers). Return all lifts to 2O
    (list of 48-lists) found by GF(2) solving for signs beta, or [] if none.  elems: subset of
    the 24 rotation indices forming a subgroup (default all)."""
    Rs = list(range(24)) if elems is None else sorted(elems)
    idx = {r: i for i, r in enumerate(Rs)}; rows = []; rhs = []
    for a in Rs:
        for b in Rs:
            g = MUL[SEC[a]][SEC[b]]; ab = PROJ[g]
            wv = 0 if g == SEC[ab] else 1
            X, Y = D[a] @ D[b], D[ab]
            if np.allclose(X, Y): e = 0
            elif np.allclose(X, -Y): e = 1
            else: return []
            x = 0
            for t in (idx[a], idx[b], idx[ab]): x ^= 1 << t
            rows.append(x); rhs.append(e ^ wv)
    sol = gf2(rows, rhs, len(Rs))
    if sol is None: return []
    def mk(beta):
        out = {}
        for g in range(48):
            r = PROJ[g]
            if r not in idx: continue
            out[g] = ((-1) ** beta[idx[r]]) * (1 if g == SEC[r] else -1) * D[r]
        return out
    lifts = [mk(sol)]
    if elems is None:
        a2 = [sol[i] ^ W1[r] for i, r in enumerate(Rs)]; lifts.append(mk(a2))
    return lifts

def spin_char(j2, Uu):
    tr = max(-1, min(1, np.real(np.trace(Uu)) / 2)); th = 2 * np.arccos(tr)
    if abs(np.sin(th / 2)) < 1e-12: return float(j2 + 1) * (1 if np.isclose(tr, 1) else (-1) ** j2)
    return np.sin((j2 + 1) * th / 2) / np.sin(th / 2)
CH12 = np.array([spin_char(1, g) for g in G2]); CH32 = np.array([spin_char(3, g) for g in G2])
CH52 = np.array([spin_char(5, g) for g in G2]) - CH32
def decomp(chi):
    return {nm: int(round(np.real(np.sum(np.conj(c) * chi)) / 48)) for nm, c in (('E1/2', CH12), ('E5/2', CH52), ('G3/2', CH32))}

def fixed_momenta():
    """momentum shift S_R: U_R maps k -> R k + pi R s_R (my conventions)."""
    out = []
    for kk in itertools.product(range(-3, 5), repeat=3):
        k = np.array(kk) * np.pi / 4
        ok = True
        for R, (e, s) in zip(ROTS, PSG):
            k2 = R @ k + np.pi * (R @ s)
            if not np.allclose(np.exp(1j * (k2 - k)), 1): ok = False; break
        if ok: out.append(kk)
    return out
