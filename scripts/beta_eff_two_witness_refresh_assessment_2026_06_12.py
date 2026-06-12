#!/usr/bin/env python3
"""Witness-pair refresh assessment for the beta_eff no-go surface.

The runner checks the original two-witness algebra and verifies that the
post-2026-05-03 exact-coefficient rows pin Delta(beta), not beta_eff(beta).
It deliberately does not assign or predict audit status.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from frontier_gauge_vacuum_plaquette_bridge_support import plaquette_from_bessel  # noqa: E402
from frontier_gauge_vacuum_plaquette_mixed_cumulant_audit import beta_eff_beta5_coefficient  # noqa: E402


NO_GO = ROOT / "docs" / "GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_NO_GO_THEOREM_NOTE_2026-05-03.md"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

COEFFICIENT_ROWS = {
    "docs/BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md": {
        "object": "Delta(beta)",
        "coefficients": ["d_6 = 7 / 5668704", "d_7 = 5 / 17006112"],
    },
    "docs/BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md": {
        "object": "Delta(beta)",
        "coefficients": ["d_7 = 5/17006112"],
    },
    "docs/BETA6_PLAQUETTE_D8_COEFFICIENT_AND_SINGLE_PAIR_VERDICT_BOUNDED_NOTE_2026-05-30.md": {
        "object": "Delta(beta)",
        "coefficients": ["d_8 = 5/272097792"],
    },
    "docs/BETA6_PLAQUETTE_D9_COEFFICIENT_BOUNDED_NOTE_2026-06-04.md": {
        "object": "Delta(beta)",
        "coefficients": ["d_9 = -2035/264479053824"],
    },
    "docs/BETA6_PLAQUETTE_D10_COEFFICIENT_AND_RADIUS_EVIDENCE_BOUNDED_NOTE_2026-06-04.md": {
        "object": "Delta(beta)",
        "coefficients": ["d_10 = -10483 / 5289581076480"],
    },
    "docs/BETA6_PLAQUETTE_D11_COEFFICIENT_AND_CONTINUATION_SPREAD_BOUNDED_NOTE_2026-06-04.md": {
        "object": "Delta(beta)",
        "coefficients": ["d_11 = -13/3967185807360"],
    },
    "docs/BETA6_DELTA_ANALYTIC_CLASS_FRONTIER_NOTE_2026-05-30.md": {
        "object": "Delta(beta)",
        "coefficients": [
            "d-log-Pade verdict",
            "Does NOT claim:\n- any value of `P(beta=6)`, `beta_eff(6)`, `u_0`, or `alpha_s`",
        ],
    },
}

RETAINED_ROWS = {
    "docs/GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_NO_GO_THEOREM_NOTE_2026-05-03.md": "retained_no_go",
    "docs/BETA6_RESUMMATION_RADIUS_GROWTH_RATE_BOUNDED_NOTE_2026-05-30.md": "retained_grade",
}

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS: {name} -- {detail}")
    else:
        FAIL += 1
        print(f"FAIL: {name} -- {detail}")


def doc(relpath: str) -> str:
    return (ROOT / relpath).read_text(encoding="utf-8")


def ledger_statuses() -> dict[str, str]:
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    out: dict[str, str] = {}
    for row in data["rows"].values():
        path = row.get("note_path")
        if path:
            out[path] = row.get("effective_status")
    return out


def retained_grade(status: str | None) -> bool:
    return status in {"retained", "retained_bounded", "retained_no_go"}


def beta_eff_minus(beta: Fraction) -> Fraction:
    return beta + beta_eff_beta5_coefficient() * beta**5


def beta_eff_plus(beta: Fraction, c: Fraction) -> Fraction:
    return beta_eff_minus(beta) + c * beta**6


def derivative_lower_bound_positive(c: Fraction) -> bool:
    """For beta in [0, 6], all derivative addends are nonnegative."""
    a = beta_eff_beta5_coefficient()
    return a > 0 and c > 0


def polynomial_coefficients_are_exact(c: Fraction) -> bool:
    a = beta_eff_beta5_coefficient()
    minus_coeffs = {1: Fraction(1, 1), 5: a}
    plus_coeffs = {1: Fraction(1, 1), 5: a, 6: c}
    return all(
        isinstance(power, int)
        and power >= 0
        and isinstance(coefficient, Fraction)
        for coeffs in (minus_coeffs, plus_coeffs)
        for power, coefficient in coeffs.items()
    )


def main() -> int:
    beta = Fraction(6, 1)
    c = Fraction(1, 10_000_000)
    a = beta_eff_beta5_coefficient()
    minus = beta_eff_minus(beta)
    plus = beta_eff_plus(beta, c)
    delta_beta = plus - minus
    p_minus = plaquette_from_bessel(float(minus))[0]
    p_plus = plaquette_from_bessel(float(plus))[0]
    delta_p = p_plus - p_minus

    print("beta_eff two-witness refresh assessment")
    print(f"original a = {a}")
    print(f"original c = {c}")
    print(f"beta_eff_minus(6) = {minus} ~= {float(minus):.15f}")
    print(f"beta_eff_plus(6) = {plus} ~= {float(plus):.15f}")
    print(f"delta beta_eff(6) = {delta_beta} ~= {float(delta_beta):.15f}")
    print(f"R_O(beta_eff_minus(6)) ~= {p_minus:.15f}")
    print(f"R_O(beta_eff_plus(6)) ~= {p_plus:.15f}")
    print(f"delta R_O ~= {delta_p:.15e}")

    note_text = NO_GO.read_text(encoding="utf-8")
    check(
        "retained packet pins beta_eff only through beta^5",
        "`beta_eff(beta) = beta + beta^5 / 26244 + O(beta^6)`" in note_text,
        "no-go section 1 contains the retained onset datum",
    )
    check(
        "original witnesses differ first at beta^6",
        delta_beta == c * beta**6 and delta_beta == Fraction(729, 156250),
        f"delta_beta={delta_beta}",
    )
    check(
        "original witnesses are analytic polynomials",
        polynomial_coefficients_are_exact(c),
        "exact Fraction coefficients at integer powers 1, 5, and 6",
    )
    check(
        "original witnesses are strictly increasing on [0,6]",
        derivative_lower_bound_positive(c),
        "derivatives are 1 + nonnegative beta powers for beta >= 0",
    )
    check(
        "original R_O spread is positive",
        delta_p > 0.0,
        f"delta_R_O={delta_p:.15e}",
    )

    statuses = ledger_statuses()
    for path, expected in RETAINED_ROWS.items():
        actual = statuses.get(path)
        condition = actual == expected if expected != "retained_grade" else retained_grade(actual)
        check(
            f"ledger status for {path}",
            condition,
            f"effective_status={actual}",
        )

    beta_eff_pinning_rows = []
    for path, spec in COEFFICIENT_ROWS.items():
        text = doc(path)
        object_ok = spec["object"] in text
        coefficient_ok = all(fragment in text for fragment in spec["coefficients"])
        no_beta_eff_series = "beta_eff(beta) =" not in text and "beta_eff = beta" not in text
        check(
            f"{path} pins Delta object",
            object_ok and coefficient_ok and no_beta_eff_series,
            f"object={spec['object']}; effective_status={statuses.get(path)}",
        )
        check(
            f"{path} has ledger row for standing disclosure",
            statuses.get(path) is not None,
            f"effective_status={statuses.get(path)}",
        )
        if not no_beta_eff_series:
            beta_eff_pinning_rows.append(path)

    radius_text = doc("docs/BETA6_RESUMMATION_RADIUS_GROWTH_RATE_BOUNDED_NOTE_2026-05-30.md")
    check(
        "radius row threshold is the Delta tree-sector product threshold",
        "R_tree(g_tree) = 18 / g_tree^(1/4)" in radius_text
        and "R_tree > 6 iff g_tree < 81" in radius_text
        and "Delta(beta) := P_full(beta) - P_1plaq(beta)" in radius_text,
        "retained row states the sector object and threshold",
    )
    check(
        "radius inequality threshold algebra",
        Fraction(18, 6) ** 4 == Fraction(81, 1),
        "(18/6)^4 = 81",
    )
    check(
        "radius row does not bound beta_eff tail coefficient",
        "beta_eff(beta) =" not in radius_text and "tail coefficient" not in radius_text,
        "no beta_eff-series coefficient bound is stated",
    )
    check(
        "no refreshed beta_eff witness pair is triggered",
        beta_eff_pinning_rows == [],
        f"beta_eff_pinning_rows={beta_eff_pinning_rows}",
    )

    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
