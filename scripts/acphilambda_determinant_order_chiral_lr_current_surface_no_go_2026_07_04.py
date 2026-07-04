#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_DETERMINANT_ORDER_CHIRAL_LR_COUPLING_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK13 = DOCS / "ACPHILAMBDA_DYNAMICAL_INDEX_OCCUPANCY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"
INDEX_META = DOCS / "KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md"
SUPERTRACE = DOCS / "SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md"
FIRST_ORDER = DOCS / "KOIDE_FIRST_ORDER_SELECTOR_IS_THE_CHIRAL_LR_COUPLING_NOT_A_SYMMETRY_NARROW_NOTE_2026-06-05.md"
REASSESSMENT = DOCS / "STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md"
KAHLER_DIRAC = DOCS / "KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md"

SOURCE_ROWS = {
    "block13": "acphilambda_dynamical_index_occupancy_current_surface_no_go_note_2026-07-04",
    "index_meta": "koide_r_half_index_readout_non_susy_staggered_dirac_gate_meta_note_2026-06-05",
    "supertrace": "supertrace_index_holomorphic_route_to_koide_r_half_open_lead_note_2026-06-04",
    "first_order": "koide_first_order_selector_is_the_chiral_lr_coupling_not_a_symmetry_narrow_note_2026-06-05",
    "reassessment": "staggered_dirac_exercise_honest_reassessment_note_2026-06-06",
    "kahler_dirac": "koide_kahler_dirac_realization_gives_r_one_index_route_closed_bounded_no_go_note_2026-06-08",
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


def kron(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return sp.kronecker_product(a, b)


def main() -> int:
    print("AC_phi_lambda determinant-order chiral L-R current-surface no-go verifier")

    paths = [
        NOTE,
        TIER_A,
        LEDGER,
        REGISTRY,
        MINIMAL,
        BLOCK13,
        INDEX_META,
        SUPERTRACE,
        FIRST_ORDER,
        REASSESSMENT,
        KAHLER_DIRAC,
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
    expected_classes = {
        "block13": "no_go",
        "index_meta": "meta",
        "supertrace": "open_gate",
        "first_order": "bounded_theorem",
        "reassessment": "bounded_theorem",
        "kahler_dirac": "no_go",
    }
    for label, expected in expected_classes.items():
        ledger_row = row(SOURCE_ROWS[label])
        check(f"{label} claim type is {expected}", ledger_row.get("claim_type") == expected, ledger_row.get("claim_type"))
    check("new note has Type no_go", "**Type:** no_go" in note)
    check("new note has Claim type no_go", "**Claim type:** no_go" in note)

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
        "which grain/statistics the matter action implements",
        "sector-tied/count-twice",
        "orbit/holomorphic/count-once",
        "delta readout identification R-eta",
        "registered realized-state data",
    ]:
        check(f"AC registry carries {phrase[:52]}", phrase in flat(json.dumps(ac)))
    for phrase in [
        "AC_phi_lambda is not retired.",
        "The Tier-A registry is not edited.",
        "No value of `r` is derived, selected, preferred, or excluded.",
        "R-eta and theta are untouched.",
    ]:
        check(f"note preserves boundary: {phrase[:52]}", phrase in note)

    section("C. new note dependency and wording discipline")
    expected_links = {
        "../scripts/acphilambda_determinant_order_chiral_lr_current_surface_no_go_2026_07_04.py",
        "ACPHILAMBDA_DYNAMICAL_INDEX_OCCUPANCY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md",
        "KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md",
        "SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md",
        "KOIDE_FIRST_ORDER_SELECTOR_IS_THE_CHIRAL_LR_COUPLING_NOT_A_SYMMETRY_NARROW_NOTE_2026-06-05.md",
        "STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md",
        "KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md",
        "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md",
        "MINIMAL_AXIOMS_2026-06-29.md",
    }
    links = set(re.findall(r"\[[^\]]+\]\(([^)]+)\)", note))
    check("markdown link inventory is controlled", links == expected_links, sorted(links))
    for phrase in [
        "focused determinant-order route test",
        "physical chiral/Pfaffian/holomorphic determinant bridge",
        "determinant-order closure still needs a new theorem",
        "Physical L-R coupling bridge",
        "Pfaffian/Weyl quotient",
        "support for a candidate route is not a matter-action statistics law",
    ]:
        check(f"new note carries determinant-order framing: {phrase[:54]}", phrase in note_flat)
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
    check("verification threshold present", "Expected close: `FAIL=0` with at least 150 checks." in note)

    section("D. source-packet boundary checks")
    for phrase in [
        "not a derivation of `r = 1/2`",
        "necessary-not-sufficient",
        "measure-neutral",
        "first-order",
        "second-order",
        "open staggered-Dirac corner realization",
    ]:
        check(f"index meta keeps dynamics gate: {phrase[:54]}", phrase in source_flat[INDEX_META])
    for phrase in [
        "**Type:** open_gate",
        "does not claim that the conditional antecedent has been established",
        "does not derive the Koide value",
        "requires the **gated** staggered-Dirac mass/Yukawa structure",
        "compute the CHIRAL",
    ]:
        check(f"supertrace note is conditional: {phrase[:54]}", phrase in source_flat[SUPERTRACE])
    for phrase in [
        "not a derivation of `r = 1/2`",
        "The remaining selector gate is the L-R coupling plus a readout rule.",
        "not a retained bridge from",
        "physical first-order/readout `r`-weighting rule",
        "No physical `M(b)",
        "bounded algebraic localization and route-pruning theorem",
    ]:
        check(f"first-order selector note keeps bridge open: {phrase[:54]}", phrase in source_flat[FIRST_ORDER])
    for phrase in [
        "essentially closed",
        "caught an over-claim",
        "Fermionic statistics",
        "Euclidean-signature / time-direction import",
        "Chirality",
        "not** a closure of the gate",
    ]:
        check(f"staggered reassessment keeps gate open: {phrase[:54]}", phrase in source_flat[REASSESSMENT])
    for phrase in [
        "det D = |det M|",
        "singular values",
        "The index route is closed on the realization.",
        "wrong *kind* of functional",
        "does **not** retire, split, or re-grade the `AC_",
    ]:
        check(f"Kahler-Dirac realization is count-twice: {phrase[:54]}", phrase in source_flat[KAHLER_DIRAC])
    for phrase in [
        "Determinant-order route",
        "derive an actual chiral/Pfaffian/holomorphic",
        "not merely a Dirac modulus square",
        "AC_phi_lambda is not retired.",
    ]:
        check(f"block13 names determinant-order route: {phrase[:54]}", phrase in source_flat[BLOCK13])
    for phrase in [
        "does not choose a Hamiltonian or transfer operator",
        "transition probabilities or weights",
        "context selection",
        "source/action and physical-observable identification",
        "Only records are readable",
    ]:
        check(f"minimal axioms withhold source/dynamics: {phrase[:54]}", phrase in source_flat[MINIMAL])

    section("E. weight and representation algebra")
    examples = [
        (sp.Rational(1), sp.Rational(2), sp.Rational(1), "trace/vector"),
        (sp.Rational(1), sp.Rational(1), sp.Rational(1, 2), "index/holomorphic"),
        (sp.Rational(1, 2), sp.Rational(1), sp.Rational(1), "uniform complex rescaling"),
    ]
    for ws, wd, expected, label in examples:
        check(f"{label} weights give expected r", r_from_weights(ws, wd) == expected, r_from_weights(ws, wd))
    for ws_num in range(1, 6):
        for wd_num in range(1, 6):
            ws = sp.Rational(ws_num)
            wd = sp.Rational(wd_num)
            x = sp.simplify(ws / (ws + wd))
            check(f"weight map agrees with fraction ws={ws_num} wd={wd_num}", r_from_weights(ws, wd) == sp.simplify((1 - x) / (2 * x)))
    w = sp.exp(2 * sp.pi * sp.I / 3)
    chi_reg = [3, 0, 0]
    chars = ([1, 1, 1], [1, w, w**2], [1, w**2, w**4])
    inner = lambda a, b: sp.simplify(sum(x * sp.conjugate(y) for x, y in zip(a, b)) / 3)
    multiplicities = tuple(inner(chi_reg, char) for char in chars)
    check("C3 regular representation has one copy of each character", multiplicities == (1, 1, 1), multiplicities)
    check("multiplicity doublet count differs from dimension doublet count", r_from_weights(1, 1) != r_from_weights(1, 2))

    section("F. native circulant and separate-factor selector algebra")
    c = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    i3 = sp.eye(3)
    gamma_chi = sp.Rational(2, 3) * (i3 + c + c**2) - i3
    a, p, q = sp.symbols("a p q")
    h = a * i3 + p * c + q * c**2
    anti = h * gamma_chi + gamma_chi * h
    sol = sp.solve([anti[i, j] for i in range(3) for j in range(3)], [a, p, q], dict=True)
    check("Gamma_chi commutes with C", sp.simplify(gamma_chi * c - c * gamma_chi) == sp.zeros(3))
    check("native circulant anticommuting selector is zero", sol == [{a: 0, p: 0, q: 0}] or all(s[a] == 0 and s[p] == 0 and s[q] == 0 for s in sol), sol)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    c_big = kron(c, sp.eye(2))
    g_big = kron(i3, sz)
    o_big = kron(i3, sx)
    check("separate-factor escape commutes with C tensor I", sp.simplify(o_big * c_big - c_big * o_big) == sp.zeros(6))
    check("separate-factor escape anticommutes with chirality", sp.simplify(o_big * g_big + g_big * o_big) == sp.zeros(6))
    check("separate-factor escape is nonzero", o_big != sp.zeros(6))

    section("G. Dirac determinant order and measure neutrality")
    x, y, z, xb, yb, zb = sp.symbols("x y z xb yb zb", nonzero=True)
    m = sp.diag(x, y, z)
    md = sp.diag(xb, yb, zb)
    zero = sp.zeros(3)
    d_block = sp.Matrix.vstack(sp.Matrix.hstack(zero, m), sp.Matrix.hstack(md, zero))
    det_d = sp.factor(d_block.det())
    check("off-diagonal Dirac block determinant is sign times detM detMdag", sp.factor(det_d + x * y * z * xb * yb * zb) == 0, det_d)
    d2 = sp.simplify(d_block * d_block)
    check("D^2 upper block is M Mdag", d2[:3, :3] == m * md)
    check("D^2 lower block is Mdag M", d2[3:, 3:] == md * m)
    j_cs = (c - c**2) / sp.sqrt(3)
    aa, bb, cc = sp.symbols("aa bb cc")
    circulant = aa * i3 + bb * c + cc * c**2
    check("native J_cs commutes with circulants", sp.simplify(j_cs * circulant - circulant * j_cs) == sp.zeros(3))
    theta = sp.symbols("theta", real=True)
    rot = sp.eye(3) + sp.sin(theta) * j_cs + (1 - sp.cos(theta)) * (j_cs**2)
    check("J_cs flow determinant is one", sp.simplify(rot.det() - 1) == 0)

    section("H. final no-go discipline")
    for phrase in [
        "This is not a universal no-go",
        "No observed lepton masses",
        "The residual is still AC(i)'s measure-side binary",
        "This note names exactly that needed theorem",
        "does not select `r = 1/2` or `r = 1`",
    ]:
        check(f"no-go discipline phrase present: {phrase[:54]}", phrase in note_flat)
    check("new note does not introduce wall labels", set(re.findall(r"\bW_[A-Za-z0-9_]+", note)) == set())
    check("new note says audit lane only", "**Audit boundary:** independent audit lane only." in note)
    check("new note says no registry edit", "does not edit any Tier-A registry" in note_flat)

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 and PASS >= 150 else 1


if __name__ == "__main__":
    raise SystemExit(main())
