#!/usr/bin/env python3
"""Check AC_phi_lambda independence of the Lorentz-violation angular shape.

This runner verifies a narrow support theorem: for the two supplied
nearest-neighbor dispersion surfaces, the quartic Lorentz-violation operator is
the same angular polynomial after dividing out the carrier coefficient.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import sympy as sp


NOTE = Path("docs/LORENTZ_VIOLATION_ANGULAR_FINGERPRINT_AC_PHI_LAMBDA_INDEPENDENCE_BOUNDED_NOTE_2026-06-08.md")
RESULTS: list[tuple[str, bool, str]] = []


def check(label: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((label, bool(ok), detail))


def angular_value(direction: list[float]) -> float:
    vector = np.array(direction, dtype=float)
    vector = vector / np.linalg.norm(vector)
    return float(np.sum(vector**4))


def main() -> int:
    px, py, pz, a = sp.symbols("p_x p_y p_z a", real=True)
    p2 = px**2 + py**2 + pz**2
    p4sum = px**4 + py**4 + pz**4
    coeff_iso, coeff_cubic = sp.symbols("coeff_iso coeff_cubic")

    carriers = {
        "bosonic_graph_laplacian": sum(2 * (1 - sp.cos(k * a)) / a**2 for k in (px, py, pz)),
        "staggered_dirac_ac_phi_lambda": sum(sp.sin(k * a) ** 2 / a**2 for k in (px, py, pz)),
    }
    expected_c4 = {
        "bosonic_graph_laplacian": sp.Rational(-1, 12),
        "staggered_dirac_ac_phi_lambda": sp.Rational(-1, 3),
    }

    c4: dict[str, sp.Expr] = {}
    normalized_quartic: dict[str, sp.Expr] = {}
    for name, dispersion in carriers.items():
        series = sp.series(dispersion, a, 0, 6).removeO()
        leading_ok = sp.simplify(series.coeff(a, 0) - p2) == 0
        quartic = sp.expand(series.coeff(a, 2))
        equation = sp.Poly(
            sp.expand(quartic - (coeff_iso * p2**2 + coeff_cubic * p4sum)),
            px,
            py,
            pz,
        )
        solution = sp.solve(equation.coeffs(), [coeff_iso, coeff_cubic], dict=True)[0]
        c4[name] = sp.simplify(solution[coeff_cubic])
        normalized_quartic[name] = sp.expand(quartic / c4[name])
        no_odd_terms = series.coeff(a, 1) == 0 and series.coeff(a, 3) == 0

        check(
            f"{name}_quartic_is_pure_cubic_invariant",
            leading_ok
            and solution[coeff_iso] == 0
            and c4[name] == expected_c4[name]
            and no_odd_terms,
            f"c4={c4[name]}, no a^1/a^3 odd terms",
        )

    check(
        "carrier_coefficients_differ_by_factor_four",
        sp.simplify(c4["staggered_dirac_ac_phi_lambda"] / c4["bosonic_graph_laplacian"]) == 4,
        f"staggered/bosonic={sp.simplify(c4['staggered_dirac_ac_phi_lambda'] / c4['bosonic_graph_laplacian'])}",
    )
    check(
        "normalized_angular_operator_is_identical",
        all(sp.simplify(expr - p4sum) == 0 for expr in normalized_quartic.values())
        and sp.simplify(
            normalized_quartic["bosonic_graph_laplacian"]
            - normalized_quartic["staggered_dirac_ac_phi_lambda"]
        )
        == 0,
        "both normalized quartic terms equal sum_i p_i^4",
    )

    axis = angular_value([1, 0, 0])
    diagonal = angular_value([1, 1, 1])
    check(
        "axis_body_diagonal_ratio_is_three",
        abs(axis - 1.0) < 1e-12 and abs(diagonal - 1.0 / 3.0) < 1e-12 and abs(axis / diagonal - 3.0) < 1e-12,
        f"[100]={axis:.12f}, [111]={diagonal:.12f}",
    )

    theta, phi = sp.symbols("theta phi", real=True)
    n = [
        sp.sin(theta) * sp.cos(phi),
        sp.sin(theta) * sp.sin(phi),
        sp.cos(theta),
    ]
    angular_poly = sum(component**4 for component in n)
    y20 = sp.sqrt(sp.Rational(5, 16) / sp.pi) * (3 * sp.cos(theta) ** 2 - 1)
    average = sp.integrate(
        sp.integrate(angular_poly * sp.sin(theta), (theta, 0, sp.pi)),
        (phi, 0, 2 * sp.pi),
    ) / (4 * sp.pi)
    ell2_projection = sp.integrate(
        sp.integrate(sp.simplify(angular_poly * y20) * sp.sin(theta), (theta, 0, sp.pi)),
        (phi, 0, 2 * sp.pi),
    )
    check(
        "cubic_harmonic_cross_check",
        sp.simplify(average - sp.Rational(3, 5)) == 0 and sp.simplify(ell2_projection) == 0,
        "average=3/5 and ell=2 projection vanishes",
    )

    note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    check(
        "source_note_keeps_scale_and_admission_boundary",
        NOTE.exists()
        and "admission-free" not in note_text
        and "Planck-pin" not in note_text
        and "`scale_reference_primitive` is not a Tier-A admission" in note_text
        and "magnitude coefficient is carrier-independent" in note_text,
        "broad admission-free and stale Planck-pin wording absent",
    )
    check(
        "source_note_has_parent_dependencies",
        "EMERGENT_LORENTZ_INVARIANCE_NOTE.md" in note_text
        and "LORENTZ_VIOLATION_DERIVED_NOTE.md" in note_text,
        "both parent dispersion surfaces are cited",
    )

    passed = sum(1 for _, ok, _ in RESULTS if ok)
    failed = sum(1 for _, ok, _ in RESULTS if not ok)
    for label, ok, detail in RESULTS:
        status = "PASS" if ok else "FAIL"
        suffix = f" -- {detail}" if detail else ""
        print(f"{status}: {label}{suffix}")
    print()
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    print(
        "VERDICT: within the two supplied nearest-neighbor dispersion surfaces, "
        "the Lorentz-violation angular shape is independent of the AC_phi_lambda "
        "carrier coefficient. Magnitude, scale conversion, and parent-status "
        "questions remain outside this support theorem."
    )
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
