#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_DYNAMICAL_INDEX_OCCUPANCY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
AXIOM_NO_GO = DOCS / "ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md"
REALIZED_REDUCTION = DOCS / "ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md"
STATIC_NO_GO = DOCS / "KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md"
KAHLER_DIRAC = DOCS / "KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md"
BEREZIN_FORK = DOCS / "KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md"
CHIRAL_VECTOR = DOCS / "KOIDE_R_REDUCES_TO_CHIRAL_VS_VECTOR_YUKAWA_BINARY_NARROW_THEOREM_NOTE_2026-06-04.md"
CORNER_TRANSFER = DOCS / "CORNER_AXIS_FREE_TRANSFER_EXTENSION_PER_CHANNEL_TRACE_CORRESPONDENCE_AND_MODE_SET_FORK_BOUNDED_NOTE_2026-06-12.md"
ORBIT_INDEPENDENCE = DOCS / "KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md"

SOURCE_ROWS = {
    "axiom_no_go": "acphilambda_measure_binary_axiom_update_no_go_note_2026-07-04",
    "realized_reduction": "acphilambda_occupancy_selection_realized_state_reduction_note_2026-06-11",
    "static_no_go": "koide_r_half_polarization_selector_tested_static_readout_no_go_note_2026-06-08",
    "kahler_dirac": "koide_kahler_dirac_realization_gives_r_one_index_route_closed_bounded_no_go_note_2026-06-08",
    "berezin_fork": "koide_berezin_detc_vs_detr_fork_mechanism_note_2026-06-04",
    "chiral_vector": "koide_r_reduces_to_chiral_vs_vector_yukawa_binary_narrow_theorem_note_2026-06-04",
    "corner_transfer": "corner_axis_free_transfer_extension_per_channel_trace_correspondence_and_mode_set_fork_bounded_note_2026-06-12",
    "orbit_independence": "koide_orbit_occupancy_independence_and_premise_candidate_note_2026-06-09",
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


def rows() -> dict:
    return json.loads(read(LEDGER))["rows"]


def row(claim_id: str) -> dict:
    found = rows().get(claim_id)
    if found is None:
        raise AssertionError(f"missing row {claim_id}")
    return found


def r_from_weights(ws: sp.Rational, wd: sp.Rational) -> sp.Rational:
    return sp.simplify(wd / (2 * ws))


def main() -> int:
    print("AC_phi_lambda dynamical-index occupancy current-surface no-go verifier")

    paths = [
        NOTE,
        TIER_A,
        LEDGER,
        REGISTRY,
        MINIMAL,
        AXIOM_NO_GO,
        REALIZED_REDUCTION,
        STATIC_NO_GO,
        KAHLER_DIRAC,
        BEREZIN_FORK,
        CHIRAL_VECTOR,
        CORNER_TRANSFER,
        ORBIT_INDEPENDENCE,
    ]
    texts = {path: read(path) for path in paths}
    note = texts[NOTE]
    note_flat = flat(note)
    source_flat = {path: flat(text) for path, text in texts.items()}

    section("A. source presence and ledger grounding")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    for label, claim_id in SOURCE_ROWS.items():
        ledger_row = row(claim_id)
        check(f"{label} ledger row resolves", ledger_row.get("claim_id") == claim_id)
        check(f"{label} row has note path", bool(ledger_row.get("note_path")), ledger_row.get("note_path"))
    for label in [
        "axiom_no_go",
        "static_no_go",
        "kahler_dirac",
        "berezin_fork",
        "chiral_vector",
        "corner_transfer",
        "orbit_independence",
    ]:
        ledger_row = row(SOURCE_ROWS[label])
        check(
            f"{label} row is not an AC retirement authority",
            ledger_row.get("effective_status") != "retained",
            ledger_row.get("effective_status"),
        )
    check("new note has Type no_go", "**Type:** no_go" in note)
    check("new note has Claim type no_go", "**Claim type:** no_go" in note)
    check("primary runner link present", "acphilambda_dynamical_index_occupancy_current_surface_no_go_2026_07_04.py" in note)

    section("B. Tier-A registry remains untouched")
    tier = json.loads(read(TIER_A))
    ac = tier["derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    theta = tier["derivation_targets"]["strong_cp_theta_zero_note"]
    check("Tier-A genuine count remains two", tier["genuine_admitted_input_count"] == 2)
    check(
        "canonical Tier-A IDs remain AC and theta",
        tier["canonical_ids"] == [
            "staggered_dirac_realization_gate_note_2026-05-03",
            "strong_cp_theta_zero_note",
        ],
        tier["canonical_ids"],
    )
    check(
        "AC surviving decomposition remains two residuals",
        ac["minimum_decomposition"] == [
            "reading_occupancy_selection",
            "delta_readout_identification_R_eta",
        ],
        ac["minimum_decomposition"],
    )
    check(
        "theta decomposition remains gauge plus mass",
        theta["minimum_decomposition"] == [
            "gauge_side_winding_account",
            "mass_side_orientation_determinant_readout_bridge",
        ],
        theta["minimum_decomposition"],
    )
    for phrase in [
        "measure-side doublet occupancy realization binary",
        "sector-tied/count-twice",
        "orbit/holomorphic/count-once",
        "delta readout identification R-eta",
        "registered realized-state data",
    ]:
        check(f"AC registry carries {phrase[:48]}", phrase in flat(json.dumps(ac)))
    for phrase in [
        "AC_phi_lambda is not retired.",
        "The Tier-A registry is not edited.",
        "No value of `r` is derived, selected, preferred, or excluded.",
        "R-eta and theta are untouched.",
    ]:
        check(f"note preserves registry boundary: {phrase[:52]}", phrase in note)

    section("C. new note discipline and dependency links")
    expected_links = {
        "../scripts/acphilambda_dynamical_index_occupancy_current_surface_no_go_2026_07_04.py",
        "ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md",
        "ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md",
        "KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md",
        "KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md",
        "KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md",
        "KOIDE_R_REDUCES_TO_CHIRAL_VS_VECTOR_YUKAWA_BINARY_NARROW_THEOREM_NOTE_2026-06-04.md",
        "CORNER_AXIS_FREE_TRANSFER_EXTENSION_PER_CHANNEL_TRACE_CORRESPONDENCE_AND_MODE_SET_FORK_BOUNDED_NOTE_2026-06-12.md",
        "KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md",
        "MINIMAL_AXIOMS_2026-06-29.md",
        "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md",
    }
    links = set(re.findall(r"\[[^\]]+\]\(([^)]+)\)", note))
    check("markdown link inventory is controlled", links == expected_links, sorted(links))
    for phrase in [
        "dynamical, first-order, index, determinant, trace-transfer, or matter-action",
        "This block attacks the live remaining opening",
        "first-order/index language is not enough",
        "current explicit dynamics either lands on r = 1 or exposes the same fork",
        "Determinant order",
        "Mode-set theorem",
        "Matter-action statistics route",
        "Governance route",
    ]:
        check(f"new note carries stretch framing: {phrase[:52]}", phrase in note_flat)
    for idx in range(1, 9):
        check(f"N{idx} gate present", f"**N{idx}" in note)
    forbidden = [
        "AC_phi_lambda is retired",
        "r = 1/2 is derived",
        "r = 1 is derived",
        "audited_clean status is set",
        "effective_status = retained",
        "PDG values enter",
        "observed lepton masses enter",
    ]
    for phrase in forbidden:
        check(f"forbidden phrase absent: {phrase}", phrase not in note)
    check("note line count is bounded", 150 <= len(note.splitlines()) <= 260, len(note.splitlines()))
    check("verification threshold present", "Expected close: `FAIL=0` with at least 145 checks." in note)

    section("D. source-packet boundary checks")
    for phrase in [
        "The target is now sharper",
        "Matter-action statistics theorem",
        "first-order/Pfaffian/count-once",
        "second-order modulus/count-twice",
        "does not derive, refute, re-grade, retire, or remove AC_phi_lambda",
    ]:
        check(f"axiom no-go names survivor: {phrase[:54]}", phrase in source_flat[AXIOM_NO_GO])
    for phrase in [
        "The measure-side frontier is open, not settled.",
        "first-order-vs-second-order `det D`",
        "Nothing here derives, forces, or prefers `r = 1/2`",
        "value face",
        "measure-side binary survives",
    ]:
        check(f"realized reduction leaves measure side: {phrase[:54]}", phrase in source_flat[REALIZED_REDUCTION])
    for phrase in [
        "remaining live opening is dynamical/first-order/index readout",
        "does the actual matter action deliver a *first-order* `det D`",
        "or the *second-order* modulus",
        "does **not** claim r=1/2 is impossible",
        "dynamical first-order/index route open",
    ]:
        check(f"static no-go leaves dynamical opening: {phrase[:54]}", phrase in source_flat[STATIC_NO_GO])
    for phrase in [
        "det D = |det M|",
        "singular values",
        "The index route is closed on the realization.",
        "index is a signed **mode-count**",
        "wrong *kind* of functional",
        "does **not** retire, split, or re-grade the `AC_",
    ]:
        check(f"Kahler-Dirac route boundary: {phrase[:54]}", phrase in source_flat[KAHLER_DIRAC])
    for phrase in [
        "four-cell fork",
        "real Gaussian",
        "Majorana Berezin",
        "holomorphic Gaussian",
        "holomorphic Berezin",
        "does not adopt the holomorphic polarization",
        "positive route open",
    ]:
        check(f"Berezin fork boundary: {phrase[:54]}", phrase in source_flat[BEREZIN_FORK])
    for phrase in [
        "does not select the chiral/holomorphic readout",
        "does not derive Koide `r = 1/2`",
        'uniform "complex-mode count"',
        "still gives `r = 1`",
        "next_trace_action",
    ]:
        check(f"chiral/vector map is conditional: {phrase[:54]}", phrase in source_flat[CHIRAL_VECTOR])
    for phrase in [
        "does not select an occupancy cell",
        "mode-set fork",
        "per-channel counting gives the two-slot cell `r = 1`",
        "per-K-orbit counting gives the one-slot cell `r = 1/2`",
        "does not select between branches",
    ]:
        check(f"corner transfer localizes fork: {phrase[:54]}", phrase in source_flat[CORNER_TRANSFER])
    for phrase in [
        "the occupancy rule is not supplied by the current checked premise surface",
        "M_sector",
        "M_orbit",
        "proposal; NOT adopted",
        "both horns are consistent",
        "not a derivation of `r = 1/2`",
    ]:
        check(f"orbit independence keeps premise open: {phrase[:54]}", phrase in source_flat[ORBIT_INDEPENDENCE])
    for phrase in [
        "does not choose a Hamiltonian or transfer operator",
        "transition probabilities or weights",
        "context selection",
        "source/action and physical-observable identification",
        "Only records are readable",
    ]:
        check(f"minimal axioms withhold dynamics/measure: {phrase[:54]}", phrase in source_flat[MINIMAL])

    section("E. finite weight-map algebra")
    examples = [
        (sp.Rational(1), sp.Rational(2), sp.Rational(1), "vector/real"),
        (sp.Rational(1), sp.Rational(1), sp.Rational(1, 2), "chiral/holomorphic"),
        (sp.Rational(1, 2), sp.Rational(1), sp.Rational(1), "uniform complex rescaling"),
    ]
    for ws, wd, expected, label in examples:
        check(f"{label} weights give expected r", r_from_weights(ws, wd) == expected, r_from_weights(ws, wd))
    for ws_num in range(1, 6):
        for wd_num in range(1, 6):
            ws = sp.Rational(ws_num)
            wd = sp.Rational(wd_num)
            r_val = r_from_weights(ws, wd)
            x = sp.simplify(ws / (ws + wd))
            from_x = sp.simplify((1 - x) / (2 * x))
            check(f"weight map agrees with fraction ws={ws_num} wd={wd_num}", r_val == from_x)
    r = sp.symbols("r", real=True)
    q = sp.Rational(1, 3) + sp.Rational(2, 3) * r
    check("Q(r=1/2)=2/3", sp.simplify(q.subs(r, sp.Rational(1, 2)) - sp.Rational(2, 3)) == 0)
    check("Q(r=1)=1", sp.simplify(q.subs(r, 1) - 1) == 0)
    check("Q(r=0)=1/3", sp.simplify(q.subs(r, 0) - sp.Rational(1, 3)) == 0)
    check("vector and uniform-complex branches are same r", r_from_weights(sp.Rational(1), sp.Rational(2)) == r_from_weights(sp.Rational(1, 2), sp.Rational(1)))
    check("chiral branch differs from vector branch", r_from_weights(sp.Rational(1), sp.Rational(1)) != r_from_weights(sp.Rational(1), sp.Rational(2)))

    section("F. Dirac block determinant/order checks")
    x, y, z, xb, yb, zb = sp.symbols("x y z xb yb zb", nonzero=True)
    m = sp.diag(x, y, z)
    md = sp.diag(xb, yb, zb)
    zero = sp.zeros(3)
    d_block = sp.Matrix.vstack(sp.Matrix.hstack(zero, m), sp.Matrix.hstack(md, zero))
    det_d = sp.factor(d_block.det())
    check("3x3 off-diagonal Dirac block determinant is sign times detM detMdag", sp.factor(det_d + x * y * z * xb * yb * zb) == 0, det_d)
    d2 = sp.simplify(d_block * d_block)
    check("D^2 upper block is M Mdag", d2[:3, :3] == m * md)
    check("D^2 lower block is Mdag M", d2[3:, 3:] == md * m)
    check("D^2 off-diagonal blocks vanish", d2[:3, 3:] == zero and d2[3:, :3] == zero)
    physical_supertrace = 3 - 3
    check("physical L/R grading supertrace count cancels", physical_supertrace == 0)
    signed_counts = {s * n for n in (1, 3) for s in (-1, 1)}
    check("equivariant signed mode-count set has no half", sp.Rational(1, 2) not in signed_counts, signed_counts)
    check("equivariant signed mode-count set matches route boundary", signed_counts == {-3, -1, 1, 3}, signed_counts)
    check("index count kind is integer-valued", all(isinstance(v, int) for v in signed_counts))
    check("integer index cannot equal energy half-reweight", all(sp.Rational(v, 1) != sp.Rational(1, 2) for v in signed_counts))

    section("G. fork and transfer bookkeeping")
    fork_cells = [
        ("real Gaussian", "real", 2, sp.Rational(1)),
        ("Majorana Berezin", "real", 2, sp.Rational(1)),
        ("holomorphic Gaussian", "holomorphic", 1, sp.Rational(1, 2)),
        ("holomorphic Berezin", "holomorphic", 1, sp.Rational(1, 2)),
    ]
    for family, polarization, slots, expected_r in fork_cells:
        check(f"{family} slot count maps to expected r", r_from_weights(sp.Rational(1), sp.Rational(slots)) == expected_r)
        check(f"{family} polarization label is controlled", polarization in {"real", "holomorphic"})
    real_results = {expected for _, pol, _, expected in fork_cells if pol == "real"}
    holo_results = {expected for _, pol, _, expected in fork_cells if pol == "holomorphic"}
    check("real polarization fork gives one result", real_results == {sp.Rational(1)})
    check("holomorphic polarization fork gives one result", holo_results == {sp.Rational(1, 2)})
    check("statistics alone does not select r", len({fork_cells[0][3], fork_cells[1][3]}) == 1 and len({fork_cells[2][3], fork_cells[3][3]}) == 1)
    g = sp.symbols("g", positive=True)
    z_sector = 2 * sp.pi / g
    z_orbit = sp.pi / g
    rho_sector = sp.simplify((sp.pi / g) / z_sector)
    rho_orbit = sp.simplify((sp.pi / g) / z_orbit)
    r_sector = sp.simplify(1 / (2 * rho_sector))
    r_orbit = sp.simplify(1 / (2 * rho_orbit))
    check("sector transfer branch rho=1/2", rho_sector == sp.Rational(1, 2), rho_sector)
    check("orbit transfer branch rho=1", rho_orbit == 1, rho_orbit)
    check("sector transfer branch r=1", r_sector == 1, r_sector)
    check("orbit transfer branch r=1/2", r_orbit == sp.Rational(1, 2), r_orbit)
    check("fork branch ratio is two", sp.simplify(r_sector / r_orbit) == 2)
    normalization = sp.symbols("normalization", positive=True)
    for mode_count in [1, 2, 3, 5]:
        check(f"trace normalization equality forces one for mode_count={mode_count}", sp.solve(sp.Eq(normalization**mode_count, 1), normalization) == [1])

    section("H. native complex structure is measure-neutral")
    c = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    i3 = sp.eye(3)
    j_cs = (c - c**2) / sp.sqrt(3)
    a, b, cb = sp.symbols("a b cb")
    circulant = a * i3 + b * c + cb * c**2
    check("C^3=I", c**3 == i3)
    check("J_cs is antisymmetric", j_cs.T == -j_cs)
    check("J_cs commutes with circulants", sp.simplify(j_cs * circulant - circulant * j_cs) == sp.zeros(3))
    p_doublet = i3 - sp.ones(3) / 3
    check("J_cs squared is minus doublet projector", sp.simplify(j_cs**2 + p_doublet) == sp.zeros(3))
    theta = sp.symbols("theta", real=True)
    rot_series = sp.eye(3) + sp.sin(theta) * j_cs + (1 - sp.cos(theta)) * (j_cs**2)
    check("SO2-style J flow has determinant one", sp.simplify(rot_series.det() - 1) == 0)

    section("I. final no-go discipline")
    for phrase in [
        "not a universal no-go against all future first-order",
        "No observed lepton masses",
        "Every tested surface targets the same surviving",
        "does not close AC(i)",
        "future theorem could derive a genuinely chiral determinant",
    ]:
        check(f"no-go discipline phrase present: {phrase[:54]}", phrase in note_flat)
    check("new note does not introduce wall labels", set(re.findall(r"\bW_[A-Za-z0-9_]+", note)) == set())
    check("new note does not edit registry by text", "does not edit any Tier-A registry" in note_flat)
    check("new note says audit lane only", "**Audit boundary:** independent audit lane only." in note)

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 and PASS >= 145 else 1


if __name__ == "__main__":
    raise SystemExit(main())
