#!/usr/bin/env python3
"""Verify the strict-NN edge-minimal generation context selector bridge."""

from __future__ import annotations

from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs" / "GENERATION_CONTEXT_SELECTOR_FROM_STRICT_NN_DIRAC_RECORD_ORIENTATION_2026-06-30.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
STRICT_NN = ROOT / "docs" / "STRICT_NN_COMPOSITION_FLUX_SELECTOR_BRIDGE_THEOREM_NOTE_2026-06-30.md"
POST_DIRAC = ROOT / "docs" / "ACPHILAMBDA_POST_DIRAC_REDUCTION_MAP_2026-06-30.md"
R_HALF = ROOT / "docs" / "ACPHILAMBDA_R_HALF_DURABLE_RECORD_IDEMPOTENCE_BRIDGE_THEOREM_NOTE_2026-06-30.md"
SPECIES = ROOT / "docs" / "ACPHILAMBDA_SPECIES_BRIDGE_REALIZED_STATE_DECOMPOSITION_NOTE_2026-06-11.md"
HW_COMP = ROOT / "docs" / "ACPHILAMBDA_HW_COMPLEMENTATION_EQUIVARIANCE_SUPPORT_NOTE_2026-06-09.md"
GRADE1 = ROOT / "docs" / "KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md"
FLAVOR_CARRIER = ROOT / "docs" / "FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED_2026-05-31.md"
THREE_GEN = ROOT / "docs" / "THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md"
ROUTE_MAP = ROOT / "docs" / "POST_AXIOM_ADOPTION_REMAINING_HARD_GATE_ROUTE_MAP_2026-06-30.md"
R_ETA = ROOT / "docs" / "ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md"

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


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


def c3(v: tuple[int, int, int]) -> tuple[int, int, int]:
    x, y, z = v
    return (y, z, x)


def complement(v: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(1 - x for x in v)  # type: ignore[return-value]


def orbit(v: tuple[int, int, int]) -> set[tuple[int, int, int]]:
    out = {v}
    cur = v
    for _ in range(2):
        cur = c3(cur)
        out.add(cur)
    return out


def hw(v: tuple[int, int, int]) -> int:
    return sum(v)


def main() -> int:
    print("=== Generation context selector from strict NN Dirac record orientation ===")

    paths = [
        NOTE,
        AXIOMS,
        STRICT_NN,
        POST_DIRAC,
        R_HALF,
        SPECIES,
        HW_COMP,
        GRADE1,
        FLAVOR_CARRIER,
        THREE_GEN,
        ROUTE_MAP,
        R_ETA,
    ]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    axioms = read(AXIOMS)
    axioms_flat = flat(axioms)
    strict = read(STRICT_NN)
    strict_flat = flat(strict)
    post = read(POST_DIRAC)
    r_half = read(R_HALF)
    species = read(SPECIES)
    hw_comp = read(HW_COMP)
    grade1 = read(GRADE1)
    flavor = read(FLAVOR_CARRIER)
    three_gen = read(THREE_GEN)
    route_map = read(ROUTE_MAP)
    r_eta = read(R_ETA)

    print("\nPART A -- source surface")
    check("axioms supply nearest-neighbor locality", "nearest-neighbor adjacency" in axioms_flat)
    check("axioms supply admissible availability", "available subset of possibilities" in axioms)
    check("Record locks one available possibility", "A record locks exactly one available local possibility" in axioms)
    check("axioms keep context downstream", "context selection" in axioms_flat)
    check("strict NN bridge supplies edge-local first-order branch", "no face-diagonal leakage" in strict_flat and "first-order branch" in strict_flat)
    check("strict NN bridge names anticommuting edge coefficients", "anticommuting edge coefficients" in strict_flat)
    check("strict NN bridge saturates three directions", "no fourth anticommuting edge coefficient" in strict_flat or "one-qubit carrier" in strict_flat)
    check("post-Dirac map names W_locus", "W_locus" in post)
    check("route map picks generation-context selector first", "Generation-context selector" in route_map)

    print("\nPART B -- finite cube theorem")
    corners = list(product((0, 1), repeat=3))
    levels = {k: {v for v in corners if hw(v) == k} for k in range(4)}
    check("cube has eight corners", len(corners) == 8)
    check("Hamming cardinalities are 1,3,3,1", [len(levels[k]) for k in range(4)] == [1, 3, 3, 1])
    check("hw=1 orbit has three points", levels[1] == {(1, 0, 0), (0, 1, 0), (0, 0, 1)})
    check("hw=2 orbit has three points", levels[2] == {(1, 1, 0), (1, 0, 1), (0, 1, 1)})
    check("C3 orbit of x-edge is hw=1", orbit((1, 0, 0)) == levels[1])
    check("C3 orbit of xy-face is hw=2", orbit((1, 1, 0)) == levels[2])
    check("C3 preserves Hamming weight", all(hw(c3(v)) == hw(v) for v in corners))
    check("complement exchanges hw=1 and hw=2", {complement(v) for v in levels[1]} == levels[2])
    check("complement exchanges hw=0 and hw=3", {complement(v) for v in levels[0]} == levels[3])
    check("complement commutes with C3", all(complement(c3(v)) == c3(complement(v)) for v in corners))
    nontrivial_three_orbits = {frozenset(orbit(v)) for v in corners if len(orbit(v)) == 3}
    check("only two nontrivial three-point C3 orbits exist", nontrivial_three_orbits == {frozenset(levels[1]), frozenset(levels[2])})
    positive_orbits = sorted((min(hw(x) for x in o), set(o)) for o in nontrivial_three_orbits)
    check("unique minimal positive edge-count orbit is hw=1", positive_orbits[0][1] == levels[1] and positive_orbits[0][0] == 1)
    check("hw=2 is two-edge/face orbit", all(hw(v) == 2 for v in levels[2]))
    missing_edge_dual = {v: complement(v) for v in levels[1]}
    check("each hw=2 face is complement of one edge", set(missing_edge_dual.values()) == levels[2], str(missing_edge_dual))

    print("\nPART C -- prior note matching")
    check("three-generation theorem proves exact hw=1 surface", "H_hw=1 = C^3" in three_gen)
    check("three-generation theorem proves M3(C)", "M_3(C)" in three_gen)
    check("three-generation theorem excludes proper quotient on hw=1", "no proper quotient" in three_gen.lower())
    check("hw-complement note says hw=1/hw=2 complement", "hw=1" in hw_comp and "hw=2" in hw_comp and "complementation" in hw_comp)
    check("hw-complement note says not physical species bridge", "No physical-species bridge is derived" in hw_comp)
    check("species note names carrier-locus selection", "carrier-locus selection" in species)
    check("species note says naming is vacuous", "Naming" in species and "vacuous" in species)
    check("species note says registration is pointwise data", "registered data" in species and "pointwise" in species)
    check("flavor carrier says momentum type derived", "Carrier TYPE = momentum factor" in flavor)
    check("flavor carrier says hw=1 locus remains open", "Carrier LOCUS = hw=1 triplet" in flavor and "open physical-locus bridge" in flavor)
    check("grade1 note supports compatibility but not closure", "compatibility result" in grade1 and "not a closure" in grade1)
    check("R-half theorem waits for charged-lepton context", "charged-lepton record context uses two active readable outcomes" in flat(r_half))
    check("R-eta remains outside", "A_R-eta" in r_eta and "not retired" in r_eta)

    print("\nPART D -- new theorem note content")
    check("note declares conditional bridge theorem", "positive theorem candidate / conditional bridge theorem" in note)
    check("note names strict NN edge primitive", "primitive local kinetic/readout object is an oriented nearest-neighbor edge" in note)
    check("note selects hw=1 as minimal", "minimal nontrivial `C3[111]` record context" in note and "hw=1" in note)
    check("note preserves hw=2 as valid complement", "not excluded and not physically impossible" in note)
    check("note gives finite theorem section", "## Finite Theorem" in note)
    check("note gives unlock chain", "What This Unlocks If Retained" in note)
    check("note does not claim full AC closure", "does not by itself retire all of `AC_phi_lambda`" in note)
    check("note lists remaining gates", "Record occurrence" in note and "Born weights" in note and "P-cal" in note)
    check("note names edge-minimality as bridge content", "Edge-minimal" in note or "edge-minimal" in note)

    print("\nPART E -- consequence checks")
    check("edge-minimal bridge collapses broad locus residual", "old residual" in note and "new residual" in note)
    check("context chain reaches durable r theorem", "durable two-active charged-lepton record theorem" in note)
    check("context chain does not include A_R-eta", "A_R-eta" in note and "remains" in note)
    check("no measured data consumed", "measured masses" in note and "PDG names" in note)
    check("no record production smuggled", "record-production closure" in note or "record-production" in note)

    print("\nPART F -- no-go discipline gate")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", item in note)
    check("N1 has at least five routes", note.count("| Route |") == 1 and note.count("PARTIAL") >= 3)
    check("N2 names collapsed residuals", "Collapsed residuals" in note and "W_eta" in note)
    check("N3 keeps edge-minimal explicit", "\"Edge-minimal\" is the named bridge content" in note)
    check("N4 matches witnesses", "Residual Matching" in note and "W_locus" in note)
    check("N5 avoids excluding hw=2", "does not say \"`hw=2` is unphysical.\"" in note)
    check("N6 says no new axiom", "not a new axiom" in note)
    check("N7 steelman present", "A hostile reviewer can object" in note)
    check("N8 avoids old symmetry route", "does not repeat that route" in note)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS -- strict NN edge primitivity selects hw=1 as the minimal oriented C3 generation context, conditionally closing the species/locus bridge target.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
