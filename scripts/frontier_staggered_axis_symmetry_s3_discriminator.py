#!/usr/bin/env python3
"""Physical staggered axis-symmetry on the hw=1 triplet is the FULL S_3.

Falsifier check for a possible staggered-eta preemption of the
positivity -> C_3 program. The standard staggered eta-phase convention
eta_x=1, eta_y=(-1)^x, eta_z=(-1)^{x+y} treats the three axes
asymmetrically, which *looks* like it breaks even C_3. If the PHYSICAL
staggered symmetry on the hw=1 axis triplet were only a Z_2 (or less), an
orientation-preserving C_3 target would be aimed at the wrong substrate.

Claim under test: the eta-convention asymmetry is pure GAUGE; the gauge-
invariant content (plaquette Z_2 field strength + Polyakov holonomies) is
permutation-symmetric, so every axis permutation in S_3 is a physical symmetry
of the staggered operator up to a site-local sign gauge. Hence the physical
axis-symmetry is the full S_3 -- unbroken -- so the staggered eta structure does
not itself supply or preempt an S_3 -> C_3 breaking. The physical bridge from
framework positivity to an orientation-preserving triplet criterion remains
separate.

Method, on a small even periodic L^3 lattice:
  1. all plaquette phases Phi_{mu,nu}(n) = -1 (every plane, every site);
  2. all Polyakov holonomies trivial (+1);
  3. for each of the 6 axis orderings (= S_3), build the reordered eta-field
     and EXPLICITLY solve for a Z_2 gauge s(n) with eta^sigma = s-coboundary of
     eta (BFS spanning tree + full consistency check). All 6 succeed.

Pure finite Z_2 lattice-gauge bookkeeping. No PDG / fitted / scale / mass input.
Asserts no audit status.
"""

from __future__ import annotations

import itertools

import numpy as np

PASS = 0
FAIL = 0
L = 4  # even


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if condition:
        PASS += 1
        st = "PASS"
    else:
        FAIL += 1
        st = "FAIL"
    msg = f"  [{st}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def sites():
    return list(itertools.product(range(L), repeat=3))


def add(n, mu):
    m = list(n)
    m[mu] = (m[mu] + 1) % L
    return tuple(m)


def eta_ordered(n, mu, order):
    """Staggered phase for axis ordering `order` (a permutation of (0,1,2)
    giving the '<' order): eta_mu(n) = (-1)^{sum of n_nu over axes nu that
    precede mu in `order`}."""
    pos = {ax: i for i, ax in enumerate(order)}
    s = 0
    for nu in range(3):
        if pos[nu] < pos[mu]:
            s += n[nu]
    return -1 if (s % 2) else 1


def plaquette(order, n, mu, nu):
    # eta_mu(n) eta_nu(n+mu) eta_mu(n+nu) eta_nu(n)
    return (eta_ordered(n, mu, order)
            * eta_ordered(add(n, mu), nu, order)
            * eta_ordered(add(n, nu), mu, order)
            * eta_ordered(n, nu, order))


def polyakov(order, mu, transverse):
    """Product of eta_mu along the periodic mu-line at fixed transverse coords."""
    p = 1
    n = list(transverse)
    n.insert(mu, 0)  # placeholder; we sweep mu coordinate
    prod = 1
    base = list(transverse)
    # build full site by inserting mu-coordinate
    others = [a for a in range(3) if a != mu]
    for k in range(L):
        site = [0, 0, 0]
        site[mu] = k
        site[others[0]] = transverse[0]
        site[others[1]] = transverse[1]
        prod *= eta_ordered(tuple(site), mu, order)
    return prod


def solve_gauge(order):
    """Find s(n) in {+/-1} with eta^order_mu(n) = s(n) eta^id_mu(n) s(n+mu),
    i.e. s(n)s(n+mu) = r_mu(n) := eta^order_mu(n) * eta^id_mu(n).
    BFS spanning tree from origin; then verify ALL links. Returns (ok, s)."""
    idorder = (0, 1, 2)
    S = sites()
    idx = {n: i for i, n in enumerate(S)}
    s = {n: None for n in S}
    origin = (0, 0, 0)
    s[origin] = 1
    queue = [origin]
    while queue:
        n = queue.pop()
        for mu in range(3):
            r = eta_ordered(n, mu, order) * eta_ordered(n, mu, idorder)
            m = add(n, mu)
            want = r * s[n]  # s[m] = r / s[n] = r * s[n] (since s=+/-1)
            if s[m] is None:
                s[m] = want
                queue.append(m)
            # also the backward link from m-... handled when visited
    # fill any unvisited (connected lattice -> all visited), then verify all links
    ok = True
    for n in S:
        if s[n] is None:
            ok = False
        for mu in range(3):
            r = eta_ordered(n, mu, order) * eta_ordered(n, mu, idorder)
            m = add(n, mu)
            if s[n] is None or s[m] is None or s[n] * s[m] != r:
                ok = False
    return ok, s


def perm_name(order):
    idorder = (0, 1, 2)
    fixed = sum(1 for i in range(3) if order[i] == i)
    if order == idorder:
        return "identity"
    return "transposition" if fixed == 1 else "3-cycle"


def main() -> int:
    print("=" * 76)
    print("PHYSICAL STAGGERED AXIS-SYMMETRY ON hw=1 TRIPLET IS FULL S_3")
    print("=" * 76)

    idorder = (0, 1, 2)

    # 1. plaquette field strength: all -1, every plane, every site (symmetric)
    print("\n" + "-" * 76)
    print("Gauge-invariant 1: plaquette phases (Z_2 field strength)")
    print("-" * 76)
    all_minus = True
    for mu in range(3):
        for nu in range(mu + 1, 3):
            vals = {plaquette(idorder, n, mu, nu) for n in sites()}
            ok = vals == {-1}
            all_minus = all_minus and ok
            check(f"all ({mu},{nu})-plaquettes = -1", ok, detail=f"values={vals}")
    check("plaquette field strength is permutation-symmetric (all planes equal -1)",
          all_minus)

    # 2. Polyakov holonomies trivial (symmetric)
    print("\n" + "-" * 76)
    print("Gauge-invariant 2: Polyakov holonomies around periodic cycles")
    print("-" * 76)
    all_triv = True
    for mu in range(3):
        vals = set()
        for t0 in range(L):
            for t1 in range(L):
                vals.add(polyakov(idorder, mu, (t0, t1)))
        ok = vals == {1}
        all_triv = all_triv and ok
        check(f"all Polyakov loops in direction {mu} trivial (+1)", ok, detail=f"{vals}")

    # 3. every axis ordering (S_3) is gauge-equivalent to the identity ordering
    print("\n" + "-" * 76)
    print("Every axis ordering (S_3) is a physical symmetry (explicit gauge)")
    print("-" * 76)
    n_ok = 0
    for order in itertools.permutations((0, 1, 2)):
        ok, _ = solve_gauge(order)
        if ok:
            n_ok += 1
        check(f"ordering {order} ({perm_name(order)}): explicit Z_2 gauge to identity found",
              ok)
    check("all 6 S_3 axis orderings gauge-equivalent => full S_3 is physical symmetry",
          n_ok == 6, detail=f"{n_ok}/6")

    print("\n" + "=" * 76)
    print("VERDICT")
    print("=" * 76)
    if FAIL == 0:
        print(
            "  PHYSICAL AXIS-SYMMETRY = FULL S_3 (falsifier RETIRED).\n"
            "  The staggered eta-convention's axis asymmetry is pure gauge: the\n"
            "  complete gauge-invariant content (plaquette field strength all -1;\n"
            "  Polyakov holonomies all +1) is permutation-symmetric, and every one\n"
            "  of the 6 S_3 axis orderings is related to the identity ordering by\n"
            "  an explicit site-local Z_2 gauge transformation.\n\n"
            "  Consequences for the positivity -> C_3 program:\n"
            "   * the staggered kinematics does NOT break S_3 (not to C_3, not to\n"
            "     Z_2) -- the physical axis-symmetry is the full S_3;\n"
            "   * therefore the staggered eta structure does not itself supply or\n"
            "     preempt an S_3 -> C_3 breaking;\n"
            "   * any positivity/orientation mechanism selecting an orientation-\n"
            "     preserving C_3 subgroup remains a separate physical bridge.\n"
        )
    print("=" * 76)
    if FAIL:
        print(f"PASS={PASS} FAIL={FAIL}")
        return 1
    print(f"PASS={PASS} FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
