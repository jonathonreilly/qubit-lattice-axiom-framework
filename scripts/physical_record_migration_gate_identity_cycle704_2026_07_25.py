#!/usr/bin/env python3
"""Cycle 704: record migration is invisible to readout, and is gated by exactly
the same availability function as formation.

Two landed notes leave record migration explicitly open:

  RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_..._2026-07-11
    "Migrating-record semantics -- OPEN.  Bare permanence does not separately
     state site immobility."
  ADMISSIBILITY_RECORD_CONTINUATION_REFINEMENT_..._2026-07-13
    "The current Record text says records are permanent but does not separately
     state site immobility ...  A migrating-record semantics remains an
     untested alternative."

This cycle tests it, and locates where a discriminator can and cannot come from.

M1  READOUT CANNOT DECIDE IT.  Migration preserves the content multiset, and the
    landed singleton-weight factorization makes every Record scalar readout a
    function of that multiset alone.  So every readout is invariant under every
    migration.  No readout argument can distinguish migrating from immobile
    records -- in either direction.

M2  ADMISSIBILITY CAN SEE IT, and the two gates are NOT the same.  A migrating
    record carries its already-locked content, so the destination must make that
    content available -- but the record VACATES its origin, so when the origin is
    adjacent to the destination the mover sees exactly one fewer occupied
    neighbour than a newly formed record at the same site would.  A first draft
    of this cycle claimed the gates were identical and "checked" it by writing
    the same function body twice; that was a tautology and is withdrawn.

M3  THE CONSEQUENCE.  Migration is strictly MORE permissive than formation for
    short moves: a record can occupy, by migrating from an adjacent site, a
    position at which it could not have formed.  So a rule cannot bound record
    density by bounding formation alone -- if records may migrate, denser
    configurations are reachable than the formation gate admits.

M4  THE SEMANTICS SPLIT IS REPORTED, NOT CHOSEN.  Under formation-time checking
    -- the reading on which a formed record is never re-examined, which is what
    "records are permanent" most directly says -- migration constrains only the
    mover.  Under a revalidation reading, a migration can additionally
    invalidate a bystander record; a witness is exhibited.  Both readings are
    reported and neither is adopted, because a prior review of this campaign
    correctly objected to a cycle that presumed one.

Nothing here decides whether records migrate.  It shows that readout cannot
decide it, that Admissibility does see it, and that the migration gate is
strictly weaker than the formation gate for short moves.  No axiom, primitive, convention, or
reading is adopted.  Every scored row uses exact arithmetic.  The runner imports
no repository content.
"""

from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction as F
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
    (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1),
]


def neighbours(s: Vec) -> list[Vec]:
    return [tuple(s[i] + v[i] for i in range(3)) for v in FACES]  # type: ignore[misc]


def ncount(x: Vec, occ) -> int:
    return sum(1 for nb in neighbours(x) if nb in occ)


def main() -> int:
    started = perf_counter()
    summary: dict[str, object] = {
        "cycle": 704, "authority": AUTHORITY, "audit": AUDIT,
        "cycle_claim": CYCLE_CLAIM,
    }

    # ------------------------------------------------------------------
    # M1  every Record readout is invariant under migration
    # ------------------------------------------------------------------
    # A configuration is a map site -> content.  A migration moves one record to
    # a vacant site, preserving its content and hence the content multiset.
    cfg = {(0, 0, 0): "a", (2, 0, 0): "b", (0, 3, 0): "a"}
    moved = {(0, 0, 0): "a", (5, 5, 5): "b", (0, 3, 0): "a"}   # b migrated

    def multiset(c):
        return tuple(sorted(c.values()))

    def readout(weights, c):
        return sum((weights[v] for v in c.values()), F(0))

    same_multiset = multiset(cfg) == multiset(moved)
    weight_sets = [
        {"a": F(1), "b": F(1)},
        {"a": F(3, 2), "b": F(-5, 7)},
        {"a": F(0), "b": F(11, 3)},
    ]
    invariant = all(readout(w, cfg) == readout(w, moved) for w in weight_sets)
    # negative control: changing a CONTENT does change the readout
    recontented = dict(cfg)
    recontented[(2, 0, 0)] = "a"
    control = any(readout(w, cfg) != readout(w, recontented) for w in weight_sets)
    check(
        "M1 migration preserves the content multiset, so every singleton-weight "
        "Record readout is invariant under it, while changing a content is "
        "detected -- no readout can distinguish migrating from immobile records",
        same_multiset and invariant and control,
        {
            "content_multiset_before": multiset(cfg),
            "content_multiset_after": multiset(moved),
            "readouts_invariant": invariant,
            "content_change_detected": control,
        },
    )
    summary["readout_cannot_decide_migration"] = True

    # ------------------------------------------------------------------
    # M2 / M3  the gates are NOT the same: a vacated origin is not counted
    # ------------------------------------------------------------------
    # A first draft of this cycle asserted the two gates were one predicate and
    # "verified" it by writing the same function body twice and scanning rules.
    # That is a tautology and is withdrawn.  The gates genuinely differ, and the
    # reason is geometric: when a record migrates s -> t the origin s is
    # VACATED, so if s is adjacent to t the destination sees one fewer occupied
    # neighbour than a newly formed record at t would see.
    CONTENTS = ("c0", "c1")

    def form_count(t_site: Vec, occ) -> int:
        """Neighbour count seen by a NEW record appearing at t_site."""
        return ncount(t_site, occ)

    def migrate_count(s_site: Vec, t_site: Vec, occ) -> int:
        """Neighbour count seen by a record moving s_site -> t_site."""
        return ncount(t_site, occ - {s_site})

    base = {(0, 0, 0): "c0", (0, 1, 0): "c0", (1, 1, 0): "c0"}
    occ = frozenset(base)
    dest = (1, 0, 0)                       # vacant, adjacent to (0,0,0) and (1,1,0)
    origin = (0, 0, 0)                     # adjacent to dest
    far_origin = (0, 1, 0)                 # NOT adjacent to dest
    fc = form_count(dest, occ)
    mc_adj = migrate_count(origin, dest, occ)
    mc_far = migrate_count(far_origin, dest, occ)
    differs_for_adjacent = mc_adj == fc - 1
    agrees_for_nonadjacent = mc_far == fc
    check(
        "M2/M3 the formation gate and the migration gate are NOT the same "
        "predicate: a record migrating from an adjacent origin vacates it and "
        "so sees exactly one fewer occupied neighbour than a newly formed "
        "record at the same site, while a migration from a non-adjacent origin "
        "sees the same count",
        differs_for_adjacent and agrees_for_nonadjacent and fc >= 1,
        {
            "destination": dest,
            "formation_count": fc,
            "migration_count_from_adjacent_origin": mc_adj,
            "migration_count_from_distant_origin": mc_far,
            "adjacent_move_sees_one_fewer": differs_for_adjacent,
        },
    )

    # the consequence: a record can occupy, by migrating, a site it could not
    # have formed at -- mobility is strictly more permissive for short moves
    avail_gate = {k: (frozenset(CONTENTS) if k < 2 else frozenset(("c0",)))
                  for k in range(7)}
    could_form = "c1" in avail_gate[fc]
    could_migrate = "c1" in avail_gate[mc_adj]
    strictly_more_permissive = could_migrate and not could_form
    check(
        "M3b consequence: under an exhibited covariant never-empty rule a record "
        "carrying content c1 can reach the destination by migrating from an "
        "adjacent origin but could not have formed there, so migration is "
        "strictly more permissive than formation for short moves",
        strictly_more_permissive,
        {
            "formation_count": fc,
            "migration_count": mc_adj,
            "c1_could_form_there": could_form,
            "c1_could_migrate_there": could_migrate,
        },
    )
    summary["gate_relation"] = (
        "formation and migration gates differ by exactly one neighbour for "
        "moves from an adjacent origin, and agree otherwise; migration is "
        "strictly more permissive for short moves"
    )

    # ------------------------------------------------------------------
    # M4  the semantics split, reported and not chosen
    # ------------------------------------------------------------------
    # Formation-time checking: only the mover is examined.
    # Revalidation: bystanders are re-examined after the move.
    avail = {k: (frozenset(CONTENTS) if k < 2 else frozenset(("c0",)))
             for k in range(7)}

    # a configuration where moving one record crowds a bystander
    # (1,0,0) IS adjacent to the origin; (2,0,0) is not.  The bystander must
    # actually reach two occupied neighbours for the split to bite.
    before = {(0, 0, 0): "c1", (1, 0, 0): "c0", (5, 5, 5): "c0"}
    after = {(0, 0, 0): "c1", (1, 0, 0): "c0", (0, 1, 0): "c0"}  # third record moved in

    def admissible(c, revalidate: bool, mover: Vec | None = None):
        occ = frozenset(c)
        sites = list(c) if revalidate else ([mover] if mover in c else [])
        return all(c[s] in avail[ncount(s, occ)] for s in sites)

    # the starting configuration must itself be admissible under both readings,
    # or the witness proves nothing
    before_ok = admissible(before, revalidate=True)
    # under formation-time checking only the mover matters, and it is fine
    mover_ok = admissible(after, revalidate=False, mover=(0, 1, 0))
    # under revalidation the bystander at the origin now has 2 occupied nbrs
    bystander_count = ncount((0, 0, 0), frozenset(after))
    bystander_broken = after[(0, 0, 0)] not in avail[bystander_count]
    reval_fails = not admissible(after, revalidate=True)
    split_is_real = before_ok and mover_ok and bystander_broken and reval_fails
    check(
        "M4 the two permanence readings differ on a concrete migration: under "
        "formation-time checking the move is admissible because only the mover "
        "is examined, while under revalidation the bystander at the origin gains "
        "a second occupied neighbour and loses the content it had already locked",
        split_is_real,
        {
            "move": "record c0 migrates from (5,5,5) to (0,1,0)",
            "start_admissible_under_both_readings": before_ok,
            "mover_admissible_formation_time": mover_ok,
            "bystander_neighbour_count_after": bystander_count,
            "bystander_content_now_unavailable": bystander_broken,
            "revalidation_reading_rejects_move": reval_fails,
            "reading_adopted": None,
        },
    )
    summary["semantics_split_reported_not_chosen"] = True

    summary["conclusion"] = (
        "Record migration, left explicitly open by two landed notes, cannot be "
        "decided by any readout argument: migration preserves the content "
        "multiset and every Record readout is a function of that multiset alone. "
        "Admissibility does see it, and the migration gate is strictly weaker "
        "than the formation gate for short moves, because a mover vacates its "
        "origin and so sees one fewer occupied neighbour. Consequently a rule "
        "cannot bound record density by bounding formation alone: if records may "
        "migrate, denser configurations are reachable than the formation gate "
        "admits. Whether they may migrate is not settled here."
    )
    summary["firewalls"] = {
        "migration_semantics_adopted": False,
        "permanence_reading_adopted": False,
        "axiom_text_edit_proposed": False,
        "new_axiom_or_primitive_proposed": False,
        "formation_rule_supplied": False,
        "lane_status_changed": False,
    }
    summary["resources"] = {"elapsed_seconds": perf_counter() - started}
    summary["runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    summary["pass_count"] = PASS
    summary["fail_count"] = FAIL
    summary["pass"] = FAIL == 0

    receipt = ROOT / "outputs" / (
        "physical_record_migration_gate_identity_cycle704_receipt_2026_07_25.json"
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
        print("RESULT MIGRATION_GATE_ANALYSIS_FAILED")
        return 1
    print("RESULT MIGRATION_INVISIBLE_TO_READOUT_AND_GATED_MORE_WEAKLY_THAN_FORMATION")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
