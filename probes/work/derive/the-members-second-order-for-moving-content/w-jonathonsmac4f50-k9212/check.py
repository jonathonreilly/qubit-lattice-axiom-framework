#!/usr/bin/env python3
"""
check.py for J:derive:the-members-second-order-for-moving-content:a1

Question: is the member's cubic order (second order in the fields, for moving content) forced by
consistency of the member's constraints, given the quadratic action with the bond shift at
alpha = K/4 (blocks 62, 101, 136, 144 as landed on main) ?

Method (all finite, exact integer/rational data; see ATTEMPT.md for the statement and for what is
ASSUMED).  Fields phi = (u, N_i, h_ij), K = 1, alpha = 1/4, beta = -alpha.
  S2 = the quadratic action of block 144 (checked equal to the second-order part of the ADM action).
  delta0 = its linear gauge symmetry: spatial relabelling (delta h = d xi + d xi, delta N = xi_dot)
           and time relabelling (delta u = xi0_dot, delta N_i = -d_i xi0).
  A cubic kernel S3 is 'consistent' if there is a LOCAL first-order field-dependent relabelling delta1
  (bilinear in (xi, phi), one derivative fewer than S3) with   delta0 S3 + delta1 S2 = 0  identically.
  'trivial' S3 = B(phi, F2(phi,phi)) with F2 a local derivative-free bilinear map (field redefinition).
All kernels are evaluated on formal exponentials (d -> q), momentum conserved, at random integer points.
Linear algebra: exact rank over Q where cheap, rank mod a large prime (a rigorous LOWER bound of the
rational rank, hence an UPPER bound of nullities) otherwise.  The classes of kernels are SPANNED by the bases
used because their dimensions (character averages, section 3b) equal the number of independent kernels found.
Every printed number below is produced by this script; ATTEMPT.md quotes them.
"""
import sys, time, itertools, random
from fractions import Fraction as F
import numpy as np
from sympy.polys.matrices import DomainMatrix
from sympy import ZZ, QQ
import sympy as sp

T0 = time.time()
P1 = 2147483629   # prime < 2^31
RES = []
def check(name, cond, detail=""):
    RES.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + name + ((" | " + detail) if detail else ""), flush=True)
def tm(): return "[%.0fs]" % (time.time() - T0)

# ----------------------------------------------------------------------------------------------
# 1. truncated nilpotent algebra -> exact multilinear kernels of the full ADM Lagrangian
# ----------------------------------------------------------------------------------------------
class A:
    __slots__ = ('c',)
    def __init__(self, c=None): self.c = c if c is not None else [F(0)] * 8
    @staticmethod
    def const(x):
        a = A(); a.c[0] = F(x); return a
    def __add__(s, o):
        if not isinstance(o, A): o = A.const(o)
        return A([x + y for x, y in zip(s.c, o.c)])
    __radd__ = __add__
    def __neg__(s): return A([-x for x in s.c])
    def __sub__(s, o):
        if not isinstance(o, A): o = A.const(o)
        return A([x - y for x, y in zip(s.c, o.c)])
    def __mul__(s, o):
        if not isinstance(o, A): o = F(o); return A([x * o for x in s.c])
        r = [F(0)] * 8
        for m1 in range(8):
            a = s.c[m1]
            if a == 0: continue
            for m2 in range(8):
                if m1 & m2: continue
                b = o.c[m2]
                if b == 0: continue
                r[m1 | m2] += a * b
        return A(r)
    __rmul__ = __mul__

def dmu(x, qs, mu):
    r = [F(0)] * 8
    for m in range(1, 8):
        if x.c[m] != 0:
            r[m] = x.c[m] * sum(qs[j][mu] for j in range(3) if m >> j & 1)
    return A(r)

def adm_lagrangian(qs, pols, mut=None):
    """L = N sqrt(gamma)(R + K_ij K^ij - K^2), gamma = delta + h, N = 1+u, lower-index shift N_i (K = 1).
    mut: None | 'noNinv' (drop 1/N in K_ij) | 'plusK2' (+K^2 instead of -K^2) | 'upperN' (upper-index shift)
         | 'expN' (lapse exp(u))."""
    nm = len(qs); qs = list(qs) + [[0, 0, 0, 0]] * (3 - nm)
    def field(g):
        a = A()
        for j in range(nm): a.c[1 << j] = F(g(pols[j]))
        return a
    u = field(lambda p: p['u'])
    Nf = [field(lambda p, i=i: p['N'][i]) for i in range(3)]
    h = [[field(lambda p, i=i, j=j: p['h'][i][j]) for j in range(3)] for i in range(3)]
    one = A.const(1); zero = A()
    mm = lambda X, Y: [[sum((X[i][k] * Y[k][j] for k in range(3)), A()) for j in range(3)] for i in range(3)]
    I = [[one if i == j else zero for j in range(3)] for i in range(3)]
    h2 = mm(h, h); h3 = mm(h2, h)
    ginv = [[I[i][j] - h[i][j] + h2[i][j] - h3[i][j] for j in range(3)] for i in range(3)]
    tr = lambda M: sum((M[i][i] for i in range(3)), A())
    x = (tr(h) - tr(h2) * F(1, 2) + tr(h3) * F(1, 3)) * F(1, 2)
    sq = one + x + x * x * F(1, 2) + x * x * x * F(1, 6)
    d = lambda f, mu: dmu(f, qs, mu)
    dh = [[[d(h[i][j], k + 1) for k in range(3)] for j in range(3)] for i in range(3)]
    Gl = [[[(dh[l][j][i] + dh[i][l][j] - dh[i][j][l]) * F(1, 2) for j in range(3)] for i in range(3)] for l in range(3)]
    Gam = [[[sum((ginv[k][l] * Gl[l][i][j] for l in range(3)), A()) for j in range(3)] for i in range(3)] for k in range(3)]
    Ric = [[None] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            t = A()
            for k in range(3):
                t = t + d(Gam[k][i][j], k + 1) - d(Gam[k][i][k], j + 1)
                for l in range(3):
                    t = t + Gam[k][k][l] * Gam[l][i][j] - Gam[k][j][l] * Gam[l][i][k]
            Ric[i][j] = t
    Rs = sum((ginv[i][j] * Ric[i][j] for i in range(3) for j in range(3)), A())
    if mut == 'upperN':
        Nl = [sum(((I[i][j] + h[i][j]) * Nf[j] for j in range(3)), A()) for i in range(3)]
    else:
        Nl = Nf
    if mut == 'expN':
        Nn = one + u + u * u * F(1, 2) + u * u * u * F(1, 6)
        Ninv = one - u + u * u * F(1, 2) - u * u * u * F(1, 6)
    else:
        Nn = one + u; Ninv = one - u + u * u - u * u * u
    if mut == 'noNinv': Ninv = one
    DN = [[d(Nl[j], i + 1) - sum((Gam[k][i][j] * Nl[k] for k in range(3)), A()) for j in range(3)] for i in range(3)]
    Kl = [[(d(h[i][j], 0) - DN[i][j] - DN[j][i]) * Ninv * F(1, 2) for j in range(3)] for i in range(3)]
    Ku = [[sum((ginv[i][k] * ginv[j][l] * Kl[k][l] for k in range(3) for l in range(3)), A()) for j in range(3)] for i in range(3)]
    KK = sum((Kl[i][j] * Ku[i][j] for i in range(3) for j in range(3)), A())
    Kt = sum((ginv[i][j] * Kl[i][j] for i in range(3) for j in range(3)), A())
    sgn = 1 if mut == 'plusK2' else -1
    return Nn * sq * (Rs + KK + sgn * (Kt * Kt))

# ----------------------------------------------------------------------------------------------
# 2. the quadratic action (block 144 form), gauge laws, equations-of-motion tensors
# ----------------------------------------------------------------------------------------------
CFG0 = dict(alpha=F(1, 4), beta=F(-1, 4), tf=1, time_gauge=True)
def L2cross(qa, pa, qb, pb, alpha=F(1, 4), beta=F(-1, 4)):
    """cross coefficient (momenta formal, d->q) of  alpha tr(Hd^2)+beta (tr Hd)^2 + u R1 + R2 ,  K = 1"""
    def Hd(q, p): return [[q[0] * p['h'][i][j] - q[i + 1] * p['N'][j] - q[j + 1] * p['N'][i] for j in range(3)] for i in range(3)]
    Ha = Hd(qa, pa); Hb = Hd(qb, pb)
    kin = 2 * alpha * sum(Ha[i][j] * Hb[i][j] for i in range(3) for j in range(3)) + \
          2 * beta * sum(Ha[i][i] for i in range(3)) * sum(Hb[i][i] for i in range(3))
    def R1(q, p):
        qq = sum(x * x for x in q[1:])
        return sum(q[i + 1] * q[j + 1] * p['h'][i][j] for i in range(3) for j in range(3)) - qq * sum(p['h'][i][i] for i in range(3))
    lap = pa['u'] * R1(qb, pb) + pb['u'] * R1(qa, pa)
    def r2(qX, pX, qY, pY):
        hX = pX['h']; hY = pY['h']
        trX = sum(hX[i][i] for i in range(3)); trY = sum(hY[i][i] for i in range(3))
        t1 = -F(1, 4) * sum(qX[k + 1] * hX[i][j] * qY[k + 1] * hY[i][j] for i in range(3) for j in range(3) for k in range(3))
        t2 = F(1, 2) * sum(qX[i + 1] * hX[i][k] * qY[j + 1] * hY[j][k] for i in range(3) for j in range(3) for k in range(3))
        t3 = -F(1, 2) * sum(qX[i + 1] * hX[i][j] * qY[j + 1] * trY for i in range(3) for j in range(3))
        t4 = F(1, 4) * sum(qX[k + 1] * trX * qY[k + 1] * trY for k in range(3))
        return t1 + t2 + t3 + t4
    return kin + lap + r2(qa, pa, qb, pb) + r2(qb, pb, qa, pa)

def rnd_vec(rng, lo, hi, n): return np.array([rng.randint(lo, hi) for _ in range(n)], dtype=np.int64)
def rnd_mode_pol(rng, lo=-3, hi=3):
    h = np.zeros((3, 3), dtype=np.int64)
    for i in range(3):
        for j in range(i, 3): h[i, j] = h[j, i] = rng.randint(lo, hi)
    return {'u': np.array(rng.randint(lo, hi), dtype=np.int64), 'N': rnd_vec(rng, lo, hi, 3), 'h': h}
def to_listpol(p):
    return {'u': int(p['u']), 'N': [int(x) for x in p['N']], 'h': [[int(p['h'][i, j]) for j in range(3)] for i in range(3)]}
def pol_to_vec(pol):
    h = pol['h']
    return [int(pol['u'])] + [int(x) for x in pol['N']] + [int(h[0][0]), int(h[0][1]), int(h[0][2]), int(h[1][1]), int(h[1][2]), int(h[2][2])]
def vec_to_pol(v):
    return {'u': np.array(v[0], dtype=np.int64), 'N': np.array(v[1:4], dtype=np.int64),
            'h': np.array([[v[4], v[5], v[6]], [v[5], v[7], v[8]], [v[6], v[8], v[9]]], dtype=np.int64)}

def gauge_pol(q, xi0, xi, cfg):
    """pure-gauge polarisation delta0 xi at momentum q:  du = tf q_t xi0, dN_i = -q_i xi0 + q_t xi_i, dh_ij = q_i xi_j + q_j xi_i"""
    q = np.asarray(q, dtype=np.int64)
    h = np.zeros((3, 3), dtype=np.int64)
    for i in range(3):
        for j in range(3): h[i, j] = q[i + 1] * xi[j] + q[j + 1] * xi[i]
    return {'u': np.array(cfg['tf'] * q[0] * xi0, dtype=np.int64),
            'N': np.array([-q[i + 1] * xi0 + q[0] * xi[i] for i in range(3)], dtype=np.int64), 'h': h}

BASIS = [('u', None, {'u': 1, 'N': [0, 0, 0], 'h': [[0] * 3 for _ in range(3)]})]
for i in range(3):
    Nn = [0, 0, 0]; Nn[i] = 1
    BASIS.append(('N', i, {'u': 0, 'N': Nn, 'h': [[0] * 3 for _ in range(3)]}))
for i in range(3):
    for j in range(i, 3):
        hh = [[0] * 3 for _ in range(3)]; hh[i][j] = 1; hh[j][i] = 1
        BASIS.append(('h', (i, j), {'u': 0, 'N': [0, 0, 0], 'h': hh}))
def Ehat8(q, pol, cfg):
    """8 x (tensor E) with  B(eta at -q, pol at q) = eta_u E_u + eta_N.E_N + sum_ij eta_ij E_ij"""
    ql = [int(x) for x in q]; mq = [-x for x in ql]; pl = to_listpol(pol)
    Eu = 0; EN = np.zeros(3, dtype=np.int64); Eh = np.zeros((3, 3), dtype=np.int64)
    for kind, idx, bp in BASIS:
        val = L2cross(mq, bp, ql, pl, cfg['alpha'], cfg['beta']) * 8
        val = F(val)
        assert val.denominator == 1
        val = int(val)
        if kind == 'u': Eu = val
        elif kind == 'N': EN[idx] = val
        else:
            i, j = idx
            if i == j: Eh[i, i] = val
            else:
                assert val % 2 == 0
                Eh[i, j] = Eh[j, i] = val // 2
    return {'u': np.array(Eu, dtype=np.int64), 'N': EN, 'h': Eh}
def Evec(q, pol, cfg):
    E = Ehat8(q, pol, cfg); h = E['h']
    return np.array([int(E['u'])] + [int(x) for x in E['N']] + [int(h[0, 0]), int(h[0, 1]), int(h[0, 2]), int(h[1, 1]), int(h[1, 2]), int(h[2, 2])], dtype=np.int64)

# ----------------------------------------------------------------------------------------------
# 3. linear algebra mod P1 and exact over Q
# ----------------------------------------------------------------------------------------------
def rref_mod(M, p=P1):
    A_ = np.array(M, dtype=np.int64) % p
    rows, cols = A_.shape; piv = []; r = 0
    for c in range(cols):
        if r >= rows: break
        nz = np.nonzero(A_[r:, c])[0]
        if len(nz) == 0: continue
        k = r + nz[0]
        if k != r: A_[[r, k]] = A_[[k, r]]
        inv = pow(int(A_[r, c]), -1, p)
        A_[r] = (A_[r] * inv) % p
        col = A_[:, c].copy(); col[r] = 0
        idx = np.nonzero(col)[0]
        if len(idx): A_[idx] = (A_[idx] - (col[idx, None] * A_[r][None, :]) % p) % p
        piv.append(c); r += 1
    return A_[:r], piv
def rank_mod(M, p=P1): return len(rref_mod(M, p)[1])
def nullspace_mod(M, p=P1):
    R, piv = rref_mod(M, p); cols = np.array(M).shape[1]
    free = [c for c in range(cols) if c not in set(piv)]
    out = []
    for f in free:
        v = np.zeros(cols, dtype=np.int64); v[f] = 1
        for i, pc in enumerate(piv): v[pc] = (-R[i, f]) % p
        out.append(v)
    return np.array(out, dtype=np.int64).reshape(len(free), cols)
def rank_exact(M):
    M = np.array(M, dtype=object)
    dm = DomainMatrix([[ZZ(int(x)) for x in r] for r in M], M.shape, ZZ).convert_to(QQ)
    return dm.rank()
def fmod(fr): return (fr.numerator % P1) * pow(fr.denominator % P1, -1, P1) % P1

# ----------------------------------------------------------------------------------------------
# 3b. exact dimension of the classes by character averaging (Molien / Weyl):  the class of ALL invariant polynomial
#     kernels is  (Pi^{x3} x Poly_w(q1,q2))^{S3 x G}   resp.  (Xi x Pi x Pi x Poly_{w-1}(q0,q1))^G ,
#     Pi = 1 + 3 + 6 the polarisations of (u, N, h), Xi = 1 + 3 the gauge parameters
# ----------------------------------------------------------------------------------------------
import cmath, math
def _pi_char(eigs): return 1 + sum(eigs) + (sum(eigs) ** 2 + sum(e ** 2 for e in eigs)) / 2
def _group(name):
    if name == 'O':
        out = []
        for sig in itertools.permutations(range(3)):
            for sgn in itertools.product([1, -1], repeat=3):
                R = np.zeros((3, 3))
                for i in range(3): R[sig[i], i] = sgn[i]
                if round(np.linalg.det(R)) == 1: out.append((list(np.linalg.eigvals(R)), 1.0 / 24))
        return out
    N = 96; out = []
    for k in range(N):
        th = -math.pi + 2 * math.pi * k / N
        out.append(([1, cmath.exp(1j * th), cmath.exp(-1j * th)], (1 - math.cos(th)) / N))
    return out
def _symw(lam, w):
    p1 = sum(lam); p2 = sum(l ** 2 for l in lam)
    return 1 if w == 0 else (p1 if w == 1 else (p1 ** 2 + p2) / 2)
def char_dim_S3(name, w):
    tot = 0
    for eigs, wt in _group(name):
        pk = lambda k: _pi_char([e ** k for e in eigs])
        lam4 = [1] + list(eigs)
        for tr, mult, std in ((pk(1) ** 3, 1, [1, 1]), (pk(2) * pk(1), 3, [1, -1]), (pk(3), 2, [cmath.exp(2j * math.pi / 3), cmath.exp(-2j * math.pi / 3)])):
            tot += wt * mult * tr * _symw([a * b for a in std for b in lam4], w)
    return int(round((tot / 6).real))
def char_dim_D(name, dw):
    tot = 0
    for eigs, wt in _group(name):
        lam = [1] + list(eigs); lam = lam + lam
        tot += wt * (1 + sum(eigs)) * _pi_char(eigs) ** 2 * _symw(lam, dw)
    return int(round(tot.real))

# ----------------------------------------------------------------------------------------------
# 4. SO(3)-covariant contraction patterns (delta and epsilon), exactly two derivatives etc.
# ----------------------------------------------------------------------------------------------
RANK = {'u': 0, 'N': 1, 'h': 2, 'x0': 0, 'x': 1}
LET = 'abcdefghijkl'
EPS = np.zeros((3, 3, 3), dtype=np.int64)
for (i, j, k), s in {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}.items(): EPS[i, j, k] = s
def matchings(lst):
    if not lst: yield []; return
    a = lst[0]
    for i in range(1, len(lst)):
        for m in matchings(lst[1:i] + lst[i + 1:]): yield [(a, lst[i])] + m
def slot_patterns(n):
    out = []; slots = list(range(n))
    if n % 2 == 0:
        for m in matchings(slots): out.append((None, tuple(m)))
    elif n >= 3:
        for tri in itertools.combinations(slots, 3):
            rest = [s for s in slots if s not in tri]
            for m in matchings(rest): out.append((tri, tuple(m)))
    return out
def einsum_str(ns, pat):
    eps, pairs = pat; lo = {}; c = 0
    for (a, b) in pairs: lo[a] = LET[c]; lo[b] = LET[c]; c += 1
    el = ''
    if eps is not None:
        for s in eps: lo[s] = LET[c]; el += LET[c]; c += 1
    subs = []; idx = 0
    for n in ns:
        subs.append(''.join(lo[idx + t] for t in range(n))); idx += n
    if eps is not None: subs.append(el)
    return ','.join(subs) + '->'
def factor_tensor(typ, nt, ns, mode):
    q, pol = mode; t = np.asarray(pol[typ], dtype=np.int64)
    for _ in range(ns): t = np.multiply.outer(t, q[1:4])
    return t * (int(q[0]) ** nt)
class Structure:
    def __init__(self, types, nts, nss):
        self.types = types; self.nts = nts; self.nss = nss
        self.nslots = [RANK[t] + s for t, s in zip(types, nss)]
        self.pats = slot_patterns(sum(self.nslots))
        self.strs = [einsum_str(self.nslots, p) for p in self.pats]
        self.haseps = [p[0] is not None for p in self.pats]
        self.bstrs = [self._bstr(s, he) for s, he in zip(self.strs, self.haseps)]
    @staticmethod
    def _bstr(s, he):
        ins, out = s.split('->'); parts = ins.split(',')
        nb = len(parts) - (1 if he else 0)
        parts = ['z' + p for p in parts[:nb]] + parts[nb:]
        return ','.join(parts) + '->z'
    def eval_batch(self, tensors):
        n = tensors[0].shape[0]; out = np.zeros((n, len(self.pats)), dtype=np.int64)
        for k, (s, he) in enumerate(zip(self.bstrs, self.haseps)):
            out[:, k] = np.einsum(s, *(list(tensors) + ([EPS] if he else [])))
        return out
def structures(tm_, w):
    seen = set(); res = []
    per = [(nt, ns) for nt in range(w + 1) for ns in range(w + 1) if nt + ns <= w]
    for d in itertools.product(per, repeat=3):
        if sum(a + b for a, b in d) != w: continue
        key = tuple(sorted(zip(tm_, d)))
        if key in seen: continue
        seen.add(key); res.append((tuple(tm_), tuple(x[0] for x in d), tuple(x[1] for x in d)))
    return res
def all_structs(w):
    return [Structure(*s) for tm_ in itertools.combinations_with_replacement(['u', 'N', 'h'], 3) for s in structures(tm_, w)]
def d_structs(w):
    S = []; dw = w - 1
    if dw < 0: return S
    per = [(nt, ns) for nt in range(dw + 1) for ns in range(dw + 1) if nt + ns <= dw]
    for xt in ('x0', 'x'):
        for pt in ('u', 'N', 'h'):
            for et in ('u', 'N', 'h'):
                for d1 in per:
                    for d2 in per:
                        if sum(d1) + sum(d2) != dw: continue
                        S.append(Structure((xt, pt, et), (d1[0], d2[0], 0), (d1[1], d2[1], 0)))
    return S
def f2_structs():
    return [Structure((x, y, e), (0, 0, 0), (0, 0, 0)) for x in ('u', 'N', 'h') for y in ('u', 'N', 'h') for e in ('u', 'N', 'h')]
def bfactor(typ, nt, ns, mode):
    Q, pol = mode; t = pol[typ]; n = Q.shape[0]
    for _ in range(ns):
        t = t[..., None] * Q[:, 1:4].reshape((n,) + (1,) * (t.ndim - 1) + (3,))
    return t * (Q[:, 0].astype(np.int64) ** nt).reshape((n,) + (1,) * (t.ndim - 1))
def Wb(structs, modes):
    """cross kernel (sum over the 6 assignments of 3 modes to 3 factors) for every pattern; batched over points"""
    outs = []
    for S in structs:
        acc = None
        for perm in itertools.permutations(range(3)):
            v = S.eval_batch([bfactor(S.types[f], S.nts[f], S.nss[f], modes[perm[f]]) for f in range(3)])
            acc = v if acc is None else acc + v
        outs.append(acc)
    return np.hstack(outs)
def Db(structs, xim, phim, Em):
    return np.hstack([S.eval_batch([bfactor(S.types[0], S.nts[0], S.nss[0], xim), bfactor(S.types[1], S.nts[1], S.nss[1], phim),
                                    bfactor(S.types[2], S.nts[2], S.nss[2], Em)]) for S in structs])
def stack_modes(modes):
    Q = np.array([m[0] for m in modes], dtype=np.int64)
    pol = {k: np.array([np.asarray(m[1][k]) for m in modes], dtype=np.int64) for k in modes[0][1]}
    return (Q, pol)
def rand_modes3(rng, n):
    pts = []
    for _ in range(n):
        q1 = rnd_vec(rng, -3, 3, 4); q2 = rnd_vec(rng, -3, 3, 4); q0 = -q1 - q2
        pts.append(((q0, rnd_mode_pol(rng)), (q1, rnd_mode_pol(rng)), (q2, rnd_mode_pol(rng))))
    return pts
def batch3(pts): return [stack_modes([p[j] for p in pts]) for j in range(3)]
def xi_mode(q, xi0, xi): return (q, {'x0': np.array(xi0, dtype=np.int64), 'x': np.array(xi, dtype=np.int64)})
def pivots(M):
    return rref_mod(np.array(M, dtype=np.int64) % P1)[1]

SO3 = {}   # caches per weight
def so3_prepare(w, seed=0):
    """independent cubic kernels / D-forms of weight w (SO(3), proper rotations: delta and epsilon)"""
    S3 = all_structs(w); D = d_structs(w); rng = random.Random(100 + w + 1000 * seed)
    npat = sum(len(s.pats) for s in S3); ndp = sum(len(s.pats) for s in D)
    ng = 330 if w == 2 else 100
    M = Wb(S3, batch3(rand_modes3(rng, ng)))
    selS = pivots(M)
    selD = []
    if D:
        xs = []; ph = []; Es = []
        for _ in range(ng):
            q0 = rnd_vec(rng, -3, 3, 4); q1 = rnd_vec(rng, -3, 3, 4)
            xs.append(xi_mode(q0, rng.randint(-3, 3), rnd_vec(rng, -3, 3, 3))); ph.append((q1, rnd_mode_pol(rng))); Es.append((-q0 - q1, rnd_mode_pol(rng)))
        selD = pivots(Db(D, stack_modes(xs), stack_modes(ph), stack_modes(Es)))
    M2 = Wb(S3, batch3(rand_modes3(rng, ng // 3)))
    rk_all = rank_mod(np.vstack([M, M2]) % P1)
    SO3[w] = dict(S3=S3, D=D, selS=selS, selD=selD, npat=npat, ndp=ndp, rk_all=rk_all)
    return SO3[w]

def so3_system(w, cfg, seed=1):
    """gauge-identity rows for the SO(3) class.  returns A (rows x nc), B (rows x nd)"""
    c = SO3[w]; S3, D, selS, selD = c['S3'], c['D'], c['selS'], c['selD']
    nc, nd = len(selS), len(selD); rng = random.Random(777 + w + 1000 * seed)
    neq = nc + nd + 60; A0s = []; m1s = []; m2s = []; xs = []; E1s = []; E2s = []
    for _ in range(neq):
        q1 = rnd_vec(rng, -3, 3, 4); q2 = rnd_vec(rng, -3, 3, 4); q0 = -q1 - q2
        xi0 = rng.randint(-3, 3) if cfg['time_gauge'] else 0
        xi = rnd_vec(rng, -3, 3, 3)
        A0s.append((q0, gauge_pol(q0, xi0, xi, cfg))); m1 = (q1, rnd_mode_pol(rng)); m2 = (q2, rnd_mode_pol(rng))
        m1s.append(m1); m2s.append(m2); xs.append(xi_mode(q0, xi0, xi))
        if D: E1s.append((q1, Ehat8(q1, m1[1], cfg))); E2s.append((q2, Ehat8(q2, m2[1], cfg)))
    Ab = Wb(S3, [stack_modes(A0s), stack_modes(m1s), stack_modes(m2s)])
    # select columns: patterns are stored structure by structure
    Am = Ab[:, selS]
    if D:
        bx = stack_modes(xs)
        Bm = (Db(D, bx, stack_modes(m1s), stack_modes(E2s)) + Db(D, bx, stack_modes(m2s), stack_modes(E1s)))[:, selD]
    else: Bm = np.zeros((neq, 0), dtype=np.int64)
    return Am, Bm

def count_dim(Am, Bm):
    nc = Am.shape[1]; nd = Bm.shape[1]
    J = np.hstack([Am, Bm]) % P1
    rJ = rank_mod(J); rB = rank_mod(Bm % P1) if nd else 0
    return nc - (rJ - rB), rJ, rB

# ----------------------------------------------------------------------------------------------
# 5. the 24 proper cubic rotations: orbit sums of component monomials (lattice symmetry class)
# ----------------------------------------------------------------------------------------------
COMPS = ['u', 'N0', 'N1', 'N2', 'h00', 'h01', 'h02', 'h11', 'h12', 'h22']
CIDX = {c: i for i, c in enumerate(COMPS)}
def comp_act(c, sig, sgn):
    if c == 'u': return 1, 'u'
    if c[0] == 'N':
        i = int(c[1]); return sgn[i], 'N%d' % sig[i]
    i = int(c[1]); j = int(c[2]); a, b = sig[i], sig[j]
    if a > b: a, b = b, a
    return sgn[i] * sgn[j], 'h%d%d' % (a, b)
GO = []
for sig in itertools.permutations(range(3)):
    for sgn in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3), dtype=int)
        for i in range(3): R[sig[i], i] = sgn[i]
        if round(np.linalg.det(R)) == 1: GO.append((sig, sgn))
def comp_tables(g):
    sig, sgn = g
    idx = np.zeros(10, dtype=int); sg = np.zeros(10, dtype=np.int64)
    for c in COMPS:
        s, c2 = comp_act(c, sig, sgn); idx[CIDX[c]] = CIDX[c2]; sg[CIDX[c]] = s
    qidx = np.zeros(4, dtype=int); qsg = np.zeros(4, dtype=np.int64); qidx[0] = 0; qsg[0] = 1
    for i in range(3): qidx[i + 1] = sig[i] + 1; qsg[i + 1] = sgn[i]
    return idx, sg, qidx, qsg
TABLES = [comp_tables(g) for g in GO]
def act_comp_arr(Pm, tab):
    idx, sg, _, _ = tab; out = np.zeros_like(Pm); out[:, idx] = Pm * sg[None, :]; return out
def act_q_arr(Q, tab):
    _, _, qidx, qsg = tab; out = np.zeros_like(Q); out[:, qidx] = Q * qsg[None, :]; return out
def act_S3(m, tab):
    c1, c2, c3, e = m; idx, sg, qidx, qsg = tab
    s = sg[c1] * sg[c2] * sg[c3]; ne = []
    for v in e:
        mode = v // 4; mu = v % 4; s *= qsg[mu]; ne.append(mode * 4 + qidx[mu])
    return int(s), (int(idx[c1]), int(idx[c2]), int(idx[c3]), tuple(sorted(int(x) for x in ne)))
def act_D(m, tab):
    xc, pc, ec, qv = m; idx, sg, qidx, qsg = tab
    s = qsg[xc] * sg[pc] * sg[ec]; nq = None
    if qv is not None:
        mode = qv // 4; mu = qv % 4; s *= qsg[mu]; nq = mode * 4 + qidx[mu]
    return int(s), (int(qidx[xc]), int(idx[pc]), int(idx[ec]), None if nq is None else int(nq))
def act_F2(m, tab):
    a, b, c = m; idx, sg, _, _ = tab
    return int(sg[a] * sg[b] * sg[c]), (int(idx[a]), int(idx[b]), int(idx[c]))
def canon_reduce(mons, act):
    seen = set(); reps = []
    for m in mons:
        if m in seen: continue
        orb = {}; zero = False
        for tab in TABLES:
            s, m2 = act(m, tab)
            if m2 in orb and orb[m2] != s: zero = True
            orb[m2] = s
        for m2 in orb: seen.add(m2)
        if not zero: reps.append(m)
    return reps
def reps_S3(w):
    mons = [(c1, c2, c3, e) for c1 in range(10) for c2 in range(10) for c3 in range(10) for e in itertools.combinations_with_replacement(range(8), w)]
    return canon_reduce(mons, act_S3)
def reps_D(w):
    dw = w - 1
    if dw < 0: return []
    qv = [None] if dw == 0 else list(range(8))
    return canon_reduce([(xc, pc, ec, q) for xc in range(4) for pc in range(10) for ec in range(10) for q in qv], act_D)
def reps_F2(): return canon_reduce([(a, b, c) for a in range(10) for b in range(10) for c in range(10)], act_F2)

def eval_S3(reps, Pm, Qm):
    n = Pm[0].shape[0]; R = len(reps)
    c1 = np.array([m[0] for m in reps]); c2 = np.array([m[1] for m in reps]); c3 = np.array([m[2] for m in reps])
    ne = len(reps[0][3]); ev = [np.array([m[3][k] for m in reps]) for k in range(ne)]
    out = np.zeros((n, R), dtype=np.int64)
    for tab in TABLES:
        Pg = [act_comp_arr(p, tab) for p in Pm]; Qg = [act_q_arr(q, tab) for q in Qm]
        for a, b, c in itertools.permutations(range(3)):
            val = Pg[a][:, c1] * Pg[b][:, c2] * Pg[c][:, c3]
            qcat = np.concatenate([Qg[a], Qg[b]], axis=1)
            for k in range(ne): val = val * qcat[:, ev[k]]
            out += val
    return out
def eval_D(reps, X, Q0, Pp, Q1, E):
    n = X.shape[0]; R = len(reps)
    xc = np.array([m[0] for m in reps]); pc = np.array([m[1] for m in reps]); ec = np.array([m[2] for m in reps])
    qv = np.array([-1 if m[3] is None else m[3] for m in reps]); qvv = np.where(qv < 0, 8, qv)
    out = np.zeros((n, R), dtype=np.int64)
    for tab in TABLES:
        Xg = act_q_arr(X, tab); Qg0 = act_q_arr(Q0, tab); Qg1 = act_q_arr(Q1, tab)
        Pg = act_comp_arr(Pp, tab); Eg = act_comp_arr(E, tab)
        qcat = np.concatenate([Qg0, Qg1, np.ones((n, 1), dtype=np.int64)], axis=1)
        out += Xg[:, xc] * Pg[:, pc] * Eg[:, ec] * qcat[:, qvv]
    return out
def eval_F2(reps, Pa, Pb, E):
    n = Pa.shape[0]; a = np.array([m[0] for m in reps]); b = np.array([m[1] for m in reps]); c = np.array([m[2] for m in reps])
    out = np.zeros((n, len(reps)), dtype=np.int64)
    for tab in TABLES:
        out += act_comp_arr(Pa, tab)[:, a] * act_comp_arr(Pb, tab)[:, b] * act_comp_arr(E, tab)[:, c]
    return out
def make_modes(rng, n):
    Q = [np.zeros((n, 4), dtype=np.int64) for _ in range(3)]; Pm = [np.zeros((n, 10), dtype=np.int64) for _ in range(3)]
    for k in range(n):
        q1 = rnd_vec(rng, -3, 3, 4); q2 = rnd_vec(rng, -3, 3, 4); q0 = -q1 - q2
        for j, (q, pol) in enumerate(((q0, rnd_mode_pol(rng)), (q1, rnd_mode_pol(rng)), (q2, rnd_mode_pol(rng)))):
            Q[j][k] = q; Pm[j][k] = pol_to_vec(pol)
    return Q, Pm

OC = {}
def o_prepare(w, seed=0):
    rng = random.Random(5000 + w + 100 * seed)
    reps = reps_S3(w); Dreps = reps_D(w)
    ng = max(len(reps) // 3 + 80, 500) if w == 2 else (len(reps) + 20 if len(reps) <= 200 else len(reps) // 3 + 80)
    Q, Pm = make_modes(rng, ng); M = eval_S3(reps, Pm, Q)
    selS = rref_mod(M % P1)[1]
    # saturation of the rank at fresh points
    Q2, P2 = make_modes(rng, ng // 3); M2 = eval_S3(reps, P2, Q2)
    rk_all = rank_mod(np.vstack([M, M2]) % P1)
    selD = []
    if Dreps:
        n2 = len(Dreps) + 60; Q, Pm = make_modes(rng, n2)
        X = np.array([[rng.randint(-3, 3) for _ in range(4)] for _ in range(n2)], dtype=np.int64)
        E = np.array([pol_to_vec(rnd_mode_pol(rng)) for _ in range(n2)], dtype=np.int64)
        selD = rref_mod(eval_D(Dreps, X, Q[1], Pm[1], Q[2], E) % P1)[1]
    OC[w] = dict(reps=reps, Dreps=Dreps, selS=selS, selD=selD, rk_all=rk_all, nreps=len(reps))
    return OC[w]
def o_system(w, cfg, seed=1):
    c = OC[w]; reps, Dreps, selS, selD = c['reps'], c['Dreps'], c['selS'], c['selD']
    nc, nd = len(selS), len(selD); rng = random.Random(9000 + w + 100 * seed)
    neq = nc + nd + 60; Q, Pm = make_modes(rng, neq)
    Xi = np.zeros((neq, 4), dtype=np.int64); A0P = np.zeros((neq, 10), dtype=np.int64)
    E1 = np.zeros((neq, 10), dtype=np.int64); E2 = np.zeros((neq, 10), dtype=np.int64)
    for k in range(neq):
        xi0 = rng.randint(-3, 3) if cfg['time_gauge'] else 0; xi = rnd_vec(rng, -3, 3, 3)
        Xi[k] = [xi0] + list(xi); A0P[k] = pol_to_vec(gauge_pol(Q[0][k], xi0, xi, cfg))
        E1[k] = Evec(Q[1][k], vec_to_pol(Pm[1][k]), cfg); E2[k] = Evec(Q[2][k], vec_to_pol(Pm[2][k]), cfg)
    A_ = eval_S3(reps, [A0P, Pm[1], Pm[2]], Q)[:, selS]
    if Dreps:
        B_ = (eval_D(Dreps, Xi, Q[0], Pm[1], Q[1], E2) + eval_D(Dreps, Xi, Q[0], Pm[2], Q[2], E1))[:, selD]
    else: B_ = np.zeros((neq, 0), dtype=np.int64)
    return A_, B_

# ----------------------------------------------------------------------------------------------
# 6. checks
# ----------------------------------------------------------------------------------------------
def adm_cross3(Q, Pm, k, mut=None):
    qs = [[int(x) for x in Q[i][k]] for i in range(3)]
    pols = []
    for i in range(3):
        v = [int(x) for x in Pm[i][k]]
        pols.append({'u': v[0], 'N': v[1:4], 'h': [[v[4], v[5], v[6]], [v[5], v[7], v[8]], [v[6], v[8], v[9]]]})
    return adm_lagrangian(qs, pols, mut).c[7]
MUTS = [None, 'upperN', 'expN', 'noNinv', 'plusK2']

print("=== 0. setting: block 144 / 101 quadratic action, K=1, alpha=1/4, beta=-alpha ===", flush=True)
rng = random.Random(5)
ok = True
for _ in range(40):
    qa = [rng.randint(-3, 3) for _ in range(4)]; qb = [-x for x in qa]
    pa = {'u': rng.randint(-3, 3), 'N': [rng.randint(-3, 3) for _ in range(3)], 'h': [[0] * 3 for _ in range(3)]}
    pb = {'u': rng.randint(-3, 3), 'N': [rng.randint(-3, 3) for _ in range(3)], 'h': [[0] * 3 for _ in range(3)]}
    for pp in (pa, pb):
        for i in range(3):
            for j in range(i, 3): pp['h'][i][j] = pp['h'][j][i] = rng.randint(-3, 3)
    if adm_lagrangian([qa, qb], [pa, pb]).c[3] != L2cross(qa, pa, qb, pb): ok = False
check("S0.1 second-order part of N sqrt(gamma)(K_ij K^ij - K^2 + R) equals block 144's quadratic action (alpha=K/4, beta=-alpha), 40 random cross-kernels", ok)
rng = random.Random(3); ok = True; ok_bad = True
for _ in range(60):
    q = rnd_vec(rng, -3, 3, 4); phi = rnd_mode_pol(rng)
    xi0 = rng.randint(-3, 3); xi = rnd_vec(rng, -3, 3, 3)
    for cfg_, expect_zero in ((CFG0, True),):
        E = Ehat8(q, phi, cfg_); A0 = gauge_pol(-q, xi0, xi, cfg_)
        val = int(A0['u'] * E['u']) + int(np.dot(A0['N'], E['N'])) + int(np.sum(A0['h'] * E['h']))
        if val != 0: ok = False
    cfgb = dict(alpha=F(1, 2), beta=F(-1, 2), tf=1, time_gauge=True)       # wrong time law for alpha != K/4
    E = Ehat8(q, phi, cfgb); A0 = gauge_pol(-q, xi0, xi, cfgb)
    if xi0 != 0 and int(A0['u'] * E['u']) + int(np.dot(A0['N'], E['N'])) + int(np.sum(A0['h'] * E['h'])) != 0: ok_bad = False
check("S0.2 the quadratic action is invariant under spatial relabelling (dh=d xi+d xi, dN=xi_dot) and time relabelling (du=xi0_dot, dN=-d xi0) at alpha=K/4, 60 random points", ok)
check("S0.3 control: at alpha=K/2 the undeformed time law du=xi0_dot is NOT a symmetry (block 144 T2(c)); deformed law du=(4 alpha/K) xi0_dot is",
      (not ok_bad))
rng = random.Random(8); okd = True; cfgd = dict(alpha=F(1, 2), beta=F(-1, 2), tf=2, time_gauge=True)
for _ in range(60):
    q = rnd_vec(rng, -3, 3, 4); phi = rnd_mode_pol(rng); xi0 = rng.randint(-3, 3); xi = rnd_vec(rng, -3, 3, 3)
    E = Ehat8(q, phi, cfgd); A0 = gauge_pol(-q, xi0, xi, cfgd)
    if int(A0['u'] * E['u']) + int(np.dot(A0['N'], E['N'])) + int(np.sum(A0['h'] * E['h'])) != 0: okd = False
check("S0.3b deformed law du=(4 alpha/K) xi0_dot is a symmetry at alpha=1/2", okd)

# static sector: conformal metric gamma = psi^4 delta  (block 60's lengths l = chi^2, chi = psi)
x, y, z = sp.symbols('x y z'); psi = sp.Function('psi')(x, y, z); X = [x, y, z]
g = sp.diag(psi**4, psi**4, psi**4); gi = g.inv()
Gam = [[[sum(gi[k, l] * (sp.diff(g[l, i], X[j]) + sp.diff(g[l, j], X[i]) - sp.diff(g[i, j], X[l])) for l in range(3)) / 2 for j in range(3)] for i in range(3)] for k in range(3)]
Ric = sp.zeros(3, 3)
for i in range(3):
    for j in range(3):
        Ric[i, j] = sum(sp.diff(Gam[k][i][j], X[k]) - sp.diff(Gam[k][i][k], X[j]) for k in range(3)) + \
            sum(Gam[k][k][l] * Gam[l][i][j] - Gam[k][j][l] * Gam[l][i][k] for k in range(3) for l in range(3))
Rs = sum(gi[i, j] * Ric[i, j] for i in range(3) for j in range(3))
expr = sp.simplify(psi**6 * Rs + 8 * psi * sum(sp.diff(psi, v, 2) for v in X))
check("S0.4 conformally flat slice gamma=psi^4 delta (lengths l=chi^2, chi=psi): sqrt(gamma) R = -8 psi laplacian(psi) exactly; so N sqrt(gamma) R = -8 N chi laplacian chi, block 60's F with lapse multiplier N=w", sp.simplify(expr) == 0)
print(tm(), flush=True)

# ---------------- SO(3) class -------------------------------------------------------------
print("=== 1. class SO(3): local polynomial cubic kernels of exactly w derivatives, delta/epsilon contractions ===", flush=True)
res3 = {}
for w in (0, 1, 2):
    c = so3_prepare(w)
    Am, Bm = so3_system(w, CFG0)
    nc, nd = Am.shape[1], Bm.shape[1]
    Jm = np.hstack([Am, Bm]) % P1
    rJ = rank_mod(Jm); rBe = rank_exact(Bm) if nd else 0
    upper = nc - rJ + rBe
    res3[w] = dict(nc=nc, nd=nd, rJ=rJ, rB=rBe, upper=upper, Am=Am, Bm=Bm)
    check("S1.%d.a w=%d: %d contraction patterns span %d independent kernels (rank saturates at fresh points: %d)" % (w, w, c['npat'], nc, c['rk_all']),
          c['rk_all'] == nc, "n_c=%d n_d=%d" % (nc, nd))
    cS = char_dim_S3('SO3', w); cD = char_dim_D('SO3', w - 1) if w >= 1 else 0
    check("S1.%d.c w=%d: character count of the class of ALL SO(3)-invariant symmetric cubic kernels = %d and of ALL local gauge-deformation forms = %d; equal to n_c=%d, n_d=%d, so the independent kernels span both classes" % (w, w, cS, cD, nc, nd), cS == nc and cD == nd)
    check("S1.%d.b w=%d: consistent vertices <= n_c - rank_p[A B] + rank_Q B = %d - %d + %d = %d" % (w, w, nc, rJ, rBe, upper), True)
print(tm(), flush=True)
check("S1.3 SO(3) weight 0 and weight 1: NO consistent cubic vertex (upper bound 0)", res3[0]['upper'] == 0 and res3[1]['upper'] == 0)
check("S1.4 SO(3) weight 2: consistent cubic vertices form a space of dimension <= 19", res3[2]['upper'] == 19)

Am_b, Bm_b = so3_system(2, CFG0, seed=2)
d_b, rJ_b, rB_b = count_dim(Am_b, Bm_b)
check("S1.5 independent second sample of gauge points (seed 2): same dimension bound %d (mod p ranks %d, %d)" % (d_b, rJ_b, rB_b), d_b == 19)

# trivial vertices (field redefinitions) and the ADM vertex, in c-coordinates
c = SO3[2]; S3 = c['S3']; selS = c['selS']; nc3 = len(selS); nc = nc3; F2 = f2_structs(); nF2 = sum(len(s.pats) for s in F2)
rng = random.Random(9090); ngen = nc + 80
pts = rand_modes3(rng, ngen); bm = batch3(pts)
Wsel = Wb(S3, bm)[:, selS]
Tt = np.zeros((ngen, nF2), dtype=np.int64)
Eb = [stack_modes([(p[i][0], Ehat8(p[i][0], p[i][1], CFG0)) for p in pts]) for i in range(3)]
for i in range(3):
    j, kk = [xx for xx in range(3) if xx != i]
    Tt += Db(F2, bm[j], bm[kk], Eb[i]) + Db(F2, bm[kk], bm[j], Eb[i])
ADMs = {mu: [] for mu in MUTS}
for p in pts:
    qs = [[int(xx) for xx in mm[0]] for mm in p]; pols = [to_listpol(mm[1]) for mm in p]
    for mu in MUTS: ADMs[mu].append(adm_lagrangian(qs, pols, mu).c[7])
def uK2_kernel(bm):
    """cross kernel of  int u [ Hdot_ij Hdot_ij - (tr Hdot)^2 ] ,  Hdot = h_dot - d N - d N^T  (a lapse-dependent rescaling of the kinetic term)"""
    def Hd(mode):
        Q, p = mode; qi = Q[:, 1:4]; N = p['N']
        return Q[:, 0][:, None, None] * p['h'] - (qi[:, :, None] * N[:, None, :] + N[:, :, None] * qi[:, None, :])
    out = 0
    for a_, b_, c_ in itertools.permutations(range(3)):
        Hb = Hd(bm[b_]); Hc = Hd(bm[c_])
        out = out + bm[a_][1]['u'] * (np.einsum('zij,zij->z', Hb, Hc) - np.einsum('zii->z', Hb) * np.einsum('zii->z', Hc))
    return out
U2 = uK2_kernel(bm).reshape(-1, 1)
Wm = Wsel % P1
Tint = Tt
rkT = rank_exact(Tint)
Am_ = {mu: np.array([[fmod(v)] for v in ADMs[mu]], dtype=np.int64) for mu in MUTS}
aug = np.hstack([Wm, Tint % P1] + [Am_[mu] for mu in MUTS] + [U2 % P1])
Rr, piv = rref_mod(aug)
check("S1.6 the %d F2-patterns (local derivative-free field redefinitions) give %d independent trivial cubic kernels (exact rank over Q), all inside the class; the ADM cubic kernel, 4 variants and the kinetic-rescaling kernel too (rank of [W|T|ADM variants|uK2] = n_c = %d)" % (nF2, rkT, nc),
      len(piv) == nc and rkT == 18, "rank=%d" % len(piv))
ctr = Rr[:nc, nc:nc + Tint.shape[1]].T
cvec = {mu: Rr[:nc, nc + Tint.shape[1] + i] for i, mu in enumerate(MUTS)}
cU2 = Rr[:nc, nc + Tint.shape[1] + len(MUTS)]
J2 = np.hstack([res3[2]['Am'], res3[2]['Bm']]) % P1
Nsp = nullspace_mod(J2); sol3 = Nsp[:, :nc]
dsol = rank_mod(sol3)
check("S1.7 mod-p dimension of the consistent space is %d (equals the upper bound)" % dsol, dsol == res3[2]['upper'])
check("S1.8 every trivial vertex is consistent (rank[sol; trivial] = rank sol)", rank_mod(np.vstack([sol3, ctr])) == dsol and rank_mod(ctr) == rkT)
def in_span(basis, v): return rank_mod(np.vstack([basis, v[None, :]])) == rank_mod(basis)
check("S1.9 the ADM cubic vertex is consistent (lies in the space of consistent vertices)", in_span(sol3, cvec[None]))
check("S1.10 field-redefined ADM variants (upper-index shift; exponential lapse) are consistent (positive control)", in_span(sol3, cvec['upperN']) and in_span(sol3, cvec['expN']))
check("S1.11 mutated ADM (drop 1/N in K_ij) is NOT consistent; nor is ADM with +K^2 (negative controls)", (not in_span(sol3, cvec['noNinv'])) and (not in_span(sol3, cvec['plusK2'])))
rk_tr = rank_mod(ctr); rk_tra = rank_mod(np.vstack([ctr, cvec[None][None, :]]))
check("S1.12 ADM is NOT a trivial vertex: rank[trivial; ADM] = rank[trivial] + 1 = %d (rank mod p is a lower bound for the rank over Q)" % rk_tra, rk_tra == rk_tr + 1 and rk_tr == rkT)
quot3 = res3[2]['upper'] - rkT
check("S1.13 SO(3), weight 2: consistent vertices / trivial vertices has dimension <= %d - %d = %d and ADM spans it" % (res3[2]['upper'], rkT, quot3), quot3 == 1)
print(tm(), flush=True)

# ---------------- O class (proper cubic rotations: the Lattice axiom's symmetry) --------------
print("=== 2. class O: the 24 proper cubic rotations (no SO(3) assumed); orbit sums of component monomials ===", flush=True)
resO = {}
for w in (0, 1, 2):
    c = o_prepare(w)
    Ao, Bo = o_system(w, CFG0)
    nc, nd = Ao.shape[1], Bo.shape[1]
    rJ = rank_mod(np.hstack([Ao, Bo]) % P1); rBe = rank_exact(Bo) if nd else 0
    resO[w] = dict(nc=nc, nd=nd, rJ=rJ, rB=rBe, upper=nc - rJ + rBe, A=Ao, B=Bo)
    check("S2.%d.a w=%d: %d orbit sums span %d independent O-invariant kernels (rank at fresh points %d); n_d=%d" % (w, w, c['nreps'], nc, c['rk_all'], nd), c['rk_all'] == nc)
    cS = char_dim_S3('O', w); cD = char_dim_D('O', w - 1) if w >= 1 else 0
    check("S2.%d.c w=%d: character count of ALL O-invariant symmetric cubic kernels = %d, of ALL local gauge-deformation forms = %d; equal to n_c=%d, n_d=%d (the bases span both classes)" % (w, w, cS, cD, nc, nd), cS == nc and cD == nd)
    check("S2.%d.b w=%d: consistent vertices <= %d - %d + %d = %d" % (w, w, nc, rJ, rBe, resO[w]['upper']), True)
check("S2.3 O class, weight 0 and 1: NO consistent cubic vertex", resO[0]['upper'] == 0 and resO[1]['upper'] == 0)
check("S2.4 O class, weight 2: consistent cubic vertices form a space of dimension <= 31", resO[2]['upper'] == 31)
print(tm(), flush=True)
cO = OC[2]; repsO = cO['reps']; selSO = cO['selS']; ncO = len(selSO)
rng = random.Random(31337); ngO = ncO + 100
Q, Pm = make_modes(rng, ngO)
WO = eval_S3(repsO, Pm, Q)[:, selSO]
F2reps = reps_F2()
Ev = [np.array([Evec(Q[i][k], vec_to_pol(Pm[i][k]), CFG0) for k in range(ngO)], dtype=np.int64) for i in range(3)]
TO = np.zeros((ngO, len(F2reps)), dtype=np.int64)
for i in range(3):
    j, kk = [xx for xx in range(3) if xx != i]
    TO += eval_F2(F2reps, Pm[j], Pm[kk], Ev[i]) + eval_F2(F2reps, Pm[kk], Pm[j], Ev[i])
rkTO = rank_exact(TO)
ADMO = {mu: np.array([[fmod(adm_cross3(Q, Pm, k, mu))] for k in range(ngO)], dtype=np.int64) for mu in MUTS}
augO = np.hstack([WO % P1, TO % P1] + [ADMO[mu] for mu in MUTS])
RrO, pivO = rref_mod(augO)
check("S2.5 %d O-class F2 patterns give %d independent trivial kernels (exact rank over Q), inside the class; ADM and variants inside the class (rank %d = n_c)" % (len(F2reps), rkTO, ncO), len(pivO) == ncO and rkTO == 30)
ctrO = RrO[:ncO, ncO:ncO + TO.shape[1]].T
cvO = {mu: RrO[:ncO, ncO + TO.shape[1] + i] for i, mu in enumerate(MUTS)}
solO = nullspace_mod(np.hstack([resO[2]['A'], resO[2]['B']]) % P1)[:, :ncO]
dsolO = rank_mod(solO)
check("S2.6 mod-p dimension of the consistent O-space is %d; every trivial vertex is consistent" % dsolO, dsolO == resO[2]['upper'] and rank_mod(np.vstack([solO, ctrO])) == dsolO)
check("S2.7 ADM and its field-redefined variants are consistent; mutated variants are not (O class)",
      in_span(solO, cvO[None]) and in_span(solO, cvO['upperN']) and in_span(solO, cvO['expN']) and (not in_span(solO, cvO['noNinv'])) and (not in_span(solO, cvO['plusK2'])))
rk_trO = rank_mod(ctrO); rk_traO = rank_mod(np.vstack([ctrO, cvO[None][None, :]]))
check("S2.8 ADM is not trivial in the O class: rank[trivial; ADM] = %d = rank[trivial] + 1" % rk_traO, rk_traO == rk_trO + 1 and rk_trO == rkTO)
quotO = resO[2]['upper'] - rkTO
check("S2.9 O class, weight 2: consistent / trivial has dimension <= %d - %d = %d and ADM spans it" % (resO[2]['upper'], rkTO, quotO), quotO == 1)
Ao_b, Bo_b = o_system(2, CFG0, seed=2)
dO_b, rJO_b, rBO_b = count_dim(Ao_b, Bo_b)
check("S2.9b independent second sample (seed 2), O class: same bound %d (mod p ranks %d, %d)" % (dO_b, rJO_b, rBO_b), dO_b == 31)
# cross-check of the two independent code paths: every SO(3) kernel is O-invariant
rng = random.Random(4711); n_x = ncO + 40
modes = rand_modes3(rng, n_x); bmx = batch3(modes)
Qx = [bmx[j][0] for j in range(3)]
Px = [np.array([pol_to_vec(m[j][1]) for m in modes], dtype=np.int64) for j in range(3)]
Wo = eval_S3(repsO, Px, Qx)[:, selSO]
Ws = Wb(S3, bmx)[:, selS] % P1
check("S2.10 cross-check of the two code paths: all %d SO(3)-invariant kernels lie in the span of the %d O-invariant kernels (rank of the union stays %d)" % (nc, ncO, ncO),
      rank_mod(np.hstack([Wo % P1, Ws])) == ncO)
print(tm(), flush=True)

# ---------------- controls on the premises ---------------------------------------------------
print("=== 3. controls on the premises (SO(3) class, weight 2) ===", flush=True)
cfgs = [("alpha=K/2 with the deformed time law du=2 xi0_dot", dict(alpha=F(1, 2), beta=F(-1, 2), tf=2, time_gauge=True)),
        ("alpha=K/4 but ONLY the spatial relabelling required (lapse constraint not required to be preserved)", dict(alpha=F(1, 4), beta=F(-1, 4), tf=1, time_gauge=False)),
        ("beta != -alpha (no time relabelling exists), spatial relabelling only", dict(alpha=F(1, 4), beta=F(-1, 8), tf=1, time_gauge=False))]
ctrl = {}
for name, cfg in cfgs:
    Am2, Bm2 = so3_system(2, cfg)
    dm, rJ2, rB2 = count_dim(Am2, Bm2)
    sol_c = nullspace_mod(np.hstack([Am2, Bm2]) % P1)[:, :nc3]
    ctrl[name] = (dm, in_span(sol_c, cvec[None]), in_span(sol_c, cU2), rank_mod(np.vstack([ctr, cU2[None, :]])) == rkT + 1)
    print("  control:", name, "-> consistent dimension", dm, "; baseline ADM vertex consistent:", ctrl[name][1], flush=True)
nm_ = [n for n, _ in cfgs]
check("S3.1 alpha=K/2 (time law deformed to stay a symmetry): the baseline ADM vertex is NOT consistent with that quadratic action; dimension %d" % ctrl[nm_[0]][0], (not ctrl[nm_[0]][1]) and ctrl[nm_[0]][0] >= 19)
check("S3.2 spatial relabelling only: consistent cubic vertices are more numerous (%d > 19): uniqueness fails if the lapse constraint is not required to survive" % ctrl[nm_[1]][0], ctrl[nm_[1]][0] > 19)
check("S3.2b explicit counterexample when only the shift constraints are kept: ADM + kappa * int u [Hdot_ij Hdot_ij - (tr Hdot)^2] (a lapse-dependent rescaling of the kinetic term) is consistent for spatial relabelling only (Hdot and u are invariant under it), is not a field redefinition, and is NOT consistent once the time relabelling is required",
      ctrl[nm_[1]][2] and ctrl[nm_[1]][3] and (not in_span(sol3, cU2)))
check("S3.3 beta != -alpha, spatial relabelling only: dimension %d > 19" % ctrl[nm_[2]][0], ctrl[nm_[2]][0] > 19)
print(tm(), flush=True)

# ---------------- what the static sector can and cannot see ----------------------------------
print("=== 4. what static (block 60) data can see ===", flush=True)
rng = random.Random(11)
def sc_mode(rng, q):
    s = rng.randint(-3, 3)
    return (q, {'u': np.array(rng.randint(-3, 3), dtype=np.int64), 'N': np.zeros(3, dtype=np.int64), 'h': np.array(2 * s * np.eye(3, dtype=np.int64))})
secres = {}
for label, static in (("static conformal sector (q_t=0, N=0, h=2 phi delta)", True), ("conformal sector with time dependence (N=0, h=2 phi delta, q_t free)", False)):
    pts = []
    for _ in range(120):
        q1 = rnd_vec(rng, -3, 3, 4); q2 = rnd_vec(rng, -3, 3, 4); q0 = -q1 - q2
        if static: q0[0] = q1[0] = q2[0] = 0
        pts.append(tuple(sc_mode(rng, q) for q in (q0, q1, q2)))
    bm_ = batch3(pts); Eb_ = [stack_modes([(p[i][0], Ehat8(p[i][0], p[i][1], CFG0)) for p in pts]) for i in range(3)]
    Tl = np.zeros((len(pts), nF2), dtype=np.int64)
    for i in range(3):
        j, kk = [xx for xx in range(3) if xx != i]
        Tl += Db(F2, bm_[j], bm_[kk], Eb_[i]) + Db(F2, bm_[kk], bm_[j], Eb_[i])
    Ad = [adm_lagrangian([[int(xx) for xx in mm[0]] for mm in p], [to_listpol(mm[1]) for mm in p]).c[7] for p in pts]
    Tmm = Tl % P1; Amm = np.array([[fmod(v)] for v in Ad], dtype=np.int64)
    secres[static] = (rank_mod(Tmm), rank_mod(np.hstack([Tmm, Amm])), bool(Amm.any()))
check("S4.1 ADM cubic vertex restricted to STATIC conformal data (lapse u, conformal factor) is nonzero but equals a local field redefinition there (rank %d -> %d): static data cannot force or normalise the cubic vertex modulo redefinitions" % secres[True][:2],
      secres[True][2] and secres[True][0] == secres[True][1])
check("S4.2 ... with time dependence (conformal sector, N=0) it is NOT removable (rank %d -> %d): moving/time-dependent content carries the physical cubic information" % secres[False][:2],
      secres[False][1] == secres[False][0] + 1)
print(tm(), flush=True)

# ---------------- summary ----------------
npass = sum(RES); nfail = len(RES) - npass
if nfail == 0:
    print("HIT: within the class {local polynomial cubic vertices of (u, N_i, h_ij) with exactly two derivatives (each d_t or d_i), invariant under the 24 proper cubic rotations (and separately under SO(3) with epsilon allowed)}, for the quadratic action of block 144 at alpha=K/4 with its spatial and time relabellings, the vertices admitting a local first-order field-dependent relabelling that keeps the constraint identities at second order form a space of dimension <= 31 (O) / 19 (SO(3)); modulo local derivative-free field redefinitions (dimension 30 / 18) it is exactly one-dimensional and spanned by the cubic part of N sqrt(gamma)(K_ij K^ij - K^2 + R); weight 0 and 1 admit none; dropping the lapse constraint (spatial relabelling only) destroys uniqueness; static conformal data cannot see the vertex mod redefinitions, time-dependent data can; the overall scale is not fixed by vacuum consistency.", flush=True)
print("TOTAL: PASS=%d FAIL=%d" % (npass, nfail), flush=True)
print("SUMMARY: PARTIAL - exact finite classification (CHECKED, not PROVED for all points): in the stated class (two-derivative, local, O or SO(3) invariant, quadratic action of block 144) the consistent cubic vertices are, modulo field redefinitions, the line spanned by the ADM cubic vertex; scale, higher weights, lattice corrections, sources and the equivalence 'constraints preserved' <=> 'local gauge identity' are not proved here. [runtime %.0fs]" % (time.time() - T0), flush=True)
sys.exit(0 if nfail == 0 else 1)
