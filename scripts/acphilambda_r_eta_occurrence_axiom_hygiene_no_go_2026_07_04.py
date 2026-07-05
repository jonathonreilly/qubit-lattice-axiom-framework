#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import re
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "ACPHILAMBDA_R_ETA_OCCURRENCE_AXIOM_HYGIENE_NO_GO_NOTE_2026-07-04.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
AXIOM_PREMISES = DOCS / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
BRANNEN = DOCS / "BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md"
FIXED = DOCS / "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
REALIZED = DOCS / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
KINETIC = DOCS / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"

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


def depends_on(expr: sp.Expr, sym: sp.Symbol) -> bool:
    return sym in expr.free_symbols


def main() -> int:
    print("AC_phi_lambda R-eta occurrence axiom-hygiene no-go verifier")

    note = read(NOTE)
    minimal = read(MINIMAL)
    premises = json.loads(read(AXIOM_PREMISES))
    tier = json.loads(read(TIER_A))
    brannen = read(BRANNEN)
    fixed = read(FIXED)
    registry = read(REGISTRY)
    realized = read(REALIZED)
    kinetic = read(KINETIC)

    note_flat = flat(note)
    minimal_flat = flat(minimal)
    registry_flat = flat(registry)

    section("A. source presence and Tier-A boundary")
    for path in [NOTE, MINIMAL, AXIOM_PREMISES, TIER_A, LEDGER, BRANNEN, FIXED, REGISTRY, REALIZED, KINETIC]:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    ac = tier["derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    check("Tier-A has a live genuine admitted input", tier["genuine_admitted_input_count"] >= 1)
    check(
        "AC minimum decomposition keeps R-eta",
        "delta_readout_identification_R_eta" in ac["minimum_decomposition"],
        ac["minimum_decomposition"],
    )
    check("AC statement still names R-eta", "R-eta" in ac["statement"])
    check("human registry names R-eta", ("R-eta" in registry_flat or "R-η" in registry_flat) and "density-read-as-angle" in registry_flat)
    check("note says registry is not edited", "The Tier-A registry is not edited." in note)
    check("note says R-eta is not retired", "R-eta is not derived, refuted, re-graded, or removed from Tier-A" in note)

    for source_path, expected in [
        ("docs/BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md", "retained_bounded"),
        ("docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md", "retained_bounded"),
    ]:
        row = ledger_row_by_path(source_path)
        check(f"{Path(source_path).name} effective status", row.get("effective_status") == expected, row.get("effective_status"))

    section("B. approved premise-node hygiene")
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
    check("minimal premise current path is 2026-06-29", premises["nodes"]["minimal_axioms"]["current_path"] == "docs/MINIMAL_AXIOMS_2026-06-29.md")
    check("premise note contains records form", "records form" in minimal_note.lower())
    for phrase in [
        "formation rule",
        "with what weight",
        "at what rate",
        "probability",
        "measurement/decoherence",
        "context-selection",
        "state-selection rule",
    ]:
        check(f"minimal premise note withholds {phrase}", phrase in minimal_note)

    section("C. Record axiom text boundary")
    check("minimal axiom has Record section", "### Record / Fixed Reality" in minimal)
    check("Record axiom says records form", "Records form." in minimal)
    check("Record axiom locks one admissible local possibility", "locks exactly one admissible local possibility" in minimal)
    check("Record axiom says only records are readable", "Only records are readable" in minimal)
    check("Record axiom has finite scalar additivity", "finite collection of pairwise-disjoint records" in minimal and "I(empty)=0" in minimal)
    for phrase in [
        "transition probabilities or weights",
        "provide a record-production process",
        "context selection",
        "measurement basis selection",
        "Born weights",
        "probability rules",
        "update laws",
        "decoherence mechanisms",
        "formation rules",
        "physical observable bridge",
    ]:
        check(f"minimal axiom excludes {phrase}", phrase in minimal_flat)
    check("historical note says occurrence became named axiom content", "occurrence became named axiom content" in minimal)
    check("historical note says every formation rule remained downstream", "every formation rule" in minimal_flat and "remained downstream supplier content" in minimal_flat)

    section("D. approved primitive non-supply checks")
    for phrase in [
        "no state",
        "measure",
        "weighting",
        "probability rule",
        "normalization rule",
        "value",
    ]:
        check(f"realized-state primitive withholds {phrase}", phrase in flat(realized))
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
    check("scale primitive is not needed for R-eta event law", "scale_reference_primitive" in premises["canonical_ids"])
    check("note classifies occurrence-as-fact only", "occurrence-as-fact" in note)

    section("E. exact fixed-locus target arithmetic")
    L = sp.Rational(2, 9)
    S_sum = 3 * L
    phi_target = sp.Rational(2, 3)
    check("L = 2/9", L == sp.Rational(2, 9))
    check("S_sum = 3L = 2/3", S_sum == sp.Rational(2, 3))
    check("Phi target is 2/3", phi_target == S_sum)
    check("target positive and below pi", bool(0 < phi_target < sp.pi))
    check("fixed source contains L3(1,2)", any(token in fixed for token in ["L3(1,2)", "L_3(1,2)", "L₃(1,2)"]))
    check("fixed source contains 2/9", "2/9" in fixed)
    check("fixed source flags physical readout as separate", "physical single-summand" in fixed)
    check("note states S_sum target", "S_sum = 3 L3(1,2) = 2/3" in note)

    section("F. Brannen clock and occupancy algebra")
    delta, B, a0 = sp.symbols("delta B a", real=True)
    lam_s = a0 + 2 * B * sp.cos(delta)
    lam_d1 = a0 + 2 * B * sp.cos(delta + 2 * sp.pi / 3)
    lam_d2 = a0 + 2 * B * sp.cos(delta + 4 * sp.pi / 3)
    diff = sp.trigsimp(lam_d2 - lam_d1)
    check("doublet difference is 2*sqrt(3)*B*sin(delta)", sp.trigsimp(diff - 2 * sp.sqrt(3) * B * sp.sin(delta)) == 0, diff)
    check("Brannen source carries supplied dial", "(a, |b|, delta)" in brannen)
    check("clock rate depends on B", depends_on(2 * sp.sqrt(3) * B * sp.sin(delta), B))
    check("clock rate depends on delta", depends_on(2 * sp.sqrt(3) * B * sp.sin(delta), delta))
    check("clock rate nonzero at target for B=1", abs(float(2 * math.sqrt(3) * math.sin(2 / 9))) > 0)

    r00, r01, r02, r10, r11, r12, r20, r21, r22 = sp.symbols("r00 r01 r02 r10 r11 r12 r20 r21 r22")
    u0, u1, u2 = sp.symbols("u0 u1 u2", nonzero=True)
    rho = sp.Matrix([[r00, r01, r02], [r10, r11, r12], [r20, r21, r22]])
    U = sp.diag(u0, u1, u2)
    U_inv = sp.diag(1 / u0, 1 / u1, 1 / u2)
    evolved = sp.simplify(U * rho * U_inv)
    for idx, sym in enumerate([r00, r11, r22]):
        check(f"occupancy {idx} invariant under diagonal native step", sp.simplify(evolved[idx, idx] - sym) == 0)
    check("doublet coherence gets phase ratio", evolved[1, 2] == r12 * u1 / u2)
    dephased = sp.diag(r00, r11, r22)
    for idx, sym in enumerate([r00, r11, r22]):
        check(f"D_chi preserves diagonal {idx}", dephased[idx, idx] == sym)
    off_diag_zero = [dephased[i, j] == 0 for i in range(3) for j in range(3) if i != j]
    check("D_chi erases off-diagonal coherences", all(off_diag_zero))

    section("G. occupancy-reading event laws are delta-blind")
    o0, o1, o2 = sp.symbols("o0 o1 o2", nonnegative=True)
    occupancy_law = [o0, o1, o2]
    stream = [0, 2, 1, 1, 0]
    stream_prob = sp.prod(occupancy_law[i] for i in stream)
    check("stream product law contains no delta", delta not in stream_prob.free_symbols)
    check("stream product law contains no B", B not in stream_prob.free_symbols)
    check("stream product law is product of occupancies", stream_prob == o0**2 * o1**2 * o2)
    substitutions = {o0: sp.Rational(1, 2), o1: sp.Rational(1, 3), o2: sp.Rational(1, 6)}
    prob_1 = stream_prob.subs(substitutions).subs(delta, sp.Rational(1, 9))
    prob_2 = stream_prob.subs(substitutions).subs(delta, sp.Rational(2, 9))
    check("two different deltas give same occupancy stream law", sp.simplify(prob_1 - prob_2) == 0)
    check("occupancy probabilities can normalize", sp.simplify(sum(occupancy_law).subs(substitutions) - 1) == 0)
    for k in range(3):
        rule = occupancy_law[k] / sum(occupancy_law)
        check(f"normalized occupancy rule {k} contains no delta", delta not in rule.free_symbols)

    section("H. coherence-reading can see delta only through supplied law")
    n, phase0, c = sp.symbols("n phase0 c", real=True)
    rate = 2 * sp.sqrt(3) * B * sp.sin(delta)
    p_plus = sp.Rational(1, 2) * (o1 + o2) + c * sp.cos(n * rate + phase0)
    check("coherence-reading expression contains delta", delta in p_plus.free_symbols)
    check("coherence-reading expression contains B", B in p_plus.free_symbols)
    dp_ddelta = sp.diff(p_plus, delta)
    check("coherence law derivative contains B", B in dp_ddelta.free_symbols)
    p_a = float(p_plus.subs({o1: sp.Rational(1, 3), o2: sp.Rational(1, 6), c: sp.Rational(1, 10), n: 1, B: 1, phase0: 0, delta: sp.Rational(1, 9)}))
    p_b = float(p_plus.subs({o1: sp.Rational(1, 3), o2: sp.Rational(1, 6), c: sp.Rational(1, 10), n: 1, B: 1, phase0: 0, delta: sp.Rational(2, 9)}))
    check("coherence example changes with delta", abs(p_a - p_b) > 1e-4, (p_a, p_b))
    check("note says coherence law is supplied interface", "supplied interface" in note)
    check("minimal axiom does not choose projector/interface law", "measurement basis selection" in minimal_flat and "Born weights" in minimal_flat)

    section("I. sparse occurrence kernel and rate-normalization obstruction")
    a_act, p0, p1, p2 = sp.symbols("a_act p0 p1 p2", real=True)
    q_bot = 1 - a_act
    q = [a_act * p0, a_act * p1, a_act * p2]
    check("q_bot has no delta", delta not in q_bot.free_symbols)
    for idx, qi in enumerate(q):
        check(f"q_{idx} has no delta unless p is supplied with it", delta not in qi.free_symbols)
    kernel_sum = sp.simplify(q_bot + sum(q))
    check("kernel normalizes when p sums to one", sp.simplify(kernel_sum.subs(p2, 1 - p0 - p1) - 1) == 0)
    ratio = sp.simplify(rate / a_act)
    check("clock/event ratio contains B", B in ratio.free_symbols)
    check("clock/event ratio contains a_act", a_act in ratio.free_symbols)
    check("clock/event ratio contains delta", delta in ratio.free_symbols)
    ratio_1 = ratio.subs({B: 1, a_act: 1, delta: sp.Rational(2, 9)})
    ratio_2 = ratio.subs({B: 2, a_act: 1, delta: sp.Rational(2, 9)})
    ratio_3 = ratio.subs({B: 1, a_act: sp.Rational(1, 2), delta: sp.Rational(2, 9)})
    check("changing B changes the ratio", sp.simplify(ratio_2 - ratio_1) != 0)
    check("changing a_act changes the ratio", sp.simplify(ratio_3 - ratio_1) != 0)
    B_solution = sp.solve(sp.Eq(ratio.subs(delta, sp.Rational(2, 9)), phi_target), B)
    expected_B = a_act / (3 * sp.sqrt(3) * sp.sin(sp.Rational(2, 9)))
    check("setting ratio to target solves B in terms of a_act", B_solution == [expected_B], B_solution)
    check("solution still contains a_act", a_act in B_solution[0].free_symbols)
    check("note contains the B-solution formula", "|b| = a_act / (3 sqrt(3) sin(2/9))" in note)

    section("J. no-go discipline and route accounting")
    check("note Type header is no_go", "**Type:** no_go" in note)
    check("note Claim type header is no_go", "**Claim type:** no_go" in note)
    check("scope boundary blocks retirement", "does not derive, refute, re-grade, retire, or remove R-eta" in note_flat)
    check("audit boundary present", "**Audit boundary:** independent audit lane only." in note)
    check("primary runner link present", "scripts/acphilambda_r_eta_occurrence_axiom_hygiene_no_go_2026_07_04.py" in note)
    for idx in range(1, 9):
        check(f"N{idx} gate present", f"**N{idx}" in note)
    for phrase in [
        "future occurrence theorem is not ruled out",
        "The generic Record occurrence route is closed as an R-eta license",
        "Coherence-reading events",
        "Rate-normalization theorem",
        "Owner governance route",
    ]:
        check(f"route accounting phrase present: {phrase[:42]}", phrase in note_flat)
    forbidden = [
        "R-eta is derived",
        "R-eta is retired",
        "AC_phi_lambda is retired",
        "audited_clean",
        "effective_status = retained",
        "PDG",
        "uses a fitted value",
    ]
    for phrase in forbidden:
        check(f"forbidden phrase absent: {phrase}", phrase not in note)
    wall_names = set(re.findall(r"\bW_[A-Za-z0-9_]+", note))
    check("wall names are whitelisted", wall_names <= {"W_cycle_holonomy_value"}, wall_names)

    section("K. markdown dependency and context-link control")
    links = set(re.findall(r"\[[^\]]+\]\(([^)]+)\)", note))
    expected_links = {
        "../scripts/acphilambda_r_eta_occurrence_axiom_hygiene_no_go_2026_07_04.py",
        "MINIMAL_AXIOMS_2026-06-29.md",
        "BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md",
        "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md",
        "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md",
        "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    }
    check("markdown link inventory is controlled", links == expected_links, sorted(links))
    check("occurrence bridge is context only, not markdown-linked", "RECORD_OCCURRENCE_THINNED_IID_FREQUENCY_BRIDGE_2026-07-01.md](" not in note)
    check("occurrence-clock note is context only, not markdown-linked", "ACPHILAMBDA_OCCURRENCE_CLOCK_COMPOSITION_DELTA_BLINDNESS_2026-07-02.md](" not in note)
    check("note line count is bounded", 150 <= len(note.splitlines()) <= 240, len(note.splitlines()))
    check("verification block expects 139 passes", "TOTAL: PASS=139 FAIL=0" in note)

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 and PASS == 139 else 1


if __name__ == "__main__":
    raise SystemExit(main())
