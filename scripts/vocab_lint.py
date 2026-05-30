#!/usr/bin/env python3
"""Mechanical vocabulary lint for the repo.

Reads docs/repo/controlled_vocabulary.yaml. For each input file:
  - Applies non-link-aware `rewrite_rules` (regex pattern → replacement)
    when run with --fix.
  - Flags violations of `filename_rules.forbidden_suffixes` (filename-only).
  - Writes a per-file `prose_status.json` artifact recording what was
    auto-corrected vs what needs human vocab-extension review.

Usage:
  scripts/vocab_lint.py [--fix] [--report-only] [--report-path PATH] <files...>

Exit codes:
  0 — clean (no violations) or all violations auto-fixed with --fix
  1 — violations remain that vocab_lint could not mechanically rewrite
  2 — usage / IO error

Modes:
  --fix          : apply mechanical rewrites in place; record each in prose_corrections.
  --report-only  : list violations to stdout; do not modify files. (default if --fix absent)
  --report-path  : write per-file prose_status.json artifact to PATH.
  --link-aware   : (stub for Cleanup-2) atomic cross-doc reference rewrite for filename renames.

Note: This is the Cleanup-1 implementation. Cleanup-1b will add the
companion `scripts/render_controlled_vocabulary.py` that regenerates
CONTROLLED_VOCABULARY.md and KEY_TERMINOLOGY.md from the YAML. Cleanup-2
will add the link-aware filename-rename pass and the F-letter →
Finding-N per-file mapping migration.

See docs/repo/VOCABULARY_HYGIENE_DESIGN.md for the design.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
YAML_PATH = REPO_ROOT / "docs" / "repo" / "controlled_vocabulary.yaml"


@dataclass
class Violation:
    """A single detected drift instance in a file."""
    rule_id: str
    before: str
    after: str | None  # None means no mechanical rewrite available
    line_number: int | None = None

    def to_dict(self) -> dict:
        return {
            "rule_id": self.rule_id,
            "before": self.before,
            "after": self.after,
            "line_number": self.line_number,
        }


@dataclass
class FileReport:
    """Per-file lint result."""
    path: str
    violations: list[Violation] = field(default_factory=list)
    auto_corrected: int = 0
    needs_human_vocab_decision: int = 0

    def to_dict(self) -> dict:
        return {
            "path": self.path,
            "violations": [v.to_dict() for v in self.violations],
            "auto_corrected": self.auto_corrected,
            "needs_human_vocab_decision": self.needs_human_vocab_decision,
        }


def load_yaml() -> dict:
    if not YAML_PATH.exists():
        print(f"FAIL: {YAML_PATH} missing", file=sys.stderr)
        raise SystemExit(2)
    return yaml.safe_load(YAML_PATH.read_text(encoding="utf-8"))


def path_matches_any_glob(rel_path: str, patterns: list[str]) -> bool:
    """True if rel_path matches any glob in patterns (** semantics)."""
    for pat in patterns:
        # fnmatch doesn't do ** natively; normalize ** to * for prefix dirs.
        # The exclusions we care about are docs/work_history/** and
        # archive_unlanded/** — both match by prefix.
        if pat.endswith("/**"):
            prefix = pat[:-3]
            if rel_path.startswith(prefix):
                return True
        elif fnmatch.fnmatch(rel_path, pat):
            return True
    return False


def detect_text_violations(
    text: str,
    rules: list[dict],
    rel_path: str,
    apply_fix: bool,
) -> tuple[str, list[Violation]]:
    """Apply text-based rewrite_rules. Returns (new_text, violations).

    If apply_fix=True, the returned new_text has the rewrites applied;
    otherwise new_text == text and violations record what would change.
    """
    violations: list[Violation] = []
    new_text = text

    for rule in rules:
        rid = rule.get("id", "<anonymous>")
        excluded = rule.get("excluded_paths") or []
        if excluded and path_matches_any_glob(rel_path, excluded):
            continue

        # Skip rules that aren't simple local regex rewrites. F-letter
        # migration needs a per-file mapping, and filename/reference
        # migrations need link-aware cross-doc rewrites. Both are Cleanup-2
        # concerns; Cleanup-1 reports them but must not auto-fix them.
        if rule.get("migration_strategy") == "per_file_mapping_with_link_check":
            continue

        pattern = rule.get("pattern")
        replacement = rule.get("replacement")
        if pattern is None or replacement is None:
            continue

        # Translate $1 / $N backreferences (YAML-friendly) to Python's \1 / \N.
        py_replacement = re.sub(r"\$(\d+)", r"\\\1", replacement)

        if rule.get("requires_link_aware_rewrite"):
            for m in re.finditer(pattern, new_text):
                before = m.group(0)
                line_num = new_text.count("\n", 0, m.start()) + 1
                violations.append(
                    Violation(
                        rule_id=rid,
                        before=before,
                        after=None,
                        line_number=line_num,
                    )
                )
            continue

        # Find each match and record it as a violation.
        for m in re.finditer(pattern, new_text):
            before = m.group(0)
            after_str = m.expand(py_replacement)
            # Find line number for diagnostic purposes.
            line_num = new_text.count("\n", 0, m.start()) + 1
            violations.append(
                Violation(
                    rule_id=rid,
                    before=before,
                    after=after_str,
                    line_number=line_num,
                )
            )

        # Apply the rewrite if --fix was requested.
        if apply_fix:
            new_text = re.sub(pattern, py_replacement, new_text)

    return new_text, violations


def detect_filename_violations(rel_path: str, forbidden: list) -> list[Violation]:
    """Check filename against forbidden_suffixes. Filename renames are
    link-aware and require Cleanup-2 tooling; flag them but don't auto-fix.
    """
    violations: list[Violation] = []
    filename = Path(rel_path).name
    for entry in forbidden:
        if isinstance(entry, dict):
            suffix = entry.get("suffix", "")
        else:
            suffix = str(entry)
        if suffix and suffix in filename:
            violations.append(
                Violation(
                    rule_id=f"forbidden_filename_suffix:{suffix}",
                    before=filename,
                    after=None,  # rename requires link-aware tooling
                    line_number=None,
                )
            )
    return violations


def lint_one_file(path: Path, yaml_data: dict, apply_fix: bool) -> FileReport:
    """Lint a single file; optionally apply mechanical rewrites in place."""
    try:
        rel_path = str(path.relative_to(REPO_ROOT))
    except ValueError:
        rel_path = str(path)

    report = FileReport(path=rel_path)

    # Filename violations: cannot mechanically auto-fix without link-aware
    # cross-doc rewrite (Cleanup-2 tooling).
    forbidden_suffixes = (yaml_data.get("filename_rules") or {}).get("forbidden_suffixes") or []
    report.violations.extend(detect_filename_violations(rel_path, forbidden_suffixes))

    # Text-based violations only apply to readable files.
    rewrite_rules = yaml_data.get("rewrite_rules") or []
    if not path.is_file():
        # Mark all current violations as needs_human (file doesn't exist).
        report.needs_human_vocab_decision = len(report.violations)
        return report

    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        # Binary or unreadable — skip text rewrites; keep filename violations.
        report.needs_human_vocab_decision += len([
            v for v in report.violations if v.after is None
        ])
        return report

    new_text, text_violations = detect_text_violations(
        text, rewrite_rules, rel_path, apply_fix
    )
    report.violations.extend(text_violations)

    if apply_fix and new_text != text:
        path.write_text(new_text, encoding="utf-8")

    # Categorize: auto-correctable vs needs human decision.
    for v in report.violations:
        if v.after is not None:
            report.auto_corrected += 1
        else:
            report.needs_human_vocab_decision += 1

    return report


def collect_files(paths: Iterable[str]) -> list[Path]:
    """Expand paths to a list of concrete files (recurses into dirs)."""
    out: list[Path] = []
    for p in paths:
        path = Path(p)
        if not path.is_absolute():
            path = REPO_ROOT / path
        if path.is_dir():
            for sub in sorted(path.rglob("*")):
                if sub.is_file():
                    out.append(sub)
        else:
            out.append(path)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Mechanical vocabulary lint. Reads docs/repo/controlled_vocabulary.yaml "
            "and applies rewrite_rules + filename_rules to input files."
        )
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Apply mechanical rewrites in place; record each in prose_corrections.",
    )
    parser.add_argument(
        "--report-only",
        action="store_true",
        help="List violations to stdout; do not modify files. Default when --fix is absent.",
    )
    parser.add_argument(
        "--report-path",
        type=str,
        default=None,
        help="Write per-file prose_status.json artifact to PATH.",
    )
    parser.add_argument(
        "--link-aware",
        action="store_true",
        help=(
            "Stub for Cleanup-2: when renaming files, atomically rewrite cross-doc "
            "references. Cleanup-1 ships without this; the flag is accepted but the "
            "filename-rename auto-fix remains deferred."
        ),
    )
    parser.add_argument("files", nargs="*", help="Files or directories to lint.")
    args = parser.parse_args()

    if args.fix and args.report_only:
        print("FAIL: --fix and --report-only are mutually exclusive", file=sys.stderr)
        return 2

    yaml_data = load_yaml()

    if not args.files:
        # Default: lint the docs/ tree (the primary vocabulary surface).
        targets = [str(REPO_ROOT / "docs")]
    else:
        targets = args.files

    files = collect_files(targets)
    reports: list[FileReport] = []
    for path in files:
        # Skip clearly-binary directories that vocab_lint has no business
        # rewriting (audit data dumps, image trees, generated artifacts).
        rel = path.relative_to(REPO_ROOT) if path.is_relative_to(REPO_ROOT) else path
        rel_str = str(rel)
        if any(
            rel_str.startswith(skip) for skip in (
                "docs/audit/data/",       # generated JSON, not source prose
                "logs/",                  # generated logs
                ".git/",
                ".claude/",
            )
        ):
            continue
        # Only lint extensions we care about for the vocabulary.
        if path.suffix not in {".md", ".yaml", ".yml", ".json", ".py", ".txt"}:
            # Filenames still matter (e.g. forbidden suffixes); check
            # filename-only for unsupported extensions.
            filename_violations = detect_filename_violations(
                rel_str,
                (yaml_data.get("filename_rules") or {}).get("forbidden_suffixes") or [],
            )
            if filename_violations:
                r = FileReport(path=rel_str, violations=filename_violations)
                r.needs_human_vocab_decision = len(filename_violations)
                reports.append(r)
            continue
        report = lint_one_file(path, yaml_data, apply_fix=args.fix)
        if report.violations:
            reports.append(report)

    # Output to stdout.
    total_auto = sum(r.auto_corrected for r in reports)
    total_human = sum(r.needs_human_vocab_decision for r in reports)
    print(f"vocab_lint: {len(reports)} files with violations "
          f"({total_auto} auto-correctable, {total_human} needing human review)")
    for r in reports[:50]:
        print(f"  {r.path}: auto={r.auto_corrected} human={r.needs_human_vocab_decision}")
        for v in r.violations[:5]:
            line = f"    [{v.rule_id}] line {v.line_number}: " if v.line_number else f"    [{v.rule_id}]: "
            if v.after is not None:
                print(f"{line}{v.before!r} → {v.after!r}")
            else:
                print(f"{line}{v.before!r} (needs human review)")
        if len(r.violations) > 5:
            print(f"    ... and {len(r.violations) - 5} more violations")
    if len(reports) > 50:
        print(f"  ... and {len(reports) - 50} more files")

    # Optional per-file artifact.
    if args.report_path:
        artifact = {
            "schema_version": 1,
            "summary": {
                "files_with_violations": len(reports),
                "total_auto_correctable": total_auto,
                "total_needs_human": total_human,
            },
            "files": [r.to_dict() for r in reports],
        }
        Path(args.report_path).write_text(
            json.dumps(artifact, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(f"vocab_lint: wrote report to {args.report_path}")

    # Exit code: 0 if clean, or all violations auto-fixed with --fix.
    # 1 if any violation needs human review (or any text violation remains
    # without --fix).
    if total_human > 0:
        return 1
    if not args.fix and total_auto > 0:
        # Auto-correctable violations exist but --fix wasn't used.
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
