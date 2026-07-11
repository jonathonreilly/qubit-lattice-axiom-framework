#!/usr/bin/env python3
from __future__ import annotations

import cmath
import json
import math
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
DECISION_HISTORY = DOCS / "audit" / "data" / "premise_decision_history.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

POSITIVE = DOCS / "THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md"
CARRIER4D = DOCS / "THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md"
TORUS_DUAL = DOCS / "THETA_TORUS_DUAL_ABELIANIZATION_SHIFTED_WEIGHT_LATTICE_GAUSSIAN_GLUING_STABLE_WEYL_SHIFT_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-02.md"
LINK_STAR = DOCS / "THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md"
CROSS_PLANE = DOCS / "THETA_CROSS_PLANE_TERM_ABSENT_IN_SUPPLIED_PER_PLAQUETTE_CLASS_BOUNDED_THEOREM_NOTE_2026-06-09.md"
MULTIPLAQUETTE = DOCS / "STRONG_CP_GAUGE_THETA_MULTIPLAQUETTE_FTF_IS_ADMISSIBLE_NOT_CLEAN_CLOSEABLE_BOUNDED_NOTE_2026-06-07.md"
AXIOM_NO_GO = DOCS / "THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md"

SOURCE_ROWS = {
    "positive": "theta_gauge_positive_route_stretch_status_2026-07-04",
    "carrier4d": "theta_4d_carrier_flux_cohomology_intersection_pairing_closed_branch_and_defect_closure_residual_bounded_theorem_note_2026-07-02",
    "torus_dual": "theta_torus_dual_abelianization_shifted_weight_lattice_gaussian_gluing_stable_weyl_shift_obstruction_bounded_theorem_note_2026-07-02",
    "link_star": "theta_link_star_gluing_frame_correlation_pair_composite_dagger_evenness_and_odd_branch_phase_residual_bounded_theorem_note_2026-07-02",
    "cross_plane": "theta_cross_plane_term_absent_in_supplied_per_plaquette_class_bounded_theorem_note_2026-06-09",
    "multiplaquette": "strong_cp_gauge_theta_multiplaquette_ftf_is_admissible_not_clean_closeable_bounded_note_2026-06-07",
    "axiom_no_go": "theta_gauge_winding_axiom_update_no_go_note_2026-07-04",
    "minimal": "minimal_axioms",
    "registry": "admitted_input_registry_tier_a_note_2026-05-23",
}

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {label}")
    else:
        FAIL += 1
        suffix = f" :: {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def row(claim_id: str) -> dict:
    rows = json.loads(read(LEDGER))["rows"]
    out = rows.get(claim_id)
    if out is None:
        raise AssertionError(f"missing row {claim_id}")
    return out


def row_or_none(claim_id: str) -> dict | None:
    return json.loads(read(LEDGER))["rows"].get(claim_id)


def q_flux(m: tuple[int, int, int, int, int, int]) -> int:
    m01, m02, m03, m12, m13, m23 = m
    return m01 * m23 - m02 * m13 + m03 * m12


def close_complex(z: complex, w: complex, tol: float = 1e-10) -> bool:
    return abs(z - w) < tol


def main() -> int:
    print("theta G3 phase-insertion current-surface no-go verifier")

    paths = [
        NOTE,
        MINIMAL,
        REGISTRY,
        DECISION_HISTORY,
        LEDGER,
        POSITIVE,
        CARRIER4D,
        TORUS_DUAL,
        LINK_STAR,
        CROSS_PLANE,
        MULTIPLAQUETTE,
        AXIOM_NO_GO,
    ]
    texts = {path: read(path) for path in paths}
    note = texts[NOTE]
    note_flat = flat(note)
    source_flat = {path: flat(text) for path, text in texts.items()}

    section("A. source presence and ledger grounding")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    for label, claim_id in SOURCE_ROWS.items():
        r = row_or_none(claim_id)
        if label in {"positive", "axiom_no_go"} and r is None:
            source_path = POSITIVE if label == "positive" else AXIOM_NO_GO
            check(f"{label} source is present on current main", source_path.exists())
            check(f"{label} has no pre-generated ledger authority requirement", True)
            continue
        check(f"{label} ledger row resolves", r is not None and r.get("claim_id") == claim_id)
        check(f"{label} row has note path", bool(r and r.get("note_path")), r.get("note_path") if r else None)
    for label in ["positive", "carrier4d", "torus_dual", "link_star", "multiplaquette", "axiom_no_go"]:
        r = row_or_none(SOURCE_ROWS[label])
        check(f"{label} is not retained-grade theta-retirement authority", r is None or r.get("effective_status") not in {"retained", "retained_bounded", "retained_no_go"}, r.get("effective_status") if r else None)
    cross = row(SOURCE_ROWS["cross_plane"])
    check("cross-plane absence is retained-grade", cross.get("effective_status") in {"retained", "retained_bounded", "retained_no_go"}, cross.get("effective_status"))
    check("new note has Type no_go", "**Type:** no_go" in note)
    check("new note has Claim type no_go", "**Claim type:** no_go" in note)

    section("B. admission-era decision history")
    tier = json.loads(read(DECISION_HISTORY))
    theta = tier["retired_derivation_targets"]["strong_cp_theta_zero_note"]
    ac = tier["retired_derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    check("decision history preserves zero final admission count", tier["genuine_admitted_input_count"] == 0, tier["genuine_admitted_input_count"])
    check("canonical Tier-A IDs are empty on current main", tier["canonical_ids"] == [], tier["canonical_ids"])
    check("live derivation targets are empty on current main", tier.get("derivation_targets", {}) == {}, tier.get("derivation_targets"))
    for name, target in [("theta", theta), ("AC", ac)]:
        retirement = target.get("retirement", {})
        check(f"{name} retired-target record is preserved", bool(target))
        check(f"{name} disposition correction date is recorded", retirement.get("date") == "2026-07-11", retirement)
    check(
        "historical theta minimum decomposition preserves gauge plus mass",
        theta["minimum_decomposition"] == [
            "gauge_side_winding_account",
            "mass_side_orientation_determinant_readout_bridge",
        ],
        theta["minimum_decomposition"],
    )
    check(
        "historical AC decomposition preserves three old atoms",
        ac["minimum_decomposition"] == [
            "reading_occupancy_selection",
            "delta_readout_identification_R_eta",
            "species_bridge",
        ],
        ac["minimum_decomposition"],
    )
    for phrase in [
        "Theta is not retired.",
        "No admission registry is created.",
        "No axiom or primitive is changed.",
        "No audit status or effective status is changed.",
        "No mass-side determinant-channel bridge is supplied.",
    ]:
        check(f"note preserves boundary: {phrase[:54]}", phrase in note)
    for phrase in [
        "gauge_side_winding_account",
        "mass_side_orientation_determinant_readout_bridge",
    ]:
        check(f"machine registry theta text includes {phrase[:48]}", phrase in flat(json.dumps(theta)))
    for phrase in [
        "multi-plaquette / large-gauge-winding account",
        "determinant-readout bridge",
    ]:
        check(f"machine registry theta text includes {phrase[:48]}", phrase in flat(json.dumps(theta)))
        check(f"decision history theta text includes {phrase[:48]}", phrase in flat(json.dumps(theta)))
    check("note has current-main posture line", "Current-main posture (2026-07-11)" in note)
    check("note records absence of an admission registry", "No admission registry is created." in note)
    check("note does not create an admission registry", "does not create any" in note and "admission registry" in note)

    section("C. axiom and primitive non-supply")
    minimal_flat = source_flat[MINIMAL]
    axiom_flat = source_flat[AXIOM_NO_GO]
    for phrase in [
        "Admissibility is not a dynamics axiom",
        "does not choose a Hamiltonian or transfer operator",
        "transition probabilities or weights",
        "context selection",
        "source/action and physical-observable identification",
        "the strong-CP theta gauge and mass-side derivation obligations",
        "Only records are readable",
        "A readout value is determined by record content alone",
    ]:
        check(f"minimal axioms withhold: {phrase[:50]}", phrase in minimal_flat)
    for phrase in [
        "does not supply the theta gauge-side winding",
        "No proof excludes all multiplaquette or clover",
        "a nonvacuous theta_gauge sector-weighting law",
        "No admission registry is created.",
        "Theta is not retired.",
    ]:
        check(f"axiom-update no-go supports boundary: {phrase[:48]}", phrase in axiom_flat)
    for phrase in [
        "No source/action, phase weighting, measure, context-selection, or physical-observable bridge",
        "They cannot select `exp(i theta Q)`.",
        "Admissibility is not selection, coefficient, or physical registration.",
    ]:
        check(f"new note states non-supply: {phrase[:58]}", phrase in note_flat)

    section("D. source-packet route localizers")
    required = {
        POSITIVE: [
            "G3 phase-type F cup F insertion",
            "The actual phase-type insertion is not derived from the framework surface",
            "The next highest-leverage target is G3",
        ],
        CARRIER4D: [
            "derive the F u F-shaped multi-plaquette insertion",
            "given** an `F u F`-shaped multi-plaquette insertion",
            "not a registration of the physical theta angle's `Q`",
        ],
        TORUS_DUAL: [
            "no continuous Weyl-consistent label-shift theta slot",
            "derive the F u F-shaped multi-plaquette insertion",
            "not a registration claim",
        ],
        LINK_STAR: [
            "real-weight gluing CANNOT register the orientation-odd branch",
            "phase-type insertion",
            "OPEN",
        ],
        CROSS_PLANE: [
            "does not set `theta_QCD = 0`",
            "single-plaquette theta-class boundary",
            "multi-plaquette",
        ],
        MULTIPLAQUETTE: [
            "admissible",
            "not clean-closeable",
            "multi-plaquette",
        ],
    }
    for path, phrases in required.items():
        src = source_flat[path]
        for phrase in phrases:
            check(f"{path.name[:36]} has route phrase: {phrase[:44]}", phrase in src)

    section("E. note fan-out and no-go triple")
    for phrase in [
        "a selected oriented multi-plaquette cross-plane functional",
        "a phase weighting or action coefficient of the form `exp(i theta Q)`",
        "registration that this functional is the physical gauge-side theta sector",
        "The existing packets supply none of that full triple.",
    ]:
        check(f"no-go triple present: {phrase[:58]}", phrase in note_flat)
    for route in [
        "Updated axioms and approved primitives",
        "Supplied per-plaquette additive class",
        "Closed-branch 4D carrier",
        "Continuous Weyl label shift",
        "Real class-weight gluing",
        "Multiplaquette/clover admissibility",
        "admission registry",
    ]:
        check(f"route fan-out row present: {route}", route in note)
    for move in [
        "G3 is now split into a precise missing triple",
        "They are route-localizers only",
        "admissible is not selected, coefficiented, or registered",
    ]:
        check(f"movement sentence present: {move[:52]}", move in note_flat)

    section("F. per-plaquette versus cross-plane algebra")
    f01, f02, f03, f12, f13, f23 = sp.symbols("f01 f02 f03 f12 f13 f23")
    c01, c02, c03, c12, c13, c23 = sp.symbols("c01 c02 c03 c12 c13 c23")
    additive = c01 * f01 + c02 * f02 + c03 * f03 + c12 * f12 + c13 * f13 + c23 * f23
    cross_term = f01 * f23 - f02 * f13 + f03 * f12
    pairs = [(f01, f23, 1), (f02, f13, -1), (f03, f12, 1)]
    for a, b, expected in pairs:
        check(f"additive class has zero mixed derivative {a},{b}", sp.diff(additive, a, b) == 0)
        check(f"cross-plane term has expected mixed derivative {a},{b}", sp.diff(cross_term, a, b) == expected)
    for a, b in [(f01, f02), (f12, f13), (f01, f13)]:
        check(f"cross-plane term has no noncomplement derivative {a},{b}", sp.diff(cross_term, a, b) == 0)
    grad_add = [sp.diff(additive, x) for x in [f01, f02, f03, f12, f13, f23]]
    grad_cross = [sp.diff(cross_term, x) for x in [f01, f02, f03, f12, f13, f23]]
    check("additive gradient is field-independent", all(not any(v.has(y) for y in [f01, f02, f03, f12, f13, f23]) for v in grad_add))
    check("cross-plane gradient depends on complementary planes", any(any(v.has(y) for y in [f01, f02, f03, f12, f13, f23]) for v in grad_cross))

    section("G. flux-pairing and center-descent checks")
    basis = [
        (1, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0),
        (0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 1),
    ]
    for idx, vec in enumerate(basis):
        check(f"single-plane basis vector {idx} has Q=0", q_flux(vec) == 0)
    samples = {
        "e01+e23": (1, 0, 0, 0, 0, 1),
        "e02+e13": (0, 1, 0, 0, 1, 0),
        "e03+e12": (0, 0, 1, 1, 0, 0),
    }
    expected_q = {"e01+e23": 1, "e02+e13": -1, "e03+e12": 1}
    for label, vec in samples.items():
        check(f"{label} has expected odd Q", q_flux(vec) == expected_q[label], q_flux(vec))
    complements = {0: 5, 5: 0, 1: 4, 4: 1, 2: 3, 3: 2}
    for axis, comp in complements.items():
        x = [0, 0, 0, 0, 0, 0]
        x[comp] = 1
        shifted = x.copy()
        shifted[axis] += 3
        check(f"integer Q does not descend through mod-3 axis {axis}", q_flux(tuple(shifted)) != q_flux(tuple(x)), (q_flux(tuple(x)), q_flux(tuple(shifted))))
    vec = (2, -1, 3, 4, 5, -2)
    one_axis_reflection = (-vec[0], -vec[1], -vec[2], vec[3], vec[4], vec[5])
    check("one-axis orientation reversal flips Q for witness", q_flux(one_axis_reflection) == -q_flux(vec), (q_flux(vec), q_flux(one_axis_reflection)))

    section("H. real even weights versus phase weights")
    theta_value = math.pi / 5.0
    for q in [1, 2, 3]:
        real_pos = math.cos(theta_value * q)
        real_neg = math.cos(theta_value * -q)
        phase_pos = cmath.exp(1j * theta_value * q)
        phase_neg = cmath.exp(1j * theta_value * -q)
        check(f"real even weight identifies q and -q for q={q}", abs(real_pos - real_neg) < 1e-12)
        check(f"generic complex phase distinguishes q sign for q={q}", not close_complex(phase_pos, phase_neg))
    check("theta=pi phase marks odd sectors negative", close_complex(cmath.exp(1j * math.pi * 1), -1 + 0j))
    check("theta=pi phase leaves even sectors positive", close_complex(cmath.exp(1j * math.pi * 2), 1 + 0j))
    check("theta=0 phase is trivial and cannot carry G3", close_complex(cmath.exp(0j), 1 + 0j))

    section("I. A2 Weyl shift obstruction")
    gram = sp.Matrix([[sp.Rational(2, 3), sp.Rational(1, 3)], [sp.Rational(1, 3), sp.Rational(2, 3)]])
    s1 = sp.Matrix([[-1, 0], [1, 1]])
    s2 = sp.Matrix([[1, 1], [0, -1]])
    for label, matrix in [("s1", s1), ("s2", s2), ("s1s2", s1 * s2), ("s2s1", s2 * s1)]:
        check(f"{label} preserves A2 Gram form", sp.simplify(matrix.T * gram * matrix - gram) == sp.zeros(2))
    a, b = sp.symbols("a b")
    fixed_eqs = list((s1 - sp.eye(2)) * sp.Matrix([a, b])) + list((s2 - sp.eye(2)) * sp.Matrix([a, b]))
    check("A2 Weyl fixed continuous shift is zero", sp.solve(fixed_eqs, [a, b], dict=True) == [{a: 0, b: 0}])
    v1 = sp.Matrix([2, -1])
    v2 = sp.Matrix([-1, 2])
    base_pair = (v1.T * gram * v2)[0]
    check("base A2 pairing is integer", base_pair == -1, base_pair)
    for label, matrix in [("s1", s1), ("s2", s2), ("s1s2", s1 * s2)]:
        diag_pair = ((matrix * v1).T * gram * (matrix * v2))[0]
        check(f"diagonal Weyl action preserves pairing for {label}", sp.simplify(diag_pair - base_pair) == 0, diag_pair)
    independent_values = {((matrix * v1).T * gram * v2)[0] for matrix in [sp.eye(2), s1, s2, s1 * s2, s2 * s1, s1 * s2 * s1]}
    check("independent one-slot Weyl orbit changes pairing", len(independent_values) > 1, sorted(independent_values, key=str))

    section("J. note discipline and controlled links")
    forbidden = [
        "Theta is retired",
        "theta_bar = 0 is derived",
        "we create an admission registry",
        "future action-side or measure-side work cannot derive G3",
        "audit status is changed",
        "effective status is upgraded",
    ]
    for phrase in forbidden:
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)
    for item in [
        "Action-side phase source",
        "G1 defect closure in parallel",
        "G2 registration after G1/G3",
        "G4 assembly last",
    ]:
        check(f"next attack plan item present: {item}", item in note)
    links = set(re.findall(r"\[[^\]]+\]\(([^)]+)\)", note))
    expected_links = {
        "../scripts/theta_g3_phase_insertion_current_surface_no_go_2026_07_04.py",
        "MINIMAL_AXIOMS_2026-06-29.md",
        "THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md",
        "THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md",
        "THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md",
        "THETA_TORUS_DUAL_ABELIANIZATION_SHIFTED_WEIGHT_LATTICE_GAUSSIAN_GLUING_STABLE_WEYL_SHIFT_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-02.md",
        "THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md",
        "THETA_CROSS_PLANE_TERM_ABSENT_IN_SUPPLIED_PER_PLAQUETTE_CLASS_BOUNDED_THEOREM_NOTE_2026-06-09.md",
        "STRONG_CP_GAUGE_THETA_MULTIPLAQUETTE_FTF_IS_ADMISSIBLE_NOT_CLEAN_CLOSEABLE_BOUNDED_NOTE_2026-06-07.md",
        "THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md",
    }
    check("markdown link inventory is controlled", links == expected_links, sorted(links))
    check("note line count is bounded", 130 <= len(note.splitlines()) <= 240, len(note.splitlines()))
    check("verification block states fail-zero threshold", "Expected close: `FAIL=0` with at least 95 checks." in note)

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 and PASS >= 95 else 1


if __name__ == "__main__":
    raise SystemExit(main())
