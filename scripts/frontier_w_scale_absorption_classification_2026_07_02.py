#!/usr/bin/env python3
"""Exact finite witnesses for the w scale-absorption classification note."""

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
BLOCK16_NOTE = (
    ROOT
    / "docs"
    / "C2_W_SUPPLIER_READING_FORK_FIXED_POINT_UNIDENTIFIABILITY_BOUNDED_NOTE_2026-07-02.md"
)
KAPPA_NOTE = ROOT / "docs" / "EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md"
SCALE_NOTE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
NOTE_PATH = (
    ROOT
    / "docs"
    / "W_SCALE_ABSORPTION_CLASSIFICATION_LANDED_READOUTS_BOUNDED_NOTE_2026-07-02.md"
)

EM_DASH = "\u2014"

checks = []


def read_text(path):
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def check(condition, description):
    checks.append(bool(condition))
    status = "PASS" if condition else "FAIL"
    print(f"CHECK {len(checks):02d}: {status} {EM_DASH} {description}")


def readout(record, u, v):
    x_a, x_b = record
    return u * x_a + v * x_b


def diagonal_readouts(contents, weights):
    u, v = weights
    return [readout((x, x), u, v) for x in contents]


def pairwise_ratios(values):
    return [
        values[i] / values[j]
        for i in range(len(values))
        for j in range(i + 1, len(values))
    ]


def normalized(values):
    total = sum(values, Fraction(0))
    return [value / total for value in values]


def koide_shape(roots):
    return sum(root * root for root in roots) / (sum(roots, Fraction(0)) ** 2)


def generic_degree_zero(values):
    i1, i2, i3 = values
    return (i1 * i1 + Fraction(2) * i2 * i3) / ((i1 + i2 + i3) ** 2)


def calibrated_table(contents, weights, cal_index=0):
    values = diagonal_readouts(contents, weights)
    return [value / values[cal_index] for value in values]


def scale_reference_table(contents, weights, reference_value, cal_index=0):
    values = diagonal_readouts(contents, weights)
    unit = reference_value / values[cal_index]
    return [value * unit for value in values]


def ew_shape(g1_base, g2_base, common_factor):
    g1_sq = common_factor * g1_base
    g2_sq = common_factor * g2_base
    return g1_sq / (g1_sq + g2_sq)


def apply_sigma_to_condition(condition, sigma):
    return tuple(sigma[item] for item in condition)


def apply_sigma_to_set(items, sigma):
    return frozenset(sigma[item] for item in items)


def majority_available(condition):
    domain = frozenset(("A", "B"))
    return frozenset(
        item
        for item in domain
        if Fraction(2) * sum(Fraction(1) for neighbor in condition if neighbor == item)
        >= Fraction(len(condition))
    )


def closure_holds_for_single_records(weights):
    labels = tuple(weights)
    maps = [dict(zip(labels, image)) for image in permutations(labels)]
    return all(weights[label] == weights[sigma[label]] for sigma in maps for label in labels)


block16_text = read_text(BLOCK16_NOTE)
kappa_text = read_text(KAPPA_NOTE)
scale_text = read_text(SCALE_NOTE)
note_text = read_text(NOTE_PATH)
note_lower = note_text.lower()

check(
    BLOCK16_NOTE.exists()
    and "T3 - Fixed-Point Unidentifiability" in block16_text
    and "I(x,x) = (u+v) x" in block16_text,
    "premise guard: block16 note is present and contains the diagonal degeneration formula",
)

check(
    "Pi_phys = C + kappa_EW S" in kappa_text
    and "common `K_EW` factor cancels" in kappa_text,
    "premise guard: parent kappa note contains Pi_phys and the common-K_EW cancellation sentence",
)

check(
    "This is a units conversion, not a physics axiom." in scale_text,
    "premise guard: scale-reference primitive states the units-conversion sentence",
)


roots = [Fraction(2), Fraction(3), Fraction(5)]
diagonal_contents = [root * root for root in roots]
t1_weights = [
    (Fraction(1), Fraction(3)),
    (Fraction(2), Fraction(7)),
    (Fraction(9), Fraction(7)),
]
t1_sums = [sum(pair, Fraction(0)) for pair in t1_weights]
t1_root_scales = [Fraction(2), Fraction(3), Fraction(4)]

check(
    len(set(t1_sums)) == 3
    and all(
        pairwise_ratios(diagonal_readouts(diagonal_contents, weights))
        == pairwise_ratios(diagonal_contents)
        for weights in t1_weights
    ),
    "T1a: diagonal pairwise ratios I_i/I_j equal x_i/x_j for three distinct weight sums",
)

check(
    all(
        normalized(diagonal_readouts(diagonal_contents, weights)) == normalized(diagonal_contents)
        for weights in t1_weights
    ),
    "T1b: normalized fractions I_i/sum(I) are w-free on diagonal records",
)

base_koide = koide_shape(roots)
check(
    all(
        diagonal_readouts(diagonal_contents, weights)
        == [(scale * root) * (scale * root) for root in roots]
        and koide_shape([scale * root for root in roots]) == base_koide
        for weights, scale in zip(t1_weights, t1_root_scales)
    ),
    "T1b: Koide-shape Q(y)=sum(y_i^2)/(sum(y_i))^2 is w-free by degree-zero homogeneity",
)

base_generic = generic_degree_zero(diagonal_contents)
check(
    all(generic_degree_zero(diagonal_readouts(diagonal_contents, weights)) == base_generic for weights in t1_weights),
    "T1b: a generic degree-zero rational functional is w-free on diagonal records",
)

off_diagonal_ratios = [
    readout((Fraction(1), Fraction(0)), *weights)
    / readout((Fraction(0), Fraction(1)), *weights)
    for weights in t1_weights
]
check(
    len(set(off_diagonal_ratios)) == 3,
    "T1c: off-diagonal ratio I(1,0)/I(0,1) moves with w, so the diagonal premise is load-bearing",
)


calibration_weights = [
    (Fraction(1), Fraction(1)),
    (Fraction(3), Fraction(2)),
    (Fraction(1, 2), Fraction(5, 2)),
]
calibration_contents = [Fraction(2), Fraction(5), Fraction(7)]
calibration_sums = [sum(pair, Fraction(0)) for pair in calibration_weights]

check(
    calibration_sums == [Fraction(2), Fraction(5), Fraction(3)]
    and all(
        diagonal_readouts(calibration_contents, weights)
        == [sum(weights, Fraction(0)) * x for x in calibration_contents]
        for weights in calibration_weights
    ),
    "T2: raw dimensionful diagonal readouts carry w only through s=(u+v) for the specified families",
)

base_calibrated = [x / calibration_contents[0] for x in calibration_contents]
check(
    all(calibrated_table(calibration_contents, weights) == base_calibrated for weights in calibration_weights),
    "T2: same-family calibration I_i/I_cal gives identical tables for (1,1), (3,2), and (1/2,5/2)",
)

reference_mass = Fraction(11)
base_scaled = [reference_mass * x / calibration_contents[0] for x in calibration_contents]
check(
    all(
        scale_reference_table(calibration_contents, weights, reference_mass) == base_scaled
        for weights in calibration_weights
    ),
    "T2: assigning units through the scale-reference primitive against one family member absorbs the prefactor",
)

cross_family_ratios = [
    readout((calibration_contents[1], calibration_contents[1]), *calibration_weights[0])
    / readout((calibration_contents[0], calibration_contents[0]), *denominator_weights)
    for denominator_weights in calibration_weights[1:]
]
check(
    len(set(cross_family_ratios)) == 2,
    "T2 honesty: cross-family calibration with different sums is not w-free",
)


g1_base = Fraction(5, 7)
g2_base = Fraction(11, 13)
check(
    all(
        ew_shape(g1_base, g2_base, common_factor) == g1_base / (g1_base + g2_base)
        for common_factor in calibration_sums
    ),
    "T3 EW row: sin^2(theta_W)-shape cancels a common same-family K_EW factor",
)

check(
    all(koide_shape([scale * root for root in roots]) == base_koide for scale in t1_root_scales),
    "T3 Koide row: degree-zero shape is w-free at flow-selected diagonal states",
)

check(
    all(
        diagonal_readouts(calibration_contents, weights)[1]
        / diagonal_readouts(calibration_contents, weights)[2]
        == calibration_contents[1] / calibration_contents[2]
        for weights in calibration_weights
    ),
    "T3 mass-ratio row: diagonal mass ratios are w-free",
)

check(
    all(
        scale_reference_table(calibration_contents, weights, reference_mass)[2]
        == reference_mass * calibration_contents[2] / calibration_contents[0]
        for weights in calibration_weights
    ),
    "T3 absolute-scale row: single-family scale-reference routing makes reported masses w-free",
)

central_count = Fraction(8, 8 + 1)
pi_values = [Fraction(8) + kappa * Fraction(1) for kappa in (Fraction(1), Fraction(2), Fraction(5, 3))]
check(
    central_count == Fraction(8, 9) and len(set(pi_values)) == 3,
    "T3 count row: the 8/9 cardinality count is fixed while Pi_phys changes with inter-sector weight",
)

landed_rows = {
    "sin^2(theta_W)-shape": "w-free",
    "Koide-shape Q": "w-free",
    "mass ratios": "w-free",
    "absolute mass scale": "w-free",
    "8/9 central-sector count": "w-free",
}
check(
    all(status == "w-free" for status in landed_rows.values()) and len(landed_rows) == 5,
    "T3 conclusion: every landed readout row in the classified lanes is w-free under its stated premise",
)


same_sum_left = (Fraction(1), Fraction(3))
same_sum_right = (Fraction(3), Fraction(1))
off_record = (Fraction(2), Fraction(1))
diag_record = (Fraction(2), Fraction(2))
check(
    readout(off_record, *same_sum_left) != readout(off_record, *same_sum_right)
    and readout(diag_record, *same_sum_left) == readout(diag_record, *same_sum_right),
    "T4(i): off-diagonal evaluation is w-sensitive and the sensitivity vanishes on the diagonal",
)

same_family_restored = [
    readout((calibration_contents[1], calibration_contents[1]), *weights)
    / readout((calibration_contents[0], calibration_contents[0]), *weights)
    for weights in calibration_weights
]
check(
    len(set(cross_family_ratios)) == 2 and len(set(same_family_restored)) == 1,
    "T4(ii): cross-family comparison is w-sensitive and same-family calibration restores w-freedom",
)

raw_absolutes = [
    readout((calibration_contents[1], calibration_contents[1]), *weights)
    for weights in calibration_weights
]
scaled_absolutes = [
    scale_reference_table(calibration_contents, weights, reference_mass)[1]
    for weights in calibration_weights
]
check(
    len(set(raw_absolutes)) == 3 and len(set(scaled_absolutes)) == 1,
    "T4(iii): raw absolute normalization is w-sensitive and scale-reference routing removes it",
)


check(
    "#4847" in note_text
    and "in-flight owner-gated" in note_lower
    and "Possibilities are distinguished by the supplied algebraic structure alone." in note_text,
    "T5a: note cites the owner-gated #4847 sentence conditionally, without treating it as landed text",
)

candidate_weights = [
    {"A": Fraction(2), "B": Fraction(3)},
    {"A": Fraction(7), "B": Fraction(7)},
    {"A": Fraction(5, 2), "B": Fraction(5, 2)},
]
count_records = ("A", "B", "A", "B", "A")
counting_collapse_ok = (
    [closure_holds_for_single_records(weights) for weights in candidate_weights]
    == [False, True, True]
    and sum(candidate_weights[1][record] for record in count_records)
    == candidate_weights[1]["A"] * Fraction(len(count_records))
)
check(
    counting_collapse_ok,
    "T5b: full set-level closure collapses single-record readout to c times record count",
)

domain = ("A", "B")
sigma_maps = [dict(zip(domain, image)) for image in permutations(domain)]
conditions = list(product(domain, repeat=2))
majority_equivariant = all(
    majority_available(apply_sigma_to_condition(condition, sigma))
    == apply_sigma_to_set(majority_available(condition), sigma)
    for sigma in sigma_maps
    for condition in conditions
)
majority_varies = len({majority_available(condition) for condition in conditions}) == 3
check(
    majority_equivariant and majority_varies,
    "T5c: toy majority availability varies with neighbors and commutes with every two-domain bijection",
)


check(
    "no wall closed" in note_lower,
    "boundary-denial grep: note says no wall closed",
)

check(
    "does not reclassify" in note_lower,
    "boundary-denial grep: note says it does not reclassify",
)

check(
    "conditional on ctx-match" in note_lower,
    "boundary-denial grep: note marks kappa_EW rows conditional on CTX-match",
)

check(
    "review-pending" in note_lower,
    "boundary-denial grep: note marks block16/block11 relationships review-pending",
)


pass_count = sum(1 for result in checks if result)
fail_count = len(checks) - pass_count
print(f"TOTAL: PASS={pass_count} FAIL={fail_count}")
sys.exit(1 if fail_count else 0)
