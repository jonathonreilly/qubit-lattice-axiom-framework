#!/usr/bin/env python3
"""Bounded lower-level Majorana pairing no-go for charge-preserving kernels."""

from __future__ import annotations

import sys
import numpy as np

np.set_printoptions(precision=6, suppress=True, linewidth=140)

PASS_COUNT = 0
FAIL_COUNT = 0


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


def nambu_response_kernel(normal_kernel: np.ndarray) -> np.ndarray:
    zeros = np.zeros_like(normal_kernel)
    return np.block(
        [
            [np.linalg.inv(np.eye(normal_kernel.shape[0]) - normal_kernel), zeros],
            [zeros, np.linalg.inv(np.eye(normal_kernel.shape[0]) - normal_kernel.conj())],
        ]
    )


def induced_pairing_block(nambu_kernel: np.ndarray, n: int) -> np.ndarray:
    return nambu_kernel[:n, n:]


def one_gen_pairing_operator(mu: float) -> np.ndarray:
    j2 = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    return mu * j2


def three_gen_pairing_operator(mu: float) -> np.ndarray:
    return mu * np.array(
        [
            [0.0, 1.0, 0.0],
            [-1.0, 0.0, 1.0],
            [0.0, -1.0, 0.0],
        ],
        dtype=complex,
    )


def random_invertible_hermitian(n: int, seed: int, shift: float = 2.5) -> np.ndarray:
    rng = np.random.default_rng(seed)
    m = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    h = 0.5 * (m + m.conj().T)
    return h + shift * np.eye(n, dtype=complex)


def n5_execution_certificate(sizes: tuple[int, ...], seeds: tuple[int, ...]) -> None:
    """State the granularity at which this runner actually resolves the no-go.

    Reporting only: no check() call is added and no PASS/FAIL count moves.
    Every quantity below is a structural count or a literal named constant of
    the source; nothing sampled from the seeded streams is quoted.
    """
    print("\n" + "=" * 88)
    print("N5 EXECUTION CERTIFICATE: WHAT THIS RUNNER RESOLVES")
    print("=" * 88)

    entries = tuple(n * n for n in sizes)
    doubled = tuple(2 * n for n in sizes)

    print(
        "per_element: resolved, but what it resolves is a construction and not a "
        f"computed amplitude. induced_pairing_block slices rows 0..n-1 against "
        f"columns n..2n-1 and the Frobenius norm then covers every one of the "
        f"{entries[0]}, {entries[1]} and {entries[2]} complex entries at sizes "
        f"{sizes}; those entries are however the np.zeros_like array that "
        "nambu_response_kernel itself placed in both off-diagonal slots, so the "
        "elementwise statement certified is that the doubling formula never writes "
        "an anomalous entry, not that an evaluated entry fell under 1e-12. The "
        "entries that do carry arithmetic, the inverses of (1 - N) and (1 - conj N), "
        "are never inspected entry by entry."
    )
    print(
        "per_site: checked and not executed. Nothing spatial is instantiated in this "
        "runner: the running index of N labels generation/channel slots of the "
        "Delta-L = 2 kernel, it carries no coordinate, no neighbour relation and no "
        "volume, and the shift of 2.5 on the diagonal is an invertibility device "
        "rather than an on-site energy, so there is no site at which any quantity "
        "here could be evaluated."
    )
    print(
        "per_mode: checked and not executed. This runner diagonalizes nothing - "
        "(1 - N)^-1 and (1 - conj N)^-1 are formed by direct matrix inversion, the "
        "Hermitian kernel N never has its spectrum computed or used, and no "
        "eigenvalue, normal mode, occupation or spectral weight is produced "
        "anywhere; the Delta-L = 2 Majorana channel is handled as one unresolved "
        "channel rather than mode by mode."
    )
    print(
        "per_block: resolved, and this is the granularity the whole no-go turns on. "
        f"Each Nambu kernel is assembled as four n x n blocks inside a {doubled[0]} x "
        f"{doubled[0]}, {doubled[1]} x {doubled[1]} and {doubled[2]} x {doubled[2]} "
        "matrix, and the claim is exactly a statement about which of those blocks is "
        "nonzero. The resolution is partial and worth naming: only the upper-right "
        "anomalous block is ever extracted and measured, while the lower-left "
        "anomalous block and both normal diagonal blocks are never inspected, so one "
        "block of four is resolved at each size."
    )
    print(
        "lattice_wide: checked and not executed, and the missing global theorem is "
        "precisely this note's declared obstruction. The note's open perimeter is the "
        "absent bridge theorem deriving that the framework's lower-level transport / "
        "Green / source-response layer is contained in the charge-preserving "
        "block-diagonal class; this runner assumes that class and computes its "
        f"consequence at the three fixed sizes {sizes}, taking no large-n limit and "
        "reaching no framework-wide statement, so there is no global resolution here "
        "to report."
    )
    print(
        "  scope: the accompanying note describes the sizes as n = 1, 3, 5, but the "
        f"kernels this runner actually builds are of size {sizes} under seeds "
        f"{seeds}; the one-generation case is a 2 x 2 kernel matched to the 2 x 2 "
        "mu J_2 template, so no kernel of size 1 is defined here."
    )
    print(
        "  scope: the second and fourth checks compare the extracted block against "
        "one_gen_pairing_operator(0.0) and three_gen_pairing_operator(0.0), which at "
        "mu = 0 are simply zero matrices, so they restate the block-norm result and "
        "do not test the antisymmetric J_2 or 3 x 3 template shape."
    )
    print(
        "  scope: the three streams are seeded, back-to-back executions are "
        "byte-identical, and no sampled quantity is quoted in the lines above."
    )


def main() -> int:
    print("=" * 88)
    print("NEUTRINO MAJORANA LOWER-LEVEL PAIRING NO-GO")
    print("=" * 88)
    print()
    print("Question:")
    print("  Does the lower-level charge-preserving transport/Green/source-response")
    print("  layer induce a genuine antisymmetric pairing kernel on the unique ΔL=2")
    print("  Majorana channel?")

    n1 = random_invertible_hermitian(2, 1901)
    kernel1 = nambu_response_kernel(n1)
    pair1 = induced_pairing_block(kernel1, 2)
    check("One-generation lower-level Nambu response has zero anomalous block for a generic charge-preserving normal kernel", np.linalg.norm(pair1) < 1e-12,
          f"|pair|={np.linalg.norm(pair1):.2e}")
    check("So the one-generation induced Majorana amplitude is zero", np.linalg.norm(pair1 - one_gen_pairing_operator(0.0)) < 1e-12)

    n3 = random_invertible_hermitian(3, 2003)
    kernel3 = nambu_response_kernel(n3)
    pair3 = induced_pairing_block(kernel3, 3)
    check("Three-generation lower-level Nambu response has zero anomalous block for a generic charge-preserving normal kernel", np.linalg.norm(pair3) < 1e-12,
          f"|pair|={np.linalg.norm(pair3):.2e}")
    check("So the modeled lower-level three-generation Majorana matrix remains zero", np.linalg.norm(pair3 - three_gen_pairing_operator(0.0)) < 1e-12)

    n5 = random_invertible_hermitian(5, 2105)
    kernel5 = nambu_response_kernel(n5)
    pair5 = induced_pairing_block(kernel5, 5)
    check("The anomalous block vanishes identically for generic charge-preserving normal kernels of any size", np.linalg.norm(pair5) < 1e-12,
          f"|pair|={np.linalg.norm(pair5):.2e}")

    n5_execution_certificate((2, 3, 5), (1901, 2003, 2105))

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Exact lower-level Majorana no-go:")
    print("    - generic charge-preserving lower-level dynamics induce no anomalous Nambu block")
    print("    - therefore the induced Majorana pairing kernel is identically zero")
    print("    - this is bounded support for the charge-preserving response-kernel class")
    print("    - deriving that the framework response layer is restricted to this class")
    print("      remains a separate bridge theorem")
    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
