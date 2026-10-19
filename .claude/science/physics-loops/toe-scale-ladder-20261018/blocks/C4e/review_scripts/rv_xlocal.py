"""Phase C: is the matched range-2 3-magnon extension compatible with QCA range 2 for alpha(X_x)?

For a monomial U|c> = e^{i theta}|pi c>, range 2 of alpha = Ad U needs alpha(Z_x) AND alpha(X_x) in
A_{B_2(x)}.  alpha(Z_x) <=> pi^{-1} radius 2 (G-locality, used by c4e_02).  alpha(X_x) acts on the
configuration basis (up to phases) as d -> G_x(d) = pi(pi^{-1}(d) xor {x}); it lies in A_{B_2(x)}
only if the modification G_x(d) xor d is inside B_2(x) and depends only on d ∩ B_2(x).
c4e_02 does not impose this ("X-locality").  We test it on every (d, x) whose G_x(d) stays in the
k <= 3 sector, using the assembled pi (author matching + reviewer W/spectator/equivariance).
"""
import os, itertools, time
import rv_matching_verify as V
import rv_core as C

HERE = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(HERE, 'logs', 'xlocal%s.txt' % V.SUF), 'w')
ck = C.Check(f)
t0 = time.time()
INV = {}
for c in V.confs:
    d = V.pi(c)
    m0 = min(d)
    INV[frozenset(C.sub(x, m0) for x in d)] = (c, m0)


def pinv(d):
    m = min(d)
    nd = frozenset(C.sub(x, m) for x in d)
    if nd not in INV:
        return None
    c, m0 = INV[nd]
    return C.tr(c, C.sub(m, m0))


TAB = {}
viol = []
out_of_ball = []
n = 0
skipped = 0
for d in V.confs:
    k = len(d)
    e = pinv(d)
    if e is None:
        skipped += 1
        continue
    if k <= 2:
        xs = set()
        for z in set(d) | set(e):
            for o in itertools.product(range(-6, 7), repeat=3):
                xs.add(C.add(z, o))
    else:
        xs = set(e)  # only x in pi^{-1}(d): target in 2-sector
    for x in xs:
        src = e ^ {x}
        if len(src) == 0:
            g = frozenset()
        else:
            g = V.pi(src)
        mod = d ^ g
        modr = frozenset(C.sub(y, x) for y in mod)
        if any(max(map(abs, y)) > 2 for y in modr):
            out_of_ball.append((sorted(d), x, sorted(g)))
            continue
        key = tuple(sorted(C.sub(y, x) for y in d if C.cheb(y, x) <= 2))
        n += 1
        old = TAB.get(key)
        if old is None:
            TAB[key] = (modr, d, x)
        elif old[0] != modr:
            viol.append((key, sorted(old[0]), sorted(modr), sorted(old[1]), old[2], sorted(d), x))
ck.info(f"tested {n} (d,x) pairs with G_x(d) in the k<=3 sector, {len(TAB)} window keys; skipped {skipped} d without stored preimage; {time.time()-t0:.0f}s")
ck(not out_of_ball, f"X-locality (a): modification inside B_2(x): {len(out_of_ball)} violations; e.g. {out_of_ball[:2]}")
ck(not viol, f"X-locality (b): modification depends only on d ∩ B_2(x): {len(viol)} conflicts; e.g. {viol[:2]}")
# which classes are involved in violations
inv3 = set()
for (dd, x, g) in out_of_ball:
    src = (pinv(frozenset(map(tuple, dd))) or frozenset()) ^ {x}
    if len(src) == 3 and V.spectator(src) is None:
        inv3.add(V.keyframe(src)[0])
ck.info(f"C3 orbits whose matched image is involved in an out-of-ball violation: {len(inv3)}")


# ---- classify conflicts: are both sides forced (k<=2 or spectator class), or does a free C3 image enter?
def cls(c):
    if len(c) <= 2:
        return 'k<=2'
    return 'D' if V.spectator(c) is not None else 'C3'


def kind_of(d, x):
    # G_x(d) = pi(pi^{-1}(d) xor x): free (matching-dependent) if EITHER the preimage pi^{-1}(d)
    # or the source pi^{-1}(d) xor x is a connected 3-class (C3)
    pre = pinv(frozenset(d)) or frozenset()
    src = pre ^ {x}
    a, b = cls(pre), cls(src)
    return 'C3' if 'C3' in (a, b) else 'forced'


kinds = {}
forced = []
for (key, m_old, m_new, d_old, x_old, d_new, x_new) in viol:
    ka = kind_of(d_old, x_old)
    kb = kind_of(d_new, x_new)
    kk = tuple(sorted((ka, kb)))
    kinds[kk] = kinds.get(kk, 0) + 1
    if 'C3' not in kk:
        forced.append((key, d_old, x_old, d_new, x_new))
ck.info(f"conflict types (source class of the two sides): {kinds}")
ck.info(f"conflicts with BOTH sides forced (k<=2 rule / spectator lemma): {len(forced)}; e.g. {forced[:3]}")
ck.total()
f.close()
