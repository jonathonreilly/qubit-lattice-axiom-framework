#!/usr/bin/env python3
"""Boundary runner for the kinetic-isotropy framework primitive.

This runner verifies only source/registry/policy alignment for
`kinetic_isotropy_primitive`. It does not prove Lorentz restoration, a spacing
ratio, a dynamics theorem, or any dimensionless observable.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
POLICY = ROOT / "docs" / "audit" / "AXIOM_MINIMALITY_POLICY.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
PURITY_GUARD = ROOT / "docs" / "audit" / "scripts" / "check_axiom_premise_clean.py"
CLAIM_ID = "kinetic_isotropy_primitive"

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


def load_registry() -> dict:
    return json.loads(read(REGISTRY))


def main() -> int:
    print("=" * 78)
    print("KINETIC-ISOTROPY PRIMITIVE BOUNDARY CHECK")
    print("=" * 78)
    print("Scope: primitive registry/source firewall only; no downstream theorem.")
    print()

    note = read(NOTE)
    policy = read(POLICY)
    registry = load_registry()
    registry_node = (registry.get("nodes") or {}).get(CLAIM_ID, {})

    check("source note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    check("policy exists", POLICY.exists(), str(POLICY.relative_to(ROOT)))
    check("registry exists", REGISTRY.exists(), str(REGISTRY.relative_to(ROOT)))
    check("source type is meta", "**Type:** meta" in note)
    check("source declares framework primitive status", "**Status:** framework primitive declaration" in note)
    check("registry canonical ids include kinetic primitive", CLAIM_ID in registry.get("canonical_ids", []))
    check("registry node exists", bool(registry_node))
    check(
        "registry current path points at source note",
        registry_node.get("current_path") == str(NOTE.relative_to(ROOT)),
        str(registry_node.get("current_path")),
    )
    check(
        "registry note records dimensionless structural premise",
        "dimensionless STRUCTURAL premise" in registry_node.get("note", ""),
    )
    check(
        "registry note forbids dynamical-content laundering",
        "carries no dimensionless DYNAMICAL content" in registry_node.get("note", ""),
    )

    check("policy records owner approval section", "## 6. Explicit Owner Approval For Axioms And Primitives" in policy)
    check("policy records kinetic primitive approval", "2026-06-09 -- kinetic-isotropy primitive" in policy)
    check(
        "policy records no-laundering boundary",
        contains(policy, "The primitive carries no mass ratio, coupling, mixing angle, phase, selector, readout bridge, or empirical fit."),
    )
    check(
        "policy records emergent-time boundary",
        contains(policy, "This primitive does not re-axiomatize time"),
    )

    check("note states c_t = c_s", "c_t = c_s" in note)
    check("note states OS0/hypercubic graining", "Osterwalder-Schrader OS0 kinetic" in note)
    check("note says no dimensionless dynamical content", "It carries no dimensionless dynamical content" in note)
    check("note says it is not a fourth spatial dimension", "not a fourth spatial dimension" in note)
    check("note says it does not add or amend an axiom", "It does not add or amend an axiom." in note)
    check("note says it does not re-axiomatize time", "It does not re-axiomatize time." in note)
    check("note says no audit verdict changes", "It does not change any audit verdict." in note)
    check("note cites premise registry", "docs/audit/data/axiom_premise_nodes.json" in note)
    check("note cites purity guard", "check_axiom_premise_clean.py" in note)

    forbidden_claims = (
        r"m_t\s*=",
        r"y_t\s*=",
        r"mixing angle is derived",
        r"retained Lorentz restoration",
        r"physical observable is supplied",
        r"dimensionless dynamical quantity is supplied",
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
    check(
        "axiom/primitive purity guard passes",
        guard.returncode == 0,
        guard.stdout.strip().splitlines()[-1] if guard.stdout.strip() else guard.stderr.strip(),
    )

    print()
    print(f"SUMMARY: KINETIC ISOTROPY PRIMITIVE BOUNDARY PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
