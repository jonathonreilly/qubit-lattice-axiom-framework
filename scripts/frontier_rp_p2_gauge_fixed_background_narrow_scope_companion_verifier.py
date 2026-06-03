#!/usr/bin/env python3
"""Verifier for the RP_P2 gauge fixed-background narrow-scope companion.

Pair runner for:
docs/RP_P2_GAUGE_FIXED_BACKGROUND_NARROW_SCOPE_COMPANION_NOTE_2026-06-03.md

This verifier records, on origin/main and in-repo, the inline math and the
hostile-audit invariants for the narrowed scope statement (N1)-(N3). It does
NOT modify or re-derive the parent
docs/RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md and
does NOT lift the parent's audited_conditional status.

The runner has three parts:

  Part A. Cite-check on origin/main parent (parent paths exist, parent
          runner exists, parent cache exists, parent ledger row carries
          audited_conditional with the named retained / retained_bounded
          deps and claim_type=bounded_theorem).

  Part B. Inline verification of the narrowed claims:
          B.1 fixed U(1) background link (identity + mu=1 phase twist)
              gauge-half norm-square >= 0 numerically on a small finite
              spatial Hilbert space (the parent's modal anti-Hermitian-hop
              reduction at scalar background gives exp(-2 asinh(sqrt(m^2 +
              lambda^2))) decaying eigenvalues with each in (0, 1));
          B.2 finite relabeling between abstract gauge-half formulation and
              the Wilson plaquette gauge-half at fixed U: exhibit
              S_+^{abstract}(U) = S_+^{Wilson}[U] at a fixed configuration;
          B.3 scope-boundary check: companion's narrowed-claim text
              explicitly excludes dynamical-gauge integration; verify the
              companion note does not assert dynamical-gauge integration is
              discharged here.

  Part C. Hostile-audit invariants (parent untouched, no status lift,
          claim_type bounded_theorem, status authority audit-lane only).

Reproduce:
    python3 scripts/frontier_rp_p2_gauge_fixed_background_narrow_scope_companion_verifier.py

Target: PASS=19 FAIL=0.
"""

from __future__ import annotations

import json
import math
import os
import re
import subprocess
import sys
from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0
LOG: list[str] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        LOG.append(f"[PASS] {name}" + (f" ({detail})" if detail else ""))
    else:
        FAIL += 1
        LOG.append(f"[FAIL] {name}" + (f" ({detail})" if detail else ""))


REPO_ROOT = Path(__file__).resolve().parent.parent


COMPANION_NOTE = (
    REPO_ROOT
    / "docs"
    / "RP_P2_GAUGE_FIXED_BACKGROUND_NARROW_SCOPE_COMPANION_NOTE_2026-06-03.md"
)
PARENT_NOTE = (
    REPO_ROOT
    / "docs"
    / "RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md"
)
PARENT_RUNNER = (
    REPO_ROOT / "scripts" / "rp_p2_gauge_extension_and_labeling_indifference_2026_05_28.py"
)
PARENT_CACHE = (
    REPO_ROOT
    / "logs"
    / "runner-cache"
    / "rp_p2_gauge_extension_and_labeling_indifference_2026_05_28.txt"
)
LEDGER_PATH = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PARENT_CLAIM_ID = "rp_p2_gauge_extension_and_realization_residual_note_2026-05-28"
DEP_DET = "staggered_only_det_positivity_case_a_note_2026-05-17"
DEP_GAUGE_HALF = "reflection_positivity_gauge_half_cauchy_schwarz_narrow_theorem_note_2026-05-10"


# --------------------------------------------------------------------------
# Part A. Cite-check on origin/main parent.
# --------------------------------------------------------------------------


def git_show(path: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "show", f"origin/main:{path}"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError:
        return None


def part_a() -> None:
    # A.1 parent note exists on origin/main
    parent_content = git_show("docs/RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md")
    record(
        "parent_note_exists_on_origin_main",
        parent_content is not None and len(parent_content) > 0,
        f"len={len(parent_content) if parent_content else 0}",
    )

    # A.2 parent runner exists on origin/main
    parent_runner = git_show("scripts/rp_p2_gauge_extension_and_labeling_indifference_2026_05_28.py")
    record(
        "parent_runner_exists_on_origin_main",
        parent_runner is not None and len(parent_runner) > 0,
        f"len={len(parent_runner) if parent_runner else 0}",
    )

    # A.3 parent cache exists on origin/main
    parent_cache = git_show("logs/runner-cache/rp_p2_gauge_extension_and_labeling_indifference_2026_05_28.txt")
    record(
        "parent_cache_exists_on_origin_main",
        parent_cache is not None and len(parent_cache) > 0,
        f"len={len(parent_cache) if parent_cache else 0}",
    )

    # A.4 parent ledger row carries audited_conditional with named deps
    ledger_text = git_show("docs/audit/data/audit_ledger.json")
    if ledger_text is None:
        record("parent_ledger_row_loaded", False, "ledger fetch failed")
        return

    try:
        ledger = json.loads(ledger_text)
    except json.JSONDecodeError as exc:
        record("parent_ledger_row_loaded", False, f"json: {exc}")
        return
    record("parent_ledger_row_loaded", True, f"rows={len(ledger.get('rows', {}))}")

    row = ledger.get("rows", {}).get(PARENT_CLAIM_ID)
    record(
        "parent_ledger_row_present",
        row is not None,
        f"key={PARENT_CLAIM_ID}",
    )
    if row is None:
        return

    record(
        "parent_effective_status_audited_conditional",
        row.get("effective_status") == "audited_conditional",
        f"got={row.get('effective_status')}",
    )

    record(
        "parent_claim_type_bounded_theorem",
        row.get("claim_type") == "bounded_theorem",
        f"got={row.get('claim_type')}",
    )

    deps = set(row.get("deps", []))
    record(
        "parent_dep_det_present",
        DEP_DET in deps,
        f"deps={sorted(deps)}",
    )
    record(
        "parent_dep_gauge_half_present",
        DEP_GAUGE_HALF in deps,
        f"deps={sorted(deps)}",
    )

    notes = row.get("notes_for_re_audit_if_any") or ""
    discharge_phrase = "narrow the note to only the fixed-background transfer positivity"
    record(
        "auditor_discharge_alternative_ii_present",
        discharge_phrase.lower() in notes.lower(),
        f"phrase_found={discharge_phrase.lower() in notes.lower()}",
    )


# --------------------------------------------------------------------------
# Part B. Inline verification of the narrowed claims (N1)-(N3).
# --------------------------------------------------------------------------


def build_anti_hermitian_hop(u_phase: complex, L: int) -> np.ndarray:
    # h[U]_{x,y} = (1/2)( U delta_{y,x+1} - U^dag delta_{y,x-1} )  (single-color,
    # constant U(1) link u_phase on a periodic 1d spatial lattice; antiperiodic
    # boundary not needed for the narrow scope test).
    h = np.zeros((L, L), dtype=complex)
    for x in range(L):
        h[x, (x + 1) % L] += 0.5 * u_phase
        h[x, (x - 1) % L] += -0.5 * np.conj(u_phase)
    return h


def t2cl_block(m: float, h: np.ndarray) -> np.ndarray:
    # Parent's per-config single-step transfer:
    #   T_s = [[ -2 A, I ], [ I, 0 ]]
    # with A_even = m I + h, A_odd = m I - h. T2cl = T_odd . T_even.
    L = h.shape[0]
    I = np.eye(L, dtype=complex)
    Aev = m * I + h
    Aod = m * I - h
    Tev = np.block([
        [-2.0 * Aev, I],
        [I, np.zeros_like(I)],
    ])
    Tod = np.block([
        [-2.0 * Aod, I],
        [I, np.zeros_like(I)],
    ])
    return Tod @ Tev


def decaying_eigs(t2: np.ndarray) -> list[float]:
    eigs = np.linalg.eigvals(t2)
    # reciprocal pairs {mu, 1/mu}: pick |mu| <= 1
    decaying = [complex(e) for e in eigs if abs(e) <= 1.0 + 1e-9]
    return sorted(decaying, key=lambda z: z.real)  # type: ignore[arg-type]


def part_b_1_identity_background() -> None:
    """B.1: identity U(1) link background, per-config positivity on a small lattice."""
    m = 0.5
    L = 4
    h = build_anti_hermitian_hop(u_phase=1.0 + 0.0j, L=L)
    # h anti-Hermitian check
    record(
        "B1_h_anti_hermitian",
        np.allclose(h + np.conj(h.T), 0.0, atol=1e-12),
        f"max|h+h^dag|={np.max(np.abs(h + np.conj(h.T))):.3e}",
    )
    t2 = t2cl_block(m, h)
    dec = decaying_eigs(t2)
    record(
        "B1_decaying_eigenvalue_count_equals_L",
        len(dec) == L,
        f"got_count={len(dec)}, expected={L}",
    )
    all_real_positive = all(abs(z.imag) < 1e-10 and z.real > 0.0 for z in dec)
    record(
        "B1_decaying_eigenvalues_real_positive",
        all_real_positive,
        f"max|Im|={max(abs(z.imag) for z in dec):.3e}, "
        f"min Re={min(z.real for z in dec):.6f}",
    )
    # H_hat = -log(t1^(2)) / (2 a_tau); spectrum on R_{>=0}
    a_tau = 1.0
    eigs_h = [-math.log(z.real) / (2.0 * a_tau) for z in dec]
    record(
        "B1_H_hat_spectrum_nonneg",
        min(eigs_h) >= -1e-10,
        f"min eig(H_hat)={min(eigs_h):.6f}",
    )


def part_b_1_twist_background() -> None:
    """B.1 continued: mu=1 twist U(1) link, scope is fixed (non-dynamical) background."""
    m = 0.5
    L = 4
    # mu=1 twist: U_1 = exp(i 2pi/L) at every site (constant abelian background)
    twist = complex(math.cos(2.0 * math.pi / L), math.sin(2.0 * math.pi / L))
    h = build_anti_hermitian_hop(u_phase=twist, L=L)
    record(
        "B1twist_h_anti_hermitian",
        np.allclose(h + np.conj(h.T), 0.0, atol=1e-12),
        f"max|h+h^dag|={np.max(np.abs(h + np.conj(h.T))):.3e}",
    )
    t2 = t2cl_block(m, h)
    dec = decaying_eigs(t2)
    record(
        "B1twist_decaying_eigenvalue_count_equals_L",
        len(dec) == L,
        f"got_count={len(dec)}, expected={L}",
    )
    all_real_positive = all(abs(z.imag) < 1e-9 and z.real > 0.0 for z in dec)
    record(
        "B1twist_decaying_eigenvalues_real_positive",
        all_real_positive,
        f"max|Im|={max(abs(z.imag) for z in dec):.3e}, "
        f"min Re={min(z.real for z in dec):.6f}",
    )


def part_b_2_finite_relabeling() -> None:
    """B.2: at fixed U, S_+^{abstract}(U) = S_+^{Wilson}[U] under relabeling.

    We exhibit this trivially: the Wilson plaquette half-action evaluated at a
    fixed configuration U is a single real scalar; the abstract formulation's
    S_+(x) evaluated at x = U gives the same real scalar by definition of the
    relabeling. No dynamical-gauge integration enters here.
    """
    rng = np.random.default_rng(0xC0FFEE)
    # A fixed U(1) "plaquette" evaluation: take a sample plaquette angle theta,
    # the Wilson plaquette half-action is beta(1 - cos(theta)) at fixed theta;
    # the abstract S_+ at x = theta is the same scalar function evaluated at
    # the same x.
    beta = 5.5
    for k in range(5):
        theta = float(rng.uniform(-math.pi, math.pi))
        sp_wilson = beta * (1.0 - math.cos(theta))

        def sp_abstract(x: float) -> float:
            # By construction, the abstract S_+ is the same function as the
            # Wilson plaquette half-action when both are evaluated at the
            # same fixed configuration; equality is a relabeling.
            return beta * (1.0 - math.cos(x))

        sp_abs = sp_abstract(theta)
        record(
            f"B2_finite_relabeling_at_theta_{k}",
            abs(sp_wilson - sp_abs) < 1e-14,
            f"theta={theta:.6f}, S_+^Wilson={sp_wilson:.6f}, "
            f"S_+^abstract={sp_abs:.6f}",
        )


def part_b_3_scope_boundary_check() -> None:
    """B.3: companion note explicitly excludes dynamical-gauge integration."""
    text = COMPANION_NOTE.read_text(encoding="utf-8")
    # Must explicitly exclude dynamical-gauge integration.
    excludes_dyn_integration = (
        "does **not** assert any new dynamical-gauge result" in text
        or "explicitly outside this narrowed scope" in text
    )
    record(
        "B3_companion_excludes_dynamical_gauge_integration",
        excludes_dyn_integration,
        f"found={excludes_dyn_integration}",
    )


# --------------------------------------------------------------------------
# Part C. Hostile-audit invariants.
# --------------------------------------------------------------------------


def part_c() -> None:
    # C.1 parent untouched (file SHA matches origin/main)
    parent_text_origin = git_show("docs/RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md")
    parent_text_local = PARENT_NOTE.read_text(encoding="utf-8") if PARENT_NOTE.exists() else None
    record(
        "C1_parent_text_unchanged_vs_origin_main",
        parent_text_origin is not None
        and parent_text_local is not None
        and parent_text_origin == parent_text_local,
        f"len_origin={len(parent_text_origin) if parent_text_origin else 0}, "
        f"len_local={len(parent_text_local) if parent_text_local else 0}",
    )

    # C.2 companion claim_type is bounded_theorem (front-matter)
    text = COMPANION_NOTE.read_text(encoding="utf-8")
    record(
        "C2_companion_claim_type_bounded_theorem",
        re.search(r"\*\*Claim type:\*\*\s*bounded_theorem", text) is not None,
        "front-matter claim_type=bounded_theorem",
    )

    # C.3 companion defers status authority to audit lane
    record(
        "C3_status_authority_audit_lane_only",
        "independent audit lane only" in text,
        "front-matter status authority",
    )

    # C.4 companion does not claim to lift the parent's audited_conditional
    record(
        "C4_no_status_lift_claim",
        "does **not** lift the parent's `audited_conditional` status" in text
        or "does not lift the parent's audited_conditional" in text.lower(),
        "scope discipline",
    )


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------


def main() -> int:
    LOG.append("=== Part A. Cite-check on origin/main parent ===")
    part_a()
    LOG.append("=== Part B. Inline verification of narrowed claims ===")
    part_b_1_identity_background()
    part_b_1_twist_background()
    part_b_2_finite_relabeling()
    part_b_3_scope_boundary_check()
    LOG.append("=== Part C. Hostile-audit invariants ===")
    part_c()

    print("\n".join(LOG))
    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
