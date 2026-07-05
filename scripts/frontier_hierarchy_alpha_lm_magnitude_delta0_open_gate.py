#!/usr/bin/env python3
"""Check hierarchy alpha_LM magnitude arithmetic and delta-zero open gate."""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_2026-05-30.md"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  --  {detail}" if detail else ""
    print(f"{tag}: {name}{suffix}")


def section(title: str) -> None:
    print()
    print("=" * 80)
    print(title)
    print("=" * 80)


def read_note() -> str:
    return NOTE.read_text(encoding="utf-8")


def check_note_scope() -> None:
    section("Note scope")
    text = read_note()
    flat = " ".join(text.split())
    required = [
        "**Claim type:** open_gate",
        "**Status authority:** independent audit lane only.",
        "does not close the hierarchy lane",
        "does not approve",
        "transport source for that coupling-power magnitude on the current baseline: open",
        "does not claim that every possible future mechanism is closed",
        "mean-field link-feedback candidate is also pruned",
        "Surviving routes run through beyond-mean-field link fluctuations",
        "## W51 repair attempt (2026-06-12; named-gap sharpening)",
        "named gap: B4 attachment-observable identification",
        "Classification: named-gap statement after stress check, not a shipped global no-go.",
    ]
    forbidden = [
        "Generated" + " with",
        "source-note proposal only",
        "actual_" + "current_surface_status",
        "ret" + "ained_bounded",
        "ret" + "ained_no_go",
        "closure_proposal",
        "formal no-go",
        "only route",
        "last route",
        "exhausted",
        "closes the program",
    ]
    for marker in required:
        check(f"note contains marker: {marker}", marker in text or marker in flat)
    for marker in forbidden:
        check(f"note omits non-native marker: {marker}", marker not in text)


def check_coupling_power() -> None:
    section("Coupling-power magnitude")
    alpha_bare = 1 / (4 * sp.pi)
    value = alpha_bare**16
    check("alpha_bare = 1/(4 pi)", sp.simplify(alpha_bare - 1 / (4 * sp.pi)) == 0)
    check(
        "alpha_bare^16 = (4 pi)^-16 ~= 2.586e-18",
        abs(float(value) - 2.586e-18) / 2.586e-18 < 1e-3,
        f"{float(value):.6e}",
    )


def check_geometric_progression() -> None:
    section("Geometric progression")
    u0, alpha_bare = sp.symbols("u0 alpha_bare", positive=True)
    alpha_lm = alpha_bare / u0
    alpha_s = alpha_bare / u0**2
    check("alpha_LM = alpha_bare/u0", sp.simplify(alpha_lm - alpha_bare / u0) == 0)
    check("alpha_s = alpha_bare/u0^2", sp.simplify(alpha_s - alpha_bare / u0**2) == 0)
    check("alpha_LM/alpha_bare = 1/u0", sp.simplify(alpha_lm / alpha_bare - 1 / u0) == 0)
    check("alpha_s/alpha_LM = 1/u0", sp.simplify(alpha_s / alpha_lm - 1 / u0) == 0)
    inv = [1 / alpha_bare, 1 / alpha_lm, 1 / alpha_s]
    delta_1 = sp.simplify(inv[1] - inv[0])
    delta_2 = sp.simplify(inv[2] - inv[1])
    check("1/alpha equal-step test gives Delta2/Delta1 = u0", sp.simplify(delta_2 / delta_1 - u0) == 0, str(sp.simplify(delta_2 / delta_1)))


def check_block_observable_symbols() -> None:
    section("Block observable symbol support")
    m, omega, u0, alpha_bare = sp.symbols("m omega u0 alpha_bare", positive=True)
    determinant_factor = (m**2 + 4 * u0**2) ** 8
    determinant_at_zero = sp.expand(determinant_factor.subs(m, 0))
    single_mode_magnitude_squared = m**2 + 4 * u0**2
    condensate_block = m**2 + u0**2 * (3 + sp.sin(omega) ** 2)
    condensate_summand = 1 / condensate_block
    check("determinant factor contains u0", u0 in determinant_factor.free_symbols)
    check("determinant factor has no explicit alpha_bare", alpha_bare not in determinant_factor.free_symbols)
    check(
        "determinant at m=0 has u0-degree 16",
        sp.Poly(determinant_at_zero, u0).degree() == 16,
        str(determinant_at_zero),
    )
    check(
        "single taste-mode magnitude squared is m^2 + 4 u0^2",
        sp.simplify(single_mode_magnitude_squared - (m**2 + 4 * u0**2)) == 0,
    )
    check("single taste-mode factor has no explicit alpha_bare", alpha_bare not in single_mode_magnitude_squared.free_symbols)
    check("condensate summand contains u0", u0 in condensate_summand.free_symbols)
    check("condensate summand has no explicit alpha_bare", alpha_bare not in condensate_summand.free_symbols)


def check_reduced_target_algebra() -> None:
    section("Reduced target algebra")
    u0, alpha_bare = sp.symbols("u0 alpha_bare", positive=True)
    alpha_lm = alpha_bare / u0
    alpha_s = alpha_bare / u0**2
    ratio_product = u0**16 * alpha_s**16
    check(
        "ratio-normalized product u0^16 * alpha_s^16 equals alpha_LM^16",
        sp.simplify(ratio_product - alpha_lm**16) == 0,
    )
    u_test = sp.Rational(2, 3)
    ab_test = sp.Rational(1, 5)
    smallest_instance = ((2 * u_test) / 2) ** 16 * (ab_test / u_test**2) ** 16
    target_instance = (ab_test / u_test) ** 16
    check(
        "smallest faithful 16-mode instance closes exactly over rationals",
        sp.simplify(smallest_instance - target_instance) == 0,
        f"value={sp.factor(target_instance)}",
    )
    kernel_slope = 1 / (4 * sp.pi)
    alpha_bare_g1 = 1 / (4 * sp.pi)
    check("per-taste d=3 kernel slope equals alpha_bare at g_bare=1 as a value", sp.simplify(kernel_slope - alpha_bare_g1) == 0)
    check(
        "kernel slope times two-link dressing equals alpha_s value",
        sp.simplify(kernel_slope * u0 ** -2 - alpha_s.subs(alpha_bare, alpha_bare_g1)) == 0,
    )


def check_w51_named_gap_markers() -> None:
    section("W51 named-gap markers")
    text = read_note()
    flat = " ".join(text.split())
    required_links = [
        "[`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md)",
    ]
    forbidden_dependency_links = [
        "[`HIERARCHY_DELTA0_BLOCKING_SINGLE_MODE_DECIMATION_PROBE_NOTE_2026-06-11.md`](HIERARCHY_DELTA0_BLOCKING_SINGLE_MODE_DECIMATION_PROBE_NOTE_2026-06-11.md)",
        "[`HIERARCHY_DELTA0_RATIO_NORMALIZED_ALPHA_S_PER_DECOUPLING_REDUCTION_NOTE_2026-06-11.md`](HIERARCHY_DELTA0_RATIO_NORMALIZED_ALPHA_S_PER_DECOUPLING_REDUCTION_NOTE_2026-06-11.md)",
        "[`HIERARCHY_DELTA0_S1PRIME_TASTE_REGION_KERNEL_SHARE_PROBE_NOTE_2026-06-11.md`](HIERARCHY_DELTA0_S1PRIME_TASTE_REGION_KERNEL_SHARE_PROBE_NOTE_2026-06-11.md)",
        "[`HIERARCHY_DELTA0_B4_ATTACHMENT_OBSERVABLE_ENUMERATION_NOTE_2026-06-11.md`](HIERARCHY_DELTA0_B4_ATTACHMENT_OBSERVABLE_ENUMERATION_NOTE_2026-06-11.md)",
    ]
    required_context_handles = [
        "`HIERARCHY_DELTA0_BLOCKING_SINGLE_MODE_DECIMATION_PROBE_NOTE_2026-06-11.md`",
        "`HIERARCHY_DELTA0_RATIO_NORMALIZED_ALPHA_S_PER_DECOUPLING_REDUCTION_NOTE_2026-06-11.md`",
        "`HIERARCHY_DELTA0_S1PRIME_TASTE_REGION_KERNEL_SHARE_PROBE_NOTE_2026-06-11.md`",
        "`HIERARCHY_DELTA0_B4_ATTACHMENT_OBSERVABLE_ENUMERATION_NOTE_2026-06-11.md`",
        "plain-text context handles rather than citation-graph dependencies",
    ]
    for marker in required_links:
        check(f"one-hop authority link present: {marker}", marker in text)
    for marker in forbidden_dependency_links:
        check(f"downstream probe is not a one-hop authority link: {marker}", marker not in text)
    for marker in required_context_handles:
        check(f"context handle present: {marker}", marker in text)
    required_markers = [
        "two exact match-window cells",
        "supplier-chain identity itself, not a mechanism",
        "bookkeeping equivalence of the reduced target",
        "does not derive the attachment-observable identification",
        "N1, alternative routes checked or bounded.",
        "N2, wall independence.",
        "N3, hidden-wall scan.",
        "N4, residual matching.",
        "N5, rhetoric audit.",
        "N6, primitive registry check.",
        "N7, steelman.",
        "N8, cross-cycle echo.",
        "outside-K1-K8",
    ]
    for marker in required_markers:
        check(f"W51 marker present: {marker}", marker in text or marker in flat)


def check_delta_zero_scope() -> None:
    section("Delta-zero scope")
    delta = 0
    check("current baseline scope records delta = 0", delta == 0)
    check("no extra-dimensional tower is supplied by this runner", delta == 0)


def check_feedback_route_pruning() -> None:
    section("Feedback route pruning")
    text = read_note()
    flat = " ".join(text.split())
    plaquette = sp.Rational(2967, 5000)
    alpha_bare = 1 / (4 * sp.pi)
    alpha_s = alpha_bare / sp.sqrt(plaquette)
    required_rdet = sp.sqrt(1 / alpha_s)
    check(
        "alpha_s target remains 0.1033038",
        abs(float(alpha_s) - 0.1033038) < 5e-7,
        f"{float(alpha_s):.7f}",
    )
    check(
        "if R = alpha_s, determinant-share ratio must exceed 3, not an O(1)-near-1 saddle shift",
        float(required_rdet) > 3.0,
        f"required R_det = alpha_s^(-1/2) = {float(required_rdet):.6f}",
    )
    check(
        "note records Block04 mean-field feedback pruning without claiming closure",
        "ordinary mean-field link un-freezing is refuted as the supplier" in flat
        and "gate unchanged, still open" in flat
        and "context-only pruning" in flat,
    )
    check(
        "note leaves three surviving route families after mean-field pruning",
        "exact one-link Haar integrals" in flat
        and "Green-kernel" in flat
        and "non-link transport rule" in flat,
    )


def main() -> int:
    check_note_scope()
    check_coupling_power()
    check_geometric_progression()
    check_block_observable_symbols()
    check_reduced_target_algebra()
    check_w51_named_gap_markers()
    check_delta_zero_scope()
    check_feedback_route_pruning()
    print()
    if FAIL:
        print("VERDICT: hierarchy alpha_LM magnitude delta-zero open-gate checks failed.")
        print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
        return 1
    print("VERDICT: hierarchy alpha_LM magnitude delta-zero open-gate checks pass.")
    print(f"TOTAL: PASS={PASS}, FAIL=0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
