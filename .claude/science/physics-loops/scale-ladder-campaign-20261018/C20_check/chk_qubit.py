"""Independent Pauli-algebra check of the C20 qubit build (claim A), using only the code definitions of the C17 module
(qubit layout, hop operators A, vertex parities B, stabilizer generators) and the fermion gauge u.
Own: Pauli product/phase, stabilizer row reduction (lowest-bit echelon, ascending sweep), randomized DFS paths
(different from the runner's BFS), Wilson loops along random paths, and product (not only commutator) relations."""
import sys, random, os
import numpy as np
from chk_common import load, R as RUN
sys.setrecursionlimit(100000)
Mdl, X, Mm, seeds = load()
import corner_fermion_qubit_code_genuine_cube_rotation_action_spin_half_class_2026_10_17 as qc
argv = sys.argv; sys.argv = ['qcode', '4', '1011']; qc.FAIL = 0
try: qc._run_reviewed_program()
except SystemExit: pass
finally: sys.argv = argv
NQ = qc.NQ
random.seed(77)

# ---- own Pauli algebra: (x, z, p) = i^p X^x Z^z
def mul(a, b):
    return (a[0] ^ b[0], a[1] ^ b[1], (a[2] + b[2] + 2 * (bin(a[1] & b[0]).count('1') & 1)) % 4)
def commutes(a, b):
    return (bin(a[0] & b[1]).count('1') + bin(a[1] & b[0]).count('1')) % 2 == 0

class Stab:
    def __init__(self): self.rows = {}; self.order = []
    def key(self, P): return P[0] | (P[1] << NQ)
    def low(self, v): return (v & -v).bit_length() - 1
    def reduce(self, P):
        v = self.key(P); acc = P
        for c in self.order:                         # ascending pivots; rows only touch higher bits
            if (v >> c) & 1:
                rv, rP = self.rows[c]; v ^= rv; acc = mul(acc, rP)
        return v, acc
    def add(self, P):
        v, acc = self.reduce(P)
        if v == 0: return 'dep', acc[2] % 4
        c = self.low(v); self.rows[c] = (v, acc)
        self.order = sorted(self.rows); return 'new', None

S = Stab()
gens = [qc.Rop(v, h) for v in qc.SITES for h in qc.HALF if sum(h[1]) > 0] + \
       [qc.loop_op(seq, qc.FLUX[kind]) for kind, seq in qc.cycles()]
inconsistent = 0
for P in gens:
    r = S.add(P)
    if r[0] == 'dep' and r[1] != 0: inconsistent += 1
print('local stabilizer generators:', len(gens), 'rank', len(S.rows), 'inconsistent', inconsistent)

dl_index = {(v, c): i for i, (v, c) in enumerate(Mdl['VERTS'])}
def u_sign(q, r):
    a = dl_index[(q[0], frozenset(q[1]))]; b = dl_index[(r[0], frozenset(r[1]))]
    return (-1) ** int(Mdl['u'][Mdl['C']['EID'][frozenset((a, b))]])
NB = {q: [nb for _, _, nb in qc.INC[q]] for q in qc.VERTS}
def rpath(src, dst, maxlen=40):
    """random walk biased toward dst (simple path), via randomized greedy BFS on shuffled neighbours"""
    from collections import deque
    prev = {src: None}; dq = deque([src])
    while dq:
        x = dq.popleft()
        if x == dst: break
        nbs = NB[x][:]; random.shuffle(nbs)
        for nb in nbs:
            if nb not in prev: prev[nb] = x; dq.append(nb)
    p = [dst]
    while p[-1] != src: p.append(prev[p[-1]])
    return p[::-1]
def detour_path(src, dst):
    mid = random.choice(qc.VERTS)
    p1 = rpath(src, mid); p2 = rpath(mid, dst)
    return p1 + p2[1:]                               # a walk (may revisit vertices; fine for a product of hops)

def hop_string(p):
    n = len(p) - 1; P = (0, 0, n % 4); sgn = 1
    for i in range(n): P = mul(P, qc.A(p[i], p[i + 1])); sgn *= u_sign(p[i], p[i + 1])
    return P, sgn
# Wilson loops along a random noncontractible walk; then a second random walk in the same class must be dependent (+)
def wilson(a, seed):
    random.seed(seed)
    c0 = [c for c in qc.CORN if a not in c and qc.neg(a) not in c][random.randrange(2)]
    q = ((0, 0, 0), c0); seq = [q]
    for step in range(qc.L):
        nxt = (tuple((x + y) % qc.L for x, y in zip(q[0], a)), c0); seq += rpath(q, nxt)[1:]; q = nxt
    P, sgn = hop_string(seq)
    if sgn < 0: P = (P[0], P[1], (P[2] + 2) % 4)
    return P
for a in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
    W = wilson(a, 1); print('Wilson', a, S.add(W))
    W2 = wilson(a, 2); print('   second random Wilson loop in the same class:', S.add(W2), '(dep, 0) expected')

# ---- operators as dict {(x,z): coef}, reduced to canonical form on the code space (right action)
def op(P, c=1.0): return {(P[0], P[1]): c * 1j ** P[2]}
def omul(A, B):
    out = {}
    for (x1, z1), c1 in A.items():
        for (x2, z2), c2 in B.items():
            P = mul((x1, z1, 0), (x2, z2, 0)); k = (P[0], P[1]); out[k] = out.get(k, 0) + c1 * c2 * 1j ** P[2]
    return out
def oadd(*terms):
    out = {}
    for s, A in terms:
        for k, v in A.items(): out[k] = out.get(k, 0) + s * v
    return out
def canon(A):
    out = {}
    for (x, z), c in A.items():
        v, acc = S.reduce((x, z, 0))
        k = (acc[0], acc[1]); out[k] = out.get(k, 0) + c * 1j ** acc[2]
    return {k: v for k, v in out.items() if abs(v) > 1e-9}
ONE = {(0, 0): 1.0}
def n_(q): return oadd((0.5, ONE), (-0.5, op(qc.Bop(q))))
def hop(q, r, p=None):
    p = p or detour_path(q, r); P, sgn = hop_string(p)
    G = op(P, 1.0 / sgn)
    return omul(omul(oadd((1, ONE), (1, op(qc.Bop(q)))), G), oadd((1, ONE), (-1, op(qc.Bop(r))))) if False else \
        {k: v / 4 for k, v in omul(omul(G, oadd((1, ONE), (1, op(qc.Bop(q))))), oadd((1, ONE), (-1, op(qc.Bop(r))))).items()}
def dag(A):
    out = {}
    for (x, z), c in A.items():
        out[(x, z)] = out.get((x, z), 0) + np.conj(c) * (-1) ** (bin(x & z).count('1') & 1)
    return out
def zero(A): return len(canon(A)) == 0

V = qc.VERTS
res = dict(herm=0, prod=0, loop=0, back=0, stab=0, n=0)
for t in range(12):
    a, b, c = random.sample(V, 3)
    Hab = hop(a, b); Hba = hop(b, a); Hbc = hop(b, c); Hac = hop(a, c); Hca = hop(c, a)
    res['herm'] += zero(oadd((1, dag(Hab)), (-1, Hba)))
    # c+_a c_b c+_b c_c = c+_a c_c (1 - n_b)
    res['prod'] += zero(oadd((1, omul(Hab, Hbc)), (-1, omul(Hac, oadd((1, ONE), (-1, n_(b)))))))
    # c+_a c_b c+_b c_c c+_c c_a = n_a (1 - n_b)(1 - n_c)
    lhs = omul(omul(Hab, Hbc), Hca)
    rhs = omul(omul(n_(a), oadd((1, ONE), (-1, n_(b)))), oadd((1, ONE), (-1, n_(c))))
    res['loop'] += zero(oadd((1, lhs), (-1, rhs)))
    # c+_a c_b c+_b c_a = n_a (1 - n_b)
    res['back'] += zero(oadd((1, omul(Hab, Hba)), (-1, omul(n_(a), oadd((1, ONE), (-1, n_(b)))))))
    # every Pauli of the image commutes with every stabilizer row
    res['stab'] += all(commutes((x, z, 0), rP) for (x, z) in Hab for (_, rP) in random.sample(list(S.rows.values()), 300))
    res['n'] += 1
print('sampled (random walk paths incl. detours through random vertices):', res)
# negative control: dropping the fermion gauge sign along the path must break the loop relation on some samples
bad = 0
for t in range(8):
    a, b, c = random.sample(V, 3)
    def hop_nogauge(q, r):
        p = detour_path(q, r); P, _ = hop_string(p); G = op(P)
        return {k: v / 4 for k, v in omul(omul(G, oadd((1, ONE), (1, op(qc.Bop(q))))), oadd((1, ONE), (-1, op(qc.Bop(r))))).items()}
    lhs = omul(omul(hop_nogauge(a, b), hop_nogauge(b, c)), hop_nogauge(c, a))
    rhs = omul(omul(n_(a), oadd((1, ONE), (-1, n_(b)))), oadd((1, ONE), (-1, n_(c))))
    bad += not zero(oadd((1, lhs), (-1, rhs)))
print('negative control (gauge sign dropped): loop relation fails on', bad, '/ 8 samples (expect > 0)')
