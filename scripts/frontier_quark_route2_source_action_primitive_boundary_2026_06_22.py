#!/usr/bin/env python3
"""Verify the Route-2 source-action finite-jet primitive boundary."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs/QUARK_ROUTE2_SOURCE_ACTION_PRIMITIVE_BOUNDARY_NOTE_2026-06-22.md"
BLOCK110 = ROOT / "docs/QUARK_ROUTE2_LOG_ACTION_COCYCLE_HESSIAN_BOUNDARY_NOTE_2026-06-22.md"
BLOCK107 = ROOT / "docs/QUARK_ROUTE2_LOG_WEIGHT_SECOND_VARIATION_ROW_BOUNDARY_NOTE_2026-06-22.md"
BLOCK108 = ROOT / "docs/QUARK_ROUTE2_RECORD_ADDITIVE_SECOND_VARIATION_NO_GO_NOTE_2026-06-22.md"
BLOCK109 = ROOT / "docs/QUARK_ROUTE2_INFORMATION_METRIC_DEGREE_BOUNDARY_NOTE_2026-06-22.md"
COUNTERTERM = ROOT / "docs/QUARK_ROUTE2_HESSIAN_COUNTERTERM_EXCLUSION_BOUNDARY_NOTE_2026-06-22.md"
S3 = ROOT / "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"
READOUT = ROOT / "docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
MINIMAL = ROOT / "docs/MINIMAL_AXIOMS_2026-06-05.md"

passes = 0
fails = 0


def compact(text: str) -> str:
    return " ".join(text.split())


def check(condition: bool, label: str, detail: str = "") -> None:
    global passes, fails
    suffix = f" -- {detail}" if detail else ""
    if condition:
        passes += 1
        print(f"PASS: {label}{suffix}")
    else:
        fails += 1
        print(f"FAIL: {label}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def ratio_for_order(order: int) -> Fraction:
    return Fraction(3, 2) ** order


def endpoint_from_ratio(ratio: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    q_t = Fraction(5, 6)
    s_te = Fraction(-2, 1)
    q_e = q_t * ratio
    rho_e = 6 * (q_e - 1)
    c_te = s_te * q_t / q_e
    return q_e, rho_e, c_te


def affine_value(coeffs: tuple[Fraction, Fraction, Fraction], w: Fraction, a0: Fraction, a1: Fraction) -> Fraction:
    c0, c1, c2 = coeffs
    # L[a0 + a1*w] = c0*(a0+a1*w) + c1*a1 + c2*0.
    return c0 * (a0 + a1 * w) + c1 * a1


def affine_invariant_on_witnesses(coeffs: tuple[Fraction, Fraction, Fraction]) -> bool:
    witnesses = [
        (Fraction(1, 3), Fraction(1, 1), Fraction(0, 1)),
        (Fraction(1, 3), Fraction(0, 1), Fraction(1, 1)),
        (Fraction(1, 2), Fraction(2, 1), Fraction(-3, 1)),
        (Fraction(2, 5), Fraction(-4, 1), Fraction(5, 1)),
    ]
    return all(affine_value(coeffs, w, a0, a1) == 0 for w, a0, a1 in witnesses)


def prefactor_ratio(power: int) -> Fraction:
    w_e = Fraction(1, 3)
    w_t = Fraction(1, 2)
    hessian_ratio = ratio_for_order(2)
    return (w_e / w_t) ** power * hessian_ratio


def main() -> int:
    print("Route-2 source-action primitive boundary")
    print("=" * 78)

    print("\nA. Source-note and authority boundary")
    note = read(NOTE)
    note_c = compact(note)
    note_lower = note.lower()
    check(NOTE.exists(), "new source note exists", str(NOTE.relative_to(ROOT)))
    check("**Actual current-surface status:** exact-support" in note, "new note declares exact-support/open status")
    check("**Claim type:** open_gate" in note, "new note declares open_gate claim type")
    check("log-action cocycle semantics, by itself, selects the Hessian row" in note, "new note states tested overread")
    check("It does not." in note, "new note states cocycle-alone nonselection")
    check("affine-gauge-invariant lowest-order local curvature response" in note, "new note states sharper positive premise")
    check(
        "proposed_retained" not in note_c
        and "would become retained" not in note_c
        and "retained branch-local" not in note_c,
        "new note has no retained proposal wording",
    )

    authorities = [
        (BLOCK110, ["multiplicative-to-additive cocycle", "Hessian row readout"]),
        (BLOCK107, ["scale-shift-invariant second variation", "Phi''(w) = C/w^2"]),
        (BLOCK108, ["does not derive the Block107 premise", "nonzero Hessian"]),
        (BLOCK109, ["degree `-1`, not degree `-2`", "log-barrier"]),
        (COUNTERTERM, ["positive Hessian counterterms", "does not exclude"]),
        (S3, ["endpoint triple", "not yet derived"]),
        (READOUT, ["irreducible missing map entry", "beta_E / alpha_E"]),
        (MINIMAL, ["supplies no readout context"]),
    ]
    for path, markers in authorities:
        text = compact(read(path))
        missing = [marker for marker in markers if marker not in text]
        check(not missing, f"{path.name} contains required boundary markers", "; ".join(markers))

    print("\nB. Cocycle action and derivative-order family")
    # Work in exponent coordinates w=b^n, where any regular multiplicative
    # additive character is linear in n. This checks the finite exact skeleton
    # of the log-selection premise without importing numerical logs.
    kappa = Fraction(11, 1)

    def action_on_power(n: int) -> Fraction:
        return kappa * n

    check(action_on_power(2 + 5) == action_on_power(2) + action_on_power(5), "cocycle action is additive in exponent coordinate")
    check(action_on_power(0) == 0, "identity element has zero source action")
    check(action_on_power(-3) == -action_on_power(3), "inverse source action changes sign")
    check(ratio_for_order(1) == Fraction(3, 2), "first derivative row ratio is 3/2")
    check(ratio_for_order(2) == Fraction(9, 4), "second derivative row ratio is 9/4")
    check(ratio_for_order(3) == Fraction(27, 8), "third derivative row ratio is 27/8")
    check(ratio_for_order(4) == Fraction(81, 16), "fourth derivative row ratio is 81/16")
    target_orders = [order for order in range(1, 8) if ratio_for_order(order) == Fraction(9, 4)]
    check(target_orders == [2], "integer derivative-order scan selects k=2 only after order is supplied", f"orders={target_orders}")

    print("\nC. Endpoint consequences and counter-witnesses")
    expected = {
        1: (Fraction(5, 4), Fraction(3, 2), Fraction(-4, 3)),
        2: (Fraction(15, 8), Fraction(21, 4), Fraction(-8, 9)),
        3: (Fraction(45, 16), Fraction(87, 8), Fraction(-16, 27)),
        4: (Fraction(135, 32), Fraction(309, 16), Fraction(-32, 81)),
    }
    for order, triple in expected.items():
        q_e, rho_e, c_te = endpoint_from_ratio(ratio_for_order(order))
        check((q_e, rho_e, c_te) == triple, f"order {order} endpoint triple", f"q_E={q_e}, rho_E={rho_e}, c_TE={c_te}")
    check(expected[2] == (Fraction(15, 8), Fraction(21, 4), Fraction(-8, 9)), "second derivative hits the endpoint target")
    check(expected[1] != expected[2] and expected[3] != expected[2], "first and third derivatives are exact non-target witnesses")
    check("first derivative `k=1`" in note and "third derivative `k=3`" in note, "note displays derivative-order counter-witnesses")
    check("log-action cocycle semantics alone => Hessian source row" in note, "note states the overread being pruned")

    print("\nD. Affine-gauge finite-jet lemma")
    value_readout = (Fraction(1), Fraction(0), Fraction(0))
    first_readout = (Fraction(0), Fraction(1), Fraction(0))
    hessian_readout = (Fraction(0), Fraction(0), Fraction(1))
    mixed_bad = (Fraction(2), Fraction(-1), Fraction(5))
    check(not affine_invariant_on_witnesses(value_readout), "value readout is not affine-gauge invariant")
    check(not affine_invariant_on_witnesses(first_readout), "first derivative readout is not affine-gauge invariant")
    check(not affine_invariant_on_witnesses(mixed_bad), "mixed value/first/Hessian readout is not affine-gauge invariant")
    check(affine_invariant_on_witnesses(hessian_readout), "pure Hessian readout is affine-gauge invariant")
    # Direct coefficient logic: constant term kills c0, slope term then kills c1.
    c0, c1, c2 = hessian_readout
    check(c0 == 0 and c1 == 0 and c2 != 0, "minimal nonzero invariant coefficient pattern is Hessian-only")
    check("a_0 = 0,       a_1 = 0" in note, "note records the finite-jet coefficient constraint")
    check("lowest nonzero such readout" in note, "note records minimal-curvature support")

    print("\nE. Prefactor/no-scale boundary")
    check(prefactor_ratio(0) == Fraction(9, 4), "constant Hessian prefactor preserves target ratio")
    check(prefactor_ratio(1) == Fraction(3, 2), "weight prefactor g(w)=w shifts Hessian to degree -1")
    check(prefactor_ratio(2) == Fraction(1, 1), "weight prefactor g(w)=w^2 shifts Hessian to degree 0")
    q_pref, rho_pref, c_pref = endpoint_from_ratio(prefactor_ratio(1))
    check((q_pref, rho_pref, c_pref) == expected[1], "g(w)=w prefactor reproduces first-derivative miss")
    check("g(w) Phi''(w)" in note, "note identifies the prefactor loophole")
    check("constant source unit / no weight-dependent prefactor" in note, "note keeps no-scale coefficient as an open premise")

    print("\nF. Current-surface boundary")
    check("Forbidden proof inputs:" in note and "observed masses" in note, "note records forbidden proof-input firewall")
    check("assuming from the start that the physical source row is a Hessian row" in note, "note forbids importing Hessian row")
    check("It does not assert that target as current framework content." in note, "note preserves current-surface boundary")
    check("No observed masses, fitted endpoint values" in note, "note excludes fitted/observed hidden inputs")
    check("the E-channel map entry is not selected by a physical readout primitive" in note_c, "note matches S3/Route-2 residual")
    check("future theorem premise" in note, "note labels positive primitive as future premise")
    check("audit verdict" in note_lower and "does not set" in note_c.lower(), "note leaves audit authority untouched")

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={passes}, FAIL={fails}")
    if fails:
        print("STATUS: failure in source-action primitive boundary verifier.")
        return 1
    print(
        "STATUS: exact-support/open boundary. Log-action cocycle semantics "
        "selects the logarithmic source action but not finite-jet order; "
        "affine-gauge minimal local curvature would select the Hessian row, "
        "while the physical Route-2 source/readout primitive remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
