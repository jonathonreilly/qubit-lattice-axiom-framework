"""The cube-inversion rule (C4e candidate construction).

Unit cube K(c) = c + {0,1}^3 (c = lower corner).  A(K) = sites of K with the parity of c
(parity = x+y+z mod 2), B(K) = the other four.  inv_K(z) = 2c + (1,1,1) - z (point inversion
through the cube centre; it maps A(K) <-> B(K) and every face diagonal to the parallel face
diagonal of the opposite face).
A configuration is a finite set of occupied sites (magnons).  Version 'v1':
  candidate(K)  : |conf n A(K)| >= 2
  active(K)     : candidate and no other candidate cube shares a site with K
  F(conf)       : invert every active cube (they are pairwise site-disjoint)
  G = I F I     : I = point inversion z -> -z  (swaps the roles of A and B)
"""
DELTA_EVEN = ((0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1))

def par(z): return (z[0] + z[1] + z[2]) & 1

def candidates(conf, rule='v1'):
    cnt = {}
    for z in conf:
        for d in DELTA_EVEN:   # cubes in which z is an A-site: corner c = z - d with parity(c)=parity(z)
            c = (z[0] - d[0], z[1] - d[1], z[2] - d[2])
            cnt[c] = cnt.get(c, 0) + 1
    return {c for c, n in cnt.items() if n >= 2}

def active(conf, rule='v1'):
    cand = candidates(conf, rule)
    act = set()
    for c in cand:
        ok = True
        for d0 in (-1, 0, 1):
            for d1 in (-1, 0, 1):
                for d2 in (-1, 0, 1):
                    if d0 == d1 == d2 == 0: continue
                    if (c[0] + d0, c[1] + d1, c[2] + d2) in cand: ok = False; break
                if not ok: break
            if not ok: break
        if ok: act.add(c)
    return act

NEI = [(a, b, c) for a in (-1, 0, 1) for b in (-1, 0, 1) for c in (-1, 0, 1) if (a, b, c) != (0, 0, 0)]
CUBE = ((0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1))

def inv_cube(conf, c):
    S = {(c[0]+d[0], c[1]+d[1], c[2]+d[2]) for d in CUBE}
    return frozenset(((2*c[0]+1-z[0], 2*c[1]+1-z[1], 2*c[2]+1-z[2]) if z in S else z) for z in conf)

def neg_conf(conf): return frozenset((-z[0], -z[1], -z[2]) for z in conf)

def gcand_near(conf, c):
    """G-candidates (>=2 B-sites) among cubes sharing a site with cube c, excluding c"""
    # G-candidate of conf at corner k  <=>  F-candidate of -conf at corner -k-(1,1,1)
    nc = candidates(neg_conf(conf))
    return [d for d in NEI if (-(c[0]+d[0])-1, -(c[1]+d[1])-1, -(c[2]+d[2])-1) in nc]

def active_v2(conf):
    cand = candidates(conf)
    act = set()
    for c in cand:
        if any((c[0]+d[0], c[1]+d[1], c[2]+d[2]) in cand for d in NEI): continue
        if gcand_near(inv_cube(conf, c), c): continue
        act.add(c)
    return act

def F(conf, rule='v1'):
    act = active(conf, rule) if rule == 'v1' else active_v2(conf)
    out = set()
    for z in conf:
        img = z
        for d in ((0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)):
            c = (z[0] - d[0], z[1] - d[1], z[2] - d[2])
            if c in act:
                img = (2*c[0] + 1 - z[0], 2*c[1] + 1 - z[1], 2*c[2] + 1 - z[2]); break
        out.add(img)
    return frozenset(out)

def G(conf, rule='v1'):
    return frozenset((-z[0], -z[1], -z[2]) for z in F([(-z[0], -z[1], -z[2]) for z in conf], rule))
