"""Freeze a source-bound review receipt after full report/evidence inspection."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

D = Path(__file__).resolve().parent
S = D.parent
output = D / "receipt.json"
assert not output.exists(), "Never replace a frozen receipt"
verification = json.loads((D / "source_verification.json").read_text())
assert verification["all_match"]
pre = json.loads((D / "pre_helper_receipt.json").read_text())
author = json.loads((S / "interspecies_current_rigidity/receipt.json").read_text())


def record(path, roles):
    path = Path(path)
    raw = path.read_bytes()
    return {"path": str(path), "sha256": hashlib.sha256(raw).hexdigest(),
            "bytes": len(raw), "logical_lines": len(raw.splitlines()), "roles": roles}


bindings = {}
for group, rows in verification["groups"].items():
    if group == "frozen_pre_helper_reconstruction":
        continue
    for row in rows:
        entry = bindings.setdefault(row["path"], {"expected": row["expected_sha256"], "roles": []})
        assert entry["expected"] == row["expected_sha256"]
        entry["roles"].append(group)
sources = []
for path in sorted(bindings):
    r = record(path, sorted(set(bindings[path]["roles"])))
    assert r["sha256"] == bindings[path]["expected"], "A source changed before final freezing"
    sources.append(r)
artifacts = [record(S / "INTERSPECIES_CURRENT_RIGIDITY_REVIEW.md", ["final independent bounded review"])]
artifacts += [record(p, ["complete review evidence or checkpoint"])
              for p in sorted(D.iterdir()) if p.is_file() and p != output]
execution = json.loads((D / "independent_execution.json").read_text())
receipt = {
    "schema": "bounded-independent-review-receipt-v1",
    "frozen_utc": datetime.now(timezone.utc).isoformat(),
    "target": {"path": str(S / "INTERSPECIES_CURRENT_RIGIDITY_PROBE.md"),
               "sha256": "ca44d1c852e6cd0437cf9e98913fb5fb106abb1b42567c68fb6bf3e9a60c80b8",
               "labels": "I1-I24"},
    "disposition": "No consequential mathematical defect found under the explicit hypotheses; no source repair requested.",
    "independence": {
        "reviewer_authored_target": False,
        "analytic_reconstruction_before_author_helper": True,
        "independent_fixture_and_run_before_author_helper": True,
        "target_proof_and_expected_finite_case_outcomes_visible": True,
        "blind_discovery_claimed": False,
        "distinct_fixture": "Symbolic K2,2 multipliers and all-parameter skew-line determinants; actual unequal-mass continuum AB collisions with general quadratic scalar charges; current-selection and beta-sign witnesses.",
    },
    "reading_coverage": {
        "target": "All 559 lines, including every I1-I24 argument and evidence prose.",
        "C1_report": "All 266 lines.",
        "C1_short_referee": "All 21 logical lines, no final newline.",
        "C1_full_referee": "All 23 long lines; separately re-displayed in full after reconstruction.",
        "author_evidence": "Complete 209-line helper, full log, execution metadata, receipt, development log, checkpoint, bounded search log, source checks.",
        "new_review_evidence": "Complete analytic reconstruction, independent helper and runner, full independent log/metadata, final report and checkpoint inspected.",
        "truncated_displays": "Recovered in bounded reads; truncated displays were not treated as completed inspection.",
        "historical_other_C1_claims": "Read as context, not recertified.",
        "author_C1_helpers": "Neither opened nor replayed.",
        "instructions": "Applicable complete prior readings reused at unchanged identities; no platform instruction or editable prompt changes."
    },
    "controls": {
        "independent_checks": 15, "independent_formal_run_count": 1,
        "failed_independent_formal_runs": 0, "source_mutant_processes": 0,
        "execution": execution,
        "author_helper_replayed": False,
        "author_evidence_status": "Inspected consistency evidence only; eight exact rational matrix cases plus additional checks.",
        "limits": "Exact controls test specified geometry and a quadratic-charge ansatz; they do not prove the unrestricted C1 theorem or a physical measure/selection rule."
    },
    "source_counts": {"distinct_frozen_input_paths": len(sources),
                      "group_record_counts": verification["group_record_counts"],
                      "exact_C1_git_blobs": 3, "review_artifacts": len(artifacts)},
    "exact_C1_git_blobs": verification["exact_c1_git_blobs"],
    "open_application_obligations": [
        "Match individual scalar bands and connected open regular domains; justify full affine spans or the checked cubic-domain alternatives.",
        "Supply the actual full-support regular joint collision measure and nonzero-amplitude additive-conservation selection rule.",
        "Identify the actual current as E_s grad E_s with required regularity and componentwise conservation.",
        "Supply any positive-curvature/minimum or excluded-set extension premise needed for stronger conclusions."
    ],
    "no_native_law_or_physical_measure_verified": True,
    "no_audit_or_retained_status_adoption": True,
    "no_repository_authored_source_prior_composition_or_prompt_edits": True,
    "sources": sources, "artifacts": artifacts,
    "receipt_self_hash": "Excluded to avoid self-reference; communicated separately."
}
output.write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps({"receipt": record(output, ["final source-bound receipt"]),
                  "review": artifacts[0], "counts": receipt["source_counts"]}, indent=2))
