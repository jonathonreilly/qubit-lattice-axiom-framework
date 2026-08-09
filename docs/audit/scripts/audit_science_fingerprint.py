#!/usr/bin/env python3
"""Content-addressed scientific provenance for audit judgments.

``science_fingerprint_v2`` deliberately excludes audit-packet policy.  A
packet/schema change may require a new certificate, but it does not by itself
change the scientific judgment.  Conversely, every surface that can change
the meaning or evidential basis of that judgment is captured here and must
match exactly before any prior judgment can be reused.

The fingerprint is shared by apply, invalidation, restoration, and queue
routing.  Do not mirror this logic in a caller: a provenance comparison is a
security boundary and must have one producer/comparator.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Callable


sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts"))


SCIENCE_FINGERPRINT_SCHEMA = "science_fingerprint_v2"
PACKET_POLICY_FINGERPRINT_SCHEMA = "packet_policy_fingerprint_v1"
JUDGMENT_FINGERPRINT_SCHEMA = "frozen_audit_judgment_v1"

# These sources define which inputs are admissible, how dependency readiness
# is interpreted, and whether runner evidence is authentic and complete.  The
# manifest in ``dependency_policy_epoch.json`` must contain this exact set.
# Keep the tuple centralized so tests and maintenance tools cannot silently
# mirror a narrower policy boundary.
DEPENDENCY_POLICY_SOURCES = (
    "docs/audit/FRESH_LOOK_REQUIREMENTS.md",
    "docs/audit/scripts/audit_science_fingerprint.py",
    "docs/audit/scripts/build_citation_graph.py",
    "docs/audit/scripts/classify_runner_passes.py",
    "docs/audit/scripts/compute_audit_queue.py",
    "docs/audit/scripts/compute_effective_status.py",
    "docs/audit/scripts/forensic_evidence_readiness.py",
    "docs/audit/scripts/premise_nodes.py",
    "docs/audit/scripts/runner_pin_gate.py",
    "scripts/runner_cache.py",
    "docs/audit/data/doc_authority_registry.json",
    "docs/audit/data/tier_a_admissions.json",
    "docs/audit/data/owner_governed_premise_nodes.json",
    "docs/audit/data/source_path_aliases.json",
)
OPTIONAL_DEPENDENCY_POLICY_SOURCES = {
    "docs/audit/data/tier_a_admissions.json",
    "docs/audit/data/owner_governed_premise_nodes.json",
}

# ---------------------------------------------------------------------------
# Claim-scoped helper-registry carve-out
# (owner ruling 2026-08-09, "amend gate + restore"; ACTIVE_REVIEW_QUEUE item
#  2026-08-08-dependency-policy-epoch-debt-helper-registry).
#
# ``build_citation_graph.py`` remains a governed dependency-policy source,
# byte-exact EXCEPT for the ``EXPLICIT_PACKET_HELPER_RUNNER_PATHS``
# assignment. That dict registers additional helper-runner source files for
# individual claims' restricted audit packets. Registrations are additive
# claim-scoped metadata, not dependency-interpretation policy: each
# registered helper lands on the affected row's ``helper_runner_paths``,
# where ``science_fingerprint_v2`` already binds that helper's exact bytes
# and declared inputs on the registered claim itself. A new registration
# therefore perturbs only the registered claim's own fingerprint; it cannot
# change how dependencies, premises, chain sufficiency, or evidence
# readiness are interpreted for any other row. Hashing the registry bytes
# into the repository-wide policy epoch made every additive registration a
# ~900-row hard reset, so registrations were deferred and the manifest gate
# went stale (the 2026-08-08 epoch-debt queue item). Under the owner ruling
# the epoch instead hashes a normalized rendering of the builder with
# exactly that assignment's source span spliced out, located via the AST
# (never a regex) so nested braces, comments, and string contents cannot
# desynchronize the span. Every other byte of the builder stays governed
# byte-exact, and the carve-out fails closed with
# ``ScienceFingerprintError`` unless the name is bound exactly once in the
# whole module — in ANY binding form, including a second assignment,
# annotated/augmented assignment, tuple unpacking, walrus, ``del``, an
# import alias, a wildcard import, a ``def``/``async def``/``class``, a
# parameter, a
# ``for``/``with``/``except``/``match`` binding, a PEP 695 type parameter
# (``def f[NAME]``, ``class C[NAME]``, ``type A[NAME] = ...``, and the
# ``**NAME``/``*NAME`` spellings), a ``type NAME = ...`` alias, or a
# ``global``/
# ``nonlocal`` declaration — by a single-target module-level assignment
# whose value is a strictly literal ``{str: [str, ...]}`` display. Nothing
# executable (``**`` unpacking, a call, a comprehension, a name reference,
# a starred element) may sit inside the excluded span, because those bytes
# would otherwise carry live policy semantics outside the governed hash.
# ---------------------------------------------------------------------------
CLAIM_SCOPED_HELPER_REGISTRY_SOURCE = "docs/audit/scripts/build_citation_graph.py"
CLAIM_SCOPED_HELPER_REGISTRY_NAME = "EXPLICIT_PACKET_HELPER_RUNNER_PATHS"

_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")

# PEP 695 (Python 3.12+) introduced a binding form that no earlier node type
# covers: a type parameter list on ``def``/``class``/``type`` binds each
# parameter name through ``ast.TypeVar`` / ``ast.ParamSpec`` /
# ``ast.TypeVarTuple`` nodes whose ``name`` field is a plain ``str``.  The
# lookups are guarded so this module stays importable on pre-3.12
# interpreters, where the syntax cannot be written at all.
_TYPE_PARAM_NODE_TYPES = tuple(
    node_type
    for node_type in (
        getattr(ast, "TypeVar", None),
        getattr(ast, "ParamSpec", None),
        getattr(ast, "TypeVarTuple", None),
    )
    if isinstance(node_type, type)
)
_TYPE_ALIAS_NODE_TYPES = tuple(
    node_type
    for node_type in (getattr(ast, "TypeAlias", None),)
    if isinstance(node_type, type)
)


class ScienceFingerprintError(ValueError):
    """A scientific provenance baseline cannot be produced or validated."""


def _canonical_json(value: object) -> bytes:
    try:
        rendered = json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        raise ScienceFingerprintError(
            f"scientific provenance is not canonical JSON: {exc}"
        ) from exc
    return rendered.encode("utf-8")


def _digest(value: object) -> str:
    return hashlib.sha256(_canonical_json(value)).hexdigest()


def _epoch_value(
    repo_root: Path,
    cache: dict[str, str] | None,
    key: str,
    builder: Callable[[Path], str],
) -> str:
    """Memoize repository-wide epochs only when a caller owns the cache.

    Direct calls remain uncached so unit tests, migrations, and review probes
    observe filesystem edits immediately.  Long ledger sweeps pass a cache
    whose lifetime is one immutable repository read, avoiding thousands of
    repeated hashes of the same governed sources.
    """
    if cache is None:
        return builder(repo_root)
    if key not in cache:
        cache[key] = builder(repo_root)
    return cache[key]


def _file_sha256(path: Path, *, required: bool = False) -> str | None:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError as exc:
        if required:
            raise ScienceFingerprintError(
                f"required scientific provenance surface is unreadable: {path}"
            ) from exc
        return None


def _binds_registry_name(node: ast.AST) -> bool:
    """True when ``node`` is a construct that binds the registry name.

    Every binding form Python has is enumerated here on purpose.  The
    carve-out's security promise is that the spliced-out span is the module's
    ONE definition of the registry, so a second construct that could rebind,
    shadow, alias, or delete the name has to fail the gate rather than be
    silently ignored while its own bytes leave the governed surface.
    """
    name = CLAIM_SCOPED_HELPER_REGISTRY_NAME
    if isinstance(node, ast.Name):
        # Assign/AnnAssign/AugAssign targets, tuple/list unpacking, walrus,
        # for/with/comprehension targets (Store), and `del NAME` (Del).
        return node.id == name and isinstance(node.ctx, (ast.Store, ast.Del))
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return node.name == name
    if isinstance(node, ast.alias):
        # `import x as NAME`, `from m import NAME`, `import NAME.sub`, and
        # `from m import *`, which can bind any name and so is never decidable
        # as safe from the source alone.
        if node.name == "*":
            return True
        return (node.asname or node.name.split(".", 1)[0]) == name
    if isinstance(node, ast.ExceptHandler):
        return node.name == name
    if isinstance(node, (ast.Global, ast.Nonlocal)):
        return name in node.names
    if isinstance(node, ast.arg):
        return node.arg == name
    if isinstance(node, (ast.MatchAs, ast.MatchStar)):
        return node.name == name
    if isinstance(node, ast.MatchMapping):
        return node.rest == name
    if _TYPE_PARAM_NODE_TYPES and isinstance(node, _TYPE_PARAM_NODE_TYPES):
        # PEP 695 type parameters: `def f[NAME]()`, `class C[NAME]`,
        # `type Alias[NAME] = ...`, and the `**NAME` (ParamSpec) / `*NAME`
        # (TypeVarTuple) spellings.  Each binds NAME inside its own scope and
        # would otherwise shadow the registry with bytes outside the splice.
        return getattr(node, "name", None) == name
    if _TYPE_ALIAS_NODE_TYPES and isinstance(node, _TYPE_ALIAS_NODE_TYPES):
        # `type NAME = ...`.  The statement's own target is an ``ast.Name`` in
        # Store context, so the ``ast.Name`` branch above already reports it;
        # naming the statement explicitly keeps the enumeration complete and
        # only ever raises the binding count, which cannot turn a refusal into
        # an acceptance.
        alias_target = getattr(node, "name", None)
        return (
            isinstance(alias_target, ast.Name)
            and alias_target.id == name
            and isinstance(alias_target.ctx, (ast.Store, ast.Del))
        )
    return False


def _is_literal_registry_dict(value: ast.AST) -> bool:
    """True only for a strictly literal ``{str: [str, ...]}`` display.

    Nothing that can execute, unpack, or read another name may sit inside the
    excluded span: `**other`, a call, a comprehension, a name reference, an
    f-string, or a starred element would all be live policy-bearing code
    hidden from the governed hash.  ``ast.Constant`` string keys and
    list/tuple-of-``ast.Constant``-string values are the entire admissible
    grammar.
    """
    if not isinstance(value, ast.Dict):
        return False
    if len(value.keys) != len(value.values):
        return False
    for key, element_list in zip(value.keys, value.values):
        # A ``None`` key is `**mapping` unpacking, not a literal entry.
        if not (isinstance(key, ast.Constant) and isinstance(key.value, str)):
            return False
        if not isinstance(element_list, (ast.List, ast.Tuple)):
            return False
        for element in element_list.elts:
            if not (
                isinstance(element, ast.Constant)
                and isinstance(element.value, str)
            ):
                return False
    return True


def _is_registry_literal_assignment(node: ast.AST) -> bool:
    """True for the one module-level statement the carve-out may exclude."""
    return (
        isinstance(node, ast.Assign)
        and len(node.targets) == 1
        and isinstance(node.targets[0], ast.Name)
        and node.targets[0].id == CLAIM_SCOPED_HELPER_REGISTRY_NAME
        and _is_literal_registry_dict(node.value)
    )


def _helper_registry_span(source: bytes, path: Path) -> tuple[int, int]:
    """Locate the exact byte span of the helper-registry assignment.

    AST end positions (UTF-8 byte columns) identify the statement span, so
    nested braces, inline comments, and string contents inside the dict can
    never desynchronize the splice the way a regex could. Fails closed when
    the name is bound anywhere in the module in any form other than exactly
    one module-level, single-target, strictly literal ``{str: [str, ...]}``
    assignment.
    """
    try:
        tree = ast.parse(source.decode("utf-8"))
    except (SyntaxError, ValueError, UnicodeDecodeError) as exc:
        raise ScienceFingerprintError(
            f"governed policy source is not parseable Python: {path}: {exc}"
        ) from exc
    bindings = [node for node in ast.walk(tree) if _binds_registry_name(node)]
    if len(bindings) != 1:
        raise ScienceFingerprintError(
            f"{CLAIM_SCOPED_HELPER_REGISTRY_NAME} must be bound exactly once "
            f"in {path}: found {len(bindings)} bindings"
        )
    assignment = next(
        (node for node in tree.body if _is_registry_literal_assignment(node)),
        None,
    )
    if assignment is None:
        raise ScienceFingerprintError(
            f"{CLAIM_SCOPED_HELPER_REGISTRY_NAME} in {path} must be a "
            "single-target module-level literal-dict assignment whose keys "
            "are string constants and whose values are lists/tuples of "
            "string constants; anything else is a policy change and needs a "
            "reviewed epoch refresh"
        )
    line_starts = [0]
    for index, byte in enumerate(source):
        if byte == 0x0A:
            line_starts.append(index + 1)
    start = line_starts[assignment.lineno - 1] + assignment.col_offset
    end = line_starts[assignment.end_lineno - 1] + assignment.end_col_offset
    return start, end


def _claim_scoped_registry_normalized_sha256(path: Path) -> str:
    """Hash the registry-bearing builder with the registry span removed."""
    try:
        source = path.read_bytes()
    except OSError as exc:
        raise ScienceFingerprintError(
            f"required scientific provenance surface is unreadable: {path}"
        ) from exc
    start, end = _helper_registry_span(source, path)
    return hashlib.sha256(source[:start] + source[end:]).hexdigest()


def dependency_policy_source_sha256(repo_root: Path, path: str) -> str | None:
    """Hash one governed dependency-policy source under the current rule.

    Single producer for both the epoch gate (``dependency_policy_epoch``)
    and the manifest refresh path
    (``refresh_dependency_policy_manifest``), so the comparator and the
    manifest writer can never disagree about the governed byte surface.
    """
    if path == CLAIM_SCOPED_HELPER_REGISTRY_SOURCE:
        return _claim_scoped_registry_normalized_sha256(repo_root / path)
    return _file_sha256(
        repo_root / path,
        required=path not in OPTIONAL_DEPENDENCY_POLICY_SOURCES,
    )


def _load_json_object(path: Path, label: str) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ScienceFingerprintError(f"cannot read {label}: {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ScienceFingerprintError(f"{label} must contain a JSON object: {path}")
    return value


def _premise_registry(repo_root: Path) -> dict:
    path = repo_root / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
    registry = _load_json_object(path, "axiom-premise registry")
    canonical_ids = registry.get("canonical_ids")
    nodes = registry.get("nodes")
    if (
        not isinstance(canonical_ids, list)
        or not all(isinstance(item, str) and item for item in canonical_ids)
        or len(canonical_ids) != len(set(canonical_ids))
        or not isinstance(nodes, dict)
    ):
        raise ScienceFingerprintError("axiom-premise registry has an invalid shape")
    for claim_id in canonical_ids:
        node = nodes.get(claim_id)
        current_path = node.get("current_path") if isinstance(node, dict) else None
        if not isinstance(current_path, str) or not current_path:
            raise ScienceFingerprintError(
                f"axiom-premise registry has no current_path for {claim_id}"
            )
    return registry


def _non_evidence_context_ids(repo_root: Path) -> set[str]:
    path = repo_root / "docs" / "audit" / "data" / "doc_authority_registry.json"
    registry = _load_json_object(path, "document-authority registry")
    rows = registry.get("rows")
    if not isinstance(rows, list):
        raise ScienceFingerprintError("document-authority registry rows must be a list")
    return {
        str(item["claim_id"])
        for item in rows
        if isinstance(item, dict)
        and item.get("chain_satisfying") is False
        and isinstance(item.get("claim_id"), str)
        and item.get("claim_id")
    }


def accepted_premise_ids(repo_root: Path) -> set[str]:
    """Return the current canonical axiom/approved-primitive membership."""
    return set(_premise_registry(repo_root)["canonical_ids"])


def legacy_premise_snapshot_change(
    snapshot: dict,
    row: dict,
    rows: dict[str, dict],
    repo_root: Path,
) -> str | None:
    """Fail-closed compatibility check for pre-v2 premise hash snapshots.

    A key in ``dep_axiom_premise_note_hash`` proves that the dependency was an
    accepted premise when audited.  It must therefore remain both a direct
    dependency and an accepted premise, and its registered note hash must
    still match.  Crucially, iteration starts from the historical keys; using
    current registry membership here would make removal/reclassification
    invisible.
    """
    historical = snapshot.get("dep_axiom_premise_note_hash") or {}
    if not isinstance(historical, dict):
        return "legacy_premise_snapshot_invalid"
    current_deps = set(row.get("deps") or [])
    current_premises = accepted_premise_ids(repo_root)
    historical_premises = set(historical)
    current_direct_premises = current_deps & current_premises
    newly_classified = sorted(current_direct_premises - historical_premises)
    if newly_classified:
        return f"axiom_premise_classification_changed:{newly_classified[0]}"
    for dep_id, before in sorted(historical.items()):
        if dep_id not in current_deps:
            return f"axiom_premise_dependency_removed:{dep_id}"
        if dep_id not in current_premises:
            return f"axiom_premise_classification_changed:{dep_id}"
        after = (rows.get(dep_id) or {}).get("note_hash")
        if before != after:
            before_short = before[:8] if isinstance(before, str) else "missing"
            after_short = after[:8] if isinstance(after, str) else "missing"
            return (
                f"axiom_premise_changed:{dep_id}:"
                f"{before_short}->{after_short}"
            )
    return None


def premise_classification(
    dep_id: str,
    *,
    accepted_premise_ids: set[str],
    non_evidence_context_ids: set[str],
) -> str:
    if dep_id in accepted_premise_ids:
        return "accepted_premise"
    if dep_id in non_evidence_context_ids:
        return "non_evidence_context"
    return "ordinary_claim"


def framework_premise_epoch(repo_root: Path) -> str:
    """Bind premise membership, governance metadata, paths, and source bytes.

    The full registry hash is intentional.  A change to what an axiom or
    approved primitive means, how it is classified, or which source owns it is
    scientifically relevant even when every ledger row remains ``meta``.
    """
    registry_path = (
        repo_root / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
    )
    registry = _premise_registry(repo_root)
    node_sources: list[dict[str, str]] = []
    for claim_id in registry["canonical_ids"]:
        current_path = registry["nodes"][claim_id]["current_path"]
        node_sources.append(
            {
                "claim_id": claim_id,
                "current_path": current_path,
                "source_sha256": _file_sha256(
                    repo_root / current_path,
                    required=True,
                ),
            }
        )
    return _digest(
        {
            "schema": "framework_premise_epoch_v2",
            "registry_sha256": _file_sha256(registry_path, required=True),
            "node_sources": node_sources,
        }
    )


def _dependency_policy_manifest_path(repo_root: Path) -> Path:
    return repo_root / "docs" / "audit" / "data" / "dependency_policy_epoch.json"


def dependency_policy_epoch(repo_root: Path) -> str:
    """Bind the rules that decide dependency identity and chain sufficiency.

    Exact row/dependency bytes are insufficient when the interpretation of a
    dependency changes while its stored status string does not.  Hashing these
    governed policy surfaces makes a premise/admission/readiness rule change a
    deliberate re-audit event whose blast radius is visible in review.

    The claim-scoped helper registry inside ``build_citation_graph.py`` is
    excluded from the governed byte surface (see the carve-out note above
    ``CLAIM_SCOPED_HELPER_REGISTRY_SOURCE``); the rest of that builder and
    every other source stay governed byte-exact.
    """
    actual_sources = {
        path: dependency_policy_source_sha256(repo_root, path)
        for path in DEPENDENCY_POLICY_SOURCES
    }
    manifest_path = _dependency_policy_manifest_path(repo_root)
    manifest = _load_json_object(manifest_path, "dependency-policy epoch")
    if (
        manifest.get("schema") != "dependency_policy_epoch_manifest_v1"
        or not isinstance(manifest.get("epoch"), str)
        or not manifest.get("epoch")
        or manifest.get("sources") != actual_sources
    ):
        raise ScienceFingerprintError(
            "dependency-policy epoch manifest does not exactly match its "
            "governed sources; review the policy change and refresh "
            "docs/audit/data/dependency_policy_epoch.json"
        )
    return _digest(
        {
            "schema": "dependency_policy_epoch_v1",
            "epoch": manifest["epoch"],
            "manifest_sha256": _file_sha256(manifest_path, required=True),
            "sources": actual_sources,
        }
    )


def legacy_science_epoch_change(
    repo_root: Path,
    *,
    epoch_cache: dict[str, str] | None = None,
) -> str | None:
    """Protect pre-v2 judgments against future premise/policy drift.

    Existing audit snapshots predate the per-judgment premise and policy
    epochs. The immutable deployment baseline records both governed epochs as
    installed when v2 was introduced. Once either moves, any still-legacy
    judgment must receive a fresh audit (or a separately reviewed provenance
    migration) instead of silently inheriting changed axioms or dependency
    criteria.
    """
    baseline_path = (
        repo_root
        / "docs"
        / "audit"
        / "data"
        / "legacy_science_epoch_baseline.json"
    )
    baseline = _load_json_object(
        baseline_path,
        "legacy science-epoch baseline",
    )
    expected_framework = baseline.get("framework_premise_epoch_digest")
    expected_policy = baseline.get("dependency_policy_epoch_digest")
    if (
        baseline.get("schema") != "legacy_science_epoch_baseline_v1"
        or not isinstance(expected_framework, str)
        or not _SHA256_RE.fullmatch(expected_framework)
        or not isinstance(expected_policy, str)
        or not _SHA256_RE.fullmatch(expected_policy)
    ):
        raise ScienceFingerprintError(
            "legacy science-epoch baseline is malformed; do not refresh "
            "it to silence premise or policy drift"
        )
    if _epoch_value(
        repo_root,
        epoch_cache,
        "framework_premise_epoch",
        framework_premise_epoch,
    ) != expected_framework:
        return "legacy_framework_premise_epoch_changed"
    if _epoch_value(
        repo_root,
        epoch_cache,
        "dependency_policy_epoch",
        dependency_policy_epoch,
    ) != expected_policy:
        return "legacy_dependency_policy_epoch_changed"
    return None


def _declared_input_state(runner_path: Path, repo_root: Path) -> dict[str, Any]:
    # Import lazily so this module remains usable by small migration tools that
    # set up the repository script path after import.
    import runner_cache

    declared = runner_cache.declared_input_paths(runner_path)
    if declared == ():
        raise ScienceFingerprintError(
            f"invalid AUDIT_INPUT_PATHS declaration: {runner_path}"
        )
    if declared is None:
        return {
            "declared_input_paths": None,
            "declared_input_fingerprint_sha256": None,
            "declared_inputs": [],
        }

    digest = hashlib.sha256()
    digest.update(b"runner-cache-input-fingerprint-v1\0")
    inputs: list[dict[str, str]] = []
    for relative in declared:
        source_path = repo_root / relative
        try:
            body = source_path.read_bytes()
        except OSError as exc:
            raise ScienceFingerprintError(
                f"declared runner input is unreadable: {relative}"
            ) from exc
        relative_bytes = relative.encode("utf-8")
        digest.update(len(relative_bytes).to_bytes(8, "big"))
        digest.update(relative_bytes)
        digest.update(len(body).to_bytes(8, "big"))
        digest.update(body)
        inputs.append(
            {
                "path": relative,
                "sha256": hashlib.sha256(body).hexdigest(),
            }
        )
    return {
        "declared_input_paths": list(declared),
        "declared_input_fingerprint_sha256": digest.hexdigest(),
        "declared_inputs": inputs,
    }


def _runner_state(path: str, role: str, repo_root: Path) -> dict[str, Any]:
    absolute = repo_root / path
    source_sha = _file_sha256(absolute)
    state: dict[str, Any] = {
        "role": role,
        "path": path,
        "present": source_sha is not None,
        "sha256": source_sha,
        "declared_input_paths": None,
        "declared_input_fingerprint_sha256": None,
        "declared_inputs": [],
    }
    if source_sha is not None:
        state.update(_declared_input_state(absolute, repo_root))
    return state


def build_science_fingerprint(
    row: dict,
    rows: dict[str, dict],
    repo_root: Path,
    *,
    epoch_cache: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Build the exact scientific-input baseline for one audit judgment."""
    claim_id = row.get("claim_id")
    note_path = row.get("note_path")
    if not isinstance(claim_id, str) or not claim_id:
        raise ScienceFingerprintError("audit row has no claim_id")
    if not isinstance(note_path, str) or not note_path:
        raise ScienceFingerprintError(f"audit row {claim_id} has no note_path")

    registry = _premise_registry(repo_root)
    accepted_ids = set(registry["canonical_ids"])
    non_evidence_ids = _non_evidence_context_ids(repo_root)
    deps = sorted(row.get("deps") or [])
    if not all(isinstance(dep, str) and dep for dep in deps):
        raise ScienceFingerprintError(f"audit row {claim_id} has invalid dependencies")
    if len(deps) != len(set(deps)):
        raise ScienceFingerprintError(f"audit row {claim_id} has duplicate dependencies")

    dependency_states: list[dict[str, Any]] = []
    for dep_id in deps:
        dep = rows.get(dep_id)
        dep_path = dep.get("note_path") if isinstance(dep, dict) else None
        dependency_states.append(
            {
                "claim_id": dep_id,
                "present": isinstance(dep, dict),
                "note_path": dep_path,
                "note_sha256": (
                    _file_sha256(repo_root / dep_path)
                    if isinstance(dep_path, str) and dep_path
                    else None
                ),
                "ledger_note_hash": (
                    dep.get("note_hash") if isinstance(dep, dict) else None
                ),
                "claim_type": (
                    dep.get("claim_type") if isinstance(dep, dict) else None
                ),
                "claim_scope": (
                    dep.get("claim_scope") if isinstance(dep, dict) else None
                ),
                "effective_status": (
                    dep.get("effective_status") if isinstance(dep, dict) else None
                ),
                "premise_classification": premise_classification(
                    dep_id,
                    accepted_premise_ids=accepted_ids,
                    non_evidence_context_ids=non_evidence_ids,
                ),
            }
        )

    runners: list[dict[str, Any]] = []
    primary = row.get("runner_path")
    if isinstance(primary, str) and primary:
        runners.append(_runner_state(primary, "primary", repo_root))
    helpers = sorted(set(row.get("helper_runner_paths") or []))
    if not all(isinstance(path, str) and path for path in helpers):
        raise ScienceFingerprintError(f"audit row {claim_id} has invalid helper paths")
    runners.extend(_runner_state(path, "helper", repo_root) for path in helpers)

    body: dict[str, Any] = {
        "schema": SCIENCE_FINGERPRINT_SCHEMA,
        "target": {
            "claim_id": claim_id,
            "note_path": note_path,
            "note_sha256": _file_sha256(repo_root / note_path, required=True),
            "ledger_note_hash": row.get("note_hash"),
            "claim_type": row.get("claim_type"),
            "claim_scope": row.get("claim_scope"),
        },
        "dependencies": dependency_states,
        "runners": runners,
        "framework_premise_epoch": _epoch_value(
            repo_root,
            epoch_cache,
            "framework_premise_epoch",
            framework_premise_epoch,
        ),
        "dependency_policy_epoch": _epoch_value(
            repo_root,
            epoch_cache,
            "dependency_policy_epoch",
            dependency_policy_epoch,
        ),
    }
    body["digest"] = _digest(body)
    return body


def science_fingerprint_problems(value: object) -> list[str]:
    if not isinstance(value, dict):
        return ["fingerprint:not_object"]
    problems: list[str] = []
    if value.get("schema") != SCIENCE_FINGERPRINT_SCHEMA:
        problems.append("schema:not_science_fingerprint_v2")
    if not isinstance(value.get("target"), dict):
        problems.append("target:not_object")
    if not isinstance(value.get("dependencies"), list):
        problems.append("dependencies:not_list")
    if not isinstance(value.get("runners"), list):
        problems.append("runners:not_list")
    if not (
        isinstance(value.get("framework_premise_epoch"), str)
        and _SHA256_RE.fullmatch(value["framework_premise_epoch"])
    ):
        problems.append("framework_premise_epoch:not_sha256")
    if not (
        isinstance(value.get("dependency_policy_epoch"), str)
        and _SHA256_RE.fullmatch(value["dependency_policy_epoch"])
    ):
        problems.append("dependency_policy_epoch:not_sha256")
    digest = value.get("digest")
    if not isinstance(digest, str) or not _SHA256_RE.fullmatch(digest):
        problems.append("digest:not_sha256")
    elif digest != _digest({k: v for k, v in value.items() if k != "digest"}):
        problems.append("digest:mismatch")
    return problems


def science_fingerprint_change(
    before: object,
    after: object,
) -> str | None:
    """Return a typed scientific drift reason, or ``None`` for exact equality."""
    before_problems = science_fingerprint_problems(before)
    if before_problems:
        return "science_fingerprint_invalid:" + ",".join(before_problems[:3])
    after_problems = science_fingerprint_problems(after)
    if after_problems:
        return "science_fingerprint_current_invalid:" + ",".join(after_problems[:3])
    assert isinstance(before, dict) and isinstance(after, dict)
    if before["digest"] == after["digest"]:
        return None
    if before["framework_premise_epoch"] != after["framework_premise_epoch"]:
        return "science_changed:framework_premise_epoch"
    if before["dependency_policy_epoch"] != after["dependency_policy_epoch"]:
        return "science_changed:dependency_policy_epoch"
    if before["target"] != after["target"]:
        return "science_changed:target_source"

    before_deps = {
        item.get("claim_id"): item
        for item in before["dependencies"]
        if isinstance(item, dict)
    }
    after_deps = {
        item.get("claim_id"): item
        for item in after["dependencies"]
        if isinstance(item, dict)
    }
    if set(before_deps) != set(after_deps):
        return "science_changed:dependency_membership"
    dependency_fields = (
        "present",
        "note_path",
        "note_sha256",
        "ledger_note_hash",
        "claim_type",
        "claim_scope",
        "effective_status",
        "premise_classification",
    )
    for dep_id in sorted(before_deps):
        for field in dependency_fields:
            if before_deps[dep_id].get(field) != after_deps[dep_id].get(field):
                return f"science_changed:dependency:{dep_id}:{field}"
    if before["runners"] != after["runners"]:
        return "science_changed:runner_or_declared_input"
    return "science_changed:unclassified"


def packet_policy_fingerprint(repo_root: Path) -> dict[str, str]:
    """Fingerprint packet-generation/validation policy separately from science."""
    paths = (
        "docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md",
        "docs/audit/scripts/apply_audit.py",
        "docs/audit/scripts/audit_contract.py",
        "docs/audit/scripts/no_go_discipline_gate.py",
        "docs/audit/scripts/orchestrate_audit_loop.py",
        "docs/ai_methodology/skills/audit-loop/SKILL.md",
        "scripts/codex_audit_runner.py",
    )
    sources = {
        path: _file_sha256(repo_root / path, required=True)
        for path in paths
    }
    body = {
        "schema": PACKET_POLICY_FINGERPRINT_SCHEMA,
        "sources": sources,
    }
    return {**body, "digest": _digest(body)}


def _without_packet(value: object) -> object:
    """Remove supplemental packet material while retaining seat judgments."""
    if isinstance(value, dict):
        return {
            key: _without_packet(item)
            for key, item in value.items()
            if key != "no_go_discipline"
        }
    if isinstance(value, list):
        return [_without_packet(item) for item in value]
    return value


def judgment_fingerprint(row: dict) -> dict[str, Any]:
    """Freeze the prior scientific judgment independently of its N1-N8 packet."""
    fields = (
        "audit_status",
        "audit_date",
        "auditor",
        "auditor_family",
        "auditor_model",
        "auditor_reasoning_effort",
        "audit_invocation_id",
        "independence",
        "claim_type",
        "claim_scope",
        "claim_type_provenance",
        "load_bearing_step",
        "load_bearing_step_class",
        "chain_closes",
        "chain_closure_explanation",
        "verdict_rationale",
        "notes_for_re_audit_if_any",
        "open_dependency_paths",
        "decoration_parent_claim_id",
        "auditor_confidence",
        "negative_assertion_classes",
        "runner_check_breakdown",
        "cross_confirmation",
    )
    body: dict[str, Any] = {
        "schema": JUDGMENT_FINGERPRINT_SCHEMA,
        "claim_id": row.get("claim_id"),
        "judgment": _without_packet(
            {field: row.get(field) for field in fields}
        ),
    }
    body["digest"] = _digest(body)
    return body


def judgment_fingerprint_problems(value: object) -> list[str]:
    if not isinstance(value, dict):
        return ["judgment_fingerprint:not_object"]
    problems: list[str] = []
    if value.get("schema") != JUDGMENT_FINGERPRINT_SCHEMA:
        problems.append("schema:not_frozen_audit_judgment_v1")
    if not isinstance(value.get("claim_id"), str) or not value.get("claim_id"):
        problems.append("claim_id:invalid")
    if not isinstance(value.get("judgment"), dict):
        problems.append("judgment:not_object")
    digest = value.get("digest")
    if not isinstance(digest, str) or not _SHA256_RE.fullmatch(digest):
        problems.append("digest:not_sha256")
    elif digest != _digest({k: v for k, v in value.items() if k != "digest"}):
        problems.append("digest:mismatch")
    return problems


def judgment_fingerprint_change(before: object, row: dict) -> str | None:
    problems = judgment_fingerprint_problems(before)
    if problems:
        return "judgment_fingerprint_invalid:" + ",".join(problems[:3])
    assert isinstance(before, dict)
    current = judgment_fingerprint(row)
    if before["digest"] == current["digest"]:
        return None
    return "audit_judgment_changed_without_new_fingerprint"


def refresh_dependency_policy_manifest(
    repo_root: Path,
    *,
    epoch: str | None = None,
) -> dict:
    """Recompute the controlled manifest under the current governed-hash rule.

    This is the reviewed apply-and-write refresh path: it reuses
    ``dependency_policy_source_sha256`` (the same single producer the epoch
    gate compares against), so a refreshed manifest matches the gate by
    construction.  It preserves the manifest's schema and description and
    only replaces the source hashes, plus the epoch label when a new one is
    supplied.  Refreshing the manifest is itself a policy-epoch move: every
    stored science fingerprint and the legacy deployment baseline keep the
    old digest, so run it only inside a reviewed policy pass.
    """
    manifest_path = _dependency_policy_manifest_path(repo_root)
    manifest = _load_json_object(manifest_path, "dependency-policy epoch")
    if manifest.get("schema") != "dependency_policy_epoch_manifest_v1":
        raise ScienceFingerprintError(
            "dependency-policy epoch manifest has an unsupported schema; "
            "refusing to refresh"
        )
    if epoch is not None:
        if not isinstance(epoch, str) or not epoch:
            raise ScienceFingerprintError("epoch label must be a non-empty string")
        manifest["epoch"] = epoch
    if not isinstance(manifest.get("epoch"), str) or not manifest["epoch"]:
        raise ScienceFingerprintError(
            "dependency-policy epoch manifest has no epoch label"
        )
    manifest["sources"] = {
        path: dependency_policy_source_sha256(repo_root, path)
        for path in DEPENDENCY_POLICY_SOURCES
    }
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Inspect the governed science epochs, or refresh the "
            "dependency-policy epoch manifest under the current rule "
            "(reviewed policy passes only)."
        )
    )
    parser.add_argument(
        "--refresh-dependency-policy-manifest",
        action="store_true",
        help=(
            "Recompute docs/audit/data/dependency_policy_epoch.json from the "
            "governed sources and write it in place."
        ),
    )
    parser.add_argument(
        "--epoch",
        default=None,
        help=(
            "New epoch label to record while refreshing "
            "(requires --refresh-dependency-policy-manifest)."
        ),
    )
    args = parser.parse_args(argv)
    repo_root = Path(__file__).resolve().parents[3]
    if args.refresh_dependency_policy_manifest:
        manifest = refresh_dependency_policy_manifest(repo_root, epoch=args.epoch)
        print(f"dependency-policy manifest refreshed: epoch={manifest['epoch']}")
        print(f"dependency_policy_epoch: {dependency_policy_epoch(repo_root)}")
        return 0
    if args.epoch is not None:
        parser.error("--epoch requires --refresh-dependency-policy-manifest")
    print(f"framework_premise_epoch: {framework_premise_epoch(repo_root)}")
    print(f"dependency_policy_epoch: {dependency_policy_epoch(repo_root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
