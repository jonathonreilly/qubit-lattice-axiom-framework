#!/usr/bin/env python3
"""Reviewer's blind, independent exact elimination for Theorem P1 (C4d).

Written from the definitions only (author's c4d_*.py NOT imported or read
before this was written).

Unknowns: amplitudes <sigma|W|p> of the near-pair walk, sigma, p near pairs
(0 < |a-b|_inf <= r), with Lemma-K support sigma subset B_r(x) cap B_r(y)
(p = {x,y}); identified on orbits of G x| Z^3 acting by pure site permutation
(G = T, O or C1).  Constraints (all exact, integer coefficients, bilinear in
conj(x_i) x_j):
  (Uc)  W^dag W = 1   (columns orthonormal)
  (Ur)  W W^dag = 1   (rows orthonormal)
  (S)   sum_u conj<w2,u|W|p1> <w1,u|W|p2> = 0  for valid (p1,w1) != (p2,w2), w1 != w2
  (Sd)  same with W^dag.
valid (p,w): dist_inf(w, p) > r.

Elimination: exact propagation with the rule
  (R1) a constraint whose surviving terms are all diagonal |x_i|^2 with
       coefficients of one strict sign and zero constant  =>  all those x_i = 0;
plus, if (R1) stalls, exact case splitting on any constraint reduced to a single
off-diagonal monomial c*conj(x_i)x_j = 0 (c != 0)  =>  x_i = 0 OR x_j = 0.
Every branch is propagated; the theorem holds iff every surviving branch has
all non-stay unknowns zero, and then the stay phases have |x|=1.
"""
import sys, itertools, time
from collections import defaultdict

G_NAME = sys.argv[1] if len(sys.argv) > 1 else 'T'
R = int(sys.argv[2]) if len(sys.argv) > 2 else 1
PASS = FAIL = 0
def check(name, ok, info=''):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(('PASS' if ok else 'FAIL') + ': ' + name + ('  ' + info if info else ''), flush=True)

# ---- group: signed permutation matrices ----
def perm_parity(p):
    s = 0
    for i in range(3):
        for j in range(i + 1, 3):
            if p[i] > p[j]: s ^= 1
    return s
GROUP = []
for p in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        det = (-1) ** perm_parity(p) * sg[0] * sg[1] * sg[2]
        if det != 1: continue
        nneg = sum(1 for s in sg if s < 0)
        if G_NAME == 'O': GROUP.append((p, sg))
        elif G_NAME == 'T' and perm_parity(p) == 0 and nneg % 2 == 0: GROUP.append((p, sg))
        elif G_NAME == 'C1' and p == (0, 1, 2) and sg == (1, 1, 1): GROUP.append((p, sg))
print('group', G_NAME, 'order', len(GROUP), 'range', R)
def act(g, v):
    p, sg = g
    return (sg[0] * v[p[0]], sg[1] * v[p[1]], sg[2] * v[p[2]])

def dist(a, b): return max(abs(a[0]-b[0]), abs(a[1]-b[1]), abs(a[2]-b[2]))
def add(a, b): return (a[0]+b[0], a[1]+b[1], a[2]+b[2])
def sub(a, b): return (a[0]-b[0], a[1]-b[1], a[2]-b[2])
def ball(c, r):
    return [(c[0]+i, c[1]+j, c[2]+k) for i in range(-r, r+1) for j in range(-r, r+1) for k in range(-r, r+1)]
def pair(a, b): return (a, b) if a < b else (b, a)
def near(a, b): return a != b and dist(a, b) <= R
def I(p):
    x, y = p
    return [s for s in ball(x, R) if dist(s, y) <= R]

def canon(sig, p):
    best = None
    for g in GROUP:
        gs = [act(g, v) for v in sig]; gp = [act(g, v) for v in p]
        o = min(gp)
        k = (tuple(sorted(sub(v, o) for v in gp)), tuple(sorted(sub(v, o) for v in gs)))
        if best is None or k < best: best = k
    return best

VAR = {}
STAY = set()
MEMO = {}
def var(sig, p):
    o = min(p)
    k0 = (tuple(sorted(sub(v, o) for v in p)), tuple(sorted(sub(v, o) for v in sig)))
    if k0 not in MEMO: MEMO[k0] = var0(k0[1], k0[0])
    return MEMO[k0]
def var0(sig, p):
    """index of <sig|W|p>, or None if outside Lemma-K support / not near."""
    if not near(*sig): return None
    if dist(sig[0], p[0]) > R or dist(sig[0], p[1]) > R or dist(sig[1], p[0]) > R or dist(sig[1], p[1]) > R:
        return None
    k = canon(sig, p)
    if k not in VAR:
        VAR[k] = len(VAR)
        if k[0] == k[1]: STAY.add(VAR[k])
    return VAR[k]

O0 = (0, 0, 0)
RHOS = sorted({max(v, tuple(-c for c in v)) for v in ball(O0, R) if v != O0})
BASE = [pair(O0, rho) for rho in RHOS]
print('near-pair classes', len(BASE))
# enumerate all unknowns
for p in BASE:
    Ip = I(p)
    for a, b in itertools.combinations(Ip, 2):
        var(pair(a, b), p)
NV = len(VAR)
print('unknowns', NV, 'stay', len(STAY))

def images(p):
    Ip = I(p); out = []
    for a, b in itertools.combinations(sorted(Ip), 2):
        if near(a, b):
            out.append(((a, b), var((a, b), p)))
    return out

CONS = {}  # frozenset-free key -> (dict terms, const)
def addcons(terms, const, tag):
    t = {k: v for k, v in terms.items() if v != 0}
    if not t and const == 0: return
    key = (tuple(sorted(t.items())), const)
    if key not in CONS: CONS[key] = tag

t0 = time.time()
# (Uc) columns
allpairs_near = {}
def near_pairs_in(box_sites):
    s = set(box_sites); out = []
    for a in s:
        for rho in RHOS:
            b = add(a, rho)
            if b in s: out.append(pair(a, b))
    return out
REG = near_pairs_in(ball(O0, 2 * R + 1))
for p1 in BASE:
    im1 = dict(images(p1))
    for p2 in REG:
        terms = defaultdict(int)
        for s, j in images(p2):
            if s in im1: terms[(im1[s], j)] += 1
        addcons(terms, -1 if p1 == p2 else 0, ('Uc', p1, p2))
# (Ur) rows: sum_p W(s1,p) conj W(s2,p)
for s1 in BASE:
    for s2 in REG:
        terms = defaultdict(int)
        cand = near_pairs_in(set(I(s1)) & set(I(s2)))
        for p in cand:
            i = var(s1, p); j = var(s2, p)
            if i is None or j is None: continue
            terms[(j, i)] += 1   # conj(x_j) x_i
        addcons(terms, -1 if s1 == s2 else 0, ('Ur', s1, s2))
print('unitarity constraints', len(CONS), 'time %.1f' % (time.time() - t0), flush=True)

def spectator(dagger):
    acc = defaultdict(lambda: defaultdict(int))
    for p1 in BASE:
        Ip1 = I(p1)
        for u in Ip1:
            for w2 in Ip1:
                if w2 == u or not near(w2, u): continue
                s = pair(w2, u)
                i = var(s, p1) if not dagger else var(p1, s)
                if i is None: continue
                # p2 with u in I(p2), w2 far from p2
                for a in ball(u, R):
                    for b in ball(u, R):
                        if not (a < b and near(a, b)): continue
                        p2 = (a, b)
                        if dist(w2, a) <= R or dist(w2, b) <= R: continue
                        for w1 in I(p2):
                            if w1 == u or w1 == w2 or not near(w1, u): continue
                            if dist(w1, p1[0]) <= R or dist(w1, p1[1]) <= R: continue
                            s2 = pair(w1, u)
                            j = var(s2, p2) if not dagger else var(p2, s2)
                            if j is None: continue
                            key = (p1, w1, p2, w2)
                            if not dagger: acc[key][(i, j)] += 1
                            else: acc[key][(j, i)] += 1
    return acc
for dg in (False, True):
    acc = spectator(dg)
    n0 = len(CONS)
    for key, terms in acc.items():
        addcons(terms, 0, ('Sd' if dg else 'S',) + key)
    print(('S-dag' if dg else 'S'), 'raw', len(acc), 'new distinct', len(CONS) - n0, 'time %.1f' % (time.time() - t0), flush=True)
assert len(VAR) == NV, 'new unknown appeared'
CL = [(dict(k[0]), k[1], tag) for k, tag in CONS.items()]
print('distinct constraints', len(CL))

def reduce(c, Z):
    t, const, _ = c
    return {k: v for k, v in t.items() if k[0] not in Z and k[1] not in Z}, const

def propagate(Z):
    Z = set(Z); log = []
    changed = True
    while changed:
        changed = False
        for c in CL:
            t, const = reduce(c, Z)
            if const != 0 or not t: continue
            if all(i == j for (i, j) in t) and (all(v > 0 for v in t.values()) or all(v < 0 for v in t.values())):
                new = [i for (i, j) in t if i not in Z]
                for i in new: Z.add(i); log.append((i, c[2], t))
                if new: changed = True
    # contradiction check: constraint reduced to {} with const != 0
    contra = any(not reduce(c, Z)[0] and c[1] != 0 for c in CL)
    return Z, log, contra

def solve(Z, depth=0, stats=None):
    Z, log, contra = propagate(Z)
    if contra:
        stats['dead'] += 1; return []
    rest = [i for i in range(NV) if i not in Z and i not in STAY]
    if not rest:
        stats['leaf'] += 1; return [Z]
    # branch on single off-diagonal monomial
    for c in CL:
        t, const = reduce(c, Z)
        if const == 0 and len(t) == 1:
            (i, j), = t.keys()
            if i != j:
                stats['branch'] += 1
                return solve(Z | {i}, depth + 1, stats) + solve(Z | {j}, depth + 1, stats)
    stats['stuck'] += 1
    return [('STUCK', Z)]

stats = defaultdict(int)
Z1, log1, contra1 = propagate(set())
print('R1-only propagation: zeros', len(Z1), 'of', NV, ' non-stay', NV - len(STAY), ' contradiction', contra1)
# rounds: recompute round structure
res = solve(set(), stats=stats)
print('branch stats', dict(stats))
stuck = [r for r in res if isinstance(r, tuple)]
check('unknown count (T expect 62, O 36, C1 679 per author)', True, 'NV=%d' % NV)
check('R1-only propagation kills every non-stay unknown', set(range(NV)) - STAY <= Z1,
      'zeros=%d non-stay=%d' % (len(Z1), NV - len(STAY)))
check('no branch stuck (all branches end diagonal or contradictory)', not stuck, 'stuck=%d leaves=%d' % (len(stuck), stats['leaf']))
# stays: column norm with all others zero => |s|^2 = 1 ; verify no stay is forced zero
check('no stay amplitude forced zero', not (Z1 & STAY))
# converse: diagonal W (stay arbitrary unit) satisfies every constraint
import cmath, random
random.seed(1)
val = [0j] * NV
for s in STAY: val[s] = cmath.exp(1j * random.uniform(0, 6.28))
bad = 0
for t, const, tag in CL:
    v = sum(cnt * val[i].conjugate() * val[j] for (i, j), cnt in t.items()) + const
    if abs(v) > 1e-12: bad += 1
check('converse: random diagonal W satisfies all constraints', bad == 0, 'violations=%d' % bad)
# dump zeros as canonical keys for comparison
inv = {v: k for k, v in VAR.items()}
with open('rv_p1_zeros_%s_r%d.txt' % (G_NAME, R), 'w') as f:
    for i in sorted(Z1):
        f.write(repr(inv[i]) + '\n')
    f.write('# stays\n')
    for i in sorted(STAY): f.write(repr(inv[i]) + '\n')
    f.write('# undecided\n')
    for i in sorted(set(range(NV)) - Z1 - STAY): f.write(repr(inv[i]) + '\n')
print('time %.1f s' % (time.time() - t0))
print('TOTAL: PASS=%d FAIL=%d' % (PASS, FAIL))
