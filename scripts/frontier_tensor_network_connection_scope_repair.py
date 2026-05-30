#!/usr/bin/env python3
"""Scope-boundary checker for the tensor-network connection note."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
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


def has_phrase(text: str, phrase: str) -> bool:
    return " ".join(phrase.split()) in " ".join(text.split())


def main() -> int:
    print("Tensor network connection scope repair")
    print("=" * 72)

    note = NOTE.read_text(encoding="utf-8")
    runner = RUNNER.read_text(encoding="utf-8")

    print()
    print("A. Note scope")
    print("-" * 72)
    check("note declares bounded_theorem", "**Claim type:** bounded_theorem" in note)
    check("note has no branch-local status authority", "Status authority" not in note)
    check("note has primary runner", "**Primary runner:** `scripts/frontier_tensor_network_connection.py`" in note)
    check(
        "note rejects holographic promotion",
        has_phrase(note, "No continuum AdS/CFT, RT, MERA, or holographic-gravity theorem is claimed")
        and has_phrase(note, "No AdS/CFT, MERA, continuum, or physical-gravity claim is promoted"),
    )
    check(
        "note states RT fit failure",
        "inverse-coupling fit has only R^2 = 0.6465" in note
        and has_phrase(note, "direct linear fit has R^2 = 0.9745"),
    )
    check(
        "note keeps finite theorem target",
        has_phrase(note, "bounded finite-runner theorem")
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
    print("C. Runner replay")
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
