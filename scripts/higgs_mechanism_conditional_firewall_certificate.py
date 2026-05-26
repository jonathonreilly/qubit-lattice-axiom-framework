#!/usr/bin/env python3
"""Certificate for the Higgs mechanism conditional-use firewall.

This runner does not try to derive the scalar/Coleman-Weinberg substrate.
It verifies that the source note exposes that substrate as an admitted bridge
and keeps the heavy Higgs mechanism runner in diagnostic/support scope.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "HIGGS_MECHANISM_NOTE.md"
HEAVY_RUNNER = ROOT / "scripts" / "frontier_higgs_mass_derived.py"
HEAVY_CACHE = ROOT / "logs" / "runner-cache" / "frontier_higgs_mass_derived.txt"


def require(name: str, condition: bool) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {name}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    text = NOTE.read_text(encoding="utf-8")
    cache = HEAVY_CACHE.read_text(encoding="utf-8") if HEAVY_CACHE.exists() else ""

    print("HIGGS MECHANISM CONDITIONAL FIREWALL CERTIFICATE")
    print(f"note={NOTE.relative_to(ROOT)}")

    require("source note exists", NOTE.exists())
    require("heavy diagnostic runner exists", HEAVY_RUNNER.exists())
    require("heavy diagnostic cache exists", HEAVY_CACHE.exists())

    required_phrases = [
        "conditional-use firewall",
        "bounded mechanism-consistency note",
        "single load-bearing bridge remains",
        "scalar potential / Coleman-Weinberg / bare-parameter substrate",
        "The runner is therefore a diagnostic consistency artifact only",
        "be read as an audit-ratified derivation from A1/A2 alone",
        "explicit bridge premise",
        "The Higgs mechanism is derived from the framework axioms",
    ]
    for phrase in required_phrases:
        require(f"note contains firewall phrase: {phrase}", phrase in text)

    require(
        "heavy cache records diagnostic non-closure",
        "exit_code: 1" in cache and "Full m_H derivation" in cache and "FAIL" in cache,
    )

    print("CERTIFICATE PASS: Higgs mechanism note is bounded to the admitted scalar/CW/bare-parameter bridge.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
