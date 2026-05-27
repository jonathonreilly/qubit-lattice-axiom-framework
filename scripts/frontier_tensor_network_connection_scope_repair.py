#!/usr/bin/env python3
"""Scope-boundary checker for the tensor-network connection note."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
NOTE = DOCS / "TENSOR_NETWORK_CONNECTION_NOTE.md"
RUNNER = ROOT / "scripts" / "frontier_tensor_network_connection.py"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def main() -> int:
    print("Tensor network connection scope repair")
    print("=" * 72)

    note = NOTE.read_text(encoding="utf-8")
    runner = RUNNER.read_text(encoding="utf-8")
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    row = ledger["rows"]["tensor_network_connection_note"]

    print()
    print("A. Note scope")
    print("-" * 72)
    check("note declares bounded_theorem", "**Claim type:** bounded_theorem" in note)
    check("note has primary runner", "**Primary runner:** `scripts/frontier_tensor_network_connection.py`" in note)
    check(
        "note rejects holographic promotion",
        "No continuum AdS/CFT, RT,\nMERA, or holographic-gravity theorem is claimed" in note
        and "No AdS/CFT, MERA, continuum, or physical-gravity claim is promoted" in note,
    )
    check(
        "note states RT fit failure",
        "inverse-coupling fit has only R^2 = 0.6465" in note
        and "direct linear\nfit has R^2 = 0.9745" in note,
    )
    check(
        "note keeps finite theorem target",
        "bounded\nfinite-runner theorem" in note
        and "bond dimension bounded by `Ny`" in note,
    )

    print()
    print("B. Runner wording")
    print("-" * 72)
    check("runner removes RT pass label", "GATE 4 (RT connection)" not in runner)
    check("runner reports RT formula not derived", "RT formula derived: NO" in runner)
    check("runner keeps inverse fit as negative diagnostic", "not an RT S=Area/(4G) derivation" in runner)
    check("runner no longer claims holographic dictionary", "without claiming a derived holographic dictionary" in runner)

    print()
    print("C. Current ledger row")
    print("-" * 72)
    check("row was audited conditional before pipeline", row.get("audit_status") == "audited_conditional", str(row.get("audit_status")))
    check("row audited claim_type is bounded_theorem", row.get("claim_type") == "bounded_theorem", str(row.get("claim_type")))
    check(
        "row records the finite-to-holography blocker",
        "AdS/CFT" in (row.get("chain_closure_explanation") or "")
        and "RT" in (row.get("chain_closure_explanation") or ""),
    )

    print()
    print("D. Runner replay")
    print("-" * 72)
    result = subprocess.run(
        [sys.executable, str(RUNNER.relative_to(ROOT))],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    output = result.stdout
    check("runner exits cleanly", result.returncode == 0, f"returncode={result.returncode}")
    check("runner preserves four gates", "Gates passed: 4/4" in output)
    check("runner prints entropy sweep label", "TEST 4: ENTROPY COUPLING SWEEP" in output)
    check("runner states RT formula not derived", "RT formula derived: NO" in output)
    check("runner reports direct fit beats inverse fit", "not an RT S=Area/(4G) derivation" in output)

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: tensor-network row is ready for bounded re-audit.")
        return 0
    print("VERDICT: tensor-network scope repair checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
