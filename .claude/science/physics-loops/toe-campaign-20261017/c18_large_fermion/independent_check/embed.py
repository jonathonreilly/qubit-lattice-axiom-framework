"""Item 6: O-equivariant placement of the 48 site-local qubits in a 5x5x5 block; free orbits;
ranges of the code's terms in fine units (upper bounds from supports)."""
import itertools
import numpy as np
from model import *

# labels: on-site hop qubits = on-site edge types (unordered corner pairs); link halves = (corner, its direction)
ONS = sorted({tuple(sorted((c1, c2))) for (c1, c2, sh, k) in ETYPES if k == 'o'})
HALF = [(c, a) for c in range(12) for a in CORN[c]]
assert len(ONS) == 24 and len(HALF) == 24
def act(R, lab):
    if lab[0] == 'o': return ('o', tuple(sorted(rot_corner(R, c) for c in lab[1])))
    c, a = lab[1]; return ('h', (rot_corner(R, c), didx(R @ DV[a])))
LABS = [('o', x) for x in ONS] + [('h', x) for x in HALF]
orbs = {}
for l in LABS:
    orbs.setdefault(frozenset(act(R, l) for R in ROTS), None)
print("label orbits:", [len(o) for o in orbs], " all free:", all(len(o) == 24 for o in orbs))

block = list(itertools.product(range(-2, 3), repeat=3))
porb = {}
for p in block:
    o = frozenset(tuple(int(x) for x in R @ np.array(p)) for R in ROTS)
    porb.setdefault(o, p)
free_pt = [rep for o, rep in porb.items() if len(o) == 24]
print("5^3 block: point-orbit sizes", sorted(len(o) for o in porb), "; free orbits with reps", free_pt)
for n in (3,):
    b = list(itertools.product(range(-(n//2), n//2 + 1), repeat=3))
    print(f"{n}^3 block: free point orbits:", [p for p in b if len({tuple(R @ np.array(p)) for R in ROTS}) == 24])

def placement(p_on, p_h, base_on=0, base_h=0):
    pl = {}
    for lab0, p0 in ((('o', ONS[base_on]), p_on), (('h', HALF[base_h]), p_h)):
        for R in ROTS:
            pl[act(R, lab0)] = tuple(int(x) for x in R @ np.array(p0))
    return pl
pl = placement((1, 2, 0), (1, 2, 2))
bij = len(pl) == 48 and len(set(pl.values())) == 48
equiv = all(pl[act(R, l)] == tuple(int(x) for x in R @ np.array(pl[l])) for R in ROTS for l in LABS)
spect = [p for p in block if p not in set(pl.values())]
closed = all(tuple(int(x) for x in R @ np.array(p)) in set(spect) for R in ROTS for p in spect)
print(f"placement (1,2,0)/(1,2,2): bijective {bij}, equivariant {equiv}, spectators {len(spect)}, spectators O-closed {closed}")

# ranges in fine units. Qubit of label l at coarse site v sits at 5v + p(l).
def pos(v, l, pl): return np.array(v) * 5 + np.array(pl[l])
def corner_qubits(v, c):  # qubits of the edges incident to corner c at site v (superset of a BKSF Z-string)
    out = [(v, ('o', x)) for x in ONS if c in x]
    for a in CORN[c]: out.append((v, ('h', (c, a))))
    return out
def far_half(v, c, a):
    w = tuple(int(x) for x in np.array(v) + DV[a]); c2 = cnorm(didx(-DV[a]), [b for b in CORN[c] if b != a][0])
    return (w, ('h', (c2, didx(-DV[a]))))
def extent(qs, pl):
    P = np.array([pos(v, l, pl) for v, l in qs])
    D = P[:, None, :] - P[None, :, :]
    return int(np.abs(D).max()), float(np.sqrt((D**2).sum(-1)).max())
def ranges(pl):
    v0 = (0, 0, 0); r = {}
    # repetition term R = Z Z on the two halves of a link
    r['R (ZZ on link halves)'] = max(extent([(v0, ('h', (c, a))), far_half(v0, c, a)], pl) for c in range(12) for a in CORN[c])
    r['B_q (corner charge)'] = max(extent(corner_qubits(v0, c), pl) for c in range(12))
    r['on-site hop'] = max(extent(corner_qubits(v0, c1) + corner_qubits(v0, c2), pl) for c1, c2 in ONS)
    lh = []
    for c in range(12):
        for a in CORN[c]:
            w, (_, (c2, _)) = far_half(v0, c, a)
            lh.append(extent(corner_qubits(v0, c) + corner_qubits(w, c2), pl))
    r['link hop'] = max(lh)
    # plaquette loop: union over its 4 corners
    pq = []
    for i, j in ((0, 2), (2, 4), (4, 0)):
        d, e = DV[i], DV[j]
        cs = [((0,0,0), cnorm(i, j)), (tuple(d), cnorm(i+1, j)), (tuple(d+e), cnorm(i+1, j+1)), (tuple(e), cnorm(i, j+1))]
        pq.append(extent(sum((corner_qubits(v, c) for v, c in cs), []), pl))
    r['plaquette loop'] = max(pq)
    return r
for k, v in ranges(pl).items(): print(f"   {k:24s}: max Chebyshev / Euclidean extent in fine units = {v[0]} / {v[1]:.2f}")
# dependence on the choice of base image (24 x 24 choices) for the link-half repetition term
vals = []
for bo, bh in itertools.product(range(24), range(24)):
    p2 = placement((1, 2, 0), (1, 2, 2), bo, bh); vals.append(ranges(p2)['plaquette loop'][0])
print("   plaquette-loop Chebyshev extent over all 576 equivariant base choices: min", min(vals), "max", max(vals))
vals = {}
for bo, bh in itertools.product(range(24), range(24)):
    r = ranges(placement((1, 2, 0), (1, 2, 2), bo, bh))
    for k, v in r.items(): vals.setdefault(k, []).append(v[0])
for k, v in vals.items(): print(f"   {k:24s}: Chebyshev extent over the 576 base choices: min {min(v)} max {max(v)}")
