#!/usr/bin/env python3
"""J:attack-e:PR8158 — SAMPLED EVIDENCE.

Do not re-find the known Q4(a) triangle HIT (extra site on two adjacent
plaquette corners is not a Z^3 window).

Q5/N1: R1≠R2 on any window whose unrecorded component touches two recorded
sites, for every non-constant rule. Executed on three named geometries;
the checker used random pendant/bridging components. Instead of more
samples: exhaustive adversarial search of every connected unrecorded E of
size 1..3 in the box [0,2]^3 that touches exactly two recorded sites as an
induced Z^3 nn subgraph, at (3,1,2). HIT if F_C is constant (TV would be 0)
on such a bridging window.
"""
from __future__ import annotations

from itertools import combinations, product

VALS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
P, Q, Rwt = 3, 1, 2
BOX = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]


def nn(a, b) -> bool:
    return sum(abs(i - j) for i, j in zip(a, b)) == 1


def phi(s, t) -> int:
    if s == t:
        return P
    if s == (-t[0], -t[1], -t[2]):
        return Q
    return Rwt


def connected(sites) -> bool:
    sites = list(sites)
    if not sites:
        return True
    seen = {sites[0]}
    stack = [sites[0]]
    S = set(sites)
    while stack:
        u = stack.pop()
        for v in S:
            if v not in seen and nn(u, v):
                seen.add(v)
                stack.append(v)
    return len(seen) == len(sites)


def F_two_attach(E, x, y) -> dict:
    """F_C(vx, vy) = Σ_{u on E} Π_{bonds in E} φ Π_{e~x} φ(vx,ue) Π_{e~y} φ(vy,ue)."""
    E = list(E)
    bonds = [(i, j) for i in range(len(E)) for j in range(i + 1, len(E)) if nn(E[i], E[j])]
    ax = [i for i, e in enumerate(E) if nn(e, x)]
    ay = [i for i, e in enumerate(E) if nn(e, y)]
    out = {}
    for vx, vy in product(VALS, repeat=2):
        tot = 0
        for u in product(VALS, repeat=len(E)):
            w = 1
            for i, j in bonds:
                w *= phi(u[i], u[j])
            for i in ax:
                w *= phi(vx, u[i])
            for i in ay:
                w *= phi(vy, u[i])
            tot += w
        out[(vx, vy)] = tot
    return out


def is_constant(Ftab: dict) -> bool:
    return len(set(Ftab.values())) == 1


def main() -> int:
    hits = []
    n_bridge = 0
    n_const = 0
    examples = []
    # every connected E subset of the box, size 1..3; recorded attachments
    # are two distinct box sites neighboring E and not in E
    for k in (1, 2, 3):
        for E in combinations(BOX, k):
            if not connected(E):
                continue
            Es = set(E)
            attach = [p for p in BOX if p not in Es and any(nn(p, e) for e in E)]
            for x, y in combinations(attach, 2):
                # bridging: the component touches these two recorded sites
                # (and we do not add other recorded sites)
                n_bridge += 1
                Ftab = F_two_attach(E, x, y)
                const = is_constant(Ftab)
                if const:
                    n_const += 1
                    msg = (
                        f"bridging E={E} attachments {x},{y}: F_C constant "
                        f"at (3,1,2) (R1=R2 on a two-attachment Z^3 window)"
                    )
                    hits.append(msg)
                    print("HIT:", msg)
                    if n_const >= 3:
                        break
            if n_const >= 3:
                break
        if n_const >= 3:
            break
        print(f"  scanned connected E of size {k}, running bridging pairs={n_bridge}")

    # sanity: size-1 two-attachment is φ², not constant
    e = (1, 1, 1)
    x, y = (0, 1, 1), (2, 1, 1)  # opposite neighbors, distance 2
    F1 = F_two_attach((e,), x, y)
    print(f"  sanity size-1 opposite: unique F values={len(set(F1.values()))} (want >1)")
    if is_constant(F1):
        hits.append("HIT: size-1 opposite-neighbor φ² is constant at (3,1,2)")
        print(hits[-1])

    # do not build Q4(a): extra vertex not in Z^3 adjacent to two adjacent corners
    print(f"bridging windows enumerated={n_bridge} constant={n_const}")

    if hits:
        print("SUMMARY: SAMPLED EVIDENCE (PR #8158): " + "; ".join(hits[:3]))
        return 0
    print(
        "SUMMARY: SAMPLED EVIDENCE (PR #8158): Q5's 'never R1=R2 on a "
        "two-attachment window' was executed on three geometries and the "
        "checker used random components; exhaustive Z^3 search of every "
        f"connected unrecorded E of size 1..3 in [0,2]^3 with exactly two "
        f"recorded attachments ({n_bridge} bridging pairs) at (3,1,2) has "
        "F_C nonconstant on all of them (not the Q4(a) triangle); pattern "
        "has purchase and does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
