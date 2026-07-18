#!/usr/bin/env python3
"""Static integrity certificate for the 2026-07-13--18 TOE campaign archive."""

from __future__ import annotations

import ast
import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HISTORY = ROOT / "docs/work_history/repo/review_feedback"
DATE_PATTERN = re.compile(r"2026-07-(?:13|14|15|16|17|18)")
EXPECTED_HISTORY = 417
EXPECTED_SCRIPTS = 469
EXPECTED_PATH_DIGEST = (
    "981c928ffdc00f4a333b8c6b61f86c54b385c67af4f1efb426df12287e411584"
)
EXPECTED_CONTENT_DIGEST = (
    "303f193162f206a286e8ea2d69b14e83c9c9ae02e1295784fb34417d762a6d4f"
)
UNDATED_HISTORY = (
    "REST_INERTIAL_LAPSE_SOURCE_TRIANGLE_CYCLE204_NO_GO_LEDGER.md",
)
PACKAGING_HISTORY = {
    "TOE_BRIDGE_CAMPAIGN_LANDING_MANIFEST_2026-07-18.md",
}
BASE_HELPERS = {
    "audit_companion_minimal_axioms_clean_base_exact.py",
    "toe_bridge_campaign_archive_integrity_2026_07_18.py",
    "vocab_lint.py",
}
STANDALONE_ARCHIVE_SCRIPTS = {
    "common_m64_fixed_seam_synthesis_cycle311_2026_07_18.py",
    "compact_five_literal_membership_bind_cycle183_2026_07_16.py",
    "extensional_nearest_neighbor_rule_deep_probe_2026_07_13.py",
    "frontier_admissibility_record_continuation_refinement_2026_07_13.py",
    "generated_finite_composition_minimality_2026_07_13.py",
    "higher_number_fixed_seam_synthesis_cycle308_2026_07_17.py",
    "local_instrument_to_record_close_tournament_cycle279_2026_07_17.py",
    "local_m2_mass_scalar_deformation_response_route_b_2026_07_17.py",
    "observable_specific_wilson_blindness_cycle274_2026_07_17.py",
    "physical_signed_row_egress_cycle167_2026_07_16.py",
    "read_twice_packet_derive_first_unification_2026_07_13.py",
}
CANONICAL_NOTES = (
    "ADMISSIBILITY_RECORD_CONTINUATION_REFINEMENT_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-13.md",
    "EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md",
    "GENERATED_FINITE_COMPOSITION_MINIMALITY_THEOREM_2026-07-13.md",
    "READ_RESET_CADENCE_INTERFERENCE_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-17.md",
    "READ_TWICE_PACKET_DERIVE_FIRST_UNIFICATION_BOUNDED_NOTE_2026-07-13.md",
)
FORBIDDEN_PACKAGE_PATHS = (
    ".claude/science/physics-loops/read-twice-unification-20260713/REVIEW_HISTORY.md",
    ".claude/science/physics-loops/read-twice-unification-20260713/STATE.yaml",
    "logs/runner-cache/read_twice_packet_derive_first_unification_2026_07_13.txt",
)
RUNNER_TOKEN = re.compile(r"scripts/([A-Za-z0-9_./-]+\.py)")
MARKDOWN_PY_LINK = re.compile(r"\]\(([^)]+\.py)(?:#[^)]+)?\)")

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def local_import_names(tree: ast.AST) -> set[str]:
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module.split(".")[0])
    return names


def archive_inventory() -> tuple[list[Path], list[Path], list[tuple[Path, str]]]:
    history = sorted(
        path
        for path in HISTORY.glob("*.md")
        if DATE_PATTERN.search(path.name) and path.name not in PACKAGING_HISTORY
    )
    history.extend(HISTORY / name for name in UNDATED_HISTORY)
    history = sorted(set(history))

    modules = {path.stem: path for path in (ROOT / "scripts").glob("*.py")}
    history_text = "\n".join(path.read_text(encoding="utf-8") for path in history)
    scripts = {path for path in modules.values() if path.name in history_text}
    parse_failures: list[tuple[Path, str]] = []

    changed = True
    while changed:
        changed = False
        for path in tuple(scripts):
            try:
                tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            except (OSError, SyntaxError) as error:
                parse_failures.append((path, str(error)))
                continue
            for name in local_import_names(tree):
                dependency = modules.get(name)
                if dependency is not None and dependency not in scripts:
                    scripts.add(dependency)
                    changed = True

    scripts = {path for path in scripts if path.name not in BASE_HELPERS}
    scripts.update(ROOT / "scripts" / name for name in STANDALONE_ARCHIVE_SCRIPTS)
    return history, sorted(scripts), parse_failures


def digests(paths: list[Path]) -> tuple[str, str]:
    path_hash = hashlib.sha256()
    content_hash = hashlib.sha256()
    for path in sorted(paths, key=lambda item: str(item.relative_to(ROOT))):
        relative = str(path.relative_to(ROOT))
        body = path.read_bytes()
        body_hash = hashlib.sha256(body).hexdigest()
        path_hash.update(relative.encode("utf-8") + b"\n")
        content_hash.update(
            relative.encode("utf-8")
            + b"\0"
            + body_hash.encode("ascii")
            + b"\n"
        )
    return path_hash.hexdigest(), content_hash.hexdigest()


def runner_reference_failures(notes: list[Path]) -> list[tuple[str, str]]:
    failures: set[tuple[str, str]] = set()
    for note in notes:
        body = note.read_text(encoding="utf-8")
        for target in RUNNER_TOKEN.findall(body):
            path = ROOT / "scripts" / target
            if not path.exists():
                failures.add((str(note.relative_to(ROOT)), f"scripts/{target}"))
        for target in MARKDOWN_PY_LINK.findall(body):
            path = (note.parent / target).resolve()
            if not path.exists():
                failures.add((str(note.relative_to(ROOT)), target))
    return sorted(failures)


def main() -> int:
    history, scripts, early_parse_failures = archive_inventory()
    check(
        "archive history count",
        len(history) == EXPECTED_HISTORY,
        {"expected": EXPECTED_HISTORY, "observed": len(history)},
    )
    check(
        "archive script count",
        len(scripts) == EXPECTED_SCRIPTS,
        {"expected": EXPECTED_SCRIPTS, "observed": len(scripts)},
    )
    check(
        "every archived path exists",
        all(path.exists() for path in history + scripts),
        [str(path) for path in history + scripts if not path.exists()],
    )

    parse_failures = list(early_parse_failures)
    local_import_failures: list[tuple[str, str]] = []
    modules = {path.stem: path for path in (ROOT / "scripts").glob("*.py")}
    for path in scripts:
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (OSError, SyntaxError) as error:
            parse_failures.append((path, str(error)))
            continue
        for name in local_import_names(tree):
            dependency = modules.get(name)
            if dependency is not None and not dependency.exists():
                local_import_failures.append((str(path.relative_to(ROOT)), name))
    check("all archive scripts parse", not parse_failures, parse_failures)
    check(
        "all local Python imports resolve",
        not local_import_failures,
        local_import_failures,
    )

    reference_failures = runner_reference_failures(history)
    check(
        "every historical runner reference resolves",
        not reference_failures,
        reference_failures,
    )

    path_digest, content_digest = digests(history + scripts)
    check(
        "archive path digest",
        path_digest == EXPECTED_PATH_DIGEST,
        {"expected": EXPECTED_PATH_DIGEST, "observed": path_digest},
    )
    check(
        "archive content digest",
        content_digest == EXPECTED_CONTENT_DIGEST,
        {"expected": EXPECTED_CONTENT_DIGEST, "observed": content_digest},
    )

    canonical_paths = [ROOT / "docs" / name for name in CANONICAL_NOTES]
    canonical_reference_failures = runner_reference_failures(canonical_paths)
    check(
        "canonical notes exist and declare bounded theorem scope",
        all(
            path.exists()
            and (
                "**Type:** bounded_theorem" in path.read_text(encoding="utf-8")
                or "**Claim type:** bounded_theorem"
                in path.read_text(encoding="utf-8")
            )
            for path in canonical_paths
        ),
    )
    check(
        "every canonical runner reference resolves",
        not canonical_reference_failures,
        canonical_reference_failures,
    )
    check(
        "branch state and runner cache are absent",
        all(not (ROOT / path).exists() for path in FORBIDDEN_PACKAGE_PATHS),
        [path for path in FORBIDDEN_PACKAGE_PATHS if (ROOT / path).exists()],
    )

    print(
        f"SUMMARY history={len(history)} scripts={len(scripts)} "
        f"PASS={PASS} FAIL={FAIL}"
    )
    print(
        "BOUNDARY: static package integrity only; no runner PASS, physics claim, "
        "audit verdict, or constitutional conclusion is created"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
