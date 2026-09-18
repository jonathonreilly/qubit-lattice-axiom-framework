#!/usr/bin/env python3
"""J:attack:PR8149 - block 15 (PR #8149), attack pattern (d) QUANTIFIER SCOPE: U2's "for every non-constant rule, every unit U, every
environment v_O and every order: mu_sigma = mu_joint iff no site records an inside neighbour together with a second recorded neighbour"
and U4's "in a recorded environment every connected unit with at least two sites differs from its joint law under every order" are proved
by comparing, at the inside site y, a pattern "in which every value in every A_w' with y in A_w' equals b" - but in an environment the
outside records in those A_w' are fixed, so that pattern need not exist. The note executed two environments (all +x, one seeded mixed).

Adversarial construction tested here (exact integers, and the full laws on all 6^7 configurations in floating point):
  * the unit is the star (a site c and its six neighbours), formed centre first; every leaf records the centre and its five outside
    neighbours, so by U2's criterion (and U4) the sequential law must differ from the joint law;
  * sigma = -rho (rho the three-fold rotation x -> y -> z) is a signed permutation that cycles the six directions in one six-cycle
    (+x -> -y -> +z -> -x -> +y -> -z) and acts freely on the star's 18 outside sites (three orbits of six), so a sigma-equivariant
    environment exists: pick records at three orbit representatives, and set v(sigma^k o) = sigma^k v(o);
  * the rule phi(a, b) in {p, q, r} depends only on same / antipodal / orthogonal, so it is invariant under every signed permutation;
    then leaf sigma^k(d) carries the multiset sigma^k(C), its normalizer is f(sigma^-k v_c), and the product over the six leaves is
    prod_{b in M} f(b) for every centre value v_c: the sequential law is the joint law;
  * checked for all 216 choices of representative records and five rules (the executed (3,1,2), (5,2,4), (2,1,2), (7,3,5), (11,4,6)),
    against the note's own all-+x environment (where the laws differ, as the note says).
HIT if a recorded environment exists in which a connected multi-site unit's sequential law equals its joint law.
"""
import itertools
import sys
import time
from fractions import Fraction

import numpy as np

DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
IDX = {d: i for i, d in enumerate(DIRS)}


def sigma(v):                      # sigma = -rho, rho(v) = (v_z, v_x, v_y): e_x -> e_y -> e_z -> e_x
    return (-v[2], -v[0], -v[1])


def phi_int(a, b, pqr):
    p, q, r = pqr
    if a == b:
        return p
    if a == tuple(-x for x in b):
        return q
    return r


def star():
    leaves = list(DIRS)
    out = sorted({tuple(d[i] + e[i] for i in range(3)) for d in leaves for e in DIRS} - {(0, 0, 0)} - set(leaves))
    nbr = {d: [o for o in out if sum(abs(o[i] - d[i]) for i in range(3)) == 1] for d in leaves}
    return leaves, out, nbr


def equivariant_env(out, reps_vals):
    env = {}
    orbits = []
    for o in out:
        if o in env:
            continue
        orb = [o]
        while True:
            nxt = sigma(orb[-1])
            if nxt == o:
                break
            orb.append(nxt)
        orbits.append(orb)
        val = reps_vals[len(orbits) - 1]
        for k, site in enumerate(orb):
            v = val
            for _ in range(k):
                v = sigma(v)
            env[site] = v
    return env, orbits


def denominators(leaves, nbr, env, pqr):
    """D_d(v_c) = sum_s phi(v_c, s) prod_{o in nbr(d)} phi(v_o, s): the integer normalizer of leaf d's conditional, for each centre value."""
    out = {}
    for d in leaves:
        out[d] = [sum(phi_int(c, s, pqr) * np.prod([phi_int(env[o], s, pqr) for o in nbr[d]]) for s in DIRS) for c in DIRS]
    return out


def full_laws(leaves, nbr, env, pqr):
    P = np.array([[phi_int(a, b, pqr) for b in DIRS] for a in DIRS], dtype=float)
    h = {d: np.array([np.prod([phi_int(env[o], s, pqr) for o in nbr[d]]) for s in DIRS], dtype=float) for d in leaves}
    W = np.ones((6,) * 7)
    for i, d in enumerate(leaves):
        shape = [6] + [1] * 6
        shape[1 + i] = 6
        W = W * (P * h[d][None, :]).reshape(shape)
    mu_joint = W / W.sum()
    seq = np.full((6,) * 7, 1 / 6)                      # the centre forms first: r(v_c | empty) = 1/6
    for i, d in enumerate(leaves):
        Dd = (P * h[d][None, :]).sum(1)                  # sum_s phi(v_c, s) h_d(s)
        shape = [6] + [1] * 6
        shape[1 + i] = 6
        seq = seq * ((P * h[d][None, :]) / Dd[:, None]).reshape(shape)
    return 0.5 * np.abs(seq - mu_joint).sum(), seq.sum(), mu_joint.sum()


def main():
    t0 = time.time()
    leaves, out, nbr = star()
    cyc = [DIRS[0]]
    while len(cyc) < 7:
        cyc.append(sigma(cyc[-1]))
    six_cycle = cyc[6] == cyc[0] and len(set(cyc[:6])) == 6
    # freeness: no sigma^k (k = 1..5) fixes an outside site
    def pw(v, k):
        for _ in range(k):
            v = sigma(v)
        return v
    free = all(pw(o, k) != o for o in out for k in range(1, 6))
    preserves = all(phi_int(sigma(a), sigma(b), (3, 1, 2)) == phi_int(a, b, (3, 1, 2)) for a in DIRS for b in DIRS)
    maps_nbhd = all(sorted(sigma(o) for o in nbr[d]) == sorted(nbr[sigma(d)]) for d in leaves)
    print(f"[setup] star: 7 sites, {len(out)} outside sites, every leaf has {sorted({len(v) for v in nbr.values()})} outside neighbours; sigma on "
          f"directions is one six-cycle {[''.join(('+' if max(v) > 0 else '-') + 'xyz'[[abs(t) for t in v].index(1)]) for v in cyc[:6]]}: {six_cycle}; "
          f"sigma acts freely on the outside sites: {free}; preserves the rule's relation: {preserves}; maps each leaf's outside neighbourhood to "
          f"its image leaf's: {maps_nbhd}")
    rules = [(3, 1, 2), (5, 2, 4), (2, 1, 2), (7, 3, 5), (11, 4, 6)]
    n_const, n_total = 0, 0
    worst_int = {}
    for reps in itertools.product(DIRS, repeat=3):
        env, orbits = equivariant_env(out, reps)
        for pqr in rules:
            D = denominators(leaves, nbr, env, pqr)
            prod = [int(np.prod([int(D[d][ci]) for d in leaves], dtype=object)) for ci in range(6)]
            n_total += 1
            if len(set(prod)) == 1:
                n_const += 1
            else:
                worst_int[(reps, pqr)] = prod
    env, orbits = equivariant_env(out, (DIRS[4], DIRS[0], DIRS[2]))
    mults = {d: sorted(IDX[env[o]] for o in nbr[d]) for d in leaves}
    distinct_vals = sorted({IDX[env[o]] for d in leaves for o in nbr[d]})
    D = denominators(leaves, nbr, env, (3, 1, 2))
    prod_312 = [int(np.prod([int(D[d][ci]) for d in leaves], dtype=object)) for ci in range(6)]
    tv_eq = {pqr: full_laws(leaves, nbr, env, pqr)[0] for pqr in rules}
    env_x = {o: DIRS[0] for o in out}
    D_x = denominators(leaves, nbr, env_x, (3, 1, 2))
    prod_x = [int(np.prod([int(D_x[d][ci]) for d in leaves], dtype=object)) for ci in range(6)]
    tv_x = full_laws(leaves, nbr, env_x, (3, 1, 2))[0]
    # a leaf-first order in the equivariant environment, for contrast: leaf +x first, then the centre, then the other leaves
    P = np.array([[phi_int(a, b, (3, 1, 2)) for b in DIRS] for a in DIRS], dtype=object)
    others = [d for d in leaves if d != DIRS[0]]
    Fo = [int(np.prod([sum(P[ci, s] * int(np.prod([phi_int(env[o], DIRS[s], (3, 1, 2)) for o in nbr[d]], dtype=object)) for s in range(6))
                       for d in others], dtype=object)) for ci in range(6)]
    print(f"[environments] sigma-equivariant environments: {len(set(itertools.product(DIRS, repeat=3)))} choices of the three representative "
          f"records x {len(rules)} rules: product of the six leaves' integer normalizers constant in the centre value in {n_const} of {n_total} "
          f"cases; example (representatives +z, +x, +y): leaf multisets (menu indices) {list(mults.values())}, outside records span directions "
          f"{distinct_vals} (so no single b equals every recorded value around the centre); prod_d D_d(v_c) at (3,1,2) = {prod_312}")
    print(f"[full laws] all 6^7 configurations, centre first: TV(sequential, joint) in the equivariant environment = "
          + ", ".join(f"{pqr}: {tv:.1e}" for pqr, tv in tv_eq.items())
          + f"; in the note's all-+x environment at (3,1,2): TV = {tv_x:.6f} (product of normalizers {prod_x[:3]}... not constant); leaf-first order "
          f"in the equivariant environment: product over the other five leaves {Fo} (constant: {len(set(Fo)) == 1})  ({time.time() - t0:.0f}s)")
    hits = []
    if n_const == n_total and max(tv_eq.values()) < 1e-12 and six_cycle and free and preserves and maps_nbhd:
        hits.append("U2 (only-if) and U4 fail: in every sigma-equivariant recorded environment (216 choices of the three orbit records) the star "
                    "formed centre first has sequential law equal to its joint law at every tested rule, including the executed (3,1,2) "
                    f"(exact: the product of the six leaves' normalizers is constant in the centre value; full-law TV {max(tv_eq.values()):.0e}), "
                    "although every leaf records the centre together with five outside records; U2's proof pattern (all recorded values equal "
                    "to one b) is unavailable because the fixed outside records span all six directions")
    for h in hits:
        print("HIT: " + h)
    print(f"SUMMARY: attack pattern (d) QUANTIFIER SCOPE - U2's 'every environment' and U4's 'every connected unit in a recorded environment "
          f"differs under every order' tested against an adversarially constructed environment: sigma = -rho cycles the six directions and acts "
          f"freely on the star's 18 outside sites, so sigma-equivariant environments exist; in all {n_total // len(rules)} of them the centre-first "
          f"star's sequential law equals its joint law exactly at all {len(rules)} rules ({n_const}/{n_total} exact constancy checks; full-law TV "
          f"<= {max(tv_eq.values()):.0e}), while the note's all-+x environment differs (TV {tv_x:.4f}); {len(hits)} failures; attack "
          f"{'FIRES' if hits else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
