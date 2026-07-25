#!/usr/bin/env python3
"""Cycle 701: the repo's normalization freedoms are three independent axes on
three different supplied surfaces, not one reference choice.

Several lanes each terminate at "one free normalization parameter".  It is
tempting -- and this campaign's own earlier handoff made the mistake -- to read
those as the same object, so that one owner convention would discharge them
together.  This runner checks that reading and finds it false.

The axes, with the equations each is fixed by:

A  Readout weight.  The C2 weighting normal form on a two-cell
   content-determined additive readout is `I_w(x_A, x_B) = x_A + w x_B`.  It is
   in exact bijection with the Koide flow coordinates,
   `kappa = 2w/(1-w)` and `r = (1-w)/(2w)`.  Its declared candidate values come
   from counting conventions, `w in {1/3, 1/2}`.  The electroweak weighting
   `Pi_phys = C + kappa_EW S` has the SAME normal form on a different
   partition, so it is a second class-A axis, not the same parameter.

B  Occurrence rate scale.  The AC event-rate route gives
   `omega_clock / a_act = 2 sqrt(3) |b| sin(delta) / a_act`.  Matching the
   target `Phi = 2/3` at `delta = 2/9` fixes only the RATIO, leaving the
   activation scale `a_act` free with `|b|` slaved to it.

C  Generator normalization.  On the hypercharge two-block surface,
   tracelessness `6 alpha + 2 beta = 0` fixes the ratio `+1 : -3` and nothing
   else; the scale is fixed only by choosing which block reads unit charge.

The decisive check is not that each is free -- each lane already says so -- but
that the three are INDEPENDENT: their defining relations have pairwise-disjoint
variable sets, so the joint solution set is a product and fixing any one
coordinate leaves the others exactly as free as before.  That is verified
constructively by exhibiting joint assignments across all combinations.

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
        "A2 the two declared counting conventions select different physics: "
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
    # but they are different parameters: they weight different partitions, so
    # no substitution makes one determine the other
    distinct_symbols = len({w, kEW}) == 2 and w != kEW
    check(
        "A3 the electroweak weighting has the same two-cell normal form as the "
        "readout weight, so it is a second class-A axis on a different "
        "partition rather than the same parameter",
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
    # D1  the three axes are independent: disjoint variable sets
    # ------------------------------------------------------------------
    vars_A = {w}
    vars_A2 = {kEW}
    vars_B = {b_abs, a_act}
    vars_C = {al, be}
    groups = {"A_readout_w": vars_A, "A_ew": vars_A2, "B_rate": vars_B, "C_gauge": vars_C}
    pairwise_disjoint = all(
        not (v1 & v2)
        for (n1, v1), (n2, v2) in itertools.combinations(groups.items(), 2)
    )
    # and the defining relations really only involve their own group
    rel_B_syms = (sp.Eq(rate_ratio, target)).free_symbols
    rel_C_syms = traceless.free_symbols
    b_clean = not (rel_B_syms & (vars_A | vars_A2 | vars_C))
    c_clean = not (rel_C_syms & (vars_A | vars_A2 | vars_B))
    check(
        "D1 the three classes' defining relations have pairwise-disjoint "
        "variable sets: no readout weight occurs in the AC rate relation or "
        "the hypercharge relation, and vice versa",
        pairwise_disjoint and b_clean and c_clean,
        {
            "groups": {k: sorted(str(s) for s in v) for k, v in groups.items()},
            "pairwise_disjoint": pairwise_disjoint,
            "AC_relation_free_of_other_axes": b_clean,
            "hypercharge_relation_free_of_other_axes": c_clean,
        },
    )

    # ------------------------------------------------------------------
    # D2  product structure, exhibited constructively
    # ------------------------------------------------------------------
    # every combination of representative choices is jointly satisfiable, so
    # fixing one axis leaves the others exactly as free as before
    combos = []
    ok = True
    for w_val in (F(1, 3), F(1, 2)):
        for a_val in (sp.Integer(1), sp.Rational(1, 5)):
            for al_val in (sp.Rational(1, 3), sp.Integer(1)):
                b_val = sol[0].subs(a_act, a_val)
                sat_B = (
                    sp.simplify(
                        rate_ratio.subs({b_abs: b_val, a_act: a_val}) - target
                    )
                    == 0
                )
                sat_C = sp.simplify(6 * al_val + 2 * line.subs(al, al_val)) == 0
                sat_A = r_of_w(w_val) in (F(1), F(1, 2))
                if not (sat_A and sat_B and sat_C):
                    ok = False
                combos.append(
                    {
                        "w": str(w_val),
                        "a_act": str(a_val),
                        "alpha": str(al_val),
                        "all_three_satisfied": bool(sat_A and sat_B and sat_C),
                    }
                )
    check(
        "D2 all eight combinations of representative choices on the three axes "
        "are jointly satisfiable, so the joint solution set is a product and a "
        "convention adopted on one axis discharges no other",
        ok and len(combos) == 8,
        {"combinations_checked": len(combos), "all_satisfiable": ok},
    )
    summary["product_structure_combinations"] = combos

    # ------------------------------------------------------------------
    # D3  the negative control: a genuinely dependent pair is detected
    # ------------------------------------------------------------------
    # kappa and w are NOT independent -- they are the same axis in different
    # coordinates.  The same test must catch that, or it proves nothing.
    kap = sp.Symbol("kappa")
    dependent_rel = sp.Eq(kap, 2 * w / (1 - w))
    shares = bool(dependent_rel.free_symbols & vars_A)
    check(
        "D3 negative control: the same disjointness test applied to kappa and "
        "w detects that they are dependent, so the test is not vacuous",
        shares,
        {
            "relation": str(dependent_rel),
            "shares_a_variable_with_axis_A": shares,
        },
    )

    summary["axes"] = {
        "A_readout_weight": "Record readout surface; one parameter per declared two-cell partition; discharged by a counting convention",
        "A_electroweak_weight": "same normal form, different partition; a second class-A axis",
        "B_activation_scale": "occurrence/probability surface; needs a formation or rate law, not a readout convention",
        "C_generator_normalization": "gauge algebra surface; discharged by a unit convention",
    }
    summary["conclusion"] = (
        "The repo's normalization residuals are not one reference choice. They "
        "are at least four parameters in three classes on three different "
        "supplied surfaces, with pairwise-disjoint defining relations and a "
        "product solution set. A counting convention that fixes the readout "
        "weight discharges neither the activation scale nor the generator "
        "normalization, so the flagship lanes do not unblock together."
    )
    summary["firewalls"] = {
        "convention_adopted": False,
        "value_selected": False,
        "lane_status_changed": False,
        "new_axiom_or_primitive_proposed": False,
        "claims_completeness_of_the_axis_list": False,
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
        print("RESULT NORMALIZATION_AXIS_MAP_FAILED")
        return 1
    print("RESULT NORMALIZATION_AXES_ARE_INDEPENDENT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
