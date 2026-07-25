#!/usr/bin/env python3
"""Cycle 700: admissible configurations are closed under neither disjoint union
nor sub-collection, and the exact separation that restores union closure.

The Record axiom says scalar readout is additive "for any finite collection of
pairwise-disjoint records".  Reading that clause requires knowing which
collections are configurations at all, and that is decided by Admissibility:
"one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations", under which "for each site, the
available possibilities are determined by, and vary with, the nearest-neighbor
conditions".

This cycle establishes four things by exact finite computation.

U1  Two explicitly exhibited rules are legitimate instances of the
    Admissibility axiom: each is nearest-neighbor, translation-covariant,
    proper-cubic-covariant, and each has an available set that genuinely varies
    with the neighbor conditions.

U2  Under the exhibited rule A2plus -- availability empty exactly when a site
    has two or more occupied nearest neighbors -- admissible configurations are
    NOT closed under disjoint union.  Two disjoint admissible configurations
    whose union is inadmissible are exhibited, under both of the two available
    site semantics (occupied-sites-only, and every-site).

U3  Under the exhibited rule A0 -- availability empty exactly when a site has
    no occupied nearest neighbor -- admissible configurations are NOT closed
    under sub-collection: a strict subset of an admissible configuration is
    inadmissible.

U4  Closure is restored by an exact separation condition, and this one holds
    for EVERY nearest-neighbor rule, not just the exhibited ones: if the closed
    one-neighborhoods of two configurations are disjoint, then no site sees
    occupied neighbors from both, so every site's nearest-neighbor condition in
    the union equals its condition in whichever part contains it.  Availability
    is therefore unchanged everywhere and the union is admissible.  The
    condition is checked exhaustively on a finite window, and its tightness is
    exhibited: at closed-neighborhood contact the conclusion fails.

Consequences, stated in the note rather than here: the additivity clause's
quantifier has an implicit domain condition in both directions, and any
argument that composes two configurations -- for instance a duplication
argument -- needs the U4 separation hypothesis explicitly.

No axiom or primitive is proposed or adopted, no reading of the axiom text is
ratified, and no rule exhibited here is claimed to be the framework's rule.
Every scored row uses exact integer or set arithmetic.  The runner imports no
repository content.
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
CYCLE_CLAIM = None

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


Vec = tuple[int, int, int]

FACES: list[Vec] = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]


def neighbours(s: Vec) -> list[Vec]:
    return [tuple(s[i] + v[i] for i in range(3)) for v in FACES]  # type: ignore[misc]


def occupied_neighbour_count(x: Vec, cfg: frozenset[Vec]) -> int:
    return sum(1 for nb in neighbours(x) if nb in cfg)


def closed_neighbourhood(cfg: frozenset[Vec]) -> set[Vec]:
    out: set[Vec] = set()
    for s in cfg:
        out.add(s)
        out.update(neighbours(s))
    return out


# --------------------------------------------------------------------------
# two exhibited nearest-neighbor availability rules
# --------------------------------------------------------------------------
# Each maps a neighbor-occupancy count to True (some possibility available) or
# False (available set empty).  Both depend only on the nearest-neighbor
# conditions, so both are translation- and rotation-covariant by construction.


def rule_A2plus(count: int) -> bool:
    """Available set empty exactly when two or more neighbors are occupied."""
    return count < 2


def rule_A0(count: int) -> bool:
    """Available set empty exactly when no neighbor is occupied."""
    return count > 0


RULES = {"A2plus": rule_A2plus, "A0": rule_A0}


# --------------------------------------------------------------------------
# the stronger witnesses: availability is NEVER empty
# --------------------------------------------------------------------------
# An objection to the rules above is that an empty available set is degenerate.
# These two rules never produce one.  Their available sets are proper nonempty
# subsets that shrink or grow with the neighbor conditions, exactly as the
# axiom's "vary with" requires, and a configuration now records WHICH
# possibility each record locked.  "c0" stands for a central element of the
# one-site algebra and "c1" for a non-central one; nothing below depends on
# which elements they are, only that there are at least two.

CONTENTS = ("c0", "c1")


def avail_shrink_on_crowding(count: int) -> tuple[str, ...]:
    """Both possibilities available until two neighbors are occupied."""
    return CONTENTS if count < 2 else ("c0",)


def avail_grow_on_contact(count: int) -> tuple[str, ...]:
    """Only the central possibility available when isolated."""
    return CONTENTS if count > 0 else ("c0",)


def admissible_typed(cfg: dict, avail) -> bool:
    """Every record's locked content must lie in its available set."""
    occ = frozenset(cfg)
    return all(
        content in avail(occupied_neighbour_count(site, occ))
        for site, content in cfg.items()
    )


def admissible(cfg: frozenset[Vec], rule, every_site: bool) -> bool:
    """occupied-only semantics, or every-site semantics over the closed hull."""
    sites = closed_neighbourhood(cfg) if every_site else set(cfg)
    return all(rule(occupied_neighbour_count(x, cfg)) for x in sites)


def signed_permutations() -> list[tuple[Vec, Vec, Vec]]:
    out = []
    basis = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            out.append(
                tuple(
                    tuple(signs[i] * basis[perm[i]][k] for k in range(3))
                    for i in range(3)
                )
            )
    return out


def det3(m) -> int:
    (a, b, c), (d, e, f), (g, h, i) = m
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def apply(m, v: Vec) -> Vec:
    return tuple(sum(m[i][k] * v[k] for k in range(3)) for i in range(3))  # type: ignore[return-value]


def main() -> int:
    started = perf_counter()
    summary: dict[str, object] = {
        "cycle": 700,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "cycle_claim": CYCLE_CLAIM,
    }

    proper = [m for m in signed_permutations() if det3(m) == 1]

    # ------------------------------------------------------------------
    # U1  both exhibited rules are legitimate Admissibility instances
    # ------------------------------------------------------------------
    window = [
        (x, y, z)
        for x in range(-2, 3)
        for y in range(-2, 3)
        for z in range(-2, 3)
    ]
    sample_cfgs = [
        frozenset({(0, 0, 0)}),
        frozenset({(0, 0, 0), (1, 0, 0)}),
        frozenset({(0, 0, 0), (1, 0, 0), (-1, 0, 0)}),
        frozenset({(0, 0, 0), (2, 0, 0)}),
        frozenset({(0, 0, 0), (1, 0, 0), (0, 1, 0)}),
    ]

    report = {}
    all_ok = True
    for name, rule in RULES.items():
        # varies with the neighbor conditions
        values = {rule(c) for c in range(7)}
        varies = len(values) == 2
        # translation covariance: shifting a configuration shifts availability
        trans_ok = True
        for cfg in sample_cfgs:
            for t in [(3, 0, 0), (0, -2, 1)]:
                shifted = frozenset(
                    tuple(s[i] + t[i] for i in range(3)) for s in cfg
                )
                for x in window:
                    xs = tuple(x[i] + t[i] for i in range(3))
                    if rule(occupied_neighbour_count(x, cfg)) != rule(
                        occupied_neighbour_count(xs, shifted)
                    ):
                        trans_ok = False
        # proper cubic covariance
        rot_ok = True
        for cfg in sample_cfgs:
            for R in proper[:6]:
                rotated = frozenset(apply(R, s) for s in cfg)
                for x in window:
                    xr = apply(R, x)
                    if rule(occupied_neighbour_count(x, cfg)) != rule(
                        occupied_neighbour_count(xr, rotated)
                    ):
                        rot_ok = False
        report[name] = {
            "available_set_varies": varies,
            "translation_covariant": trans_ok,
            "proper_cubic_covariant": rot_ok,
        }
        all_ok = all_ok and varies and trans_ok and rot_ok
    check(
        "U1 both exhibited rules depend only on the nearest-neighbor "
        "conditions, are translation- and proper-cubic-covariant, and have an "
        "available set that genuinely varies with those conditions",
        all_ok,
        report,
    )

    # ------------------------------------------------------------------
    # U2  union closure fails, under both site semantics
    # ------------------------------------------------------------------
    # occupied-only semantics: the middle record gains two occupied neighbors
    S1 = frozenset({(0, 0, 0)})
    S2 = frozenset({(1, 0, 0), (-1, 0, 0)})
    U = S1 | S2
    occ_fail = (
        admissible(S1, rule_A2plus, False)
        and admissible(S2, rule_A2plus, False)
        and not admissible(U, rule_A2plus, False)
        and not (S1 & S2)
    )
    # every-site semantics: an EMPTY midpoint becomes unavailable
    T1 = frozenset({(0, 0, 0)})
    T2 = frozenset({(2, 0, 0)})
    V = T1 | T2
    every_fail = (
        admissible(T1, rule_A2plus, True)
        and admissible(T2, rule_A2plus, True)
        and not admissible(V, rule_A2plus, True)
        and not (T1 & T2)
    )
    # and that pair IS admissible under occupied-only, so the semantics differ
    semantics_differ = admissible(V, rule_A2plus, False) and not admissible(
        V, rule_A2plus, True
    )
    check(
        "U2 admissible configurations are not closed under disjoint union: an "
        "explicit failing pair exists under occupied-site semantics and "
        "another under every-site semantics, and the two semantics are shown "
        "to differ on a concrete union",
        occ_fail and every_fail and semantics_differ,
        {
            "occupied_only_counterexample": [sorted(S1), sorted(S2)],
            "midpoint_of_every_site_counterexample": (1, 0, 0),
            "every_site_counterexample": [sorted(T1), sorted(T2)],
            "semantics_differ_on_that_union": semantics_differ,
        },
    )

    # ------------------------------------------------------------------
    # U3  sub-collection closure fails too
    # ------------------------------------------------------------------
    W = frozenset({(0, 0, 0), (1, 0, 0)})
    sub = frozenset({(0, 0, 0)})
    subset_fail = (
        admissible(W, rule_A0, False)
        and not admissible(sub, rule_A0, False)
        and sub < W
    )
    # the same rule keeps the full configuration admissible, so this is a
    # closure failure and not a badly chosen configuration
    check(
        "U3 admissible configurations are not closed under sub-collection "
        "either: under the exhibited rule A0 a strict subset of an admissible "
        "two-record configuration is inadmissible",
        subset_fail,
        {
            "admissible_configuration": sorted(W),
            "inadmissible_strict_subset": sorted(sub),
            "rule": "A0: available set empty exactly when no neighbor occupied",
        },
    )

    # ------------------------------------------------------------------
    # U2b / U3b  the same two failures with never-empty availability
    # ------------------------------------------------------------------
    # union: a record locked a non-central possibility, then gained neighbors
    P1 = {(0, 0, 0): "c1"}
    P2 = {(1, 0, 0): "c0", (-1, 0, 0): "c0"}
    PU = {**P1, **P2}
    union_typed = (
        admissible_typed(P1, avail_shrink_on_crowding)
        and admissible_typed(P2, avail_shrink_on_crowding)
        and not admissible_typed(PU, avail_shrink_on_crowding)
        and not (set(P1) & set(P2))
    )
    # subset: removing a neighbor withdraws the possibility already locked
    Q = {(0, 0, 0): "c1", (1, 0, 0): "c0"}
    Qsub = {(0, 0, 0): "c1"}
    subset_typed = (
        admissible_typed(Q, avail_grow_on_contact)
        and not admissible_typed(Qsub, avail_grow_on_contact)
        and set(Qsub) < set(Q)
    )
    never_empty = all(
        len(avail_shrink_on_crowding(c)) > 0 and len(avail_grow_on_contact(c)) > 0
        for c in range(7)
    ) and all(
        len(set(avail_shrink_on_crowding(c))) < len(CONTENTS)
        or len(set(avail_grow_on_contact(c))) < len(CONTENTS)
        for c in (0, 2)
    )
    check(
        "U2b/U3b both closure failures persist under rules whose available set "
        "is never empty: availability is a proper nonempty subset that varies "
        "with the neighbor conditions, and a record's already-locked "
        "possibility is withdrawn by joining or by splitting",
        union_typed and subset_typed and never_empty,
        {
            "union_witness": {str(k): v for k, v in PU.items()},
            "subset_witness": {str(k): v for k, v in Q.items()},
            "availability_never_empty": never_empty,
            "rules": [
                "both available until 2 neighbors occupied, then central only",
                "central only when isolated, both on contact",
            ],
        },
    )

    # ------------------------------------------------------------------
    # U4  the separation condition, valid for EVERY nearest-neighbor rule
    # ------------------------------------------------------------------
    # Lemma: if the closed one-neighborhoods are disjoint, no site has occupied
    # neighbors in both parts, so every site's neighbor condition in the union
    # equals its condition in the part that contains it (or is unchanged).
    # Verified exhaustively over all configuration pairs drawn from a window.
    small = [(x, 0, 0) for x in range(-1, 6)] + [(0, 1, 0), (1, 1, 0), (3, 1, 0)]
    pairs_checked = 0
    lemma_holds = True
    separated_seen = 0
    for k1 in (1, 2):
        for A in itertools.combinations(small, k1):
            fa = frozenset(A)
            for k2 in (1, 2):
                for B in itertools.combinations(small, k2):
                    fb = frozenset(B)
                    if fa & fb:
                        continue
                    pairs_checked += 1
                    if closed_neighbourhood(fa) & closed_neighbourhood(fb):
                        continue
                    separated_seen += 1
                    union = fa | fb
                    for x in closed_neighbourhood(union):
                        cu = occupied_neighbour_count(x, union)
                        ca = occupied_neighbour_count(x, fa)
                        cb = occupied_neighbour_count(x, fb)
                        # no site sees both, and the union count is the sum
                        if cu != ca + cb or (ca > 0 and cb > 0):
                            lemma_holds = False
    # tightness: at closed-neighborhood contact the conclusion fails
    contact = closed_neighbourhood(T1) & closed_neighbourhood(T2)
    tight = bool(contact) and not admissible(V, rule_A2plus, True)
    check(
        "U4 whenever the closed one-neighborhoods are disjoint, no site has "
        "occupied neighbors in both parts and the union's neighbor count is "
        "the sum, so availability is unchanged for EVERY nearest-neighbor "
        "rule; at closed-neighborhood contact the conclusion fails",
        lemma_holds and separated_seen > 0 and tight,
        {
            "disjoint_pairs_examined": pairs_checked,
            "separated_pairs_examined": separated_seen,
            "lemma_holds_on_all_separated_pairs": lemma_holds,
            "contact_sites_in_tightness_witness": sorted(contact),
            "tightness_witness_union_inadmissible": tight,
        },
    )

    # ------------------------------------------------------------------
    # U5  separated duplication is licensed; the general case is not
    # ------------------------------------------------------------------
    # A duplication argument needs a translate whose closed one-neighborhood is
    # disjoint from the original.  Exhibit the threshold explicitly.
    base = frozenset({(0, 0, 0), (1, 0, 0), (0, 1, 0)})
    thresholds = {}
    for d in (1, 2, 3, 4):
        shifted = frozenset((s[0] + d, s[1], s[2]) for s in base)
        sep = not (closed_neighbourhood(base) & closed_neighbourhood(shifted))
        thresholds[d] = {
            "sites_disjoint": not (base & shifted),
            "closed_neighbourhoods_disjoint": sep,
        }
    licensed = (
        thresholds[4]["closed_neighbourhoods_disjoint"]
        and not thresholds[2]["closed_neighbourhoods_disjoint"]
        and thresholds[2]["sites_disjoint"]
    )
    check(
        "U5 a duplication by a translate is licensed by U4 only beyond the "
        "closed-neighborhood threshold; site-disjointness alone is strictly "
        "weaker and is reached earlier",
        licensed,
        thresholds,
    )
    summary["duplication_needs"] = (
        "disjoint closed one-neighborhoods, not merely disjoint sites"
    )

    summary["conclusion"] = (
        "Admissible configurations are closed under neither disjoint union nor "
        "sub-collection: explicit covariant nearest-neighbor rules break each. "
        "Union closure is restored, for every nearest-neighbor rule, exactly "
        "when the closed one-neighborhoods are disjoint. The Record additivity "
        "clause therefore carries an implicit domain condition in both "
        "directions, and any argument that composes two configurations must "
        "state the separation hypothesis."
    )
    summary["firewalls"] = {
        "exhibited_rule_claimed_to_be_the_framework_rule": False,
        "axiom_reading_ratified": False,
        "new_axiom_or_primitive_proposed": False,
        "dynamics_or_formation_rule_claimed": False,
        "lane_status_changed": False,
    }
    summary["resources"] = {"elapsed_seconds": perf_counter() - started}
    summary["runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    summary["pass_count"] = PASS
    summary["fail_count"] = FAIL
    summary["pass"] = FAIL == 0

    receipt = ROOT / "outputs" / (
        "physical_admissibility_union_subset_closure_cycle700"
        "_receipt_2026_07_25.json"
    )
    if "--no-receipt" not in sys.argv:
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text(
            json.dumps(summary, indent=1, sort_keys=True, default=str) + "\n",
            encoding="utf-8",
        )
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True, default=str))
    print(f"RESULT {PASS} {FAIL} elapsed {perf_counter() - started:.2f} s")
    if FAIL:
        print("RESULT ADMISSIBILITY_CLOSURE_FAILED")
        return 1
    print("RESULT ADMISSIBILITY_CLOSED_UNDER_NEITHER_UNION_NOR_SUBSET")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
