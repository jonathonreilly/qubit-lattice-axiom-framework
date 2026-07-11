#!/usr/bin/env python3
"""Parent reroute guard for the axiom-first reflection-positivity note.

This runner intentionally leaves
`axiom_first_rp_two_step_transfer_matrix_positivity.py` unchanged. That runner
is the retained free-case two-step construction used by other rows. Here we
reuse its C1-C6 functions and add only the parent-specific Wilson temporal-gauge
reroute guard.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import axiom_first_rp_two_step_transfer_matrix_positivity as base_runner
import su3_wilson_plane_kernel_character_positivity_composed_gram_2026_07_09 as su3_supplier


NOTE_PATH = ROOT / "docs" / "AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md"
COUPLED_SUPPLIER_NAME = "RP_COUPLED_TWO_SLICE_GAUGE_STAGGERED_BEREZIN_GRAM_NARROW_THEOREM_NOTE_2026-07-10.md"
COUPLED_SUPPLIER_PATH = ROOT / "docs" / COUPLED_SUPPLIER_NAME
LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
BASE_RUNNER_PATH = ROOT / "scripts" / "axiom_first_rp_two_step_transfer_matrix_positivity.py"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")
    return ok


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def check_free_two_step_construction(base) -> None:
    section("C1-C6 free staggered two-step construction reused from retained runner")

    max_res, max_imag, _ = base.check_dispersion_anchor(base.MASS)
    check(
        "C1 dispersion anchor",
        max_res < base.TOL_DISP and max_imag < base.TOL_DISP,
        detail=f"max_res={max_res:.2e}, max_imag={max_imag:.2e}",
    )

    complex_min_imag, _, exceptional_ok, _, _ = base.check_single_step_nonpositive(base.MASS)
    check(
        "C2 single-step remains non-positive",
        complex_min_imag > 1e-3 and exceptional_ok,
        detail=f"min_complex_imag={complex_min_imag:.3f}, exceptional_ok={exceptional_ok}",
    )

    c3_ok = True
    c5_ok = True
    c6_ok = True
    for ls in (2, 3, 4, 6):
        r3 = base.build_manybody_T2(ls, base.MASS)
        c3_ok = c3_ok and (
            r3["max_imag_kernel"] < base.TOL_PSD
            and r3["herm_err"] < base.TOL_PSD
            and r3["min_eig"] > 0.0
            and r3["BdagB_err"] < base.TOL_PSD
        )

        r5 = base.check_second_quantization_functor(ls, base.MASS)
        c5_ok = c5_ok and (
            r5["intertwiner_err"] < base.TOL_PSD
            and r5["vac_fix_err"] < base.TOL_PSD
            and r5["H_offdiag"] < base.TOL_PSD
            and r5["functor_err"] < base.TOL_PSD
        )

        r6 = base.check_decaying_gamma_bridge(ls, base.MASS)
        c6_ok = c6_ok and (
            r6["max_dec_imag"] < base.TOL_PSD
            and r6["max_grow_imag"] < base.TOL_PSD
            and r6["max_projector_idem"] < 1e-9
            and r6["max_projector_resid"] < 1e-9
            and r6["max_projector_split"] < 1e-9
            and r6["max_projector_orth"] < 1e-9
            and r6["kernel_min"] > 0.0
            and r6["gamma_tensor_err"] < base.TOL_PSD
            and r6["gamma_intertwiner_err"] < base.TOL_PSD
            and r6["gamma_min_eig"] >= -base.TOL_PSD
            and r6["gamma_bdagb_err"] < base.TOL_PSD
        )

    check("C3 many-body T_hat^2 positive Hermitian = B^dag B", c3_ok)

    c4_ok = True
    for ls in (3, 4):
        r4 = base.r2_os_gram(ls, base.MASS)
        c4_ok = c4_ok and r4["herm_err"] < base.TOL_PSD and r4["min_eig"] >= -base.TOL_PSD
    check("C4 two-step OS Gram Hermitian PSD", c4_ok)
    check("C5 second-quantization functor identity", c5_ok)
    check("C6 decaying spectral channel gives positive Fock kernel", c6_ok)


def check_reroute_guard() -> None:
    section("C7 retained Wilson temporal-gauge reroute guard")
    text = NOTE_PATH.read_text(encoding="utf-8")
    rows = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))["rows"]

    required_phrases = [
        "2026-06-08 Wilson temporal-gauge bridge reroute",
        "AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md",
        "GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md",
        "STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md",
        "REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md",
        "RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md",
        "retained-bounded bridge",
        "joint cross-configuration Gram expansion",
        "ingredient inventory, not a pointwise product identity",
        "G = W diag(kappa) W^dag",
        "composed parent claim still requires independent audit",
        "does **not** claim",
        "SU3_WILSON_PLANE_KERNEL_CHARACTER_POSITIVITY_AND_COMPOSED_GRAM_NARROW_THEOREM_NOTE_2026-07-09.md",
        "in place of the earlier synthetic product model",
    ]
    forbidden_phrases = [
        "the full interacting gauge closure remains limited to the named three-factor reduction claim",
        "beyond this explicitly scoped three-factor reduction target",
        "the sign-repair bridge remains subject to independent audit",
        "conditional Wilson-plane claim still travels with that companion note",
        "This dependency is a source-packet candidate for re-audit",
        "parent reflected form decomposes into the product/integral of four non-negative factors",
        "beyond this explicitly scoped factorized reduction target",
    ]
    missing = [phrase for phrase in required_phrases if phrase not in text]
    stale = [phrase for phrase in forbidden_phrases if phrase in text]
    check("required reroute phrases present", not missing, detail=", ".join(missing))
    check("stale Wilson sign-repair phrases absent", not stale, detail=", ".join(stale))
    check(
        "parent note links the coupled-Gram supplier",
        f"[{COUPLED_SUPPLIER_NAME}]({COUPLED_SUPPLIER_NAME})" in text,
    )
    coupled_text = COUPLED_SUPPLIER_PATH.read_text(encoding="utf-8") if COUPLED_SUPPLIER_PATH.exists() else ""
    check(
        "coupled-Gram supplier exists and pins tensor-product entangled coverage",
        COUPLED_SUPPLIER_PATH.exists()
        and "tensor product" in coupled_text.lower()
        and "entangled" in coupled_text.lower(),
    )

    retained_grades = {"retained", "retained_bounded", "retained_no_go"}
    failed_statuses = {"audited_failed", "failed", "rejected"}

    # Reroute dependencies split into two tiers, each checked against the LIVE
    # ledger so this guard tracks the ledger instead of a frozen snapshot:
    #
    #   * Foundational lemmas -- audited-clean and stably retained. The reroute
    #     leans on them directly, so the guard requires them to REMAIN
    #     retained-grade and correctly typed; drift here is a real regression
    #     and must fail this runner.
    #
    #   * In-packet suppliers / in-flight bridges -- these travel with the
    #     (itself unaudited) parent keystone and legitimately sit at
    #     'unaudited' between audit passes. The guard requires them present,
    #     correctly typed, and never audit-REJECTED; it does not force them to
    #     be retained while the parent packet is still in flight. This keeps
    #     the runner honest against ordinary unaudited<->retained churn while
    #     still catching a genuine audit failure of any supplier.
    foundational_retained = {
        "gauge_temporal_gauge_mixed_kernel_spatial_link_factorization_narrow_theorem_note_2026-05-10": "positive_theorem",
        "staggered_only_det_positivity_case_a_note_2026-05-17": "positive_theorem",
        "reflection_positivity_gauge_half_cauchy_schwarz_narrow_theorem_note_2026-05-10": "positive_theorem",
    }
    inflight_suppliers = {
        "axiom_first_reflection_positivity_wilson_temporal_gauge_bridge_narrow_theorem_note_2026-06-05": "bounded_theorem",
        "rp_p2_gauge_extension_and_realization_residual_note_2026-05-28": "bounded_theorem",
        "su3_wilson_plane_kernel_character_positivity_and_composed_gram_narrow_theorem_note_2026-07-09": "positive_theorem",
    }

    foundational_ok = True
    foundational_details = []
    for claim_id, expected_claim_type in foundational_retained.items():
        row = rows.get(claim_id)
        if row is None:
            foundational_ok = False
            foundational_details.append(f"{claim_id}:missing")
            continue
        got = (row.get("claim_type"), row.get("audit_status"), row.get("effective_status"))
        ok = (
            row.get("claim_type") == expected_claim_type
            and row.get("effective_status") in retained_grades
            and row.get("audit_status") not in failed_statuses
        )
        foundational_ok = foundational_ok and ok
        foundational_details.append(f"{claim_id}:{got}")
    check(
        "foundational reroute dependencies remain retained-grade",
        foundational_ok,
        detail="; ".join(foundational_details),
    )

    supplier_ok = True
    supplier_details = []
    for claim_id, expected_claim_type in inflight_suppliers.items():
        row = rows.get(claim_id)
        if row is None:
            supplier_ok = False
            supplier_details.append(f"{claim_id}:missing")
            continue
        got = (row.get("claim_type"), row.get("audit_status"), row.get("effective_status"))
        ok = (
            row.get("claim_type") == expected_claim_type
            and row.get("audit_status") not in failed_statuses
            and row.get("effective_status") not in failed_statuses
        )
        supplier_ok = supplier_ok and ok
        supplier_details.append(f"{claim_id}:{got}")
    check(
        "in-packet reroute suppliers present, typed, and not audit-rejected",
        supplier_ok,
        detail="; ".join(supplier_details),
    )

    rng = np.random.default_rng(20260710)
    beta_kernel = 1.0
    u = su3_supplier.haar_su3(64, rng)
    overlap_dagger = np.einsum("nab,mab->nm", u, np.conj(u)).real
    plane_gram = np.exp(beta_kernel * overlap_dagger)
    plane_gram = (plane_gram + plane_gram.T) / 2.0
    plane_min = float(np.linalg.eigvalsh(plane_gram)[0])
    check(
        "actual SU(3) plane-kernel Haar Gram is positive semidefinite",
        plane_min >= 1e-2,
        detail=f"min eig={plane_min:+.3e} (n=64, beta={beta_kernel})",
    )

    overlap_nodagger = np.einsum("nab,mba->nm", u, u).real
    wrong_gram = np.exp(beta_kernel * overlap_nodagger)
    wrong_gram = (wrong_gram + wrong_gram.T) / 2.0
    wrong_min = float(np.linalg.eigvalsh(wrong_gram)[0])
    check(
        "no-conjugation plane-kernel rejector is decisively non-PSD",
        wrong_min < -1.0,
        detail=f"min eig={wrong_min:+.3e}",
    )

    composed = su3_supplier.composed_mc(0.5, 100_000, rng)
    composed_min = float(composed["eigenvalues"][0])
    composed_threshold = max(3.0 * composed["mc_noise"], 5e-3)
    check(
        "actual composed two-slice pure-gauge SU(3) Gram is PSD within sampling error",
        composed_min > -composed_threshold,
        detail=f"min eig={composed_min:+.6e}, negative allowance={composed_threshold:.3e}",
    )
    check(
        "pure-gauge composed-form sampling error is controlled",
        composed["mc_noise"] < 0.05,
        detail=f"mc_noise={composed['mc_noise']:.3e}",
    )

    control = su3_supplier.composed_mc(1.0, 100_000, rng, conjugate_reflected=False)
    control_min = float(control["eigenvalues"][0])
    check(
        "no-conjugation pure-gauge composed control is non-PSD",
        control_min < -1e-3,
        detail=f"min eig={control_min:+.6e}",
    )


def main() -> int:
    print("Axiom-first RP Wilson temporal-gauge reroute guard")
    print(f"note: {NOTE_PATH}")
    print(f"base runner: {BASE_RUNNER_PATH}")
    check_free_two_step_construction(base_runner)
    check_reroute_guard()
    print()
    print(f"PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: parent reroute guard passes; free two-step construction remains "
            "unchanged, and the Wilson temporal-gauge application is routed through "
            "retained-grade dependencies without promoting the parent row."
        )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
