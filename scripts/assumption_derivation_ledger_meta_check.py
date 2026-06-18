#!/usr/bin/env python3
"""Meta-firewall runner for ASSUMPTION_DERIVATION_LEDGER.

This runner does not certify any ingredient row. It verifies only that the
ledger is a non-authoritative roadmap, that the former bounded-theorem status
claim is absent, and that the R_conn/F_adj row preserves the selector no-go
boundary rather than promoting a physical EW readout.
"""
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ASSUMPTION_DERIVATION_LEDGER.md"
RUNNER = "scripts/assumption_derivation_ledger_meta_check.py"


def check(label: str, ok: bool, detail: str = "") -> bool:
    print(f"  {label}: {'PASS' if ok else 'FAIL'}")
    if detail:
        print(f"    {detail}")
    return ok


def normalize(text: str) -> str:
    return " ".join(text.split())


def contains(text: str, phrase: str) -> bool:
    return normalize(phrase) in normalize(text)


def main() -> None:
    text = NOTE.read_text(encoding="utf-8")
    lowered = text.lower()

    print("=" * 72)
    print("ASSUMPTION DERIVATION LEDGER META FIREWALL")
    print("=" * 72)

    checks = [
        check("source type is meta", "**Type:** meta" in text),
        check("source claim scope is metadata", "**Claim scope:** non-authoritative roadmap/index" in text),
        check("source registers this primary runner", f"**Primary runner:** [`{RUNNER}`]" in text),
        check("YAML author hint is meta", "claim_type_author_hint: meta" in text),
        check("YAML registers this runner", f"primary_runner: {RUNNER}" in text),
        check("not a bounded theorem", "**Type:** bounded_theorem" not in text),
        check("declares non-authoritative roadmap", "non-authoritative roadmap" in lowered),
        check("sets no audit status", "sets no audit status" in lowered),
        check("uses roadmap-label table", "roadmap label (non-authoritative)" in text),
        check("no current-status table remains", "| ingredient | current status |" not in text),
        check("says labels are non-load-bearing", "non-load-bearing" in lowered),
        check("keeps authority in audit ledger/source notes", "audit_ledger.json" in text),
        check("conflicts defer to authority notes", contains(text, "Where this ledger and an authority note disagree, the authority note governs.")),
        check("R_conn row is narrowed to F_adj exact algebra", "exact `F_adj = 8/9` color fraction" in text),
        check("physical selector remains conditional", "does not derive the selector `κ_EW = 0`" in text),
        check("theorem-grade wiring is explicitly out of scope", contains(text, "This metadata version deliberately does not attempt that.")),
    ]

    all_ok = all(checks)
    print("=" * 72)
    print(f"  TOTAL: PASS={sum(checks)} FAIL={len(checks) - sum(checks)}")
    print(f"  OVERALL: {'PASS' if all_ok else 'FAIL'}")
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
