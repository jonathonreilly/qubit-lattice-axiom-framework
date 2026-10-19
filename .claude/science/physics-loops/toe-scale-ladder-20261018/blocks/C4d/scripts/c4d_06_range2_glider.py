"""C4d-06: range 2, G = T. The face-diagonal glider of Observation M (P-type pair steps +normal,
all other near pairs fixed), and the other symmetry-allowed monomial maps of the face orbit.
Question: does the exact 3-magnon spectator test (U and U^-1) already kill it at range 2, as it
kills every moving map at range 1 (c4d_02/c4d_05)?"""
from c4d_common import check, total, T, pair, add, canon_rho, near_rhos
from c4d_monomial import (orbit_reps, allowed_images, MonomialW, bijective_on_near, inverse,
                          spectator_relations, consistency, cycle_displacements)

r = 2
reps = orbit_reps(T, r)
print("orbit reps (rho, orbit size):", [(rho, len(o)) for rho, o in reps])
ident = {rho: pair((0, 0, 0), rho) for rho, _ in reps}
face = [rho for rho, _ in reps if sorted(map(abs, rho)) == [0, 1, 1]][0]
print("face-diagonal representative:", face)
opts = allowed_images(T, face, r)
print("stabiliser-fixed images of the face rep:", [sorted(s) for s in opts])
n_move = n_move_ok = 0
for s in opts:
    imgs = dict(ident); imgs[face] = s
    W = MonomialW(T, r, imgs)
    if not W.check_equivariance() or not bijective_on_near(W, r):
        print("  image", sorted(s), "-> not equivariant/bijective"); continue
    cyc = cycle_displacements(W, r)
    mv = [(rho, l, d) for rho, l, d in cyc if d != (0, 0, 0)]
    bad = consistency(spectator_relations(W, inverse(W, r), r))
    print(f"  image {sorted(s)}: moving cycles {mv[:3]}{'...' if len(mv)>3 else ''}  spectator conflicts: {len(bad)}")
    if mv:
        n_move += 1
        n_move_ok += (len(bad) == 0)
check("range 2: moving face-diagonal monomial maps exist (2-magnon level)", n_move > 0, f"{n_move}")
check("range 2: some moving map passes the exact 3-magnon spectator test (no 3-body obstruction)",
      n_move_ok > 0, f"{n_move_ok} of {n_move}")
total()
