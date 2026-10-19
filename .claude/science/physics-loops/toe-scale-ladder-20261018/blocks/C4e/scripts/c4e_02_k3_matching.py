#!/usr/bin/env python3
"""C4e-02: exact 3-magnon test for MONOMIAL range-2 QCAs carrying the face glider.

Premise (monomial): U|c> = e^{i theta(c)} |pi(c)>.  Then pi and pi^{-1} are reversible cellular
automata of radius 2 (alpha(Z_x) is diagonal, = Z at pi-image, and supported in B_2(x)).  So
pi(c)_x = f(c|B_2(x)), pi^{-1}(d)_y = g(d|B_2(y)).  Given frozen singles and the pair map W
(face pairs glide with speed 1, every other pair fixed), f and g are KNOWN on every window holding
<= 2 magnons.  Hence on the 3-magnon sector:
  * if some magnon z has dist(z, c\\z) > 2 (class D), pi(c) = W(c\\z) u {z}   (spectator);
  * otherwise (c connected, class C3), pi(c) = known1(c) u Y,  Y a subset of X(c) = cap_z B_2(z),
    where known1(c) = sites outside X(c) whose (<=2-magnon) window is mapped to 1.
Every f-value on a 3-magnon window belongs to exactly one translation class of C3 configurations,
so the unknowns of different classes are independent.  Therefore: a monomial QCA (restricted to
k <= 3) exists iff there is a T x| Z^3-equivariant bijection from C3 onto
  TARGET = (C3 \\ pi(D))  u  {d in D : pi^{-1}(d) in C3}
whose edges c -> d satisfy F-locality (above), G-locality (same with pi^{-1}, W^{-1}) and
Stab(c) = Stab(d).  Equivariant bijection  <=>  perfect matching between ORBITS (equal
stabilisers make every orbit-level edge a legitimate equivariant choice).
Usage: c4e_02_k3_matching.py  [s=-1]
"""
import sys, itertools, time, json, os
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching
sys.path.insert(0, os.path.dirname(__file__))
from c4e_common import *

s = int(sys.argv[1]) if len(sys.argv) > 1 else -1
R = R_RANGE
PASS = FAIL = 0
def check(name, ok, info=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(('PASS' if ok else 'FAIL') + ': ' + name + (('  ' + info) if info else ''), flush=True)

def spectators(c):
    return [z for z in c if dset(z, [y for y in c if y != z]) > R]

def F_D(c, inverse=False):
    sp = spectators(c); z = sp[0]
    rest = [y for y in c if y != z]
    return frozenset(W(rest, s, inverse)) | {z}

def Xset(c):
    out = None
    for z in c:
        b = set(ball(z))
        out = b if out is None else out & b
    return out

def known1(c, inverse=False):
    X = Xset(c); k1 = set(); N = set()
    for z in c: N |= set(ball(z))
    for x in N - X:
        subc = [z for z in c if dist(x, z) <= R]
        if x in F_small(subc, s, inverse): k1.add(x)
    return frozenset(k1), X

t0 = time.time()
# ---- enumerate C3 orbits (connected 3-configs; diameter <= 4)
orb = {}
O = (0, 0, 0)
box = [v for v in itertools.product(range(-4, 5), repeat=3) if v > O]
for i, a in enumerate(box):
    for b in box[i + 1:]:
        c = (O, a, b)
        if dist(a, b) > 4: continue
        if spectators(c): continue
        k = canon(c)
        if k not in orb: orb[k] = frozenset(c)
C3 = list(orb.values())
C3key = {canon(c): i for i, c in enumerate(C3)}
print('C3 orbits:', len(C3), ' (%.0fs)' % (time.time() - t0), flush=True)

def is_conn(d): return not spectators(d)

# ---- D-part bookkeeping: pi(D) n C3, and D-targets {d in D : G_D(d) in C3}
faces = sorted({tuple(sorted((O, r))) for r in itertools.product((-1, 0, 1), repeat=3) if is_face(r)})
FD_C3 = {}      # canon(d) -> d   for d connected and d = pi(c0), c0 in D
DT = {}         # canon(d) -> d   for d in D with pi^{-1}(d) connected
dpart_ok = True
for p in faces:
    for z in itertools.product(range(-5, 6), repeat=3):
        if z in p: continue
        if dset(z, p) <= R: continue
        c0 = frozenset(p) | {z}
        d = F_D(c0)                       # pi(c0)
        # consistency: pi^{-1} on pi(c0) must return c0
        if is_conn(d):
            FD_C3.setdefault(canon(d), d)
        else:
            if F_D(d, inverse=True) != c0: dpart_ok = False
        # D-targets: d' = W^{-1}-preimage side
        e = frozenset(W(list(p), s, True)) | {z}   # pi^{-1}(c0) treating c0 as an image
        if is_conn(e):
            DT.setdefault(canon(c0), c0)
check('D-part of the 3-sector is self-consistent (pi^{-1} pi = id on spectator configs)', dpart_ok)
print('orbits: |pi(D) n C3| = %d, |D-targets| = %d' % (len(FD_C3), len(DT)))

def in_FD(d):
    # d = pi(c0) with c0 in D  <=> exists z0 in d with c0 = W^{-1}(d\\z0) u z0 having z0 spectator
    for z0 in d:
        rest = [y for y in d if y != z0]
        c0 = frozenset(W(rest, s, True)) | {z0}
        if dset(z0, [y for y in c0 if y != z0]) > R: return True
    return False

# consistency of pi(D) n C3 with G-locality: G must be local on those d too
gl_ok = True
for k, d in FD_C3.items():
    # its preimage
    pre = None
    for z0 in d:
        rest = [y for y in d if y != z0]
        c0 = frozenset(W(rest, s, True)) | {z0}
        if dset(z0, [y for y in c0 if y != z0]) > R: pre = c0
    k1g, Xd = known1(d, True)
    if not (k1g <= pre and pre <= (k1g | Xd)): gl_ok = False
check('images pi(D) that are connected are G-local (pi^{-1} known there is radius-2 compatible)', gl_ok)

# ---- targets
targets = {}
for k, d in orb.items():
    if k not in FD_C3: targets[k] = d
for k, d in DT.items(): targets[k] = d
tkeys = list(targets); tindex = {k: j for j, k in enumerate(tkeys)}
print('sources (C3 orbits): %d   targets: %d' % (len(C3), len(targets)), flush=True)
check('orbit count balance |sources| == |targets|', len(C3) == len(targets))

# ---- edges
rows, cols = [], []
nedge = 0; ncand = 0
stats = []
for i, c in enumerate(C3):
    k1, X = known1(c)
    need = 3 - len(k1)
    stc = stabiliser(c)
    E = set()
    if need >= 0:
        Xl = sorted(X)
        for Y in itertools.combinations(Xl, need):
            d = k1 | frozenset(Y)
            ncand += 1
            # G-locality
            if is_conn(d):
                if in_FD(d): continue
                k1g, Xd = known1(d, True)
                if not (k1g <= c and c <= (k1g | Xd)): continue
            else:
                if in_FD(d): continue
                if F_D(d, inverse=True) != c: continue
            if stabiliser(d) != stc: continue
            kd = canon(d)
            if kd not in tindex:
                print('WARNING: edge to non-target', sorted(c), sorted(d)); continue
            E.add(tindex[kd])
    for j in E: rows.append(i); cols.append(j)
    stats.append(len(E))
    if i % 200 == 0: print('  source %d/%d  cand so far %d  (%.0fs)' % (i, len(C3), ncand, time.time() - t0), flush=True)
print('candidate images examined: %d; orbit edges: %d' % (ncand, len(rows)))
zero_deg = [i for i, n in enumerate(stats) if n == 0]
print('sources with NO admissible image: %d' % len(zero_deg))
for i in zero_deg[:10]: print('   e.g.', sorted(C3[i]))
M = csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(C3), len(targets)))
match = maximum_bipartite_matching(M, perm_type='column')
size = int((match >= 0).sum())
print('maximum matching size: %d of %d' % (size, len(C3)))
tdeg = np.asarray((M > 0).sum(axis=0)).ravel()
print('targets with no admissible preimage: %d' % int((tdeg == 0).sum()))
for j in np.where(tdeg == 0)[0][:10]: print('   e.g.', sorted(targets[tkeys[j]]))
exists = (size == len(C3) == len(targets))
print('RESULT: equivariant monomial 3-sector extension %s' % ('EXISTS' if exists else 'DOES NOT EXIST'))
# save
json.dump({'s': s, 'sources': len(C3), 'targets': len(targets), 'matching': size,
           'zero_deg_sources': [sorted(C3[i]) for i in zero_deg],
           'zero_deg_targets': [sorted(targets[tkeys[j]]) for j in np.where(tdeg == 0)[0]]},
          open(os.path.join(os.path.dirname(__file__), '..', 'logs', 'c4e_02_k3_data_s%d.json' % s), 'w'))
check('exact matching computation completed', True, 'exists=%s' % exists)
print('TOTAL: PASS=%d FAIL=%d' % (PASS, FAIL))
