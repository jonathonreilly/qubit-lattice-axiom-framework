"""Independent Majorana-monomial algebra for the 5-qubit-per-site cubic code.

Every site operator is a Majorana monomial chi_{i1}...chi_{ik} (i1<...<ik),
stored as a 10-bit mask.  Site-local JW => monomials at different sites
commute (they act on disjoint qubits).  A multi-site operator is
coef * prod_sites M(mask_s); a "poly" is dict{tuple(masks) -> coef}.
Indices: 0..5 link b_d with DIRS = (+x,+y,+z,-x,-y,-z); 6,7 up; 8,9 dn.
"""
import itertools, numpy as np

NM = 10
DIRS = [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]
DIDX = {d:i for i,d in enumerate(DIRS)}
PC = np.array([bin(i).count('1') for i in range(1 << NM)], dtype=np.int64)

# SWP[a,b] = parity of #{(i in a, j in b): i>j}  -> M(a)M(b) = (-1)^SWP M(a^b)
SWP = np.zeros((1 << NM, 1 << NM), dtype=np.int8)
for b in range(1 << NM):
    s = np.zeros(1 << NM, dtype=np.int64)
    for j in range(NM):
        if b >> j & 1:
            s += PC[np.arange(1 << NM) >> (j + 1)]
    SWP[:, b] = (s & 1)

def site_mul(a, b):
    return (-1) ** int(SWP[a, b]), a ^ b

def anticomm_site(a, b):
    return (int(PC[a]) * int(PC[b]) - int(PC[a & b])) & 1

class Lat:
    def __init__(s, L):
        s.L = L; s.N = L ** 3
    def idx(s, v):
        L = s.L
        return (v[0] % L) * L * L + (v[1] % L) * L + (v[2] % L)
    def coord(s, i):
        L = s.L
        return (i // (L * L), (i // L) % L, i % L)

def mul(A, B):
    """A,B: (coef, masks np.array)"""
    ca, ma = A; cb, mb = B
    sg = int(SWP[ma, mb].sum()) & 1
    return (ca * cb * (-1) ** sg, ma ^ mb)

def anticomm(ma, mb):
    t = (PC[ma] * PC[mb] - PC[ma & mb]).sum()
    return int(t) & 1

def dagger(A):
    c, m = A
    k = PC[m]
    e = int((k * (k - 1) // 2).sum()) & 1
    return (np.conj(c) * (-1) ** e, m)

def poly_mul(P, Q):
    R = {}
    for ka, ca in P.items():
        ma = np.array(ka, dtype=np.int64)
        for kb, cb in Q.items():
            mb = np.array(kb, dtype=np.int64)
            sg = int(SWP[ma, mb].sum()) & 1
            k = tuple((ma ^ mb).tolist())
            R[k] = R.get(k, 0) + ca * cb * (-1) ** sg
    return {k: v for k, v in R.items() if abs(v) > 1e-12}

def poly_dag(P):
    R = {}
    for k, c in P.items():
        cc, _ = dagger((c, np.array(k)))
        R[k] = cc
    return R

def mono(N, items, coef=1.0):
    """items: list of (site, majorana_index) in the order of the product."""
    op = (complex(coef), np.zeros(N, dtype=np.int64))
    for (site, k) in items:
        m = np.zeros(N, dtype=np.int64); m[site] = 1 << k
        op = mul(op, (1.0, m))
    return op

def to_poly(A):
    return {tuple(A[1].tolist()): A[0]}

# ---------------- stabilizer group with phases ----------------
class StabGroup:
    """Generators given as (coef, masks) Hermitian with eigenvalue +1 on code."""
    def __init__(s, gens):
        s.gens = gens
        s.N = len(gens[0][1])
        s.vecs = [s._bits(g[1]) for g in gens]
        # gaussian elimination with combination tracking (bitmask over gens)
        s.piv = {}   # pivot bit -> (vec, combo)
        s.relations = []
        for i, v in enumerate(s.vecs):
            combo = 1 << i
            v, combo = s._reduce(v, combo)
            if v == 0:
                s.relations.append(combo)
            else:
                p = v.bit_length() - 1
                s.piv[p] = (v, combo)
        s.rank = len(s.piv)
    def _bits(s, m):
        x = 0
        for i, mm in enumerate(m.tolist()):
            if mm: x |= int(mm) << (NM * i)
        return x
    def _reduce(s, v, combo):
        while v:
            p = v.bit_length() - 1
            if p in s.piv:
                pv, pc = s.piv[p]
                v ^= pv; combo ^= pc
            else:
                break
        # full reduction (need v==0 test only on fully reduced)
        return v, combo
    def _full_reduce(s, v):
        combo = 0
        changed = True
        while v:
            p = v.bit_length() - 1
            if p not in s.piv:
                return v, combo
            pv, pc = s.piv[p]
            v ^= pv; combo ^= pc
        return 0, combo
    def product(s, combo):
        op = (1.0 + 0j, np.zeros(s.N, dtype=np.int64))
        i = 0
        while combo:
            if combo & 1:
                op = mul(op, s.gens[i])
            combo >>= 1; i += 1
        return op
    def check_no_minus_one(s):
        bad = 0
        for c in s.relations:
            op = s.product(c)
            assert not op[1].any()
            if abs(op[0] - 1) > 1e-9:
                bad += 1
        return bad
    def commuting(s):
        bad = 0
        G = s.gens
        # use per-generator support for speed
        sup = [np.nonzero(g[1])[0] for g in G]
        for i in range(len(G)):
            for j in range(i + 1, len(G)):
                common = np.intersect1d(sup[i], sup[j])
                if len(common) == 0: continue
                if anticomm(G[i][1][common], G[j][1][common]): bad += 1
        return bad
    def _touch(s):
        if not hasattr(s, 'touch'):
            s.touch = [[] for _ in range(s.N)]
            for gi, g in enumerate(s.gens):
                for st in np.nonzero(g[1])[0]: s.touch[st].append(gi)
        return s.touch
    def syndrome(s, m):
        """indices of generators anticommuting with monomial masks m"""
        touch = s._touch()
        nz = np.nonzero(m)[0]
        cand = set()
        for st in nz: cand.update(touch[st])
        out = []
        for i in sorted(cand):
            g = s.gens[i][1]
            if anticomm(g[nz], m[nz]): out.append(i)
        return out
    def code_value(s, A):
        """value of P A P / P for monomial A=(coef,m): returns
        ('zero',0) if anticommutes with a gen, ('stab', val) if in group,
        ('logical', None) otherwise."""
        c, m = A
        if s.syndrome(m):
            return ('zero', 0.0)
        v = s._bits(m)
        r, combo = s._full_reduce(v)
        if r:
            return ('logical', None)
        g = s.product(combo)
        assert (g[1] == m).all()
        return ('stab', c / g[0])
    def code_poly_value(s, P):
        tot = 0j; kinds = {}
        for k, c in P.items():
            kind, val = s.code_value((c, np.array(k, dtype=np.int64)))
            kinds[kind] = kinds.get(kind, 0) + 1
            if kind == 'logical':
                raise RuntimeError('logical term in code-space reduction')
            tot += val
        return tot, kinds

# ---------------- the 5-qubit model ----------------
def generators(lat, include_matter=True):
    N = lat.N; L = lat.L
    gens = {'D': [], 'W': [], 'Pu': [], 'Pd': []}
    for i in range(N):
        if include_matter:
            # D = (-i)^5 chi0..chi9
            gens['D'].append(mono(N, [(i, k) for k in range(10)], (-1j) ** 5))
            gens['Pu'].append(mono(N, [(i, 6), (i, 7)], -1j))
            gens['Pd'].append(mono(N, [(i, 8), (i, 9)], -1j))
        else:
            gens['D'].append(mono(N, [(i, k) for k in range(6)], (-1j) ** 3))
    for i in range(N):
        v = lat.coord(i)
        for (a, b) in [(0, 1), (1, 2), (0, 2)]:
            W = (1.0 + 0j, np.zeros(N, dtype=np.int64))
            ea = [0, 0, 0]; ea[a] = 1; eb = [0, 0, 0]; eb[b] = 1
            for (start, dirc) in [(v, a), (tuple(np.add(v, ea)), b),
                                  (tuple(np.add(v, eb)), a), (v, b)]:
                W = mul(W, u_edge(lat, start, dirc))
            gens['W'].append(W)
    return gens

def u_edge(lat, v, a):
    """u_e = b_{v,+a} b_{v+e_a,-a}"""
    N = lat.N
    w = list(v); w[a] += 1
    return mono(N, [(lat.idx(v), a), (lat.idx(w), a + 3)])

# ---------------- rotations ----------------
def rotations():
    """24 proper signed-permutation 3x3 matrices."""
    Rs = []
    for p in itertools.permutations(range(3)):
        for sg in itertools.product([1, -1], repeat=3):
            R = np.zeros((3, 3), dtype=int)
            for c in range(3): R[p[c], c] = sg[c]
            if round(np.linalg.det(R)) == 1: Rs.append(R)
    return Rs

def dir_perm(R):
    return [DIDX[tuple(int(x) for x in R @ np.array(d))] for d in DIRS]

def perm_sign(p):
    p = list(p); s = 1
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]; p[i], p[j] = p[j], p[i]; s = -s
    return s
