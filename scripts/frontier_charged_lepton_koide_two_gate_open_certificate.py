#!/usr/bin/env python3
"""Open-gate certificate for the charged-lepton Koide packet."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs/CHARGED_LEPTON_KOIDE_NOTE_2026-04-18.md"
LEDGER = REPO_ROOT / "docs/audit/data/audit_ledger.json"
QUEUE = REPO_ROOT / "docs/audit/data/audit_queue.json"

CLAIM_ID = "charged_lepton_koide_note_2026-04-18"
RUNNER_PATH = "scripts/frontier_charged_lepton_koide_two_gate_open_certificate.py"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", kind: str = "A") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"[{status}] [{kind}] {name}{suffix}")


def note_boundary_checks() -> None:
    text = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(text.split())
    required = [
        "Claim type:** open_gate",
        "Status:** open gate",
        "two remaining charged-lepton Koide gates",
        "Koide surface selection gate",
        "Brannen phase identification gate",
        "does not claim",
        "any new axiom or audit verdict",
        "open-gate map",
    ]
    for phrase in required:
        check(f"note boundary contains: {phrase}", phrase in normalized)

    forbidden = [
        "current support packet",
        "authoritative support surface",
        "clean enough for package use",
        "conditional closure",
        "promoted on the current package surface",
        "retained closure",
        "retained promotion",
    ]
    for phrase in forbidden:
        check(f"note omits stale package phrase: {phrase}", phrase not in text)


def algebra_checks() -> None:
    print("\n=== charged-lepton Koide gate algebra ===")
    c, q, delta = sp.symbols("c q delta", real=True)
    q_expr = sp.Rational(1, 3) + c**2 / 6
    c2_at_target = sp.solve(sp.Eq(q_expr, sp.Rational(2, 3)), c**2)[0]
    r_over_a_sq = c2_at_target / 4
    delta_expr = q / 3

    check("Q target solves c^2=2", sp.simplify(c2_at_target - 2) == 0, str(c2_at_target))
    check("Q target solves r^2/a^2=1/2", sp.simplify(r_over_a_sq - sp.Rational(1, 2)) == 0, str(r_over_a_sq))
    check("c^2=2 implies Q=2/3", sp.simplify(q_expr.subs(c**2, 2) - sp.Rational(2, 3)) == 0)
    check("delta=Q/3 sends Q=2/3 to 2/9", sp.simplify(delta_expr.subs(q, sp.Rational(2, 3)) - sp.Rational(2, 9)) == 0)
    check("delta=2/9 is equivalent to Q=2/3 under delta=Q/3", sp.simplify(3 * sp.Rational(2, 9) - sp.Rational(2, 3)) == 0)
    check("Brannen phase bridge is a declared extra rule", "delta := Q/3" in NOTE.read_text(encoding="utf-8"), kind="B")


def audit_metadata_checks() -> None:
    if not LEDGER.exists() or not QUEUE.exists():
        print("\n=== audit metadata unavailable before pipeline ===")
        return
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    row = ledger["rows"][CLAIM_ID]
    queue = json.loads(QUEUE.read_text(encoding="utf-8"))["queue"]
    queue_entry = next(e for e in queue if e["claim_id"] == CLAIM_ID)

    print("\n=== regenerated audit metadata ===")
    check("ledger claim_type is open_gate", row.get("claim_type") == "open_gate")
    check("ledger audit_status reset to unaudited", row.get("audit_status") == "unaudited")
    check("ledger effective_status reset to unaudited", row.get("effective_status") == "unaudited")
    check("ledger runner_path registered", row.get("runner_path") == RUNNER_PATH, str(row.get("runner_path")))
    check("ledger has no direct deps", row.get("deps") == [], str(row.get("deps")))
    check("self dependency path removed", row.get("open_dependency_paths") == [], str(row.get("open_dependency_paths")))
    check("queue marks row ready", queue_entry.get("ready") is True, str(queue_entry.get("ready")))
    check("descendant chain remains material", int(row.get("transitive_descendants") or 0) >= 200, str(row.get("transitive_descendants")), kind="B")


def main() -> int:
    note_boundary_checks()
    algebra_checks()
    audit_metadata_checks()
    print("\nCharged-lepton Koide two-gate open certificate:", "PASS" if FAIL_COUNT == 0 else "FAIL")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
