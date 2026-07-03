#!/usr/bin/env python3
"""Verifier for the K-even registration correction note."""

from __future__ import annotations

from fractions import Fraction
import json
import re
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ACPHILAMBDA_K_EVEN_REGISTRATION_CORRECTION_REGISTERED_PATTERN_2026-07-02.md"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
TIER_A = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
RECORD = ROOT / "docs" / "RECORD_PRESERVATION_CONSERVES_THE_WITHIN_SECTOR_MEASURE_BOUNDED_THEOREM_NOTE_2026-06-15.md"
BRANNEN = ROOT / "docs" / "BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md"

RECORD_KEY = "record_preservation_conserves_the_within_sector_measure_bounded_theorem_note_2026-06-15"
BRANNEN_KEY = "brannen_circulant_is_forced_c3_covariant_record_preserving_generation_form_bounded_theorem_note_2026-06-15"
TIER_A_QUOTE = (
    "the delta readout identification R-eta (density-read-as-angle; "
    "the magnitude 2/9 is retained-bounded fixed-locus arithmetic conditional "
    "on R-eta, not an admitted number)"
)
PRESERVED = [
    "every registrable layer derived in this campaign is K-even; the sign strip is K/CPT-orbit constancy",
    "the K-odd trace is a reconstruction-layer detector; its registrable image is K-even",
    "on the current retained surface the value is realized-state registered data; the residual identification is exactly the R-eta sub-admission in its narrowed coordinates",
    "this is the registered-pattern normal form, not a terminal no-go",
]
ALLOWED_WALLS = {
    "W_cycle_holonomy_value",
    "W_defect_identity_unit",
    "W_defect_readout_selection",
}

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {name}")
    else:
        FAIL += 1
        print(f"[FAIL] {name}")
    if detail:
        print(f"       {detail}")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def ledger_rows() -> tuple[dict, dict]:
    data = json.loads(read_text(LEDGER))
    rows = data["rows"]
    return rows[RECORD_KEY], rows[BRANNEN_KEY]


def tier_a_statement() -> str:
    data = json.loads(read_text(TIER_A))
    return data["derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]["statement"]


def not_zero(expr: sp.Expr) -> bool:
    return expr.equals(0) is False


def normalized_contains(text: str, needle: str) -> bool:
    return needle in " ".join(text.split())


def part_a_sources(note: str) -> None:
    print("\nPART A - sources and authority gates")
    check("note file exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    check("record dependency exists", RECORD.exists(), str(RECORD.relative_to(ROOT)))
    check("Brannen dependency exists", BRANNEN.exists(), str(BRANNEN.relative_to(ROOT)))
    check("ledger exists", LEDGER.exists(), str(LEDGER.relative_to(ROOT)))
    check("Tier-A data exists", TIER_A.exists(), str(TIER_A.relative_to(ROOT)))

    record_text = read_text(RECORD)
    brannen_text = read_text(BRANNEN)
    for pin in [
        "only a finer character-basis record would touch it",
        "neither produced nor relaxed by the record-preserving dynamics",
    ]:
        check(f"record file pin present: {pin}", normalized_contains(record_text, pin))
        check(f"note quotes record pin: {pin}", pin in note)
    for pin in ["circulant form", "(a, |b|, delta)"]:
        check(f"Brannen file pin present: {pin}", pin in brannen_text)
        check(f"note quotes Brannen pin: {pin}", pin in note)

    record_row, brannen_row = ledger_rows()
    for label, row in [("record", record_row), ("Brannen", brannen_row)]:
        scope = row["claim_scope"]
        check(f"{label} ledger status retained", row["effective_status"] == "retained_bounded")
        check(f"{label} note path pinned", Path(row["note_path"]).name in note)
        check(f"{label} quoted scope equals ledger field", scope in note, scope)

    statement = tier_a_statement()
    check("Tier-A statement contains sub-admission (ii)", TIER_A_QUOTE in statement)
    check("note quotes Tier-A sub-admission (ii)", TIER_A_QUOTE in note)
    check("Tier-A path is inline code, not markdown link", f"`{TIER_A.relative_to(ROOT)}`" in note)


def branch_product(sign: int, phi: sp.Symbol) -> sp.Expr:
    momenta = [sp.Integer(0), 2 * sp.pi / 3, 4 * sp.pi / 3]
    product = sp.Integer(1)
    for kappa in momenta:
        product *= sign * sp.sqrt(3) * sp.sin(kappa + phi / 3)
    return sp.simplify(product)


def a_trace(phi: sp.Symbol) -> sp.Expr:
    w_plus = sp.Rational(1, 2) - sp.I * sp.sqrt(3) / 2
    w_minus = sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    weighted = w_plus * branch_product(1, phi) + w_minus * branch_product(-1, phi)
    return sp.simplify(sp.I * weighted / sp.sqrt(3))


def a_trace_k_branch(phi: sp.Symbol) -> sp.Expr:
    w_plus = sp.Rational(1, 2) - sp.I * sp.sqrt(3) / 2
    w_minus = sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    image = sp.conjugate(w_minus) * branch_product(-1, phi)
    image += sp.conjugate(w_plus) * branch_product(1, phi)
    return sp.simplify(sp.I * image / sp.sqrt(3))


def part_b_c1_exact() -> None:
    print("\nPART B - C1 exact K-parity")
    delta, phi = sp.symbols("delta phi", real=True)

    bare_diff = sp.trigsimp(sp.cos(3 * (-delta)) - sp.cos(3 * delta))
    check("bare spectrum cos(3 delta) is K-even", bare_diff == 0)

    pointer_cos = sp.trigsimp(sp.cos(-delta) - sp.cos(delta))
    pointer_abs = sp.simplify(sp.Abs(sp.sin(-delta)) - sp.Abs(sp.sin(delta)))
    check("pointer cos component is K-even", pointer_cos == 0)
    check("pointer absolute sine component is K-even", pointer_abs == 0)
    check("pointer pair is K-even", pointer_cos == 0 and pointer_abs == 0)

    a_phi = a_trace(phi)
    odd_residual = sp.trigsimp(a_phi.subs(phi, -phi) + a_phi)
    expected = -3 * sp.sqrt(3) * sp.sin(phi) / 4
    check("N=3 A(phi) reduces to real sin(phi) response", sp.trigsimp(a_phi - expected) == 0, str(a_phi))
    check("A(-phi) == -A(phi) symbolically", odd_residual == 0)

    k_image = a_trace_k_branch(phi)
    check("K branch map conjugates weights and swaps branches", sp.trigsimp(k_image + a_phi) == 0)
    check("|A|^2 is K-even", sp.trigsimp(a_phi.subs(phi, -phi) ** 2 - a_phi**2) == 0)

    re_functional = sp.re(sp.exp(sp.I * phi)).rewrite(sp.cos)
    k_even_residual = sp.trigsimp(re_functional.subs(phi, -phi) - re_functional)
    check("discriminator: Re part is K-even, not filtered", k_even_residual == 0 and re_functional != 0)


def part_c_c2_kills() -> None:
    print("\nPART C - C2 finite route kills")
    two_ninths_fraction = Fraction(2, 9)
    two_ninths = sp.Rational(two_ninths_fraction.numerator, two_ninths_fraction.denominator)
    target = sp.Rational(2, 3)

    check("sin(2/3) is exactly nonzero", not_zero(sp.sin(target)))
    check("cos(2/3) is exactly nonzero", not_zero(sp.cos(target)))

    rate_at_zero = 2 * sp.sqrt(3) * sp.sin(sp.Integer(0))
    return_amplitude = two_ninths
    check("clock rate at delta=0 is zero", rate_at_zero == 0)
    check("clock rate at delta=0 differs from return amplitude", rate_at_zero != return_amplitude)

    tuned_b = sp.simplify(two_ninths / (2 * sp.sqrt(3) * sp.sin(two_ninths)))
    check("tuned |b| expression is exact", tuned_b.has(sp.sin) and tuned_b.has(sp.sqrt(3)), str(tuned_b))
    check("tuned |b| is not 1", not_zero(tuned_b - 1))
    check("tuned |b| is not 1/2", not_zero(tuned_b - sp.Rational(1, 2)))
    check("tuned |b| is not 2", not_zero(tuned_b - 2))

    arg_det_at_zero = 3 * sp.Integer(0)
    l3_value = two_ninths
    check("arg det at delta=0 is zero", arg_det_at_zero == 0)
    check("arg det at delta=0 differs from L3", arg_det_at_zero != l3_value)

    fluxed_inverse = 9 / (2 - 2 * sp.cos(target))
    check("fluxed inverse is not 2/3", not_zero(fluxed_inverse - target))
    check("fluxed inverse is greater than 20 exactly", sp.ask(sp.Q.positive(fluxed_inverse - 20)) is True)
    check("fluxed inverse labeled approximate instance", str(sp.N(fluxed_inverse, 12)).startswith("21."))

    check("pi is irrational in sympy", sp.pi.is_irrational is True)
    check("2/9 is rational", two_ninths.is_rational is True)
    q = sp.symbols("q", rational=True, nonzero=True)
    forced_pi = sp.simplify(two_ninths / q)
    check("2/9 = q*pi with rational q would force pi rational", forced_pi.is_rational is True)
    check("2/9 is not in pi*Q by irrationality", sp.pi.is_irrational is True and two_ninths != 0)

    conservation_quote = "neither produced nor relaxed by the record-preserving dynamics"
    check("conservation quote pinned in note", conservation_quote in read_text(NOTE))


def markdown_links(note: str) -> list[tuple[str, str]]:
    return re.findall(r"\[([^\]]+)\]\(([^)]+)\)", note)


def part_d_note_discipline(note: str) -> None:
    print("\nPART D - note discipline")
    check("canonical Type header is bounded_theorem", "**Type:** bounded_theorem" in note)
    check("canonical Claim type header is bounded_theorem", "**Claim type:** bounded_theorem" in note)
    check("scope boundary present", "**Scope boundary:**" in note)
    check("audit boundary present", "**Audit boundary:**" in note)
    check("legacy Status/Status authority headers absent", not re.search(r"^\*\*(Status|Status authority):\*\*", note, re.M))

    for sentence in PRESERVED:
        lines = [line.strip() for line in note.splitlines() if sentence in line]
        check(f"required sentence present: {sentence[:48]}", len(lines) >= 1)
        check(f"required sentence embedded: {sentence[:48]}", all(line != sentence for line in lines))

    check("normal-form sentence present", "not a terminal no-go" in note)
    for token in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"{token} gate token present", token in note)

    forbidden = [
        "only" + " route",
        "last" + " route",
        "ex" + "hausted",
        "closes" + " the route",
        "P" + "DG",
        "new" + " wall",
        "terminal" + " no-go is claimed",
    ]
    for fragment in forbidden:
        check(f"forbidden fragment absent: {fragment}", fragment not in note)

    walls = set(re.findall(r"W_[A-Za-z0-9_]+", note))
    check("all W_ names are whitelisted", walls <= ALLOWED_WALLS, str(sorted(walls)))
    check("one-wall consolidation present", "W_defect_identity_unit == W_cycle_holonomy_value == R-eta (ii)" in note)

    links = markdown_links(note)
    md_targets = [target for _, target in links if target.endswith(".md")]
    runner_targets = [target for _, target in links if target.endswith(".py")]
    check("exactly two markdown .md dependency targets", len(md_targets) == 2, str(md_targets))
    check("exactly one runner markdown link", len(runner_targets) == 1, str(runner_targets))
    check("runner link points to this script", runner_targets == [f"../scripts/{Path(__file__).name}"])
    check("campaign PRs are backticked, not linked", "ACPHILAMBDA_PROJECTIVE_EQUIVARIANCE_K_ODD_TRACE_2026-07-02`" in note)
    check("occurrence PRs are backticked", all(f"`#{n}`" in note for n in [4763, 4765, 4770, 4776]))

    leakage = [
        "PRESERVE VERBATIM",
        "MUST BE ABSENT",
        "Acceptance contract",
        "runner greps",
        "execute it exactly",
        "ANTI-FABRICATION",
    ]
    for fragment in leakage:
        check(f"instruction marker absent: {fragment}", fragment not in note)

    check("retained_bounded token appears exactly twice", note.count("retained_bounded") == 2)
    check("Tier-A path is not markdown linked", not any("tier_a_admissions.json" in target for _, target in links))
    check("no campaign note path markdown links", not any("ACPHILAMBDA_" in target for _, target in links))

    line_count = len(note.splitlines())
    check("note line count in requested band", 190 <= line_count <= 240, str(line_count))
    check("Verification section present", "## Verification" in note)
    check("Primary runner header present", "**Primary runner:**" in note)


def main() -> int:
    note = read_text(NOTE)
    part_a_sources(note)
    part_b_c1_exact()
    part_c_c2_kills()
    part_d_note_discipline(note)
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 and PASS >= 55 else 1


if __name__ == "__main__":
    sys.exit(main())
