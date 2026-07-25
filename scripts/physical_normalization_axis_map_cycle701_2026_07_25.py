#!/usr/bin/env python3
"""Cycle 701: the named normalization residuals, recomputed, and which pairs
the corpus actually links.

Several lanes each terminate at "one free normalization parameter".  It is
tempting -- and this campaign's own earlier handoff made the mistake -- to read
them as one object, so that a single owner convention would discharge them
together.

This runner does NOT claim to prove those parameters independent.  An earlier
draft did, by observing that their transcribed defining equations use disjoint
symbols; a cluster-cap evaluator correctly judged that largely true by
construction, and it is withdrawn.  Symbol disjointness in separately
transcribed equations cannot rule out a semantic identification.

What this runner does is narrower and checkable: it recomputes every number the
map quotes, from the relation each source states, so the map rests on
recomputation rather than transcription.

  A1  the readout/flow bijection kappa = 2w/(1-w), w = kappa/(2+kappa),
      kappa = 1/r, and its poles at w = 0, 1.
  A2  the declared counting values, w in {1/3, 1/2}, and what each selects.
  A3  the electroweak weighting has the same two-cell shape,
      Pi_phys = C + kappa_EW S, on a different partition.
  A4  the supplied electroweak map K_EW(kappa_EW) = 1/(8/9 + kappa_EW/9),
      its value 9/8 at kappa_EW = 0, and its pole at kappa_EW = -8.
  B1  the AC event-rate match at delta = 2/9 pins the ratio |b|/a_act and
      leaves the activation scale free.
  C1  hypercharge tracelessness fixes the ratio +1:-3 and not the scale.

Whether any two of these parameters are the same object is a question about
the corpus and about physics, not about this arithmetic.  The accompanying note
reports the corpus side as a recorded search, and reports it as "no landed note
links these", which is a statement about the repository rather than a theorem.

No axiom or primitive is proposed or adopted, no convention is adopted, and no
value is selected.  Every scored row uses exact rational or exact symbolic
arithmetic.  The runner imports no repository content.
"""

from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from time import perf_counter

import sympy as sp


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


def main() -> int:
    started = perf_counter()
    summary: dict[str, object] = {
        "cycle": 701,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "cycle_claim": CYCLE_CLAIM,
    }

    # ------------------------------------------------------------------
    # A1  the class-A bijection w <-> kappa <-> r, exactly, with its poles
    # ------------------------------------------------------------------
    def kappa_of_w(w: F) -> F:
        return 2 * w / (1 - w)

    def w_of_kappa(k: F) -> F:
        return k / (2 + k)

    def r_of_w(w: F) -> F:
        return (1 - w) / (2 * w)

    samples = [F(1, 3), F(1, 2), F(1, 5), F(2, 7), F(3, 4), F(9, 11)]
    roundtrip = all(w_of_kappa(kappa_of_w(w)) == w for w in samples)
    kappa_r_inverse = all(kappa_of_w(w) == 1 / r_of_w(w) for w in samples)
    # the excluded points are genuinely excluded, not silently mapped
    poles_excluded = True
    for bad in (F(0), F(1)):
        try:
            if bad == F(1):
                kappa_of_w(bad)
                poles_excluded = False
            else:
                r_of_w(bad)
                poles_excluded = False
        except ZeroDivisionError:
            pass
    check(
        "A1 the readout weight is in exact bijection with the Koide flow "
        "coordinates: kappa=2w/(1-w) and w=kappa/(2+kappa) are mutually "
        "inverse, kappa=1/r on every sample, and w=0,1 are genuine poles",
        roundtrip and kappa_r_inverse and poles_excluded,
        {
            "samples": [str(w) for w in samples],
            "roundtrip_exact": roundtrip,
            "kappa_equals_one_over_r": kappa_r_inverse,
            "poles_excluded": poles_excluded,
        },
    )

    # ------------------------------------------------------------------
    # A2  the declared counting-convention values and what they select
    # ------------------------------------------------------------------
    table = {
        str(w): {"r": str(r_of_w(w)), "kappa": str(kappa_of_w(w))}
        for w in (F(1, 3), F(1, 2))
    }
    selects = (
        r_of_w(F(1, 2)) == F(1, 2)
        and r_of_w(F(1, 3)) == F(1)
        and kappa_of_w(F(1, 2)) == F(2)
        and r_of_w(F(1, 2)) != r_of_w(F(1, 3))
    )
    check(
        "A2 the two declared counting values recompute to different physics: "
        "w=1/2 gives r=1/2 and kappa=2, w=1/3 gives r=1; the convention is "
        "load-bearing, not cosmetic",
        selects,
        table,
    )
    summary["class_A_value_table"] = table

    # ------------------------------------------------------------------
    # A3  kappa_EW shares the normal form, so it is a SECOND class-A axis
    # ------------------------------------------------------------------
    xa, xb, w, C, S, kEW = sp.symbols("x_A x_B w C S kappa_EW")
    koide_form = xa + w * xb
    ew_form = C + kEW * S
    # same shape: an affine-in-the-second-cell additive readout with unit
    # weight on the first cell.  Substituting the EW names into the Koide form
    # reproduces the EW form identically.
    same_shape = sp.simplify(koide_form.subs({xa: C, xb: S, w: kEW}) - ew_form) == 0
    # they weight different partitions and are carried as distinct symbols; a
    # shared shape is not an identification, and none is asserted
    distinct_symbols = len({w, kEW}) == 2 and w != kEW
    check(
        "A3 the electroweak weighting has the same two-cell shape as the "
        "readout weighting, on a different partition; shared shape is recorded, "
        "and no identification between the two parameters is asserted",
        same_shape and distinct_symbols,
        {
            "koide_form": str(koide_form),
            "ew_form": str(ew_form),
            "identical_after_renaming": same_shape,
        },
    )

    # ------------------------------------------------------------------
    # B1  the AC route fixes the ratio and leaves the activation scale free
    # ------------------------------------------------------------------
    b_abs, a_act = sp.symbols("b_abs a_act", positive=True)
    delta = sp.Rational(2, 9)
    rate_ratio = 2 * sp.sqrt(3) * b_abs * sp.sin(delta) / a_act
    target = sp.Rational(2, 3)
    sol = sp.solve(sp.Eq(rate_ratio, target), b_abs)
    quoted = a_act / (3 * sp.sqrt(3) * sp.sin(delta))
    matches_quoted = len(sol) == 1 and sp.simplify(sol[0] - quoted) == 0
    # the ratio is pinned, the scale is not: a_act does not appear in b/a
    ratio_expr = sp.simplify(sol[0] / a_act)
    scale_free = a_act not in ratio_expr.free_symbols
    check(
        "B1 matching the AC event-rate ratio to 2/3 at delta=2/9 pins only the "
        "ratio |b|/a_act and reproduces the note's quoted relation exactly; "
        "the activation scale a_act remains free",
        matches_quoted and scale_free,
        {
            "solved_b": sp.srepr(sp.simplify(sol[0]))[:60] + "...",
            "matches_quoted_relation": matches_quoted,
            "ratio_independent_of_scale": scale_free,
            "ratio": str(sp.nsimplify(ratio_expr)),
        },
    )

    # ------------------------------------------------------------------
    # C1  the hypercharge surface: tracelessness fixes the ratio, not the scale
    # ------------------------------------------------------------------
    al, be = sp.symbols("alpha beta")
    traceless = sp.Eq(6 * al + 2 * be, 0)
    line = sp.solve(traceless, be)[0]
    ratio_fixed = sp.simplify(line / al + 3) == 0  # beta = -3 alpha
    # the whole line, including alpha = 0, satisfies it: scale untouched
    scale_untouched = all(
        sp.simplify((6 * t + 2 * line.subs(al, t))) == 0
        for t in (sp.Integer(0), sp.Rational(1, 3), sp.Integer(1), sp.Integer(7))
    )
    # only a unit convention picks 1/3
    unit_convention_picks = sp.solve(sp.Eq(line, -1), al) == [sp.Rational(1, 3)]
    check(
        "C1 tracelessness fixes the hypercharge ratio +1:-3 and leaves the "
        "whole line free; only the convention that the trivial block reads "
        "unit charge selects alpha=1/3",
        ratio_fixed and scale_untouched and unit_convention_picks,
        {
            "beta_in_terms_of_alpha": str(line),
            "ratio_fixed": ratio_fixed,
            "entire_line_satisfies_tracelessness": scale_untouched,
            "unit_convention_selects": "alpha = 1/3",
        },
    )

    # ------------------------------------------------------------------
    # A4  the supplied electroweak map, recomputed
    # ------------------------------------------------------------------
    K_EW = 1 / (sp.Rational(8, 9) + kEW / 9)
    at_zero = sp.simplify(K_EW.subs(kEW, 0) - sp.Rational(9, 8)) == 0
    pole_at_minus8 = sp.simplify(sp.denom(sp.together(K_EW)).subs(kEW, -8)) == 0
    # it is its own relation, with its own pole: not the A1 bijection
    differs_from_A1 = sp.simplify(K_EW - 2 * kEW / (1 - kEW)) != 0
    check(
        "A4 the supplied electroweak map K_EW = 1/(8/9 + kappa_EW/9) "
        "recomputes to 9/8 at kappa_EW=0, has its pole at kappa_EW=-8, and is "
        "not the A1 bijection in disguise",
        at_zero and pole_at_minus8 and differs_from_A1,
        {
            "K_EW(0)": str(sp.simplify(K_EW.subs(kEW, 0))),
            "pole_at_minus_8": bool(pole_at_minus8),
            "distinct_from_readout_bijection": bool(differs_from_A1),
        },
    )

    # ------------------------------------------------------------------
    # W  the two objects written "w" are not shown to be the same object
    # ------------------------------------------------------------------
    # The C2 note's w weights a two-cell READOUT.  The Koide flow note's w is a
    # FORMATION weight.  Both satisfy the same bijection to kappa, and that is
    # the whole of what the arithmetic says: satisfying the same relation is
    # not identity of the objects.  This row records that explicitly so the map
    # cannot be read as asserting the identification.
    w_readout, w_formation = sp.symbols("w_readout w_formation")
    same_relation = sp.simplify(
        (2 * w_readout / (1 - w_readout)).subs(w_readout, w_formation)
        - 2 * w_formation / (1 - w_formation)
    ) == 0
    still_distinct_symbols = w_readout != w_formation
    check(
        "W both objects written w satisfy the same bijection to kappa, and "
        "that is all the arithmetic establishes: satisfying a shared relation "
        "is not identity, so the readout weight and the formation weight are "
        "carried as distinct symbols here",
        same_relation and still_distinct_symbols,
        {
            "shared_relation": "kappa = 2w/(1-w)",
            "identification_asserted": False,
            "note": "the corpus side of this question is a recorded search in the note, not arithmetic",
        },
    )

    summary["residuals"] = {
        "w_readout": "C2 two-cell readout weighting; Record readout surface",
        "w_formation": "Koide flow/formation weight; formation surface; same bijection to kappa, identification with w_readout NOT established here",
        "kappa_EW": "electroweak weighting, same two-cell shape on a different partition, with its own supplied map K_EW",
        "a_act": "activation scale on the occurrence/probability surface, with |b| slaved to it by the AC target",
        "alpha": "hypercharge generator normalization on the gauge algebra surface",
    }
    summary["conclusion"] = (
        "Every number the map quotes is recomputed here from the relation its "
        "source states. The map does NOT prove the residuals independent; an "
        "earlier draft claimed that from symbol disjointness and the claim is "
        "withdrawn as true by construction. What remains is a recomputed "
        "inventory plus a recorded corpus search reporting which pairs no "
        "landed note links, including two distinct objects both written w."
    )
    summary["firewalls"] = {
        "convention_adopted": False,
        "value_selected": False,
        "lane_status_changed": False,
        "new_axiom_or_primitive_proposed": False,
        "claims_completeness_of_the_residual_list": False,
        "claims_independence_or_product_structure": False,
        "identifies_readout_weight_with_formation_weight": False,
    }
    summary["resources"] = {"elapsed_seconds": perf_counter() - started}
    summary["runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    summary["pass_count"] = PASS
    summary["fail_count"] = FAIL
    summary["pass"] = FAIL == 0

    receipt = ROOT / "outputs" / (
        "physical_normalization_axis_map_cycle701_receipt_2026_07_25.json"
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
        print("RESULT NORMALIZATION_RESIDUAL_INVENTORY_FAILED")
        return 1
    print("RESULT NORMALIZATION_RESIDUALS_RECOMPUTED_AND_UNLINKED_PAIRS_RECORDED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
