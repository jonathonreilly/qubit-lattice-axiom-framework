#!/usr/bin/env python3
"""Certificate for the explicit massive Wilson-staggered Dobrushin wedge."""

from __future__ import annotations

from itertools import product
from math import sqrt, tanh
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "MASSIVE_WILSON_STAGGERED_DOBRUSHIN_SPATIAL_UNIQUENESS_WEDGE_"
    "BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
PASS = 0
FAIL = 0
TOL = 2.0e-10


def check(name: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {name}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {name}: {detail}")


def directions(dimension: int = 4) -> list[tuple[int, ...]]:
    result = []
    for axis in range(dimension):
        positive = [0] * dimension
        positive[axis] = 1
        result.append(tuple(positive))
        negative = positive.copy()
        negative[axis] = -1
        result.append(tuple(negative))
    return result


def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a + b for a, b in zip(left, right))


def negate(vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(-value for value in vector)


def axis_of(vector: tuple[int, ...]) -> int:
    return next(index for index, value in enumerate(vector) if value)


def two_hop_words() -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    dirs = directions()
    return [(first, second) for first in dirs for second in dirs if second != negate(first)]


def closed_path_orientation_occurrences(order: int) -> tuple[int, tuple[int, ...]]:
    words = two_hop_words()
    closed = 0
    occurrences = [0, 0, 0, 0]
    origin = (0, 0, 0, 0)
    for word_sequence in product(words, repeat=order):
        position = origin
        local_occurrences = [0, 0, 0, 0]
        for word in word_sequence:
            for step in word:
                local_occurrences[axis_of(step)] += 1
                position = add(position, step)
        if position == origin:
            closed += 1
            for axis in range(4):
                occurrences[axis] += local_occurrences[axis]
    return closed, tuple(occurrences)


def staggered_u1_hop(side: int, rng: np.random.Generator) -> np.ndarray:
    dimension = 4
    sites = side**dimension
    matrix = np.zeros((sites, sites), dtype=complex)

    def index(coords: tuple[int, ...]) -> int:
        value = 0
        for coordinate in coords:
            value = value * side + coordinate
        return value

    for coords in product(range(side), repeat=dimension):
        left = index(coords)
        for axis in range(dimension):
            shifted = list(coords)
            shifted[axis] = (shifted[axis] + 1) % side
            right = index(tuple(shifted))
            eta = -1.0 if sum(coords[:axis]) % 2 else 1.0
            phase = np.exp(1j * rng.uniform(-np.pi, np.pi))
            block = 0.5 * eta * phase
            matrix[left, right] += block
            matrix[right, left] -= np.conj(block)
    return matrix


def alpha_f(mass: float) -> float:
    kappa = 14.0 / (mass**2 + 2.0)
    return 1.5 * kappa**2 * (2.0 - kappa) / (1.0 - kappa) ** 2


def threshold_mass() -> float:
    lower, upper = sqrt(12.0), 20.0
    for _ in range(100):
        middle = (lower + upper) / 2.0
        if alpha_f(middle) > 1.0:
            lower = middle
        else:
            upper = middle
    return (lower + upper) / 2.0


def main() -> int:
    dirs = directions()
    words = two_hop_words()
    immediate_reversals = sum(
        second == negate(first) for first in dirs for second in dirs
    )
    check(
        "Eight oriented hops split into eight reversals and 56 nonbacktracking two-hop words",
        len(dirs) == 8 and immediate_reversals == 8 and len(words) == 56,
        f"oriented={len(dirs)}, reversals={immediate_reversals}, nonbacktracking={len(words)}, "
        f"absolute row sum={len(words)/4:.0f}",
    )

    rng = np.random.default_rng(20260712)
    hop = staggered_u1_hop(4, rng)
    squared = hop @ hop
    remainder = squared + 2.0 * np.eye(squared.shape[0])
    remainder_values = np.linalg.eigvalsh((remainder + remainder.conj().T) / 2.0)
    check(
        "A random four-dimensional carrier checks the minus-two diagonal and safe R spectrum",
        np.linalg.norm(hop + hop.conj().T) < TOL
        and np.max(np.abs(np.diag(squared) + 2.0)) < TOL
        and np.min(remainder_values) >= -14.0 - TOL
        and np.max(remainder_values) <= 2.0 + TOL,
        f"anti-Hermitian={np.linalg.norm(hop+hop.conj().T):.3e}, "
        f"diagonal residual={np.max(np.abs(np.diag(squared)+2.0)):.3e}, "
        f"spec(R)=[{np.min(remainder_values):.6f},{np.max(remainder_values):.6f}]",
    )

    incidence_rows = []
    incidence_ok = True
    for order in (2, 3):
        closed, occurrences = closed_path_orientation_occurrences(order)
        current_ok = closed > 0 and len(set(occurrences)) == 1 and sum(occurrences) == 2 * order * closed
        incidence_ok = incidence_ok and current_ok
        incidence_rows.append(f"n={order}:closed={closed},occurrences={occurrences}")
    check(
        "Closed rooted paths distribute occurrence mass equally over four link orientations",
        incidence_ok,
        "; ".join(incidence_rows),
    )

    # Independent finite-distribution check of TV <= tanh(osc(log-ratio)/4).
    tv_rows = []
    tv_ok = True
    for size in (2, 5, 13):
        base = rng.random(size) + 0.1
        base /= np.sum(base)
        raw = rng.normal(size=size)
        delta = float(np.max(raw) - np.min(raw))
        changed = base * np.exp(-raw)
        changed /= np.sum(changed)
        tv = 0.5 * float(np.sum(np.abs(base - changed)))
        bound = tanh(delta / 4.0)
        tv_ok = tv_ok and tv <= bound + TOL
        tv_rows.append(f"N={size}:TV={tv:.6f}<=tanh(osc/4)={bound:.6f}")
    check(
        "Half-L1 total variation obeys the likelihood-ratio oscillation bound",
        tv_ok,
        "; ".join(tv_rows),
    )

    # Direct series partial sums versus the closed form.
    series_rows = []
    series_ok = True
    for mass in (6.0, 8.0, 10.0):
        kappa = 14.0 / (mass**2 + 2.0)
        direct = 1.5 * sum(order * kappa**order for order in range(2, 500))
        closed_form = alpha_f(mass)
        beta_max = (1.0 - closed_form) / 18.0
        series_ok = series_ok and abs(direct - closed_form) < 2.0e-14 and beta_max > 0.0
        series_rows.append(
            f"m={mass:g}:kappa={kappa:.6f},alphaF={closed_form:.6f},beta<{beta_max:.7f}"
        )
    check(
        "Fermion incidence series and explicit nonempty uniqueness intervals agree",
        series_ok,
        "; ".join(series_rows),
    )

    critical_mass = threshold_mass()
    check(
        "The beta-zero wedge has the stated sharp threshold for this sufficient bound",
        abs(critical_mass - 5.809057503265459) < 2.0e-12
        and abs(alpha_f(critical_mass) - 1.0) < 2.0e-12,
        f"m0={critical_mass:.12f}, alphaF(m0)={alpha_f(critical_mass):.12f}",
    )

    note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    conditions = [
        "supplied Wilson-staggered action",
        "strict Dobrushin inequality",
        "positive mass",
        "spatial uniqueness",
        "continuum/SM/GR closure",
    ]
    pairs = [
        f"| {conditions[left]} | {conditions[right]} |"
        for left in range(len(conditions))
        for right in range(left + 1, len(conditions))
    ]
    required = [
        "kappa=14/(m^2+2)",
        "m>sqrt(12)",
        "alpha_W<=6*3*beta=18beta",
        "3 kappa^n/4",
        "||mu-nu||_TV=sup_A|mu(A)-nu(A)|=(1/2)||dmu-dnu||_1",
        "Failure of (0.2) says",
        "does not reach `beta=6`",
        "Euclidean or physical probability rule",
        "No axiom-update stop",
        "No-Go Discipline N1--N8",
        "### N3 — hidden-condition phrase scan",
        "### N4 — citation/residual matching",
        "### N5 — rhetoric and resolution audit",
        "### N6 — partial-closure, convention, reframe, and primitive scan",
        "### N7 — hostile steelman",
        "### N8 — cross-cycle echo",
        "Test and result",
        "Left closes right? | Right closes left? | Independent?",
        "Cited witness and location | Witness residual | Present residual | Match? | Disposition",
        "Statement / resolution | Tested? | Permitted conclusion",
        "Points failing (0.2) | No",
        "Volume-growing/nonlocal observables | No",
        "invariant vacuum is one-dimensional",
        "Delta_OS>=-(2a_tau)^(-1)log rho>0",
        "Unconstructed charged superselection sectors | No",
        "four-dimensional scalar `U(1)`",
        "actual `SU(3)` dependence is analytic",
        "Lattice, Qubit, Admissibility, and Record",
        "weighted comparison form gives exponential",
        "weighted row below one gives the exponential comparison/covariance decay",
        "strict Dobrushin inequality | spatial uniqueness | Yes | No | No",
        "Sole direct in-repo dependency",
        "Retirement mechanism and applicability",
    ]
    hidden_rows = [
        "| `we assume` |",
        "| `by construction` |",
        "| `as is standard` |",
        "| `the framework provides` |",
        "| `bridge context` |",
        "| `background` |",
        "| `naturally` |",
        "| `obviously` |",
        "| `standard QFT` |",
        "| `registered` |",
        "| `canonical` |",
    ]
    missing = [item for item in required + hidden_rows + pairs if item not in note_text]
    attempted = note_text.count("| `ATTEMPTED` |")
    independent_pairs = note_text.count("| No | No | Yes |")
    forbidden = [
        item
        for item in ("Lattice, Quantum", "Block 20", "Block 21", "Blocks 20--21")
        if item in note_text
    ]
    check(
        "Source-note boundary and N1-N8 contract",
        not missing
        and not forbidden
        and attempted >= 8
        and independent_pairs >= 9,
        f"missing={missing}; forbidden={forbidden}; attempted={attempted}; "
        f"independent pairs={independent_pairs}",
    )

    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
