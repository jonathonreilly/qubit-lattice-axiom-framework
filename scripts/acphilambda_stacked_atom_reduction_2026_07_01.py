#!/usr/bin/env python3
"""Verify the AC_phi_lambda stacked atom reduction note."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "ACPHILAMBDA_STACKED_ATOM_REDUCTION_2026-07-01.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
STRICT_NN = DOCS / "STRICT_NN_COMPOSITION_FLUX_SELECTOR_BRIDGE_THEOREM_NOTE_2026-06-30.md"
GEN_CONTEXT = DOCS / "GENERATION_CONTEXT_SELECTOR_FROM_STRICT_NN_DIRAC_RECORD_ORIENTATION_2026-06-30.md"
R_HALF = DOCS / "ACPHILAMBDA_R_HALF_DURABLE_RECORD_IDEMPOTENCE_BRIDGE_THEOREM_NOTE_2026-06-30.md"
R_ETA = DOCS / "ACPHILAMBDA_R_ETA_EDGE_DEFECT_LOCALIZATION_BRIDGE_2026-06-30.md"
POST_DIRAC = DOCS / "ACPHILAMBDA_POST_DIRAC_REDUCTION_MAP_2026-06-30.md"
POST_STACK = DOCS / "POST_STACK_HARD_GATE_STATUS_MAP_2026-06-30.md"
SPECIES = DOCS / "ACPHILAMBDA_SPECIES_BRIDGE_REALIZED_STATE_DECOMPOSITION_NOTE_2026-06-11.md"
R_ETA_NARROW = DOCS / "ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def lower_flat(text: str) -> str:
    return flat(text).casefold()


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + title)


def main() -> int:
    print("=== AC_phi_lambda stacked atom reduction ===")

    paths = [
        NOTE,
        AXIOMS,
        STRICT_NN,
        GEN_CONTEXT,
        R_HALF,
        R_ETA,
        POST_DIRAC,
        POST_STACK,
        SPECIES,
        R_ETA_NARROW,
        TIER_A,
    ]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    note_lower = note_flat.casefold()
    axioms = read(AXIOMS)
    strict = read(STRICT_NN)
    strict_flat = flat(strict)
    gen = read(GEN_CONTEXT)
    gen_flat = flat(gen)
    gen_lower = lower_flat(gen)
    r_half = read(R_HALF)
    r_half_flat = flat(r_half)
    r_half_lower = lower_flat(r_half)
    r_eta = read(R_ETA)
    r_eta_flat = flat(r_eta)
    post_dirac = read(POST_DIRAC)
    post_stack = read(POST_STACK)
    species = read(SPECIES)
    r_eta_narrow = read(R_ETA_NARROW)
    tier_a = read(TIER_A)

    section("PART A -- source stack")
    check("axiom surface is current reset", "Minimal Framework Axioms (Lattice, Qubit, Admissibility, Record)" in axioms)
    check("axioms supply physical lattice locality", "Lattice / Physical Locality" in axioms)
    check("axioms supply fixed records", "A record locks exactly one available local possibility" in axioms)
    check("strict NN supplies first-order branch", "first-order branch" in strict_flat and "no face-diagonal leakage" in strict_flat)
    check("strict NN supplies edge coefficients", "edge coefficients" in strict_flat)
    check("generation bridge selects hw=1", "-> hw=1 generation context" in gen)
    check("generation bridge preserves A_R-eta outside", "A_R-eta" in gen and "remains" in gen)
    check("r-half bridge maps durable two-active record to r=1/2", "durable two-active" in r_half_flat and "r = 1/2" in r_half)
    check("r-half bridge preserves context dependence", "after a finite record context exists" in r_half)
    check("R-eta bridge localizes defect density", "L3(1,2) = 2/9" in r_eta)
    check("R-eta bridge names phase-defect coupling", "phase-defect coupling" in r_eta_flat)
    check("Tier-A still carries AC_phi_lambda", '"label": "AC_phi_lambda"' in tier_a)

    section("PART B -- prior residual matching")
    check("post-Dirac map names W_r", "W_r" in post_dirac)
    check("post-Dirac map names W_eta", "W_eta" in post_dirac)
    check("post-Dirac map names W_locus", "W_locus" in post_dirac)
    check("post-stack map names phase-defect coupling", "phase-defect coupling" in post_stack)
    check("species note reduces naming/assignment", "Naming" in species and "carrier-locus" in species)
    check("R-eta narrowing isolates A_R-eta", "A_R-eta" in r_eta_narrow and "h-class" in r_eta_narrow and "h-unit" in r_eta_narrow)

    section("PART C -- composition theorem content")
    check("note declares bounded composition theorem", "bounded composition theorem / audit dependency reduction" in note)
    check("note gives full dependency chain", "2026-06-29 axioms" in note and "strict nearest-neighbor composition" in note)
    check("note composes generation context", "edge-minimal oriented C3 record context" in note and "hw=1 generation context" in note)
    check("note composes r-half theorem", "agreement-composition durable readout" in note and "-> r = 1/2" in note)
    check("note composes R-eta localization", "local scalar defect density L3(1,2) = 2/9" in note)
    check("note names W_phase_defect", "W_phase_defect" in note)
    check("note collapses residuals to stack adoption and phase defect", "W_stack_adoption" in note and "W_phase_defect" in note)
    check("note avoids full closure claim", "does not set an audit verdict" in note_flat and "claim full `AC_phi_lambda` retirement" in note_flat)
    check("note says no axiom update", "No axiom update is requested" in note)

    section("PART D -- finite composition logic")
    old_atoms = {"W_r", "W_eta", "W_locus"}
    after_atoms = {"W_stack_adoption", "W_phase_defect"}
    check("old atom set has three named atoms", old_atoms == {"W_r", "W_eta", "W_locus"})
    check("post composition residual set has two audit atoms", after_atoms == {"W_stack_adoption", "W_phase_defect"})
    check("context atom has supplier", "edge-minimal route" in gen_lower and "succeeds conditionally" in gen_lower)
    check("r atom has supplier", "agreement composition" in r_half_lower and "succeeds conditionally" in r_half_lower)
    check("eta atom is narrowed not closed", "remaining wall is no longer broad R-eta" in r_eta_flat)
    check("composition keeps phase coupling as residual", "the charged-lepton phase magnitude records the selected local C3" in note)

    section("PART E -- non-claims and audit consequence")
    for phrase in [
        "record occurrence",
        "Born frequencies",
        "theta",
        "physical source/action coefficients",
        "metric scale",
        "named electron/muon/tau empirical labels",
    ]:
        check(f"non-claim includes {phrase}", phrase in note)
    check("audit consequence restates blocker", "derive charged-lepton context, r=1/2, and R-eta" in note)
    check("audit consequence names phase-defect coupling", "phase-defect coupling" in note)
    check("note focuses next science work", "focuses the next science work" in note)

    section("PART F -- no-go discipline gate")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", item in note)
    check("N1 enumerates seven routes", note.count("| Broad dynamics route |") == 1 and note.count("| New primitive route |") == 1)
    check("N2 names collapsed residuals", "Collapsed residuals after this composition" in note)
    check("N3 exposes direct-unit boundary", "Direct-unit" in note)
    check("N4 matches five witnesses", note.count("| `ACPHILAMBDA") >= 3 and "POST_STACK_HARD_GATE_STATUS_MAP" in note)
    check("N5 avoids solved rhetoric", "not \"AC_phi_lambda is solved.\"" in note_flat)
    check("N6 lists live closure paths", "derive the phase-defect coupling" in note)
    check("N7 steelman admits bookkeeping objection", "mostly bookkeeping" in note)
    check("N8 cross-cycle echo present", "blending context" in note)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS -- AC_phi_lambda stack reduces to bridge adoption plus W_phase_defect.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
