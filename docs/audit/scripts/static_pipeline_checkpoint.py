#!/usr/bin/env python3
"""Build or verify the local full-pipeline checkpoint for fast verdict gates.

The gitignored checkpoint is finalized only after a staged full build proves
that its graph and classifier caches were freshly written and that their input
fingerprints stayed stable through the build and the remaining pipeline. It is
an optimization receipt, never an audit authority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import secrets
import subprocess
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
DATA = REPO_ROOT / "docs" / "audit" / "data"
CHECKPOINT = DATA / "static_pipeline_checkpoint.json"
FINAL_SCHEMA = "audit_static_pipeline_checkpoint_v2"
BUILDING_SCHEMA = "audit_static_pipeline_building_v2"
PREPARED_SCHEMA = "audit_static_pipeline_prepared_v2"
CAPTURED_SCHEMA = "audit_static_pipeline_captured_v2"
STATIC_CACHE_NAMES = (
    "citation_graph.json",
    "runner_classification.json",
)
FULL_STATIC_GENERATED_PATHS = frozenset({
    "docs/audit/data/citation_graph_manifest.json",
})
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

# Only these known auditor-owned or downstream-derived fields may change
# without invalidating a skipped seed/classifier pass. Unknown fields are
# hashed by default, so schema growth fails closed rather than silently being
# treated as verdict-owned.
LEDGER_VERDICT_FIELDS = frozenset({
    "audit_date",
    "audit_invocation_history",
    "audit_invocation_id",
    "audit_state_snapshot",
    "audit_status",
    "auditor",
    "auditor_confidence",
    "auditor_family",
    "auditor_model",
    "auditor_reasoning_effort",
    "blocker",
    "chain_closes",
    "chain_closure_explanation",
    "claim_scope",
    "claim_type",
    "claim_type_last_reviewed",
    "claim_type_provenance",
    "cross_confirmation",
    "decoration_parent_claim_id",
    "effective_status",
    "effective_status_reason",
    "independence",
    "intrinsic_status",
    "load_bearing_step",
    "load_bearing_step_class",
    "max_descendant_status",
    "max_descendant_status_rank",
    "negative_assertion_classes",
    "no_go_discipline",
    "notes_for_re_audit_if_any",
    "open_dependency_paths",
    "previous_auditor_family",
    "previous_audits",
    "prose_corrections",
    "prose_status",
    "relabel_date",
    "relabel_reason",
    "restoration_history",
    "runner_check_breakdown",
    "unattributed_audit_provenance",
    "verdict_rationale",
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
        field: value
        for field, value in sorted(payload.items())
        if field not in LEDGER_VERDICT_FIELDS
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


def _graph_markdown_inputs() -> tuple[set[str] | None, str]:
    """Enumerate filesystem notes consumed by the skipped graph builder.

    The graph builder intentionally discovers Markdown from the filesystem,
    including ignored files. Keep the same broad input boundary here while
    excluding its generated audit/report surfaces. Including class-F memos is
    conservative: they are rare and hashing them can only force a full run.
    """
    inputs: set[str] = set()
    docs = REPO_ROOT / "docs"
    try:
        for path in docs.rglob("*.md"):
            relative = path.relative_to(REPO_ROOT).as_posix()
            docs_relative = path.relative_to(docs)
            if docs_relative.parts[:1] == ("audit",):
                continue
            if docs_relative.parts[:2] == ("publication", "ci3_z3") and (
                docs_relative.name == "PUBLICATION_AUDIT_DIVERGENCE.md"
                or docs_relative.name.endswith("_EFFECTIVE_STATUS.md")
            ):
                continue
            if docs_relative.parts[:1] == ("repo",) and docs_relative.name in {
                "FRONT_DOOR_STATUS.md",
                "RETAINED_BACKBONE.md",
            }:
                continue
            inputs.add(relative)
    except OSError as exc:
        return None, f"cannot enumerate graph Markdown inputs: {exc}"
    return inputs, "graph Markdown inputs enumerated"


def _runner_inputs(ledger_paths: set[str]) -> tuple[set[str] | None, str]:
    """Enumerate exact runner paths consumed by the skipped classifier."""
    inputs: set[str] = set()
    for relative in sorted(ledger_paths):
        try:
            payload = json.loads((REPO_ROOT / relative).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            return None, f"cannot inspect runner path in {relative}: {exc}"
        if not isinstance(payload, dict):
            return None, f"ledger shard is not a JSON object: {relative}"
        runner = payload.get("runner_path")
        if runner is None:
            continue
        if not isinstance(runner, str) or not runner:
            return None, f"ledger shard has invalid runner_path: {relative}"
        runner_path = Path(runner)
        if runner_path.is_absolute() or ".." in runner_path.parts:
            return None, f"ledger shard runner_path escapes repository: {relative}"
        inputs.add(runner_path.as_posix())
    return inputs, "classifier runner inputs enumerated"


def static_input_fingerprint(
    *, include_ledger_static: bool = True
) -> tuple[str | None, str]:
    """Hash all current non-verdict inputs, failing closed on inspection."""
    listed = run_git(["ls-files", "-co", "--exclude-standard"])
    if listed.returncode != 0:
        return None, (
            "git ls-files input inspection failed: "
            f"{(listed.stderr or listed.stdout).strip()[:240]}"
        )
    inputs = {line for line in listed.stdout.splitlines() if line}
    graph_inputs, detail = _graph_markdown_inputs()
    if graph_inputs is None:
        return None, detail
    inputs.update(graph_inputs)
    ledger_paths = {
        relative for relative in inputs
        if relative.startswith(VERDICT_GENERATED_PREFIXES)
        and relative.endswith(".json")
    }
    runner_inputs, detail = _runner_inputs(ledger_paths)
    if runner_inputs is None:
        return None, detail
    inputs.update(runner_inputs)

    digest = hashlib.sha256()
    for relative in sorted(inputs):
        path = REPO_ROOT / relative
        if relative.startswith(VERDICT_GENERATED_PREFIXES) and relative.endswith(
            ".json"
        ):
            if not include_ledger_static:
                continue
            content, detail = _ledger_static_bytes(path, relative)
            if content is None:
                return None, detail
        elif relative in VERDICT_GENERATED_PATHS:
            continue
        elif not include_ledger_static and relative in FULL_STATIC_GENERATED_PATHS:
            continue
        elif relative in runner_inputs and not path.exists():
            # Classifier output records missing runners. Bind that absence so
            # the later appearance of an ignored runner invalidates the cache.
            content = b"\0MISSING RUNNER\0"
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


def _read_checkpoint(expected_schema: str) -> tuple[dict | None, str]:
    try:
        checkpoint = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return None, f"cannot read full-pipeline checkpoint: {exc}"
    if not isinstance(checkpoint, dict) or checkpoint.get("schema") != expected_schema:
        return None, "full-pipeline checkpoint has an unsupported build phase"
    return checkpoint, "checkpoint phase loaded"


def _write_checkpoint(payload: dict) -> tuple[bool, str]:
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
    return True, "checkpoint phase written"


def _cache_fresh_since(name: str, started_ns: int) -> tuple[bool, str]:
    if not isinstance(started_ns, int) or started_ns < 0:
        return False, "full-build checkpoint has an invalid start timestamp"
    try:
        modified_ns = (DATA / name).stat().st_mtime_ns
    except OSError as exc:
        return False, f"cannot inspect required cache {name}: {exc}"
    if modified_ns < started_ns:
        return False, f"required cache {name} was not rebuilt in this full run"
    return True, f"{name} rebuilt"


def _matches_checkpoint(checkpoint: dict) -> tuple[bool, str]:
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
    return True, f"checkpoint {fingerprint[:12]} matches current inputs"


def begin_checkpoint() -> tuple[bool, str]:
    """Invalidate fast mode and record inputs before any full-build stage."""
    fingerprint, detail = static_input_fingerprint(include_ledger_static=False)
    if fingerprint is None:
        return False, detail
    payload = {
        "schema": BUILDING_SCHEMA,
        "build_nonce": secrets.token_hex(16),
        "started_ns": time.time_ns(),
        "build_input_sha256": fingerprint,
    }
    ok, detail = _write_checkpoint(payload)
    return (ok, f"began full build {fingerprint[:12]}" if ok else detail)


def prepare_checkpoint() -> tuple[bool, str]:
    """Prove graph/seed completion and snapshot classifier inputs."""
    checkpoint, detail = _read_checkpoint(BUILDING_SCHEMA)
    if checkpoint is None:
        return False, detail
    fingerprint, detail = static_input_fingerprint(include_ledger_static=False)
    if fingerprint is None:
        return False, detail
    if fingerprint != checkpoint.get("build_input_sha256"):
        return False, "full-build source inputs changed during graph generation"
    fresh, detail = _cache_fresh_since(
        "citation_graph.json", checkpoint.get("started_ns", -1)
    )
    if not fresh:
        return False, detail
    static_fingerprint, detail = static_input_fingerprint()
    if static_fingerprint is None:
        return False, detail
    hashes, detail = cache_hashes()
    if hashes is None:
        return False, detail
    payload = {
        **checkpoint,
        "schema": PREPARED_SCHEMA,
        "citation_graph_sha256": hashes["citation_graph.json"],
        "static_input_sha256": static_fingerprint,
    }
    ok, detail = _write_checkpoint(payload)
    return (
        ok,
        f"prepared classifier inputs {static_fingerprint[:12]}" if ok else detail,
    )


def capture_checkpoint() -> tuple[bool, str]:
    """Bind freshly generated static caches to unchanged classifier inputs."""
    checkpoint, detail = _read_checkpoint(PREPARED_SCHEMA)
    if checkpoint is None:
        return False, detail
    fresh, detail = _cache_fresh_since(
        "runner_classification.json", checkpoint.get("started_ns", -1)
    )
    if not fresh:
        return False, detail
    fingerprint, detail = static_input_fingerprint()
    if fingerprint is None:
        return False, detail
    if fingerprint != checkpoint.get("static_input_sha256"):
        return False, "classifier inputs changed while static caches were built"
    hashes, detail = cache_hashes()
    if hashes is None:
        return False, detail
    if hashes["citation_graph.json"] != checkpoint.get("citation_graph_sha256"):
        return False, "citation graph changed after its full-build stage"
    payload = {
        **checkpoint,
        "schema": CAPTURED_SCHEMA,
        "static_cache_sha256": hashes,
    }
    ok, detail = _write_checkpoint(payload)
    return (ok, f"captured full-build caches {fingerprint[:12]}" if ok else detail)


def finalize_checkpoint() -> tuple[bool, str]:
    """Finalize only when the rest of the full pipeline preserved the proof."""
    checkpoint, detail = _read_checkpoint(CAPTURED_SCHEMA)
    if checkpoint is None:
        return False, detail
    matches, detail = _matches_checkpoint(checkpoint)
    if not matches:
        return False, detail
    payload = {**checkpoint, "schema": FINAL_SCHEMA}
    ok, write_detail = _write_checkpoint(payload)
    fingerprint = checkpoint["static_input_sha256"]
    return (ok, f"finalized full checkpoint {fingerprint[:12]}" if ok else write_detail)


def verify_checkpoint() -> tuple[bool, str]:
    checkpoint, detail = _read_checkpoint(FINAL_SCHEMA)
    if checkpoint is None:
        return False, detail
    matches, detail = _matches_checkpoint(checkpoint)
    if not matches:
        return False, detail
    return True, f"full checkpoint {checkpoint['static_input_sha256'][:12]} verified"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action", choices=("begin", "prepare", "capture", "finalize", "verify")
    )
    args = parser.parse_args()
    actions = {
        "begin": begin_checkpoint,
        "prepare": prepare_checkpoint,
        "capture": capture_checkpoint,
        "finalize": finalize_checkpoint,
        "verify": verify_checkpoint,
    }
    ok, detail = actions[args.action]()
    print(detail)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
