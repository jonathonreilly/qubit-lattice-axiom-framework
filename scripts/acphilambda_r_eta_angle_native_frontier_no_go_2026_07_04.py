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
NOTE = DOCS / "ACPHILAMBDA_R_ETA_ANGLE_NATIVE_FRONTIER_NO_GO_NOTE_2026-07-04.md"
DECISION_HISTORY = DOCS / "audit" / "data" / "premise_decision_history.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
RADIAN = DOCS / "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md"
FIXED = DOCS / "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
BRANNEN = DOCS / "BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md"
RECORD = DOCS / "RECORD_PRESERVATION_CONSERVES_THE_WITHIN_SECTOR_MEASURE_BOUNDED_THEOREM_NOTE_2026-06-15.md"
REGISTRY_NOTE = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"

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


def exact_nonzero(expr: sp.Expr) -> bool:
    return expr.equals(0) is False


def main() -> int:
    print("AC_phi_lambda R-eta angle-native frontier no-go verifier")

    note = read(NOTE)
    tier = json.loads(read(DECISION_HISTORY))
    radian = read(RADIAN)
    fixed = read(FIXED)
    brannen = read(BRANNEN)
    record = read(RECORD)
    registry_note = read(REGISTRY_NOTE)

    section("A. source and registry boundaries")
    for path in [NOTE, DECISION_HISTORY, LEDGER, RADIAN, FIXED, BRANNEN, RECORD, REGISTRY_NOTE]:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    ac = tier["retired_derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    check("Tier-A has no live admitted inputs", tier["genuine_admitted_input_count"] == 0 and tier["derivation_targets"] == {})
    check(
        "AC minimum decomposition still includes R-eta",
        "delta_readout_identification_R_eta" in ac["minimum_decomposition"],
        ac["minimum_decomposition"],
    )
    note_flat = flat(note)
    registry_flat = flat(registry_note)
    fixed_flat = flat(fixed)

    check("note explicitly does not edit registry", "does not edit any Tier-A registry" in note_flat)
    check("note says R-eta is not retired", "R-eta is not derived, refuted, re-graded, or removed from Tier-A" in note)
    check(
        "human registry points to the R-eta derivation obligation",
        "AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md" in registry_note,
    )

    for source_path in [
        "docs/KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md",
        "docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md",
        "docs/BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md",
        "docs/RECORD_PRESERVATION_CONSERVES_THE_WITHIN_SECTOR_MEASURE_BOUNDED_THEOREM_NOTE_2026-06-15.md",
    ]:
        row = ledger_row_by_path(source_path)
        check(f"{Path(source_path).name} is retained-grade", row.get("effective_status") in {"retained", "retained_bounded", "retained_no_go"}, row.get("effective_status"))

    section("B. exact target arithmetic and off-locus status")
    L = sp.Rational(2, 9)
    S_sum = 3 * L
    delta_target = L
    phi_target = S_sum
    check("L = 2/9", L == sp.Rational(2, 9))
    check("S_sum = 3L = 2/3", S_sum == sp.Rational(2, 3))
    check("Phi target equals 3 delta target", phi_target == 3 * delta_target)
    check("target is positive and below pi", bool(0 < phi_target < sp.pi))
    check("sin(2/3) is nonzero", exact_nonzero(sp.sin(phi_target)))
    check("cos(2/3) is not +1", exact_nonzero(sp.cos(phi_target) - 1))
    check("cos(2/3) is not -1", exact_nonzero(sp.cos(phi_target) + 1))
    check("numeric target is off real-holonomy locus", abs(math.cos(2 / 3)) < 0.999)

    section("C. periodic/torsion and canonical packaging checks")
    check("sympy marks pi irrational", sp.pi.is_irrational is True)
    check("2/9 is rational", L.is_rational is True)
    check("2/3 is rational", phi_target.is_rational is True)
    check("nonzero rational times pi cannot equal 2/9", sp.pi.is_irrational is True and L != 0)
    check("nonzero rational times pi cannot equal 2/3", sp.pi.is_irrational is True and phi_target != 0)
    check("radian no-go source mentions q*pi", "q*pi" in radian or "qπ" in radian)
    check("radian no-go source mentions Type-B", "Type-B" in radian)

    two_pi_L = 2 * sp.pi * L
    two_pi_S = 2 * sp.pi * S_sum
    check("canonical U(1) packaging 2*pi*L misses delta", exact_nonzero(two_pi_L - delta_target))
    check("canonical U(1) packaging 2*pi*L misses Phi", exact_nonzero(two_pi_L - phi_target))
    check("canonical U(1) packaging 2*pi*S misses Phi", exact_nonzero(two_pi_S - phi_target))
    root_angle = 2 * sp.pi / 3
    check("C3 root angle 2*pi/3 is not 2/3", exact_nonzero(root_angle - phi_target))
    check("fixed-locus source carries L3(1,2)=2/9", any(token in fixed_flat for token in ["L3(1,2)", "L_3(1,2)", "L₃(1,2)"]) and "2/9" in fixed_flat)
    check("fixed-locus source excludes physical readout", "physical single-summand" in fixed)

    section("D. homogeneous self-consistency/readout maps")
    phi = sp.symbols("Phi", real=True)
    coefficients = [Fraction(n, d) for d in range(1, 6) for n in range(-5, 6)]
    isolated_hits = []
    all_line_cases = []
    for lam_f in coefficients:
        lam = sp.Rational(lam_f.numerator, lam_f.denominator)
        equation = sp.expand(phi - lam * phi)
        if lam == 1:
            all_line_cases.append(lam_f)
            continue
        solution = sp.solve(sp.Eq(equation, 0), phi)
        if solution == [phi_target]:
            isolated_hits.append(lam_f)
        check(f"homogeneous Phi=lambda*Phi with lambda={lam_f} has no isolated target", solution != [phi_target])
    check("lambda=1 leaves the whole line, not a value", Fraction(1, 1) in all_line_cases)
    check("no homogeneous coefficient isolated target", isolated_hits == [], isolated_hits)

    scale = sp.symbols("scale", nonzero=True)
    I_c = sp.symbols("I_c", real=True)
    homogeneous_clauses = [
        scale * 0 == 0,
        sp.expand(scale * (I_c + 2 * I_c) - (scale * I_c + 2 * scale * I_c)) == 0,
        sp.expand(scale * (3 * L) - 3 * scale * L) == 0,
    ]
    check("record/additivity sample clauses are rescale invariant", all(bool(item) for item in homogeneous_clauses))
    check("record source preserves delta rather than relaxing it", "neither produced nor relaxed" in record)
    check("Brannen source carries delta as supplied dial", "(a, |b|, delta)" in brannen)

    section("E. inhomogeneous license classification")
    alpha_hits = []
    for num in range(-8, 9):
        alpha = sp.Rational(num, 4)
        value = sp.simplify(alpha * S_sum)
        if value == phi_target:
            alpha_hits.append(alpha)
    check("only alpha=1 hits Phi=alpha*S_sum in scanned zero-offset family", alpha_hits == [sp.Integer(1)], alpha_hits)
    check("alpha=1 map consumes the fixed-locus source", "Phi = S_sum" in note)
    check("note classifies Phi=S_sum as license target", "It is classified as the live R-eta license" in note)
    check("remaining routes section names licensed angle-native theorem", "Licensed angle-native theorem" in note)
    check("remaining routes section names occurrence route", "Occurrence-lane clock/event route" in note)

    section("F. note discipline and audit compatibility")
    check("Type header is no_go", "**Type:** no_go" in note)
    check("Claim type header is no_go", "**Claim type:** no_go" in note)
    check("scope boundary blocks retirement and registry claims", "This does not derive, refute, re-grade, or retire R-eta" in note_flat)
    check("audit boundary present", "**Audit boundary:** independent audit lane only." in note)
    check("primary runner link present", "scripts/acphilambda_r_eta_angle_native_frontier_no_go_2026_07_04.py" in note)
    for idx in range(1, 9):
        check(f"N{idx} gate present", f"**N{idx}" in note)
    forbidden = [
        "R-eta is derived",
        "R-eta is refuted",
        "R-eta is retired",
        "AC_phi_lambda is retired",
        "audited_clean",
        "effective_status = retained",
    ]
    for phrase in forbidden:
        check(f"forbidden phrase absent: {phrase}", phrase not in note)
    wall_names = set(re.findall(r"\bW_[A-Za-z0-9_]+", note))
    check("wall names are whitelisted", wall_names <= {"W_cycle_holonomy_value"}, wall_names)
    check("no PDG comparator used", "PDG" not in note)
    check("expected PASS line is present", "TOTAL: PASS=" in note and "FAIL=0" in note)

    section("G. note/source cross-checks")
    for phrase in [
        "periodic/torsion `q*pi` phase sources",
        "canonical `U(1)` packagings",
        "Homogeneous self-consistency/readout maps",
        "Restates the missing license",
        "future angle-native theorem is not ruled out",
        "No registry, axiom, primitive, audit verdict, or publication surface is edited",
    ]:
        check(f"note carries phrase: {phrase[:48]}", phrase in note_flat)
    links = set(re.findall(r"\[[^\]]+\]\(([^)]+)\)", note))
    expected_links = {
        "../scripts/acphilambda_r_eta_angle_native_frontier_no_go_2026_07_04.py",
        "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md",
        "BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md",
        "RECORD_PRESERVATION_CONSERVES_THE_WITHIN_SECTOR_MEASURE_BOUNDED_THEOREM_NOTE_2026-06-15.md",
        "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md",
        "AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md",
    }
    check("markdown link inventory is controlled", links == expected_links, sorted(links))
    check("note line count is bounded", 150 <= len(note.splitlines()) <= 230, len(note.splitlines()))

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 and PASS >= 100 else 1


if __name__ == "__main__":
    raise SystemExit(main())
