#!/usr/bin/env python3
"""Executable open-gate inventory check for the Koide Cl(3) selector gap.

This runner intentionally does not close the selector gap.  It makes the
critical open-gate row mechanically checkable by verifying that the source note
keeps its only load-bearing authority, per-route conditional perimeter, and
open-route residuals explicit.
"""
from __future__ import annotations

import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "docs" / "KOIDE_CL3_SELECTOR_GAP_NOTE_2026-04-19.md"

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
    suffix = f"  [{detail}]" if detail else ""
    print(f"{tag}: {label}{suffix}")


def compact(text: str) -> str:
    replacements = {
        "*": "",
        "`": "",
        "×": "x",
        "→": "->",
        "−": "-",
        "₂": "2",
        "₃": "3",
        "⁺": "+",
    }
    out = text.lower()
    for old, new in replacements.items():
        out = out.replace(old, new)
    return " ".join(out.split())


def main() -> int:
    raw = NOTE.read_text(encoding="utf-8")
    text = compact(raw)

    print("Koide Cl(3) selector-gap open-gate inventory runner")
    print(f"note={NOTE.relative_to(ROOT)}")
    print()

    check("note declares Type/Status as open gate", "**Type:** open_gate" in raw and "open selector-gap inventory" in text)
    check("audit-status authority remains independent", "status authority" in text and "independent audit lane only" in text)
    check(
        "single load-bearing parent is the V_eff coefficient-assignment context",
        "single load-bearing item" in text
        and "v_eff coefficient assignment" in text
        and "koide_z3_scalar_potential_lepton_mass_tower_note_2026-04-19" in text,
    )
    check(
        "downstream use is forbidden for route exhaustions",
        "downstream consumers must not cite this note for" in text
        and "any specific route's exhaustion" in text,
    )
    check(
        "global Cl(3)-alone non-derivability is held open",
        "closed \"cl(3) alone cannot derive m_\" bounded theorem" in text
        and "global closure-statement stays open" in text,
    )

    routes = {
        "kramers doublets": "conditional pending direct retained dep/runner",
        "doublet-a equal-diagonal": "conditional pending direct retained dep/runner",
        "j2 off-diagonal": "conditional pending direct retained dep/runner",
        "baryon schur": "conditional pending retained 4x4 derivation",
        "su(3) coupling-mod": "conditional pending retained cl(3)->sm-embedding theorem",
        "no degeneracy crossing": "conditional pending direct retained runner",
        "m_ from h_ witness": "conditional pending first-principles kappa_ derivation",
        "open routes": "open-gate inventory only",
    }
    for label, posture in routes.items():
        check(f"per-route table keeps {label} conditional/open", label in text and posture in text)

    check("open route (a) full 4x4 block remains named", "full 4x4 block diagonalization" in text and "not yet formally proved" in text)
    check("open route (b) transport gap remains observation only", "transport gap 4" in text and "observation only" in text)
    check("open route (c) kappa_* derivation remains central open problem", "first-principles derivation of kappa_" in text and "central open problem" in text)

    m_da = -math.sqrt(2.0 / 3.0)
    m_star = -1.1605
    gap = abs(m_da - m_star)
    rel = gap / abs(m_star)
    check("m_DA arithmetic: -sqrt(2/3) = -0.816497 to displayed precision", abs(m_da + 0.816497) < 5e-7)
    check("m_DA misses m_* by about 0.344 and about 30 percent", 0.343 < gap < 0.345 and 0.29 < rel < 0.31)
    check("off-diagonal GAMMA inventory value is explicitly 1/2", "gamma = 1/2" in text and "conditional pending direct retained dep/runner" in text)

    eigs = [-2.507, -0.848, 2.195]
    min_gap = min(abs(a - b) for i, a in enumerate(eigs) for b in eigs[i + 1 :])
    check("listed H_sel(m_*) eigenvalues are mutually distinct", min_gap > 1.0, detail=f"min_gap={min_gap:.3f}")

    transport = 4.0 * math.pi / math.sqrt(6.0)
    mismatch = abs(5.29 - transport) / 5.29
    check("transport comparator 4*pi/sqrt(6) is near 5.13 with about 3 percent mismatch", 5.12 < transport < 5.14 and 0.02 < mismatch < 0.04)

    check(
        "source note refuses status promotion or charged-lepton package upgrade",
        "does not upgrade the authoritative bounded charged-lepton package" in text
        and "does not promote the exploratory q = 2/3-surface" in text,
    )
    check(
        "runnerization section is boundary-only, not a new retained authority",
        "2026-06-13 executable inventory runner" in text
        and "does not supply any per-route retained authority" in text,
    )

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
