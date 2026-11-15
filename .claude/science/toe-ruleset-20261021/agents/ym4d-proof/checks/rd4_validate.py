"""RD4 provenance/document checks only; this is not a scientific test runner."""

from __future__ import annotations

import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def permitted(name: str) -> bool:
    return name in {"RD4.md", "RD4_LOG.md"} or name.startswith("checks/rd4_")


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    output_name = "checks/rd4_validation.json"
    baseline_path = root / "checks/rd4_input_manifest.json"
    baseline = json.loads(baseline_path.read_text())
    current = {
        str(path.relative_to(root)): digest(path)
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }
    missing = sorted(set(baseline["files"]) - set(current))
    changed = sorted(
        name for name, old in baseline["files"].items()
        if name in current and current[name] != old
    )
    added = sorted(set(current) - set(baseline["files"]))
    forbidden = [name for name in added if not permitted(name)]
    required = ["RD4.md", "RD4_LOG.md", "checks/rd4_review.md"]
    absent_outputs = [name for name in required if name not in current]
    link_errors = []
    table_errors = []
    for name in required:
        if name in absent_outputs:
            continue
        expected_separators = None
        fenced = False
        for line_number, line in enumerate((root / name).read_text().splitlines(), 1):
            if line.startswith("```"):
                fenced = not fenced
                continue
            if fenced or line.startswith("    "):
                continue
            if line.startswith("|"):
                separators = len(re.findall(r"(?<!\\)\|", line))
                if expected_separators is None:
                    expected_separators = separators
                if separators != expected_separators:
                    table_errors.append([name, line_number, separators, expected_separators])
            else:
                expected_separators = None
            for target in re.findall(r"\]\(([^)]+)\)", line):
                if "://" in target or target.startswith("#"):
                    continue
                relative_path = target.split("#")[0].strip("<>")
                candidate = (root / name).parent.joinpath(relative_path)
                # This invocation creates its own receipt after checking inputs.
                if not candidate.exists() and candidate.resolve() != (root / output_name).resolve():
                    link_errors.append([name, line_number, target])

    science = (root / "RD4.md").read_text()
    labels = []
    for line in science.splitlines():
        if line.startswith("    "):
            match = re.search(r"\(([CLKI]\d+[a-z]?)\)\s*$", line)
            if match:
                labels.append(match.group(1))
    expected_labels = (
        {f"C{i}" for i in range(1, 12)} | {"C3a", "C3b"}
        | {f"L{i}" for i in range(1, 11)}
        | {f"K{i}" for i in range(1, 4)}
        | {f"I{i}" for i in range(1, 5)}
    )
    label_errors = {
        "missing": sorted(expected_labels - set(labels)),
        "unexpected": sorted(set(labels) - expected_labels),
        "duplicates": sorted({label for label in labels if labels.count(label) > 1}),
    }
    review_path = root / "checks/rd4_review.md"
    review = review_path.read_text() if review_path.exists() else ""
    source_bound = current["RD4.md"] in review
    last_line = review.strip().splitlines()[-1] if review.strip() else ""
    verdict_present = last_line in {"VERDICT: LAND", "VERDICT: HOLD"}
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    tracked_diff = subprocess.check_output(["git", "diff", "--name-only", "HEAD"], cwd=root, text=True).splitlines()
    errors = any([
        missing, changed, forbidden, absent_outputs, link_errors, table_errors,
        any(label_errors.values()), not source_bound, not verdict_present,
        head != baseline["head"], tracked_diff,
    ])
    receipt = {
        "kind": "provenance_and_document_structure_only",
        "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "scientific_numerics_executed": False,
        "mathematical_verification": "Written proofs and the separately bound reviewer report; not this script.",
        "head": head,
        "baseline_head": baseline["head"],
        "baseline_file_count": len(baseline["files"]),
        "changed_preexisting_files": changed,
        "missing_preexisting_files": missing,
        "added_files_including_this_receipt": sorted(set(added) | {output_name}),
        "forbidden_additions": forbidden,
        "absent_outputs": absent_outputs,
        "link_errors": link_errors,
        "table_errors": table_errors,
        "equation_label_errors": label_errors,
        "review_binds_current_science": source_bound,
        "review_last_line": last_line,
        "tracked_diff_paths": tracked_diff,
        "artifact_sha256": {
            name: current[name] for name in [
                *required, "checks/rd4_input_manifest.json", "checks/rd4_validate.py"
            ] if name in current
        },
        "checks_satisfied": not errors,
    }
    (root / output_name).write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "receipt": str(root / output_name),
        "checks_satisfied": not errors,
        "baseline_file_count": len(baseline["files"]),
        "science_sha256": current["RD4.md"],
        "review_last_line": last_line,
        "errors": {
            "changed": changed, "missing": missing, "forbidden": forbidden,
            "absent_outputs": absent_outputs, "links": link_errors, "tables": table_errors,
            "labels": label_errors,
        },
    }, indent=2))
    return int(errors)


if __name__ == "__main__":
    raise SystemExit(main())
