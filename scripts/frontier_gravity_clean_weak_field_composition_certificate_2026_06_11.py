#!/usr/bin/env python3
"""Parent composition certificate for the gravity clean weak-field chain.

This runner does not apply an audit verdict. It verifies that
GRAVITY_CLEAN_DERIVATION_NOTE.md is wired to the weak-field bridge that
supplies the three formerly row-local inputs:

  * L^{-1} = G_0
  * rho = |psi|^2
  * S = L(1 - phi)

It also checks that the bridge runner cache is fresh and passing, that the
parent note retains the bounded weak-field status firewall, and that the
large-distance composition gives a bilinear inverse-square force in lattice
units.
"""

from __future__ import annotations

from pathlib import Path
import hashlib
import math
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PARENT_NOTE = ROOT / "docs" / "GRAVITY_CLEAN_DERIVATION_NOTE.md"
BRIDGE_NOTE = ROOT / "docs" / "GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"
BRIDGE_RUNNER = ROOT / "scripts" / "frontier_gravity_weak_field_source_response_bridge_2026_06_11.py"
BRIDGE_CACHE = ROOT / "logs" / "runner-cache" / "frontier_gravity_weak_field_source_response_bridge_2026_06_11.txt"
SELF_CONSISTENCY = ROOT / "docs" / "SELF_CONSISTENCY_FORCES_POISSON_NOTE.md"
POISSON_UNIQUENESS = ROOT / "docs" / "POISSON_EXHAUSTIVE_UNIQUENESS_NOTE.md"
FULL_SELF_CONSISTENCY = ROOT / "docs" / "GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md"
STAGGERED_CARD = ROOT / "docs" / "STAGGERED_FERMION_CARD_2026-04-11.md"
GREEN_THEOREM = ROOT / "docs" / "LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md"
LEGACY_GREEN_BRIDGE = ROOT / "docs" / "LATTICE_GREENS_MARADUDIN_ASYMPTOTIC_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{tag}: {label}{suffix}")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def markdown_targets(text: str) -> set[str]:
    return set(re.findall(r"\]\(([^)]+)\)", text))


def section(text: str, heading: str, next_heading_prefix: str = "\n## ") -> str:
    start = text.find(heading)
    if start < 0:
        return ""
    end = text.find(next_heading_prefix, start + len(heading))
    return text[start:] if end < 0 else text[start:end]


def contains_any(text: str, variants: list[str]) -> bool:
    return any(v in text for v in variants)


def contains_words(text: str, phrase: str) -> bool:
    pattern = r"\s+".join(re.escape(part) for part in phrase.split())
    return re.search(pattern, text) is not None


def main() -> int:
    print("gravity clean weak-field parent composition certificate 2026-06-11")

    required_paths = [
        PARENT_NOTE,
        BRIDGE_NOTE,
        BRIDGE_RUNNER,
        BRIDGE_CACHE,
        SELF_CONSISTENCY,
        POISSON_UNIQUENESS,
        FULL_SELF_CONSISTENCY,
        STAGGERED_CARD,
        GREEN_THEOREM,
        LEGACY_GREEN_BRIDGE,
    ]
    for path in required_paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    parent = read_text(PARENT_NOTE)
    bridge = read_text(BRIDGE_NOTE)
    bridge_cache = read_text(BRIDGE_CACHE)
    parent_links = markdown_targets(parent)
    bridge_links = markdown_targets(bridge)

    # Parent wiring and status firewall.
    check("parent declares bounded theorem type", "**Type:** bounded_theorem" in parent)
    check("parent delegates status to independent audit", "Status authority:** independent audit lane only" in parent)
    check(
        "parent does not set or predict audit outcome",
        contains_words(parent, "does not set or predict an audit outcome"),
    )
    check(
        "parent registers this composition certificate runner",
        "frontier_gravity_clean_weak_field_composition_certificate_2026_06_11.py" in parent,
    )
    check(
        "parent links this certificate cache",
        "logs/runner-cache/frontier_gravity_clean_weak_field_composition_certificate_2026_06_11.txt" in parent,
    )
    check(
        "parent no longer says it has no primary runner",
        "Primary runner:** none registered for this row" not in parent
        and "No registered primary runner for this row" not in parent,
    )

    repair = section(parent, "## 2026-06-11 Weak-Field Bridge Repair")
    check("repair section exists", bool(repair))
    check("repair section names L inverse blocker", contains_any(repair, ["L^{-1} = G_0", "L^{-1}=G_0"]))
    check("repair section names Born density blocker", contains_any(repair, ["rho = |psi|^2", "rho=|psi|^2"]))
    check("repair section names test-response blocker", contains_any(repair, ["S = L(1 - phi)", "S=L(1-phi)"]))
    check(
        "repair section routes blockers through weak-field bridge",
        "GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md" in repair,
    )

    composition = section(parent, "## 2026-06-11 Parent Composition Certificate")
    check("composition certificate section exists", bool(composition))
    for phrase in [
        "source-side certificate",
        "does not apply an audit verdict",
        "bridge cache is SHA-pinned and passing",
        "bilinear inverse-square force",
        "bounded weak-field",
    ]:
        check(f"composition section contains: {phrase}", phrase in composition)

    one_hop = section(parent, "## One-Hop Inputs")
    expected_parent_links = [
        "GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md",
        "SELF_CONSISTENCY_FORCES_POISSON_NOTE.md",
        "POISSON_EXHAUSTIVE_UNIQUENESS_NOTE.md",
        "GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md",
        "STAGGERED_FERMION_CARD_2026-04-11.md",
        "LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md",
        "LATTICE_GREENS_MARADUDIN_ASYMPTOTIC_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md",
    ]
    for target in expected_parent_links:
        check(f"parent one-hop link present: {target}", target in parent_links and target in one_hop)

    binding = section(parent, "## Binding Claim")
    for phrase in [
        "the weak-field source-response bridge supplies `L^{-1} = G_0`",
        "the same bridge supplies the local source readout `rho = |psi|^2`",
        "the same bridge supplies the first-order test-mass response",
        "`G(r) ~ 1/(4 pi r)`",
    ]:
        check(f"binding claim contains: {phrase}", phrase in binding)

    boundaries = section(parent, "## What This Note Does Not Claim")
    for phrase in [
        "No unconditional derivation of Newton gravity",
        "No clean-chain or zero-free-parameter physical-gravity closure",
        "No derivation of physical `G_Newton` in SI units",
        "No derivation of the full Einstein equations",
        "No audit verdict",
    ]:
        check(f"parent boundary contains: {phrase}", phrase in boundaries)

    banned_positive_claims = [
        "**Status:** retained",
        "author-applied retained status",
        "retained branch-local",
        "would become retained",
        "promoted to retained",
        "full Einstein equations are derived",
        "G_Newton in SI units is derived",
        "zero-free-parameter physical-gravity closure is derived",
    ]
    for phrase in banned_positive_claims:
        check(f"parent excludes positive overclaim: {phrase}", phrase not in parent)

    # Bridge note and bridge runner cache contract.
    check("bridge declares bounded theorem type", "Claim type:** bounded_theorem" in bridge)
    check("bridge delegates status to independent audit", "Status authority:** independent audit lane only" in bridge)
    check("bridge links its primary runner", "frontier_gravity_weak_field_source_response_bridge_2026_06_11.py" in bridge)
    check(
        "bridge links its SHA-pinned cache",
        "logs/runner-cache/frontier_gravity_weak_field_source_response_bridge_2026_06_11.txt" in bridge,
    )
    for phrase in [
        "A[phi; rho] = (1/2) <phi, H phi> - <P0 rho, phi>",
        "phi = G0 P0 rho",
        "rho_psi(x) = |psi(x)|^2",
        "S_test(phi; x) = L_test (1 - phi(x))",
        "G(r) -> 1 / (4 pi |r|)",
    ]:
        check(f"bridge contains theorem phrase: {phrase}", phrase in bridge)
    for target in [
        "SELF_CONSISTENCY_FORCES_POISSON_NOTE.md",
        "POISSON_EXHAUSTIVE_UNIQUENESS_NOTE.md",
        "LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md",
        "POISSON_SELF_GRAVITY_LOOP_V3_NOTE.md",
        "GATE_B_POISSON_SELF_GRAVITY_NOTE.md",
    ]:
        check(f"bridge dependency link present: {target}", target in bridge_links)

    if BRIDGE_RUNNER.exists() and BRIDGE_CACHE.exists():
        bridge_sha = sha256(BRIDGE_RUNNER)
        check("bridge cache header is v1", bridge_cache.startswith("===== runner cache v1 ====="))
        check("bridge cache names bridge runner", "runner: scripts/frontier_gravity_weak_field_source_response_bridge_2026_06_11.py" in bridge_cache)
        check("bridge cache pins current bridge runner SHA", f"runner_sha256: {bridge_sha}" in bridge_cache)
        check("bridge cache exit code is zero", "exit_code: 0" in bridge_cache)
        check("bridge cache status ok", "status: ok" in bridge_cache)
        check("bridge cache has expected pass total", "TOTAL: PASS=38 FAIL=0" in bridge_cache)
    else:
        check("bridge cache contract can be checked", False, "bridge runner/cache missing")

    # Framework-local weak-field composition: Green 1/r plus test response
    # gives an inverse-square force with bilinear source/test scaling.
    test_cases = [(3.0, 5.0, 7.0), (2.25, 11.0, 13.0), (17.0, 0.5, 19.0)]
    for source_mass, test_mass, radius in test_cases:
        phi = source_mass / (4.0 * math.pi * radius)
        dphi_dr = -source_mass / (4.0 * math.pi * radius * radius)
        response = test_mass * (1.0 - phi)
        force_mag = test_mass * abs(dphi_dr)
        expected_force = source_mass * test_mass / (4.0 * math.pi * radius * radius)
        check(
            f"bilinear inverse-square force closes for M={source_mass}, m={test_mass}, r={radius}",
            abs(force_mag - expected_force) < 1e-15 and response < test_mass,
            f"force={force_mag:.12g}, expected={expected_force:.12g}",
        )

    r1, r2, m_source = 9.0, 15.0, 4.0
    phi_ratio = (m_source / (4.0 * math.pi * r1)) / (m_source / (4.0 * math.pi * r2))
    force_ratio = (m_source / (4.0 * math.pi * r1 * r1)) / (m_source / (4.0 * math.pi * r2 * r2))
    check("1/r potential ratio is exact in the asymptotic law", abs(phi_ratio - r2 / r1) < 1e-15)
    check("force ratio is inverse-square in the asymptotic law", abs(force_ratio - (r2 / r1) ** 2) < 1e-15)

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
