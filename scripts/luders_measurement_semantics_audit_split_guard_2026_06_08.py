#!/usr/bin/env python3
"""Guard the 2026-06-08 Lueders audit-target split.

The parent Lueders row is useful, but only as a conditional-support assembly:
native finite algebra closes PEP/KP/projective-instrument facts, while the
physical measurement-probability bridge remains open. This runner verifies the
source text keeps that split explicit.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PARENT = DOCS / "LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md"
PEP = DOCS / "LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
KP = DOCS / "LSP_PROJECTIVE_CANONICAL_KP_EQUALS_P_NARROW_THEOREM_NOTE_2026-06-05.md"
RECORD_WRITE = DOCS / "RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md"
KERNEL = DOCS / "RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-05.md"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    parent = read(PARENT)
    pep = read(PEP)
    kp = read(KP)
    record_write = read(RECORD_WRITE)
    kernel = read(KERNEL)
    axioms = read(AXIOMS)

    print("LUEDERS MEASUREMENT-SEMANTICS AUDIT SPLIT GUARD 2026-06-08")

    for path in (PARENT, PEP, KP, RECORD_WRITE, KERNEL, AXIOMS):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    check("parent declares conditional-support assembly", "conditional-support assembly over exact finite subclaims" in parent)
    check("parent says not retained/unbounded/native Lueders theorem", "not a retained, unbounded, or framework-native" in parent)
    check("parent names 2026-06-08 split", "2026-06-08 Audit-Target Split" in parent)
    check("parent enumerates PEP finite support", "The finite `PEP` compression theorem" in parent)
    check("parent enumerates KP finite support", "The canonical projective Kraus selection" in parent)
    check("parent enumerates finite pointer-record write", "The finite pointer-record write bridge" in parent)
    check("parent enumerates typed record-instrument kernel", "The typed record-instrument kernel interface" in parent)
    check("parent identifies residual measurement-semantics bridge", "Residual open bridge for this parent" in parent)
    check("parent states Record axiom supplies no probability/instrument", "supplies no probability, normalization, measurement/decoherence" in parent)
    check("parent keeps Born/measurement probability premise open", "Born/measurement probability premise" in parent)

    check("PEP bridge denies measurement probability semantics", "does not obtain the Lüders state update, Born rule" in pep)
    check("KP bridge scopes out general apparatus label-mixing", "label-mixing" in kp and "dilation of the same projective measurement" in kp)
    check("record-write bridge is finite pointer-model conditional", "finite pointer model" in record_write and "ideal record-write" in record_write)
    check("record-write bridge denies Born/probability derivation", "does not derive a Born rule or probability law" in record_write)
    check("kernel interface is under supplied instrument", "supplied finite instrument" in kernel and "trace/effect pairing" in kernel)
    check("kernel interface leaves trace/effect probability open", "Deriving the trace/effect probability rule" in kernel)
    check("minimal axioms deny instrument/Born content", "instrument, Born rule" in axioms and "probability" in axioms)

    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
