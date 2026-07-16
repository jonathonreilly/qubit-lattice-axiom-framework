#!/usr/bin/env python3
"""Conditional Clifford/CAR algebraic-equivalence verifier.

Authority note:
    docs/AREA_LAW_NATIVE_CAR_SEMANTICS_TIGHTENING_NOTE_2026-04-25.md

The stable historical path is preserved, but this runner verifies only the
conditional finite-algebra equivalence. It also executes hostile controls
showing that rank four is not a CAR selector, that the specified exterior
one-form spatial action has no equivariant spinor intertwiner, and that the
natural full-cell odd Clifford action does not reduce to the
Hamming-weight-one block.

Exit code: 0 on full PASS, 1 on any FAIL.
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/AREA_LAW_NATIVE_CAR_SEMANTICS_TIGHTENING_NOTE_2026-04-25.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, passed: bool, detail: str) -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if passed else "FAIL"
    if passed:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"[{status}] {name}: {detail}")
    return passed


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
SIGMA_MINUS = np.array([[0, 1], [0, 0]], dtype=complex)


def kron(*ops: np.ndarray) -> np.ndarray:
    out = ops[0]
    for op in ops[1:]:
        out = np.kron(out, op)
    return out


def jw_annihilator(mode: int, modes: int) -> np.ndarray:
    return kron(*([Z] * mode + [SIGMA_MINUS] + [I2] * (modes - mode - 1)))


def anticommutator(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b + b @ a


def commutator(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def algebra_words(generators: list[np.ndarray]) -> list[np.ndarray]:
    ident = np.eye(generators[0].shape[0], dtype=complex)
    words = [ident]
    for degree in range(1, len(generators) + 1):
        for indices in itertools.combinations(range(len(generators)), degree):
            word = ident.copy()
            for idx in indices:
                word = word @ generators[idx]
            words.append(word)
    return words


def complex_span_rank(matrices: list[np.ndarray], tol: float = 1.0e-10) -> int:
    columns = np.column_stack([matrix.reshape(-1) for matrix in matrices])
    return int(np.linalg.matrix_rank(columns, tol=tol))


def deterministic_unitary(dim: int) -> np.ndarray:
    rng = np.random.default_rng(5428)
    raw = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
    q, r = np.linalg.qr(raw)
    phases = np.diag(r)
    return q @ np.diag(np.conj(phases / np.abs(phases)))


def intertwiner_operator(
    source: list[np.ndarray], target: list[np.ndarray]
) -> np.ndarray:
    dim = source[0].shape[0]
    ident = np.eye(dim, dtype=complex)
    return np.vstack(
        [
            np.kron(source_matrix.T, ident) - np.kron(ident, target_matrix)
            for source_matrix, target_matrix in zip(source, target)
        ]
    )


def main() -> int:
    print("=" * 78)
    print("AREA-LAW CONDITIONAL CLIFFORD-CAR ALGEBRAIC EQUIVALENCE")
    print("=" * 78)
    print()
    print("Question: what follows after an irreducible Cl_4(C) or two-mode")
    print("CAR response is supplied on C^4, and what does not follow from")
    print("rank four or the specified exterior one-form action?")
    print()

    active_dim = 4
    check(
        "conditional active representation has dimension four",
        active_dim == 4,
        "dim_C K=4",
    )
    check(
        "two complex CAR modes have Fock dimension four",
        2**2 == active_dim,
        "dim F(C^2)=4",
    )

    c0 = jw_annihilator(0, 2)
    c1 = jw_annihilator(1, 2)
    annihilators = [c0, c1]
    creators = [c.conj().T for c in annihilators]
    ident = np.eye(active_dim, dtype=complex)

    max_cc = 0.0
    max_cct = 0.0
    for i, ci in enumerate(annihilators):
        for j, cj in enumerate(annihilators):
            max_cc = max(max_cc, np.linalg.norm(anticommutator(ci, cj)))
            expected = ident if i == j else np.zeros_like(ident)
            max_cct = max(
                max_cct,
                np.linalg.norm(anticommutator(ci, creators[j]) - expected),
            )
    check(
        "supplied annihilators obey {c_i,c_j}=0",
        max_cc < 1.0e-12,
        f"max error={max_cc:.2e}",
    )
    check(
        "supplied annihilators obey {c_i,c_j^dagger}=delta_ij",
        max_cct < 1.0e-12,
        f"max error={max_cct:.2e}",
    )

    gammas = [
        c0 + c0.conj().T,
        -1j * (c0 - c0.conj().T),
        c1 + c1.conj().T,
        -1j * (c1 - c1.conj().T),
    ]
    max_hermitian = max(np.linalg.norm(g - g.conj().T) for g in gammas)
    max_clifford = 0.0
    for i, gi in enumerate(gammas):
        for j, gj in enumerate(gammas):
            expected = (2.0 if i == j else 0.0) * ident
            max_clifford = max(
                max_clifford,
                np.linalg.norm(anticommutator(gi, gj) - expected),
            )
    check(
        "CAR modes define four Hermitian Majoranas",
        max_hermitian < 1.0e-12,
        f"max Hermitian error={max_hermitian:.2e}",
    )
    check(
        "Majoranas obey the Cl_4(C) relations",
        max_clifford < 1.0e-12,
        f"max Clifford error={max_clifford:.2e}",
    )
    word_rank = complex_span_rank(algebra_words(gammas))
    check(
        "Majorana words generate M_4(C)",
        word_rank == 16,
        f"complex span rank={word_rank}",
    )
    recovered = [
        0.5 * (gammas[0] + 1j * gammas[1]),
        0.5 * (gammas[2] + 1j * gammas[3]),
    ]
    recovery_error = max(
        np.linalg.norm(recovered[i] - annihilators[i]) for i in range(2)
    )
    check(
        "paired Majoranas recover the supplied CAR annihilators",
        recovery_error < 1.0e-12,
        f"max recovery error={recovery_error:.2e}",
    )

    change_of_basis = deterministic_unitary(active_dim)
    rotated_gammas = [
        change_of_basis.conj().T @ gamma @ change_of_basis for gamma in gammas
    ]
    pauli_operator = intertwiner_operator(rotated_gammas, gammas)
    _, singular_values, vh = np.linalg.svd(pauli_operator)
    pauli_nullity = int(np.count_nonzero(singular_values < 1.0e-10))
    raw_intertwiner = vh.conj().T[:, -1].reshape(
        (active_dim, active_dim), order="F"
    )
    normalization = np.sqrt(
        np.trace(raw_intertwiner.conj().T @ raw_intertwiner).real / active_dim
    )
    unitary_intertwiner = raw_intertwiner / normalization
    unitary_error = np.linalg.norm(
        unitary_intertwiner.conj().T @ unitary_intertwiner - ident
    )
    intertwining_error = max(
        np.linalg.norm(
            unitary_intertwiner @ source - target @ unitary_intertwiner
        )
        for source, target in zip(rotated_gammas, gammas)
    )
    check(
        "an arbitrary irreducible Cl_4 presentation has one intertwiner line",
        pauli_nullity == 1,
        f"nullity={pauli_nullity}",
    )
    check(
        "the normalized Pauli intertwiner is unitary",
        unitary_error < 1.0e-11,
        f"unitary error={unitary_error:.2e}",
    )
    check(
        "the unitary intertwiner identifies the noncanonical representation",
        intertwining_error < 1.0e-11,
        f"max intertwining error={intertwining_error:.2e}",
    )

    n0 = c0.conj().T @ c0
    n1 = c1.conj().T @ c1
    parity = (ident - 2.0 * n0) @ (ident - 2.0 * n1)
    parity_eigs = sorted(round(float(x.real)) for x in np.linalg.eigvals(parity))
    parity_square_error = np.linalg.norm(parity @ parity - ident)
    parity_odd_error = max(
        np.linalg.norm(anticommutator(parity, gamma)) for gamma in gammas
    )
    bilinears = [
        1j * gammas[i] @ gammas[j]
        for i in range(4)
        for j in range(i + 1, 4)
    ]
    parity_even_error = max(
        np.linalg.norm(commutator(parity, bilinear)) for bilinear in bilinears
    )
    check(
        "conditional fermion parity squares to identity",
        parity_square_error < 1.0e-12,
        f"error={parity_square_error:.2e}",
    )
    check(
        "conditional fermion parity has a 2+2 split",
        parity_eigs == [-1, -1, 1, 1],
        f"eigenvalues={parity_eigs}",
    )
    check(
        "Majoranas are odd under the conditional parity",
        parity_odd_error < 1.0e-12,
        f"max anticommutator={parity_odd_error:.2e}",
    )
    check(
        "Majorana bilinears are even under the conditional parity",
        parity_even_error < 1.0e-12,
        f"max commutator={parity_even_error:.2e}",
    )

    spin_a = kron(X, I2)
    spin_b = kron(I2, X)
    spin_commutator = np.linalg.norm(commutator(spin_a, spin_b))
    spin_anticommutator = np.linalg.norm(anticommutator(spin_a, spin_b))
    check(
        "the same C^4 supports commuting two-qubit factors",
        spin_commutator < 1.0e-12,
        f"commutator norm={spin_commutator:.2e}",
    )
    check(
        "commuting two-qubit factors are not CAR generators",
        spin_anticommutator > 1.0,
        f"anticommutator norm={spin_anticommutator:.2e}",
    )
    check(
        "rank four is not a CAR selector",
        spin_commutator < 1.0e-12 and spin_anticommutator > 1.0,
        "CAR and non-CAR operator semantics coexist on C^4",
    )

    inv_sqrt_two = 1.0 / np.sqrt(2.0)
    spin_one = [
        np.array(
            [
                [0.0, inv_sqrt_two, 0.0],
                [inv_sqrt_two, 0.0, inv_sqrt_two],
                [0.0, inv_sqrt_two, 0.0],
            ],
            dtype=complex,
        ),
        np.array(
            [
                [0.0, -1j * inv_sqrt_two, 0.0],
                [1j * inv_sqrt_two, 0.0, -1j * inv_sqrt_two],
                [0.0, 1j * inv_sqrt_two, 0.0],
            ],
            dtype=complex,
        ),
        np.diag([1.0, 0.0, -1.0]).astype(complex),
    ]
    substrate_generators = []
    for generator in spin_one:
        lifted = np.zeros((4, 4), dtype=complex)
        lifted[1:, 1:] = generator
        substrate_generators.append(lifted)
    spinor_generators = [np.kron(I2, sigma / 2.0) for sigma in (X, Y, Z)]
    substrate_casimir = sum(
        generator @ generator for generator in substrate_generators
    )
    spinor_casimir = sum(generator @ generator for generator in spinor_generators)
    substrate_spectrum = np.sort(np.linalg.eigvalsh(substrate_casimir).real)
    spinor_spectrum = np.sort(np.linalg.eigvalsh(spinor_casimir).real)
    equivariance_operator = np.vstack(
        [
            np.kron(np.eye(4), spinor_generator)
            - np.kron(substrate_generator.T, np.eye(4))
            for spinor_generator, substrate_generator in zip(
                spinor_generators, substrate_generators
            )
        ]
    )
    equivariance_rank = int(np.linalg.matrix_rank(equivariance_operator, tol=1e-10))
    check(
        "specified exterior P_A action has 0+2 Casimir while spinor has 3/4",
        np.allclose(substrate_spectrum, [0.0, 2.0, 2.0, 2.0])
        and np.allclose(spinor_spectrum, [0.75, 0.75, 0.75, 0.75]),
        f"P_A={substrate_spectrum.tolist()}, spinor={spinor_spectrum.tolist()}",
    )
    check(
        "specified 1+3 to 2+2 equivariant intertwiner space is zero",
        equivariance_rank == 16,
        f"rank={equivariance_rank}, nullity={16-equivariance_rank}",
    )

    full_annihilators = [jw_annihilator(mode, 4) for mode in range(4)]
    full_gammas = [c + c.conj().T for c in full_annihilators]
    ident16 = np.eye(16, dtype=complex)
    full_clifford_error = 0.0
    for i, gi in enumerate(full_gammas):
        for j, gj in enumerate(full_gammas):
            expected = (2.0 if i == j else 0.0) * ident16
            full_clifford_error = max(
                full_clifford_error,
                np.linalg.norm(anticommutator(gi, gj) - expected),
            )
    pa = np.diag(
        [1.0 if int(index).bit_count() == 1 else 0.0 for index in range(16)]
    ).astype(complex)
    compression = max(np.linalg.norm(pa @ gamma @ pa) for gamma in full_gammas)
    leakage = max(np.linalg.norm((ident16 - pa) @ gamma @ pa) for gamma in full_gammas)
    check(
        "natural full-cell odd generators realize Cl_4",
        full_clifford_error < 1.0e-12,
        f"max error={full_clifford_error:.2e}",
    )
    check(
        "natural full-cell odd generators compress to zero on P_A",
        compression < 1.0e-12,
        f"max ||P_A gamma_i P_A||={compression:.2e}",
    )
    check(
        "natural full-cell odd generators leak out of P_A",
        leakage > 1.0,
        f"max leakage norm={leakage:.6f}",
    )

    note = NOTE.read_text(encoding="utf-8")
    check(
        "source title is narrowed to conditional algebraic equivalence",
        note.startswith("# Area-Law Conditional Clifford–CAR Algebraic Equivalence Note"),
        NOTE.name,
    )
    check(
        "source scope forbids exterior-action descent laundering",
        "no exterior-action descent,\nphysical carrier, or coframe-response claim"
        in note,
        "scope firewall present",
    )
    check(
        "source explicitly stops before the physical channel assignment",
        "it does not imply `c_Widom=1/4`" in note
        and "It does not imply\n\n```text\nnormal channel + self-dual tangent channel" in note,
        "algebra-to-physics implication denied",
    )
    check(
        "source records the exact supplied-action obstruction",
        "simultaneous equivariant intertwiner space has dimension zero" in note
        and "P_A gamma_i P_A = 0" in note,
        "intertwiner and compression controls cited",
    )
    check(
        "source leaves all positive bridges explicit",
        "## Exact open bridges" in note
        and "None is currently supplied" in note,
        "open-bridge inventory present",
    )
    check(
        "superseded native-promotion wording is absent",
        "Why this is native enough to promote conditionally" not in note
        and "gives the positive chain" not in note,
        "no native or uniqueness laundering",
    )

    print()
    print("=" * 78)
    print(f"SUMMARY: PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    print("=" * 78)
    if FAIL_COUNT:
        print()
        print("Verdict: FAIL; the conditional algebra or claim boundary is broken.")
        return 1

    print()
    print("Verdict: CONDITIONAL ALGEBRAIC EQUIVALENCE ONLY.")
    print("A supplied irreducible Cl_4(C) response on C^4 is equivalent to")
    print("two-mode CAR. Rank four and the specified exterior one-form action")
    print("do not derive that response, a physical channel assignment, or 1/4;")
    print("other substrate actions and intrinsic active-block laws remain open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
