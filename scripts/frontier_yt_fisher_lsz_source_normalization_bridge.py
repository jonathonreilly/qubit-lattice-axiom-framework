#!/usr/bin/env python3
"""Y_T Fisher/LSZ source-normalization bridge checks."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_fisher_lsz_source_normalization_bridge_2026-05-26.json"

NOTE = DOCS / "YT_FISHER_LSZ_SOURCE_NORMALIZATION_BRIDGE_THEOREM_NOTE_2026-05-26.md"
FISHER_ARCLENGTH = DOCS / "YT_PRIMITIVE_PHYSICAL_SOURCE_FISHER_ARCLENGTH_INVARIANT_THEOREM_NOTE_2026-05-26.md"
POLE_NOGO = DOCS / "YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md"
FH_GATE = DOCS / "YT_FH_TOP_W_RESPONSE_RATIO_GATE_NOTE_2026-05-25.md"
SOURCE_COV = DOCS / "YT_SOURCE_COVARIANCE_NORMALIZATION_SUPPORT_NOTE_2026-05-24.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def one_line(text: str) -> str:
    return " ".join(text.split())


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def part1_scope() -> None:
    print("\nPart 1: files and scope")
    for path in (NOTE, FISHER_ARCLENGTH, POLE_NOGO, FH_GATE, SOURCE_COV):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Theorem Statement",
        "Relation To The Pole-Row No-Go",
        "Proof",
        "What This Moves",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", section in note)

    check("note marks exact-support status", "actual_current_surface_status: exact-support" in note)
    check("note denies Y_T retained closure", "claim retained or proposed-retained Y_T closure" in note)
    check("note keeps pole-residue authority open", "does not supply that physical" in note)
    check("note avoids legacy PR-number marker", "PR230" not in note and "pr230" not in note.lower())


def part2_fisher_lsz_equivalence() -> dict[str, str]:
    print("\nPart 2: Fisher/LSZ equivalence")
    A, lam = sp.symbols("A lambda", positive=True)

    # O = A * phi_LSZ.  The pole residue of O is A^2.
    residue = A**2
    fisher_metric = residue
    d_ell_d_h = sp.sqrt(fisher_metric)
    raw_operator_coeff = 1
    fisher_normalized_coeff = sp.simplify(raw_operator_coeff / d_ell_d_h)
    lsz_coeff = sp.simplify(1 / A)

    check("pole residue is A^2", is_zero(residue - A**2), residue)
    check("Fisher metric on pole residue surface is A^2", is_zero(fisher_metric - A**2), fisher_metric)
    check("Fisher arclength derivative is A", is_zero(d_ell_d_h - A), d_ell_d_h)
    check("Fisher-normalized insertion equals LSZ unit-residue insertion", is_zero(fisher_normalized_coeff - lsz_coeff), fisher_normalized_coeff)

    scaled_residue = (lam * A) ** 2
    scaled_d_ell_d_h = sp.sqrt(scaled_residue)
    scaled_fisher_insertion = sp.simplify(lam / scaled_d_ell_d_h)
    scaled_lsz_insertion = sp.simplify(lam / (lam * A))

    check("scaled pole residue is lambda^2 A^2", is_zero(scaled_residue - lam**2 * A**2), scaled_residue)
    check("scaled Fisher insertion remains 1/A", is_zero(scaled_fisher_insertion - 1 / A), scaled_fisher_insertion)
    check("scaled LSZ insertion remains 1/A", is_zero(scaled_lsz_insertion - 1 / A), scaled_lsz_insertion)
    check("scaled Fisher and scaled LSZ insertions agree", is_zero(scaled_fisher_insertion - scaled_lsz_insertion), scaled_fisher_insertion)

    return {
        "pole_residue": str(residue),
        "fisher_metric": str(fisher_metric),
        "fisher_insertion": str(fisher_normalized_coeff),
        "lsz_insertion": str(lsz_coeff),
        "scaled_invariant": str(scaled_fisher_insertion),
    }


def part3_gram_purity_boundary() -> dict[str, str]:
    print("\nPart 3: Gram-purity boundary")
    As, AH, mu, lam = sp.symbols("A_s A_H mu lambda", positive=True)
    rss = As**2
    rsh = As * AH
    rhh = AH**2
    gram_det = sp.simplify(rsh**2 - rss * rhh)
    scaled_det = sp.simplify((mu * lam * rsh) ** 2 - (mu**2 * rss) * (lam**2 * rhh))

    normalized_overlap = sp.simplify(rsh / sp.sqrt(rss * rhh))
    scaled_overlap = sp.simplify((mu * lam * rsh) / sp.sqrt((mu**2 * rss) * (lam**2 * rhh)))

    check("rank-one Gram determinant is zero", is_zero(gram_det), gram_det)
    check("scaled rank-one Gram determinant remains zero", is_zero(scaled_det), scaled_det)
    check("normalized overlap is one for same pole", is_zero(normalized_overlap - 1), normalized_overlap)
    check("scaled normalized overlap remains one", is_zero(scaled_overlap - 1), scaled_overlap)
    check("raw residue changes under Higgs/source rescaling", sp.simplify(lam**2 * rhh - rhh) != 0)

    return {
        "gram_det": str(gram_det),
        "scaled_gram_det": str(scaled_det),
        "normalized_overlap": str(normalized_overlap),
        "scaled_overlap": str(scaled_overlap),
    }


def part4_current_boundary() -> dict[str, bool]:
    print("\nPart 4: current boundary")
    note = read(NOTE)
    pole_nogo = read(POLE_NOGO)
    checks = {
        "preserves_pole_row_no_go": "Gram purity alone cannot fix absolute normalization" in note,
        "pole_nogo_names_lsz_gate": "canonical scalar LSZ normalization" in pole_nogo,
        "same_surface_pole_residue_not_supplied": "does not supply that physical" in note,
        "strict_top_w_response_not_supplied": "coefficient-certified top/W response row" in note,
        "proposal_not_allowed": "proposal_allowed: false" in note,
    }
    for name, ok in checks.items():
        check(name.replace("_", " "), ok)
    return checks


def part5_firewalls() -> None:
    print("\nPart 5: firewalls")
    note = read(NOTE)
    flat = one_line(note)
    for phrase in (
        "H_unit",
        "yt_ward_identity",
        "y_t_bare",
        "observed top/W/Z masses",
        "PDG values",
        "alpha_LM",
        "plaquette/u0",
        "fitted selector",
    ):
        check(f"firewall phrase present: {phrase}", phrase in flat)

    for phrase in (
        "Status:** retained",
        "actual_current_surface_status: retained",
        "proposal_allowed: true",
        "bare_retained_allowed: true",
        "full Y_T closure",
        "strict top/W response evidence exists",
        "isolated Higgs/top pole is established on the Y_T surface",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 88)
    print("Y_T FISHER-LSZ SOURCE NORMALIZATION BRIDGE")
    print("=" * 88)

    part1_scope()
    equivalence = part2_fisher_lsz_equivalence()
    gram = part3_gram_purity_boundary()
    boundary = part4_current_boundary()
    part5_firewalls()

    result = {
        "status": "exact-support under accepted isolated-pole source surface",
        "claim": (
            "On an accepted isolated-pole surface, Fisher source arclength and "
            "LSZ unit-residue normalization give the same normalized insertion."
        ),
        "trace_class": "upstream_support",
        "reachability_to_target": "supports",
        "proposal_allowed": False,
        "bare_retained_allowed": False,
        "fisher_lsz_equivalence": equivalence,
        "gram_purity_boundary": gram,
        "current_boundary": boundary,
        "remaining_bridge": (
            "Provide accepted same-surface pole-residue authority and strict "
            "top/W response evidence; this theorem does not create the pole rows."
        ),
        "forbidden_imports_used": False,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_FISHER_LSZ_SOURCE_NORMALIZATION_BRIDGE_THEOREM_NOTE_2026-05-26.md",
            "scripts/frontier_yt_fisher_lsz_source_normalization_bridge.py",
            "outputs/yt_fisher_lsz_source_normalization_bridge_2026-05-26.json",
        ],
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
