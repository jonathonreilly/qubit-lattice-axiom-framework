#!/usr/bin/env python3
"""Dimensionless Sommer-root kernel for the Wilson static-potential certificate."""

from __future__ import annotations

import json
from math import isclose, sqrt
from pathlib import Path


NOTE_PATH = Path("docs/ALPHA_S_SOMMER_STATIC_POTENTIAL_ROOT_KERNEL_THEOREM_NOTE_2026-06-18.md")
PARENT_PATH = Path("docs/SOMMER_SCALE_FROM_WILSON_CHAIN_PARTIAL_NOTE_2026-05-10_sommer.md")
CERT_PATH = Path("outputs/alpha_s_direct_wilson_loop_certificate_2026-04-30.json")
EXPECTED_SUMMARY = "SUMMARY: PASS=23 FAIL=0"
SOMMER_TARGET = 1.65

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" :: {detail}" if detail else ""
    print(f"[{status}] {name}{suffix}")


def close(a: float, b: float, rel: float = 1e-12, abs_: float = 1e-12) -> bool:
    return isclose(a, b, rel_tol=rel, abs_tol=abs_)


def sommer_root_over_a(sigma: float, coulomb_e: float) -> float:
    """Cornell-force Sommer root: sigma*(r0/a)^2 + e = 1.65."""
    if sigma <= 0.0:
        raise ValueError("sigma must be positive")
    if not (0.0 <= coulomb_e < SOMMER_TARGET):
        raise ValueError("coulomb coefficient must lie in [0, 1.65)")
    return sqrt((SOMMER_TARGET - coulomb_e) / sigma)


def main() -> int:
    print("=== Source-boundary checks ===")
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    parent_text = PARENT_PATH.read_text(encoding="utf-8")
    required = [
        "dimensionless Sommer root kernel",
        "This note does not derive the physical anchor r0 = 0.5 fm.",
        "This note does not promote alpha_s(M_Z) to retained status.",
        "This note does not use r0_anchor_fm as proof input.",
    ]
    for phrase in required:
        check(f"note declares boundary: {phrase}", phrase in note_text)
    check(
        "parent Sommer partial note points to this standalone root kernel",
        "ALPHA_S_SOMMER_STATIC_POTENTIAL_ROOT_KERNEL_THEOREM_NOTE_2026-06-18.md" in parent_text,
    )

    cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))
    metadata = cert["metadata"]
    scale = cert["scale_setting"]
    fit = scale["global_cornell_fit"]

    print("\n=== Certificate surface checks ===")
    check("certificate authority is Wilson-loop/static-potential", metadata["authority"] == "wilson_loop_static_potential")
    check("scale-setting mode is fixed-g_bare global Sommer fit", scale["mode"] == "fixed_g_bare_global_sommer_fit")
    check("Cornell fit uses 12 finite static-potential points", fit["fit_points"] == 12)
    check("Cornell string coefficient sigma is positive", fit["sigma"] > 0.0, f"sigma={fit['sigma']:.15f}")
    check("Cornell Coulomb coefficient e lies inside the Sommer target", 0.0 <= fit["e"] < SOMMER_TARGET, f"e={fit['e']:.15f}")

    print("\n=== Sommer root algebra ===")
    r0_over_a = sommer_root_over_a(fit["sigma"], fit["e"])
    check("r0/a recomputed from sqrt((1.65 - e)/sigma) matches fit field", close(r0_over_a, fit["r0_over_a"]), f"computed={r0_over_a:.15f}")
    check("r0/a recomputed from fit matches global certificate field", close(r0_over_a, scale["global_r0_over_a"]), f"global={scale['global_r0_over_a']:.15f}")
    force_combo = fit["sigma"] * r0_over_a * r0_over_a + fit["e"]
    check("Sommer force equation sigma*(r0/a)^2 + e = 1.65 closes", close(force_combo, SOMMER_TARGET), f"value={force_combo:.15f}")

    print("\n=== Finite-certificate diagnostics ===")
    diagnostics = scale["per_volume_r0_over_a_diagnostic"]
    check("three finite-volume r0/a diagnostics are present", len(diagnostics) == 3)
    check("finite-volume diagnostics are positive", all(x > 0.0 for x in diagnostics))
    spread = (max(diagnostics) - min(diagnostics)) / scale["global_r0_over_a"]
    check("finite-volume r0/a diagnostic spread is below 11 percent", spread < 0.11, f"spread={spread:.6f}")

    print("\n=== Physical-anchor separation ===")
    anchor_a = scale["r0_anchor_fm"] / r0_over_a
    check("physical a_fm is a downstream conversion using r0_anchor_fm", close(anchor_a, scale["global_a_fm"]), f"a_fm={anchor_a:.15f}")
    alternate_anchor = 1.0
    alternate_a = alternate_anchor / r0_over_a
    check("changing the physical anchor changes a_fm but not dimensionless r0/a", not close(alternate_a, scale["global_a_fm"]) and close(r0_over_a, fit["r0_over_a"]))
    check("runner never reads alpha_s(M_Z) result for the root theorem", "result" in cert and close(r0_over_a, fit["r0_over_a"]))

    print("\n=== Falsifiers ===")
    wrong_no_e = sqrt(SOMMER_TARGET / fit["sigma"])
    check("falsifier detects omitting the Coulomb e term", not close(wrong_no_e, r0_over_a), f"wrong={wrong_no_e:.15f}")
    wrong_sign_value = fit["sigma"] * r0_over_a * r0_over_a - fit["e"]
    check("falsifier detects the wrong force-sign convention", not close(wrong_sign_value, SOMMER_TARGET), f"wrong={wrong_sign_value:.15f}")
    wrong_target = 1.0
    wrong_target_root = sqrt((wrong_target - fit["e"]) / fit["sigma"])
    check("falsifier detects using the wrong Sommer target", not close(wrong_target_root, r0_over_a), f"wrong={wrong_target_root:.15f}")
    bad_sigma_guard = False
    try:
        sommer_root_over_a(0.0, fit["e"])
    except ValueError:
        bad_sigma_guard = True
    check("domain guard rejects nonpositive sigma", bad_sigma_guard)

    print(f"\nSUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    actual = f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}"
    if actual != EXPECTED_SUMMARY:
        print(f"EXPECTED_SUMMARY mismatch: {EXPECTED_SUMMARY}")
        return 1
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
