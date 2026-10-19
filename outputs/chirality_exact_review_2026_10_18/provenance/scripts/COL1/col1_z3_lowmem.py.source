"""COL-1 check 5: the token construction with links on Z^3 (one qubit per site, gauge point at every site).

Token at p=(x,y,z) lies along +x, 35 qubits:
  0-2 marker 110 | 3-5 q (3) | 6:0 | 7-9 p (3bar) | 10:0 |
  for k, mu in enumerate(x,y,z):  11+8k..13+8k  A^mu (3bar of SU(3)_p) | 14+8k:0 | 15+8k..17+8k  B^mu (3 of SU(3)_{p+mu}) | 18+8k:0
Pi_p = V(p) AND V(p-35x) AND V(p-y) AND V(p-z)      (the far end of the x-link is the next token in the row;
                                                      y/z links go to the aligned token in the neighbouring row)
G_p = Pi_p [T q_p + Tbar p_p + sum_mu Tbar A^mu_p + T B^x_{p-35x} + T B^y_{p-y} + T B^z_{p-z}] Pi_p
Checks: exact parse lemma (P1/P2, disjoint quantum groups) over all relative displacements with
overlapping supports; register-level gauge invariance of the y-direction pair-creation term.
"""
import itertools, numpy as np, scipy.sparse as sps
from su3common import T, Tbar, F
from parse_lemma import satisfiable, colour_blind, onehot_or_empty

TOK = 35
add = lambda p, d: (p[0] + d[0], p[1] + d[1], p[2] + d[2])
X = lambda n: (n, 0, 0)

def V(p):
    row = lambda o: add(p, X(o))
    cons = [((row(0), row(1), row(2)), {(1, 1, 0)})]
    m = set()
    for q in onehot_or_empty(3):
        for pp in onehot_or_empty(3):
            if sum(q) + sum(pp) <= 1:
                m.add(q + (0,) + pp + (0,))
    cons.append((tuple(row(o) for o in range(3, 11)), m))
    l = set()
    for A in onehot_or_empty(3):
        for B in onehot_or_empty(3):
            if sum(A) == sum(B):
                l.add(A + (0,) + B + (0,))
    for k in range(3):
        cons.append((tuple(row(o) for o in range(11 + 8 * k, 19 + 8 * k)), l))
    return cons

UNIT = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
def far(p, k):          # the token whose B^mu group is the far end of p's mu-link
    return add(p, X(TOK)) if k == 0 else add(p, UNIT[k])
def near(p, k):         # the token whose mu-link ends at p
    return add(p, X(-TOK)) if k == 0 else add(p, tuple(-c for c in UNIT[k]))

def Pi(p):
    return V(p) + V(near(p, 0)) + V(near(p, 1)) + V(near(p, 2))

def grp(p, o):
    return tuple(add(p, X(o + k)) for k in range(3))

def groups(p):
    g = [(grp(p, 3), 'T'), (grp(p, 7), 'Tbar')]
    for k in range(3):
        g.append((grp(p, 11 + 8 * k), 'Tbar'))                 # A^mu_p
        g.append((grp(near(p, k), 15 + 8 * k), 'T'))           # B^mu of the incoming link
    return g

def support(p):
    s = set()
    for pos, _ in Pi(p):
        s.update(pos)
    return s

O = (0, 0, 0)
S0 = support(O)
compatible, fails, sharedq = [], [], []
tested = 0
for dx in range(-2 * TOK - 2, 2 * TOK + 3):
    for dy in (-1, 0, 1):
        for dz in (-1, 0, 1):
            d = (dx, dy, dz)
            if d == O or not (S0 & support(d)):
                continue
            tested += 1
            if satisfiable(Pi(O) + Pi(d)):
                compatible.append(d)
                for g, _ in groups(O):
                    if not colour_blind(g, Pi(d)):
                        fails.append((d, 'Pi_d vs G_0', g))
                for g, _ in groups(d):
                    if not colour_blind(g, Pi(O)):
                        fails.append((d, 'Pi_0 vs G_d', g))
                q0 = set(sum([list(g) for g, _ in groups(O)], []))
                qd = set(sum([list(g) for g, _ in groups(d)], []))
                if q0 & qd:
                    sharedq.append((d, sorted(q0 & qd)))
own = [g for g, _ in groups(O) if not colour_blind(g, Pi(O))]
print("=== Z^3 parse lemma (exact constraint satisfaction)")
print("  support of G_p: %d qubits; displacements with overlapping supports tested: %d" % (len(S0), tested))
print("  jointly satisfiable (compatible) overlapping displacements: %s" % compatible)
print("  P2 failures: %s | own-register failures: %s | quantum groups shared by compatible pairs: %s" % (fails, own, sharedq))

# register-level gauge invariance of the y-direction pair-creation term, with spectators
# registers: m_p (q,p of p: 7 states), link_y of p (A,B: 10 states), m_{p+y} (7), spectator incoming
# x-link far end at p (B^x_{p-35x}: one-hot or empty, 4 states)
mat = [(q, pp) for q in onehot_or_empty(3) for pp in onehot_or_empty(3) if sum(q) + sum(pp) <= 1]
lnk = [(A, B) for A in onehot_or_empty(3) for B in onehot_or_empty(3) if sum(A) == sum(B)]
spec = onehot_or_empty(3)
states = list(itertools.product(range(len(mat)), range(len(lnk)), range(len(mat)), range(len(spec))))
idx = {s: i for i, s in enumerate(states)}
N = len(states)
def vec(oh):
    return None if sum(oh) == 0 else oh.index(1)
def gen_on(kind_slot, M, s):
    """apply M (3x3) to one colour slot of state s; returns list of (state, amp)"""
    mp, l, my, sp_ = s
    out = []
    def put(new):
        out.append(new)
    if kind_slot == 'q_p' or kind_slot == 'p_p' or kind_slot == 'q_y' or kind_slot == 'p_y':
        which = 0 if kind_slot.endswith('_p') else 2
        mi = s[which]; q, pp = mat[mi]
        slot = q if kind_slot.startswith('q') else pp
        j = vec(slot)
        if j is None:
            return []
        res = []
        for i in range(3):
            if abs(M[i, j]) > 0:
                oh = tuple(1 if k == i else 0 for k in range(3))
                newm = (oh, pp) if kind_slot.startswith('q') else (q, oh)
                ns = list(s); ns[which] = mat.index(newm)
                res.append((tuple(ns), M[i, j]))
        return res
    if kind_slot in ('A', 'B'):
        A, B = lnk[l]
        slot = A if kind_slot == 'A' else B
        j = vec(slot)
        if j is None:
            return []
        res = []
        for i in range(3):
            if abs(M[i, j]) > 0:
                oh = tuple(1 if k == i else 0 for k in range(3))
                newl = (oh, B) if kind_slot == 'A' else (A, oh)
                ns = list(s); ns[1] = lnk.index(newl)
                res.append((tuple(ns), M[i, j]))
        return res
    if kind_slot == 'spec':
        j = vec(spec[sp_])
        if j is None:
            return []
        res = []
        for i in range(3):
            if abs(M[i, j]) > 0:
                ns = list(s); ns[3] = i
                res.append((tuple(ns), M[i, j]))
        return res

def build(terms):
    r, c, v = [], [], []
    for s in states:
        for slot, mat_ in terms:
            for t, amp in gen_on(slot, mat_, s):
                r.append(idx[t]); c.append(idx[s]); v.append(amp)
    return sps.csr_matrix((v, (r, c)), shape=(N, N), dtype=complex)

Gp = [build([('q_p', T[a]), ('p_p', Tbar[a]), ('A', Tbar[a]), ('spec', T[a])]) for a in range(8)]
Gy = [build([('q_y', T[a]), ('p_y', Tbar[a]), ('B', T[a])]) for a in range(8)]
Kr, Kc = [], []
empty_m = mat.index(((0, 0, 0), (0, 0, 0))); empty_l = lnk.index(((0, 0, 0), (0, 0, 0)))
for s in states:
    if s[0] == empty_m and s[1] == empty_l and s[2] == empty_m:
        for a in range(3):
            for b in range(3):
                oh = lambda i: tuple(1 if k == i else 0 for k in range(3))
                t = (mat.index((oh(a), (0, 0, 0))), lnk.index((oh(a), oh(b))), mat.index(((0, 0, 0), oh(b))), s[3])
                Kr.append(idx[t]); Kc.append(idx[s])
K = sps.csr_matrix((np.ones(len(Kr)), (Kr, Kc)), shape=(N, N), dtype=complex)
H = K + K.conj().T
mxs = lambda m: float(abs(sps.csr_matrix(m)).max()) if sps.csr_matrix(m).nnz else 0.0
gi = max(mxs(H @ g - g @ H) for g in Gp + Gy)
cr = max(mxs(Gp[a] @ Gy[b] - Gy[b] @ Gp[a]) for a in range(8) for b in range(8))
rel = 0.0
for G in (Gp, Gy):
    for a in range(8):
        for b in range(a + 1, 8):
            rel = max(rel, mxs(G[a] @ G[b] - G[b] @ G[a] - sum(1j * F[a, b, c] * G[c] for c in range(8))))
print("=== register-level y-link algebra (dim %d): su(3) err %.1e | [G_p, G_p+y] %.1e | [K+K^dag, G] %.1e"
      % (N, rel, cr, gi))
