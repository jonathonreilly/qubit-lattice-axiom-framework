"""Phase C: add alpha(X_x)-locality (range 2) to the c4e_02 matching problem, as UNARY filters
against forced data only, then re-match.

Forced data (independent of the matching): k<=2 images (frozen singles + face glider W) and
spectator images (class D, C4d Lemma S).  Forced X-table TABF: window key (d ∩ B_2(x)) - x -> required
modification (G_x(d) xor d) - x, from every transition (d, x) whose preimage pi^{-1}(d) and source
pi^{-1}(d) xor x are both forced.  A candidate image dimg for a C3 source c is rejected if, for some
x in c (c' = c minus x, e' = W(c') forced), the transitions (e', x) -> dimg or (dimg, x) -> e'
have a modification outside B_2(x) or contradicting TABF.  These rejections are rigorous
consequences of range 2 for monomial QCAs.  Couplings between two free C3 choices are NOT used
here; they are checked afterwards on the re-matched pi with rv_xlocal.py.
Input: logs/candidates_s-1.json (author's admissible F/G/stabiliser candidates, rv_extract_candidates.py).
"""
import os, json, time, itertools
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching
import rv_matching_verify as V
import rv_core as C

HERE = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(HERE, 'logs', 'xfilter.txt'), 'w')
ck = C.Check(f)
t0 = time.time()
J = json.load(open(os.path.join(HERE, 'logs', 'candidates_s-1.json')))
C3 = [frozenset(map(tuple, c)) for c in J['C3']]
cands = [(i, j, frozenset(map(tuple, d))) for i, j, d in J['cands']]
ck.info(f"{len(C3)} sources, {len(cands)} admissible candidate images (author filter), {time.time()-t0:.0f}s")


def cls(c):
    if len(c) <= 2:
        return 'k<=2'
    return 'D' if V.spectator(c) is not None else 'C3'


# forced preimage map: images of k<=2 and D classes
FINV = {}
for c in V.confs:
    if cls(c) == 'C3':
        continue
    d = V.pi(c)
    m0 = min(d)
    FINV[frozenset(C.sub(x, m0) for x in d)] = (c, m0)


def finv(d):
    m = min(d)
    nd = frozenset(C.sub(x, m) for x in d)
    if nd not in FINV:
        return None
    c, m0 = FINV[nd]
    return C.tr(c, C.sub(m, m0))


TABF = {}
bad_forced = 0
nT = 0
for d in V.confs:
    pre = finv(d)
    if pre is None:
        continue
    if len(d) <= 2:
        xs = set()
        for z in set(d) | set(pre):
            for o in itertools.product(range(-6, 7), repeat=3):
                xs.add(C.add(z, o))
    else:
        xs = set(pre)
    for x in xs:
        src = pre ^ {x}
        if cls(src) == 'C3':
            continue
        g = V.pi(src) if src else frozenset()
        mod = frozenset(C.sub(y, x) for y in d ^ g)
        key = tuple(sorted(C.sub(y, x) for y in d if C.cheb(y, x) <= 2))
        nT += 1
        if any(max(map(abs, y)) > 2 for y in mod):
            bad_forced += 1
            continue
        old = TABF.get(key)
        if old is None:
            TABF[key] = mod
        elif old != mod:
            bad_forced += 1
ck(bad_forced == 0, f"forced X-table: {nT} forced transitions, {len(TABF)} keys, internal conflicts/out-of-ball {bad_forced} (0 = forced data alone are X-local)")


def unary_ok(c, dimg):
    for x in c:
        cp = c - {x}
        ep = V.W(cp)
        mod = frozenset(C.sub(y, x) for y in dimg ^ ep)
        if any(max(map(abs, y)) > 2 for y in mod):
            return False
        for dd in (ep, dimg):
            key = tuple(sorted(C.sub(y, x) for y in dd if C.cheb(y, x) <= 2))
            if key in TABF and TABF[key] != mod:
                return False
    return True


surv = [(i, j, d) for (i, j, d) in cands if unary_ok(C3[i], d)]
deg = {}
for i, j, d in surv:
    deg.setdefault(i, set()).add(j)
zero = [i for i in range(len(C3)) if i not in deg]
ck.info(f"candidates surviving X-local unary filter: {len(surv)} of {len(cands)}; orbit edges {sum(len(v) for v in deg.values())}; {time.time()-t0:.0f}s")
ck.info(f"sources with no surviving candidate: {len(zero)}; e.g. {[sorted(C3[i]) for i in zero[:5]]}")
rows = [i for i in deg for j in deg[i]]
cols = [j for i in deg for j in deg[i]]
nt = J['tkeys_n']
M = csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(C3), nt))
match = maximum_bipartite_matching(M, perm_type='column')
size = int((match >= 0).sum())
ck.info(f"maximum matching with X-local unary filter: {size} of {len(C3)}")
if size == len(C3):
    wit = {}
    for i, j, d in surv:
        if j == match[i] and i not in wit:
            wit[i] = d
    out = [{'src': sorted(C3[i]), 'img': sorted(wit[i])} for i in range(len(C3))]
    json.dump(out, open(os.path.join(HERE, 'logs', 'matching_xfiltered_s-1.json'), 'w'))
    ck.info("wrote logs/matching_xfiltered_s-1.json (check full X-locality with MATCHING_JSON=... rv_xlocal.py)")
ck(True, "filter + matching computation completed")
ck.total()
