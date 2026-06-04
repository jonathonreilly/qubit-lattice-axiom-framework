#!/usr/bin/env python3
"""Structural guard: axiom/primitive premise docs must stay pure premise content.

An axiom/approved-primitive premise node (see
docs/audit/data/axiom_premise_nodes.json) is granted an auditor carve-out:
citing it does not, by itself, block a clean verdict
(AUDIT_AGENT_PROMPT_TEMPLATE.md). That carve-out is only safe while the source
doc contains pure approved-premise content. If a framework-rule / ratification
clause is ever introduced into one of these docs, the carve-out becomes a
laundering path: any rule dropped into the premise doc could then be "cleanly
derived" by citing the premise.

This guard tripwires that. For each allowlisted premise doc, it fails
if the doc contains a ratification / load-bearing-rule MARKER (a clause that
*asserts* a framework rule), not the mere keywords — explicit "this is NOT a
framework rule" disclaimers are fine.

Behavior:
  - Registry absent (axiom_premise not yet wired): no-op pass.
  - Registry present, doc clean: pass.
  - Registry present, doc carries a ratification marker: FAIL (exit 1),
    pointing at the cleanup requirement.

Run standalone or from run_pipeline.sh. Deterministic, offline, read-only.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
AXIOM_PREMISE_NODES_PATH = REPO_ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

# High-signal markers that only appear in an *asserted* framework-rule /
# ratification clause, not in a "this is NOT a framework rule" disclaimer.
FORBIDDEN_PATTERNS = [
    (re.compile(r"load-bearing ratification", re.IGNORECASE), "load-bearing ratification clause"),
    (re.compile(r"ratification clause\s*\(", re.IGNORECASE), "explicit 'Ratification clause (...)' marker"),
    (re.compile(r"load-bearing axiom content", re.IGNORECASE), "'load-bearing axiom content' assertion"),
    (re.compile(r"load-bearing framework-rule", re.IGNORECASE), "'load-bearing framework-rule' assertion"),
    (re.compile(r"^#{1,6}\s+Ratification\b", re.IGNORECASE | re.MULTILINE), "Ratification heading"),
    (re.compile(r"^#{1,6}\s+Hardening\s+(?:II|III)\b", re.IGNORECASE | re.MULTILINE), "Hardening II/III ratification heading"),
]


def load_axiom_premise_docs() -> list[tuple[str, str]]:
    """Return (canonical_id, current_path) for each allowlisted premise node."""
    if not AXIOM_PREMISE_NODES_PATH.exists():
        return []
    try:
        data = json.loads(AXIOM_PREMISE_NODES_PATH.read_text(encoding="utf-8"))
    except Exception:
        return []
    out: list[tuple[str, str]] = []
    for cid, entry in (data.get("nodes") or {}).items():
        cur = entry.get("current_path")
        if cur:
            out.append((cid, cur))
    return out


def scan_doc(path: Path) -> list[str]:
    """Return a list of violation descriptions for one doc (empty = clean)."""
    text = path.read_text(encoding="utf-8", errors="replace")
    violations: list[str] = []
    for pattern, desc in FORBIDDEN_PATTERNS:
        if pattern.search(text):
            violations.append(desc)
    return violations


def main() -> int:
    docs = load_axiom_premise_docs()
    if not docs:
        print("check_axiom_premise_clean: no axiom/primitive premise registry; nothing to check.")
        return 0

    failed = False
    for cid, rel_path in docs:
        path = REPO_ROOT / rel_path
        if not path.exists():
            print(f"  FAIL {cid}: registered path missing on disk: {rel_path}")
            failed = True
            continue
        violations = scan_doc(path)
        if violations:
            failed = True
            print(f"  FAIL {cid} ({rel_path}): axiom/primitive premise doc carries framework-rule markers:")
            for v in violations:
                print(f"        - {v}")
        else:
            print(f"  OK   {cid} ({rel_path}): pure premise content")

    if failed:
        print(
            "\ncheck_axiom_premise_clean: an axiom/primitive premise doc contains a framework-rule\n"
            "ratification clause. The premise auditor carve-out is only safe while\n"
            "the source doc is pure premise content. Move the rule into a named derivation lane,\n"
            "or remove the node from\n"
            "docs/audit/data/axiom_premise_nodes.json."
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
