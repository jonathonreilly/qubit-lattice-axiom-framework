"""Firewall for ASSUMPTION_DERIVATION_LEDGER metadata conversion."""
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ASSUMPTION_DERIVATION_LEDGER.md"


def check(label: str, ok: bool, detail: str = "") -> bool:
    print(f"  {label}: {'PASS' if ok else 'FAIL'}")
    if detail:
        print(f"    {detail}")
    return ok


def main() -> None:
    text = NOTE.read_text()
    lowered = text.lower()

    print("=" * 72)
    print("ASSUMPTION DERIVATION LEDGER META FIREWALL")
    print("=" * 72)

    checks = [
        check("source type is meta", "**Type:** meta" in text),
        check("source claim scope is metadata", "**Claim scope:** non-authoritative roadmap/index" in text),
        check("YAML author hint is meta", "claim_type_author_hint: meta" in text),
        check("not a bounded theorem", "**Type:** bounded_theorem" not in text),
        check("declares non-authoritative roadmap", "non-authoritative roadmap" in lowered),
        check("sets no audit status", "sets no audit status" in lowered),
        check("uses roadmap-label table", "roadmap label (non-authoritative)" in text),
        check("no current-status table remains", "| ingredient | current status |" not in text),
        check("says labels are non-load-bearing", "non-load-bearing" in lowered),
        check("keeps authority in audit ledger/source notes", "audit_ledger.json" in text),
    ]

    all_ok = all(checks)
    print("=" * 72)
    print(f"  TOTAL: PASS={sum(checks)} FAIL={len(checks) - sum(checks)}")
    print(f"  OVERALL: {'PASS' if all_ok else 'FAIL'}")
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
