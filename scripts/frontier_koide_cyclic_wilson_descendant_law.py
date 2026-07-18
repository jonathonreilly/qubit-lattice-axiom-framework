#!/usr/bin/env python3
"""Verify an abstract cyclic-compression three-coordinate reconstruction lemma.

The historical runner path is retained for graph stability. This runner proves
only finite linear algebra for a supplied ``H in Herm(3)``. It does not derive
a microscopic Wilson first variation, an action map, a physical carrier, a
mass spectrum, a scale/readout map, or a selector mechanism.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import sympy as sp


PASS_COUNT = 0
FAIL_COUNT = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "KOIDE_CYCLIC_WILSON_DESCENDANT_LAW_NOTE_2026-04-18.md"


def check(name: str, condition: bool, detail: str = "", kind: str = "EXACT") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    tag = f" [{kind}]" if kind != "EXACT" else ""
    message = f"  [{status} (A)]{tag} {name}"
    if detail:
        message += f"  ({detail})"
    print(message)
    return condition


def scope_firewall_violations(note_text: str, source_text: str) -> list[str]:
    """Return missing scope markers or reintroduced load-bearing overclaims."""
    required_note = (
        "# Abstract Cyclic-Compression Three-Coordinate Reconstruction Lemma",
        "**Type:** positive_theorem",
        "**Status:** proposed_retained",
        "supplied Hermitian matrix",
        "Riesz/trace coordinates",
        "No microscopic source or action map is derived.",
        "No physical carrier identification is derived.",
        "No scale or readout map is derived.",
        "No selector mechanism is derived.",
        "KOIDE_DWEH_CYCLIC_COMPRESSION_NOTE_2026-04-18.md",
    )
    forbidden_prose = (
        "The la" + "w is now ex" + "plicit.",
        "actual cyclic " + "Wilson descendant law",
        "Given any local " + "Wilson first-variation law",
        "Observed charged-" + "lepton witness",
        "matches the actual " + "charged-lepton target",
        "r0 = dW_" + "W(B0)",
    )
    forbidden_source = forbidden_prose + (
        "cls=" + '"D"',
        "PD" + "G",
        "fourier_" + "matrix",
        "part5_" + "observed",
        "masses = " + "np.array",
    )
    violations = [f"missing note marker: {item}" for item in required_note if item not in note_text]
    violations.extend(
        f"forbidden note claim: {item}" for item in forbidden_prose if item in note_text
    )
    violations.extend(
        f"forbidden runner claim: {item}" for item in forbidden_source if item in source_text
    )
    return violations


def matrix_unit(i: int, j: int) -> np.ndarray:
    out = np.zeros((3, 3), dtype=complex)
    out[i - 1, j - 1] = 1.0
    return out


def chain_data() -> dict[str, np.ndarray]:
    data = {f"E{i}{j}": matrix_unit(i, j) for i in range(1, 4) for j in range(1, 4)}
    for i, j in ((1, 2), (1, 3), (2, 3)):
        data[f"X{i}{j}"] = data[f"E{i}{j}"] + data[f"E{j}{i}"]
        data[f"Y{i}{j}"] = 1j * (data[f"E{j}{i}"] - data[f"E{i}{j}"])
    return data


def real_trace_pair(left: np.ndarray, right: np.ndarray) -> float:
    return float(np.trace(left @ right).real)


def cycle_matrix() -> np.ndarray:
    return np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)


def cyclic_basis() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    c = cycle_matrix()
    c2 = c @ c
    return np.eye(3, dtype=complex), c + c2, 1j * (c - c2)


def cyclic_projector(matrix: np.ndarray) -> np.ndarray:
    c = cycle_matrix()
    c2 = c @ c
    return (matrix + c @ matrix @ c2 + c2 @ matrix @ c) / 3.0


def cyclic_responses(matrix: np.ndarray) -> tuple[float, float, float]:
    return tuple(real_trace_pair(basis, matrix) for basis in cyclic_basis())


def reconstruct(responses: tuple[float, float, float]) -> np.ndarray:
    r0, r1, r2 = responses
    b0, b1, b2 = cyclic_basis()
    return (r0 / 3.0) * b0 + (r1 / 6.0) * b1 + (r2 / 6.0) * b2


def hermitian_basis() -> tuple[np.ndarray, ...]:
    data = chain_data()
    return (
        data["E11"],
        data["E22"],
        data["E33"],
        data["X12"],
        data["X13"],
        data["X23"],
        data["Y12"],
        data["Y13"],
        data["Y23"],
    )


def part0_scope_firewall() -> None:
    print("=" * 88)
    print("PART 0: source scope is the abstract supplied-matrix lemma")
    print("=" * 88)
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    source_text = Path(__file__).read_text(encoding="utf-8")
    violations = scope_firewall_violations(note_text, source_text)
    check(
        "The note and runner retain the required theorem boundary and reject prior overclaims",
        not violations,
        detail="; ".join(violations) if violations else "scope firewall clean",
    )


def part1_chain_algebra_contains_basis() -> None:
    print()
    print("=" * 88)
    print("PART 1: the adjacent-chain path algebra contains the signed cyclic basis")
    print("=" * 88)
    data = chain_data()
    c = cycle_matrix()
    c2 = c @ c
    b0, b1, b2 = cyclic_basis()
    forward = data["E21"] + data["E32"] + data["E13"]
    backward = data["E12"] + data["E23"] + data["E31"]

    check(
        "E12 E23 equals the long corner E13",
        np.array_equal(data["E12"] @ data["E23"], data["E13"]),
    )
    check(
        "E32 E21 equals the long corner E31",
        np.array_equal(data["E32"] @ data["E21"], data["E31"]),
    )
    check(
        "The fixed forward-cycle convention is C = E21 + E32 + E13",
        np.array_equal(forward, c),
    )
    check(
        "The backward cycle is C^2 = E12 + E23 + E31",
        np.array_equal(backward, c2),
    )
    check(
        "C has order three and C^2 = C^dagger",
        np.array_equal(c @ c2, b0) and np.array_equal(c2, c.conj().T),
    )
    check(
        "B1 = C + C^2 is in the adjacent-chain algebra",
        np.array_equal(forward + backward, b1),
    )
    check(
        "The B2 sign is i(C-C^2) = Y12 + Y23 - Y13",
        np.array_equal(data["Y12"] + data["Y23"] - data["Y13"], b2),
    )


def part2_projector_and_image() -> None:
    print()
    print("=" * 88)
    print("PART 2: cyclic averaging is the exact rank-three Hermitian projector")
    print("=" * 88)
    c = cycle_matrix()
    b0, b1, b2 = cyclic_basis()
    h_basis = hermitian_basis()
    projections = [cyclic_projector(item) for item in h_basis]

    check(
        "The projector fixes B0, B1, and B2",
        all(np.array_equal(cyclic_projector(item), item) for item in (b0, b1, b2)),
    )
    check(
        "The projector is idempotent on a real basis of Herm(3)",
        all(np.allclose(cyclic_projector(item), item) for item in projections),
    )
    check(
        "Every projected basis element is Hermitian",
        all(np.allclose(item, item.conj().T) for item in projections),
    )
    check(
        "Every projected basis element commutes with C",
        all(np.allclose(item @ c, c @ item) for item in projections),
    )

    real_columns = [np.concatenate((item.real.ravel(), item.imag.ravel())) for item in projections]
    image_rank = int(np.linalg.matrix_rank(np.column_stack(real_columns), tol=1e-12))
    check(
        "The real Hermitian image has rank exactly three",
        image_rank == 3,
        detail=f"rank={image_rank}",
    )

    gram = np.array(
        [
            [real_trace_pair(left, right) for right in (b0, b1, b2)]
            for left in (b0, b1, b2)
        ]
    )
    check(
        "The real trace Gram matrix is exactly diag(3,6,6)",
        np.array_equal(gram, np.diag([3.0, 6.0, 6.0])),
        detail=f"gram={gram.tolist()}",
    )
    check(
        "All nine projected basis elements obey the trace-coordinate reconstruction",
        all(
            np.allclose(reconstruct(cyclic_responses(item)), projected)
            for item, projected in zip(h_basis, projections)
        ),
    )


def part3_exact_supplied_matrix_reconstruction() -> None:
    print()
    print("=" * 88)
    print("PART 3: three trace coordinates reconstruct the projection of a supplied H")
    print("=" * 88)
    d0, d1, d2, x01, x02, x12, y01, y02, y12 = sp.symbols(
        "d0 d1 d2 x01 x02 x12 y01 y02 y12", real=True
    )
    h = sp.Matrix(
        [
            [d0, x01 - sp.I * y01, x02 - sp.I * y02],
            [x01 + sp.I * y01, d1, x12 - sp.I * y12],
            [x02 + sp.I * y02, x12 + sp.I * y12, d2],
        ]
    )
    c = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    c2 = c**2
    b0, b1, b2 = sp.eye(3), c + c2, sp.I * (c - c2)
    projected = sp.simplify((h + c * h * c2 + c2 * h * c) / 3)
    responses = tuple(sp.simplify(sp.trace(basis * h)) for basis in (b0, b1, b2))
    reconstructed = sp.simplify(
        (responses[0] / 3) * b0
        + (responses[1] / 6) * b1
        + (responses[2] / 6) * b2
    )
    expected_responses = (
        d0 + d1 + d2,
        2 * (x01 + x02 + x12),
        2 * (y01 - y02 + y12),
    )

    check(
        "The generic supplied Hermitian matrix reconstructs symbolically",
        sp.simplify(projected - reconstructed) == sp.zeros(3),
    )
    check(
        "The three symbolic trace coordinates are real polynomials",
        all(sp.simplify(sp.im(item)) == 0 for item in responses),
    )
    check(
        "The signed symbolic coordinates have the fixed normalization",
        all(
            sp.simplify(actual - expected) == 0
            for actual, expected in zip(responses, expected_responses)
        ),
        detail="r0=sum(diagonal), r1=2 sum(xij), r2=2(y01-y02+y12)",
    )


def part4_koide_coordinate_equivalence() -> None:
    print()
    print("=" * 88)
    print("PART 4: the supplied-matrix Koide cone has the exact response equation")
    print("=" * 88)
    r0, r1, r2 = sp.symbols("r0 r1 r2", real=True)
    cone_residual = (r0 / 3) ** 2 - 2 * ((r1 / 6) ** 2 + (r2 / 6) ** 2)
    response_residual = (2 * r0**2 - r1**2 - r2**2) / 18
    check(
        "a^2-2(x^2+y^2) equals (2r0^2-r1^2-r2^2)/18",
        sp.simplify(cone_residual - response_residual) == 0,
    )
    check(
        "The response-space equation has the required factor two",
        sp.simplify(cone_residual - (r0**2 - r1**2 - r2**2) / 18) != 0,
    )


def main() -> int:
    part0_scope_firewall()
    part1_chain_algebra_contains_basis()
    part2_projector_and_image()
    part3_exact_supplied_matrix_reconstruction()
    part4_koide_coordinate_equivalence()

    print()
    print("Interpretation:")
    print("  The exact result is an abstract rank-three cyclic compression of a supplied")
    print("  Hermitian matrix, reconstructed from its real trace coordinates on B0, B1,")
    print("  and B2. The Koide cone is equivalent to 2 r0^2 = r1^2 + r2^2.")
    print("  No microscopic source/action map, physical carrier or spectrum, scale/readout")
    print("  map, or selector mechanism is derived by these identities.")
    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
