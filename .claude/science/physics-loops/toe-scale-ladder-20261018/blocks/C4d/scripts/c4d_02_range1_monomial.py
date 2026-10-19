"""C4d-02: range 1, EXHAUSTIVE over all monomial (deterministic up to phases) pair maps W that are
equivariant under G in {T, O} (+ translations), bijective on near pairs, with Lemma-K support.
For each: does a pair move (non-zero cycle displacement)?  Does W survive the exact 3-magnon
spectator test (forward for U and backward for U^-1)?"""
import itertools
from c4d_common import check, total, T, O
from c4d_monomial import (orbit_reps, allowed_images, MonomialW, bijective_on_near, inverse,
                          spectator_relations, consistency, cycle_displacements)

r = 1
for name, G in (("T", T), ("O", O)):
    reps = orbit_reps(G, r)
    opts = [allowed_images(G, rho, r) for rho, _ in reps]
    print(f"[{name}] orbit reps:", [(rho, len(orb), len(o)) for (rho, orb), o in zip(reps, opts)])
    n_tot = n_bij = n_move = n_move_ok = n_ok = 0
    survivors = []
    for choice in itertools.product(*opts):
        imgs = {rho: s for (rho, _), s in zip(reps, choice)}
        W = MonomialW(G, r, imgs)
        n_tot += 1
        if not W.check_equivariance():
            print("equivariance failure", imgs); continue
        if not bijective_on_near(W, r):
            continue
        n_bij += 1
        cyc = cycle_displacements(W, r)
        moves = any(d != (0, 0, 0) for _, _, d in cyc)
        Winv = inverse(W, r)
        bad = consistency(spectator_relations(W, Winv, r))
        n_move += moves
        if not bad:
            n_ok += 1
            survivors.append((imgs, cyc))
            n_move_ok += moves
        elif moves and n_move - n_move_ok <= 2:
            print(f"  moving map rejected, e.g. {bad[0][0]}: {sorted(map(sorted, [bad[0][1][0]]))} vs {sorted(map(sorted,[bad[0][2][0]]))}")
    print(f"[{name}] maps={n_tot} bijective={n_bij} moving={n_move} pass-spectator={n_ok} moving&pass={n_move_ok}")
    check(f"[{name}] exhaustive: no moving monomial range-1 pair map survives the 3-magnon spectator test",
          n_move_ok == 0, f"{n_move} moving bijective maps, {n_ok} survivors (all non-moving)")
    if name == "T":
        check("[T] moving bijective monomial maps exist at the 2-magnon level (test is not vacuous)", n_move > 0)
    for imgs, cyc in survivors[:3]:
        print("   survivor cycles:", [(rho, l) for rho, l, d in cyc])
total()
