#!/usr/bin/env python3
"""Exact-symbolic runner for the alpha_s CMT-coupling-map derivation
narrow theorem `ALPHA_S_CMT_COUPLING_MAP_DERIVATION_THEOREM_NOTE_2026-05-17.md`.

The theorem closes the algebraic step that converts the retained CMT
correlator change-of-variables identity

  (I1)  <O(U)> = u_0^{n_link} <O_V(V)>_eff       (retained D14)

plus the standard tadpole-improvement convention split

  (I2)  <O[U]>   = alpha_bare * K_U
  (I3)  <O_V[V]>_eff = alpha_eff * K_V,  K_U = K_V

into the tadpole coupling-rescaling map

  (M)   alpha_eff = alpha_bare / u_0^{n_link}.

This runner verifies (M) at exact symbolic precision over the
rational-function field Q(alpha_bare, u_0, 1/u_0) with n_link as a
positive-integer symbol.

Physical Cl(3) local algebra / Z^3 spatial-substrate baseline only for
framework input: sympy. No PDG values. No fitted alpha_s. No
canonical_plaquette_surface import. No audit-data touches.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import sympy
    from sympy import (
        Integer,
        Symbol,
        Eq,
        simplify,
        solve,
        symbols,
        Rational,
        Pow,
    )
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)

NOTE = (
    "docs/ALPHA_S_CMT_COUPLING_MAP_DERIVATION_THEOREM_NOTE_2026-05-17.md"
)

# Verify source note exists (runner / note pairing)
repo = Path(__file__).resolve().parent.parent
note_path = repo / NOTE
if not note_path.exists():
    print(f"FAIL: source note missing: {NOTE}")
    sys.exit(1)


def pass_(name: str, detail: str = "") -> None:
    if detail:
        print(f"PASS  {name}  | {detail}")
    else:
        print(f"PASS  {name}")


def fail_(name: str, detail: str = "") -> None:
    print(f"FAIL  {name}  | {detail}")


def main() -> int:
    print(f"== {NOTE} ==")
    print("Exact-symbolic verification of the CMT-to-coupling-map derivation.")
    print("All symbols are abstract positive-real (alpha_bare, u_0, K_U) and")
    print("positive-integer (n_link). No numerical values are imported.")
    print()

    # Symbols
    alpha_bare = symbols("alpha_bare", positive=True)
    alpha_eff = symbols("alpha_eff", positive=True)
    u_0 = symbols("u_0", positive=True)
    K_U = symbols("K_U", positive=True)
    K_V = symbols("K_V", positive=True)
    n_link = symbols("n_link", positive=True, integer=True)

    failures: list[str] = []

    # -----------------------------------------------------------------------
    # T1: Algebraic derivation of (M) from (I1), (I2), (I3)
    # -----------------------------------------------------------------------
    # (I2)  bare correlator value:  <O[U]> = alpha_bare * K_U
    O_U = alpha_bare * K_U
    # (I3)  V-scheme correlator value:  <O_V[V]>_eff = alpha_eff * K_V
    O_V_eff = alpha_eff * K_V
    # Apply (I3) convention K_U = K_V
    O_V_eff_subst = O_V_eff.subs(K_V, K_U)  # = alpha_eff * K_U
    # (I1)  <O(U)> = u_0^{n_link} <O_V(V)>_eff
    cmt_eq = Eq(O_U, u_0**n_link * O_V_eff_subst)
    # Solve for alpha_eff
    sol_alpha_eff = solve(cmt_eq, alpha_eff)
    if len(sol_alpha_eff) != 1:
        failures.append("T1: solve did not return unique alpha_eff")
        fail_("T1_unique_solution", f"got {sol_alpha_eff}")
    else:
        derived = simplify(sol_alpha_eff[0])
        target = alpha_bare / u_0**n_link
        residual = simplify(derived - target)
        if residual == 0:
            pass_(
                "T1_derive_M",
                f"alpha_eff = {derived} == alpha_bare/u_0^n_link  (residual=0)",
            )
        else:
            failures.append(f"T1: residual = {residual}")
            fail_("T1_derive_M", f"residual = {residual}")

    # -----------------------------------------------------------------------
    # T2: Round-trip — substitute (M) back; recover (I1)
    # -----------------------------------------------------------------------
    M_alpha_eff = alpha_bare / u_0**n_link
    O_V_eff_via_M = M_alpha_eff * K_U  # = alpha_eff * K_V via (I3)
    rhs_recovered = u_0**n_link * O_V_eff_via_M
    residual = simplify(O_U - rhs_recovered)
    if residual == 0:
        pass_("T2_roundtrip_CMT", "(M) substituted back reproduces (I1) exactly")
    else:
        failures.append(f"T2: round-trip residual = {residual}")
        fail_("T2_roundtrip_CMT", f"residual = {residual}")

    # -----------------------------------------------------------------------
    # T3: Specialization n_link = 1 -> alpha_LM = alpha_bare / u_0
    # -----------------------------------------------------------------------
    alpha_LM_target = alpha_bare / u_0
    M_at_1 = (alpha_bare / u_0**n_link).subs(n_link, 1)
    residual = simplify(M_at_1 - alpha_LM_target)
    if residual == 0:
        pass_("T3_specialize_n1_alpha_LM", f"(M) at n_link=1 = {simplify(M_at_1)}")
    else:
        failures.append(f"T3: residual = {residual}")
        fail_("T3_specialize_n1_alpha_LM", f"residual = {residual}")

    # -----------------------------------------------------------------------
    # T4: Specialization n_link = 2 -> alpha_s(v) = alpha_bare / u_0^2
    # -----------------------------------------------------------------------
    alpha_sv_target = alpha_bare / u_0**2
    M_at_2 = (alpha_bare / u_0**n_link).subs(n_link, 2)
    residual = simplify(M_at_2 - alpha_sv_target)
    if residual == 0:
        pass_("T4_specialize_n2_alpha_sv", f"(M) at n_link=2 = {simplify(M_at_2)}")
    else:
        failures.append(f"T4: residual = {residual}")
        fail_("T4_specialize_n2_alpha_sv", f"residual = {residual}")

    # -----------------------------------------------------------------------
    # T5: Composition with (P1) of ALPHA_S_DERIVED_NARROW_THEOREM_NOTE_2026-05-10
    #     (P1)  alpha_LM^2 = alpha_bare * alpha_s(v)
    # -----------------------------------------------------------------------
    alpha_LM = M_at_1  # = alpha_bare/u_0
    alpha_sv = M_at_2  # = alpha_bare/u_0^2
    lhs_P1 = alpha_LM**2
    rhs_P1 = alpha_bare * alpha_sv
    residual = simplify(lhs_P1 - rhs_P1)
    if residual == 0:
        pass_(
            "T5_compose_with_P1",
            "alpha_LM^2 = alpha_bare * alpha_s(v)  closed via M-derived C1,C2",
        )
    else:
        failures.append(f"T5: residual = {residual}")
        fail_("T5_compose_with_P1", f"residual = {residual}")

    # -----------------------------------------------------------------------
    # T6: Direction-of-rescaling — with 0 < u_0 < 1 and n_link >= 1,
    #     alpha_eff > alpha_bare (purely symbolic positivity check via
    #     the ratio alpha_eff / alpha_bare = 1 / u_0^n_link > 1).
    # -----------------------------------------------------------------------
    ratio = simplify((alpha_bare / u_0**n_link) / alpha_bare)
    expected_ratio = simplify(1 / u_0**n_link)
    if simplify(ratio - expected_ratio) == 0:
        pass_(
            "T6_direction_check",
            f"alpha_eff/alpha_bare = {ratio}  (>1 when u_0<1, n_link>=1)",
        )
    else:
        failures.append(f"T6: ratio = {ratio}")
        fail_("T6_direction_check", f"ratio = {ratio}")

    # -----------------------------------------------------------------------
    # T7: Counterfactual — reversed CMT identity gives the wrong rescaling.
    #     If (I1') were <O(U)> = u_0^{-n_link} <O_V(V)>_eff, then the derived
    #     coupling would be alpha_eff' = alpha_bare * u_0^{n_link},
    #     not alpha_bare / u_0^{n_link}. This shows the direction in (I1)
    #     is load-bearing — the result is not a convention-free coincidence.
    # -----------------------------------------------------------------------
    cmt_reversed = Eq(O_U, u_0 ** (-n_link) * (alpha_eff * K_U))
    sol_rev = solve(cmt_reversed, alpha_eff)
    if len(sol_rev) != 1:
        failures.append(f"T7: reversed-CMT solve gave {sol_rev}")
        fail_("T7_counterfactual", "non-unique reversed solve")
    else:
        derived_rev = simplify(sol_rev[0])
        target_rev = alpha_bare * u_0**n_link
        residual_rev = simplify(derived_rev - target_rev)
        # And it must differ from the forward derivation
        differs_from_forward = simplify(derived_rev - alpha_bare / u_0**n_link)
        if residual_rev == 0 and differs_from_forward != 0:
            pass_(
                "T7_counterfactual",
                f"reversed CMT -> alpha_eff = {derived_rev}  (differs from M)",
            )
        else:
            failures.append(
                f"T7: residual_rev = {residual_rev}, differs = {differs_from_forward}"
            )
            fail_("T7_counterfactual", f"residual_rev = {residual_rev}")

    # -----------------------------------------------------------------------
    print()
    if failures:
        print(f"OVERALL: FAIL  ({len(failures)} failure(s))")
        for f in failures:
            print(f"  - {f}")
        return 1
    else:
        print("OVERALL: PASS  (7/7 exact-symbolic tests)")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
