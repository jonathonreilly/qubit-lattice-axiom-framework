#!/usr/bin/env python3
"""Verifier for the theta G3 central-sector phase-character support note."""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_G3_CENTRAL_SECTOR_PHASE_CHARACTER_EXACT_SUPPORT_NOTE_2026-07-04.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
BLOCK31 = DOCS / "THETA_SU3_STAR_PAIRWISE_REDUCTION_OBSTRUCTION_NO_GO_NOTE_2026-07-04.md"
BLOCK32 = DOCS / "THETA_SU3_STAR_CENTRAL_SECTOR_PROJECTION_EXACT_SUPPORT_NOTE_2026-07-04.md"
LINK_STAR = DOCS / "THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md"
G3_NO_GO = DOCS / "THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
POSITIVE = DOCS / "THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md"
CARRIER4D = DOCS / "THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md"

PASS = 0
FAIL = 0


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        print(f"PASS: {label}")
    else:
        FAIL += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"FAIL: {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "-" * 86)
    print(title)
    print("-" * 86)


def mod3(value: int) -> int:
    return value % 3


Vec = tuple[int, int]


def add_vec(left: Vec, right: Vec) -> Vec:
    return (mod3(left[0] + right[0]), mod3(left[1] + right[1]))


def neg_vec(vec: Vec) -> Vec:
    return (mod3(-vec[0]), mod3(-vec[1]))


def sub_vec(left: Vec, right: Vec) -> Vec:
    return add_vec(left, neg_vec(right))


def is_central(vec: Vec) -> bool:
    return vec == (0, 0)


def product_word(word: list[Vec]) -> tuple[int, Vec]:
    """Return central phase exponent k and vector for prod X^a Z^b."""

    phase = 0
    a = 0
    b = 0
    for c, d in word:
        phase = mod3(phase - b * c)
        a = mod3(a + c)
        b = mod3(b + d)
    return phase, (a, b)


def central_projection_phase(word: list[Vec]) -> int | None:
    phase, vec = product_word(word)
    if is_central(vec):
        return phase
    return None


def oriented_cocycle(triple: tuple[Vec, Vec, Vec]) -> int | None:
    a, b, c = triple
    abc = central_projection_phase([a, b, c])
    acb = central_projection_phase([a, c, b])
    if abc is None or acb is None:
        return None
    return mod3(abc - acb)


def symplectic_area(a: Vec, b: Vec) -> int:
    return mod3(a[0] * b[1] - a[1] * b[0])


def phase_character(q: int, m: int = 1) -> complex:
    omega = np.exp(-2j * np.pi / 3)
    return complex(omega ** mod3(m * q))


def pairwise_signature(triple: tuple[Vec, Vec, Vec]) -> tuple[str, ...]:
    labels: list[str] = []
    for vec in triple:
        labels.append("central" if is_central(vec) else "noncentral")
    for i in range(3):
        for j in range(i + 1, 3):
            vi = triple[i]
            vj = triple[j]
            labels.append("sum:central" if is_central(add_vec(vi, vj)) else "sum:noncentral")
            labels.append("diff:central" if is_central(sub_vec(vi, vj)) else "diff:noncentral")
            labels.append("diff:central" if is_central(sub_vec(vj, vi)) else "diff:noncentral")
    return tuple(sorted(labels))


def close(left: complex | float, right: complex | float, tol: float = 1e-10) -> bool:
    return abs(left - right) < tol


NONCENTRAL: tuple[Vec, ...] = tuple(
    (a, b) for a in range(3) for b in range(3) if (a, b) != (0, 0)
)


SOURCE_ROWS = {
    "block31": "theta_su3_star_pairwise_reduction_obstruction_no_go_note_2026-07-04",
    "block32": "theta_su3_star_central_sector_projection_exact_support_note_2026-07-04",
    "link_star": "theta_link_star_gluing_frame_correlation_pair_composite_dagger_evenness_and_odd_branch_phase_residual_bounded_theorem_note_2026-07-02",
    "g3_no_go": "theta_g3_phase_insertion_current_surface_no_go_note_2026-07-04",
    "positive_route": "theta_gauge_positive_route_stretch_status_2026-07-04",
    "carrier4d": "theta_4d_carrier_flux_cohomology_intersection_pairing_closed_branch_and_defect_closure_residual_bounded_theorem_note_2026-07-02",
    "minimal": "minimal_axioms",
}


def main() -> int:
    print("Theta G3 central-sector phase-character exact support")
    print("=" * 86)

    paths = [
        NOTE,
        MINIMAL,
        TIER_A,
        LEDGER,
        REGISTRY,
        BLOCK31,
        BLOCK32,
        LINK_STAR,
        G3_NO_GO,
        POSITIVE,
        CARRIER4D,
    ]
    texts = {path: read(path) for path in paths}
    note = texts[NOTE]
    note_flat = flat(note)
    minimal_flat = flat(texts[MINIMAL])
    registry_flat = flat(texts[REGISTRY])
    block31_flat = flat(texts[BLOCK31])
    block32_flat = flat(texts[BLOCK32])
    link_flat = flat(texts[LINK_STAR])
    g3_flat = flat(texts[G3_NO_GO])
    positive_flat = flat(texts[POSITIVE])
    carrier_flat = flat(texts[CARRIER4D])
    ledger = json.loads(texts[LEDGER])
    tier = json.loads(texts[TIER_A])

    section("A - source, registry, and status boundaries")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    for label, claim_id in SOURCE_ROWS.items():
        row = ledger["rows"].get(claim_id)
        check(f"ledger row resolves for {label}", row is not None)
        if row:
            check(f"{label} is not effective retained authority", row.get("effective_status") != "retained", row.get("effective_status"))

    theta = tier["derivation_targets"]["strong_cp_theta_zero_note"]
    ac = tier["derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    check("note declares bounded theorem type", "**Type:** bounded_theorem" in note)
    check("note declares bounded_theorem claim type", "**Claim type:** bounded_theorem" in note)
    check("note declares exact-support status", "exact-support source-side split" in note_flat)
    check("runner path is wired in note", Path(__file__).name in note)
    check("Tier-A genuine admitted input count remains two", tier["genuine_admitted_input_count"] == 2)
    check(
        "canonical Tier-A IDs remain AC and theta",
        tier["canonical_ids"]
        == [
            "staggered_dirac_realization_gate_note_2026-05-03",
            "strong_cp_theta_zero_note",
        ],
        tier["canonical_ids"],
    )
    check(
        "theta minimum decomposition remains gauge plus mass",
        theta["minimum_decomposition"]
        == ["gauge_side_winding_account", "mass_side_orientation_determinant_readout_bridge"],
        theta["minimum_decomposition"],
    )
    check(
        "AC minimum decomposition remains two atoms",
        ac["minimum_decomposition"]
        == ["reading_occupancy_selection", "delta_readout_identification_R_eta"],
        ac["minimum_decomposition"],
    )
    for phrase in [
        "Theta is not retired.",
        "The Tier-A registry is not edited.",
        "No physical SU(3) theta sector is registered.",
        "No G3 phase source, coefficient, action entry, or physical weighting law is supplied.",
        "No G2 physical sector/readout theorem is supplied.",
        "No mass-side determinant-channel bridge is supplied.",
        "No audit status or effective status is changed.",
    ]:
        check(f"note preserves boundary: {phrase[:58]}", phrase in note_flat)
    check("human registry keeps theta gauge winding residual", "multi-plaquette / large-gauge-winding account" in registry_flat)
    check("human registry keeps theta mass determinant residual", "determinant-readout bridge" in registry_flat)

    section("B - current-surface non-supply remains explicit")
    for phrase in [
        "source/action and physical-observable identification",
        "central-sector decomposition",
        "readout-context selection",
        "the strong-CP theta admission",
        "Axioms and approved primitives are not Tier-A admitted derivation targets",
    ]:
        check(f"minimal axioms withhold or classify: {phrase[:54]}", phrase in minimal_flat)
    for phrase in [
        "pairwise composite class data do not determine",
        "central-sector projection kills nonclosed triples",
        "records a central phase",
        "real class-weight gluing is orientation-reversal-even",
        "current surface does not derive the G3 phase insertion",
        "oriented functional, phase coefficient, and physical registration",
        "The actual phase-type insertion is not derived from the framework surface",
        "surface: **given** an `F u F`-shaped multi-plaquette insertion",
        "cross-plane intersection pairing",
    ]:
        sources = " ".join([block31_flat, block32_flat, link_flat, g3_flat, positive_flat, carrier_flat, note_flat])
        check(f"source surface contains: {phrase[:58]}", phrase in sources)
    for phrase in [
        "does not create a central-sector cocycle",
        "select a complex character",
        "provide an action coefficient",
        "identify the result as the physical theta gauge sector",
        "does not prove the full 4D continuum or lattice `F cup F` insertion",
    ]:
        check(f"scope discipline states: {phrase[:58]}", phrase in note_flat)

    section("C - exact finite cocycle algebra")
    closed = ((1, 0), (0, 1), (2, 2))
    reflected = ((0, 1), (1, 0), (2, 2))
    open_triple = ((1, 0), (0, 1), (1, 1))
    check("closed witness vector sum closes", is_central(add_vec(add_vec(closed[0], closed[1]), closed[2])))
    check("reflected witness vector sum closes", is_central(add_vec(add_vec(reflected[0], reflected[1]), reflected[2])))
    check("open witness vector sum does not close", not is_central(add_vec(add_vec(open_triple[0], open_triple[1]), open_triple[2])))
    check("closed witness ABC phase is 1", central_projection_phase(list(closed)) == 1, central_projection_phase(list(closed)))
    check("closed witness ACB phase is 0", central_projection_phase([closed[0], closed[2], closed[1]]) == 0)
    check("reflected witness ABC phase is 0", central_projection_phase(list(reflected)) == 0)
    check("reflected witness ACB phase is 1", central_projection_phase([reflected[0], reflected[2], reflected[1]]) == 1)
    check("open witness ABC killed by central projection", central_projection_phase(list(open_triple)) is None)
    check("open witness ACB killed by central projection", central_projection_phase([open_triple[0], open_triple[2], open_triple[1]]) is None)

    q_closed = oriented_cocycle(closed)
    q_reflected = oriented_cocycle(reflected)
    check("closed q_c equals 1", q_closed == 1, q_closed)
    check("reflected q_c equals -1 mod 3", q_reflected == 2, q_reflected)
    check("reflection maps q_c to -q_c", q_reflected == mod3(-q_closed), (q_closed, q_reflected))
    check("open q_c is unavailable, not zero", oriented_cocycle(open_triple) is None)
    check("closed pairwise signatures match under reflection", pairwise_signature(closed) == pairwise_signature(reflected))
    check("closed separate entries are all noncentral", all(not is_central(vec) for vec in closed + reflected))

    all_closed_count = 0
    nonzero_count = 0
    reflection_ok = True
    formula_ok = True
    killed_ok = True
    q_counts = {0: 0, 1: 0, 2: 0}
    for a in NONCENTRAL:
        for b in NONCENTRAL:
            for c in NONCENTRAL:
                total = add_vec(add_vec(a, b), c)
                q = oriented_cocycle((a, b, c))
                if is_central(total):
                    all_closed_count += 1
                    if q is None:
                        killed_ok = False
                        continue
                    q_counts[q] += 1
                    if q != symplectic_area(a, b):
                        formula_ok = False
                    q_reflect = oriented_cocycle((b, a, c))
                    if q_reflect != mod3(-q):
                        reflection_ok = False
                    if q:
                        nonzero_count += 1
                elif q is not None:
                    killed_ok = False
    check("all closed noncentral triples have q_c", killed_ok, {"closed": all_closed_count})
    check("q_c equals first-pair symplectic area for all closed triples", formula_ok)
    check("swapping first two staples reverses q_c for all closed triples", reflection_ok)
    check("closed population has nonzero odd sectors", nonzero_count > 0, {"q_counts": q_counts})
    check("all three q_c sectors occur", all(q_counts[q] > 0 for q in [0, 1, 2]), q_counts)
    check("q=1 and q=2 populations match", q_counts[1] == q_counts[2], q_counts)

    section("D - phase character and real-weight evenness")
    chi_plus = phase_character(q_closed)
    chi_minus = phase_character(q_reflected)
    check("phase character conjugates under reflection", close(chi_minus, chi_plus.conjugate()), (chi_plus, chi_minus))
    check("real parts are orientation-even", close(chi_plus.real, chi_minus.real), (chi_plus.real, chi_minus.real))
    check("imaginary parts are orientation-odd", close(chi_plus.imag, -chi_minus.imag), (chi_plus.imag, chi_minus.imag))
    check("nontrivial character has real part -1/2 on q=1", close(chi_plus.real, -0.5), chi_plus)
    check("nontrivial character has |imag| sqrt(3)/2", close(abs(chi_plus.imag), math.sqrt(3) / 2), chi_plus)
    check("trivial q=0 character is one", close(phase_character(0), 1 + 0j), phase_character(0))
    for m in [1, 2]:
        for q in [0, 1, 2]:
            lhs = phase_character(mod3(-q), m)
            rhs = phase_character(q, m).conjugate()
            check(f"m={m} q={q} reflection conjugacy", close(lhs, rhs), (lhs, rhs))

    real_weight_blind = True
    complex_weight_distinguishes = True
    for q in [1, 2]:
        if not close(phase_character(q).real, phase_character(mod3(-q)).real):
            real_weight_blind = False
        if close(phase_character(q), phase_character(mod3(-q))):
            complex_weight_distinguishes = False
    check("real projection of character cannot distinguish nonzero orientations", real_weight_blind)
    check("complex character distinguishes nonzero oriented branches", complex_weight_distinguishes)

    section("E - note movement and overclaim guards")
    for phrase in [
        "The result is support for the shape of G3, not a derivation of G3.",
        "is the exact finite odd-branch-sensitive slot",
        "Real class weights can see only the even part.",
        "derive a physical action/source law",
        "with coefficient and registration",
        "This exact support is conditional on the supplied central-sector projection",
    ]:
        check(f"note states honest movement: {phrase[:58]}", phrase in note_flat)
    banned = [
        "Theta is retired",
        "theta is retired",
        "theta_bar = 0 is derived",
        "Tier-A registry is edited",
        "G3 is derived",
        "physical G3 phase source is supplied",
        "The physical SU(3) theta sector is registered",
        "A physical SU(3) theta sector is registered",
        "The mass-side determinant-channel bridge is supplied",
        "A mass-side determinant-channel bridge is supplied",
        "retained on the actual surface",
        "would become retained",
        "promoted to retained",
    ]
    for phrase in banned:
        check(f"banned overclaim absent: {phrase}", phrase not in note_flat)

    print("\n" + "=" * 86)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
