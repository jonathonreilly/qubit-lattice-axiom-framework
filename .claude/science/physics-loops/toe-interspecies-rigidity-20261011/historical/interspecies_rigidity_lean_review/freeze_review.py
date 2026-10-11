"""Freeze the independent statement review without invoking the Lean runtime."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

D = Path(__file__).resolve().parent
S = D.parent
P = S / "interspecies_rigidity_lean"
out = D / "receipt.json"
assert not out.exists(), "Preserve frozen review receipts"
verification = json.loads((D / "source_verification.json").read_text())
assert verification["all_match"]


def identity(path, role):
    path = Path(path)
    raw = path.read_bytes()
    return {"path": str(path), "sha256": hashlib.sha256(raw).hexdigest(),
            "bytes": len(raw), "role": role}


sources = []
for rec in verification["source_records"]:
    current = identity(rec["path"], rec["group"])
    assert current["sha256"] == rec["expected_sha256"]
    sources.append(current)
runtime = S / "lean_audit/lean-4.35.0-rc4-darwin_aarch64"
commands = []
for item in verification["execution_history"]:
    execution = item["execution"]
    source = Path(execution["command"][5])
    expected = [str(runtime / "bin/lake"), "env", "lean", "-R", str(P), str(source),
                "-o", str(P / (source.stem + ".olean"))]
    assert execution["command"] == expected and source.parent == P
    assert execution["cwd"] == str(S / "lean_audit/mathlib")
    assert execution["path_prepend"] == str(runtime / "bin")
    assert all(Path(v).is_relative_to(P) for v in execution["environment_overrides"].values())
    commands.append({"label": item["label"], "command_and_local_paths_match": True,
                     "exit": execution["exit"], "timeout_seconds": execution["timeout_seconds"]})
report = identity(S / "LEAN_RIGIDITY_STATEMENT_REVIEW.md", "final independent statement review")
artifacts = [report] + [identity(p, "review evidence or checkpoint")
                       for p in sorted(D.iterdir()) if p.is_file() and p != out]
receipt = {
    "schema": "scoped-lean-independent-statement-review-v1",
    "frozen_utc": datetime.now(timezone.utc).isoformat(),
    "principal_sha256": "c72e7a9a961d1eec1ff60842ac3e8a5530c8b71dfc1505dc098d7cab780044df",
    "author_receipt_sha256": "4f1512919a9e4aa41cac168882d3975e4b95f72cd4620876aa7cc959201c9048",
    "disposition": "No consequential statement mismatch or proof defect found in the six scoped declarations; no source repair requested.",
    "positive_formal_scope": [
        "Four-point affine-independence coefficient adapter.",
        "Four-cross-edge cycle multiplier equality, I9-I10.",
        "Common homothety on the four anchors only.",
        "Opposite-line residual elimination for all explicit line parameters and residual coefficients.",
        "I14 direction exclusion in two-coefficient form.",
        "Disjointness of the two opposite parameterized anchor lines."
    ],
    "excluded_formal_scope": [
        "Anchor extraction and extra-velocity choices from full affine span.",
        "Residual confinement I12-I13, the other Section 4.3 branch, and final propagation to all labels.",
        "Complete I7-I8 geometry theorem or complete I1-I24 analytic theorem.",
        "Shell differentiation, measure upgrade, integration, cubic/current and physical premises."
    ],
    "independence": {"reviewer_authored_Lean_packet": False,
                     "prior_independent_analytic_reconstruction_reused": True,
                     "blind_discovery_claimed": False,
                     "additional_Lean_or_Lake_invocations": 0,
                     "reason_no_replay": "No actual statement concern remained that a focused compiler check needed to resolve."},
    "reading_coverage": {
        "principal": "Complete final 146 lines.",
        "controls": "Complete accepted 91 lines, all four false files, and complete 17-line axiom inventory.",
        "documents_and_runners": "Complete statement map, scope report, scoped obligations, checkpoint, runtime identity, runners and receipt freezer.",
        "logs": "All nine complete compiler logs and four wrapper logs; duplicate aliases verified bytewise.",
        "history": "Historical snapshots compared with fully read final sources; complete changes inspected, including the sole Finset.univ repair.",
        "receipt": "Structured fields and all source bindings inspected; initial oversized display truncation recovered before completion.",
        "original_note": "Unchanged prior complete independent reading reused; full finite-geometry section reread.",
        "upstream_manual_ranges": {"Mathlib/LinearAlgebra/AffineSpace/Independent.lean": ["25-150", "770-840"],
                                    "Mathlib/LinearAlgebra/AffineSpace/Combination.lean": ["220-272", "407-429"],
                                    "Mathlib/Tactic/Module.lean": ["1-75"]},
        "unreviewed_upstream": "No whole transitive dependency rebuild, executable provenance audit, or manual review of every imported proof."
    },
    "evidence": {"principal_theorems": 6, "accepted_control_theorems": 8,
                 "allowed_printed_axioms": ["propext", "Classical.choice", "Quot.sound"],
                 "recorded_compiler_processes": 9, "successful_processes": 4,
                 "preserved_initial_control_failure": 1, "deliberate_false_statement_failures": 4,
                 "source_mutations_of_principal_executed": 0,
                 "commands_checked": commands,
                 "mathlib_commit": verification["mathlib_commit"],
                 "mathlib_tracked_status": verification["mathlib_tracked_status"],
                 "packages": verification["packages"]},
    "sources": sources, "artifacts": artifacts,
    "counts": {"source_records": len(sources), "review_artifacts": len(artifacts)},
    "no_installation_or_dependency_change": True,
    "no_authored_source_historical_file_worktree_prior_review_or_prompt_edit": True,
    "no_audit_or_retained_status_decision": True,
    "receipt_self_hash": "Excluded to avoid self-reference; communicated separately."
}
out.write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps({"report": report, "receipt": identity(out, "final source-bound receipt"),
                  "counts": receipt["counts"]}, indent=2))
