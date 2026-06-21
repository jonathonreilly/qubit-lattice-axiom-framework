#!/usr/bin/env python3
"""Route-2 double-local projector-normalization conditional bridge.

This is a stretch attempt on the nonseparable E/T covariance primitive exposed
by the Route-2 q_E no-go stack.  It does not adopt a new primitive.  It records
the exact condition under which the covariance bridge would close:

    q_X must scale as w_X^{-2},

where w_X is the local per-arm projector weight for the E or T1 channel on the
six-arm O_h star.  Since w_E=1/3 and w_T=1/2, this gives

    q_E/q_T = (w_E/w_T)^{-2} = 9/4.

The runner also falsifies the nearby one-factor and raw quadratic variants.
No observed masses, fitted targets, or audit verdicts are used.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import itertools

import numpy as np


TARGET_QT = Fraction(5, 6)
TARGET_QE = Fraction(15, 8)
TARGET_LAMBDA = Fraction(9, 4)
TARGET_RHO_E = Fraction(21, 4)

ARMS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
AIDX = {a: i for i, a in enumerate(ARMS)}


@dataclass
class Check:
    name: str
    ok: bool
    detail: str
    status: str


CHECKS: list[Check] = []


def record(name: str, ok: bool, detail: str, status: str = "EXACT") -> None:
    CHECKS.append(Check(name=name, ok=ok, detail=detail, status=status))
    tag = "PASS" if ok else "FAIL"
    print(f"[{status}] {tag}: {name}")
    if detail:
        print(f"    {detail}")


def oh_group() -> list[np.ndarray]:
    mats: list[np.ndarray] = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            m = np.zeros((3, 3), dtype=int)
            for row in range(3):
                m[row, perm[row]] = signs[row]
            mats.append(m)
    return mats


def arm_rep(m: np.ndarray) -> np.ndarray:
    p = np.zeros((6, 6), dtype=float)
    for arm in ARMS:
        image = tuple(int(x) for x in (m @ np.array(arm)))
        p[AIDX[image], AIDX[arm]] = 1.0
    return p


def fraction_from_float(value: float) -> Fraction:
    return Fraction(value).limit_denominator(10_000)


def projector_weights() -> tuple[Fraction, Fraction, Fraction]:
    reps = [arm_rep(m) for m in oh_group()]
    p_a1 = sum(reps) / len(reps)
    antipodal = arm_rep(-np.eye(3, dtype=int))
    p_t1 = (np.eye(6) - antipodal) / 2.0
    p_e = (np.eye(6) + antipodal) / 2.0 - p_a1
    return (
        fraction_from_float(p_a1[0, 0]),
        fraction_from_float(p_e[0, 0]),
        fraction_from_float(p_t1[0, 0]),
    )


def lambda_for_exponent(power: int, w_e: Fraction, w_t: Fraction) -> Fraction:
    ratio = w_e / w_t
    if power >= 0:
        return ratio**power
    return Fraction(1, 1) / (ratio ** abs(power))


def endpoint_chain(lambda_value: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    q_e = lambda_value * TARGET_QT
    rho_e = 6 * (q_e - 1)
    center_te = Fraction(-2, 1) * TARGET_QT / q_e
    return q_e, rho_e, center_te


def main() -> int:
    print("Route-2 double-local projector-normalization conditional bridge")
    print("=" * 86)

    w_a1, w_e, w_t = projector_weights()
    kappa = w_t / w_e
    record(
        "the six-arm O_h projector weights are exact and give kappa=3/2",
        (w_a1, w_e, w_t, kappa) == (Fraction(1, 6), Fraction(1, 3), Fraction(1, 2), Fraction(3, 2)),
        f"w_A1={w_a1}, w_E={w_e}, w_T1={w_t}, kappa=w_T1/w_E={kappa}",
    )

    rows: list[tuple[str, int, Fraction, bool]] = [
        ("channel-blind lift", 0, lambda_for_exponent(0, w_e, w_t), False),
        ("raw local projector weight", 1, lambda_for_exponent(1, w_e, w_t), False),
        ("raw quadratic projector weight", 2, lambda_for_exponent(2, w_e, w_t), False),
        ("single reciprocal local normalization", -1, lambda_for_exponent(-1, w_e, w_t), False),
        ("double reciprocal local normalization", -2, lambda_for_exponent(-2, w_e, w_t), True),
    ]

    print("\nCandidate local-weight laws")
    print("law                                      exponent p   lambda=(w_E/w_T1)^p   hits target")
    print("-" * 98)
    for label, power, value, hits in rows:
        print(f"{label:<42} {power:>6}        {str(value):>8}              {hits}")

    misses = [label for label, _, value, hits in rows if not hits and value != TARGET_LAMBDA]
    hit_rows = [label for label, _, value, hits in rows if hits and value == TARGET_LAMBDA]
    record(
        "all one-factor/raw local projector-weight variants miss lambda=9/4",
        len(misses) == 4 and hit_rows == ["double reciprocal local normalization"],
        "; ".join(f"{label} misses" for label in misses) + "; hit=" + ", ".join(hit_rows),
        status="FALSIFIER",
    )

    q_e, rho_e, center_te = endpoint_chain(TARGET_LAMBDA)
    record(
        "conditional on the double reciprocal local normalization primitive, the endpoint chain closes exactly",
        q_e == TARGET_QE and rho_e == TARGET_RHO_E and center_te == Fraction(-8, 9),
        f"lambda={TARGET_LAMBDA} -> q_E={q_e}, rho_E={rho_e}, center T/E={center_te}",
        status="CONDITIONAL",
    )

    # Minimality over small integer exponents: if the only local datum is the
    # per-arm projector weight and the law is a monomial w^p, p=-2 is the unique
    # small exponent that hits the target.
    hits = [p for p in range(-6, 7) if lambda_for_exponent(p, w_e, w_t) == TARGET_LAMBDA]
    record(
        "within monomial laws q_X proportional to w_X^p for |p|<=6, p=-2 is the unique target exponent",
        hits == [-2],
        f"target exponents in [-6,6]: {hits}",
        status="EXACT",
    )

    # This is the hidden-import firewall: the target is not obtained from
    # O_h equivariance alone, because independent E/T scales can multiply any
    # chosen local-weight law.
    free_scale_examples = {
        "channel_blind": Fraction(1, 1),
        "target": TARGET_LAMBDA,
        "single_reciprocal": lambda_for_exponent(-1, w_e, w_t),
        "raw_quadratic": lambda_for_exponent(2, w_e, w_t),
    }
    record(
        "the double reciprocal law is a primitive candidate, not a consequence of equivariance",
        len(set(free_scale_examples.values())) == len(free_scale_examples),
        "; ".join(f"{k} lambda={v}" for k, v in free_scale_examples.items()),
        status="FIREWALL",
    )

    # Falsify common denominator slips around the exact endpoint denominator 6.
    wrong_denominators: dict[int, tuple[Fraction, Fraction]] = {}
    for denom in (5, 7, 12):
        q_e_wrong = 1 + TARGET_RHO_E / denom
        center_wrong = Fraction(-2, 1) * TARGET_QT / q_e_wrong
        wrong_denominators[denom] = (q_e_wrong, center_wrong)
    wrong_ok = all(q_e != TARGET_QE and c != Fraction(-8, 9) for q_e, c in wrong_denominators.values())
    record(
        "nearby center-excess denominator slips do not close the endpoint chain",
        wrong_ok,
        "; ".join(f"d={d}: q_E={q}, center T/E={c}" for d, (q, c) in wrong_denominators.items()),
        status="FALSIFIER",
    )

    n_pass = sum(check.ok for check in CHECKS)
    n_fail = sum(not check.ok for check in CHECKS)
    print("\nVerdict:")
    print(
        "The exact positive target is now isolated: a double reciprocal local projector-normalization "
        "primitive would give lambda=q_E/q_T=9/4 and hence rho_E=21/4.  The adjacent one-factor, raw, "
        "and quadratic variants miss.  The primitive is not derived here; it is the named remaining "
        "bridge that a future positive proof must justify."
    )
    print(f"\nTOTAL: PASS={n_pass} FAIL={n_fail}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
