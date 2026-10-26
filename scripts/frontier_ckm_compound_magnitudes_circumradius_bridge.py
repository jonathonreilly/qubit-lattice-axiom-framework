#!/usr/bin/env python3
"""CKM compound-magnitude circumradius bridge.

Checks the supplied algebraic closed forms in
  docs/CKM_COMPOUND_MAGNITUDES_CIRCUMRADIUS_BRIDGE_THEOREM_NOTE_2026-04-25.md

Conditional identities for the supplied hybrid magnitude formulas:

  (C1) Three-magnitude circumradius bridge (NEW):
        N_color * |V_td|^2  =  N_pair * (N_quark - 1) * |V_us|^2 * |V_cb|^2 * R_bar^2,

       i.e.,
        3 |V_td|^2  =  10 |V_us|^2 |V_cb|^2 R_bar^2,
       or
        |V_td|^2  =  (N_pair (N_quark - 1)/N_color) |V_us|^2 |V_cb|^2 R_bar^2
                  =  (10/3) |V_us|^2 |V_cb|^2 R_bar^2.

  (C2) Four-magnitude circumradius bridge (NEW):
        (|V_td V_us| / |V_cb V_ub|)^2  =  N_pair^2 * N_color * (N_quark - 1) * R_bar^2 / alpha_s
                                        =  60 R_bar^2 / alpha_s.

  (C3) Equivalent form (eliminating alpha_s via |V_us|^2 = alpha_s/N_pair):
        (|V_td V_us| / |V_cb V_ub|)^2  =  N_pair * N_color * (N_quark - 1)
                                          * R_bar^2 / |V_us|^2
                                        =  30 R_bar^2 / |V_us|^2.

  (C4) PDG numerical comparison.
"""

from __future__ import annotations

# Actual documentary reads/existence checks; presence is not scientific authority.
AUDIT_INPUT_PATHS = ['docs/CKM_NLO_BARRED_TRIANGLE_PROTECTED_GAMMA_THEOREM_NOTE_2026-04-25.md', 'docs/CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md', 'docs/CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md', 'docs/CKM_BARRED_CIRCUMRADIUS_EXACT_CLOSED_FORM_THEOREM_NOTE_2026-04-25.md', 'docs/WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md']

import math
import re
import sys
from pathlib import Path

import sympy as sp


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {name}{suffix}")
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1


def banner(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


REPO_ROOT = Path(__file__).resolve().parents[1]


def read_authority(rel_path: str) -> str:
    path = REPO_ROOT / rel_path
    if not path.exists():
        return ""
    return path.read_text()


def extract_status_text(content: str) -> str:
    if not content:
        return ""
    for line in content.splitlines()[:30]:
        stripped = line.strip()
        if stripped.lower().startswith("**status:**") or stripped.lower().startswith("status:"):
            text = stripped
            for prefix in ("**Status:**", "**status:**", "Status:", "status:"):
                if text.lower().startswith(prefix.lower()):
                    text = text[len(prefix):].strip()
                    break
            return text
    return ""


def audit_inputs() -> None:
    banner("Documentary dependency inventory, not retention proof")
    paths = (
        "docs/CKM_NLO_BARRED_TRIANGLE_PROTECTED_GAMMA_THEOREM_NOTE_2026-04-25.md",
        "docs/CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md",
        "docs/CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md",
        "docs/CKM_BARRED_CIRCUMRADIUS_EXACT_CLOSED_FORM_THEOREM_NOTE_2026-04-25.md",
        "docs/WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md",
    )
    for path in paths:
        content = read_authority(path)
        print(f"  {path}: Status text={extract_status_text(content)!r} (metadata only)")
        check(f"documentary source present: {path}", bool(content))
    print("  No status string is classified as retained authority; identities use supplied values.")


def extract_retained_inputs() -> dict:
    banner("Checking documentary count patterns; supplied numeric inputs are 2,3,6")

    counts = read_authority(
        "docs/CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md"
    )
    n_pair_match = re.search(r"n[_\s]pair\s*=\s*(\d+)", counts, re.IGNORECASE)
    n_color_match = re.search(r"n[_\s]color\s*=\s*(\d+)", counts, re.IGNORECASE)
    n_quark_match = re.search(r"n[_\s]quark\s*=\s*n[_\s]pair\s*n[_\s]color", counts, re.IGNORECASE)

    print(f"  N_pair extracted:                  {n_pair_match.group(0) if n_pair_match else 'NOT FOUND'}")
    print(f"  N_color extracted:                 {n_color_match.group(0) if n_color_match else 'NOT FOUND'}")
    print(f"  N_quark = N_pair * N_color:        {'FOUND' if n_quark_match else 'NOT FOUND'}")

    check("MAGNITUDES text contains N_pair = 2", n_pair_match and int(n_pair_match.group(1)) == 2)
    check("MAGNITUDES text contains N_color = 3", n_color_match and int(n_color_match.group(1)) == 3)
    check("MAGNITUDES text contains N_quark = N_pair * N_color (=6)", bool(n_quark_match))

    return {
        "N_pair": 2,
        "N_color": 3,
        "N_quark": 6,
    }


def setup_symbolic(N: dict):
    a_s = sp.symbols("alpha_s", positive=True)

    lambda_sq = a_s / 2
    A_sq = sp.Rational(2, 3)
    rho = sp.Rational(1, 6)
    eta = sp.sqrt(5) / 6

    Vus_sq = lambda_sq
    Vcb_sq = A_sq * lambda_sq ** 2
    Vub_sq = A_sq * lambda_sq ** 3 * (rho ** 2 + eta ** 2)

    rho_bar = (4 - a_s) / 24
    eta_bar = sp.sqrt(5) * (4 - a_s) / 24
    R_bar_sq = sp.Rational(1, 4) + a_s ** 2 / 320
    Vtd_sq = A_sq * lambda_sq ** 3 * ((1 - rho_bar) ** 2 + eta_bar ** 2)
    Vts_sq = A_sq * lambda_sq ** 2

    return {
        "a_s": a_s,
        "Vus_sq": Vus_sq,
        "Vcb_sq": Vcb_sq,
        "Vub_sq": Vub_sq,
        "Vtd_sq": Vtd_sq,
        "Vts_sq": Vts_sq,
        "R_bar_sq": R_bar_sq,
    }


def audit_c1_three_magnitude_bridge(N: dict, S: dict) -> None:
    banner("C1: NEW three-magnitude circumradius bridge")

    a_s = S["a_s"]
    Vtd_sq = S["Vtd_sq"]
    Vus_sq = S["Vus_sq"]
    Vcb_sq = S["Vcb_sq"]
    R_bar_sq = S["R_bar_sq"]

    N_pair, N_color, N_quark = N["N_pair"], N["N_color"], N["N_quark"]
    expected = sp.simplify(
        sp.Rational(N_pair * (N_quark - 1), N_color) * Vus_sq * Vcb_sq * R_bar_sq
    )
    diff = sp.simplify(Vtd_sq - expected)

    print(f"  |V_td|^2 (computed) = {sp.simplify(Vtd_sq)}")
    print(f"  Expected: (N_pair (N_quark - 1)/N_color) |V_us|^2 |V_cb|^2 R_bar^2")
    print(f"          = (10/3) |V_us|^2 |V_cb|^2 R_bar^2")
    print(f"          = {expected}")
    print(f"  Difference: {diff}")

    check("C1: |V_td|^2 = (N_pair (N_quark - 1)/N_color) |V_us|^2 |V_cb|^2 R_bar^2",
          diff == 0)

    # Equivalent form: N_color |V_td|^2 = N_pair (N_quark - 1) |V_us|^2 |V_cb|^2 R_bar^2.
    diff_alt = sp.simplify(N_color * Vtd_sq - N_pair * (N_quark - 1) * Vus_sq * Vcb_sq * R_bar_sq)
    check("C1 alt: N_color |V_td|^2 = N_pair (N_quark - 1) |V_us|^2 |V_cb|^2 R_bar^2",
          diff_alt == 0)


def audit_c2_four_magnitude_bridge(N: dict, S: dict) -> None:
    banner("C2: NEW four-magnitude circumradius bridge")

    a_s = S["a_s"]
    Vtd_sq = S["Vtd_sq"]
    Vus_sq = S["Vus_sq"]
    Vcb_sq = S["Vcb_sq"]
    Vub_sq = S["Vub_sq"]
    R_bar_sq = S["R_bar_sq"]

    compound_sq = sp.simplify(Vtd_sq * Vus_sq / (Vcb_sq * Vub_sq))

    N_pair, N_color, N_quark = N["N_pair"], N["N_color"], N["N_quark"]
    expected = sp.simplify(N_pair ** 2 * N_color * (N_quark - 1) * R_bar_sq / a_s)
    diff = sp.simplify(compound_sq - expected)

    print(f"  (|V_td V_us|/|V_cb V_ub|)^2 (computed) = {compound_sq}")
    print(f"  Expected: N_pair^2 N_color (N_quark - 1) R_bar^2 / alpha_s")
    print(f"          = 60 R_bar^2 / alpha_s")
    print(f"          = {expected}")
    print(f"  Difference: {diff}")

    check("C2: (|V_td V_us|/|V_cb V_ub|)^2 = N_pair^2 N_color (N_quark - 1) R_bar^2 / alpha_s",
          diff == 0)

    # Alternative form using |V_us|^2 = alpha_s/N_pair: alpha_s = N_pair |V_us|^2.
    # Thus 60/alpha_s = 60/(N_pair |V_us|^2) = 30/|V_us|^2.
    expected_alt2 = sp.simplify(N_pair * N_color * (N_quark - 1) * R_bar_sq / Vus_sq)
    diff_alt = sp.simplify(compound_sq - expected_alt2)
    print(f"\n  Equivalent form: 30 R_bar^2 / |V_us|^2")
    print(f"          = N_pair N_color (N_quark - 1) R_bar^2 / |V_us|^2")
    print(f"  Difference: {diff_alt}")
    check("C2 alt: (|V_td V_us|/|V_cb V_ub|)^2 = N_pair N_color (N_quark - 1) R_bar^2 / |V_us|^2",
          diff_alt == 0)


def audit_c3_pdg_comparison(N: dict, S: dict) -> None:
    banner("C3: historical central-value diagnostics; no covariance or theory budget")

    a_s = S["a_s"]
    Vtd_sq = S["Vtd_sq"]
    Vus_sq = S["Vus_sq"]
    Vcb_sq = S["Vcb_sq"]
    Vub_sq = S["Vub_sq"]
    R_bar_sq = S["R_bar_sq"]

    s_canonical = 0.103

    # Three-magnitude bridge.
    Vtd_pred = math.sqrt(float(Vtd_sq.subs(a_s, s_canonical)))
    Vus_pred = math.sqrt(float(Vus_sq.subs(a_s, s_canonical)))
    Vcb_pred = math.sqrt(float(Vcb_sq.subs(a_s, s_canonical)))
    Vub_pred = math.sqrt(float(Vub_sq.subs(a_s, s_canonical)))
    R_bar_pred = math.sqrt(float(R_bar_sq.subs(a_s, s_canonical)))

    # Verify: 3 |V_td|^2 = 10 |V_us|^2 |V_cb|^2 R_bar^2 numerically.
    lhs_C1 = 3 * Vtd_pred ** 2
    rhs_C1 = 10 * Vus_pred ** 2 * Vcb_pred ** 2 * R_bar_pred ** 2

    print(f"  At canonical alpha_s = {s_canonical}:")
    print(f"    |V_td| = {Vtd_pred:.6f}, |V_us| = {Vus_pred:.6f}")
    print(f"    |V_cb| = {Vcb_pred:.6f}, |V_ub| = {Vub_pred:.6f}")
    print(f"    R_bar  = {R_bar_pred:.6f}, R_bar^2 = {R_bar_pred ** 2:.6f}")
    print()
    print(f"  C1 check: 3 |V_td|^2 vs 10 |V_us|^2 |V_cb|^2 R_bar^2:")
    print(f"    LHS = 3 |V_td|^2                       = {lhs_C1:.10f}")
    print(f"    RHS = 10 |V_us|^2 |V_cb|^2 R_bar^2     = {rhs_C1:.10f}")
    check("C1 numerical: 3 |V_td|^2 = 10 |V_us|^2 |V_cb|^2 R_bar^2 within absolute 1e-10",
          abs(lhs_C1 - rhs_C1) < 1e-10)

    # PDG values (central):
    pdg = {"|V_us|": 0.2243, "|V_cb|": 0.0410, "|V_ub|": 0.00382, "|V_td|": 0.00861}

    pdg_lhs_C1 = 3 * pdg["|V_td|"] ** 2
    # For PDG, R_bar isn't directly measured, so use framework's R_bar at canonical alpha_s.
    pdg_rhs_C1 = 10 * pdg["|V_us|"] ** 2 * pdg["|V_cb|"] ** 2 * R_bar_pred ** 2
    rel_diff = abs(pdg_lhs_C1 - pdg_rhs_C1) / pdg_lhs_C1 * 100

    print(f"\n  C1 PDG check (with framework R_bar):")
    print(f"    LHS_PDG = 3 |V_td|_PDG^2          = {pdg_lhs_C1:.10f}")
    print(f"    RHS_PDG = 10 |V_us|_PDG^2 |V_cb|_PDG^2 R_bar^2  =  {pdg_rhs_C1:.10f}")
    print(f"    |Delta/LHS| = {rel_diff:.2f} %")
    print("  Hybrid model-radius/data comparison only; no combined PDG error was supplied.")

    # Four-magnitude compound.
    compound_sq_pred = float((Vtd_sq * Vus_sq / (Vcb_sq * Vub_sq)).subs(a_s, s_canonical))
    pdg_compound_sq = (pdg["|V_td|"] * pdg["|V_us|"]) ** 2 / (pdg["|V_cb|"] * pdg["|V_ub|"]) ** 2
    rel_diff_C2 = abs(compound_sq_pred - pdg_compound_sq) / pdg_compound_sq * 100

    print(f"\n  C2 PDG check: (|V_td V_us|/|V_cb V_ub|)^2:")
    print(f"    Framework = {compound_sq_pred:.4f}")
    print(f"    PDG       = {pdg_compound_sq:.4f}")
    print(f"    |Delta/PDG| = {rel_diff_C2:.2f} %")
    print("  Descriptive central-value comparison only, not a statistical validation.")


def audit_summary() -> None:
    banner("Conditional supplied identities, no retained-status conclusion")
    print("  C1: 3 Vtd² = 10 Vus² Vcb² Rbar².")
    print("  C2: Vtd² Vus²/(Vcb² Vub²) = 60 Rbar²/alpha_s = 30 Rbar²/Vus².")
    print("  Inputs mix leading unbarred Vub with a barred-apex Vtd formula.")
    print("  Exact symbolic equality within this supplied model is not an all-orders CKM result.")
    print("  Historical comparisons use alpha_s=.103 and a model radius, without covariance.")


def main() -> int:
    print("=" * 88)
    print("CKM compound-magnitudes circumradius bridge audit")
    print("See docs/CKM_COMPOUND_MAGNITUDES_CIRCUMRADIUS_BRIDGE_THEOREM_NOTE_2026-04-25.md")
    print("=" * 88)

    audit_inputs()
    N = extract_retained_inputs()
    S = setup_symbolic(N)
    audit_c1_three_magnitude_bridge(N, S)
    audit_c2_four_magnitude_bridge(N, S)
    audit_c3_pdg_comparison(N, S)
    audit_summary()

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
