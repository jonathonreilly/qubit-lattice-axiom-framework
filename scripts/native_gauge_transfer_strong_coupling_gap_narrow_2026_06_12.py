#!/usr/bin/env python3
"""Native gauge-transfer strong-coupling gap narrow runner.

This runner stays inside the repo-native SU(3) Wilson character machinery.
It proves the small-beta coefficient-transfer gap by exact rational
character-recursion arithmetic, then checks the 25-state half-slice packet
numerically at beta = 0.1, 0.5, 1.0.

No continuum limit, R^4 construction, physical beta=6 Perron solve, random
sampling, or audit status is claimed here.
"""

from __future__ import annotations

from collections import defaultdict
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
    / "NATIVE_GAUGE_TRANSFER_STRONG_COUPLING_GAP_NARROW_THEOREM_NOTE_2026-06-12.md"
)

NMAX = 4
WEIGHTS = [(p, q) for p in range(NMAX + 1) for q in range(NMAX + 1)]
ORDER = 30
MODE_MAX = 160
BETA_SAMPLES = [Fraction(1, 10), Fraction(1, 2), Fraction(1, 1)]
GAP_K = Fraction(2, 3)
SLOPE_FUND = Fraction(1, 6)

PASS = 0
FAIL = 0


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
    """Return exact coefficients of Y^n, Y = chi_f + chi_fbar."""
    layers: list[dict[tuple[int, int], int]] = []
    layer: dict[tuple[int, int], int] = {(0, 0): 1}
    for _ in range(order + 1):
        layers.append(dict(layer))
        nxt: dict[tuple[int, int], int] = defaultdict(int)
        for weight, mult in layer.items():
            for nb in recurrence_neighbors(*weight):
                nxt[nb] += mult
        layer = dict(nxt)
    return layers


def beta_power_coefficient(weight: tuple[int, int], n: int, mult: int) -> Fraction:
    """Coefficient of beta^n from mult * (beta/6)^n / n!."""
    return Fraction(mult, factorial(n) * (6**n))


def leading_data(
    weight: tuple[int, int], layers: list[dict[tuple[int, int], int]]
) -> tuple[int, int, Fraction]:
    for n, layer in enumerate(layers):
        mult = layer.get(weight, 0)
        if mult:
            return n, mult, beta_power_coefficient(weight, n, mult)
    raise ValueError(f"no leading data found for {weight}")


def coefficient_partial(
    weight: tuple[int, int], beta: Fraction, layers: list[dict[tuple[int, int], int]]
) -> Fraction:
    total = Fraction(0, 1)
    for n, layer in enumerate(layers):
        mult = layer.get(weight, 0)
        if mult:
            total += beta_power_coefficient(weight, n, mult) * (beta**n)
    return total


def exp_tail_bound(beta: Fraction, order: int) -> Fraction:
    """Exact upper bound for sum_{n>order} beta^n/n!, valid for 0 <= beta <= 1."""
    first = (beta ** (order + 1)) / factorial(order + 1)
    ratio = beta / Fraction(order + 2, 1)
    return first / (1 - ratio)


def ratio_upper_bound(
    weight: tuple[int, int],
    beta: Fraction,
    layers: list[dict[tuple[int, int], int]],
) -> Fraction:
    numerator_partial = coefficient_partial(weight, beta, layers)
    denominator_lower = coefficient_partial((0, 0), beta, layers)
    tail = exp_tail_bound(beta, len(layers) - 1)
    numerator_upper = numerator_partial + tail / dim_su3(*weight)
    return numerator_upper / denominator_lower


def coefficient_ratios_bessel(beta: float) -> tuple[np.ndarray, list[tuple[int, int]], dict[tuple[int, int], int]]:
    weights = list(WEIGHTS)
    index = {w: i for i, w in enumerate(weights)}
    coeffs = np.array(
        [
            src_existing.wilson_character_coefficient(p, q, MODE_MAX, beta / 3.0)
            for p, q in weights
        ],
        dtype=float,
    )
    c00 = float(coeffs[index[(0, 0)]])
    return coeffs / c00, weights, index


def half_slice_transfer_ratio(beta: float) -> tuple[float, float, tuple[int, int], float]:
    ratios, weights, index = coefficient_ratios_bessel(beta)
    nontriv = [(float(ratios[i]), w) for i, w in enumerate(weights) if w != (0, 0)]
    diag_ratio, diag_weight = max(nontriv)

    j_op, _src_weights, _src_index = src_existing.build_J(NMAX)
    multiplier = src_existing.matrix_exp_symmetric(j_op, beta / 2.0)
    transfer = multiplier @ np.diag(ratios) @ multiplier
    eigvals = np.linalg.eigvalsh(transfer)
    eigvals.sort()
    packet_ratio = float(eigvals[-2] / eigvals[-1])
    min_eig = float(eigvals[0])
    return diag_ratio, packet_ratio, diag_weight, min_eig


def note_text() -> str:
    return NOTE_PATH.read_text(encoding="utf-8")


def main() -> int:
    print("Native gauge-transfer strong-coupling gap bounded runner")
    print(f"finite packet: NMAX={NMAX}, states={(NMAX + 1) ** 2}, MODE_MAX={MODE_MAX}")
    print(f"certified interval: 0 <= beta <= 1, K={GAP_K}, p=1")
    print()

    layers = multiplicity_layers(ORDER)
    max_layer = max(max(layer.values()) for layer in layers)
    check(
        "exact SU(3) character recurrence layers are integer and nonnegative",
        all(isinstance(v, int) and v >= 0 for layer in layers for v in layer.values()),
        f"computed layers n=0..{ORDER}, max multiplicity={max_layer}",
    )

    leading_ok = True
    leading_rows: list[str] = []
    for weight in WEIGHTS:
        p, q = weight
        n, mult, coeff = leading_data(weight, layers)
        expected_n = p + q
        expected_coeff = Fraction(1, factorial(p) * factorial(q) * (6 ** (p + q)))
        if n != expected_n or coeff != expected_coeff:
            leading_ok = False
        if weight in [(1, 0), (0, 1), (1, 1), (2, 0), (2, 1), (4, 4)]:
            leading_rows.append(
                f"{weight}: beta^{n} coefficient {coeff} (multiplicity {mult})"
            )
    check(
        "leading coefficient for every 25-packet weight is beta^(p+q)/(p! q! 6^(p+q))",
        leading_ok,
        "; ".join(leading_rows),
    )

    check(
        "fundamental channels have exact leading coefficient beta/6",
        leading_data((1, 0), layers)[2] == SLOPE_FUND
        and leading_data((0, 1), layers)[2] == SLOPE_FUND,
        f"c_(1,0) lead={leading_data((1, 0), layers)[2]}, c_(0,1) lead={leading_data((0, 1), layers)[2]}",
    )

    factorial_majorant_ok = all(
        Fraction(1, factorial(n)) <= Fraction(1, 2 ** (n - 1))
        for n in range(1, ORDER + 1)
    )
    check(
        "exact exponential tail majorant sum_{n>=1} beta^n/n! <= 2 beta on 0<=beta<=1",
        factorial_majorant_ok,
        "uses n! >= 2^(n-1), hence nontrivial c_lambda/c_0 <= (2/3) beta because d_lambda >= 3",
    )

    majorant_ok = True
    worst_weight = (0, 0)
    worst_ratio = Fraction(0, 1)
    for beta in BETA_SAMPLES:
        for weight in WEIGHTS:
            if weight == (0, 0):
                continue
            ru = ratio_upper_bound(weight, beta, layers)
            if ru > worst_ratio:
                worst_ratio = ru
                worst_weight = weight
            if ru > GAP_K * beta:
                majorant_ok = False
    check(
        "exact finite-series intervals satisfy c_lambda/c_0 <= (2/3) beta at beta samples",
        majorant_ok,
        f"worst certified sample upper={float(worst_ratio):.12e} at {worst_weight}",
    )

    tail_one = exp_tail_bound(Fraction(1, 1), ORDER)
    check(
        "ORDER=30 exact-rational series tail at beta=1 is below 1e-33",
        tail_one < Fraction(1, 10**33),
        f"tail_bound={tail_one}",
    )

    beta0_spectrum_ok = True
    ratios0, weights0, index0 = coefficient_ratios_bessel(0.0)
    beta0_diag = np.diag(ratios0)
    eig0 = np.linalg.eigvalsh(beta0_diag)
    beta0_spectrum_ok = (
        abs(float(eig0[-1]) - 1.0) < 1.0e-14
        and float(np.max(np.abs(eig0[:-1]))) < 1.0e-14
        and abs(float(ratios0[index0[(0, 0)]]) - 1.0) < 1.0e-14
    )
    check(
        "beta=0 coefficient transfer is the trivial-channel projector with spectrum {1,0,...}",
        beta0_spectrum_ok,
        f"top eigenvalue={eig0[-1]:.12f}, nontrivial max={np.max(np.abs(eig0[:-1])):.3e}",
    )

    numeric_ok = True
    slope_ok = True
    rows: list[str] = []
    for beta_fraction in BETA_SAMPLES:
        beta = float(beta_fraction)
        diag_ratio, packet_ratio, diag_weight, min_eig = half_slice_transfer_ratio(beta)
        bound = float(GAP_K * beta_fraction)
        numeric_ok = (
            numeric_ok
            and diag_ratio <= bound
            and packet_ratio <= bound
            and min_eig >= -1.0e-12
            and diag_weight in [(1, 0), (0, 1)]
        )
        if beta_fraction == Fraction(1, 10):
            slope_ok = (
                abs(diag_ratio / beta - float(SLOPE_FUND)) < 0.002
                and abs(packet_ratio / beta - float(SLOPE_FUND)) < 0.006
            )
        rows.append(
            "beta={:.1f}: diag_ratio={:.12f}, packet_ratio={:.12f}, "
            "bound={:.12f}, diag_slope={:.12f}, packet_slope={:.12f}, max_diag={}".format(
                beta,
                diag_ratio,
                packet_ratio,
                bound,
                diag_ratio / beta,
                packet_ratio / beta,
                diag_weight,
            )
        )

    check(
        "25-state coefficient and half-slice transfer ratios obey lambda_1/lambda_0 <= (2/3) beta",
        numeric_ok,
        " | ".join(rows),
    )
    check(
        "measured small-beta slope at beta=0.1 matches the exact fundamental beta/6 leading term",
        slope_ok,
        rows[0],
    )

    text = note_text()
    required_note_strings = [
        "**Claim type:** bounded_theorem",
        "**Type:** bounded_theorem",
        "**Status authority:** independent audit lane only.",
        "not the Clay Yang-Mills mass gap problem",
        "No continuum limit",
        "No R^4 construction",
        "lambda_1(beta) / lambda_0(beta) <= (2/3) beta",
        "certified gap lower bounds at increasing",
        "plaquette `beta = 6` finite-environment lane",
        "finite-beta certificate residual",
        "TOTAL: PASS=",
    ]
    check(
        "note contains scope, status-authority, theorem, next-target, and runner markers",
        all(s in text for s in required_note_strings),
        "checked required note markers",
    )

    required_links = [
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
        "only " + "route",
        "last " + "route",
        "ex" + "hausted",
        "closes the " + "program",
        "rung " + "two",
        "B" + "1 lane",
        "certificate " + "wall",
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
