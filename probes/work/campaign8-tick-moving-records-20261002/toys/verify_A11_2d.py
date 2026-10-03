"""Coordinator check of A11 D1-D3 (written from the statement): 2D 4-sub-step swap cycle on an L x L torus.
A sites: x+y even. Sub-step j swaps each A site a with a + d_j, d = (+x,+y,-x,-y). Pairs containing a locked site are skipped.
Checks: bulk identity away from records; around an s x s locked block, the moved sites form ONE orbit of length 2s+1
that goes once around the block (winding -1, i.e. clockwise); mirror schedule (-x,+y,+x,-y) reverses it."""
import numpy as np
L = 24
def cycle(locked, d):
    perm = {(x, y): (x, y) for x in range(L) for y in range(L)}   # content position after steps: track where each item goes
    pos = {(x, y): (x, y) for x in range(L) for y in range(L)}    # item -> current site
    where = {v: k for k, v in pos.items()}                         # site -> item
    for dx, dy in d:
        new_where = dict(where)
        for x in range(L):
            for y in range(L):
                if (x + y) % 2: continue
                a = (x, y); b = ((x + dx) % L, (y + dy) % L)
                if a in locked or b in locked: continue
                new_where[a], new_where[b] = where[b], where[a]
        where = new_where
    return {item: site for site, item in where.items()}           # item -> final site
def angle(p, c):
    return np.arctan2(p[1] - c[1], p[0] - c[0])
for s in (1, 2, 3, 4):
    x0 = y0 = 10
    locked = {(x0 + i, y0 + j) for i in range(s) for j in range(s)}
    for name, d in (("right-handed", [(1,0),(0,1),(-1,0),(0,-1)]), ("mirror", [(-1,0),(0,1),(1,0),(0,-1)])):
        f = cycle(locked, d)
        moved = [k for k, v in f.items() if k != v and k not in locked]
        far_moved = [k for k in moved if max(min(abs(k[0]-(x0+i)) for i in range(s)), min(abs(k[1]-(y0+j)) for j in range(s))) > 1]
        # orbit structure among moved sites
        seen, orbits = set(), []
        for k in moved:
            if k in seen: continue
            orb, cur = [], k
            while cur not in seen:
                seen.add(cur); orb.append(cur); cur = f[cur]
            orbits.append(orb)
        c = (x0 + (s - 1) / 2, y0 + (s - 1) / 2)
        wind = []
        for orb in orbits:
            tot = 0.0
            for k in orb:
                da = angle(f[k], c) - angle(k, c)
                tot += (da + np.pi) % (2 * np.pi) - np.pi
            wind.append(round(tot / (2 * np.pi), 6))
        print("s=%d %-12s moved=%2d (expect %d) orbits=%s windings=%s moved-far-from-block=%d" %
              (s, name, len(moved), 2 * s + 1, [len(o) for o in orbits], wind, len(far_moved)))
f0 = cycle(set(), [(1,0),(0,1),(-1,0),(0,-1)])
print("no records: bulk identity =", all(k == v for k, v in f0.items()))
