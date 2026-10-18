"""C4c-01: two-magnon kinematics of a range-r, one-qubit, TI, U(1) QCA with frozen singles.

(a) count of near-pair relative positions d_r (13 at r=1, 62 at r=2);
(b) the support relation c ~ c' (all four cross distances <= r) that W(K) and W(K)^dag obey
    (NOTE.md Lemma K) and that it ALLOWS centre-of-mass motion (so no kinematic no-go);
(c) monomial (basis-permuting x phases) QCAs: for every near pair c, list the images c' ~ c that
    are fixed by Stab_G(c) in the space group G x Z^3 (G = T for the axis action, G = O for the
    full action); if all such c' have COM(c') = COM(c) the pair is frozen.
"""
import itertools
import numpy as np
from c4c_common import check, total, O, T, cheb


def near_reps(r):
    reps = []
    for rho in itertools.product(range(-r, r + 1), repeat=3):
        if rho == (0, 0, 0):
            continue
        nz = [v for v in rho if v != 0][0]
        if nz > 0:
            reps.append(rho)
    return reps


def canon(c):
    return tuple(sorted(tuple(int(v) for v in p) for p in c))


def near(c, r):
    a, b = c
    return 0 < cheb(a, b) <= r


def related(c, d, r):
    return all(cheb(p, q) <= r for p in c for q in d)


def stab(c, G):
    """space-group elements (R,t) with R c + t = c (setwise)."""
    out = []
    a, b = [np.array(p) for p in c]
    for R in G:
        for (u, v) in ((a, b), (b, a)):
            t = u - R @ a          # R a + t = u
            if np.array_equal(R @ b + t, v):
                out.append((R, t))
    return out


def act(g, c):
    R, t = g
    return canon([R @ np.array(p) + t for p in c])


for r in (1, 2):
    reps = near_reps(r)
    d = len(reps)
    check(f"r={r}: number of near-pair relative positions d_r = ((2r+1)^3-1)/2",
          d == ((2 * r + 1) ** 3 - 1) // 2, f"d_{r} = {d}")

# (b) relation and COM motion at r = 1
r = 1
c0 = canon([(0, 0, 0), (1, 0, 0)])
box = [p for p in itertools.product(range(-2, 3), repeat=3)]
cands = [canon([p, q]) for p, q in itertools.combinations(box, 2)]
rel = [c for c in set(cands) if near(c, r) and related(c, c0, r)]
moving = [c for c in rel if not np.array_equal(np.sum(c, 0), np.sum(c0, 0))]
print("r=1: pairs c' ~ {0,e1}:", len(rel), " of which with different COM:", len(moving))
check("r=1: kinematics allows COM motion (e.g. {0,e1} ~ {e2,e1+e2})",
      canon([(0, 1, 0), (1, 1, 0)]) in rel and len(moving) > 0)

# (c) monomial certificate
for r in (1, 2):
    for Gname, G in (("T (axis action)", T), ("O (full action)", O)):
        reps = near_reps(r)
        free = []
        for rho in reps:
            c = canon([(0, 0, 0), rho])
            St = stab(c, G)
            loc = [p for p in itertools.product(range(-2 * r, 2 * r + 2), repeat=3)]
            cand = set()
            for p in loc:
                for q in loc:
                    if p < q:
                        cc = canon([p, q])
                        if near(cc, r) and related(cc, c, r):
                            cand.add(cc)
            fixed = [cc for cc in cand if all(act(g, cc) == cc for g in St)]
            mov = [cc for cc in fixed if not np.array_equal(np.sum(cc, 0), np.sum(c, 0))]
            if mov:
                free.append((rho, len(St), mov))
        if r == 1:
            check(f"r=1, G={Gname}: every Stab-fixed image of every near pair has the same COM "
                  "(monomial U(1) QCAs freeze pairs)", len(free) == 0,
                  f"{len(free)} exceptional relative positions")
        else:
            print(f"r=2, G={Gname}: relative positions whose stabiliser allows a COM-moving "
                  f"monomial image: {len(free)}")
            for rho, ns, mov in free:
                dcom = sorted(set(tuple((np.sum(m, 0) - np.array(rho)).tolist()) for m in mov))
                print(f"   rho={rho} |Stab|={ns}  2*dCOM options={dcom}")
            check(f"r=2, G={Gname}: exceptional set computed (informational; not a no-go)", True,
                  f"{len(free)} of 62")
total()
