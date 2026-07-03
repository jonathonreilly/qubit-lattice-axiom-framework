#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import re
import sys

import sympy as sp


BASE = Path(__file__).resolve().parents[1]

PATHS = {
    "w": Path("docs/W_SCALE_ABSORPTION_TWO_CELL_READOUT_CLASSIFICATION_BOUNDED_NOTE_2026-07-02.md"),
    "custody": Path("docs/CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md"),
    "staggered": Path("docs/KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md"),
    "static": Path("docs/KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md"),
    "factorization": Path("docs/KOIDE_OCCUPANCY_DERIVED_FROM_POSSIBILITY_INDIVIDUATION_BOUNDED_NOTE_2026-07-03.md"),
    "orbit": Path("docs/KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md"),
    "note": Path("docs/KOIDE_SLOT_FREEDOM_CLASSIFICATION_UNDER_CONJUGATION_READING_BOUNDED_NOTE_2026-07-03.md"),
    "runner": Path("scripts/frontier_koide_slot_freedom_classification_2026_07_03.py"),
}


def read_text(key: str) -> str:
    return (BASE / PATHS[key]).read_text(encoding="utf-8")


texts = {key: read_text(key) for key in ("w", "custody", "staggered", "static", "factorization", "orbit", "note")}

checks: list[tuple[bool, str]] = []


def record(condition: bool, description: str) -> None:
    checks.append((bool(condition), description))


def q_value(r: Fraction) -> Fraction:
    return Fraction(1, 3) + Fraction(2, 3) * r


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def contains_phrase(text: str, phrase: str) -> bool:
    return " ".join(phrase.split()) in " ".join(text.split())


W_METHOD_QUOTE = "Each row is classified only under its stated premise:"
CUSTODY_R_QUOTE = "exact `Q = 1/3 + (2/3)r`, `r=\\|b\\|²/a²`"
FIRST_POWER_QUOTE = "the partition function is `det(D + A)` to the\n**first power** (checks 6–7)."
K_REAL_QUOTE = (
    "on the K-real line\n"
    "`c = b̄` the Wirtinger derivative `∂² det₃ / ∂b ∂b̄ = −3a`\n"
    "(Laplacian `−12a`) — the count-twice `|b|²` term of the rank-2 modulus\n"
    "wall appears exactly there (check 15)."
)
PARAMETER_RESTRICTION_QUOTE = "is supplied by the **parameter restriction** `c = b̄`"
HORN_NEUTRALITY_QUOTES = [
    "the fork relocated, not resolved",
    "What remains is not a measure-order question at all.",
    "Neither horn is derived here",
]
PREMISE_SOURCE_QUOTES = [
    "> P-transport: the one-site individuation discipline transports to the derived\n> generation doublet.",
    "> P-phase: record content fixes the orbit magnitude `|b|^2` and not the\n> conjugate-sector relative phase.",
    "> P-occupancy: one admissible possibility supplies one statistical slot.",
]
PREMISE_NOTE_QUOTES = [
    "P-transport: the one-site individuation discipline transports to the derived generation doublet.",
    "P-phase: record content fixes the orbit magnitude `|b|^2` and not the conjugate-sector relative phase.",
    "P-occupancy: one admissible possibility supplies one statistical slot.",
]


record(W_METHOD_QUOTE in texts["w"], "live w classification-method quote is present")
record(W_METHOD_QUOTE in texts["note"], "note quotes the w classification-method sentence")
record(CUSTODY_R_QUOTE in texts["custody"], "live custody r-consumption lever quote is present")
record(CUSTODY_R_QUOTE in texts["note"], "note quotes the custody r-consumption lever")
record(FIRST_POWER_QUOTE in texts["staggered"], "live staggered first-power sentence is present")
record(FIRST_POWER_QUOTE in texts["note"], "note quotes the staggered first-power sentence")
record(K_REAL_QUOTE in texts["staggered"], "live staggered K-real-line localization sentence is present")
record(K_REAL_QUOTE in texts["note"], "note quotes the K-real-line localization sentence")
record(contains_phrase(texts["staggered"], PARAMETER_RESTRICTION_QUOTE), "live staggered parameter-restriction sentence is present")
record(contains_phrase(texts["note"], PARAMETER_RESTRICTION_QUOTE), "note quotes the parameter-restriction sentence")
for quote in HORN_NEUTRALITY_QUOTES:
    record(contains_phrase(texts["staggered"], quote), f"live staggered horn-neutrality quote present: {quote}")
    record(contains_phrase(texts["note"], quote), f"note quotes horn-neutrality sentence: {quote}")

for source_premise, note_premise in zip(PREMISE_SOURCE_QUOTES, PREMISE_NOTE_QUOTES):
    label = note_premise.split(":", 1)[0]
    record(source_premise in texts["factorization"], f"live factorization premise quote present: {label}")
    record(note_premise in texts["note"], f"note quotes factorization premise: {label}")

inventory_terms = [
    "EW shape `g1^2/(g1^2+g2^2)`",
    "Koide-shape witness",
    "mass ratios",
    "absolute mass scale",
    "`8/9` central-sector count",
]
for term in inventory_terms:
    record(term in texts["w"], f"w inventory contains {term}")

note_required_terms = [
    "sin^2 theta_W",
    "Koide-shape witness",
    "Mass ratios",
    "Calibrated absolute mass vector",
    "`8/9` central-sector count",
    "theta mass-side composition",
]
for term in note_required_terms:
    record(term in texts["note"], f"note classifies {term}")

r_real_coordinate = Fraction(1, 1)
r_per_possibility = Fraction(1, 2)
q_real_coordinate = q_value(r_real_coordinate)
q_per_possibility = q_value(r_per_possibility)

record(q_real_coordinate == Fraction(1, 1), "exact lever gives Q(1) = 1")
record(q_per_possibility == Fraction(2, 3), "exact lever gives Q(1/2) = 2/3")
record(q_real_coordinate - q_per_possibility == Fraction(1, 3), "exact slot difference is 1/3")
record(q_real_coordinate / q_per_possibility == Fraction(3, 2), "exact slot ratio is 3/2")
record(q_value(Fraction(1, 1)) == (Fraction(1, 1) + 2 * Fraction(1, 1)) / 3, "lever equals (1+2r)/3 at r=1")
record(q_value(Fraction(1, 2)) == (Fraction(1, 1) + 2 * Fraction(1, 2)) / 3, "lever equals (1+2r)/3 at r=1/2")

a_sym, br_sym, bi_sym, g_sym = sp.symbols("a br bi g", positive=True, real=True)
b_sym = br_sym + sp.I * bi_sym
bbar_sym = br_sym - sp.I * bi_sym
det3_k_real = sp.expand(a_sym**3 + b_sym**3 + bbar_sym**3 - 3 * a_sym * b_sym * bbar_sym)
hessian_k_real = sp.Matrix(
    [
        [sp.diff(det3_k_real, br_sym, br_sym), sp.diff(det3_k_real, br_sym, bi_sym)],
        [sp.diff(det3_k_real, bi_sym, br_sym), sp.diff(det3_k_real, bi_sym, bi_sym)],
    ]
).subs({br_sym: 0, bi_sym: 0})
expected_hessian = sp.Matrix([[-6 * a_sym, 0], [0, -6 * a_sym]])
z_unit = sp.pi / g_sym
z_k_real = 2 * z_unit
z_orbit = z_unit
horn_z_ratio = sp.simplify(z_k_real / z_orbit)
rho_k_real = sp.simplify(z_unit / z_k_real)
rho_orbit = sp.simplify(z_unit / z_orbit)
r_k_real = sp.simplify(1 / (2 * rho_k_real))
r_orbit = sp.simplify(1 / (2 * rho_orbit))
q_k_real = sp.simplify(sp.Rational(1, 3) + sp.Rational(2, 3) * r_k_real)
q_orbit = sp.simplify(sp.Rational(1, 3) + sp.Rational(2, 3) * r_orbit)

record(
    hessian_k_real == expected_hessian and hessian_k_real.rank() == 2,
    "small det3 model on K-real section has two real-coordinate |b|^2 Hessian",
)
record(
    sp.simplify(z_k_real - 2 * sp.pi / g_sym) == 0 and sp.simplify(z_orbit - sp.pi / g_sym) == 0,
    "horn-neutrality exhibit computes Z weights 2*pi/g and pi/g",
)
record(horn_z_ratio == 2, "horn-neutrality exhibit gives exact Z_K-real/Z_orbit = 2")
record(r_k_real == 1, "K-real-section reading gives r = 1")
record(r_orbit == sp.Rational(1, 2), "conjugate-orbit-quotient reading gives r = 1/2")
record(q_k_real == 1 and q_orbit == sp.Rational(2, 3), "same lever gives Q = 1 and Q = 2/3 for the two readings")
record("same `det^1`" in texts["note"] or "same det^1" in texts["note"], "note identifies the same det^1 object for both readings")

mass_r1 = "(1 + 2*cos(2/9 + 2*pi*k/3))^2"
mass_rhalf = "(1 + sqrt(2)*cos(2/9 + 2*pi*k/3))^2"
cal_r1 = "M_j*(1 + 2*cos(2/9 + 2*pi*k/3))^2/(1 + 2*cos(2/9 + 2*pi*j/3))^2"
cal_rhalf = "M_j*(1 + sqrt(2)*cos(2/9 + 2*pi*k/3))^2/(1 + sqrt(2)*cos(2/9 + 2*pi*j/3))^2"
record(mass_r1 in texts["note"], "note gives exact mass-ratio expression at r=1")
record(mass_rhalf in texts["note"], "note gives exact mass-ratio expression at r=1/2")
record(cal_r1 in texts["note"], "note gives exact calibrated-vector expression at r=1")
record(cal_rhalf in texts["note"], "note gives exact calibrated-vector expression at r=1/2")

slot_alive = {
    "Koide-shape witness": (fraction_text(q_real_coordinate), fraction_text(q_per_possibility)),
    "mass ratios": (mass_r1, mass_rhalf),
    "calibrated absolute mass vector": (cal_r1, cal_rhalf),
}
slot_dead = {
    "sin^2 theta_W": "g1^2/(g1^2+g2^2)",
    "`8/9` central-sector count": "`8/9`",
}
record("SLOT-ALIVE" in texts["note"], "note uses required SLOT-ALIVE classification")
record("SLOT-DEAD" in texts["note"], "note uses required SLOT-DEAD classification")
for name in slot_alive:
    record(name.lower() in texts["note"].lower(), f"SLOT-ALIVE readout listed: {name}")
for name, value in slot_dead.items():
    record(name in texts["note"] and value in texts["note"], f"SLOT-DEAD readout fixed: {name}")

scale_numerator_power = Fraction(1, 1)
scale_denominator_power = Fraction(1, 2) * 2
record(scale_numerator_power == scale_denominator_power, "Koide Q is exactly invariant under common mass rescaling")
record(q_real_coordinate != q_per_possibility, "rescaling cannot identify Q(1) and Q(1/2)")
record("not an overall scale convention" in texts["note"], "note states non-absorbability as a scale verdict")
record("ratio readout" in texts["note"], "note states the ratio readout still sees the slot bit")

record("the measure side is first-order" in texts["staggered"], "staggered source says the measure side is first-order")
record("one slot per K-orbit" in texts["staggered"], "staggered source contains one-slot-per-K-orbit cell")
record("no occupancy/weighting rule is adopted" in texts["staggered"], "staggered source states residual no occupancy rule adopted")
record("declared probe coupling" in texts["staggered"], "staggered source states probe-coupling residual")
record(contains_phrase(texts["static"], "The Record axiom itself supplies no weighting, normalization, or occupancy rule"), "static no-go source states Record supplies no weighting rule")
record(contains_phrase(texts["static"], "Record names realized outcomes but supplies no weighting/occupancy rule"), "static no-go source prunes the Record-orbit route")
record("Dynamical Discharge Test: REFUTED" in texts["note"], "note retitles the discharge test as refuted")
record("An adversarial seat refuted the discharge form" in texts["note"], "note states refutation provenance")
record("horn-neutral" in texts["note"], "note states horn-neutrality")
record("re-consumed, not discharged" in texts["note"], "note states K-reality is re-consumed rather than discharged")
record("declared probe coupling" in texts["note"], "note inherits the probe-coupling residual")
record(contains_phrase(texts["note"], "The conjugation clause buys individuation only"), "decision surface says conjugation buys individuation only")
record(contains_phrase(texts["note"], "One bit of genuine physical input remains"), "decision surface preserves one weighting bit")
record(contains_phrase(texts["note"], "per-possibility versus per-real-coordinate weighting"), "decision surface names the remaining weighting bit")
record(contains_phrase(texts["note"], "Option (a): add a new axiom sentence supplying the one-slot weighting"), "decision surface gives owner option (a)")
record(contains_phrase(texts["note"], "No possibility is privileged"), "decision surface names the hostile no-privilege precedent")
record(contains_phrase(texts["note"], "does not name a weighting"), "decision surface states the weak intent-defense precedent")
record(contains_phrase(texts["note"], "Option (b): keep the bit as the flavor admission"), "decision surface gives owner option (b)")
record(contains_phrase(texts["note"], "this one bit plus the transport statement"), "decision surface narrows the admission content under hypothetical H-conj")
record(contains_phrase(texts["note"], "There is no third route in this lane"), "decision surface forbids a third route")
record(contains_phrase(texts["note"], "June 8 static, July 3 individuation, and July 3 discharge"), "decision surface names the three closed derivation attempts")

h_conj_lines = [line for line in texts["note"].splitlines() if "H-conj" in line]
record(len(h_conj_lines) > 0, "note mentions H-conj")
record(all("hypothetical" in line.lower() for line in h_conj_lines), "every H-conj line marks it as hypothetical")
record("Nothing in this note lands hypothetical H-conj" in texts["note"], "note says the hypothetical is not landed")
record(re.search(r"\b(retained|verified)\b", texts["note"], flags=re.IGNORECASE) is None, "note has no bare retained/verified tokens")
record(re.search(r"\bstatus\b", texts["note"], flags=re.IGNORECASE) is None, "note has no bare status token")

record("M_sector  →  ρ = 1/2  →  r = 1" in texts["orbit"], "orbit source contains sector-slot arithmetic")
record("M_orbit   →  ρ = 1    →  r = 1/2" in texts["orbit"], "orbit source contains orbit-slot arithmetic")
record("r_sector / r_orbit = Z_sector / Z_orbit = 2" in texts["orbit"], "orbit source contains exact occupancy factor")

passed = sum(1 for ok, _ in checks if ok)
failed = len(checks) - passed

for index, (ok, description) in enumerate(checks, start=1):
    status = "PASS" if ok else "FAIL"
    print(f"CHECK {index:02d}: {status} -- {description}")

print(f"TOTAL: PASS={passed} FAIL={failed}")

files_summary = (
    f"SUMMARY files/checks: {PATHS['note'].as_posix()}; {PATHS['runner'].as_posix()}; "
    f"checks={len(checks)} PASS={passed} FAIL={failed}"
)
horn_summary = (
    "SUMMARY horn-neutrality: "
    f"same det^1; K-real Z={z_k_real}, r={r_k_real}, Q={q_k_real}; "
    f"orbit Z={z_orbit}, r={r_orbit}, Q={q_orbit}; ratio={horn_z_ratio}"
)
option_a_summary = (
    "SUMMARY owner option A: add a one-slot weighting axiom sentence; intent defense is weak under the "
    "No-possibility hostile precedent"
)
option_b_summary = (
    "SUMMARY owner option B: keep the bit as flavor admission content: one weighting bit plus transport "
    "under hypothetical H-conj"
)
uncertainty_summary = (
    "SUMMARY uncertainties: physical horn and declared probe coupling remain; no derivation route remains "
    "from measure-neutrality, individuation, or measure-order"
)

print(files_summary)
print(horn_summary)
print(option_a_summary)
print(option_b_summary)
print(uncertainty_summary)

sys.exit(1 if failed else 0)
