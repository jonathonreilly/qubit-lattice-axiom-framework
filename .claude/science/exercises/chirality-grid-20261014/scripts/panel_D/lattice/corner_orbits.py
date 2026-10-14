"""Corner orbits and node chiralities: Z^3 cubic (set C) vs Z^4 hypercubic (set B).
Weyl symbol: d=3 Hamiltonian H(p)=sum_a sigma_a sin p_a; d=4 Euclidean D(p)=sum_mu e_mu sin p_mu,
e=(i*1, sigma_x, sigma_y, sigma_z) (Euclidean Weyl operator). Node chirality = sign det of the
linearisation Jacobian (product of cos p at the corner, times the fixed orientation sign).
Orbits: hyperoctahedral group (coordinate permutations + sign flips) acting on {0,pi}^d.
"""
import itertools, numpy as np
from math import pi
for d in (3, 4):
    corners = list(itertools.product((0, 1), repeat=d))  # 1 means pi
    # chirality: product over directions of cos(p_mu) = (-1)^{hw}
    chi = {c: (-1) ** sum(c) for c in corners}
    # orbits under permutations and sign flips (sign flips fix 0 and pi mod 2pi)
    seen, orbits = set(), []
    for c in corners:
        if c in seen: continue
        orb = set()
        for perm in itertools.permutations(range(d)):
            orb.add(tuple(c[i] for i in perm))
        seen |= orb; orbits.append(sorted(orb))
    sizes = [(len(o), sum(o[0]), chi[o[0]]) for o in orbits]
    print(f"d={d}: orbits (size, hw, chirality):", sizes, " net chirality:", sum(chi.values()))
    # all symmetry-invariant same-chirality light sets
    sets = {}
    for r in range(1, len(orbits) + 1):
        for combo in itertools.combinations(range(len(orbits)), r):
            ch = {chi[orbits[k][0]] for k in combo}
            if len(ch) == 1:
                n = sum(len(orbits[k]) for k in combo)
                sets.setdefault(ch.pop(), set()).add(n)
    print(f"   sizes of invariant single-chirality light sets: +1 -> {sorted(sets.get(1, []))}, -1 -> {sorted(sets.get(-1, []))}")
    print(f"   3 light generations possible as an invariant corner set: {any(3 in s for s in sets.values())}")
# chirality at a corner = sign of the Jacobian diag(cos p_mu) = (-1)^hw (standard; not re-derived numerically here)
