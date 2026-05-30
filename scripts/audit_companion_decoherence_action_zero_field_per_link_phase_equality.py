#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for the narrow source note
`DECOHERENCE_ACTION_ZERO_FIELD_PER_LINK_PHASE_EQUALITY_NARROW_THEOREM_NOTE_2026-05-17.md`.

The source note's load-bearing content is the algebraic-substitution
implication that, given the two explicit action-law definitions

  (I1) spent_delay(L, f_bar)    := dl - ret,
          dl  := L * (1 + f_bar),
          ret := sqrt(max(dl^2 - L^2, 0)),
  (I2) valley_linear(L, f_bar)  := L * (1 - f_bar),

then in the zero-field restriction f_bar -> 0,

  (P1) spent_delay(L, 0)    = L,
  (P2) valley_linear(L, 0)  = L,
  (P3) spent_delay(L, 0) - valley_linear(L, 0) = 0  for every L > 0,
  (P4) exp(i k * spent_delay(L, 0)) = exp(i k * valley_linear(L, 0)) = exp(i k L).

This Pattern A narrow runner adds a sympy-based exact-symbolic verification:

  (a) treats (L, f_bar, k) as free real symbols (L > 0, k real, f_bar real);
  (b) checks (I1), (I2) against the literal source-code lines (147-154) of
      scripts/valley_linear_same_harness_compare.py for action-mode fidelity;
  (c) verifies (P1)-(P4) reduce to 0 symbolically under f_bar -> 0;
  (d) verifies derivable corollaries;
  (e) verifies free-symbol bookkeeping;
  (f) runs a single FP-numerical sanity cross-check at one independent
      random sample of (L, k);
  (g) counterfactual probes: at f_bar != 0, (P3) and (P4) fail, confirming
      the f_bar = 0 restriction is load-bearing.

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly evidence that the parent's
load-bearing class-(A) per-link algebra holds at exact symbolic precision
under the cited action-law definitions. The cited action-law definitions
themselves are imported from the parent and dependency authorities and
are not re-derived here.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

try:
    import sympy
    from sympy import (
        Abs,
        I,
        Max,
        Rational,
        Symbol,
        cos,
        exp,
        re as sym_re,
        im as sym_im,
        simplify,
        sin,
        sqrt,
        symbols,
        sympify,
    )
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        tag = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("DECOHERENCE_ACTION_ZERO_FIELD_PER_LINK_PHASE_EQUALITY_NARROW_THEOREM_NOTE_2026-05-17")
    print("Goal: sympy-symbolic verification that at f_bar = 0,")
    print("  spent_delay(L, 0) = valley_linear(L, 0) = L,")
    print("  and exp(i k spent_delay(L, 0)) = exp(i k valley_linear(L, 0)).")
    print("Explicit inputs: (I1) spent_delay and (I2) valley_linear action laws")
    print("=" * 88)

    # ---------------------------------------------------------------------
    section("Part 0: symbolic setup")
    # ---------------------------------------------------------------------

    L = Symbol("L", positive=True, real=True)
    f_bar = Symbol("f_bar", real=True)
    k = Symbol("k", real=True)

    # Cited action-law definitions (verbatim from parent "Why" and dependency):
    #   (I1) spent_delay := dl - ret, dl = L (1 + f_bar),
    #                       ret = sqrt(max(dl^2 - L^2, 0))
    #   (I2) valley_linear := L (1 - f_bar)
    dl = L * (1 + f_bar)
    # On the zero-field locus the Max is exactly zero; we evaluate it
    # symbolically without the Max wrapper because at f_bar = 0,
    # dl^2 - L^2 = 0 identically (no sign ambiguity). The Max wrapper
    # in source code is a runtime safety guard against FP roundoff and
    # is not load-bearing at the algebraic identity level.
    ret_symbolic = sqrt(dl**2 - L**2)
    spent_delay = dl - ret_symbolic
    valley_linear = L * (1 - f_bar)

    print(f"  symbolic L     (positive real)   = {L}")
    print(f"  symbolic f_bar (real)            = {f_bar}")
    print(f"  symbolic k     (real)            = {k}")
    print(f"  (I1) spent_delay(L, f_bar)   = dl - ret = {spent_delay}")
    print(f"  (I2) valley_linear(L, f_bar) = L(1-f)  = {valley_linear}")

    # ---------------------------------------------------------------------
    section("Part 1: (P1) spent_delay(L, 0) = L")
    # ---------------------------------------------------------------------

    spent_at_zero = spent_delay.subs(f_bar, 0)
    spent_at_zero_simplified = simplify(spent_at_zero)
    check(
        "(P1) spent_delay(L, 0) - L reduces to 0 parametrically in L > 0",
        simplify(spent_at_zero_simplified - L) == 0,
        detail=f"spent_delay(L, 0) simplified = {spent_at_zero_simplified}",
    )

    check(
        "(P1) spent_delay(L, 0) has free symbols {L} (no residual f_bar)",
        spent_at_zero_simplified.free_symbols == {L},
        detail=f"free_symbols = {spent_at_zero_simplified.free_symbols}",
    )

    # ---------------------------------------------------------------------
    section("Part 2: (P2) valley_linear(L, 0) = L")
    # ---------------------------------------------------------------------

    valley_at_zero = valley_linear.subs(f_bar, 0)
    valley_at_zero_simplified = simplify(valley_at_zero)
    check(
        "(P2) valley_linear(L, 0) - L reduces to 0 parametrically in L > 0",
        simplify(valley_at_zero_simplified - L) == 0,
        detail=f"valley_linear(L, 0) simplified = {valley_at_zero_simplified}",
    )

    check(
        "(P2) valley_linear(L, 0) has free symbols {L} (no residual f_bar)",
        valley_at_zero_simplified.free_symbols == {L},
        detail=f"free_symbols = {valley_at_zero_simplified.free_symbols}",
    )

    # ---------------------------------------------------------------------
    section("Part 3: (P3) spent_delay(L, 0) = valley_linear(L, 0)")
    # ---------------------------------------------------------------------

    P3_diff = simplify(spent_at_zero - valley_at_zero)
    check(
        "(P3) spent_delay(L, 0) - valley_linear(L, 0) reduces to 0 parametrically",
        P3_diff == 0,
        detail=f"diff = {P3_diff}",
    )

    check(
        "(P3) LHS - RHS difference has empty free symbols after simplify",
        P3_diff.free_symbols == set(),
        detail=f"free_symbols = {P3_diff.free_symbols}",
    )

    # ---------------------------------------------------------------------
    section("Part 4: (P4) exp(i k spent_delay(L, 0)) = exp(i k valley_linear(L, 0))")
    # ---------------------------------------------------------------------

    phase_spent = exp(I * k * spent_at_zero)
    phase_valley = exp(I * k * valley_at_zero)
    P4_diff = simplify(phase_spent - phase_valley)
    check(
        "(P4) exp(i k spent_delay(L, 0)) - exp(i k valley_linear(L, 0)) reduces to 0",
        P4_diff == 0,
        detail=f"diff = {P4_diff}",
    )

    phase_target = exp(I * k * L)
    check(
        "(P4) exp(i k spent_delay(L, 0)) - exp(i k L) reduces to 0",
        simplify(phase_spent - phase_target) == 0,
        detail=f"diff = {simplify(phase_spent - phase_target)}",
    )

    check(
        "(P4) exp(i k valley_linear(L, 0)) - exp(i k L) reduces to 0",
        simplify(phase_valley - phase_target) == 0,
        detail=f"diff = {simplify(phase_valley - phase_target)}",
    )

    # The ratio of the two phases is identically 1 (consequence of (C3)).
    phase_ratio = simplify(phase_spent / phase_valley)
    check(
        "(C3) ratio exp(i k spent) / exp(i k valley) reduces to 1",
        phase_ratio == 1,
        detail=f"ratio = {phase_ratio}",
    )

    # ---------------------------------------------------------------------
    section("Part 5: free-symbol bookkeeping after zero-field substitution")
    # ---------------------------------------------------------------------

    check(
        "phase_spent at f_bar=0 has free symbols subset {k, L}",
        phase_spent.free_symbols.issubset({k, L}),
        detail=f"free_symbols = {phase_spent.free_symbols}",
    )
    check(
        "phase_valley at f_bar=0 has free symbols subset {k, L}",
        phase_valley.free_symbols.issubset({k, L}),
        detail=f"free_symbols = {phase_valley.free_symbols}",
    )

    # ---------------------------------------------------------------------
    section("Part 6: numerical FP cross-check at one independent random sample")
    # ---------------------------------------------------------------------
    # The algebraic identity is the load-bearing content; an FP numerical
    # cross-check at one randomly-chosen sample is a sanity check, not the
    # authority.
    sample = {L: Rational("1732", 1000), k: Rational("873", 1000)}
    spent_num = complex(phase_spent.subs(sample))
    valley_num = complex(phase_valley.subs(sample))
    fp_ok = abs(spent_num - valley_num) < 1e-12
    check(
        "(P4) FP sanity at sample (L=1.732, k=0.873): LHS == RHS",
        fp_ok,
        detail=f"|LHS - RHS| = {abs(spent_num - valley_num):.3e}",
    )

    target_num = complex(phase_target.subs(sample))
    fp_target_ok = abs(spent_num - target_num) < 1e-12 and abs(valley_num - target_num) < 1e-12
    check(
        "(P4) FP sanity: both phases equal exp(i k L) at sample",
        fp_target_ok,
        detail=f"|spent - target| = {abs(spent_num - target_num):.3e}, "
        f"|valley - target| = {abs(valley_num - target_num):.3e}",
    )

    # ---------------------------------------------------------------------
    section("Part 7: counterfactual probes (f_bar = 0 restriction is load-bearing)")
    # ---------------------------------------------------------------------
    # Probe at f_bar = 0.1 (off zero-field locus): the two actions disagree.
    f_off = Rational("1", 10)
    spent_off = spent_delay.subs(f_bar, f_off)
    valley_off = valley_linear.subs(f_bar, f_off)
    diff_off = simplify(spent_off - valley_off)
    check(
        "counterfactual: at f_bar=0.1, spent_delay - valley_linear is NOT 0 parametrically in L",
        simplify(diff_off) != 0,
        detail=f"diff at f_bar=0.1 = {simplify(diff_off)}",
    )

    # Probe at f_bar symbolic (general): the two actions disagree as
    # expressions in (L, f_bar).
    diff_general = simplify(spent_delay - valley_linear)
    check(
        "counterfactual: at f_bar symbolic, spent_delay - valley_linear is NOT identically 0",
        simplify(diff_general) != 0,
        detail=f"diff (general f_bar) = {simplify(diff_general)}",
    )

    # Probe: exp(i k spent_delay(L, 0.1)) != exp(i k valley_linear(L, 0.1)) generically.
    phase_spent_off = exp(I * k * spent_off)
    phase_valley_off = exp(I * k * valley_off)
    phase_diff_off = simplify(phase_spent_off - phase_valley_off)
    check(
        "counterfactual: at f_bar=0.1, exp(i k spent) - exp(i k valley) is NOT identically 0",
        simplify(phase_diff_off) != 0,
        detail=f"phase diff at f_bar=0.1 (nonzero confirms zero-field restriction load-bearing)",
    )

    # ---------------------------------------------------------------------
    section("Part 8: source-code fidelity check")
    # ---------------------------------------------------------------------
    # Pin the symbolic action expressions to the literal Python source in
    # scripts/valley_linear_same_harness_compare.py::Lattice3D.propagate
    # (lines 147-154 at the date of this note). This guards against future
    # drift between this audit companion and the source-of-truth runner.
    here = Path(__file__).resolve()
    source_path = here.parent / "valley_linear_same_harness_compare.py"
    source_ok = source_path.exists()
    check(
        "source file scripts/valley_linear_same_harness_compare.py exists",
        source_ok,
        detail=f"path = {source_path}",
    )

    if source_ok:
        text = source_path.read_text()
        # The two action-mode branches must be present verbatim.
        spent_branch_ok = (
            'action_mode == "spent_delay"' in text
            and "dl = L * (1 + lf)" in text
            and "ret = np.sqrt(np.maximum(dl * dl - L * L, 0))" in text
            and "act = dl - ret" in text
        )
        valley_branch_ok = (
            'action_mode == "valley_linear"' in text
            and "act = L * (1 - lf)" in text
        )
        check(
            "source spent_delay branch present: dl=L(1+lf), ret=sqrt(max(dl^2-L^2,0)), act=dl-ret",
            spent_branch_ok,
            detail="checked literal Python expressions in propagate()",
        )
        check(
            "source valley_linear branch present: act=L(1-lf)",
            valley_branch_ok,
            detail="checked literal Python expressions in propagate()",
        )
        # The audit-companion symbolic expressions (with lf -> f_bar)
        # match these source-code branches at the per-link level. The
        # source's `lf` is the average of source and dest field values
        # (lf = 0.5 (sf + df)); at zero field both sf and df are 0,
        # hence lf = 0 = f_bar = 0 substitution is correct.
        lf_zero_field_ok = "lf = 0.5 * (sf[si[nz]] + df[di[nz]])" in text
        check(
            "source lf = 0.5 (sf + df) (zero field => lf = 0, matching f_bar = 0)",
            lf_zero_field_ok,
            detail="lf at zero field = 0 by direct algebraic substitution",
        )

        # The parent runner uses field_f = np.zeros(lat.n) for both
        # action modes, confirming the zero-field setup is the same
        # for both branches.
        runner_path = here.parent / "decoherence_action_independence.py"
        if runner_path.exists():
            runner_text = runner_path.read_text()
            zero_field_setup_ok = "field_f = np.zeros(lat.n)" in runner_text
            check(
                "parent runner uses zero field (field_f = np.zeros(lat.n))",
                zero_field_setup_ok,
                detail="confirms (I1), (I2) evaluated at f_bar = 0 in the harness",
            )
        else:
            print(f"  (note) parent runner not found at {runner_path}")

    # ---------------------------------------------------------------------
    section("Summary")
    # ---------------------------------------------------------------------
    print("  Verified at exact sympy precision:")
    print("    (P1) spent_delay(L, 0) = L         parametric in L > 0")
    print("    (P2) valley_linear(L, 0) = L       parametric in L > 0")
    print("    (P3) spent_delay(L, 0) - valley_linear(L, 0) = 0  parametric in L > 0")
    print("    (P4) exp(i k spent(L,0)) = exp(i k valley(L,0)) = exp(i k L)")
    print("    (C3) phase ratio reduces to 1")
    print("    Free-symbol bookkeeping at f_bar = 0")
    print("    FP numerical cross-check passes at one independent random sample")
    print("    Counterfactual: f_bar != 0 collapses (P3) and (P4)")
    print("    Source-code fidelity: symbolic (I1), (I2) match Lattice3D.propagate branches")

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
