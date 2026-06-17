#!/usr/bin/env python3
"""Verify the plaquette beta=6 Wilson-normalization import repair."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "PLAQUETTE_BETA6_WILSON_NORMALIZATION_NATIVE_IMPORT_REPAIR_2026-06-17.md"
OLD = ROOT / "docs" / "PLAQUETTE_BETA6_PERTURBATIVE_DERIVATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-27.md"
BETA_REL = ROOT / "docs" / "NATIVE_GAUGE_TRANSFER_BETA_IDENTIFICATION_PHYSICAL_PLAQUETTE_RELATIONSHIP_BOUNDED_NOTE_2026-06-12.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")
    return ok


def squash(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    print("Plaquette beta=6 Wilson-normalization import repair verifier")

    note = NOTE.read_text(encoding="utf-8")
    old = OLD.read_text(encoding="utf-8")
    beta_rel = BETA_REL.read_text(encoding="utf-8")
    note_flat = squash(note)
    old_flat = squash(old)
    beta_flat = squash(beta_rel)

    nc = Fraction(3, 1)
    beta = Fraction(6, 1)
    g2 = Fraction(2, 1) * nc / beta

    check("exact beta=6 Wilson algebra gives g_bare^2 = 1", g2 == 1, f"g2={g2}")
    check("exact beta relation note identifies the shared Wilson coupling", "Same Wilson coupling; different functionals." in beta_rel)
    check("exact beta relation note states beta/(2Nc) character argument", "beta/(2 N_c)" in beta_rel and "N_c = 3" in beta_rel)
    check("exact beta relation note fences physical plaquette value", "0.5934" in beta_rel and "admitted comparison/reuse" in beta_rel)
    check("exact beta relation note refuses physical mass-gap bridge", "NOT a physical mass-gap bridge" in beta_rel and "not the physical mass gap" in beta_rel)
    check("old diagnostic still lists W1-W4 admitted-input set", "W1 the NSPT coefficient packet, W2 the beta=6 Wilson normalization, W3 the MC comparator, and W4 the F2 comparator" in old_flat)
    check("old diagnostic contains new 2026-06-17 partial import-retirement section", "2026-06-17 partial import retirement: beta=6 Wilson normalization" in old)
    check("old diagnostic keeps NSPT/MC/F2 conditional after the repair", "W1, W3, and W4 remain admitted diagnostic inputs" in old_flat)
    check("new note declares exact support and independent audit authority", "**Claim type:** exact support theorem" in note and "independent audit lane only" in note)
    check("new note retires only W2, not the whole diagnostic", "retires only W2" in note and "partial import-retirement note" in note)
    check("new note preserves non-perturbative and comparator boundaries", "does not derive `<P>(beta=6)`" in note and "not a new comparator authority" in note)
    check("new note gives downstream citation rule for normalization only", "Rows that need only the Wilson normalization" in note and "must not cite this repair for those claims" in note)
    check("new note names remaining unretired inputs", all(x in note for x in ["W1", "W3", "W4"]))
    check("new note routes through native beta relationship", "NATIVE_GAUGE_TRANSFER_BETA_IDENTIFICATION_PHYSICAL_PLAQUETTE_RELATIONSHIP_BOUNDED_NOTE_2026-06-12.md" in note)
    check("old diagnostic remains runner-local route pruning", "runner-local route pruning" in old_flat and "actual beta=6 plaquette surface" in old)

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
