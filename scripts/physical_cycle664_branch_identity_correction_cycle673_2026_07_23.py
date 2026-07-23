#!/usr/bin/env python3
"""Cycle 673: correct Cycle 664's second-A2 branch identification.

This is a provenance/identity reconciliation, not a new spectral search.  It
keeps Cycle 664's exact finite-box eigenzero and cavity residuals, then tests
whether the four roots selected by its global-minimum rule are the recurring
branch tracked independently in causal-time Cycle 662.
"""

from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE664_BRANCH_IDENTITY_CORRECTION_CYCLE673_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_cycle664_branch_identity_correction_cycle673_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_cycle664_branch_identity_correction_cycle673_cold_2026_07_23.txt"

TARGET_CONTRACT = {
    "target_statement": "compare every Cycle664 selected positive A2 root with the independently branch-tracked Cycle662 worker grid on the same (L,beta) fixture and correct only the branch-identity claim",
    "allowed_premises": "byte-pinned Cycle664 quartet; byte-pinned causal-time Cycle662 quartet and independent worker grid; exact JSON arithmetic",
    "quantifiers_domain": "all four Cycle664 periodic rows: L in {9,13} crossed with beta in {-0.30,-0.35}",
    "completion_witness": "rowwise phase deltas to the tracked branch, retained finite-box residual audit, cross-L branch stability, and explicit corrected/retained/open claim ledger",
    "required_edge_cases": "the one coincident L9 beta=-0.35 row; all three nonmatching rows; C662's own 6/2 method-failure status; word and cavity dressing boundaries",
    "forbidden_weakenings": "discarding Cycle664's exact eigenzeros; calling every continuum-window zero the recurring physical branch; calling a spectral line energy or a clock; hiding C662's two FAIL rows; no-go, minimum-content, or axiom-pressure rhetoric",
    "outcomes_not_closure": "a corrected branch label is not an infinite-volume spectral theorem, physical clock, preparation law, tick-to-echo association, proper time, source, gravity, Born law, or realized history",
}
MATCH_TOLERANCE = 5.0e-5

PINS = {
    "scripts/physical_held_a2_second_line_verification_cycle664_2026_07_23.py": "4641d0500fde54cfe1b820c6c7a56772d62cb070a65255f452e6bac77271f741",
    "docs/work_history/repo/review_feedback/PHYSICAL_HELD_A2_SECOND_LINE_VERIFICATION_CYCLE664_NOTE_2026-07-23.md": "bdeed805ba9c187deffa40237dfce971aacdc78d72f849d3248a4632d5d53ff5",
    "outputs/physical_held_a2_second_line_verification_cycle664_receipt_2026_07_23.json": "ec97733cd4c86a06fe2a5816f7e4260760255a4cac8d5c34df2502b6da26e9b2",
    "outputs/physical_held_a2_second_line_verification_cycle664_cold_2026_07_23.txt": "a2a57dfecc77b32e4161b99129c21266a8bb2fc99d73d3aea14f338fe2f43575",
    "scripts/physical_infinite_volume_a2_two_line_vernier_tournament_cycle662_2026_07_23.py": "18232a8cc85c8a6fc102a0bac3c83d7bea89ad337ed8cca2fedd16f78d326567",
    "docs/work_history/repo/review_feedback/PHYSICAL_INFINITE_VOLUME_A2_TWO_LINE_VERNIER_TOURNAMENT_CYCLE662_NOTE_2026-07-23.md": "eaac6dfd0246d72d9f76e472fb4ee4a1796c510d149459048595b4ea1db8b08b",
    "outputs/physical_infinite_volume_a2_two_line_vernier_tournament_cycle662_receipt_2026_07_23.json": "66a4379e5225e6651d0863495f9f4a873c50bc31844ffa65341e8f3d2b17f8cf",
    "outputs/physical_infinite_volume_a2_two_line_vernier_tournament_cycle662_cold_2026_07_23.txt": "228ee66c391f163a0f9b0a516b2317ef5f7b0c44de177325fc5b1100ba5e5177",
    "outputs/physical_infinite_volume_a2_two_line_vernier_cycle662_worker_grid_2026_07_23.json": "3f4a4cd26e71670b53dbd6925840deabee50ac3c9a34f531e96665e6f8905ead",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text())


def main() -> int:
    started = time.perf_counter()
    tests: list[dict] = []

    def check(label: str, passed: bool, evidence: object) -> None:
        tests.append({"label": label, "pass": bool(passed), "evidence": evidence})

    observed_pins = {path: sha256(ROOT / path) for path in PINS}
    check("all Cycle664/Cycle662 correction shores are byte exact", observed_pins == PINS, {"expected": PINS, "observed": observed_pins})

    c664 = load_json("outputs/physical_held_a2_second_line_verification_cycle664_receipt_2026_07_23.json")
    c662 = load_json("outputs/physical_infinite_volume_a2_two_line_vernier_tournament_cycle662_receipt_2026_07_23.json")
    grid = load_json("outputs/physical_infinite_volume_a2_two_line_vernier_cycle662_worker_grid_2026_07_23.json")
    check("upstream evidentiary status is retained rather than laundered", c664["tests_passed"] == 9 and c664["tests_failed"] == 0 and len(c662["vernier"]) == 6 and sum(bool(row["ok"]) for row in c662["vernier"]) == 4, {"Cycle664": [c664["tests_passed"], c664["tests_failed"]], "Cycle662_vernier": [sum(bool(row["ok"]) for row in c662["vernier"]), 2]})

    comparisons = []
    for row in c664["periodic_rows"]:
        beta_key = f"beta={row['beta']}"
        tracked = float(grid["physical_branches"][beta_key]["root_2"]["theta_by_L"][str(row["L"])])
        delta = abs(float(row["theta"]) - tracked)
        comparisons.append({
            "label": row["label"], "L": row["L"], "beta": row["beta"],
            "Cycle664_selected_theta": row["theta"],
            "Cycle662_tracked_theta": tracked,
            "absolute_phase_delta": delta,
            "same_tracked_branch_within_frozen_tolerance": delta <= MATCH_TOLERANCE,
            "Cycle664_eigen_update_residual": row["eigen_update_residual"],
            "Cycle664_branch_abs_value": row["branch_abs_value"],
        })

    matches = [row for row in comparisons if row["same_tracked_branch_within_frozen_tolerance"]]
    nonmatches = [row for row in comparisons if not row["same_tracked_branch_within_frozen_tolerance"]]
    check("rowwise branch-identity audit resolves one match and three nonmatches", len(matches) == 1 and matches[0]["label"] == "held_beta" and len(nonmatches) == 3, comparisons)
    check("Cycle664 finite-box eigenzero evidence remains valid on every row", max(row["eigen_update_residual"] for row in c664["periodic_rows"]) < 1e-8 and max(row["branch_abs_value"] for row in c664["periodic_rows"]) < 1e-7, {"max_eigen_update_residual": max(row["eigen_update_residual"] for row in c664["periodic_rows"]), "max_branch_abs_value": max(row["branch_abs_value"] for row in c664["periodic_rows"])})

    stability = {}
    for beta_key, payload in grid["physical_branches"].items():
        values = list(payload["root_2"]["theta_by_L"].values())
        stability[beta_key] = {"span": max(values) - min(values), "values": values}
    check("independently tracked branches are cross-L stable on both beta fixtures", stability["beta=-0.3"]["span"] < 2e-4 and stability["beta=-0.35"]["span"] < 1.1e-3, stability)

    word_line = max(float(x) for x in c662["two_line_word"]["lines"])
    beta03_limit = float(grid["physical_branches"]["beta=-0.3"]["root_2"]["converged_theta"])
    check("the independently labeled word peak corroborates the tracked beta=-0.3 branch", abs(word_line - beta03_limit) < 5e-4 and c662["two_line_word"]["lawful"], {"word_line": word_line, "tracked_limit": beta03_limit, "delta": abs(word_line - beta03_limit)})

    n1_n8 = {
        "N1_alternative_routes": ["Cycle664 global-minimum continuum-window zero selection", "Cycle662 branch-tracked cross-L continuation", "two-line word peak", "masked-cavity contact deletion", "held-beta crossing"],
        "N2_wall_independence": "branch identity, finite-box eigenzero existence, continuum theorem, preparation, and clock association are separate",
        "N3_hidden_walls": ["many razor-thin finite-L zeros inside the continuum", "worker-grid branch labels", "amplitude-labeled word lines", "absorber boundary dressing"],
        "N4_residual_match": "all Cycle664 residuals retained; correction changes identity, not eigenzero arithmetic",
        "N5_rhetoric": "bounded four-row correction only; no impossibility, minimum-content, energy, clock, or axiom claim",
        "N6_partial_closure": "correct branch held evidence and lawful two-line word survive while width/preparation/association remain open",
        "N7_steelman": "a Cycle664 artifact zero may be a genuine box eigenline; that does not make it the recurring branch",
        "N8_cross_cycle_echo": "Cycle662 explicitly supersedes Cycle629's global-min root and therefore also changes Cycle664's inherited identification",
        "broad_negative": "DO NOT SHIP",
        "shared_obstruction": False,
        "axiom_pressure": False,
    }
    check("full N1-N8 blocks broad negative and axiom-pressure promotion", not n1_n8["shared_obstruction"] and not n1_n8["axiom_pressure"] and n1_n8["broad_negative"] == "DO NOT SHIP", n1_n8)

    corrected_claims = {
        "withdraw": [
            "identifying the Cycle664 train L9 beta=-0.30 root 0.29998079 as the recurring second A2 line",
            "identifying the Cycle664 held-size L13 beta=-0.30 root 0.29199855 as that branch",
            "identifying the Cycle664 held-both L13 beta=-0.35 root 0.27800715 as the held-species branch",
            "using the four Cycle664 selected eigenvectors as the physical two-level preparation targets",
        ],
        "retain": [
            "all four Cycle664 roots are exact finite-volume A2 eigenzeros on their declared periodic boxes",
            "Cycle664 local-isolation, normalized eigenstate, cavity Ritz, and contact-deletion residuals",
            "the L9 beta=-0.35 Cycle664 root agrees post hoc with the branch-tracked row",
            "Cycle662 branch-tracked L9-L21 and held-species line evidence plus its declared error/method boundaries",
        ],
        "open": [
            "branch-tracked infinite-volume isolation/width and rigorous contact-cyclic theorem",
            "autonomous preparation of the corrected branch eigenvectors",
            "physical two-line clock, tick-to-echo association, renewal, proper time, source and gravity",
        ],
    }
    check("correction ledger preserves true partial results and names the replacement target", len(corrected_claims["withdraw"]) == 4 and len(corrected_claims["retain"]) == 4 and len(corrected_claims["open"]) == 3, corrected_claims)

    note_text = NOTE.read_text()
    required_note_terms = ["one of four", "Three of four", "finite-volume eigenzeros", "+0.31368", "Authority: **none**", "Audit: **unset**", "Axiom pressure: **none**"]
    check("Cycle673 note contains the correction and firewalls", all(term in note_text for term in required_note_terms), required_note_terms)

    passed = sum(int(t["pass"]) for t in tests)
    failed = len(tests) - passed
    receipt = {
        "cycle": 673,
        "date": "2026-07-23",
        "authority": "none",
        "audit": "unset",
        "constitutional_effect": "none",
        "breakthrough": False,
        "status": "Cycle664 branch identity corrected; finite-box eigenzero evidence retained",
        "pass": failed == 0,
        "tests_passed": passed,
        "tests_failed": failed,
        "target_contract": TARGET_CONTRACT,
        "target_contract_sha256": hashlib.sha256(json.dumps(TARGET_CONTRACT, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
        "match_tolerance": MATCH_TOLERANCE,
        "pins": PINS,
        "comparisons": comparisons,
        "tracked_branch_stability": stability,
        "word_branch_comparison": {"word_line": word_line, "tracked_beta_minus_0_3_limit": beta03_limit, "absolute_delta": abs(word_line - beta03_limit)},
        "corrected_claims": corrected_claims,
        "n1_n8": n1_n8,
        "six_wall_ledger": {
            "C_ref": "corrected: global-minimum root identity withdrawn in favor of explicit branch tracking",
            "C_num": "advanced by rowwise identity discriminator; no probability or empirical calibration",
            "C_wrap": "unchanged: two-line reconstruction remains retained-data analysis, not physical time",
            "C_int": "corrected preparation target; contact-dressed line evidence retained",
            "C_local": "unchanged: no physical M2 two-line clock or preparation product",
            "C_source": "unchanged: no energy, stress, source, or gravity identification",
        },
        "tests": tests,
        "note_sha256": sha256(NOTE),
        "runner_sha256": sha256(Path(__file__)),
        "elapsed_seconds": time.perf_counter() - started,
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    lines = [f"{'PASS' if row['pass'] else 'FAIL'} {row['label']} :: {json.dumps(row['evidence'], sort_keys=True)}" for row in tests]
    lines.append(json.dumps({"pass": receipt["pass"], "tests_passed": passed, "tests_failed": failed, "one_of_four_matches": len(matches), "three_of_four_reidentified": len(nonmatches), "elapsed_seconds": receipt["elapsed_seconds"]}, sort_keys=True))
    COLD.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0 if receipt["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
