#!/usr/bin/env python3
"""Assembly-consistency runner for the color-derivation campaign brief.

Audits the six sibling block notes when present (post-landing) and reports
pending-landing skips when absent (pre-landing). Also audits the brief's own
quotes against the June-5 residual map, and self-scans for side effects.
"""

import ast
import sys
from pathlib import Path

POST_LANDING = "--post-landing" in sys.argv

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS = 0
FAIL = 0
SKIP = 0


def report(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"{tag} {label}" + (f" :: {detail}" if detail else ""))


def skip(label, detail=""):
    global SKIP
    SKIP += 1
    print(f"[SKIP] {label}" + (f" :: {detail}" if detail else ""))


def normalize(text):
    return " ".join(text.split())


BLOCKS = {
    "block02": (
        "COLOR_ARENA_BONDED_PAIR_ADMISSIBILITY_CROSS_SITE_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-06.md",
        "color_arena_bonded_pair_admissibility_cross_site_2026_07_06.txt",
        ["Citation contract", "R5"],
    ),
    "block03": (
        "COLOR_SINGLET_RECORDS_G2_FACTORIZATION_SITE_LOCAL_LOCKING_BOUNDED_THEOREM_NOTE_2026-07-06.md",
        "color_singlet_records_g2_factorization_site_local_locking_2026_07_06.txt",
        ["MARGINAL-READ", "FERMI-FILL", "Citation contract"],
    ),
    "block04": (
        "GAUGE_FACTOR_PRESERVATION_RECORD_TYPED_SELECTOR_CONDITIONAL_DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-07-06.md",
        "gauge_factor_preservation_record_typed_selector_2026_07_06.txt",
        ["REGISTERED-FACTOR", "Citation contract"],
    ),
    "block05": (
        "COLOR_COMPOSITION_RULE_MATTER_BILINEAR_POLAR_TRANSPORT_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md",
        "color_composition_rule_matter_bilinear_polar_transport_2026_07_06.txt",
        ["SUPPLIED-C3", "SUPPLIED-BILINEAR", "Citation contract"],
    ),
    "block06": (
        "COLOR_ORIENTATION_THREE_VS_THREEBAR_SUCCESSION_CANDIDATE_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md",
        "color_orientation_three_vs_threebar_succession_candidate_2026_07_06.txt",
        ["ARROW", "SUCCESSION-ORIENT", "Citation contract"],
    ),
    "block01": (
        "COLOR_COMP_HURWITZ_CLAUSE_SCOPE_REDUCTION_NARROW_THEOREM_NOTE_2026-07-06.md",
        "color_comp_hurwitz_clause_scope_reduction_2026_07_06.txt",
        ["Citation contract", "Hurwitz"],
    ),
}


def main():
    residual_map = DOCS / "COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md"
    text = normalize(residual_map.read_text(encoding="utf-8"))
    mr_needles = [
        "quark matter occupies the 3D symmetric-base fundamental Sym^2(C^2),",
        "A future matter-sector theorem could assign quark fields to",
    ]
    report(
        "june5_residual_map_quotes_present",
        all(normalize(n) in text for n in mr_needles),
    )

    brief = DOCS / "COLOR_DERIVATION_CAMPAIGN_20260706_ASSEMBLY_AND_HONEST_REBOUNDING_META_NOTE_2026-07-06.md"
    brief_text = brief.read_text(encoding="utf-8")
    ledger_premises = [
        "SUPPLIED-C3",
        "MARGINAL-READ",
        "WEIGHT-UNIFORMITY",
        "FERMI-FILL",
        "REGISTERED-FACTOR",
        "SUPPLIED-BILINEAR",
        "ARROW",
        "SUCCESSION-ORIENT",
    ]
    report(
        "brief_premise_ledger_lists_all_eight",
        all(p in brief_text for p in ledger_premises),
        "eight named premises",
    )
    report(
        "brief_verdict_states_not_derived_and_count_zero",
        "NOT derived" in brief_text and "count stays 0" in brief_text,
    )

    for key, (note_name, cache_name, needles) in sorted(BLOCKS.items()):
        note_path = DOCS / note_name
        cache_path = ROOT / "logs" / "runner-cache" / cache_name
        if not note_path.exists():
            if POST_LANDING:
                report(f"{key}_note_present", False, f"MISSING at landing: {note_name}")
            else:
                skip(f"{key}_note_pending_landing", note_name)
            continue
        note_text = note_path.read_text(encoding="utf-8")
        ok = all(n in note_text for n in needles if n)
        report(f"{key}_note_present_with_expected_needles", ok, note_name)
        if cache_path.exists():
            cache_lines = [
                ln for ln in cache_path.read_text(encoding="utf-8").splitlines() if ln.strip()
            ]
            # Anchor to the FINAL summary line, not any substring in the body.
            final = cache_lines[-1] if cache_lines else ""
            summary = next(
                (ln for ln in reversed(cache_lines) if ln.startswith("TOTAL")), final
            )
            report(
                f"{key}_cache_final_summary_zero_fail",
                ("FAIL=0" in summary) or ("/ 0 FAIL" in summary),
                f"{cache_name} :: {summary[:60]}",
            )
        else:
            if POST_LANDING:
                report(f"{key}_cache_present", False, f"MISSING at landing: {cache_name}")
            else:
                skip(f"{key}_cache_pending_landing", cache_name)

    # AST self-scan: no writes, no network/subprocess imports.
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    bad_imports = []
    bad_opens = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] in {"socket", "subprocess", "requests", "urllib", "http"}:
                    bad_imports.append(alias.name)
        if isinstance(node, ast.ImportFrom) and node.module:
            if node.module.split(".")[0] in {"socket", "subprocess", "requests", "urllib", "http"}:
                bad_imports.append(node.module)
        if isinstance(node, ast.Call):
            func = node.func
            name = getattr(func, "id", None) or getattr(func, "attr", None)
            if name == "open":
                mode_vals = [
                    a.value for a in node.args[1:2]
                    if isinstance(a, ast.Constant) and isinstance(a.value, str)
                ] + [
                    kw.value.value for kw in node.keywords
                    if kw.arg == "mode" and isinstance(kw.value, ast.Constant)
                ]
                if any(any(ch in str(m) for ch in "wax+") for m in mode_vals):
                    bad_opens += 1
    report("ast_self_scan_no_writes_no_network", not bad_imports and bad_opens == 0)

    if POST_LANDING:
        print("MODE: post-landing (landing invariant; absences are failures)")
    else:
        print(
            "MODE: pre-landing -- THIS RUN IS NOT A LANDING VALIDATION; "
            "skips mark pending sibling landings"
        )
    print(
        "DECLARATION meta adjudication brief consistency only; no audit "
        "verdicts applied"
    )
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL / {SKIP} SKIP")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
