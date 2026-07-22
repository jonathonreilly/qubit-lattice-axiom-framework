#!/usr/bin/env python3
"""Write or verify the local full-pipeline checkpoint for fast verdict gates.

The checkpoint is a gitignored optimization cache written only by the
successful full branch of ``run_pipeline.sh``. It binds the two skipped-stage
caches to a content fingerprint of every non-verdict repository input. Ledger
shards contribute only source/topology fields, so ordinary audit fields may
change while note, runner, dependency, and criticality drift forces a full run.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
DATA = REPO_ROOT / "docs" / "audit" / "data"
CHECKPOINT = DATA / "static_pipeline_checkpoint.json"
STATIC_CACHE_NAMES = (
    "citation_graph.json",
    "runner_classification.json",
)
VERDICT_GENERATED_PREFIXES = (
    "docs/audit/data/ledger/",
)
VERDICT_GENERATED_PATHS = frozenset({
    "docs/audit/AUDIT_DISPATCH_QUEUE.md",
    "docs/audit/AUDIT_QUEUE.md",
    "docs/audit/data/audit_dispatch_queue.json",
    "docs/audit/data/auditor_reliability.json",
    "docs/audit/data/cycle_inventory.json",
    "docs/audit/data/dispatch_shadow_state.json",
    "docs/audit/data/effective_status_summary.json",
    "docs/audit/data/lane_certification.json",
    "docs/audit/data/ledger_meta.json",
    "docs/audit/data/load_bearing_summary.json",
    "docs/audit/data/reaudit_candidates.json",
    "docs/publication/ci3_z3/CLAIMS_TABLE_EFFECTIVE_STATUS.md",
    "docs/publication/ci3_z3/DERIVATION_ATLAS_EFFECTIVE_STATUS.md",
    "docs/publication/ci3_z3/PUBLICATION_MATRIX_EFFECTIVE_STATUS.md",
    "docs/publication/ci3_z3/FULL_CLAIM_LEDGER_EFFECTIVE_STATUS.md",
    "docs/publication/ci3_z3/USABLE_DERIVED_VALUES_INDEX_EFFECTIVE_STATUS.md",
    "docs/publication/ci3_z3/RESULTS_INDEX_EFFECTIVE_STATUS.md",
    "docs/publication/ci3_z3/QUANTITATIVE_SUMMARY_TABLE_EFFECTIVE_STATUS.md",
    "docs/publication/ci3_z3/DERIVATION_VALIDATION_MAP_EFFECTIVE_STATUS.md",
    "docs/publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md",
    "docs/publication/ci3_z3/ARXIV_DRAFT_EFFECTIVE_STATUS.md",
    "docs/repo/FRONT_DOOR_STATUS.md",
    "docs/repo/RETAINED_BACKBONE.md",
})

# These fields are derived from source text, runner attachment, or citation
# topology. An ordinary verdict transaction must never change them. Other
# top-level fields are auditor-owned or verdict-derived and remain outside the
# static-input fingerprint.
LEDGER_STATIC_FIELDS = frozenset({
    "claim_id",
    "claim_type_author_hint",
    "claim_type_author_hint_raw",
    "criticality",
    "deps",
    "direct_in_degree",
    "helper_runner_paths",
    "note_hash",
    "note_path",
    "runner_path",
    "title",
    "transitive_descendants",
})


def run_git(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


def verdict_generated_path(path: str) -> bool:
    return path in VERDICT_GENERATED_PATHS or path.startswith(
        VERDICT_GENERATED_PREFIXES
    )


def cache_hashes() -> tuple[dict[str, str] | None, str]:
    hashes = {}
    for name in STATIC_CACHE_NAMES:
        path = DATA / name
        try:
            hashes[name] = hashlib.sha256(path.read_bytes()).hexdigest()
        except OSError as exc:
            return None, f"cannot hash required cache {name}: {exc}"
    return hashes, "static caches hashed"


def _ledger_static_bytes(path: Path, relative: str) -> tuple[bytes | None, str]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return None, f"cannot read ledger shard {relative}: {exc}"
    if not isinstance(payload, dict):
        return None, f"ledger shard is not a JSON object: {relative}"
    projection = {
        field: payload.get(field)
        for field in sorted(LEDGER_STATIC_FIELDS)
    }
    return (
        json.dumps(
            projection,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        ).encode("utf-8"),
        "ledger static fields projected",
    )


def static_input_fingerprint() -> tuple[str | None, str]:
    """Hash all current non-verdict inputs, failing closed on inspection."""
    listed = run_git(["ls-files", "-co", "--exclude-standard"])
    if listed.returncode != 0:
        return None, (
            "git ls-files input inspection failed: "
            f"{(listed.stderr or listed.stdout).strip()[:240]}"
        )
    digest = hashlib.sha256()
    for relative in sorted({line for line in listed.stdout.splitlines() if line}):
        path = REPO_ROOT / relative
        if relative.startswith(VERDICT_GENERATED_PREFIXES) and relative.endswith(
            ".json"
        ):
            content, detail = _ledger_static_bytes(path, relative)
            if content is None:
                return None, detail
        elif verdict_generated_path(relative):
            continue
        else:
            try:
                content = path.read_bytes()
            except OSError as exc:
                return None, f"cannot read static input {relative}: {exc}"
        relative_bytes = relative.encode("utf-8")
        digest.update(len(relative_bytes).to_bytes(8, "big"))
        digest.update(relative_bytes)
        digest.update(len(content).to_bytes(8, "big"))
        digest.update(content)
    return digest.hexdigest(), "static input tree fingerprinted"


def verify_checkpoint() -> tuple[bool, str]:
    try:
        checkpoint = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return False, f"cannot read full-pipeline checkpoint: {exc}"
    if not isinstance(checkpoint, dict) or checkpoint.get("schema") != (
        "audit_static_pipeline_checkpoint_v1"
    ):
        return False, "full-pipeline checkpoint has an unsupported schema"

    actual_hashes, detail = cache_hashes()
    if actual_hashes is None:
        return False, detail
    if actual_hashes != checkpoint.get("static_cache_sha256"):
        return False, "derived caches do not match the full-pipeline checkpoint"
    fingerprint, detail = static_input_fingerprint()
    if fingerprint is None:
        return False, detail
    if fingerprint != checkpoint.get("static_input_sha256"):
        return False, "static repository inputs changed since the full pipeline"
    return True, f"full checkpoint {fingerprint[:12]} verified"


def write_checkpoint() -> tuple[bool, str]:
    hashes, detail = cache_hashes()
    if hashes is None:
        return False, detail
    fingerprint, detail = static_input_fingerprint()
    if fingerprint is None:
        return False, detail
    payload = {
        "schema": "audit_static_pipeline_checkpoint_v1",
        "static_cache_sha256": hashes,
        "static_input_sha256": fingerprint,
    }
    temporary = CHECKPOINT.with_suffix(".tmp")
    try:
        temporary.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        os.replace(temporary, CHECKPOINT)
    except OSError as exc:
        temporary.unlink(missing_ok=True)
        return False, f"cannot write full-pipeline checkpoint: {exc}"
    return True, f"wrote full checkpoint {fingerprint[:12]}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("verify", "write"))
    args = parser.parse_args()
    ok, detail = verify_checkpoint() if args.action == "verify" else write_checkpoint()
    print(detail)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
