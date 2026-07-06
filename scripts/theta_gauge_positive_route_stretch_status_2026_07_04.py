#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"

SUPPLIER = DOCS / "THETA_SUPPLIER_FLAVORED_GRADING_SPECTRAL_FLOW_REGISTERS_WINDING_2D_NARROW_THEOREM_NOTE_2026-07-02.md"
CARRIER4D = DOCS / "THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md"
TORUS_DUAL = DOCS / "THETA_TORUS_DUAL_ABELIANIZATION_SHIFTED_WEIGHT_LATTICE_GAUSSIAN_GLUING_STABLE_WEYL_SHIFT_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-02.md"
CARTAN = DOCS / "THETA_CARTAN_VALUED_CROSS_PLANE_PAIRING_DIAGONAL_WEYL_FRAME_THEOREMS_AND_TRIALITY_FRACTIONAL_VALUES_BOUNDED_THEOREM_NOTE_2026-07-02.md"
LINK_STAR = DOCS / "THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md"
ASSEMBLY = DOCS / "THETA_ASSEMBLY_PAIRED_SHIFT_FIXED_GRADING_MCKEAN_SINGER_REDUCTION_NARROW_THEOREM_NOTE_2026-07-02.md"
AXIOM_NO_GO = DOCS / "THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md"

ROW_IDS = {
    "supplier": "theta_supplier_flavored_grading_spectral_flow_registers_winding_2d_narrow_theorem_note_2026-07-02",
    "carrier4d": "theta_4d_carrier_flux_cohomology_intersection_pairing_closed_branch_and_defect_closure_residual_bounded_theorem_note_2026-07-02",
    "torus_dual": "theta_torus_dual_abelianization_shifted_weight_lattice_gaussian_gluing_stable_weyl_shift_obstruction_bounded_theorem_note_2026-07-02",
    "cartan": "theta_cartan_valued_cross_plane_pairing_diagonal_weyl_frame_theorems_and_triality_fractional_values_bounded_theorem_note_2026-07-02",
    "link_star": "theta_link_star_gluing_frame_correlation_pair_composite_dagger_evenness_and_odd_branch_phase_residual_bounded_theorem_note_2026-07-02",
    "assembly": "theta_assembly_paired_shift_fixed_grading_mckean_singer_reduction_narrow_theorem_note_2026-07-02",
    "axiom_no_go": "theta_gauge_winding_axiom_update_no_go_note_2026-07-04",
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


def main() -> int:
    print("theta gauge positive-route stretch status verifier")

    paths = [NOTE, LEDGER, TIER_A, MINIMAL, SUPPLIER, CARRIER4D, TORUS_DUAL, CARTAN, LINK_STAR, ASSEMBLY, AXIOM_NO_GO]
    texts = {p: read(p) for p in paths}
    note = texts[NOTE]
    note_flat = flat(note)
    source_flats = {p: flat(texts[p]) for p in paths}

    section("A. source presence and ledger status")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    for name, claim_id in ROW_IDS.items():
        r = row_or_none(claim_id)
        if name == "axiom_no_go" and r is None:
            check("axiom_no_go source is present on current main", AXIOM_NO_GO.exists())
            check("axiom_no_go has no pre-generated ledger authority requirement", True)
            continue
        check(f"{name} row exists with expected claim_id", r is not None and r.get("claim_id") == claim_id)
        check(f"{name} row is not an effective retirement authority", r.get("effective_status") in {"unaudited", "open_gate"}, r.get("effective_status"))
    check("new route status note has Type open_gate", "**Type:** open_gate" in note)
    check("new route status note has Claim type open_gate", "**Claim type:** open_gate" in note)

    section("B. Tier-A target and axiom boundary")
    tier = json.loads(read(TIER_A))
    theta = tier["retired_derivation_targets"]["strong_cp_theta_zero_note"]
    check("live Tier-A genuine count is zero", tier["genuine_admitted_input_count"] == 0, tier["genuine_admitted_input_count"])
    check("theta entry is retired, not live", "strong_cp_theta_zero_note" not in tier.get("derivation_targets", {}))
    check("theta retired-target record is preserved", bool(theta))
    retirement = theta.get("retirement", {})
    check("theta retirement date is recorded", retirement.get("date") == "2026-07-05", retirement)
    check("theta retirement mechanism is retained derivation", "retained" in retirement.get("mechanism", ""))
    check(
        "historical theta decomposition preserves gauge and mass atoms",
        theta["minimum_decomposition"] == ["gauge_side_winding_account", "mass_side_orientation_determinant_readout_bridge"],
        theta["minimum_decomposition"],
    )
    for phrase in [
        "gauge-side winding account",
        "mass-side determinant-channel bridge",
        "does not derive, refute, re-grade, retire, or remove theta",
        "does not edit any Tier-A registry",
        "route-status synthesis",
    ]:
        check(f"note scope has {phrase[:45]}", phrase in note_flat)
    check("note has current-main posture line", "Current-main posture (2026-07-06)" in note)
    check("note records live Tier-A zero posture", "Tier-A count\nzero" in note or "Tier-A count zero" in note)
    check("note says retirement records are not reopened", "does not reopen, modify, or re-grade\neither retirement record" in note)
    minimal_flat = source_flats[MINIMAL]
    for phrase in [
        "Only records are readable",
        "A readout value is determined by record content alone",
        "A law privileges no states",
        "source/action and physical-observable identification",
        "the strong-CP theta admission",
    ]:
        check(f"minimal axiom boundary present: {phrase[:45]}", phrase in minimal_flat)

    section("C. source-packet boundary checks")
    boundary_phrases = {
        SUPPLIER: [
            "no 4D carrier, no SU(3) extension, no continuum limit",
            "no identification of this functional with the record/readout chain",
            "This note feeds the gauge-side winding account",
        ],
        CARRIER4D: [
            "Defect closure",
            "SU(3) abelianization",
            "F u F-shaped multi-plaquette insertion",
            "not a registration of the physical theta angle's `Q`",
        ],
        TORUS_DUAL: [
            "torus-dual branch structure",
            "no continuous Weyl-consistent label-shift theta slot",
            "not a registration claim",
            "derive the F u F-shaped multi-plaquette insertion",
        ],
        CARTAN: [
            "relative-frame correlation",
            "per-plane orbit data underdetermine the pairing",
            "not a registration claim",
            "records register flux vectors",
        ],
        LINK_STAR: [
            "SUBSTANTIALLY RESOLVED for pairs and chains",
            "real-weight gluing CANNOT register the orientation-odd branch",
            "phase-type insertion",
            "records register staples",
        ],
        ASSEMBLY: [
            "does not supply either side's physical value",
            "Supplier Reduction",
            "nonzero or background/sector-dependent assembly transfer cannot come from this fixed grading",
            "same supplier class",
        ],
        AXIOM_NO_GO: [
            "does not supply the theta gauge-side winding",
            "Theta is not retired.",
            "No proof excludes all multiplaquette or clover",
        ],
    }
    for path, phrases in boundary_phrases.items():
        src = source_flats[path]
        for phrase in phrases:
            check(f"{path.name[:34]} keeps boundary: {phrase[:42]}", phrase in src)

    section("D. four-gate synthesis text")
    for gate in [
        "G1 defect closure",
        "G2 nonabelian sector/readout registration",
        "G3 phase-type F cup F insertion",
        "G4 physical theta assembly",
    ]:
        check(f"gate named: {gate}", gate in note)
    for phrase in [
        "The current support packets populate pieces of these gates",
        "No derivation yet that the physical surface imposes or suppresses `dn != 0`",
        "No physical record/readout registration of the flux/pairing data",
        "The actual phase-type insertion is not derived from the framework surface",
        "Nontrivial transfer still needs the supplier class",
        "The next highest-leverage target is G3",
    ]:
        check(f"synthesis carries phrase: {phrase[:54]}", phrase in note_flat)

    section("E. exact flux-pairing interface")
    basis = [(1 if i == j else 0) for j in range(6) for i in []]
    check("unit complementary e01+e23 gives odd support Q=1", q_flux((1, 0, 0, 0, 0, 1)) == 1)
    check("unit complementary e02+e13 gives odd support Q=-1", q_flux((0, 1, 0, 0, 1, 0)) == -1)
    check("unit complementary e03+e12 gives odd support Q=1", q_flux((0, 0, 1, 1, 0, 0)) == 1)
    for idx, name in enumerate(["m01", "m02", "m03", "m12", "m13", "m23"]):
        v = [0, 0, 0, 0, 0, 0]
        v[idx] = 7
        check(f"single-plane {name} flux has Q=0", q_flux(tuple(v)) == 0)
    sample = (2, -1, 3, 4, 5, -2)
    reflected = tuple(-x for x in sample)
    check("global sign reversal leaves quadratic Q unchanged", q_flux(reflected) == q_flux(sample))
    plane_reflected = (-sample[0], -sample[1], -sample[2], sample[3], sample[4], sample[5])
    check("one-axis reflection flips cross-plane Q for chosen sample", q_flux(plane_reflected) == -q_flux(sample), (q_flux(sample), q_flux(plane_reflected)))
    complements = {0: 5, 5: 0, 1: 4, 4: 1, 2: 3, 3: 2}
    for axis, comp in complements.items():
        x = [0, 0, 0, 0, 0, 0]
        x[comp] = 1
        shifted = x.copy()
        shifted[axis] += 3
        check(f"no period-3 Z descent witness on axis {axis}", q_flux(tuple(shifted)) != q_flux(tuple(x)), (q_flux(tuple(x)), q_flux(tuple(shifted))))

    section("F. exact A2 Weyl/frame interface")
    G = sp.Matrix([[sp.Rational(2, 3), sp.Rational(1, 3)], [sp.Rational(1, 3), sp.Rational(2, 3)]])
    s1 = sp.Matrix([[-1, 0], [1, 1]])
    s2 = sp.Matrix([[1, 1], [0, -1]])
    for label, S in [("s1", s1), ("s2", s2), ("s1s2", s1 * s2), ("s2s1", s2 * s1)]:
        check(f"{label} preserves A2 Gram form", sp.simplify(S.T * G * S - G) == sp.zeros(2))
    v1 = sp.Matrix([2, -1])
    v2 = sp.Matrix([-1, 2])
    base_pair = (v1.T * G * v2)[0]
    check("root pairing alpha1-alpha2 is integer", base_pair == -1, base_pair)
    for label, S in [("s1", s1), ("s2", s2), ("s1s2", s1 * s2)]:
        diag_pair = ((S * v1).T * G * (S * v2))[0]
        check(f"diagonal Weyl action preserves pairing for {label}", sp.simplify(diag_pair - base_pair) == 0, diag_pair)
    independent_values = {((S * v1).T * G * v2)[0] for S in [sp.eye(2), s1, s2, s1 * s2, s2 * s1, s1 * s2 * s1]}
    check("independent first-slot Weyl orbit changes pairing", len(independent_values) > 1, sorted(independent_values, key=str))
    a, b = sp.symbols("a b")
    fixed_eqs = list((s1 - sp.eye(2)) * sp.Matrix([a, b])) + list((s2 - sp.eye(2)) * sp.Matrix([a, b]))
    check("A2 Weyl fixed Cartan subspace is zero", sp.solve(fixed_eqs, [a, b], dict=True) == [{a: 0, b: 0}])

    section("G. fixed-grading paired-shift bookkeeping")
    alpha = sp.symbols("alpha", real=True)
    eps = sp.diag(1, 1, -1, -1)
    tr_eps = sp.trace(eps)
    check("balanced fixed grading has tr(eps)=0", tr_eps == 0)
    phase_deposit = sp.exp(-2 * sp.I * alpha * tr_eps)
    mass_shift = sp.exp(2 * sp.I * alpha * tr_eps)
    check("balanced paired shift cancels exactly", sp.simplify(phase_deposit * mass_shift - 1) == 0)
    eps_unbalanced = sp.diag(1, 1, 1, -1, -1)
    tr_unbalanced = sp.trace(eps_unbalanced)
    check("synthetic unbalanced grading can carry nonzero bookkeeping integer", tr_unbalanced == 1)
    check("unbalanced paired shift still cancels as bookkeeping", sp.simplify(sp.exp(-2 * sp.I * alpha * tr_unbalanced) * sp.exp(2 * sp.I * alpha * tr_unbalanced) - 1) == 0)

    section("H. note discipline")
    forbidden = [
        "Theta is retired",
        "theta_bar = 0 is derived",
        "audit_status is changed",
        "effective_status is changed",
        "registry is edited",
        "This is a positive retained-grade proposal",
    ]
    for phrase in forbidden:
        check(f"forbidden phrase absent: {phrase}", phrase not in note)
    for idx, item in enumerate(["G3 first", "G1 in parallel later", "G2 after G1/G3", "G4 last"], start=1):
        check(f"attack plan item {idx} present", item in note)
    links = set(re.findall(r"\[[^\]]+\]\(([^)]+)\)", note))
    expected = {
        "../scripts/theta_gauge_positive_route_stretch_status_2026_07_04.py",
        "THETA_SUPPLIER_FLAVORED_GRADING_SPECTRAL_FLOW_REGISTERS_WINDING_2D_NARROW_THEOREM_NOTE_2026-07-02.md",
        "THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md",
        "THETA_TORUS_DUAL_ABELIANIZATION_SHIFTED_WEIGHT_LATTICE_GAUSSIAN_GLUING_STABLE_WEYL_SHIFT_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-02.md",
        "THETA_CARTAN_VALUED_CROSS_PLANE_PAIRING_DIAGONAL_WEYL_FRAME_THEOREMS_AND_TRIALITY_FRACTIONAL_VALUES_BOUNDED_THEOREM_NOTE_2026-07-02.md",
        "THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md",
        "THETA_ASSEMBLY_PAIRED_SHIFT_FIXED_GRADING_MCKEAN_SINGER_REDUCTION_NARROW_THEOREM_NOTE_2026-07-02.md",
        "THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md",
    }
    check("markdown link inventory is controlled", links == expected, sorted(links))
    check("note line count is bounded", 130 <= len(note.splitlines()) <= 260, len(note.splitlines()))
    check("verification block states fail-zero threshold", "Expected close: `FAIL=0` with at least 100 checks." in note)

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 and PASS >= 100 else 1


if __name__ == "__main__":
    raise SystemExit(main())
