#!/usr/bin/env python3
"""Build the citation graph from all docs/*.md notes.

Walks every .md file under docs/ (excluding docs/audit/), extracts:
  - claim_id (stable, derived from path)
  - title (first H1)
  - optional Claim type: hint for auditor-owned claim_type
  - optional legacy Status-line migration hint for claim_type backfill
  - cited authorities (markdown links to other .md files in docs/)
  - primary runner script path
  - helper runner script paths (transitive `from scripts.X import` imports
    of the primary runner; needed by the audit packet builder so the
    auditor sees the full source chain and doesn't fall back to class C
    on missing-helper grounds)
  - note hash (sha256 of body)

Writes docs/audit/data/citation_graph.json.

This script is deterministic, offline, and read-only against the docs.
"""
from __future__ import annotations

import ast
import hashlib
import json
import re
import urllib.parse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
DOCS_DIR = REPO_ROOT / "docs"
AUDIT_DATA_DIR = REPO_ROOT / "docs" / "audit" / "data"
OUTPUT_PATH = AUDIT_DATA_DIR / "citation_graph.json"

# Skip the audit lane itself and generated publication views.
SKIP_PREFIXES = ("audit/",)
GENERATED_PUBLICATION_FILES = {"PUBLICATION_AUDIT_DIVERGENCE.md"}
GENERATED_PUBLICATION_SUFFIXES = ("_EFFECTIVE_STATUS.md",)

# Legacy Status-line normalization is used only as a temporary migration hint
# for seeding claim_type on rows that predate Type: metadata. It is not emitted
# as an audit authority field.
LEGACY_STATUS_TO_CLAIM_TYPE_PATTERNS = [
    (re.compile(r"\b(?:proposed[_ -]no[_ -]?go|retained[_ -]no[_ -]?go|no-?go)\b", re.IGNORECASE), "no_go"),
    (re.compile(r"\bbounded\b", re.IGNORECASE), "bounded_theorem"),
    (re.compile(r"\b(open|scaffold|planning)\b", re.IGNORECASE), "open_gate"),
    (re.compile(r"\b(?:proposed[_ -]retained|proposed[_ -]promoted|retained|promoted|flagship\s+closed|support|accepted|derived|outside\s+audit-ratified\s+tier|superseded_by)\b", re.IGNORECASE), "positive_theorem"),
]

LEGACY_STATUS_LINE_RE = re.compile(
    r"^\s*(?:\*\*Status:?\*\*|Status:)\s*(.+)$",
    re.IGNORECASE | re.MULTILINE,
)
CLAIM_TYPE_LINE_RE = re.compile(
    r"^\s*(?:\*\*Claim type:?\*\*|Claim type:)\s*(.+)$",
    re.IGNORECASE | re.MULTILINE,
)
TYPE_LINE_RE = re.compile(
    r"^\s*(?:\*\*Type:?\*\*|Type:)\s*(.+)$",
    re.IGNORECASE | re.MULTILINE,
)
CLAIM_TYPES = {
    "positive_theorem",
    "bounded_theorem",
    "no_go",
    "open_gate",
    "decoration",
    "meta",
}
TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
RUNNER_LABEL_RE = re.compile(
    r"^\s*(?:[-*]\s*)?"
    r"(?:\*\*(?:Primary runner|Primary runners|Primary artifact|Primary artifacts|Primary files|"
    r"Derivation runner|Source runner|Source runners|Script|Scripts|Runner|Runners|"
    r"Files|Harnesses):?\*\*|"
    r"Primary runner:|Primary runners:|Primary artifact:|Primary artifacts:|"
    r"Derivation runner:|Source runner:|Source runners:|Script:|Scripts:|Runner:|Runners:|"
    r"Files:|Harnesses:)\s*",
    re.IGNORECASE,
)
RUNNER_PATH_RE = re.compile(
    r"(scripts/[A-Za-z0-9_./\-]+\.py)|(?<![A-Za-z0-9_./\-])([A-Za-z0-9_.\-]+\.py)"
)
RUNNER_SECTION_RE = re.compile(
    r"^#{2,6}\s+(?:(?:Primary|Key|Audited|New|Source|Validated|Corrected(?:\s+live)?)\s+)?"
    r"(?:Artifact(?:\s+chain)?|Artifacts|Script|Scripts|Runner|Runners|Files|Surfaces|What\s+was\s+tested)\b.*$",
    re.IGNORECASE | re.MULTILINE,
)
HEADING_RE = re.compile(r"^#{1,6}\s+", re.MULTILINE)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s#]+\.md)(?:#[^)]*)?\)")

EXPLICIT_PACKET_HELPER_RUNNER_PATHS = {
    # The atomic work-history note's primary runner is a packet verifier. Its
    # load-bearing companion sources are certified by that verifier but are not
    # imports, so list them explicitly for the restricted audit packet.
    "work_history.atomic.hydrogen_helium_atomic_companion_note_2026-04-18": [
        "scripts/frontier_atomic_hydrogen_lattice_companion.py",
        "scripts/frontier_atomic_helium_hartree_companion.py",
        "scripts/frontier_atomic_helium_jastrow_companion.py",
        "scripts/frontier_hydrogen_helium_atomic_lattice_kinetic_dependency_narrow_repair_verifier.py",
    ],
    # This wrapper row exists specifically to expose helpers loaded through
    # `_frontier_loader.load_frontier(...)`; AST import discovery cannot see
    # those dynamic loads, but the helpers are one-hop packet sources.
    "one_parameter_reduced_shell_law_helpers_umbrella_note_2026-04-13": [
        "scripts/frontier_star_shell_projector.py",
        "scripts/frontier_same_source_metric_ansatz_scan.py",
        "scripts/frontier_coarse_grained_exterior_law.py",
        "scripts/frontier_sewing_shell_source.py",
        "scripts/frontier_radial_shell_matching_law.py",
    ],
}


AXIOM_PREMISE_NODES_PATH = AUDIT_DATA_DIR / "axiom_premise_nodes.json"


def _load_axiom_premise_path_map() -> dict[str, str]:
    """Map repo-relative source path -> canonical un-dated claim_id.

    Lets a re-datable axiom doc (e.g. MINIMAL_AXIOMS_2026-05-20.md) keep a
    stable claim_id (`minimal_axioms`) so inbound citation edges and the
    axiom-premise status survive re-dating. Allowlist only; see
    docs/audit/data/axiom_premise_nodes.json.
    """
    if not AXIOM_PREMISE_NODES_PATH.exists():
        return {}
    try:
        data = json.loads(AXIOM_PREMISE_NODES_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}
    out: dict[str, str] = {}
    for canonical_id, entry in (data.get("nodes") or {}).items():
        for p in entry.get("aliased_paths", []):
            out[str(p)] = canonical_id
    return out


_AXIOM_PREMISE_PATH_MAP: dict[str, str] | None = None


def _axiom_premise_path_map() -> dict[str, str]:
    global _AXIOM_PREMISE_PATH_MAP
    if _AXIOM_PREMISE_PATH_MAP is None:
        _AXIOM_PREMISE_PATH_MAP = _load_axiom_premise_path_map()
    return _AXIOM_PREMISE_PATH_MAP


def claim_id_from_path(path: Path) -> str:
    """Stable claim_id from doc path: docs/X/Y.md -> X.Y (stem, lowercase).

    Allowlisted axiom-premise source paths are canonicalized to their
    stable un-dated id (see docs/audit/data/axiom_premise_nodes.json).
    """
    rel_repo = path.resolve().relative_to(REPO_ROOT).as_posix()
    canonical = _axiom_premise_path_map().get(rel_repo)
    if canonical is not None:
        return canonical
    rel = path.relative_to(DOCS_DIR)
    parts = list(rel.with_suffix("").parts)
    return ".".join(parts).lower()


def claim_type_from_legacy_status(raw: str | None) -> str | None:
    if not raw:
        return None
    text = raw.strip()
    for pattern, label in LEGACY_STATUS_TO_CLAIM_TYPE_PATTERNS:
        if pattern.search(text):
            return label
    return None


def extract_legacy_status_claim_type(body: str) -> str | None:
    m = LEGACY_STATUS_LINE_RE.search(body)
    if not m:
        return None
    return claim_type_from_legacy_status(m.group(1).strip())


def normalize_claim_type(raw: str | None) -> str | None:
    if not raw:
        return None
    token = raw.strip().split()[0].strip("`*_:.").lower()
    token = token.replace("-", "_")
    if token == "nogo":
        token = "no_go"
    if token in CLAIM_TYPES:
        return token
    phrase = raw.strip().lower().replace("-", " ").replace("_", " ")
    phrase = " ".join(phrase.split())
    aliases = {
        "positive theorem": "positive_theorem",
        "bounded theorem": "bounded_theorem",
        "no go": "no_go",
        "open gate": "open_gate",
    }
    return aliases.get(phrase)


def extract_claim_type_hint(body: str) -> tuple[str | None, str | None]:
    m = CLAIM_TYPE_LINE_RE.search(body) or TYPE_LINE_RE.search(body)
    if not m:
        return None, None
    raw = m.group(1).strip()
    return raw, normalize_claim_type(raw)


def extract_title(body: str) -> str | None:
    m = TITLE_RE.search(body)
    return m.group(1).strip() if m else None


def normalize_runner_path(path: str) -> str | None:
    path = path.strip()
    if not path:
        return None
    candidates: list[str] = []
    raw_path = Path(path)
    if path.startswith("scripts/"):
        candidates.append(path)
    elif not raw_path.is_absolute():
        candidates.extend([path, f"scripts/{path}"])
    basename = raw_path.name
    if basename.endswith(".py"):
        candidates.append(f"scripts/{basename}")

    seen: set[str] = set()
    for candidate in candidates:
        if candidate in seen:
            continue
        seen.add(candidate)
        candidate_path = REPO_ROOT / candidate
        if candidate_path.exists():
            return candidate_path.relative_to(REPO_ROOT).as_posix()
    return None


def runner_paths(text: str) -> list[str]:
    paths: list[str] = []
    for m in RUNNER_PATH_RE.finditer(text):
        raw = m.group(1) or m.group(2)
        if raw:
            path = normalize_runner_path(raw)
            if path:
                paths.append(path)
    return paths


def first_runner_path(text: str) -> str | None:
    paths = runner_paths(text)
    return paths[0] if paths else None


def extract_section(body: str, start: int) -> str:
    m = HEADING_RE.search(body, start)
    end = m.start() if m else len(body)
    return body[start:end]


def _parse_script_imports(script_path: Path) -> set[str]:
    """Return basenames of scripts/*.py that this script imports.

    Handles `from scripts.X import ...`, `from scripts import X [as Y]`,
    `import scripts.X`, relative imports inside `scripts/`
    (`from .X import ...`, `from . import X`), and bare PYTHONPATH-style
    imports (`from X import ...`, `import X`) where `scripts/X.py` exists —
    common in this repo because runners are invoked with
    `PYTHONPATH=scripts python3 scripts/X.py`.

    Filters to imports that exist as scripts/<name>.py, so third-party
    libraries (numpy, scipy, etc.) are excluded.

    Used to compute helper_runner_paths so the audit packet builder can
    include the full source chain. Without this, primary runners that
    import from helpers (e.g. lattice_no_barrier_distance.py importing
    from lattice_mirror_distance) cause the auditor to see opaque
    function references → spurious class-C verdicts on packet
    incompleteness grounds alone.
    """
    if not script_path.exists():
        return set()
    try:
        tree = ast.parse(script_path.read_text(encoding="utf-8"))
    except (SyntaxError, UnicodeDecodeError):
        return set()
    scripts_dir = REPO_ROOT / "scripts"
    helpers: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            module = node.module or ""
            if module.startswith("scripts."):
                helpers.add(module.removeprefix("scripts."))
            elif module == "scripts" and node.level == 0:
                # `from scripts import X [as Y]` -> the imported NAMES are the
                # helper modules (X), not the package `scripts`. Use alias.name
                # (the real module name), never alias.asname (the local alias).
                for alias in node.names:
                    helpers.add(alias.name)
            elif node.level >= 1 and module:
                helpers.add(module)
            elif node.level >= 1 and not module:
                for alias in node.names:
                    helpers.add(alias.name)
            elif module and node.level == 0:
                helpers.add(module.split(".")[0])
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.startswith("scripts."):
                    helpers.add(alias.name.removeprefix("scripts."))
                else:
                    helpers.add(alias.name.split(".")[0])
    return {h for h in helpers if (scripts_dir / f"{h}.py").exists()}


def resolve_helper_runner_paths(primary_runner_path: str | None) -> list[str]:
    """Walk transitive imports from the primary runner; return the full
    set of helper script paths the audit packet must include.

    Returns `scripts/X.py` paths (sorted), excluding the primary itself.
    Empty list if no primary or no helpers. Cycles are handled via a
    seen-set; result is fixed-point of the transitive-closure walk.
    """
    if not primary_runner_path:
        return []
    primary = REPO_ROOT / primary_runner_path
    if not primary.exists():
        return []
    primary_basename = primary.stem
    seen: set[str] = set()
    frontier = _parse_script_imports(primary)
    while frontier:
        new = frontier - seen - {primary_basename}
        if not new:
            break
        seen.update(new)
        next_frontier: set[str] = set()
        for h in new:
            next_frontier.update(
                _parse_script_imports(REPO_ROOT / "scripts" / f"{h}.py")
            )
        frontier = next_frontier - seen - {primary_basename}
    return sorted(f"scripts/{h}.py" for h in seen)


def helper_runner_paths_for_claim(claim_id: str,
                                  primary_runner_path: str | None) -> list[str]:
    """Return packet helper sources for a claim.

    Most helper paths are transitive imports of the primary runner. A small
    number of legacy work-history rows register sibling runner artifacts in
    the source note instead; keep those as explicit packet helpers so the
    restricted audit prompt sees their full source.
    """
    paths: list[str] = []
    for path in resolve_helper_runner_paths(primary_runner_path):
        if path not in paths:
            paths.append(path)
    for path in EXPLICIT_PACKET_HELPER_RUNNER_PATHS.get(claim_id, []):
        if path != primary_runner_path and (REPO_ROOT / path).exists() and path not in paths:
            paths.append(path)
    return paths


def extract_runner(body: str, rel_path: str | None = None) -> str | None:
    if rel_path and rel_path.startswith("ai_methodology/raw/"):
        return None

    lines = body.splitlines()
    for i, line in enumerate(lines):
        if not RUNNER_LABEL_RE.search(line):
            continue
        window = "\n".join(lines[i : i + 4])
        runner = first_runner_path(window)
        if runner:
            return runner

    for m in RUNNER_SECTION_RE.finditer(body):
        runner = first_runner_path(extract_section(body, m.end()))
        if runner:
            return runner

    # Some older cards put the runner name directly in a section heading, e.g.
    # "## 1. Canonical 17-Card (frontier_staggered_17card.py)".
    for line in lines[:120]:
        if line.startswith("#"):
            runner = first_runner_path(line)
            if runner:
                return runner

    if rel_path and not rel_path.startswith(("repo/", "work_history/", "publication/", "lanes/")):
        first_heading = HEADING_RE.search(body)
        preamble = body[: first_heading.start()] if first_heading else "\n".join(lines[:20])
        preamble_paths = list(dict.fromkeys(runner_paths(preamble)))
        if len(preamble_paths) > 1:
            return preamble_paths[0]

    top_paths = list(dict.fromkeys(runner_paths("\n".join(lines[:80]))))
    if len(top_paths) == 1:
        return top_paths[0]

    return None


def resolve_link_target(link_target: str, source_path: Path) -> Path | None:
    """Resolve a markdown link target relative to source_path. Returns
    the resolved path under DOCS_DIR if it lands inside DOCS_DIR, else None.

    Absolute paths from legacy repo locations (e.g. links written against
    /Users/jonreilly/Projects/Physics/docs/...) are rewritten to the
    current REPO_ROOT/docs/ tree by detecting the '/docs/' segment so
    citations survive repo moves and machine renames. URL-encoded
    characters in the link (%20 etc.) are decoded before resolution.
    """
    decoded = urllib.parse.unquote(link_target)
    if decoded.startswith("/"):
        marker = "/docs/"
        idx = decoded.find(marker)
        if idx < 0:
            return None
        candidate = (DOCS_DIR / decoded[idx + len(marker):]).resolve()
    else:
        candidate = (source_path.parent / decoded).resolve()
    try:
        candidate.relative_to(DOCS_DIR)
    except ValueError:
        return None
    if not candidate.exists():
        return None
    return candidate


def extract_citations(body: str, source_path: Path) -> list[Path]:
    seen: dict[Path, None] = {}
    for raw_target in LINK_RE.findall(body):
        target_path = resolve_link_target(raw_target, source_path)
        if target_path is None or target_path == source_path:
            continue
        seen.setdefault(target_path, None)
    return list(seen.keys())


def is_skipped(rel_path: Path) -> bool:
    rel_str = rel_path.as_posix()
    if any(rel_str.startswith(prefix) for prefix in SKIP_PREFIXES):
        return True
    if rel_path.parts[:2] == ("publication", "ci3_z3"):
        if rel_path.name in GENERATED_PUBLICATION_FILES:
            return True
        if rel_path.name.endswith(GENERATED_PUBLICATION_SUFFIXES):
            return True
    return False


def discover_notes() -> list[Path]:
    notes = []
    for path in sorted(DOCS_DIR.rglob("*.md")):
        rel = path.relative_to(DOCS_DIR)
        if is_skipped(rel):
            continue
        notes.append(path)
    return notes


def build_graph() -> dict:
    notes = discover_notes()
    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    path_to_id: dict[Path, str] = {}

    # First pass: register every note as a node.
    for note_path in notes:
        cid = claim_id_from_path(note_path)
        rel = note_path.relative_to(DOCS_DIR)
        body = note_path.read_text(encoding="utf-8", errors="replace")
        raw_type, claim_type_hint = extract_claim_type_hint(body)
        legacy_status_hint = extract_legacy_status_claim_type(body)
        claim_type_seed_hint = claim_type_hint or legacy_status_hint
        primary_runner = extract_runner(body, rel.as_posix())
        nodes[cid] = {
            "claim_id": cid,
            "path": note_path.relative_to(REPO_ROOT).as_posix(),
            "title": extract_title(body),
            "claim_type_author_hint_raw": raw_type,
            "claim_type_author_hint": claim_type_hint,
            "claim_type_seed_hint": claim_type_seed_hint,
            "runner_path": primary_runner,
            "helper_runner_paths": helper_runner_paths_for_claim(cid, primary_runner),
            "note_hash": hashlib.sha256(body.encode("utf-8")).hexdigest(),
            "deps": [],
        }
        path_to_id[note_path] = cid

    # Second pass: resolve citations into deps.
    for note_path in notes:
        cid = path_to_id[note_path]
        body = note_path.read_text(encoding="utf-8", errors="replace")
        for cited_path in extract_citations(body, note_path):
            cited_cid = path_to_id.get(cited_path)
            if cited_cid is None or cited_cid == cid:
                continue
            if cited_cid in nodes[cid]["deps"]:
                continue
            nodes[cid]["deps"].append(cited_cid)
            edges.append({"from": cid, "to": cited_cid})

    # Stats.
    claim_type_hint_counts: dict[str, int] = {}
    claim_type_seed_hint_counts: dict[str, int] = {}
    for n in nodes.values():
        hint = n.get("claim_type_author_hint") or "none"
        claim_type_hint_counts[hint] = claim_type_hint_counts.get(hint, 0) + 1
        seed_hint = n.get("claim_type_seed_hint") or "none"
        claim_type_seed_hint_counts[seed_hint] = claim_type_seed_hint_counts.get(seed_hint, 0) + 1

    runners_with_path = sum(1 for n in nodes.values() if n["runner_path"])
    roots = [cid for cid, n in nodes.items() if not n["deps"]]
    leaves = [cid for cid in nodes if not any(e["to"] == cid for e in edges)]

    return {
        "schema_version": 1,
        "stats": {
            "node_count": len(nodes),
            "edge_count": len(edges),
            "claim_type_author_hint_counts": claim_type_hint_counts,
            "claim_type_seed_hint_counts": claim_type_seed_hint_counts,
            "runners_with_path": runners_with_path,
            "root_count": len(roots),
            "leaf_count": len(leaves),
        },
        "nodes": nodes,
        "edges": edges,
        "roots": sorted(roots),
    }


def main() -> int:
    AUDIT_DATA_DIR.mkdir(parents=True, exist_ok=True)
    graph = build_graph()
    OUTPUT_PATH.write_text(json.dumps(graph, indent=2, sort_keys=True) + "\n")
    s = graph["stats"]
    print(f"Wrote {OUTPUT_PATH.relative_to(REPO_ROOT)}")
    print(f"  nodes: {s['node_count']}  edges: {s['edge_count']}")
    print(f"  roots: {s['root_count']}  leaves: {s['leaf_count']}")
    print(f"  runners attached: {s['runners_with_path']}")
    print(f"  claim_type_seed_hint_counts: {s['claim_type_seed_hint_counts']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
