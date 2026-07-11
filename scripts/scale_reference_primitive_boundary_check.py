#!/usr/bin/env python3
"""Boundary runner for the scale-reference framework primitive.

This runner verifies only source, registry, policy, and purity-guard alignment
for `scale_reference_primitive`. It does not derive the Planck length, assert
`a/l_P = 1`, or license any dimensionless physics.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
POLICY = ROOT / "docs" / "audit" / "AXIOM_MINIMALITY_POLICY.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A = ROOT / "docs" / "audit" / "data" / "premise_decision_history.json"
PURITY_GUARD = ROOT / "docs" / "audit" / "scripts" / "check_axiom_premise_clean.py"
RUNNER = "scripts/scale_reference_primitive_boundary_check.py"
CLAIM_ID = "scale_reference_primitive"

PASS_COUNT = 0
FAIL_COUNT = 0


def normalize(text: str) -> str:
    return " ".join(text.split())


def contains(text: str, phrase: str) -> bool:
    return normalize(phrase) in normalize(text)


def check(name: str, ok: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {name}{suffix}")
    return ok


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    return json.loads(read(path))


def main() -> int:
    print("=" * 78)
    print("SCALE-REFERENCE PRIMITIVE BOUNDARY CHECK")
    print("=" * 78)
    print("Scope: primitive registry/source firewall only; no downstream theorem.")
    print()

    note = read(NOTE)
    policy = read(POLICY)
    registry = load_json(REGISTRY)
    tier_a = load_json(TIER_A)
    registry_node = (registry.get("nodes") or {}).get(CLAIM_ID, {})
    derivation_targets = tier_a.get("derivation_targets") or {}
    reclassified_primitives = tier_a.get("reclassified_primitives") or {}
    tier_a_scale = reclassified_primitives.get(CLAIM_ID, {})

    check("source note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    check("policy exists", POLICY.exists(), str(POLICY.relative_to(ROOT)))
    check("registry exists", REGISTRY.exists(), str(REGISTRY.relative_to(ROOT)))
    check("Tier-A registry exists", TIER_A.exists(), str(TIER_A.relative_to(ROOT)))
    check("source type is meta", "**Type:** meta" in note)
    check("source declares framework primitive status", "**Status:** framework primitive declaration" in note)
    check("registry canonical ids include scale primitive", CLAIM_ID in registry.get("canonical_ids", []))
    check("registry node exists", bool(registry_node))
    check(
        "registry current path points at source note",
        registry_node.get("current_path") == str(NOTE.relative_to(ROOT)),
        str(registry_node.get("current_path")),
    )
    check(
        "registry note records units-conversion-only scope",
        "Units conversion only" in registry_node.get("note", ""),
    )
    check(
        "registry note forbids dimensionless content",
        "carries no dimensionless content" in registry_node.get("note", ""),
    )
    check(
        "registry note forbids Planck-length self-consistency laundering",
        "does not assert a/l_P=1" in registry_node.get("note", ""),
    )
    check(
        "registry note records non-bounding chain satisfaction",
        "chain-satisfy without bounding downstream rows" in registry_node.get("note", ""),
    )

    check("policy records owner approval section", "## 6. Explicit Owner Approval For Axioms And Primitives" in policy)
    check("policy records scale primitive approval", "2026-06-04 -- scale-reference primitive" in policy)
    check(
        "policy records dimensional irreducibility",
        contains(policy, "The framework baseline carries no dimensionful number, so one scale reference is irreducible by dimensional analysis."),
    )
    check(
        "policy records no-laundering boundary",
        contains(policy, "The primitive carries no mass ratio, coupling, mixing angle, phase, selector, readout bridge, or empirical fit."),
    )
    check(
        "policy keeps Planck-length self-consistency separate",
        contains(policy, "the self-consistency that the natural unit equals the Planck length remains a separate open gravity derivation."),
    )

    check(
        "decision history preserves zero final admission count",
        tier_a.get("genuine_admitted_input_count") == 0,
        str(tier_a.get("genuine_admitted_input_count")),
    )
    check("scale primitive was never a historical derivation target", CLAIM_ID not in derivation_targets)
    check("decision history records scale reclassification provenance", bool(tier_a_scale))
    check(
        "historical reclassification says not status-bounding",
        "not a status-bounding dependency" in tier_a_scale.get("statement", ""),
    )

    check("note declares exactly one dimensionful reference", "exactly one dimensionful reference" in note)
    check("note names Planck mass scale reference", "a^{-1} = M_Pl" in note)
    check("note says units conversion not physics axiom", "This is a units conversion, not a physics axiom." in note)
    check("note says zero dimensionless content", "It carries zero dimensionless\ncontent" in note)
    check("note disclaims deriving the chosen physical scale", "No derivation of the chosen\nphysical scale is claimed here" in note)
    check("note says it does not add or amend an axiom", "It does not add or amend an axiom." in note)
    check("note says it does not assert a/l_P = 1 as derived", "It does not assert `a/l_P = 1` as a derived theorem." in note)
    check("note says it does not supply dimensionless quantity", "It does not supply any dimensionless quantity." in note)
    check("note says it does not change audit verdicts", "It does not change any audit verdict." in note)
    check("note names the sole foundation registry", "axiom_premise_nodes.json" in note and "sole foundation registry" in note)
    check("note rejects an admission registry", "no admission registry or third premise class exists" in note)

    forbidden_claims = (
        r"derives?\s+(?:the\s+)?Planck length",
        r"derives?\s+(?:the\s+)?Planck mass",
        r"a/l_P\s*=\s*1\s+is\s+derived",
        r"299792458",
        r"1\.616255",
        r"mixing angle\s*=",
        r"mass ratio\s*=",
        r"coupling\s*=",
        r"empirical fit\s*=",
    )
    for pattern in forbidden_claims:
        check(f"forbidden overclaim absent: {pattern}", re.search(pattern, note, re.IGNORECASE) is None)

    guard = subprocess.run(
        [sys.executable, str(PURITY_GUARD)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    guard_detail = guard.stdout.strip().splitlines()[-1] if guard.stdout.strip() else guard.stderr.strip()
    check("axiom/primitive purity guard passes", guard.returncode == 0, guard_detail)

    print()
    print(f"SUMMARY: SCALE REFERENCE PRIMITIVE BOUNDARY PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
