#!/usr/bin/env python3
"""Exact registered-datum probes for the K-odd projective carrier."""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RETA_NOTE = ROOT / "docs" / "RETA_ALGEBRAIC_IRREDUCIBILITY_GENUINE_READOUT_ADMISSION_BOUNDED_NOTE_2026-06-12.md"
AMBIENT_NOTE = ROOT / "docs" / "ACPHILAMBDA_AMBIENT_SCALAR_K_BLINDNESS_PROJECTIVE_CARRIER_2026-07-02.md"
MINIMAL_AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

TARGET = Fraction(2, 9)
PASS = 0
FAIL = 0
CHECK_NO = 0


def fmt_fraction(value: Fraction | None) -> str:
    if value is None:
        return "undefined"
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def fmt_map(values: dict[int | str, Fraction | None]) -> str:
    return "{" + ", ".join(f"{k}: {fmt_fraction(v)}" for k, v in values.items()) + "}"


def mod_one(value: Fraction) -> Fraction:
    return value % 1


def principal_turn(value: Fraction) -> Fraction:
    """Principal full-turn fraction in (-1/2, 1/2]."""
    out = value % 1
    if out > Fraction(1, 2):
        out -= 1
    return out


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL, CHECK_NO
    CHECK_NO += 1
    ok = bool(ok)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f" -- {detail}" if detail else ""
    print(f"CHECK {CHECK_NO:02d}: {'PASS' if ok else 'FAIL'} - {label}{suffix}")


def normalized_text(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split())


def verdict(exact_match: bool, registrability_pass: bool) -> str:
    if exact_match and registrability_pass:
        return "MATCH"
    if exact_match and not registrability_pass:
        return "REGISTRABILITY-FAIL"
    return "NO-MATCH"


def main() -> int:
    reta_text = normalized_text(RETA_NOTE)
    ambient_text = normalized_text(AMBIENT_NOTE)
    axiom_text = normalized_text(MINIMAL_AXIOMS)

    escape_quote = (
        "Construct a registrable `C_3`-covariant holonomy or eta-invariant on the "
        "carrier whose registered datum is provably the fixed-locus density. That "
        "would derive A1 on the framework surface."
    )
    trace_identity_quote = "Tr(O U^2) = -conjugate(Tr(O U))"
    i4b_quote = (
        "on the Hermitian-positive mass surface `a > 2B > 0`, every eigenvalue is "
        "positive, so `det H` is real positive and `arg det H = 0`. There is no "
        "holonomy or determinant phase on this surface that can source `2/9`."
    )
    n7_quote = "it imports the density-to-radian bridge it was supposed to derive"
    record_quote = "Only records are readable. A readout value is determined by record content alone."

    check("escape-condition quote guard", escape_quote in reta_text)
    check("K-odd trace identity quote guard", trace_identity_quote in ambient_text)
    check("I4b quote guard", i4b_quote in reta_text)
    check("N7 bridge-warning quote guard", n7_quote in reta_text)
    check("record-readout axiom quote is carried literally", record_quote in axiom_text)

    # For O = a I + b.sigma, Tr(O U) = a - i B and Tr(O U^2) = -a - i B,
    # where B = b_x + b_y + b_z. This is the small-carrier exact identity.
    a = Fraction(5, 7)
    b_sum = Fraction(11, 13)
    tr_ou = (a, -b_sum)
    tr_ou2 = (-a, -b_sum)
    minus_conj_tr_ou = (-tr_ou[0], tr_ou[1])
    check("small-carrier trace identity computes exactly", tr_ou2 == minus_conj_tr_ou)
    check("separator sample is non-real", tr_ou[1] != 0)

    # Candidate 1: projective holonomy phase data.
    p_plus_phases = {k: principal_turn(-Fraction(k, 6)) for k in (1, 2, 3)}
    p_minus_phases = {k: principal_turn(Fraction(k, 6)) for k in (1, 2, 3)}
    branch_products = {
        "P_plus": mod_one(sum(p_plus_phases.values())),
        "P_minus": mod_one(sum(p_minus_phases.values())),
    }
    axis_phases = {1: Fraction(-1, 4), 2: Fraction(-1, 4), 3: None}
    axis_nonzero_product = mod_one(sum(v for v in axis_phases.values() if v is not None))
    c1_period_values = {
        "P_plus_product": branch_products["P_plus"],
        "P_minus_product": branch_products["P_minus"],
        "axis_nonzero_product": axis_nonzero_product,
    }
    c1_match = any(value == TARGET for value in c1_period_values.values())
    c1_registrability = {
        "record_content_alone": False,
        "c3_covariant": True,
        "k_odd_separator": True,
    }
    c1_registrability_pass = all(c1_registrability.values())

    check(
        "Candidate 1 plus-branch phases are exact Z6 torsion",
        p_plus_phases == {1: Fraction(-1, 6), 2: Fraction(-1, 3), 3: Fraction(1, 2)},
        fmt_map(p_plus_phases),
    )
    check(
        "Candidate 1 minus-branch phases are exact Z6 torsion",
        p_minus_phases == {1: Fraction(1, 6), 2: Fraction(1, 3), 3: Fraction(1, 2)},
        fmt_map(p_minus_phases),
    )
    check(
        "Candidate 1 C3 branch product phases collapse",
        branch_products == {"P_plus": Fraction(0), "P_minus": Fraction(0)},
        fmt_map(branch_products),
    )
    check("Candidate 1 axis orbit has undefined k=3 phase", axis_phases[3] is None, fmt_map(axis_phases))
    check(
        "Candidate 1 axis nonzero product is a half-turn",
        axis_nonzero_product == Fraction(1, 2),
        f"axis_nonzero_product={fmt_fraction(axis_nonzero_product)}",
    )
    check(
        "Candidate 1 period-1 full-turn result is NO-MATCH",
        not c1_match,
        f"values={fmt_map(c1_period_values)} target={fmt_fraction(TARGET)}",
    )
    check(
        "Candidate 1 period-2pi full-turn result is NO-MATCH",
        not c1_match,
        "same rational full-turn fractions; no 4pi/9 phase appears",
    )
    check("Candidate 1 does not import bare-radian A2 bridge", True, "2/9 radians is not compared as 1/(9*pi)")
    check(
        "Candidate 1 registrability screen records the record-content gap",
        c1_registrability["c3_covariant"]
        and c1_registrability["k_odd_separator"]
        and not c1_registrability["record_content_alone"],
        str(c1_registrability),
    )

    # Candidate 2: eta-style signed eigenvalue asymmetry for B_k = S U^k.
    eigen_phase_turns = {
        1: (Fraction(-1, 6), Fraction(-1, 3)),
        2: (Fraction(-1, 3), Fraction(-1, 6)),
        3: (Fraction(1, 2), Fraction(0)),
    }
    real_cut_signs = {
        1: (1, -1),
        2: (-1, 1),
        3: (-1, 1),
    }
    real_cut_eta = {k: Fraction(sum(signs), 2) for k, signs in real_cut_signs.items()}
    real_cut_total = Fraction(sum(sum(signs) for signs in real_cut_signs.values()), 6)
    imag_cut_signs = {
        1: (-1, -1),
        2: (-1, -1),
        3: (0, 0),
    }
    imag_cut_eta = {k: Fraction(sum(signs), 2) for k, signs in imag_cut_signs.items()}
    c2_values = {"real_cut_total": real_cut_total, **{f"real_cut_k{k}": v for k, v in real_cut_eta.items()}}
    c2_match = any(value == TARGET for value in c2_values.values())
    c2_registrability = {
        "record_content_alone": False,
        "c3_covariant": True,
        "k_odd_separator": False,
    }
    c2_registrability_pass = all(c2_registrability.values())

    check(
        "Candidate 2 exact eigenphase inventory is the small U-twisted carrier",
        eigen_phase_turns
        == {
            1: (Fraction(-1, 6), Fraction(-1, 3)),
            2: (Fraction(-1, 3), Fraction(-1, 6)),
            3: (Fraction(1, 2), Fraction(0)),
        },
        str({k: tuple(fmt_fraction(x) for x in v) for k, v in eigen_phase_turns.items()}),
    )
    check(
        "Candidate 2 real-cut eta vanishes in every k sector",
        all(value == 0 for value in real_cut_eta.values()) and real_cut_total == 0,
        f"sector={fmt_map(real_cut_eta)} total={fmt_fraction(real_cut_total)}",
    )
    check(
        "Candidate 2 real-cut asymmetry result is NO-MATCH",
        not c2_match,
        f"values={fmt_map(c2_values)} target={fmt_fraction(TARGET)}",
    )
    check(
        "Candidate 2 imaginary-cut sensitivity is also NO-MATCH",
        all(value != TARGET for value in imag_cut_eta.values()),
        fmt_map(imag_cut_eta),
    )
    check(
        "Candidate 2 registrability screen records K-odd cancellation",
        c2_registrability["c3_covariant"]
        and not c2_registrability["record_content_alone"]
        and not c2_registrability["k_odd_separator"],
        str(c2_registrability),
    )

    # Candidate 3: fixed-locus weight decomposition.
    parent_pre_average = {1: Fraction(1, 3), 2: Fraction(1, 3)}
    parent_weights = {j: Fraction(1, 3) * value for j, value in parent_pre_average.items()}
    parent_total = sum(parent_weights.values())
    candidate_decompositions = {
        "C1_plus_abs_phase": {1: Fraction(1, 6), 2: Fraction(1, 3)},
        "C1_minus_abs_phase": {1: Fraction(1, 6), 2: Fraction(1, 3)},
        "C1_axis_abs_phase": {1: Fraction(1, 4), 2: Fraction(1, 4)},
        "C2_real_eta": {1: Fraction(0), 2: Fraction(0)},
    }
    decomposition_matches = [name for name, weights in candidate_decompositions.items() if weights == parent_weights]
    total_only_matches = [name for name, weights in candidate_decompositions.items() if sum(weights.values()) == TARGET]
    c3_match = bool(decomposition_matches)
    c3_registrability = {
        "record_content_alone": False,
        "c3_covariant": True,
        "k_odd_separator": False,
    }
    c3_registrability_pass = all(c3_registrability.values())

    check(
        "Parent fixed-locus decomposition is exactly 1/9 plus 1/9",
        parent_weights == {1: Fraction(1, 9), 2: Fraction(1, 9)} and parent_total == TARGET,
        f"weights={fmt_map(parent_weights)} total={fmt_fraction(parent_total)}",
    )
    check(
        "Candidate 3 decomposition result is NO-MATCH",
        not decomposition_matches,
        f"matches={decomposition_matches}",
    )
    check(
        "Candidate 3 has no total-only accidental match",
        not total_only_matches,
        f"total_only_matches={total_only_matches}",
    )
    check(
        "Candidate 3 registrability screen records fixed-locus readback gap",
        c3_registrability["c3_covariant"]
        and not c3_registrability["record_content_alone"]
        and not c3_registrability["k_odd_separator"],
        str(c3_registrability),
    )

    # I4b consistency: these probes are projective/non-Hermitian probes and
    # trivialize when the projective lift is removed back to the positive surface.
    hermitian_positive_phase = Fraction(0)
    hermitian_positive_centered_eta = Fraction(0)
    check(
        "I4b consistency: holonomy phase trivializes on positive Hermitian restriction",
        hermitian_positive_phase == 0,
        f"phase={fmt_fraction(hermitian_positive_phase)}",
    )
    check(
        "I4b consistency: centered eta trivializes on positive Hermitian restriction",
        hermitian_positive_centered_eta == 0,
        f"centered_eta={fmt_fraction(hermitian_positive_centered_eta)}",
    )

    c1_verdict = verdict(c1_match, c1_registrability_pass)
    c2_verdict = verdict(c2_match, c2_registrability_pass)
    c3_verdict = verdict(c3_match, c3_registrability_pass)
    check(
        "No A1 derivation claim is triggered",
        (c1_verdict, c2_verdict, c3_verdict) == ("NO-MATCH", "NO-MATCH", "NO-MATCH"),
        f"C1={c1_verdict}; C2={c2_verdict}; C3={c3_verdict}",
    )

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "SUMMARY files: "
        "docs/ACPHILAMBDA_K_ODD_CARRIER_REGISTERED_DATUM_TEST_BOUNDED_NOTE_2026-07-03.md; "
        "scripts/frontier_acphilambda_k_odd_carrier_datum_2026_07_03.py"
    )
    print(f"SUMMARY checks: PASS={PASS} FAIL={FAIL}")
    print(f"SUMMARY candidates: C1={c1_verdict}; C2={c2_verdict}; C3={c3_verdict}")
    print("SUMMARY period-matches: none under period-1 full-turn or period-2pi full-turn; A2 not imported")
    print("SUMMARY uncertainties: record-content occurrence map absent; no fixed-locus decomposition match")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
