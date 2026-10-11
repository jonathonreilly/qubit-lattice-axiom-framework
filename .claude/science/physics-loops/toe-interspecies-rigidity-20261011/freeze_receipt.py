"""Bind the external publication composition and actual execution evidence."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import subprocess
import sys

D = Path(__file__).resolve().parent
S = D.parent


def sha(b):
    return hashlib.sha256(b).hexdigest()


def rec(p, role):
    b = p.read_bytes()
    return {"path": str(p), "relative_to_S": str(p.relative_to(S)),
            "sha256": sha(b), "bytes": len(b), "role": role}


manifest = json.loads((D / "SOURCE_COMPOSITION.json").read_text())
binding = json.loads((D / "source_binding_verification.json").read_text())
for item in binding["records"]:
    assert sha(Path(item["path"]).read_bytes()) == item["sha256"]
for item in binding["protected_guards"]:
    assert sha(Path(item["path"]).read_bytes()) == item["sha256"]

original = (S / "INTERSPECIES_CURRENT_RIGIDITY_PROBE.md").read_bytes()
note = (S / manifest["outputs"][0]["name"]).read_bytes()
helper = (S / "interspecies_current_rigidity/rigidity_controls.py").read_bytes()
primary = (S / manifest["outputs"][1]["name"]).read_bytes()
for output, raw in zip(manifest["outputs"], [note, primary]):
    assert sha(raw) == output["sha256"]
proof_part = manifest["outputs"][0]["parts"][1]
lo, hi = proof_part["output_byte_range_half_open"]
assert note[lo:hi] == b"".join(original.splitlines(keepends=True)[56:513])
body_part = manifest["outputs"][1]["parts"][1]
lo, hi = body_part["output_byte_range_half_open"]
assert primary[lo:hi] == b"".join(helper.splitlines(keepends=True)[8:])
labels = {}
for i in range(1, 25):
    tag = ("tag{I" + str(i) + "}").encode()
    assert original.count(tag) == note.count(tag) == 1
    labels[f"I{i}"] = 1

old_log = (S / "interspecies_current_rigidity/controls.log").read_bytes()
new_log = (D / "primary.log").read_bytes()
assert new_log == old_log + b"TOTAL: PASS=13 FAIL=0\n"
execution = json.loads((D / "primary_execution.json").read_text())
assert execution["exit_code"] == 0 and not execution["timed_out"]
assert execution["primary_sha256"] == sha(primary)
assert execution["log_sha256"] == sha(new_log)

# Compare changed evidence-link destinations against the packaged originals.
links = re.findall(rb"\]\(([^)]+)\)", note)
prefix = b"../.claude/science/physics-loops/toe-interspecies-rigidity-20261011/"
relocated = []
for link in links:
    if link.startswith(prefix):
        rel = link[len(prefix):].decode()
        assert (D / rel).is_file(), rel
        relocated.append(rel)
assert len(relocated) == 4

receipt_path = D / "receipt.json"
assert not receipt_path.exists(), "Preserve final receipt rather than overwrite it"
artifacts = [rec(S / output["name"], "final publication candidate")
             for output in manifest["outputs"]]
for p in sorted(D.rglob("*")):
    if p.is_file() and p != receipt_path:
        artifacts.append(rec(p, "publication reconstruction, preserved history or actual execution evidence"))
receipt = {
    "schema": "external-publication-composition-receipt-v1",
    "frozen_utc": datetime.now(timezone.utc).isoformat(),
    "claim_id": manifest["claim_id"],
    "status": "provisional",
    "actual_current_surface_status": "conditional-support",
    "canonical_note": manifest["canonical_note"],
    "canonical_primary": manifest["canonical_primary"],
    "canonical_evidence_root": manifest["canonical_evidence_root"],
    "composition_scope": "Author assembly of unchanged I1-I24 mathematics and complete executable author-helper body; new metadata/evidence presentation only.",
    "independent_mathematical_review": {
        "path": str(S / "INTERSPECIES_CURRENT_RIGIDITY_REVIEW.md"),
        "sha256": "78c3bc3c8f223b988713cb5bd5210c1a801e8cdc5f428ee648d6284c400d97d6",
        "status": "completed selective analytic review of frozen proof, not this publication composition"
    },
    "scoped_Lean_statement_review": {
        "path": str(S / "LEAN_RIGIDITY_STATEMENT_REVIEW.md"),
        "sha256": "14d5a11bf7476975b8067fd5d9c7f9e91381804a1b926fb324ff5b9bfd57b519",
        "status": "completed for six declared finite-geometry statements and preserved author compiler evidence; no review compilation"
    },
    "checks": {
        "proof_fragment_byte_identity": proof_part["raw_fragment_sha256"],
        "helper_body_byte_identity": body_part["raw_fragment_sha256"],
        "all_I1_I24_labels_preserved_once": labels,
        "historical_receipt_records_rehashed": len(binding["records"]),
        "distinct_bound_paths": len({r["path"] for r in binding["records"]}),
        "historical_copies": len(manifest["historical_files"]),
        "compiled_objects_intentionally_omitted": 3,
        "reconstruction": "exit 0; complete log inspected",
        "primary_formal_runs": 1,
        "primary_execution": execution,
        "original_output_prefix_byte_identical": True,
        "relocated_links_bound": relocated,
    },
    "limits": [
        "No new independent science review or Lean execution.",
        "No full theorem formalization or complete upstream-library rebuild/authentication.",
        "No canonical cache, whole-primary semantic mutants, repository conformance, publication or audit performed.",
        "No mathematical dependency on historical C1 or candidate PR9476.",
        "Physical current, conservation, collision measure/selection and domain premises remain application conditions.",
    ],
    "reading_coverage_and_failures": "PACKAGING_REPORT.md",
    "no_repository_or_frozen_source_or_prompt_edits": True,
    "no_runtime_or_installed_dependency_copy": True,
    "no_network_or_subdelegation": True,
    "selected_model_and_effort": "unchanged",
    "artifacts": artifacts,
    "receipt_self_hash": "excluded to avoid self-reference; communicated separately",
}
receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps({
    "receipt": rec(receipt_path, "final external source-composition receipt"),
    "note": artifacts[0], "primary": artifacts[1],
    "source_bindings": len(binding["records"]),
    "distinct_bound_paths": receipt["checks"]["distinct_bound_paths"],
    "recorded_artifacts": len(artifacts),
}, indent=2))
