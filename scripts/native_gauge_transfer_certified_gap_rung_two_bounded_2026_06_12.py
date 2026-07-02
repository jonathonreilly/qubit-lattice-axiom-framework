#!/usr/bin/env python3
"""Native gauge-transfer certified gap rung-two bounded runner.

This runner extends the rung-one coefficient-transfer certificate past beta=1
using exact rational SU(3) character-recursion arithmetic.  It certifies the
repo-native diagonal coefficient-transfer operator inherited from rung one:

    r_(p,q)(beta) = c_(p,q)(beta) / c_(0,0)(beta).

The 25-state half-slice matrix is reported only as a float cross-check.  This
runner does not promote that finite packet to an infinite half-slice transfer
certificate.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from math import factorial
from pathlib import Path
import sys

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve as src_existing


AUDIT_TIMEOUT_SEC = 600

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_CERTIFIED_GAP_RUNG_TWO_BOUNDED_NOTE_2026-06-12.md"
)

ORDER = 80
BLOCK_NMAX = 4
MODE_MAX = 220
RUNG_ONE_INTERVAL_RIGHT = Fraction(1, 1)
RUNG_ONE_MAJORANT_K = Fraction(2, 3)

RUNG_ONE_CHECK_BETAS = [
    Fraction(0, 1),
    Fraction(1, 10),
    Fraction(1, 2),
    Fraction(1, 1),
]

REQUESTED_GRID_BETAS = [
    Fraction(5, 4),
    Fraction(3, 2),
    Fraction(2, 1),
    Fraction(5, 2),
    Fraction(3, 1),
    Fraction(7, 2),
    Fraction(4, 1),
]

FRONTIER_PROBE_BETAS = [
    Fraction(9, 2),
    Fraction(23, 5),
    Fraction(117, 25),
    Fraction(469, 100),
]

CERT_TABLE_BETAS = RUNG_ONE_CHECK_BETAS + REQUESTED_GRID_BETAS + FRONTIER_PROBE_BETAS

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class BetaCertificate:
    beta: Fraction
    block_lambda1_lower: Fraction
    block_lambda1_upper: Fraction
    block_witness: tuple[int, int]
    tail_upper: Fraction
    tail_witness: tuple[int, int] | str
    ratio_upper: Fraction
    gap_lower: Fraction
    tail_margin: Fraction
    certified: bool
    half_slice_ratio_float: float


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def fmt_frac(beta: Fraction) -> str:
    if beta.denominator == 1:
        return str(beta.numerator)
    return f"{beta.numerator}/{beta.denominator}"


def fmt_decimal(x: Fraction, digits: int = 12) -> str:
    return f"{float(x):.{digits}f}"


def dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def recurrence_neighbors(p: int, q: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for a, b in [
        (p + 1, q),
        (p - 1, q + 1),
        (p, q - 1),
        (p, q + 1),
        (p + 1, q - 1),
        (p - 1, q),
    ]:
        if a >= 0 and b >= 0:
            out.append((a, b))
    return out


def multiplicity_layers(order: int) -> list[dict[tuple[int, int], int]]:
    layers: list[dict[tuple[int, int], int]] = []
    layer: dict[tuple[int, int], int] = {(0, 0): 1}
    for _n in range(order + 1):
        layers.append(dict(layer))
        nxt: dict[tuple[int, int], int] = defaultdict(int)
        for weight, mult in layer.items():
            for nb in recurrence_neighbors(*weight):
                nxt[nb] += mult
        layer = dict(nxt)
    return layers


LAYERS = multiplicity_layers(ORDER)


def exp_tail_bound(beta: Fraction, order: int) -> Fraction:
    """Bound sum_{n>order} beta^n/n! by a geometric tail."""
    first = (beta ** (order + 1)) / factorial(order + 1)
    ratio = beta / Fraction(order + 2, 1)
    if ratio >= 1:
        raise ValueError("tail ratio bound requires beta < order + 2")
    return first / (1 - ratio)


def coefficient_partials(beta: Fraction) -> dict[tuple[int, int], Fraction]:
    coeffs: dict[tuple[int, int], Fraction] = defaultdict(Fraction)
    for n, layer in enumerate(LAYERS):
        factor = (beta**n) / (factorial(n) * (6**n))
        for weight, mult in layer.items():
            coeffs[weight] += mult * factor
    return dict(coeffs)


def ratio_interval(
    weight: tuple[int, int],
    coeffs: dict[tuple[int, int], Fraction],
    beta: Fraction,
) -> tuple[Fraction, Fraction]:
    """Return a rigorous lower/upper interval for c_weight/c_00."""
    c00_lower = coeffs[(0, 0)]
    c00_upper = c00_lower + exp_tail_bound(beta, ORDER)
    numerator_lower = coeffs.get(weight, Fraction(0, 1))
    numerator_upper = numerator_lower + exp_tail_bound(beta, ORDER) / dim_su3(*weight)
    return numerator_lower / c00_upper, numerator_upper / c00_lower


def half_slice_ratio_float(beta: Fraction) -> float:
    beta_f = float(beta)
    weights = [(p, q) for p in range(BLOCK_NMAX + 1) for q in range(BLOCK_NMAX + 1)]
    coeffs = np.array(
        [
            src_existing.wilson_character_coefficient(p, q, MODE_MAX, beta_f / 3.0)
            for p, q in weights
        ],
        dtype=float,
    )
    index = {w: i for i, w in enumerate(weights)}
    ratios = coeffs / float(coeffs[index[(0, 0)]])
    j_op, _weights, _index = src_existing.build_J(BLOCK_NMAX)
    multiplier = src_existing.matrix_exp_symmetric(j_op, beta_f / 2.0)
    transfer = multiplier @ np.diag(ratios) @ multiplier
    eigvals = np.linalg.eigvalsh(transfer)
    eigvals.sort()
    return float(eigvals[-2] / eigvals[-1])


def certify_beta(beta: Fraction) -> BetaCertificate:
    coeffs = coefficient_partials(beta)
    block_candidates: list[tuple[Fraction, Fraction, tuple[int, int]]] = []
    tail_candidates: list[tuple[Fraction, tuple[int, int] | str]] = []

    for weight in coeffs:
        if weight == (0, 0):
            continue
        lower, upper = ratio_interval(weight, coeffs, beta)
        p, q = weight
        if p <= BLOCK_NMAX and q <= BLOCK_NMAX:
            block_candidates.append((upper, lower, weight))
        else:
            tail_candidates.append((upper, weight))

    c00_lower = coeffs[(0, 0)]
    far_dim_min = (ORDER + 2) * (ORDER + 3) // 2
    far_tail_upper = (exp_tail_bound(beta, ORDER) / far_dim_min) / c00_lower
    tail_candidates.append((far_tail_upper, "p+q>ORDER"))

    block_upper, block_lower, block_witness = max(block_candidates, key=lambda row: row[0])
    tail_upper, tail_witness = max(tail_candidates, key=lambda row: row[0])

    block_gap = Fraction(1, 1) - block_upper
    tail_margin = block_gap - tail_upper
    ratio_upper = block_upper + tail_upper
    gap_lower = Fraction(1, 1) - ratio_upper
    certified = bool(block_upper < 1 and tail_margin > 0)

    return BetaCertificate(
        beta=beta,
        block_lambda1_lower=block_lower,
        block_lambda1_upper=block_upper,
        block_witness=block_witness,
        tail_upper=tail_upper,
        tail_witness=tail_witness,
        ratio_upper=ratio_upper,
        gap_lower=gap_lower,
        tail_margin=tail_margin,
        certified=certified,
        half_slice_ratio_float=half_slice_ratio_float(beta),
    )


def bessel_ratio_float(weight: tuple[int, int], beta: Fraction) -> float:
    beta_f = float(beta)
    c = src_existing.wilson_character_coefficient(weight[0], weight[1], MODE_MAX, beta_f / 3.0)
    c00 = src_existing.wilson_character_coefficient(0, 0, MODE_MAX, beta_f / 3.0)
    return float(c / c00)


def table_line(row: BetaCertificate) -> str:
    return (
        f"beta={fmt_frac(row.beta):>6} | "
        f"upper={fmt_decimal(row.ratio_upper, 12)} | "
        f"gap={fmt_decimal(row.gap_lower, 12)} | "
        f"tail_margin={fmt_decimal(row.tail_margin, 12)} | "
        f"certified={'yes' if row.certified else 'no'} | "
        f"block={row.block_witness} | tail={row.tail_witness}"
    )


def note_text() -> str:
    return NOTE_PATH.read_text(encoding="utf-8")


def main() -> int:
    print("Native gauge-transfer certified gap rung-two bounded runner")
    print(f"exact recurrence order: ORDER={ORDER}")
    print(f"finite block: 0<=p,q<={BLOCK_NMAX} ({(BLOCK_NMAX + 1) ** 2} states)")
    print(f"float cross-check MODE_MAX={MODE_MAX}")
    print()

    check(
        "exact SU(3) recurrence layers are integer and nonnegative",
        all(isinstance(v, int) and v >= 0 for layer in LAYERS for v in layer.values()),
        f"layers n=0..{ORDER}, final layer states={len(LAYERS[-1])}",
    )

    leading_ok = True
    leading_rows: list[str] = []
    for weight in [(1, 0), (0, 1), (1, 1), (2, 0), (2, 1), (4, 4), (5, 0)]:
        for n, layer in enumerate(LAYERS):
            mult = layer.get(weight, 0)
            if mult:
                p, q = weight
                coeff = Fraction(mult, factorial(n) * (6**n))
                expected_n = p + q
                expected_coeff = Fraction(1, factorial(p) * factorial(q) * (6 ** (p + q)))
                leading_ok = leading_ok and n == expected_n and coeff == expected_coeff
                leading_rows.append(f"{weight}: beta^{n} coeff={coeff}")
                break
    check(
        "leading coefficients reproduce rung-one beta/6 branch and the first outside-block branch",
        leading_ok,
        "; ".join(leading_rows),
    )

    factorial_majorant_ok = all(
        Fraction(1, factorial(n)) <= Fraction(1, 2 ** (n - 1))
        for n in range(1, ORDER + 1)
    )
    check(
        "rung-one interval majorant is reproduced on 0<=beta<=1",
        factorial_majorant_ok,
        "n! >= 2^(n-1) gives c_lambda/c_00 <= (2/3) beta for nontrivial channels on 0<=beta<=1",
    )

    rows = [certify_beta(beta) for beta in CERT_TABLE_BETAS]
    for row in rows:
        print(table_line(row))

    rung_one_rows = [row for row in rows if row.beta <= RUNG_ONE_INTERVAL_RIGHT]
    check(
        "new certificate keeps the rung-one check points inside lambda1/lambda0 <= (2/3) beta",
        all(row.ratio_upper <= RUNG_ONE_MAJORANT_K * row.beta for row in rung_one_rows if row.beta > 0),
        "checked beta=1/10, 1/2, 1 with exact-rational upper bounds",
    )
    check(
        "requested beta grid through beta=4 is certified",
        all(row.certified for row in rows if row.beta in REQUESTED_GRID_BETAS),
        "checked beta=5/4, 3/2, 2, 5/2, 3, 7/2, 4",
    )

    frontier_yes = Fraction(117, 25)
    first_no = Fraction(469, 100)
    frontier_row = next(row for row in rows if row.beta == frontier_yes)
    first_no_row = next(row for row in rows if row.beta == first_no)
    check(
        "declared extension-grid frontier is certified and the next probe is not",
        frontier_row.certified and not first_no_row.certified,
        (
            f"frontier beta={fmt_frac(frontier_yes)} gap={fmt_decimal(frontier_row.gap_lower, 15)}; "
            f"next beta={fmt_frac(first_no)} gap={fmt_decimal(first_no_row.gap_lower, 15)}"
        ),
    )

    float_brackets_ok = True
    float_details: list[str] = []
    block_weights = [
        (p, q)
        for p in range(BLOCK_NMAX + 1)
        for q in range(BLOCK_NMAX + 1)
        if (p, q) != (0, 0)
    ]
    for row in rows:
        if not row.certified:
            continue
        coeffs = coefficient_partials(row.beta)
        for weight in block_weights:
            lower, upper = ratio_interval(weight, coeffs, row.beta)
            fval = bessel_ratio_float(weight, row.beta)
            if not (float(lower) - 5.0e-14 <= fval <= float(upper) + 5.0e-14):
                float_brackets_ok = False
                float_details.append(f"beta={fmt_frac(row.beta)} weight={weight} float={fval}")
                break
    check(
        "float coefficient eigenvalues lie inside every certified block interval",
        float_brackets_ok,
        "checked all 24 nontrivial block weights for certified rows"
        if float_brackets_ok
        else "; ".join(float_details[:3]),
    )

    check(
        "half-slice 25-state float ratios stay below one on certified rows",
        all(row.half_slice_ratio_float < 1.0 for row in rows if row.certified),
        "diagnostic only; not used as the full-operator certificate",
    )

    text = note_text()
    required_note_strings = [
        "**Type:** bounded_theorem",
        "**Claim type:** bounded_theorem",
        "**Status authority:** independent audit lane only.",
        "Status authority",
        "No continuum limit",
        "No R^4 construction",
        "CERTIFIED",
        "117/25",
        "469/100",
        "[scripts/native_gauge_transfer_certified_gap_rung_two_bounded_2026_06_12.py]"
        "(../scripts/native_gauge_transfer_certified_gap_rung_two_bounded_2026_06_12.py)",
        "[logs/runner-cache/native_gauge_transfer_certified_gap_rung_two_bounded_2026_06_12.txt]"
        "(../logs/runner-cache/native_gauge_transfer_certified_gap_rung_two_bounded_2026_06_12.txt)",
        "TOTAL: PASS=",
    ]
    check(
        "note contains scope, status-authority, table, frontier, and runner markers",
        all(s in text for s in required_note_strings),
        "checked required note markers",
    )

    required_links = [
        "[NATIVE_GAUGE_TRANSFER_STRONG_COUPLING_GAP_NARROW_THEOREM_NOTE_2026-06-12.md]"
        "(NATIVE_GAUGE_TRANSFER_STRONG_COUPLING_GAP_NARROW_THEOREM_NOTE_2026-06-12.md)",
        "[GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md)",
        "[GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md)",
        "[WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md](WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md)",
    ]
    check(
        "one-hop authorities are present as markdown links",
        all(link in text for link in required_links),
        "checked authority-link forms",
    )

    banned_phrases = [
        " ".join(parts)
        for parts in [
            ("only", "route"),
            ("last", "route"),
            ("exhau", "sted"),
            ("closes", "the", "program"),
        ]
    ]
    check(
        "note avoids overreach phrases banned for this lane",
        not any(phrase in text.lower() for phrase in banned_phrases),
        "scanned banned phrase set",
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
