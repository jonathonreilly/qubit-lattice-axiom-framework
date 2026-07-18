#!/usr/bin/env python3
"""Finite controls for qualitative substrate language versus exact law value.

This runner proves only the displayed finite separations.  It does not select a
law for the framework, amend an axiom, or claim that every possible uniqueness
principle is convex-closed.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from itertools import product

import numpy as np


PASS = 0
FAIL = 0


def check(condition: bool, label: str) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}")
    else:
        FAIL += 1
        print(f"FAIL {label}")


def close(a: complex | float, b: complex | float, tol: float = 1.0e-11) -> bool:
    return bool(abs(a - b) <= tol)


def bit_kernel(lam: float, n0: int, n1: int) -> tuple[float, float]:
    """Label-covariant nearest-neighbour count kernel."""
    w0 = lam**n0
    w1 = lam**n1
    z = w0 + w1
    return w0 / z, w1 / z


def stochastic_family_controls() -> None:
    # The same local, positive, normalized, label-covariant architecture has a
    # continuous parameter.  Swapping labels swaps both counts and outputs.
    for lam in (1.0, 1.25, 2.0, 3.0):
        for n0 in range(7):
            for n1 in range(7 - n0):
                p0, p1 = bit_kernel(lam, n0, n1)
                q0, q1 = bit_kernel(lam, n1, n0)
                check(p0 > 0.0 and p1 > 0.0, f"positive kernel lambda={lam} ({n0},{n1})")
                check(close(p0 + p1, 1.0), f"normalized kernel lambda={lam} ({n0},{n1})")
                check(close(p0, q1) and close(p1, q0), f"label covariance lambda={lam} ({n0},{n1})")

    p_fair = bit_kernel(1.0, 2, 1)[0]
    p_biased = bit_kernel(2.0, 2, 1)[0]
    check(close(p_fair, 0.5), "fair structural representative predicts 1/2")
    check(close(p_biased, 2.0 / 3.0), "biased structural representative predicts 2/3")
    check(not close(p_fair, p_biased), "structural predicates do not identify kernel value")

    # Convex closure: the standard qualitative constraints survive mixing,
    # while the operational probability varies affinely.
    for alpha in (0.0, 0.2, 0.5, 0.8, 1.0):
        mixed = alpha * p_fair + (1.0 - alpha) * p_biased
        check(0.0 < mixed < 1.0, f"convex mixture stays full-support alpha={alpha}")
        check(
            close(mixed, alpha * 0.5 + (1.0 - alpha) * (2.0 / 3.0)),
            f"observable varies affinely alpha={alpha}",
        )


def swap_matrix() -> np.ndarray:
    s = np.zeros((4, 4), dtype=complex)
    # Basis |00>, |01>, |10>, |11>.
    for a in (0, 1):
        for b in (0, 1):
            source = 2 * a + b
            target = 2 * b + a
            s[target, source] = 1.0
    return s


def partial_swap(theta: float) -> np.ndarray:
    s = swap_matrix()
    return math.cos(theta) * np.eye(4, dtype=complex) + 1j * math.sin(theta) * s


def su2_samples() -> list[np.ndarray]:
    i2 = np.eye(2, dtype=complex)
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    z = np.array([[1, 0], [0, -1]], dtype=complex)
    samples = [i2]
    for axis, angle in ((x, 0.37), (y, -0.91), (z, 1.23)):
        samples.append(math.cos(angle / 2) * i2 - 1j * math.sin(angle / 2) * axis)
    return samples


def unitary_family_controls() -> None:
    s = swap_matrix()
    i4 = np.eye(4, dtype=complex)
    ket01 = np.array([0.0, 1.0, 0.0, 0.0], dtype=complex)

    probabilities: list[float] = []
    for theta in (math.pi / 12, math.pi / 6, math.pi / 4, math.pi / 3):
        u = partial_swap(theta)
        check(np.allclose(u.conj().T @ u, i4), f"partial swap unitary theta={theta:.8f}")
        check(np.allclose(u @ s, s @ u), f"exchange covariance theta={theta:.8f}")
        for index, v in enumerate(su2_samples()):
            vv = np.kron(v, v)
            check(np.allclose(u @ vv, vv @ u), f"basis neutrality theta={theta:.8f} sample={index}")

        out = u @ ket01
        # Probability that the first qubit is 1: basis state |10>.
        p_first_one = float(abs(out[2]) ** 2)
        probabilities.append(p_first_one)
        check(close(p_first_one, math.sin(theta) ** 2), f"partial-swap prediction theta={theta:.8f}")

    check(len({round(p, 12) for p in probabilities}) == len(probabilities), "unitarity and covariance leave a continuous physical angle")


def n_qubit_swap(n: int, left: int, right: int) -> np.ndarray:
    dimension = 2**n
    result = np.zeros((dimension, dimension), dtype=complex)
    for bits in product((0, 1), repeat=n):
        source = sum(bit << (n - 1 - index) for index, bit in enumerate(bits))
        target_bits = list(bits)
        target_bits[left], target_bits[right] = target_bits[right], target_bits[left]
        target = sum(bit << (n - 1 - index) for index, bit in enumerate(target_bits))
        result[target, source] = 1.0
    return result


def dimensionless_ratio_control() -> None:
    # A single partial-swap angle could be challenged as a choice of clock
    # normalization.  On a centre plus two equivalent neighbours there are two
    # independent symmetric invariant operators.  Their relative coefficient
    # changes a scale-free spectral gap ratio.
    s01 = n_qubit_swap(3, 0, 1)
    s02 = n_qubit_swap(3, 0, 2)
    s12 = n_qubit_swap(3, 1, 2)
    h1 = s01 + s02
    h2 = s01 @ s02 + s02 @ s01
    samples = su2_samples()

    gap_ratios: list[float] = []
    for eta in (0.0, 1.0 / 3.0):
        h = h1 + eta * h2
        check(np.allclose(h, h.conj().T), f"three-qubit local generator Hermitian eta={eta}")
        check(np.allclose(h @ s12, s12 @ h), f"equivalent-neighbour covariance eta={eta}")
        for index, v in enumerate(samples):
            vvv = np.kron(np.kron(v, v), v)
            check(np.allclose(h @ vvv, vvv @ h), f"three-qubit basis neutrality eta={eta} sample={index}")

        levels = []
        for value in np.linalg.eigvalsh(h):
            if not levels or abs(value - levels[-1]) > 1.0e-9:
                levels.append(float(value))
        check(len(levels) == 3, f"three invariant spectral levels eta={eta}")
        gaps = (levels[1] - levels[0], levels[2] - levels[1])
        gap_ratios.append(gaps[0] / gaps[1])
        check(all(gap > 0 for gap in gaps), f"positive ordered gaps eta={eta}")

    check(close(gap_ratios[0], 2.0), "eta zero has scale-free gap ratio two")
    check(close(gap_ratios[1], 1.0), "eta one-third has scale-free gap ratio one")
    check(not close(gap_ratios[0], gap_ratios[1]), "clock rescaling and energy shift cannot remove interaction ratio")


@dataclass(frozen=True)
class DeterministicHistoryLaw:
    flip: bool

    def step(self, bit: int) -> int:
        return 1 - bit if self.flip else bit


def actuality_is_not_universally_separate() -> None:
    # A deterministic exact law gives one successor without a sampling atom.
    identity = DeterministicHistoryLaw(flip=False)
    toggle = DeterministicHistoryLaw(flip=True)
    for initial in (0, 1):
        check(identity.step(initial) == initial, f"deterministic identity unique successor initial={initial}")
        check(toggle.step(initial) == 1 - initial, f"deterministic toggle unique successor initial={initial}")
    check(identity.step(0) != toggle.step(0), "determinism removes sampling but not exact-law identity")


def main() -> int:
    stochastic_family_controls()
    unitary_family_controls()
    dimensionless_ratio_control()
    actuality_is_not_universally_separate()
    print(f"RESULT PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
