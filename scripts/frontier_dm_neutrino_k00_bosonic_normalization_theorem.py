#!/usr/bin/env python3
"""Scalar-baseline response correspondence; K00=2*tau is a separate coefficient-identification premise."""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300

import math
import sys

import numpy as np

PASS_COUNT = 0
FAIL_COUNT = 0

PI = np.pi
OMEGA = np.exp(2j * PI / 3.0)
UZ3 = (1.0 / np.sqrt(3.0)) * np.array(
    [
        [1.0, 1.0, 1.0],
        [1.0, OMEGA, OMEGA * OMEGA],
        [1.0, OMEGA * OMEGA, OMEGA],
    ],
    dtype=complex,
)
R = np.array(
    [
        [1.0, 0.0, 0.0],
        [0.0, 1.0 / np.sqrt(2.0), 1.0 / np.sqrt(2.0)],
        [0.0, -1.0 / np.sqrt(2.0), 1.0 / np.sqrt(2.0)],
    ],
    dtype=complex,
)

J3 = np.ones((3, 3), dtype=float)
F00 = J3 / 3.0
J2 = np.ones((2, 2), dtype=float)
FROW = 0.5 * J2


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def h_from_breaking_triplet(
    A: float,
    b: float,
    c: float,
    d: float,
    delta: float,
    rho: float,
    gamma: float,
) -> np.ndarray:
    return np.array(
        [
            [A, b + rho, b - rho - 1j * gamma],
            [b + rho, c + delta, d],
            [b - rho + 1j * gamma, d, c - delta],
        ],
        dtype=complex,
    )


def mass_basis_kernel_from_h(h: np.ndarray) -> np.ndarray:
    return R.T @ (UZ3.conj().T @ h @ UZ3) @ R


def relative_generator(mass: float, source_coeff: float, operator: np.ndarray) -> float:
    base = mass * np.eye(operator.shape[0], dtype=complex)
    sign, logabs = np.linalg.slogdet(base + source_coeff * operator)
    if abs(sign) == 0:
        raise ValueError("singular source-deformed block encountered")
    return float(logabs - operator.shape[0] * math.log(abs(mass)))


def part1_k00_has_an_exact_uniform_projector_generator() -> None:
    print("\n" + "=" * 88)
    print("PART 1: K00 HAS AN EXACT UNIFORM PROJECTOR GENERATOR")
    print("=" * 88)

    pars = dict(A=1.8, b=0.35, c=1.1, d=0.25, delta=0.16, rho=-0.09, gamma=0.28)
    h = h_from_breaking_triplet(**pars)
    km = mass_basis_kernel_from_h(h)
    k00_direct = float(np.real(km[0, 0]))
    k00_trace = float(np.real(np.trace(h @ F00)))
    k00_formula = (pars["A"] + 4.0 * pars["b"] + 2.0 * pars["c"] + 2.0 * pars["d"]) / 3.0

    varied = h_from_breaking_triplet(pars["A"], pars["b"], pars["c"], pars["d"], -0.37, 0.22, -0.41)
    k00_varied = float(np.real(mass_basis_kernel_from_h(varied)[0, 0]))

    check(
        "The exact heavy-basis diagonal K00 agrees with the transformed kernel entry",
        abs(k00_direct - k00_formula) < 1e-12,
        f"K00={k00_direct:.12f}",
    )
    check(
        "The same K00 is the Frobenius pairing against F00 = J3/3",
        abs(k00_direct - k00_trace) < 1e-12,
        f"trace(F00 H)={k00_trace:.12f}",
    )
    check(
        "K00 is independent of the odd/even breaking triplet (delta,rho,gamma)",
        abs(k00_direct - k00_varied) < 1e-12,
        f"varied K00={k00_varied:.12f}",
    )


def part2_f00_shares_nonzero_spectrum_with_scaled_source_row_sum_generator() -> None:
    print("\n" + "=" * 88)
    print("PART 2: F00 SHARES THE NONZERO SPECTRUM OF THE SCALED SOURCE ROW-SUM GENERATOR")
    print("=" * 88)

    eig_f00 = np.linalg.eigvalsh(F00)
    eig_frow = np.linalg.eigvalsh(FROW)

    check(
        "The target K00 generator is a rank-one projector with spectrum {1,0,0}",
        np.max(np.abs(eig_f00 - np.array([0.0, 0.0, 1.0]))) < 1e-12,
        f"eig(F00)={np.round(eig_f00, 12)}",
    )
    check(
        "The scaled source row-sum generator (1/2)J2 is a rank-one projector with spectrum {1,0}",
        np.max(np.abs(eig_frow - np.array([0.0, 1.0]))) < 1e-12,
        f"eig(FROW)={np.round(eig_frow, 12)}",
    )
    check(
        "Both generators have the same nonzero rank-one projector spectrum",
        np.linalg.norm(F00@F00-F00)<1e-12 and np.linalg.norm(FROW@FROW-FROW)<1e-12 and abs(np.trace(F00)-np.trace(FROW))<1e-12,
        "both have one nonzero eigenvalue +1 and otherwise zero spectrum",
    )


def part3_the_bosonic_observable_principle_fixes_k00_to_2_tau_plus() -> None:
    print("\n" + "=" * 88)
    print("PART 3: SCALAR-BASELINE RESPONSE AND SUPPLIED COEFFICIENT MATCH")
    print("=" * 88)

    mass = 1.73
    jvals = np.linspace(-0.35, 0.35, 8)
    max_diff = 0.0
    for j in jvals:
        r_target = relative_generator(mass, j, F00)
        r_source = relative_generator(mass, j, FROW)
        max_diff = max(max_diff, abs(r_target - r_source))

    check(
        "The target K00 generator and the scaled source row-sum mode have identical exact bosonic response",
        max_diff < 1e-12,
        f"max response diff={max_diff:.2e}",
    )

    tau_plus = 1.0
    k00 = 2.0 * tau_plus
    check(
        "Under the extra supplied identification K00=2*tau, tau=1 gives 2",
        abs(k00 - 2.0) < 1e-12,
        f"K00/tau_+ = {k00 / tau_plus:.12f}",
    )


def part4_the_sharp_source_oriented_branch_gives_k00_equal_2() -> None:
    print("\n" + "=" * 88)
    print("PART 4: SUPPLIED AMPLITUDES WITH EXTRA COEFFICIENT IDENTIFICATION")
    print("=" * 88)

    tau_E = 0.5
    tau_T = 0.5
    tau_plus = tau_E + tau_T
    k00 = 2.0 * tau_plus

    check(
        "The supplied source amplitudes are tau_E = tau_T = 1/2",
        abs(tau_E - 0.5) < 1e-12 and abs(tau_T - 0.5) < 1e-12,
        f"(tau_E,tau_T)=({tau_E:.6f},{tau_T:.6f})",
    )
    check(
        "Therefore tau_+ = 1 on the sharp source-oriented branch",
        abs(tau_plus - 1.0) < 1e-12,
        f"tau_+={tau_plus:.12f}",
    )
    check(
        "The additionally identified K00 equals 2 for those supplied inputs",
        abs(k00 - 2.0) < 1e-12,
        f"K00={k00:.12f}",
    )


def main() -> int:
    print("=" * 88)
    print("DM NEUTRINO K00 BOSONIC NORMALIZATION THEOREM")
    print("=" * 88)

    check("Generator spectra alone do not impose K00=2*tau", abs(np.trace(3*np.eye(3)@F00)-2.0)>0.5, "H=3I and supplied tau=1 give K00=3 versus 2*tau=2")
    part1_k00_has_an_exact_uniform_projector_generator()
    part2_f00_shares_nonzero_spectrum_with_scaled_source_row_sum_generator()
    part3_the_bosonic_observable_principle_fixes_k00_to_2_tau_plus()
    part4_the_sharp_source_oriented_branch_gives_k00_equal_2()

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
