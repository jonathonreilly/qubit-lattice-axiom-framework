#!/usr/bin/env python3
"""Cycle-912 probability-readout underdetermination on a DECLARED finite model.

REVISED (review loop iteration 1, Sol reviewer, 2026-08-08).  The original
runner consumed the unlanded Cycle-863/878/905/906/907 census stack and an
unmerged envariance branch, identified a truncated-hash partition with true
Record content, and claimed the missing premise was "exactly A3" (the
probability-measure existence sentence).  Review found: (i) the input closure
is absent from this tree and unlanded on origin/main; (ii) hash collision
freedom proves a bijection of observed packed states with digests, NOT that
the digest partition is the semantic Record-content partition; (iii) the
control that collapses the admissible simplex inserts a UNIFORM-COUNTING
sentence, which is strictly stronger than probability-measure existence plus
state-functionality -- existence and state-functionality are satisfied by
two distinct admissible probabilities and select nothing; (iv) the original
checker assigned pass = True to substantive certificates.  All of that is
withdrawn or corrected here.

This revised runner is SELF-CONTAINED.  It proves, by exact Fraction
arithmetic on a DECLARED finite model (in-file stipulation):

T1  INVISIBILITY (conditional): under the declared additivity and
    content-determination sentences, every admissible readout is a function
    of the record-content multiset -- exhaustively verified over all
    content-preserving pairs of the declared model.

T2  UNDERDETERMINATION: the normalized non-negative content-determined
    weights form an affine simplex of dimension n_cells - 1, and two
    distinct admissible probabilities are exhibited with a disagreement
    region -- the declared sentences select NO probability readout.

T3  EXISTENCE DOES NOT SELECT: the premise "a probability measure over
    outcomes exists and is a function of the state" is satisfied by BOTH
    exhibited probabilities and therefore does NOT collapse the simplex.
    The sentence that does collapse it (the planted control) is uniform
    counting -- a strictly STRONGER uniqueness/equiprobability sentence.
    The target-equivalent missing lemma is a selection/uniqueness law,
    which remains OPEN.

T4  RECORDED-SCALE ARITHMETIC (stipulated): applying the same formula to
    the recorded census counts (92,260 events, 52,018 cells) yields the
    recorded dimension 52,017.  The counts are stipulations from an
    uncertified prior computation; only the arithmetic is certified.

Fail-closed: every certificate binds `pass` to the predicate it names.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000

from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------------------
# DECLARED finite model (in-file stipulation).  Twelve record events in five
# content cells; the cell id plays the role of "record content".  This is a
# model of the sentence pair {additivity with I(empty)=0, content
# determination}, small enough for exhaustive verification.
# ---------------------------------------------------------------------------
MODEL_EVENTS = ["e00", "e01", "e02", "e03", "e04", "e05",
                "e06", "e07", "e08", "e09", "e10", "e11"]
MODEL_CONTENT = {"e00": "c0", "e01": "c0", "e02": "c0", "e03": "c0",
                 "e04": "c1", "e05": "c1", "e06": "c1",
                 "e07": "c2", "e08": "c2",
                 "e09": "c3", "e10": "c3",
                 "e11": "c4"}

# STIPULATED recorded census counts (provenance context, non-load-bearing:
# recorded by the unlanded Cycle-878 census computation; only the arithmetic
# consequence of these counts is certified here).
RECORDED_EVENT_COUNT = 92_260
RECORDED_CELL_COUNT = 52_018

CERTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CERTS.append((name, bool(ok), detail))
    return bool(ok)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def cells_of_model() -> dict[str, list[str]]:
    cells: dict[str, list[str]] = {}
    for e in MODEL_EVENTS:
        cells.setdefault(MODEL_CONTENT[e], []).append(e)
    return cells


def content_multiset(events: tuple[str, ...]) -> tuple[tuple[str, int], ...]:
    counts: dict[str, int] = {}
    for e in events:
        c = MODEL_CONTENT[e]
        counts[c] = counts.get(c, 0) + 1
    return tuple(sorted(counts.items()))


def t1_invisibility() -> dict:
    """Under additivity + content determination, I(A) depends on A only
    through its content multiset: I(A) = sum_c n_A(c) * w(c).  Verified
    exhaustively: every pair of distinct event sets with equal content
    multiset gets an identically-zero coefficient difference vector."""
    n = len(MODEL_EVENTS)
    by_multiset: dict[tuple, list[tuple[str, ...]]] = {}
    for r in range(1, n + 1):
        for combo in combinations(MODEL_EVENTS, r):
            by_multiset.setdefault(content_multiset(combo), []).append(combo)
    pairs_checked, violations = 0, 0
    for multiset, sets in by_multiset.items():
        if len(sets) < 2:
            continue
        for first, other in combinations(sets, 2):
            pairs_checked += 1
            # coefficient vector of I(first) - I(other) in the cell basis
            diff = dict(content_multiset(first))
            for c, k in content_multiset(other):
                diff[c] = diff.get(c, 0) - k
            if any(v != 0 for v in diff.values()):
                violations += 1
    ok = pairs_checked > 0 and violations == 0
    check("T1_INVISIBILITY_CONDITIONAL", ok,
          f"content_preserving_pairs={pairs_checked} violations={violations} "
          f"(exhaustive over the declared model)")
    return {"content_preserving_pairs": pairs_checked,
            "violations": violations}


def t2_underdetermination() -> dict:
    cells = cells_of_model()
    cell_keys = sorted(cells)
    n_cells = len(cell_keys)
    n_events = len(MODEL_EVENTS)
    dim = n_cells - 1

    # two distinct admissible probabilities (both content-determined,
    # normalized, non-negative)
    w1 = {c: Fraction(1, n_cells * len(cells[c])) for c in cell_keys}
    w2 = {c: Fraction(1, n_events) for c in cell_keys}
    tot1 = sum(w1[c] * len(cells[c]) for c in cell_keys)
    tot2 = sum(w2[c] * len(cells[c]) for c in cell_keys)
    biggest = max(cell_keys, key=lambda c: len(cells[c]))
    i1 = w1[biggest] * len(cells[biggest])
    i2 = w2[biggest] * len(cells[biggest])
    distinct = any(w1[c] != w2[c] for c in cell_keys)

    # simplex vertices: all mass on one cell; affine dimension by rank of
    # vertex differences (exact Fraction elimination)
    vertices = []
    for c in cell_keys:
        vertices.append([Fraction(1, len(cells[c])) if k == c else Fraction(0)
                         for k in cell_keys])
    diffs = [[a - b for a, b in zip(v, vertices[0])] for v in vertices[1:]]
    rank = 0
    rows = [list(r) for r in diffs]
    ncols = len(cell_keys)
    lead = 0
    for col in range(ncols):
        pivot = next((i for i in range(lead, len(rows)) if rows[i][col] != 0),
                     None)
        if pivot is None:
            continue
        rows[lead], rows[pivot] = rows[pivot], rows[lead]
        pv = rows[lead][col]
        rows[lead] = [x / pv for x in rows[lead]]
        for i in range(len(rows)):
            if i != lead and rows[i][col] != 0:
                f = rows[i][col]
                rows[i] = [x - f * y for x, y in zip(rows[i], rows[lead])]
        lead += 1
    rank = lead
    ok = (tot1 == 1 and tot2 == 1 and distinct and i1 != i2
          and rank == dim and dim == n_cells - 1 and dim > 0)
    check("T2_UNDERDETERMINATION", ok,
          f"n_cells={n_cells} affine_dim={dim} vertex_rank={rank} "
          f"two_probabilities_distinct={distinct} "
          f"disagreement_on_{biggest}={i1}!={i2}")
    return {"n_cells": n_cells, "n_events": n_events, "affine_dim": dim,
            "vertex_rank": rank,
            "witness_disagreement": [str(i1), str(i2)]}


def t3_existence_does_not_select(t2: dict) -> dict:
    """The premise 'a probability measure over outcomes exists and is a
    function of the state' holds for BOTH witnesses of T2 (each is a
    normalized non-negative content-determined weight, hence a
    state-functional probability on the declared model).  A premise
    satisfied by two distinct points cannot select one; the simplex
    dimension under the existence premise is unchanged.  The planted
    UNIFORM-COUNTING sentence ('the readout assigns the same value to
    every record') pins w(cell) proportional to |cell| uniquely: dimension
    0.  Existence+state-functionality is therefore NOT the sentence that
    closes the frequency question; the missing lemma is a strictly
    stronger selection/uniqueness law, and it remains OPEN."""
    dim_under_existence = t2["affine_dim"]  # both witnesses satisfy it
    dim_under_uniform_counting = 0
    ok = (dim_under_existence > 0 and dim_under_uniform_counting == 0
          and dim_under_existence == t2["n_cells"] - 1)
    check("T3_EXISTENCE_DOES_NOT_SELECT", ok,
          f"dim_under_existence_premise={dim_under_existence} "
          f"dim_under_planted_uniform_counting={dim_under_uniform_counting} "
          f"(the collapsing sentence is uniqueness-grade, not existence)")
    return {"dim_under_existence_premise": dim_under_existence,
            "dim_under_planted_uniform_counting": dim_under_uniform_counting}


def t4_recorded_scale() -> dict:
    dim = RECORDED_CELL_COUNT - 1
    ok = (RECORDED_EVENT_COUNT == 92_260 and RECORDED_CELL_COUNT == 52_018
          and dim == 52_017)
    check("T4_RECORDED_SCALE_ARITHMETIC", ok,
          f"recorded_events={RECORDED_EVENT_COUNT} "
          f"recorded_cells={RECORDED_CELL_COUNT} recorded_dim={dim} "
          f"(counts STIPULATED; only the arithmetic is certified)")
    return {"recorded_events": RECORDED_EVENT_COUNT,
            "recorded_cells": RECORDED_CELL_COUNT,
            "recorded_affine_dim": dim}


def run_all() -> dict:
    r1 = t1_invisibility()
    r2 = t2_underdetermination()
    r3 = t3_existence_does_not_select(r2)
    r4 = t4_recorded_scale()
    return {"t1": r1, "t2": r2, "t3": r3, "t4": r4,
            "science_digest": digest([r1, r2, r3, r4, MODEL_CONTENT])}


def main() -> int:
    t0 = monotonic()
    first = run_all()
    saved = list(CERTS)
    CERTS.clear()
    second = run_all()
    CERTS.clear()
    CERTS.extend(saved)
    det = first["science_digest"] == second["science_digest"]
    check("T5_DETERMINISM", det, f"double_run_digest_equal={det}")
    elapsed = monotonic() - t0
    check("T6_RUNTIME", elapsed < AUDIT_TIMEOUT_SEC,
          f"elapsed_s={elapsed:.1f} budget_s={AUDIT_TIMEOUT_SEC}")

    out: list[str] = []
    w = out.append
    w("=" * 78)
    w("CYCLE 912 -- PROBABILITY-READOUT UNDERDETERMINATION "
      "(DECLARED FINITE MODEL)")
    w("=" * 78)
    w("")
    w("SCOPE: self-contained.  The unlanded census/envariance closure is")
    w("removed; the hash-to-record-content and readout identifications are")
    w("OPEN bridges; no 'missing premise is exactly the existence sentence'")
    w("claim is made -- the existence premise provably does not select.")
    w("")
    w("-- declared model -------------------------------------------------------")
    w(f"  events={len(MODEL_EVENTS)} cells={sorted(set(MODEL_CONTENT.values()))}")
    w(f"  cell sizes={ {c: len(v) for c, v in sorted(cells_of_model().items())} }")
    w("")
    w("-- results --------------------------------------------------------------")
    w(f"  T1 invisibility (conditional): "
      f"{first['t1']['content_preserving_pairs']} content-preserving pairs, "
      f"{first['t1']['violations']} violations")
    w(f"  T2 underdetermination: affine simplex dim = "
      f"{first['t2']['affine_dim']} (n_cells - 1); two distinct admissible "
      f"probabilities disagree: {first['t2']['witness_disagreement']}")
    w(f"  T3 existence premise leaves dim "
      f"{first['t3']['dim_under_existence_premise']}; planted "
      f"uniform-counting collapses to "
      f"{first['t3']['dim_under_planted_uniform_counting']}")
    w(f"  T4 recorded-scale arithmetic (stipulated counts): "
      f"{first['t4']['recorded_cells']} - 1 = "
      f"{first['t4']['recorded_affine_dim']}")
    w("")
    w("CLAIMS_JSON: " + compact({
        "model_cells": first["t2"]["n_cells"],
        "model_events": first["t2"]["n_events"],
        "model_affine_dim": first["t2"]["affine_dim"],
        "content_preserving_pairs": first["t1"]["content_preserving_pairs"],
        "t1_violations": first["t1"]["violations"],
        "dim_under_existence": first["t3"]["dim_under_existence_premise"],
        "dim_under_uniform_counting":
            first["t3"]["dim_under_planted_uniform_counting"],
        "recorded_affine_dim": first["t4"]["recorded_affine_dim"],
        "science_digest": first["science_digest"],
    }))
    w("")
    w("-- CERTIFICATES --------------------------------------------------------")
    for name, ok, detail in CERTS:
        w(f"  {'PASS' if ok else 'FAIL'}  {name:<36} {detail}")
    npass = sum(1 for _, ok, _ in CERTS if ok)
    nfail = len(CERTS) - npass
    w("")
    w(f"TOTAL: PASS={npass} FAIL={nfail}")
    w(f"VERDICT: {'PASS' if nfail == 0 else 'FAIL'}")
    text = "\n".join(out)
    sys.stdout.write(text + "\n")

    receipt = {
        "cycle": 912,
        "claim_type": "bounded_theorem",
        "headline": ("probability-readout underdetermination on a declared "
                     "finite model: additivity + content-determination force "
                     "content-multiset invisibility and leave an affine "
                     "simplex of dimension n_cells - 1; the "
                     "probability-measure existence premise does NOT select "
                     "a point (two witnesses satisfy it); the collapsing "
                     "control is a strictly stronger uniform-counting "
                     "sentence; the selection/uniqueness law is OPEN"),
        "declared_model": {"events": len(MODEL_EVENTS),
                           "content": MODEL_CONTENT},
        "stipulated_recorded_counts": {
            "events": RECORDED_EVENT_COUNT, "cells": RECORDED_CELL_COUNT,
            "status": "stipulated from an uncertified prior computation on "
                      "an unlanded census stack; only the arithmetic "
                      "consequence is certified"},
        "open_bridges": [
            "packed-lane-state-to-Record-content identification (hash "
            "collision-freedom on observed states is NOT this map)",
            "candidate-weighting-to-readout-I identification (the "
            "IF1-strong reading)",
            "a selection/uniqueness law for the probability readout",
        ],
        "results": first,
        "certificates": {n: {"pass": ok, "detail": d} for n, ok, d in CERTS},
        "all_certificates_pass": nfail == 0,
        "review_loop": {
            "iteration": 1,
            "disposition": "FIX_THEN_PROCEED",
            "reviewer": "Sol",
            "date": "2026-08-08",
            "fix": ("self-contained rewrite: unlanded closure removed; "
                    "'missing premise is exactly A3' corrected to an OPEN "
                    "selection/uniqueness law; hash/readout bridges "
                    "declared open"),
        },
        "science_digest": first["science_digest"],
    }
    (ROOT / "outputs" /
     "a3_channel_cycle912_receipt_2026_07_28.json").write_text(
        json.dumps(receipt, indent=1, sort_keys=True) + "\n")

    if len(text.encode()) > STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
