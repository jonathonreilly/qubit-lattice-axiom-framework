"""Qubit level: pair test for C2 rotations about BOND-centred axes, V = U_R T_a with R a = -a.
V maps hops to rotated hops exactly (U_R does, bare translation does since conventions are translation invariant)."""
import random
from pair import *
from rot import compose

def trans_op(a):
    pi = [None] * C.nq
    for (e, c), q in C.Q.items():
        def tc(cc):
            v, ct = lat.corner_info(cc)
            return lat.corner(add(v, a), ct)
        e2 = frozenset(tc(x) for x in e)
        c2 = None if c is None else tc(c)
        pi[q] = C.Q[(e2, c2)]
    return Op(pi, [], 0)

rng = random.Random(3)
out = {}
for gi, M in enumerate(Ms):
    t = classify(M)
    for a in [(1,0,0),(0,1,0),(0,0,1)]:
        if rot_vec(M, a) != tuple(-x for x in a):
            continue
        V = compose(Uc[gi], trans_op(a))
        # check hop map on a sample
        for e in C.edges[::50]:
            j, k = tuple(e)
            def g(cc):
                v, ct = lat.corner_info(cc)
                return C.rot_corner(M, lat.corner(add(v, a), ct))
            assert V.conj(C.hop(j, k)) == C.hop(g(j), g(k))
        # lattice map in unwrapped coords: x -> R(x + a)
        def vmap(node):
            v, ct = node
            return (rot_vec(M, add(v, a)), frozenset(rot_vec(M, d) for d in ct))
        lams = set()
        cand = [((x, y, z), ct) for x in range(-2, 2) for y in range(-2, 2) for z in range(-2, 2) for ct in CTYPES]
        cand = [q for q in cand if vmap(q) != q and vmap(vmap(q)) == q]
        for q in rng.sample(cand, 8):
            Vq = vmap(q)
            # box must contain q, Vq and be V-invariant: use box [-2,1]^3 shifted appropriately -> use big box and check membership
            path = rand_path(q, Vq, 2, rng, detour=False)
            S = string(path)
            lam = G.member_sign(pmul(pdag(S), V.conj(S)))
            lams.add(lam)
        out.setdefault((t, 'bond-centred, R a = -a'), set()).update(lams)
print(out)
