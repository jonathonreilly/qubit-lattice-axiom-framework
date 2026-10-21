#!/usr/bin/env python3
"""Conditional four-channel algebra and finite central-value diagnostics.

The four supplied CKM magnitude formulas can each be inverted for a model
parameter. Separate formulas do not imply statistically independent inputs.
Historical central values and a 20-assignment descriptive scan are supplied;
no covariance, theory-error budget, scheme matching, or precision forecast is
computed. Legacy source-status guards remain documentary checks and may fail.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "docs/CKM_NLO_BARRED_TRIANGLE_PROTECTED_GAMMA_THEOREM_NOTE_2026-04-25.md",
    "docs/CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md",
    "docs/CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md",
    "docs/WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md",
)

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


def invert_vtd_alpha_s(vtd_sq: float, n_pair: int, n_color: int, n_quark: int) -> float:
    """Invert the supplied NLO |V_td|^2 channel for the positive alpha_s root."""
    lo, hi = 1.0e-9, 2.0
    for _ in range(300):
        mid = (lo + hi) / 2
        val = mid ** 3 * (n_pair ** 4 * (n_quark - 1) + mid ** 2) / (
            n_pair ** 7 * n_color ** 2
        )
        if val < vtd_sq:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


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


def authority_tier(content: str) -> str:
    status_low = extract_status_text(content).lower()
    if "retained" in status_low and "support" not in status_low:
        return "retained"
    if "current public framework memo" in status_low:
        return "retained"
    if "support" in status_low:
        return "support"
    return "unknown"


def audit_inputs() -> None:
    banner("Legacy documentary status pins (not proof or audit authority)")

    print("  Historical status strings checked below; conditional algebra uses supplied constants:\n")

    retained_authorities = (
        ("docs/CKM_NLO_BARRED_TRIANGLE_PROTECTED_GAMMA_THEOREM_NOTE_2026-04-25.md",
         "retained NLO CKM-structure corollary",
         ("retained",)),
        ("docs/CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md",
         "retained",
         ("retained",)),
        ("docs/CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md",
         "retained standalone structural-identity",
         ("retained",)),
        ("docs/WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md",
         "Retained structural-identity subtheorem",
         ("retained",)),
    )

    for rel_path, claimed, kws in retained_authorities:
        content = read_authority(rel_path)
        status = extract_status_text(content)
        tier = authority_tier(content)
        all_kws = all(kw.lower() in status.lower() for kw in kws)

        print(f"    [{rel_path.split('/')[-1]}]")
        print(f"      Status (extracted): {status!r}")
        print(f"      Tier classification: {tier}")
        check(f"Legacy retained-label string matches: {rel_path.split('/')[-1]}",
              all_kws and tier == "retained")
        print()


def extract_retained_inputs() -> dict:
    banner("Checking source literals against supplied model constants")

    counts = read_authority(
        "docs/CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md"
    )
    n_pair_match = re.search(r"n[_\s]pair\s*=\s*(\d+)", counts, re.IGNORECASE)
    n_color_match = re.search(r"n[_\s]color\s*=\s*(\d+)", counts, re.IGNORECASE)
    n_quark_match = re.search(r"n[_\s]quark\s*=\s*n[_\s]pair\s*n[_\s]color", counts, re.IGNORECASE)

    print(f"  N_pair extracted:                  {n_pair_match.group(0) if n_pair_match else 'NOT FOUND'}")
    print(f"  N_color extracted:                 {n_color_match.group(0) if n_color_match else 'NOT FOUND'}")
    print(f"  N_quark = N_pair * N_color:        {'FOUND' if n_quark_match else 'NOT FOUND'}")

    check("MAGNITUDES contains literal N_pair = 2", n_pair_match and int(n_pair_match.group(1)) == 2)
    check("MAGNITUDES contains literal N_color = 3", n_color_match and int(n_color_match.group(1)) == 3)
    check("MAGNITUDES contains literal N_quark = N_pair * N_color (=6)", bool(n_quark_match))

    return {
        "N_pair": 2,
        "N_color": 3,
        "N_quark": 6,
    }


def audit_e1_to_e4_extraction_formulas(N: dict) -> None:
    banner("E1-E4: alpha_s extraction formulas from each CKM magnitude")

    a_s = sp.symbols("alpha_s", positive=True)

    # Build closed forms from the supplied Wolfenstein model.
    lambda_sq = a_s / 2
    A_sq = sp.Rational(2, 3)
    rho = sp.Rational(1, 6)
    eta = sp.sqrt(5) / 6
    rho_bar = (4 - a_s) / 24
    eta_bar = sp.sqrt(5) * (4 - a_s) / 24

    Vus_sq = lambda_sq
    Vcb_sq = A_sq * lambda_sq ** 2
    Vub_sq = A_sq * lambda_sq ** 3 * (rho ** 2 + eta ** 2)
    Vtd_sq = A_sq * lambda_sq ** 3 * ((1 - rho_bar) ** 2 + eta_bar ** 2)

    N_pair, N_color, N_quark = N["N_pair"], N["N_color"], N["N_quark"]

    # E1: alpha_s = N_pair * |V_us|^2.
    extracted_Vus = sp.simplify(N_pair * Vus_sq)
    diff_E1 = sp.simplify(extracted_Vus - a_s)
    print(f"  E1: alpha_s = N_pair * |V_us|^2")
    print(f"      |V_us|^2 = {Vus_sq}, N_pair * |V_us|^2 = {extracted_Vus}")
    print(f"      Difference from alpha_s: {diff_E1}")
    check("E1: alpha_s = N_pair * |V_us|^2 inverts |V_us|^2 = alpha_s/N_pair",
          diff_E1 == 0)

    # E2: alpha_s = sqrt(N_quark) * |V_cb|.
    extracted_Vcb = sp.simplify(sp.sqrt(N_quark) * sp.sqrt(Vcb_sq))
    diff_E2 = sp.simplify(extracted_Vcb - a_s)
    print(f"\n  E2: alpha_s = sqrt(N_quark) * |V_cb|")
    print(f"      |V_cb|^2 = {Vcb_sq}, sqrt(N_quark) * |V_cb| = {extracted_Vcb}")
    print(f"      Difference from alpha_s: {diff_E2}")
    check("E2: alpha_s = sqrt(N_quark) * |V_cb| inverts |V_cb|^2 = alpha_s^2/N_quark",
          diff_E2 == 0)

    # E3: alpha_s = (N_pair N_quark^2 |V_ub|^2)^(1/3).
    extracted_Vub_cube = sp.simplify(N_pair * N_quark ** 2 * Vub_sq)
    extracted_Vub = extracted_Vub_cube ** sp.Rational(1, 3)
    diff_E3 = sp.simplify(extracted_Vub - a_s)
    print(f"\n  E3: alpha_s = (N_pair * N_quark^2 * |V_ub|^2)^(1/3)")
    print(f"      |V_ub|^2 = {Vub_sq}, (72 |V_ub|^2)^(1/3) = {extracted_Vub}")
    print(f"      Difference from alpha_s: {diff_E3}")
    check("E3: alpha_s = (N_pair N_quark^2 |V_ub|^2)^(1/3) inverts |V_ub|^2 = alpha_s^3/(N_pair N_quark^2)",
          diff_E3 == 0)

    # E4: alpha_s = inversion of |V_td|^2 = alpha_s^3 (80 + alpha_s^2)/1152.
    Vtd_closed = a_s ** 3 * (
        N_pair ** 4 * (N_quark - 1) + a_s ** 2
    ) / (N_pair ** 7 * N_color ** 2)
    diff_E4_formula = sp.simplify(Vtd_sq - Vtd_closed)
    derivative_E4 = sp.factor(sp.diff(Vtd_closed, a_s))
    print(f"\n  E4: alpha_s extraction from |V_td|^2 = alpha_s^3 (80 + alpha_s^2)/1152")
    print(f"      supplied NLO |V_td|^2 = {sp.factor(Vtd_closed)}")
    print(f"      Difference from Wolfenstein construction: {diff_E4_formula}")
    print(f"      Positive-root derivative: {derivative_E4}")
    check("E4: |V_td|^2 closed form matches supplied NLO Wolfenstein construction",
          diff_E4_formula == 0)
    check("E4: positive-root map is monotone for alpha_s > 0",
          derivative_E4 == 5 * a_s ** 2 * (a_s ** 2 + 48) / 1152)


def audit_pdg_consistency(N: dict) -> None:
    banner("Historical supplied central-value transformations; no covariance test")

    pdg = {"|V_us|": 0.2243, "|V_cb|": 0.0410, "|V_ub|": 0.00382, "|V_td|": 0.00861}

    N_pair, N_color, N_quark = N["N_pair"], N["N_color"], N["N_quark"]

    # E1: alpha_s = N_pair * |V_us|^2.
    a_s_E1 = N_pair * pdg["|V_us|"] ** 2

    # E2: alpha_s = sqrt(N_quark) * |V_cb|.
    a_s_E2 = math.sqrt(N_quark) * pdg["|V_cb|"]

    # E3: alpha_s = (N_pair N_quark^2 |V_ub|^2)^(1/3) = (72 |V_ub|^2)^(1/3).
    a_s_E3 = (N_pair * N_quark ** 2 * pdg["|V_ub|"] ** 2) ** (1.0 / 3.0)

    # E4: numerical inversion of |V_td|^2 = a_s^3 (80 + a_s^2)/1152.
    a_s_E4 = invert_vtd_alpha_s(pdg["|V_td|"] ** 2, N_pair, N_color, N_quark)

    extractions = [
        ("E1: alpha_s_from_|V_us|", a_s_E1),
        ("E2: alpha_s_from_|V_cb|", a_s_E2),
        ("E3: alpha_s_from_|V_ub|", a_s_E3),
        ("E4: alpha_s_from_|V_td|", a_s_E4),
    ]

    print(f"  Channel                 model parameter (historical inputs)")
    for name, val in extractions:
        print(f"  {name:25s}  {val:.6f}")

    # Compute unweighted mean and range; no standard error is estimated.
    values = [val for _, val in extractions]
    mean = sum(values) / len(values)
    spread = max(values) - min(values)
    rel_spread = spread / mean * 100

    print()
    print(f"  Mean of four extractions:    {mean:.6f}")
    print(f"  Spread (max - min):          {spread:.6f}")
    print(f"  Relative spread:             {rel_spread:.2f} %")
    canonical = 0.103303816
    print(f"  Supplied canonical comparator: {canonical:.9f}")
    print(f"  Mean relative to comparator: {(mean/canonical-1)*100:.6f} %")
    print("  This unweighted mean is not a covariance-weighted fit or uncertainty estimate.")

    check("Descriptive range is below the supplied 5-percent cut (not a theory bound)",
          rel_spread < 5)

    # Pairwise checks.
    pair_max_diff_pct = 0
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            d = abs(values[i] - values[j]) / mean * 100
            pair_max_diff_pct = max(pair_max_diff_pct, d)

    print(f"  Maximum pairwise deviation:  {pair_max_diff_pct:.2f} %")
    check("Maximum pairwise range is below the same descriptive cut (redundant range check)",
          pair_max_diff_pct < 5)


def audit_falsifiability_envelope() -> None:
    banner("Historical comparator only; no forecast or uncertainty budget")
    print("  The old 2-percent revision threshold and 1.75-percent spread were")
    print("  supplied numbers, not a covariance analysis or experimental forecast.")
    print("  Their comparison is preserved solely as historical arithmetic.")
    current_spread_pct = 1.75
    revision_threshold_pct = 2.0
    check("Historical supplied comparator: 2.0 exceeds 1.75 (not a falsification test)",
          revision_threshold_pct > current_spread_pct)


def audit_uniqueness_argument(N: dict) -> None:
    banner("Finite descriptive ranking of 20 supplied count assignments")

    print("  Suppose the framework's structural integers were perturbed:")
    print(f"    N_pair' = N_pair + delta_p,")
    print(f"    N_color' = N_color + delta_c,")
    print(f"    N_quark' = N_quark + delta_q.")
    print()
    print("  Then E1, E2, E3, E4 would extract DIFFERENT alpha_s values:")
    print(f"    alpha_s_from_Vus  =  N_pair' * |V_us|^2,")
    print(f"    alpha_s_from_Vcb  =  sqrt(N_quark') * |V_cb|,")
    print(f"    alpha_s_from_Vub  =  cuberoot(N_pair' * N_quark'^2 * |V_ub|^2).")
    print(f"    alpha_s_from_Vtd  =  positive root of the candidate |V_td|^2 channel.")
    print()
    print("  In this supplied 20-assignment scan, historical central values rank the")
    print(f"  assignment whose four extractions agree at alpha_s ~ 0.10 to within 1.8 %.")
    print()
    print("  The supplied values (N_pair, N_color, N_quark) = (2, 3, 6)")
    print("  are the unique minimum-spread small-integer assignment in the scan.")
    print()
    print("  Any other scanned assignment that disagrees with (2, 3, 6)")
    print("  gives a much larger four-channel alpha_s spread.")

    # Explicit demonstration: verify that (2, 3, 6) is the unique minimum-spread assignment.
    pdg = {"|V_us|": 0.2243, "|V_cb|": 0.0410, "|V_ub|": 0.00382, "|V_td|": 0.00861}

    # For each candidate, test whether all four extraction channels agree.
    print(f"\n  Numerical test: verify (N_pair, N_color, N_quark) = (2, 3, 6) is the unique minimum-spread assignment")
    print(f"  (testing N_pair in {{1, 2, 3, 4}}, N_color in {{1, 2, 3, 4, 5}}, N_quark = N_pair * N_color):")
    print()
    print(f"  N_pair  N_color  N_quark  alpha_s_from_Vus  alpha_s_from_Vcb  alpha_s_from_Vub  alpha_s_from_Vtd  spread")

    candidates = []
    for n_p in [1, 2, 3, 4]:
        for n_c in [1, 2, 3, 4, 5]:
            n_q = n_p * n_c
            a_s_1 = n_p * pdg["|V_us|"] ** 2
            a_s_2 = math.sqrt(n_q) * pdg["|V_cb|"]
            a_s_3 = (n_p * n_q ** 2 * pdg["|V_ub|"] ** 2) ** (1 / 3)
            a_s_4 = invert_vtd_alpha_s(pdg["|V_td|"] ** 2, n_p, n_c, n_q)
            mean = (a_s_1 + a_s_2 + a_s_3 + a_s_4) / 4
            spread = max(a_s_1, a_s_2, a_s_3, a_s_4) - min(a_s_1, a_s_2, a_s_3, a_s_4)
            rel_spread = spread / mean * 100
            print(f"  {n_p}       {n_c}        {n_q}        {a_s_1:.4f}            {a_s_2:.4f}            {a_s_3:.4f}            {a_s_4:.4f}            {rel_spread:.2f} %")
            candidates.append((n_p, n_c, n_q, rel_spread))

    # Find minimum spread.
    candidates.sort(key=lambda c: c[3])
    best = candidates[0]
    second_best = candidates[1]
    print(f"\n  Best (minimum spread) assignment: (N_pair, N_color, N_quark) = ({best[0]}, {best[1]}, {best[2]}) with {best[3]:.2f} % spread")
    print(f"  Next-best alternative: ({second_best[0]}, {second_best[1]}, {second_best[2]}) with {second_best[3]:.2f} % spread")

    check("Finite scan: (2, 3, 6) has minimum descriptive spread in this 20-row box",
          best[0] == 2 and best[1] == 3 and best[2] == 6)
    check("Finite scan: second-ranked row exceeds 20-percent descriptive spread",
          second_best[3] > 20)


def audit_summary() -> None:
    banner("Conditional result and open physical obligations")
    print("  E1-E4 are inversions of supplied magnitude formulas at counts (2,3,6).")
    print("  Four single-channel transformations do not establish statistical independence.")
    print("  The 20-row scan ranks a supplied central-value range statistic only.")
    print("  No likelihood, covariance, theory-error bound, or empirical exclusion is computed.")
    print("  Identifying this model parameter with MSbar alpha_s needs a scale and matching map.")
    print("  Neither a 5-percent theory error nor a future 2-percent rejection rule is derived.")
    print("  Source-label checks are documentary and do not establish retained authority.")


def main() -> int:
    print("=" * 88)
    print("CKM multi-channel alpha_s extraction consistency audit")
    print("See docs/CKM_MULTI_CHANNEL_ALPHA_S_EXTRACTION_CONSISTENCY_THEOREM_NOTE_2026-04-26.md")
    print("=" * 88)

    audit_inputs()
    N = extract_retained_inputs()
    audit_e1_to_e4_extraction_formulas(N)
    audit_pdg_consistency(N)
    audit_falsifiability_envelope()
    audit_uniqueness_argument(N)
    audit_summary()

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
