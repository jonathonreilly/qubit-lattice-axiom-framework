#!/usr/bin/env python3
"""Guard live causal-field packet references against stale archive reuse.

This is source-hygiene support only. It does not run the audit loop and does
not set audit status. It checks that current causal-field context links point
to the live finite-replay packet rather than the archived failed note.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LIVE = "CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md"
FIREWALL_CACHE = "logs/runner-cache/causal_field_live_packet_reference_firewall_2026_06_16.txt"
ARCHIVE_LINK = "archive_unlanded/causal-field-stale-runners-2026-04-30/CAUSAL_PROPAGATING_FIELD_NOTE.md"

LIVE_DOCS = [
    "docs/CAUSAL_CONE_SPEED_MAP_NOTE.md",
    "docs/CAUSAL_FIELD_RECONCILIATION_NOTE.md",
    "docs/CAUSAL_SOURCE_PLACEMENT_ROBUSTNESS_NOTE.md",
    "docs/CAUSAL_MOVING_UNIFICATION_NOTE.md",
    "docs/CAUSAL_DISTANCE_TAIL_NOTE.md",
    "docs/CAUSAL_FIELD_CANONICAL_CHAIN_NOTE.md",
    "docs/DIAMOND_ABSOLUTE_UNIT_BRIDGE_NOTE.md",
    "docs/SHAPIRO_DELAY_NOTE.md",
    "docs/CAUSAL_IMPACT_PARAMETER_NOTE.md",
]

ARCHIVED_SHAPIRO_DOCS = [
    "archive_unlanded/shapiro-static-renderers-and-failed-bridges-2026-04-30/SHAPIRO_DIAMOND_BRIDGE_NOTE.md",
    "archive_unlanded/shapiro-static-renderers-and-failed-bridges-2026-04-30/SHAPIRO_COMPLEX_INTERACTION_NOTE.md",
]

RENDERER_SCRIPTS = [
    "scripts/causal_distance_tail_probe.py",
    "scripts/causal_impact_parameter_probe.py",
    "scripts/shapiro_phase_lag_probe.py",
    "scripts/shapiro_complex_interaction.py",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(rel: str) -> str:
    path = ROOT / rel
    require(path.exists(), f"missing expected file: {rel}")
    return path.read_text(encoding="utf-8")


def main() -> None:
    live_note = read(f"docs/{LIVE}")
    archive = read("archive_unlanded/causal-field-stale-runners-2026-04-30/CAUSAL_PROPAGATING_FIELD_NOTE.md")

    require("Primary runner" in live_note, "live packet lost primary runner metadata")
    require("The current packet is a finite configured replay" in live_note, "live packet scope text missing")
    require("historical / diagnostic and retired as evidence" in archive, "archive is not explicitly retired as evidence")
    require("must not be listed as live evidence" in archive, "archive live-evidence firewall missing")
    require("Historical claim boundary (retracted)" in archive, "archive claim boundary not marked retracted")

    for rel in LIVE_DOCS:
        text = read(rel)
        require(LIVE in text, f"{rel} does not reference the live causal-field packet")
        require(ARCHIVE_LINK not in text, f"{rel} still references the archived failed causal-field packet")

    reconciliation = read("docs/CAUSAL_FIELD_RECONCILIATION_NOTE.md")
    forbidden = [
        "The retained causal-field note says",
        "The retained `c=0.5` result",
        "retained `~0.45` value",
        "So the correct retained split is:",
        "**retained positive:** the center-family dynamic causal cone observable",
    ]
    for phrase in forbidden:
        require(phrase not in reconciliation, f"reconciliation note still carries stale phrase: {phrase}")

    chain = read("docs/CAUSAL_FIELD_CANONICAL_CHAIN_NOTE.md")
    require("meta source-firewall chain map" in chain, "canonical chain is not scoped as a meta map")
    require("**Type:** meta" in chain and "**Claim type:** meta" in chain, "canonical chain metadata is not meta")
    require("No package-level retained" in chain, "canonical chain missing retained-status firewall")
    require(FIREWALL_CACHE in chain, "canonical chain does not link this firewall cache")
    require("causal_propagating_field_live_packet_note_2026-06-05" in chain, "canonical chain missing live-packet dependency link")
    require("causal_field_portability_note" in chain, "canonical chain missing portability dependency link")

    forbidden_chain = [
        "proposed_retained package",
        "retained phase curve",
        "This is a good retained result",
        "strongest retained claim",
        "audited-clean",
        "retained_bounded",
        "retained_no_go",
        "Current source status",
        "supports a physical field speed",
        "The Shapiro phase is a unique causal discriminator",
    ]
    for phrase in forbidden_chain:
        require(phrase not in chain, f"canonical chain still carries stale package phrase: {phrase}")

    diamond = read("docs/DIAMOND_ABSOLUTE_UNIT_BRIDGE_NOTE.md")
    require("archived `0.45` table is stale" in diamond, "diamond bridge note does not mark archived 0.45 table stale")

    for rel in ARCHIVED_SHAPIRO_DOCS:
        text = read(rel)
        require(ARCHIVE_LINK not in text, f"{rel} still points to archived causal-field packet as a dependency")
        require(LIVE in text, f"{rel} does not point to the live causal-field packet")

    stale_generated = "docs/CAUSAL_PROPAGATING_FIELD_NOTE.md"

    def active_renderer_text(text: str) -> str:
        lines: list[str] = []
        for line in text.splitlines():
            if stale_generated in line and (" not in " in line or "stale_generated" in line):
                continue
            lines.append(line)
        return "\n".join(lines)

    for rel in RENDERER_SCRIPTS:
        text = read(rel)
        active_text = active_renderer_text(text)
        require(stale_generated not in active_text, f"{rel} would regenerate the stale causal-field note link")
        require(LIVE in text, f"{rel} does not generate the live causal-field packet link")

    print("PASS: causal-field live packet reference firewall holds")


if __name__ == "__main__":
    main()
