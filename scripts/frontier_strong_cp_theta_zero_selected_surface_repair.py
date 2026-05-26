#!/usr/bin/env python3
"""Selected-surface repair runner for STRONG_CP_THETA_ZERO_NOTE.md.

The claim checked here is deliberately narrow: if the theta-free Wilson slot,
the real-positive scalar mass line, paired anti-Hermitian staggered spectrum,
and nonnegative topological-sector weights are selected as hypotheses, then
theta_eff = 0 and the internal determinant/effective-action checks close.

The runner does not derive the selected surface or apply an audit verdict.
"""

from __future__ import annotations

import cmath
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "STRONG_CP_THETA_ZERO_NOTE.md"
LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
CLAIM_ID = "strong_cp_theta_zero_note"
RUNNER_PATH = "scripts/frontier_strong_cp_theta_zero_selected_surface_repair.py"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    status = "PASS" if ok else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")


def phase(z: complex) -> float:
    return math.atan2(z.imag, z.real)


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def check_note_boundary() -> None:
    section("Selected-surface claim boundary")
    text = NOTE_PATH.read_text()
    required = [
        "bounded-support selected-surface algebra",
        "The selected surface is an explicit premise",
        "not a derived framework action-surface theorem",
        "theta_bare = 0",
        "arg det(M_u M_d) = 0",
        "This row does not derive the scalar-mass-only class",
        "It does not solve strong CP beyond the explicitly selected surface.",
    ]
    for needle in required:
        check(f"note contains required boundary: {needle!r}", needle in text)

    forbidden = [
        "retained action-surface strong-CP closure package",
        "retained-framework action-surface closure",
        "retained Wilson-plus-staggered action surface",
        "axion-model exclusion",
        "derives the theta-free action surface from the minimal framework axioms",
        "proves the theta-free action surface from the minimal framework axioms",
    ]
    for needle in forbidden:
        check(f"note avoids overclaim phrase: {needle!r}", needle not in text)


def check_mass_phase() -> None:
    section("Scalar mass determinant phase")
    masses = [(0.2, 1.7), (1.0, 1.0), (3.5, 0.4)]
    dims = [1, 2, 3, 6]
    for mu, md in masses:
        for dim in dims:
            det_prod = (mu * md) ** dim
            check(
                f"arg det(M_u M_d)=0 for m_u={mu}, m_d={md}, dim={dim}",
                det_prod > 0 and abs(phase(complex(det_prod, 0.0))) < 1e-14,
                f"det={det_prod:.12g}",
            )


def check_staggered_pair_determinant() -> None:
    section("Paired anti-Hermitian determinant positivity")
    spectra = [
        [0.15, 0.8, 2.25],
        [0.0, 0.5, 1.5, 3.0],
        [0.125, 0.25, 0.5, 1.0, 2.0],
    ]
    masses = [0.1, 0.7, 2.0]
    for lambdas in spectra:
        for mass in masses:
            det_value = 1.0
            for lam in lambdas:
                det_value *= (mass + 1j * lam) * (mass - 1j * lam)
            check(
                f"det(D+mI)>0 for paired spectrum len={len(lambdas)}, m={mass}",
                abs(det_value.imag) < 1e-12 and det_value.real > 0,
                f"det={det_value.real:.12g}+{det_value.imag:.2e}i",
            )


def check_effective_action_reality() -> None:
    section("Effective action reality")
    wilson_actions = [0.0, 12.5, 48.25]
    dets = [0.75, 1.0, 33.2, 512.0]
    for sw in wilson_actions:
        for det_value in dets:
            s_eff = sw - math.log(det_value)
            check(
                f"S_eff real for S_W={sw}, det={det_value}",
                math.isfinite(s_eff) and isinstance(s_eff, float),
                f"S_eff={s_eff:.12g}",
            )


def z_theta(weights: dict[int, float], theta: float) -> complex:
    return sum(w * cmath.exp(1j * theta * charge) for charge, w in weights.items())


def check_topological_triangle_bound() -> None:
    section("Positive sector-weight triangle inequality")
    weight_sets = [
        {-2: 0.05, -1: 0.25, 0: 1.0, 1: 0.25, 2: 0.05},
        {-3: 0.1, -1: 0.4, 0: 1.2, 2: 0.3},
        {0: 1.0, 1: 0.125, 4: 0.03125},
    ]
    grid = [k * math.pi / 32 for k in range(-64, 65)]
    for idx, weights in enumerate(weight_sets, start=1):
        z0 = z_theta(weights, 0.0)
        min_free_delta = float("inf")
        max_abs = 0.0
        for theta in grid:
            zt = z_theta(weights, theta)
            max_abs = max(max_abs, abs(zt))
            if abs(zt) > 1e-15:
                min_free_delta = min(min_free_delta, -math.log(abs(zt)) + math.log(abs(z0)))
        check(
            f"set {idx}: |Z(theta)| <= Z(0) on theta grid",
            max_abs <= abs(z0) + 1e-12,
            f"max|Z|={max_abs:.12g}, Z0={abs(z0):.12g}",
        )
        check(
            f"set {idx}: F(theta)-F(0) >= 0 where defined",
            min_free_delta >= -1e-12,
            f"min_delta={min_free_delta:.3e}",
        )


def check_axial_endpoint_discipline() -> None:
    section("Real scalar line axial endpoint discipline")
    alphas = [0.0, math.pi / 6, math.pi / 2, math.pi, 2 * math.pi]
    for alpha in alphas:
        scalar = math.cos(alpha)
        pseudoscalar = math.sin(alpha)
        stays_on_real_scalar_line = abs(pseudoscalar) < 1e-12
        positive_orientation = stays_on_real_scalar_line and scalar > 0
        expected = alpha in (0.0, 2 * math.pi)
        check(
            f"alpha={alpha:.6g}: positive real scalar orientation iff endpoint selected",
            positive_orientation == expected,
            f"cos={scalar:.6g}, sin={pseudoscalar:.6g}",
        )


def check_audit_metadata_after_pipeline() -> None:
    section("Audit metadata after pipeline regeneration")
    if not LEDGER_PATH.exists():
        check("audit ledger exists", False, str(LEDGER_PATH))
        return
    ledger = json.loads(LEDGER_PATH.read_text())
    row = ledger.get("rows", {}).get(CLAIM_ID)
    check(f"{CLAIM_ID} row exists", row is not None)
    if row is None:
        return
    check("claim_type is bounded_theorem", row.get("claim_type") == "bounded_theorem", str(row.get("claim_type")))
    check("audit_status reset to unaudited", row.get("audit_status") == "unaudited", str(row.get("audit_status")))
    check("effective_status reset to unaudited", row.get("effective_status") == "unaudited", str(row.get("effective_status")))
    check("runner path is selected-surface repair runner", row.get("runner_path") == RUNNER_PATH, str(row.get("runner_path")))
    check("direct deps are empty for selected-surface theorem", row.get("deps") == [], str(row.get("deps")))
    check("open dependency paths are empty", row.get("open_dependency_paths") == [], str(row.get("open_dependency_paths")))


def main() -> int:
    print("Strong CP theta-zero selected-surface repair runner")
    check_note_boundary()
    check_mass_phase()
    check_staggered_pair_determinant()
    check_effective_action_reality()
    check_topological_triangle_bound()
    check_axial_endpoint_discipline()
    check_audit_metadata_after_pipeline()
    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
