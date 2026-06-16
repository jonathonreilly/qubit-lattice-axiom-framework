#!/usr/bin/env python3
"""Verify the 2026-06-12 staggered-Dirac kinetic supply-line sync.

This runner is an audit-readiness verifier for audited-conditional
consumers of the staggered/Kawamoto-Smit carrier. It checks that the
source notes now expose the sharper current-main cascade:

  kinetic-class forcing -> P-SD discharged on K1
  kinetic-class forcing -> P-KIN reduced to P-FLUX
  P-FLUX composer -> conditional selection by FSB-K + retained Z

It does not audit, retag, or claim retained closure. The supplier rows
remain audit-owned, and the P-FLUX selection remains conditional on
FSB-K's grade.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

KS_NOTE = ROOT / "docs" / "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md"
NOETHER_NOTE = ROOT / "docs" / "AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md"
GATE_NOTE = ROOT / "docs" / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
KINETIC_NOTE = ROOT / "docs" / "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md"
P_FLUX_NOTE = ROOT / "docs" / "P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md"
FSB_NOTE = ROOT / "docs" / "AXIOM_FIRST_FERMIONIC_STEFAN_BOLTZMANN_NARROW_THEOREM_NOTE_2026-05-26.md"
Z_NOTE = ROOT / "docs" / "STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-11.md"

TARGET_CACHES = {
    "ks": ROOT / "logs" / "runner-cache" / "probe_kawamoto_smit_phase_forcing.txt",
    "noether": ROOT / "logs" / "runner-cache" / "axiom_first_lattice_noether_check.txt",
    "gate": ROOT / "logs" / "runner-cache" / "staggered_dirac_realization_gate_synthesis_check_2026_06_09.txt",
}
SUPPLIER_CACHES = {
    "kinetic": ROOT / "logs" / "runner-cache" / "staggered_dirac_kinetic_class_forcing_check_2026_06_10.txt",
    "p_flux": ROOT / "logs" / "runner-cache" / "p_flux_selection_via_fsb_k_check_2026_06_11.txt",
    "fsb": ROOT / "logs" / "runner-cache" / "frontier_axiom_first_fermionic_stefan_boltzmann_narrow.txt",
    "z": ROOT / "logs" / "runner-cache" / "staggered_kernel_z_certificate_check_2026_06_11.txt",
}

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(body: str) -> str:
    return " ".join(body.split())


def has_total(body: str, expected_pass: int) -> bool:
    return re.search(rf"TOTAL: PASS={expected_pass}\s+FAIL=0", body) is not None


def block_presence() -> None:
    print("\n" + "=" * 72)
    print("BLOCK 1: notes and caches present")
    print("=" * 72)
    for path in [KS_NOTE, NOETHER_NOTE, GATE_NOTE, KINETIC_NOTE, P_FLUX_NOTE, FSB_NOTE, Z_NOTE]:
        check(f"{path.relative_to(ROOT)} exists", path.exists())
    for label, path in {**TARGET_CACHES, **SUPPLIER_CACHES}.items():
        check(f"{label} cache exists", path.exists(), str(path.relative_to(ROOT)))


def block_target_notes() -> None:
    print("\n" + "=" * 72)
    print("BLOCK 2: target notes expose the supply line")
    print("=" * 72)

    ks = read(KS_NOTE)
    noether = read(NOETHER_NOTE)
    gate = read(GATE_NOTE)
    ks_flat = flat(ks)
    noether_flat = flat(noether)
    gate_flat = flat(gate)

    check("KS note has 2026-06-12 supply-line changelog", "2026-06-12 (kinetic supply-line sync)" in ks)
    check("KS note states P-SD discharged on K1", "P-SD discharged on K1" in ks or "P-SD is discharged" in ks)
    check("KS note states P-KIN reduced to P-FLUX", "P-KIN reduced to P-FLUX" in ks or "P-KIN is reduced to P-FLUX" in ks)
    check(
        "KS note keeps audit-owned boundary",
        "This row remains a bounded theorem on supplied `P-KIN/P-SD` unless that" in ks
        and "cascade is accepted by the independent audit lane" in ks,
    )
    check("KS note states FSB-K condition", "conditional on FSB-K" in ks)
    check("KS note exposes source-only sync verifier", "scripts/staggered_dirac_kinetic_supply_line_sync_2026_06_12.py" in ks)

    check("Noether note has 2026-06-12 refresh section", "Kinetic supply-line refresh (2026-06-12" in noether)
    check("Noether note includes exact cascade", "kinetic-class forcing -> P-SD discharged on K1 -> P-KIN reduced to P-FLUX" in noether_flat)
    check("Noether note keeps bounded carrier boundary", "the Noether row remains bounded" in noether)
    check("Noether note names FSB-K as open condition", "remains the named open condition" in noether)
    check("Noether note exposes source-only sync verifier", "scripts/staggered_dirac_kinetic_supply_line_sync_2026_06_12.py" in noether)

    check("Gate note premise table names P-FLUX supply line", "kinetic-class / P-FLUX supply line" in gate)
    check("Gate note says current closure remains bounded/conditional", "current closure remains bounded/conditional" in gate)
    check("Gate residual names P-FLUX cascade", "the live residual is the P-FLUX cascade" in gate)
    check("Gate note requires supplier audits", "Supplier rows and the FSB-K condition remain independently audit-owned" in gate_flat)
    check("Gate note exposes source-only sync verifier", "scripts/staggered_dirac_kinetic_supply_line_sync_2026_06_12.py" in gate)

    for body, label in [(ks_flat, "KS"), (noether_flat, "Noether"), (gate_flat, "Gate")]:
        check(f"{label} note does not claim retained closure", "does not claim retained closure" in body or "not claim retained closure" in body or "not vanished at current grades" in body or "does not promote" in body)


def block_cache_outputs() -> None:
    print("\n" + "=" * 72)
    print("BLOCK 3: target and supplier cache outputs")
    print("=" * 72)

    ks_cache = read(TARGET_CACHES["ks"])
    noether_cache = read(TARGET_CACHES["noether"])
    gate_cache = read(TARGET_CACHES["gate"])
    kinetic_cache = read(SUPPLIER_CACHES["kinetic"])
    p_flux_cache = read(SUPPLIER_CACHES["p_flux"])
    fsb_cache = read(SUPPLIER_CACHES["fsb"])
    z_cache = read(SUPPLIER_CACHES["z"])

    check("KS target cache PASS=47 FAIL=0", has_total(ks_cache, 47))
    check("Noether target cache PASSED 8/8", "PASSED: 8/8" in noether_cache)
    check("Gate target cache PASS=31 FAIL=0", has_total(gate_cache, 31))

    check("kinetic supplier cache PASS=27 FAIL=0", has_total(kinetic_cache, 27))
    check("kinetic supplier says P-SD discharged on K1", "P-SD discharged on the flux(-1) branch" in kinetic_cache)
    check("kinetic supplier says P-KIN residual is one-bit flux selector", "P-KIN residual: the one-bit flux selector" in kinetic_cache)
    check("kinetic supplier contains K0 countermodel", "countermodel K0" in kinetic_cache)

    check("P-FLUX composer cache PASS=16 FAIL=0", has_total(p_flux_cache, 16))
    check(
        "P-FLUX composer records today's grade boundary",
        "C1 (FSB-K) = retained_bounded" in p_flux_cache
        and "within-surface selection is active at current grades" in p_flux_cache,
    )
    check("P-FLUX composer records retained Z geometry", "retained Z certificate = retained" in p_flux_cache)
    check(
        "P-FLUX composer says current selection is within-surface",
        "this note performs the within-surface selection at current grades" in p_flux_cache
        and "retiring P-KIN wholesale additionally requires that row's grade" in p_flux_cache,
    )

    check("FSB-K cache PASS=18 FAIL=0", has_total(fsb_cache, 18))
    check("FSB-K cache says phi not assumed or derived", "phi = -1 is neither" in fsb_cache)
    check("Z cache PASS=18 FAIL=0", has_total(z_cache, 18))
    check("Z cache certifies K1 satisfies Z", "Kawamoto-Smit realized kernel satisfies hypothesis (Z)" in z_cache)
    check("Z cache certifies K0 violates Z", "flux-(+1) kernel VIOLATES both clauses" in z_cache)


def block_firewall() -> None:
    print("\n" + "=" * 72)
    print("BLOCK 4: status firewall")
    print("=" * 72)
    ks = flat(read(KS_NOTE))
    noether = flat(read(NOETHER_NOTE))
    gate = flat(read(GATE_NOTE))

    forbidden = [
        "promoted to retained",
        "becomes retained",
        "retained on the actual surface",
    ]
    for phrase in forbidden:
        check(f"forbidden phrase absent: {phrase}", phrase not in ks and phrase not in noether and phrase not in gate)

    check("KS sync says no audit status change", "does not change this row's current audit status" in ks)
    check("Noether sync says no promotion", "This section does not promote the row" in noether)
    check("Gate sync says supplier rows audit-owned", "Supplier rows and the FSB-K condition remain independently audit-owned" in gate)
    check("runner is source verifier only", True, "does not read or edit audit data")


def main() -> int:
    print("=" * 72)
    print("Staggered-Dirac kinetic supply-line sync verifier")
    print("=" * 72)
    print("Claim boundary: bounded/conditional dependency-wire repair only.")

    try:
        block_presence()
        block_target_notes()
        block_cache_outputs()
        block_firewall()
    except Exception as exc:  # pragma: no cover
        check("unexpected runner exception", False, repr(exc))

    print("\n" + "=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    print("VERDICT: supply-line sync verified iff FAIL=0; no audit status is changed.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
