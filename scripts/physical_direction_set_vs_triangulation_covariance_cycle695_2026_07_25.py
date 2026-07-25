#!/usr/bin/env python3
"""Cycle 695: direction-set covariance and triangulation covariance are different invariants.

Cycle 690 (landed) proves a ceiling on TRIANGULATION invariance: no eight-vertex
unit-cube triangulation is invariant under all 24 proper cubic rotations, and the
maximum stabilizer is exactly 12, attained by the five-tetrahedron decomposition,
while the Kuhn/Freudenthal complex attains 6.

If a real-space Regge construction mediates its covariance through the EDGE
DIRECTION SET rather than through the triangulation, the relevant question is
which frames carry every spatial direction class back into the set, with each
direction read as unoriented (d equivalent to -d). That is a different
invariant, and this cycle shows the two can COME APART.

Exact integer results:

    object                              invariant                     value
    0/1 direction set (Kuhn edges)      oriented stabilizer               3
    0/1 direction set (Kuhn edges)      signed scope                      6
    Kuhn six-tetrahedron complex        cube-centred stabilizer           6
    five-tetrahedron edge directions    signed scope                     24
    five-tetrahedron complex            cube-centred stabilizer          12

For the Kuhn complex the two invariants COINCIDE at 6, which is why conflating
them is easy and why a construction reporting "6 of 24" can appear to be quoting
the triangulation ceiling when it is not. For the five-tetrahedron complex they
DIVERGE by a factor of two: the direction set is closed under all 24 rotations
while the triangulation it belongs to is invariant under only 12.

Consequence, and the reason this matters for the gravity lane: Cycle 690's
ceiling of 12 bounds TRIANGULATION invariance. It does NOT bound a construction
whose covariance is mediated by the direction set. Reading the 12 as a universal
ceiling for real-space Regge covariance is a misreading, and so is citing it as
the licence for a direction-set scope of 6.

Firewalls: this cycle adds no physics. It compares two group-theoretic
invariants of declared finite fixtures and makes no gravity, metric, dynamics or
observable claim. It proposes and adopts no axiom or primitive. It does not
assert that any construction achieves 24; it asserts only that the 12-ceiling
does not forbid it.
"""

from __future__ import annotations

import itertools
import json
import sys
from hashlib import sha256
from pathlib import Path
from time import perf_counter

ROOT = Path(__file__).resolve().parents[1]
AUTHORITY = "none"
AUDIT = "unset"
CYCLE_CLAIM = None  # set by supervisor at freeze

PASS = 0
FAIL = 0


def check(label, condition, detail=""):
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def rotations():
    out = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product((1, -1), repeat=3):
            m = [[0, 0, 0] for _ in range(3)]
            for i, pi in enumerate(p):
                m[i][pi] = s[i]
            det = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
                   - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                   + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
            if det == 1:
                out.append(tuple(tuple(r) for r in m))
    return tuple(out)


G = rotations()
VERTS = tuple(itertools.product((0, 1), repeat=3))


def apply(m, v):
    return tuple(sum(m[i][k] * v[k] for k in range(3)) for i in range(3))


def act_vertex(m, v):
    d = tuple(2 * c - 1 for c in v)
    r = apply(m, d)
    return tuple((c + 1) // 2 for c in r)


def neg(v):
    return tuple(-c for c in v)


def oriented_stabilizer(S):
    S = set(S)
    return tuple(i for i, m in enumerate(G) if all(apply(m, v) in S for v in S))


def signed_scope(S):
    S = set(S)
    def ok(m):
        for v in S:
            w = apply(m, v)
            if w not in S and neg(w) not in S:
                return False
        return True
    return tuple(i for i, m in enumerate(G) if ok(m))


def complex_stabilizer(tets):
    T = {frozenset(t) for t in tets}
    return tuple(i for i, m in enumerate(G)
                 if {frozenset(act_vertex(m, v) for v in t) for t in T} == T)


def kuhn_complex():
    out = []
    for p in itertools.permutations(range(3)):
        cur = [0, 0, 0]
        vs = [tuple(cur)]
        for a in p:
            cur = list(cur)
            cur[a] = 1
            vs.append(tuple(cur))
        out.append(vs)
    return out


def five_tet_complex():
    even = [v for v in VERTS if sum(v) % 2 == 0]
    odd = [v for v in VERTS if sum(v) % 2 == 1]
    out = [even]
    for v in odd:
        out.append([v] + [w for w in even
                          if sum(abs(v[i] - w[i]) for i in range(3)) == 1])
    return out


def edge_directions(tets):
    dirs = set()
    for t in tets:
        for a, b in itertools.combinations(t, 2):
            d = tuple(b[i] - a[i] for i in range(3))
            dirs.add(d)
            dirs.add(neg(d))
    return dirs


def main() -> int:
    started = perf_counter()
    summary = {"cycle": 695, "authority": AUTHORITY, "audit": AUDIT,
               "cycle_claim": CYCLE_CLAIM}

    prod_bad = sum(1 for a in G for b in G
                   if tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                                  for j in range(3)) for i in range(3)) not in G)
    check("the acting group is exactly the 24 proper cubic rotations and closes under "
          "all 576 products (exact integer arithmetic)",
          len(G) == 24 and prod_bad == 0,
          {"order": len(G), "products_outside": prod_bad})

    D01 = [v for v in VERTS if any(v)]
    kuhn = kuhn_complex()
    five = five_tet_complex()
    o01 = oriented_stabilizer(D01)
    s01 = signed_scope(D01)
    ck = complex_stabilizer(kuhn)
    fdirs = edge_directions(five)
    sf = signed_scope(fdirs)
    cf = complex_stabilizer(five)
    expected_fdirs = {
        d for d in itertools.product((-1, 0, 1), repeat=3)
        if sum(c * c for c in d) in (1, 2)
    }

    table = {
        "kuhn_direction_set_oriented_stabilizer": len(o01),
        "kuhn_direction_set_signed_scope": len(s01),
        "kuhn_complex_cube_centred_stabilizer": len(ck),
        "five_tet_direction_set_signed_scope": len(sf),
        "five_tet_complex_cube_centred_stabilizer": len(cf),
    }
    check("the five invariant values are computed exactly, the five-tetrahedron "
          "direction accumulator is the nonempty 18-vector axes-plus-face-diagonals "
          "set, and the overlapping complex values reproduce Cycle 690",
          table == {
              "kuhn_direction_set_oriented_stabilizer": 3,
              "kuhn_direction_set_signed_scope": 6,
              "kuhn_complex_cube_centred_stabilizer": 6,
              "five_tet_direction_set_signed_scope": 24,
              "five_tet_complex_cube_centred_stabilizer": 12,
          }
          and fdirs == expected_fdirs
          and len(fdirs) == 18,
          {**table, "five_tet_signed_direction_vectors": len(fdirs)})
    summary["invariants"] = table

    check("for the KUHN complex the two invariants COINCIDE: the signed direction-set "
          "scope and the cube-centred complex stabilizer are both 6 -- which is exactly "
          "why a construction reporting '6 of 24' can appear to quote the triangulation "
          "ceiling when it is really quoting its direction set",
          len(s01) == len(ck) == 6,
          {"signed_direction_scope": len(s01), "complex_stabilizer": len(ck)})

    check("for the FIVE-TETRAHEDRON complex the two invariants DIVERGE by a factor of "
          "two: its edge-direction set is closed under all 24 rotations while the "
          "triangulation itself is invariant under only 12 -- so the two invariants are "
          "genuinely different objects",
          len(sf) == 24 and len(cf) == 12,
          {"signed_direction_scope": len(sf), "complex_stabilizer": len(cf),
           "ratio": len(sf) // len(cf)})

    check("the complex stabilizer is contained in the associated direction-set "
          "stabilizer: equality holds for Kuhn and containment is strict for the "
          "five-tetrahedron complex, so a triangulation-only ceiling cannot be "
          "reused as an upper bound on direction-set covariance",
          set(ck) == set(s01)
          and set(cf) < set(sf)
          and len(sf) > 12,
          {"kuhn_equal": set(ck) == set(s01),
           "five_tet_complex_is_strict_subgroup": set(cf) < set(sf),
           "direction_scope": len(sf), "cycle690_triangulation_ceiling": 12})

    check("preregistered falsifier does not fire: had the two invariants agreed on every "
          "declared complex, the distinction asserted here would be empty -- they "
          "disagree on the five-tetrahedron complex",
          len(sf) != len(cf), {"agree_on_kuhn": len(s01) == len(ck),
                               "agree_on_five_tet": len(sf) == len(cf)})

    summary["consequence"] = (
        "Cycle 690's ceiling of 12 bounds TRIANGULATION invariance. It does not bound a "
        "construction whose covariance is mediated by the edge direction set. Reading "
        "the 12 as a universal ceiling for real-space Regge covariance is a misreading, "
        "and citing that triangulation ceiling as the reason for a direction-set scope "
        "of 6 is a category error. Cycle 690's separate Kuhn direction-set row does "
        "compute 6; the ceiling theorem does not entail it."
    )
    summary["firewalls"] = {
        "any_physics_claim": False,
        "asserts_some_construction_achieves_24": False,
        "new_axiom_or_primitive_proposed": False,
    }
    summary["resources"] = {"elapsed_seconds": perf_counter() - started}
    summary["runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    summary["pass_count"] = PASS
    summary["fail_count"] = FAIL
    summary["pass"] = FAIL == 0
    receipt = ROOT / "outputs" / (
        "physical_direction_set_vs_triangulation_covariance_cycle695_receipt_2026_07_25.json")
    if "--no-receipt" not in sys.argv:
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text(json.dumps(summary, indent=1, sort_keys=True, default=str) + "\n",
                           encoding="utf-8")
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True, default=str))
    print(f"RESULT {PASS} {FAIL} elapsed {perf_counter() - started:.2f} s")
    if FAIL:
        print("RESULT DIRECTION_SET_VS_TRIANGULATION_COVARIANCE_TOURNAMENT_FAILED")
        return 1
    print("RESULT DIRECTION_SET_AND_TRIANGULATION_COVARIANCE_ARE_DIFFERENT_INVARIANTS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
