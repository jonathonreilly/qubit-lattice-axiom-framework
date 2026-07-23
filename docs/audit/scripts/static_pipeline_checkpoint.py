#!/usr/bin/env python3
"""Build or verify the local full-pipeline checkpoint for fast verdict gates.

The gitignored checkpoint is finalized only after a staged full build proves
that its graph and classifier caches were freshly written and that their input
fingerprints stayed stable through the build and the remaining pipeline. It is
an optimization receipt, never an audit authority.
"""
from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import re
import subprocess
import time
from contextlib import contextmanager
from functools import wraps
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
DATA = REPO_ROOT / "docs" / "audit" / "data"
CHECKPOINT = DATA / "static_pipeline_checkpoint.json"
FINAL_SCHEMA = "audit_static_pipeline_checkpoint_v2"
BUILDING_SCHEMA = "audit_static_pipeline_building_v2"
PREPARED_SCHEMA = "audit_static_pipeline_prepared_v2"
CAPTURED_SCHEMA = "audit_static_pipeline_captured_v2"
RECEIPT_SCHEMA = "audit_static_pipeline_producer_receipt_v1"
BUILD_NONCE_ENV = "AUDIT_STATIC_BUILD_NONCE"
EXPECTED_NONCE_ENV = "AUDIT_STATIC_EXPECTED_NONCE"
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
RUNNER_PATH_RE = re.compile(
    r"(scripts/[A-Za-z0-9_./\-]+\.py)|"
    r"(?<![A-Za-z0-9_./\-])([A-Za-z0-9_.\-]+\.py)"
)


@contextmanager
def _checkpoint_lock():
    lock_path = CHECKPOINT.with_suffix(".lock")
    with lock_path.open("w", encoding="utf-8") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        yield


def checkpoint_locked(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        with _checkpoint_lock():
            return function(*args, **kwargs)

    return wrapped


def run_git(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


def _environment_nonce(name: str, *, required: bool) -> tuple[str | None, str]:
    nonce = os.environ.get(name)
    if nonce is None and not required:
        return None, f"{name} not set"
    if (
        not isinstance(nonce, str)
        or len(nonce) != 32
        or any(char not in "0123456789abcdef" for char in nonce)
    ):
        return None, f"{name} must be a 32-character lowercase hex nonce"
    return nonce, "build nonce validated"


def _receipt_path(nonce: str, stage: str) -> Path:
    return DATA / f"static_pipeline_receipt_{nonce}_{stage}.json"


def _cleanup_receipts(nonce: str) -> tuple[bool, str]:
    try:
        for stage in ("citation_graph", "seed_ledger", "runner_classification"):
            _receipt_path(nonce, stage).unlink(missing_ok=True)
    except OSError as exc:
        return False, f"cannot remove static producer receipt: {exc}"
    return True, "static producer receipts removed"


def _atomic_write(path: Path, payload: dict) -> tuple[bool, str]:
    temporary = path.with_suffix(".tmp")
    try:
        temporary.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        os.replace(temporary, path)
    except OSError as exc:
        temporary.unlink(missing_ok=True)
        return False, f"cannot write static pipeline receipt: {exc}"
    return True, "static pipeline receipt written"


def verdict_generated_path(path: str) -> bool:
    return path in VERDICT_GENERATED_PATHS or path.startswith(
        VERDICT_GENERATED_PREFIXES
    )


def cache_hash(name: str) -> tuple[str | None, str]:
    try:
        digest = hashlib.sha256((DATA / name).read_bytes()).hexdigest()
    except OSError as exc:
        return None, f"cannot hash required cache {name}: {exc}"
    return digest, f"{name} hashed"


def cache_hashes() -> tuple[dict[str, str] | None, str]:
    hashes = {}
    for name in STATIC_CACHE_NAMES:
        digest, detail = cache_hash(name)
        if digest is None:
            return None, detail
        hashes[name] = digest
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


def _ledger_filesystem_inputs() -> tuple[set[str] | None, str]:
    """Enumerate every sharded-ledger file, including ignored sidecars."""
    inputs: set[str] = set()
    ledger_dir = DATA / "ledger"
    try:
        for path in ledger_dir.rglob("*"):
            if path.is_file() or path.is_symlink():
                inputs.add(path.relative_to(REPO_ROOT).as_posix())
    except OSError as exc:
        return None, f"cannot enumerate ledger filesystem inputs: {exc}"
    return inputs, "ledger filesystem inputs enumerated"


def _script_filesystem_inputs() -> tuple[set[str] | None, str]:
    """Enumerate ignored as well as Git-visible runner/helper sources."""
    inputs: set[str] = set()
    scripts_dir = REPO_ROOT / "scripts"
    try:
        for path in scripts_dir.rglob("*.py"):
            inputs.add(path.relative_to(REPO_ROOT).as_posix())
    except OSError as exc:
        return None, f"cannot enumerate runner filesystem inputs: {exc}"
    return inputs, "runner filesystem inputs enumerated"


def _note_runner_candidates(graph_inputs: set[str]) -> tuple[set[str] | None, str]:
    """Bind paths whose later appearance can change graph runner attachment."""
    candidates: set[str] = set()
    for relative in sorted(graph_inputs):
        try:
            body = (REPO_ROOT / relative).read_text(
                encoding="utf-8", errors="replace"
            )
        except OSError as exc:
            return None, f"cannot inspect runner references in {relative}: {exc}"
        for match in RUNNER_PATH_RE.finditer(body):
            raw = match.group(1) or match.group(2)
            raw_path = Path(raw)
            possible: list[Path] = []
            if raw.startswith("scripts/"):
                possible.append(raw_path)
            elif not raw_path.is_absolute():
                possible.extend((raw_path, Path("scripts") / raw_path))
            if raw_path.name.endswith(".py"):
                possible.append(Path("scripts") / raw_path.name)
            for candidate in possible:
                if candidate.is_absolute() or ".." in candidate.parts:
                    continue
                candidates.add(candidate.as_posix())
    return candidates, "note runner candidates enumerated"


def _runner_inputs(
    ledger_paths: set[str], graph_inputs: set[str]
) -> tuple[set[str] | None, str]:
    """Enumerate primary, helper, and not-yet-present runner inputs."""
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
        helpers = payload.get("helper_runner_paths") or []
        if not isinstance(helpers, list) or not all(
            isinstance(helper, str) and helper for helper in helpers
        ):
            return None, f"ledger shard has invalid helper_runner_paths: {relative}"
        for helper in helpers:
            helper_path = Path(helper)
            if helper_path.is_absolute() or ".." in helper_path.parts:
                return None, (
                    f"ledger shard helper_runner_paths escapes repository: {relative}"
                )
            inputs.add(helper_path.as_posix())
    note_candidates, detail = _note_runner_candidates(graph_inputs)
    if note_candidates is None:
        return None, detail
    inputs.update(note_candidates)
    script_inputs, detail = _script_filesystem_inputs()
    if script_inputs is None:
        return None, detail
    inputs.update(script_inputs)
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
    ledger_inputs, detail = _ledger_filesystem_inputs()
    if ledger_inputs is None:
        return None, detail
    inputs.update(ledger_inputs)
    ledger_paths = {
        relative for relative in inputs
        if relative.startswith(VERDICT_GENERATED_PREFIXES)
        and relative.endswith(".json")
    }
    runner_inputs, detail = _runner_inputs(ledger_paths, graph_inputs)
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


@checkpoint_locked
def record_producer_receipt(stage: str) -> tuple[bool, str]:
    """Record proof from the successful producer process itself.

    Standalone producer runs remain supported when no build nonce is present;
    only ``run_pipeline.sh`` full mode supplies the nonce and consumes receipts.
    """
    nonce, detail = _environment_nonce(BUILD_NONCE_ENV, required=False)
    if nonce is None:
        return True, "static receipt disabled outside a staged full build"
    stage_schema = {
        "citation_graph": BUILDING_SCHEMA,
        "seed_ledger": BUILDING_SCHEMA,
        "runner_classification": PREPARED_SCHEMA,
    }
    expected_schema = stage_schema.get(stage)
    if expected_schema is None:
        return False, f"unsupported static producer stage: {stage}"
    checkpoint, detail = _read_checkpoint(
        expected_schema, require_build_nonce=True
    )
    if checkpoint is None:
        return False, detail
    include_ledger = stage != "citation_graph"
    fingerprint, detail = static_input_fingerprint(
        include_ledger_static=include_ledger
    )
    if fingerprint is None:
        return False, detail
    output_name = {
        "citation_graph": "citation_graph.json",
        "runner_classification": "runner_classification.json",
    }.get(stage)
    output_hash = None
    if output_name is not None:
        try:
            output_hash = hashlib.sha256(
                (DATA / output_name).read_bytes()
            ).hexdigest()
        except OSError as exc:
            return False, f"cannot hash producer output {output_name}: {exc}"
    payload = {
        "schema": RECEIPT_SCHEMA,
        "stage": stage,
        "build_nonce": nonce,
        "recorded_ns": time.time_ns(),
        "input_sha256": fingerprint,
        "output_name": output_name,
        "output_sha256": output_hash,
    }
    return _atomic_write(_receipt_path(nonce, stage), payload)


def _read_receipt(nonce: str, stage: str) -> tuple[dict | None, str]:
    path = _receipt_path(nonce, stage)
    try:
        receipt = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return None, f"cannot read {stage} producer receipt: {exc}"
    if (
        not isinstance(receipt, dict)
        or receipt.get("schema") != RECEIPT_SCHEMA
        or receipt.get("stage") != stage
        or receipt.get("build_nonce") != nonce
    ):
        return None, f"{stage} producer receipt does not match this full build"
    return receipt, f"{stage} producer receipt loaded"


def _read_checkpoint(
    expected_schema: str, *, require_build_nonce: bool = False
) -> tuple[dict | None, str]:
    try:
        checkpoint = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return None, f"cannot read full-pipeline checkpoint: {exc}"
    if not isinstance(checkpoint, dict) or checkpoint.get("schema") != expected_schema:
        return None, "full-pipeline checkpoint has an unsupported build phase"
    if require_build_nonce:
        nonce, detail = _environment_nonce(BUILD_NONCE_ENV, required=True)
        if nonce is None:
            return None, detail
        if checkpoint.get("build_nonce") != nonce:
            return None, "checkpoint belongs to a different concurrent full build"
    return checkpoint, "checkpoint phase loaded"


def _write_checkpoint(payload: dict) -> tuple[bool, str]:
    ok, detail = _atomic_write(CHECKPOINT, payload)
    if not ok:
        return False, detail.replace("receipt", "checkpoint")
    return True, "checkpoint phase written"


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


@checkpoint_locked
def begin_checkpoint() -> tuple[bool, str]:
    """Invalidate fast mode and record inputs before any full-build stage."""
    nonce, detail = _environment_nonce(BUILD_NONCE_ENV, required=True)
    if nonce is None:
        return False, detail
    fingerprint, detail = static_input_fingerprint(include_ledger_static=False)
    if fingerprint is None:
        return False, detail
    payload = {
        "schema": BUILDING_SCHEMA,
        "build_nonce": nonce,
        "started_ns": time.time_ns(),
        "build_input_sha256": fingerprint,
    }
    ok, detail = _write_checkpoint(payload)
    return (ok, f"began full build {fingerprint[:12]}" if ok else detail)


@checkpoint_locked
def prepare_checkpoint() -> tuple[bool, str]:
    """Prove graph/seed completion and snapshot classifier inputs."""
    checkpoint, detail = _read_checkpoint(
        BUILDING_SCHEMA, require_build_nonce=True
    )
    if checkpoint is None:
        return False, detail
    nonce = checkpoint["build_nonce"]
    graph_receipt, detail = _read_receipt(nonce, "citation_graph")
    if graph_receipt is None:
        return False, detail
    seed_receipt, detail = _read_receipt(nonce, "seed_ledger")
    if seed_receipt is None:
        return False, detail
    fingerprint, detail = static_input_fingerprint(include_ledger_static=False)
    if fingerprint is None:
        return False, detail
    if fingerprint != checkpoint.get("build_input_sha256"):
        return False, "full-build source inputs changed during graph generation"
    if graph_receipt.get("input_sha256") != fingerprint:
        return False, "graph producer receipt has different source inputs"
    static_fingerprint, detail = static_input_fingerprint()
    if static_fingerprint is None:
        return False, detail
    if seed_receipt.get("input_sha256") != static_fingerprint:
        return False, "seed producer receipt has different classifier inputs"
    citation_graph_hash, detail = cache_hash("citation_graph.json")
    if citation_graph_hash is None:
        return False, detail
    if graph_receipt.get("output_sha256") != citation_graph_hash:
        return False, "citation graph differs from its producer receipt"
    payload = {
        **checkpoint,
        "schema": PREPARED_SCHEMA,
        "citation_graph_sha256": citation_graph_hash,
        "static_input_sha256": static_fingerprint,
    }
    ok, detail = _write_checkpoint(payload)
    return (
        ok,
        f"prepared classifier inputs {static_fingerprint[:12]}" if ok else detail,
    )


@checkpoint_locked
def capture_checkpoint() -> tuple[bool, str]:
    """Bind freshly generated static caches to unchanged classifier inputs."""
    checkpoint, detail = _read_checkpoint(
        PREPARED_SCHEMA, require_build_nonce=True
    )
    if checkpoint is None:
        return False, detail
    classifier_receipt, detail = _read_receipt(
        checkpoint["build_nonce"], "runner_classification"
    )
    if classifier_receipt is None:
        return False, detail
    fingerprint, detail = static_input_fingerprint()
    if fingerprint is None:
        return False, detail
    if fingerprint != checkpoint.get("static_input_sha256"):
        return False, "classifier inputs changed while static caches were built"
    if classifier_receipt.get("input_sha256") != fingerprint:
        return False, "classifier producer receipt has different static inputs"
    hashes, detail = cache_hashes()
    if hashes is None:
        return False, detail
    if hashes["citation_graph.json"] != checkpoint.get("citation_graph_sha256"):
        return False, "citation graph changed after its full-build stage"
    if classifier_receipt.get("output_sha256") != hashes[
        "runner_classification.json"
    ]:
        return False, "runner classification differs from its producer receipt"
    payload = {
        **checkpoint,
        "schema": CAPTURED_SCHEMA,
        "static_cache_sha256": hashes,
    }
    ok, detail = _write_checkpoint(payload)
    return (ok, f"captured full-build caches {fingerprint[:12]}" if ok else detail)


@checkpoint_locked
def finalize_checkpoint() -> tuple[bool, str]:
    """Finalize only when the rest of the full pipeline preserved the proof."""
    checkpoint, detail = _read_checkpoint(
        CAPTURED_SCHEMA, require_build_nonce=True
    )
    if checkpoint is None:
        return False, detail
    matches, detail = _matches_checkpoint(checkpoint)
    if not matches:
        return False, detail
    payload = {**checkpoint, "schema": FINAL_SCHEMA}
    ok, write_detail = _write_checkpoint(payload)
    fingerprint = checkpoint["static_input_sha256"]
    if not ok:
        return False, write_detail
    cleaned, cleanup_detail = _cleanup_receipts(checkpoint["build_nonce"])
    if not cleaned:
        return False, cleanup_detail
    return True, f"finalized full checkpoint {fingerprint[:12]}"


@checkpoint_locked
def abort_checkpoint() -> tuple[bool, str]:
    """Remove only this full build's transient receipts and partial proof."""
    nonce, detail = _environment_nonce(BUILD_NONCE_ENV, required=True)
    if nonce is None:
        return False, detail
    cleaned, detail = _cleanup_receipts(nonce)
    if not cleaned:
        return False, detail
    try:
        checkpoint = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        checkpoint = None
    if (
        isinstance(checkpoint, dict)
        and checkpoint.get("build_nonce") == nonce
        and checkpoint.get("schema") != FINAL_SCHEMA
    ):
        try:
            CHECKPOINT.unlink(missing_ok=True)
        except OSError as exc:
            return False, f"cannot remove partial full-build checkpoint: {exc}"
    return True, "full-build transient receipts removed"


@checkpoint_locked
def verify_checkpoint() -> tuple[bool, str]:
    checkpoint, detail = _read_checkpoint(FINAL_SCHEMA)
    if checkpoint is None:
        return False, detail
    expected_nonce, nonce_detail = _environment_nonce(
        EXPECTED_NONCE_ENV, required=False
    )
    if os.environ.get(EXPECTED_NONCE_ENV) is not None:
        if expected_nonce is None:
            return False, nonce_detail
        if checkpoint.get("build_nonce") != expected_nonce:
            return False, "full-pipeline checkpoint changed during fast use"
    matches, detail = _matches_checkpoint(checkpoint)
    if not matches:
        return False, detail
    return True, f"full checkpoint {checkpoint['static_input_sha256'][:12]} verified"


@checkpoint_locked
def checkpoint_identity() -> tuple[bool, str]:
    checkpoint, detail = _read_checkpoint(FINAL_SCHEMA)
    if checkpoint is None:
        return False, detail
    matches, detail = _matches_checkpoint(checkpoint)
    if not matches:
        return False, detail
    nonce = checkpoint.get("build_nonce")
    if not isinstance(nonce, str):
        return False, "full-pipeline checkpoint has no build identity"
    return True, nonce


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action",
        choices=(
            "begin", "prepare", "capture", "finalize", "abort", "verify", "identity"
        ),
    )
    args = parser.parse_args()
    actions = {
        "begin": begin_checkpoint,
        "prepare": prepare_checkpoint,
        "capture": capture_checkpoint,
        "finalize": finalize_checkpoint,
        "abort": abort_checkpoint,
        "verify": verify_checkpoint,
        "identity": checkpoint_identity,
    }
    ok, detail = actions[args.action]()
    print(detail)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
