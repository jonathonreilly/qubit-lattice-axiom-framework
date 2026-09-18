#!/usr/bin/env python3
"""J:confirm:J-attack:PR8149 — independent sigma-equivariant star normalizers.

Finder (claude-opus-5) used numpy prod and a 6^7 float TV. This script uses
only Python ints. sigma(x,y,z)=(-z,-x,-y). For every assignment of the three
orbit representatives in {±e_i}^3, it builds the equivariant environment and
checks that prod_leaves D_leaf(v_c) is independent of the centre value v_c
at (p,q,r)=(3,1,2). HIT if that product is constant while each leaf records
the centre plus five outside sites.
"""
from __future__ import annotations

from itertools import product

DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
PQR = (3, 1, 2)


def sigma(v):
    return (-v[2], -v[0], -v[1])


def phi(a, b):
    p, q, r = PQR
    if a == b:
        return p
    if a == tuple(-x for x in b):
        return q
    return r


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def main() -> None:
    leaves = list(DIRS)
    outside = sorted({add(d, e) for d in leaves for e in DIRS} - {(0, 0, 0)} - set(leaves))
    nbr = {d: [o for o in outside if sum(abs(o[i] - d[i]) for i in range(3)) == 1] for d in leaves}

    cyc = [DIRS[0]]
    for _ in range(6):
        cyc.append(sigma(cyc[-1]))
    six = cyc[6] == cyc[0] and len(set(cyc[:6])) == 6
    free = all(
        (lambda v, k: (lambda: (lambda x: [x := sigma(x) for _ in range(k)][-1])())()) or True
        for _ in [0]
    )
    # freeness without nested-lambda mess:
    def apply_k(v, k):
        for _ in range(k):
            v = sigma(v)
        return v

    free = all(apply_k(o, k) != o for o in outside for k in range(1, 6))
    print(f"outside {len(outside)} six_cycle {six} free {free} leaf_outdeg { {len(nbr[d]) for d in leaves} }")

    # orbit reps: first site of each unused orbit
    def orbits():
        seen, orbs = set(), []
        for o in outside:
            if o in seen:
                continue
            orb = [o]
            while True:
                nxt = sigma(orb[-1])
                if nxt == o:
                    break
                orb.append(nxt)
            orbs.append(orb)
            seen.update(orb)
        return orbs

    orbs = orbits()
    print(f"orbits {len(orbs)} sizes {[len(o) for o in orbs]}")

    def env_from(reps):
        env = {}
        for orb, val in zip(orbs, reps):
            v = val
            for site in orb:
                env[site] = v
                v = sigma(v)
        return env

    n_ok = n = 0
    example = None
    for reps in product(DIRS, repeat=len(orbs)):
        env = env_from(reps)
        prods = []
        for c in DIRS:
            p = 1
            for d in leaves:
                Dd = 0
                for s in DIRS:
                    w = phi(c, s)
                    for o in nbr[d]:
                        w *= phi(env[o], s)
                    Dd += w
                p *= Dd
            prods.append(p)
            n += 1
        n_ok += int(len(set(prods)) == 1)
        if example is None:
            example = prods
    print(f"equivariant envs {6**len(orbs)}; constant prod D at (3,1,2): {n_ok}/{6**len(orbs)}")
    print(f"example products {example}")

    # all-+x environment should NOT be constant (note's executed differing case)
    env_plus = {o: (1, 0, 0) for o in outside}
    prods_plus = []
    for c in DIRS:
        p = 1
        for d in leaves:
            Dd = 0
            for s in DIRS:
                w = phi(c, s)
                for o in nbr[d]:
                    w *= phi(env_plus[o], s)
                Dd += w
            p *= Dd
        prods_plus.append(p)
    print(f"all-+x products constant {len(set(prods_plus))==1} values {prods_plus[:3]}...")

    if six and free and n_ok == 6 ** len(orbs) and len(set(prods_plus)) > 1:
        print(
            "HIT: confirmed - every sigma-equivariant environment has prod_leaf D_leaf(v_c) "
            f"independent of v_c at (3,1,2) ({n_ok} envs); all-+x is not constant; each leaf "
            "records the centre plus five outside sites"
        )
        print(
            "SUMMARY: confirmed U2/U4 fail in sigma-equivariant environments: centre-first "
            "star sequential=joint by exact integer normalizer products; all-+x still differs"
        )
    else:
        print("SUMMARY: not reproduced - " + f"six={six} free={free} n_ok={n_ok}")


if __name__ == "__main__":
    main()
