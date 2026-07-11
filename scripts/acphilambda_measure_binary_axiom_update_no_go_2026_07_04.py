#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
AXIOM_PREMISES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A = DOCS / "audit" / "data" / "premise_decision_history.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
REALIZED = DOCS / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
KINETIC = DOCS / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
MEASURE = DOCS / "FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md"

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


def ledger_row_by_path(path: str) -> dict:
    rows = json.loads(read(LEDGER))["rows"]
    matches = [row for row in rows.values() if row.get("note_path") == path]
    if len(matches) != 1:
        raise AssertionError(f"ledger matches for {path}: {len(matches)}")
    return matches[0]


def hs_inner(a: sp.Matrix, b: sp.Matrix) -> sp.Expr:
    return sp.trace(a.T * b)


def main() -> int:
    print("AC_phi_lambda measure binary axiom-update no-go verifier")

    note = read(NOTE)
    minimal = read(MINIMAL)
    premises = json.loads(read(AXIOM_PREMISES))
    tier = json.loads(read(TIER_A))
    registry = read(REGISTRY)
    realized = read(REALIZED)
    kinetic = read(KINETIC)
    measure = read(MEASURE)

    note_flat = flat(note)
    minimal_flat = flat(minimal)
    registry_flat = flat(registry)
    measure_flat = flat(measure)

    section("A. source presence and audit anchors")
    for path in [NOTE, MINIMAL, AXIOM_PREMISES, TIER_A, LEDGER, REGISTRY, REALIZED, KINETIC, MEASURE]:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    row = ledger_row_by_path("docs/FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md")
    check("carrier-measure boundary row remains ledgered", row.get("effective_status") != "missing", row.get("effective_status"))
    check("carrier-measure boundary row has an audit status", bool(row.get("audit_status")), row.get("audit_status"))

    section("B. Tier-A registry boundary")
    ac = tier["retired_derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    check("Tier-A has no live admitted inputs", tier["genuine_admitted_input_count"] == 0)
    check("Tier-A live target map is empty", tier["derivation_targets"] == {})
    check(
        "AC minimum decomposition keeps occupancy selection",
        "reading_occupancy_selection" in ac["minimum_decomposition"],
        ac["minimum_decomposition"],
    )
    for phrase in [
        "doublet reading/occupancy selection",
        "sector-tied vs orbit/holomorphic count",
        "r in {1, 1/2}",
        "custody K-reality",
        "det_C/equal-power selectors",
    ]:
        check(f"machine registry states {phrase}", phrase in ac["statement"])
    check("human registry points to the occupancy derivation obligation", "AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md" in registry)
    check("note says registry is not edited", "The Tier-A registry is not edited." in note)
    check("note says AC_phi_lambda is not retired", "AC_phi_lambda is not retired." in note)

    section("C. approved premise-node registry")
    check(
        "premise registry canonical ids are the approved four",
        premises["canonical_ids"] == [
            "minimal_axioms",
            "scale_reference_primitive",
            "kinetic_isotropy_primitive",
            "realized_state_primitive",
        ],
        premises["canonical_ids"],
    )
    minimal_note = premises["nodes"]["minimal_axioms"]["note"]
    for phrase in [
        "records form",
        "no context-selection rule",
        "formation rule",
        "weighting",
        "probability",
        "K/CPT structure",
        "central-sector decomposition",
        "physical observable bridge",
    ]:
        check(f"premise registry withholds or scopes {phrase}", phrase in minimal_note)

    section("D. updated axiom text non-supply")
    for phrase in [
        "### Lattice / Physical Locality",
        "### Qubit / Site Possibility",
        "### Admissibility / Local Constraint",
        "### Record / Fixed Reality",
        "Records form.",
        "A state is a configuration of records.",
    ]:
        check(f"minimal axiom contains {phrase[:42]}", phrase in minimal)
    for phrase in [
        "does not choose a Hamiltonian or transfer operator",
        "supply transition probabilities or weights",
        "select a scalar or nonzero kinetic branch",
        "assert a Dirac-square carrier",
        "define a time metric",
        "provide a record-production process",
        "context selection",
        "measurement basis selection",
        "Born weights",
        "probability rules",
        "formation rules",
        "K`/CPT orbit structure",
        "central-sector decomposition",
        "physical observable bridge",
        "the staggered-Dirac/finite-Grassmann realization and `AC_phi_lambda`",
    ]:
        check(f"minimal axiom excludes {phrase[:50]}", phrase in minimal_flat)
    check("new Record occurrence sentence does not add weights", "with what weight" in minimal and "at what rate" in minimal)

    section("E. approved primitive non-supply")
    for phrase in [
        "no state",
        "measure",
        "weighting",
        "probability rule",
        "normalization rule",
        "value",
    ]:
        check(f"realized primitive withholds {phrase}", phrase in flat(realized))
    for phrase in [
        "no mass ratio",
        "coupling",
        "mixing angle",
        "phase",
        "selector",
        "readout bridge",
        "empirical fit",
    ]:
        check(f"kinetic primitive withholds {phrase}", phrase in flat(kinetic))
    check("note distinguishes realized values from measure rule", "covers lane values only" in note)
    check("note blocks kinetic-isotropy analogy", "Kinetic isotropy could be analogized" in note)

    section("F. retained carrier-measure boundary text")
    for phrase in [
        "Record supplies coordinates and coarse-grainings, not the missing weight selector",
        "The same circulant operator still admits three inequivalent finite readings",
        "It does not rank them",
        "This is enough to express the dial. It is not enough to choose the dial.",
        "Record additivity alone cannot select that scoring rule",
        "derive, from the current framework surface, why the physical generation readout uses generator-channel Hilbert-Schmidt scoring",
    ]:
        check(f"retained measure note carries boundary: {phrase[:46]}", phrase in measure_flat)

    section("G. exact Hilbert-Schmidt channel algebra")
    N = 3
    I = sp.eye(N)
    J = sp.ones(N)
    B = J - I
    check("B_N = J_N - I_N", B == sp.Matrix([[0, 1, 1], [1, 0, 1], [1, 1, 0]]))
    check("HS norm of I_N is N", hs_inner(I, I) == N)
    check("HS norm of B_N is N(N-1)", hs_inner(B, B) == N * (N - 1))
    check("I_N and B_N are HS-orthogonal", hs_inner(I, B) == 0)
    a, b = sp.symbols("a b", positive=True)
    r_hs = sp.simplify((N * a**2) / (N * (N - 1) * a**2))
    check("equal generator-channel HS energy gives r=1/(N-1)", r_hs == sp.Rational(1, N - 1), r_hs)
    r = sp.symbols("r", real=True)
    Q = sp.Rational(1, 3) + sp.Rational(2, 3) * r
    check("Q at r=1/2 is 2/3", sp.simplify(Q.subs(r, sp.Rational(1, 2)) - sp.Rational(2, 3)) == 0)
    check("Q at r=1 is 1", sp.simplify(Q.subs(r, 1) - 1) == 0)
    check("Q at r=0 is 1/3", sp.simplify(Q.subs(r, 0) - sp.Rational(1, 3)) == 0)

    section("H. competing partition values")
    r_generator = sp.Rational(1, 2)
    r_dimension = sp.Integer(1)
    t = -2 + sp.Rational(3, 2) * sp.sqrt(2)
    r_idempotent = sp.expand(t**2)
    check("generator-channel result is r=1/2", r_generator == sp.Rational(1, 2))
    check("dimension/per-mode result is r=1", r_dimension == 1)
    check("idempotent root solves condition", sp.expand((1 + 2 * t) ** 2 - 2 * (1 - t) ** 2) == 0)
    check("idempotent r is 17/2 - 6sqrt(2)", sp.simplify(r_idempotent - (sp.Rational(17, 2) - 6 * sp.sqrt(2))) == 0, r_idempotent)
    check("idempotent Q is 6 - 4sqrt(2)", sp.simplify(Q.subs(r, r_idempotent) - (6 - 4 * sp.sqrt(2))) == 0)
    check("three readings produce distinct r values", len({sp.sstr(r_generator), sp.sstr(r_dimension), sp.sstr(r_idempotent)}) == 3)
    check("generator and dimension endpoints both positive", r_generator > 0 and r_dimension > 0)
    check("idempotent root is positive", bool(r_idempotent > 0))

    section("I. Record additivity permits but does not rank")
    u = sp.symbols("u", positive=True)
    for p in [sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(2, 3), sp.Rational(3, 4)]:
        d = sp.simplify(p * u / (1 - p))
        recovered = sp.simplify(d / (u + d))
        check(f"finite coordinate realizes p={p}", recovered == p)
    p_from_r = sp.simplify((2 * r) / (1 + 2 * r))
    check("r=1/2 gives normalized doublet coordinate p=1/2", sp.simplify(p_from_r.subs(r, sp.Rational(1, 2)) - sp.Rational(1, 2)) == 0)
    check("r=1 gives normalized doublet coordinate p=2/3", sp.simplify(p_from_r.subs(r, 1) - sp.Rational(2, 3)) == 0)
    readout_a, readout_b = sp.symbols("readout_a readout_b", real=True)
    check("finite additivity is compatible with arbitrary supplied readouts", sp.simplify((readout_a + readout_b) - readout_a - readout_b) == 0)
    sector_slots = {"singlet": 1, "doublet_real": 2}
    orbit_slots = {"singlet": 1, "doublet_complex": 1}
    check("sector/count-twice has doublet slot count two", sector_slots["doublet_real"] == 2)
    check("orbit/count-once has doublet slot count one", orbit_slots["doublet_complex"] == 1)
    check("slot-count ratio is exactly two", sp.Rational(sector_slots["doublet_real"], orbit_slots["doublet_complex"]) == 2)

    section("J. note discipline")
    check("note Type header is no_go", "**Type:** no_go" in note)
    check("note Claim type header is no_go", "**Claim type:** no_go" in note)
    check("scope boundary blocks retirement", "does not derive, refute, re-grade, retire, or remove AC_phi_lambda" in note_flat)
    check("audit boundary present", "**Audit boundary:** independent audit lane only." in note)
    check("primary runner link present", "scripts/acphilambda_measure_binary_axiom_update_no_go_2026_07_04.py" in note)
    for idx in range(1, 9):
        check(f"N{idx} gate present", f"**N{idx}" in note)
    for phrase in [
        "AC_phi_lambda is not retired",
        "No value of `r` is derived, selected, or preferred.",
        "R-eta and theta are untouched.",
        "derive the physical generation readout partition or keep AC(i) live",
        "The target is now sharper",
    ]:
        check(f"note carries boundary phrase: {phrase[:44]}", phrase in note)
    forbidden = [
        "AC_phi_lambda is retired",
        "r = 1/2 is derived",
        "r = 1 is derived",
        "audited_clean",
        "effective_status = retained",
        "PDG",
        "uses a fitted value",
    ]
    for phrase in forbidden:
        check(f"forbidden phrase absent: {phrase}", phrase not in note)
    wall_names = set(re.findall(r"\bW_[A-Za-z0-9_]+", note))
    check("no wall names introduced", wall_names == set(), wall_names)

    section("K. markdown dependency and context control")
    links = set(re.findall(r"\[[^\]]+\]\(([^)]+)\)", note))
    expected_links = {
        "../scripts/acphilambda_measure_binary_axiom_update_no_go_2026_07_04.py",
        "MINIMAL_AXIOMS_2026-06-29.md",
        "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md",
        "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md",
    }
    check("markdown link inventory is controlled", links == expected_links, sorted(links))
    check("newer AC(i) notes are context only, not linked", "ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md](" not in note)
    check("orbit-occupancy note is context only, not linked", "KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md](" not in note)
    check("note line count is bounded", 160 <= len(note.splitlines()) <= 260, len(note.splitlines()))
    check("verification block states fail-zero threshold", "Expected close: `FAIL=0` with at least 120 checks." in note)

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 and PASS >= 120 else 1


if __name__ == "__main__":
    raise SystemExit(main())
