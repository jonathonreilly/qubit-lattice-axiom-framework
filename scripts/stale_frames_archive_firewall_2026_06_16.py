#!/usr/bin/env python3
"""Guard the archived stale-frame firewall."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive_unlanded" / "stale-frames-2026-04-30"

FILES = {
    "CL4C_CARRIER_AXIOM_CONSEQUENCE_MAP_NOTE_2026-04-28.md": [
        "Historical Cl_4(C) Carrier-Axiom Consequence Map (Retracted)",
        "historical / diagnostic and retired as evidence",
        "not an active Axiom* consequence map",
        "Historical theorem statement (retracted)",
        "Archive boundary",
    ],
    "HUBBLE_LANE5_C1_A5_MINIMAL_CARRIER_AXIOM_AUDIT_NOTE_2026-04-28.md": [
        "Historical Lane 5 `(C1)` Gate A5 Carrier-Axiom Packet (Retracted)",
        "historical / diagnostic and retired as evidence",
        "not an active A5 audit",
        "Historical theorem statement (retracted)",
        "Archive boundary",
    ],
    "HUBBLE_LANE5_C1_STUCK_FANOUT_SYNTHESIS_NOTE_2026-04-28.md": [
        "Historical Lane 5 `(C1)` Gate Stuck Fan-Out Packet (Retracted)",
        "historical / diagnostic and retired as evidence",
        "not an active global exhaustion proof",
        "Historical synthesis (retracted as global exhaustion)",
        "Archive boundary",
    ],
}

BANNED = [
    "# Cl_4(C) Carrier-Axiom Consequence Map (Cross-Lane)",
    "# Lane 5 `(C1)` Gate — A5 Minimal-Carrier-Axiom Audit",
    "# Lane 5 `(C1)` Gate — Stuck Fan-Out Synthesis",
    "## 7. Theorem (audit)",
    "## 2. Theorem (audit)",
    "## 4. What this audit closes",
    "## 4. What this synthesis closes",
    "## 8. What this map closes",
    "## 6. Implication for honest stop",
    "## 10. Implication for honest scientific decision",
    "The map confirms that minimal-axiom-extension cosmology closure",
    "This is an **audit** note",
    "This is a **stuck-fan-out synthesis** note (audit-grade)",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    for name, required in FILES.items():
        text = (ARCHIVE / name).read_text(encoding="utf-8")
        for needle in required:
            require(needle in text, f"{name}: missing required text: {needle}")
        for needle in BANNED:
            require(needle not in text, f"{name}: old live stale-frame phrase remains: {needle}")

    print("PASS: stale-frame archive firewall holds")


if __name__ == "__main__":
    main()
