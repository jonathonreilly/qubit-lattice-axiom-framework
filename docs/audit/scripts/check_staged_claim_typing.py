#!/usr/bin/env python3
"""Pre-commit ratchet: staged claim notes must carry an explicit claim type.

Reads staged repo-relative paths (one per line) from stdin, loads the
(re-seeded) audit ledger, and fails when any staged docs/**.md maps to a
ledger row whose claim_type_provenance is `default_positive_theorem` —
i.e. the note carries no `Type:`/`Claim type:` header, no legacy
Status-line migration hint, and no meta path/pattern registration, so
seed_audit_ledger silently defaulted it to positive_theorem.

Fix options (pick one):
  - add an explicit `Type:` header line to the note
    (positive_theorem | bounded_theorem | no_go | open_gate | decoration | meta);
  - catalog/index docs: register the path in
    docs/audit/data/meta_source_patterns.txt;
  - non-claim infrastructure: add it to
    docs/audit/data/excluded_source_patterns.txt.

The auditor still owns the final claim_type; this gate only refuses to
grow the silently-defaulted class, so the legacy `claim_type_defaulted`
lint debt (see audit_lint.py) can only shrink. Legacy rows are untouched
until their notes are next edited.

Exit 0 when clean, 1 with a per-file report otherwise.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
LEDGER_PATH = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"


def main() -> int:
    staged = [line.strip() for line in sys.stdin if line.strip()]
    staged_docs = [p for p in staged if p.startswith("docs/") and p.endswith(".md")]
    if not staged_docs:
        return 0
    if not LEDGER_PATH.exists():
        # Seeding did not run; nothing to check against.
        return 0
    rows = json.loads(LEDGER_PATH.read_text(encoding="utf-8")).get("rows", {})
    row_by_note_path = {row.get("note_path"): (cid, row) for cid, row in rows.items()}
    offenders: list[tuple[str, str]] = []
    for path in staged_docs:
        hit = row_by_note_path.get(path)
        if hit is None:
            # Excluded/gated infrastructure or not a ledger row at all.
            continue
        cid, row = hit
        if row.get("claim_type_provenance") == "default_positive_theorem":
            offenders.append((path, cid))
    if not offenders:
        return 0
    print("[claim-typing] staged note(s) with silently-defaulted claim_type:")
    for path, cid in offenders:
        print(f"  {path} (ledger row {cid})")
    print("  Add an explicit 'Type:' header line (positive_theorem |")
    print("  bounded_theorem | no_go | open_gate | decoration | meta), or")
    print("  register the path in docs/audit/data/meta_source_patterns.txt")
    print("  (catalog/index) or docs/audit/data/excluded_source_patterns.txt")
    print("  (non-claim infrastructure), then re-run the seeding step.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
