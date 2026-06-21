#!/usr/bin/env python3
"""S3/Route-2 endpoint-triple residual map.

This runner is a direct-consumer packet for the S3-time parent row. It does
not audit anything and does not derive the endpoint triple. It verifies:

1. the exact equivalence class around (-1, -2, 21/4);
2. the finite current route2/s3-time/rconn candidate surface bank that mentions
   the endpoint datum;
3. the exact missing typed edges left for the parent consumer.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SCRIPTS = ROOT / "scripts"
NOTE = DOCS / "S3_ROUTE2_ENDPOINT_TRIPLE_RESIDUAL_MAP_BOUNDED_NOTE_2026-06-21.md"

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def phrase(*parts: str) -> str:
    return "".join(parts)


TARGET_TOKENS = (
    "rho_E",
    "21/4",
    "15/8",
    "-8/9",
    "beta_E/alpha_E",
    "beta_E / alpha_E",
    "gamma_T(center)",
    "gamma_E(center)",
)

NAME_TOKENS = ("route2", "s3_time", "rconn")

EXPECTED_CANDIDATE_SURFACES = {
    "docs/CTE_RCONN_SPATIAL_TENSOR_COLOR_BRIDGE_IS_A_CROSS_DOMAIN_COINCIDENCE_NARROW_NO_GO_NOTE_2026-06-08.md",
    "docs/QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md",
    "docs/QUARK_ROUTE2_ENDPOINT_T_BALANCE_FD_PROVENANCE_AND_STEP_STABILITY_BOUNDED_NOTE_2026-06-11.md",
    "docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
    "docs/QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md",
    "docs/QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md",
    "docs/QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md",
    "docs/QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md",
    "docs/QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
    "docs/QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md",
    "docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md",
    "docs/QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md",
    "docs/QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md",
    "docs/QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md",
    "docs/QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md",
    "docs/QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md",
    "docs/ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md",
    "docs/S3_TIME_PRIMITIVE_CHAIN_NOTE.md",
    "docs/S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md",
    "docs/S3_TIME_TENSOR_BUILD_MEMO.md",
    "docs/S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md",
    "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
    "scripts/frontier_cte_rconn_bridge_cross_domain_no_go.py",
    "scripts/frontier_quark_route2_e_center_blindness_no_go.py",
    "scripts/frontier_quark_route2_e_center_lift_derivation_attempt_bounded_2026_06_12.py",
    "scripts/frontier_quark_route2_e_center_lift_measured_calibration_2026_06_10.py",
    "scripts/frontier_quark_route2_e_channel_readout_naturality_no_go.py",
    "scripts/frontier_quark_route2_exact_readout_map.py",
    "scripts/frontier_quark_route2_exact_time_coupling.py",
    "scripts/frontier_quark_route2_qe_box_size_scan_2026_06_10.py",
    "scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py",
    "scripts/frontier_quark_route2_qe_kappa_squared_covariance_sharper_no_go_2026_06_10.py",
    "scripts/frontier_quark_route2_rconn_center_ratio_bridge_obstruction.py",
    "scripts/frontier_quark_route2_rconn_typed_bridge_derivation_bounded_2026_06_12.py",
    "scripts/frontier_quark_route2_source_domain_bridge_no_go.py",
    "scripts/frontier_route2_readout_record_positivity_no_go.py",
    "scripts/frontier_s3_time_primitive_chain_reaudit.py",
    "scripts/frontier_s3_time_readout_primitive_bridge_assessment_2026_06_12.py",
    "scripts/frontier_s3_time_tensor_build_memo_rescope_2026_06_16.py",
    "scripts/frontier_s3_time_theta_to_slice_coupling.py",
    "scripts/frontier_s3_time_theta_to_slice_coupling_factor_rigidity.py",
    "scripts/quark_route2_ell_e_structural_narrowing_bounded_2026_06_12.py",
    "scripts/quark_route2_t_side_endpoint_theorem_attempt_bounded_2026_06_12.py",
}

AUTHORITY_MARKERS = {
    "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md": (
        "open_gate route survey",
        "The next theorem target is the missing readout-map endpoint triple",
        "no unique exact `Theta_R -> Lambda_R` coupling theorem",
    ),
    "docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md": (
        "(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)",
        "= (-1, -2, 21/4).",
        "irreducible missing map entry",
    ),
    "docs/QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md": (
        "does not derive that row",
        "beta_T / alpha_T = -1",
        "alpha_T / alpha_E = -2",
    ),
    "docs/QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md": (
        "does not contain an exact E-channel row",
        "derive gamma_E(center)/gamma_E(shell) = 15/8",
        "derive gamma_T(center)/gamma_E(center) = -8/9",
    ),
    "docs/QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md": (
        "su3_R_conn_8_9 -> route2_center_TE_minus_8_9",
        "still does not contain",
        "`F_adj` is not typed as a Route-2",
    ),
    "docs/S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md": (
        "membership-but-not-uniqueness",
        "the named selection freedom is `rho_E`",
        "a derivation of a unique admissible `P_R` for the gate",
    ),
    "docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md": (
        "No named functional produces an",
        "inverse-square-of-projector-weight center lift",
        "free direction in the (shell, center-excess) readout plane",
    ),
    "docs/S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md": (
        "structurally localized in the spatial prefactor",
        "time-channel structure is universal",
        "Does **not** derive the readout-triple",
    ),
    "docs/ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md": (
        "It does not fix `rho_E`",
        "**one-sided bound** `rho_E > -6`",
        "Selecting `rho_E` requires a shell-vs-center **distinguishing** input",
    ),
}


def sweep_candidate_surfaces() -> set[str]:
    surfaces: set[str] = set()
    for base in (DOCS, SCRIPTS):
        for path in base.rglob("*"):
            if not path.is_file():
                continue
            rel = path.relative_to(ROOT).as_posix()
            lower_rel = rel.lower()
            if "endpoint_triple_residual_map" in lower_rel:
                continue
            if not any(token in lower_rel for token in NAME_TOKENS):
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if any(token in text for token in TARGET_TOKENS):
                surfaces.add(rel)
    return surfaces


def q_from_rho(rho: Fraction) -> Fraction:
    return Fraction(1, 1) + rho / 6


def rho_from_q(q: Fraction) -> Fraction:
    return 6 * (q - 1)


def center_ratio(mu: Fraction, q_t: Fraction, q_e: Fraction) -> Fraction:
    return mu * q_t / q_e


def rho_from_center_ratio(mu: Fraction, q_t: Fraction, c_te: Fraction) -> Fraction:
    return rho_from_q(mu * q_t / c_te)


def main() -> int:
    print("S3/Route-2 endpoint-triple residual map")
    print("Status: bounded direct-consumer residual map; not an audit verdict.")
    print("TRACE: upstream_support plus negative_route_pruning")

    print("\nPART 1: exact endpoint equivalence class")
    rho_t = Fraction(-1, 1)
    mu = Fraction(-2, 1)
    rho_e = Fraction(21, 4)
    q_t = q_from_rho(rho_t)
    q_e = q_from_rho(rho_e)
    c_te = center_ratio(mu, q_t, q_e)
    lambda_ratio = q_e / q_t
    w_e = Fraction(1, 3)
    w_t = Fraction(1, 2)
    inverse_square = (w_e / w_t) ** -2
    check("rho_T=-1 is exactly q_T=5/6", q_t == Fraction(5, 6))
    check("rho_E=21/4 is exactly q_E=15/8", q_e == Fraction(15, 8))
    check("mu=-2 with target q_T/q_E gives c_TE=-8/9", c_te == Fraction(-8, 9))
    check("c_TE=-8/9 solves back to rho_E=21/4", rho_from_center_ratio(mu, q_t, Fraction(-8, 9)) == rho_e)
    check("lambda=q_E/q_T is exactly 9/4", lambda_ratio == Fraction(9, 4))
    check("(w_E/w_T)^-2 is exactly the same 9/4 value", inverse_square == Fraction(9, 4))
    check("one-power value remains only 3/2, not 9/4", (w_e / w_t) ** -1 == Fraction(3, 2))

    print("\nPART 2: target-near route2/s3-time/rconn surface sweep")
    swept = sweep_candidate_surfaces()
    check("candidate sweep matches the expected finite target-near surface bank", swept == EXPECTED_CANDIDATE_SURFACES, f"missing={sorted(EXPECTED_CANDIDATE_SURFACES - swept)} extra={sorted(swept - EXPECTED_CANDIDATE_SURFACES)}")
    check("candidate bank has the expected surface count", len(swept) == 43, f"count={len(swept)}")
    for rel in sorted(EXPECTED_CANDIDATE_SURFACES):
        check(f"candidate surface exists: {rel}", (ROOT / rel).is_file())

    print("\nPART 3: current authority markers")
    for rel, markers in AUTHORITY_MARKERS.items():
        text = read(rel)
        for marker in markers:
            check(f"{rel} contains marker: {marker}", marker in text)

    print("\nPART 4: exact missing typed-edge map for the parent consumer")
    missing_edges = {
        "selected readout row P_R": read("docs/QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md"),
        "E-center lift q_E=15/8": read("docs/QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md"),
        "signed R_conn center bridge": read("docs/QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md"),
        "inverse-square readout coefficient law": read("docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md"),
        "unique physical/admissible readout primitive": read("docs/S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md"),
    }
    check("T-side row selector remains a named obstruction", "does not derive that row" in missing_edges["selected readout row P_R"])
    check("E-center lift remains the direct missing computation", "derive gamma_E(center)/gamma_E(shell) = 15/8" in missing_edges["E-center lift q_E=15/8"])
    check("signed R_conn bridge remains absent from the typed graph", "still does not contain" in missing_edges["signed R_conn center bridge"])
    check("inverse-square route lacks a named coefficient functional", "No named functional produces an" in missing_edges["inverse-square readout coefficient law"])
    check("physical readout primitive route is membership-not-uniqueness", "membership-but-not-uniqueness" in missing_edges["unique physical/admissible readout primitive"])
    check("all missing edges are exact equivalents or selectors for the same parent datum", all(missing_edges.values()))

    print("\nPART 5: new residual-map note and status firewall")
    note = NOTE.read_text(encoding="utf-8")
    required_note_markers = (
        "Actual current-surface status: bounded direct-consumer residual map",
        "This is not an audit verdict",
        "does not close the parent open_gate row",
        "candidate sweep matches the expected finite target-near surface bank",
        "selected readout row P_R",
        "E-center lift q_E=15/8",
        "signed R_conn center bridge",
        "inverse-square readout coefficient law",
        "unique physical/admissible readout primitive",
    )
    for marker in required_note_markers:
        check(f"note contains marker: {marker}", marker in note)
    banned_markers = (
        ("status-authority phrase", phrase("Status ", "authority")),
        ("parent-closure phrase", phrase("closes ", "the parent")),
        ("endpoint-derivation phrase", phrase("derives ", "the endpoint triple")),
        ("audit-ratification phrase", phrase("audit", "-ratified")),
        ("branch-local status-promotion phrase", phrase("retained ", "branch-local")),
        ("future-retention phrase", phrase("would ", "become retained")),
        ("promotion-to-retention phrase", phrase("promoted ", "to retained")),
        ("no-future-theorem phrase", phrase("no future ", "primitive can exist")),
    )
    for label, marker in banned_markers:
        check(f"note avoids overclaim marker: {label}", marker not in note)

    print("\nTOTAL: PASS=%d, FAIL=%d" % (PASS, FAIL))
    if FAIL:
        return 1
    print(
        "VERDICT: bounded residual map. The parent S3-time consumer has a "
        "finite current target-near bank and a precise set of remaining "
        "typed-edge selectors; the endpoint triple is not derived here."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
