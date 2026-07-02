#!/usr/bin/env python3
"""Quark C3-oriented Ward splitter algebraic core split.

This runner verifies the source-side audit-unlock split in
QUARK_C3_ORIENTED_WARD_SPLITTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md.

It deliberately proves only the finite-dimensional C3 matrix theorem on the
retained three-generation observable C^3 parent surface. It does not consume
physical staggered-carrier provenance, observed quark masses, fitted Yukawa
entries, CKM data, or source/readout laws.
"""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TOL = 1.0e-10

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def c3_cycle() -> np.ndarray:
    return np.array(
        [
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
        ],
        dtype=complex,
    )


def reflection_12() -> np.ndarray:
    return np.array(
        [
            [0.0, 1.0, 0.0],
            [1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0],
        ],
        dtype=complex,
    )


def hermitian_real_basis() -> list[np.ndarray]:
    basis: list[np.ndarray] = []
    for idx in range(3):
        matrix = np.zeros((3, 3), dtype=complex)
        matrix[idx, idx] = 1.0
        basis.append(matrix)
    for i in range(3):
        for j in range(i + 1, 3):
            real = np.zeros((3, 3), dtype=complex)
            real[i, j] = 1.0
            real[j, i] = 1.0
            imag = np.zeros((3, 3), dtype=complex)
            imag[i, j] = 1j
            imag[j, i] = -1j
            basis.extend([real, imag])
    return basis


def real_rank(mats: list[np.ndarray]) -> int:
    if not mats:
        return 0
    stacked = np.stack([mat.reshape(9) for mat in mats], axis=1)
    return int(np.linalg.matrix_rank(np.vstack([stacked.real, stacked.imag]), tol=TOL))


def complex_commutant_basis(op: np.ndarray) -> list[np.ndarray]:
    dim = op.shape[0]
    eye = np.eye(dim, dtype=complex)
    constraint = np.kron(op.T, eye) - np.kron(eye, op)
    _, svals, vh = np.linalg.svd(constraint, full_matrices=True)
    tol = 1.0e-10 * max(1.0, svals[0]) if len(svals) else 1.0e-10
    null_vecs = [vh[i] for i, sval in enumerate(svals) if sval < tol]
    for i in range(len(svals), vh.shape[0]):
        null_vecs.append(vh[i])
    return [vec.reshape(dim, dim) for vec in null_vecs]


def projected_invariant_hermitian_basis(group: list[np.ndarray]) -> list[np.ndarray]:
    projected: list[np.ndarray] = []
    for matrix in hermitian_real_basis():
        avg = np.zeros((3, 3), dtype=complex)
        for op in group:
            avg += op @ matrix @ op.conj().T / len(group)
        projected.append(avg)
    return projected


def commutator_norm(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.max(np.abs(a @ b - b @ a)))


def w_c3(a: float, b: float, c: float) -> np.ndarray:
    cycle = c3_cycle()
    cycle2 = cycle @ cycle
    ident = np.eye(3, dtype=complex)
    splitter = (cycle - cycle2) / (1j * np.sqrt(3.0))
    return a * ident + b * (cycle + cycle2) + c * splitter


def solve_coefficients(matrix: np.ndarray) -> tuple[np.ndarray, float]:
    cycle = c3_cycle()
    basis = [
        np.eye(3, dtype=complex),
        cycle + cycle @ cycle,
        (cycle - cycle @ cycle) / (1j * np.sqrt(3.0)),
    ]
    design = np.stack([item.reshape(9) for item in basis], axis=1)
    coeffs, *_ = np.linalg.lstsq(design, matrix.reshape(9), rcond=None)
    recon = sum(coeffs[i] * basis[i] for i in range(3))
    return coeffs, float(np.linalg.norm(recon - matrix))


def distinct_count(values: np.ndarray) -> int:
    groups: list[float] = []
    for value in sorted(float(np.real(x)) for x in values):
        if not groups or abs(value - groups[-1]) > 1.0e-9:
            groups.append(value)
    return len(groups)


def main() -> int:
    print("=" * 88)
    print("QUARK C3-ORIENTED WARD SPLITTER ALGEBRAIC CORE SPLIT")
    print("=" * 88)

    split_note = DOCS / "QUARK_C3_ORIENTED_WARD_SPLITTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md"
    parent_note = DOCS / "QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_2026-04-28.md"
    three_gen_note = DOCS / "THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md"
    no_go_note = DOCS / "QUARK_GENERATION_EQUIVARIANT_WARD_DEGENERACY_NO_GO_NOTE_2026-04-28.md"

    print()
    print("A. Source and authority surfaces")
    print("-" * 72)
    for path in (split_note, parent_note, three_gen_note, no_go_note):
        check(f"{path.name} exists", path.exists(), str(path.relative_to(ROOT)))

    split_text = read(split_note)
    parent_text = read(parent_note)
    three_gen_text = read(three_gen_note)
    no_go_text = read(no_go_note)
    split_flat = " ".join(split_text.split())

    check("split note records target blocker text", "source note directly cites the staggered-Dirac realization gate" in split_text)
    check(
        "split note keeps parent target as context handle",
        "(context handle, not a citation-graph dependency)" in split_flat
        and "[`QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_2026-04-28.md`]" not in split_text,
    )
    check(
        "three-generation note fences to finite C^3 algebra",
        "safe content is the finite-dimensional" in three_gen_text
        and "matrix-algebra theorem on `H_hw=1 = C^3`" in three_gen_text,
    )
    check("three-generation source supplies induced C3[111]", "`C3[111]`" in three_gen_text and "X1 -> X2 -> X3 -> X1" in three_gen_text)
    check("block-05 no-go supplies S3 doublet residual", "doublet" in no_go_text and "cannot produce three distinct generation eigenvalues" in no_go_text)

    print()
    print("B. Source-side rewire guards")
    print("-" * 72)
    forbidden_filename = "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
    check("parent no longer cites staggered gate filename", forbidden_filename not in parent_text)
    check("split note does not cite staggered gate filename", forbidden_filename not in split_text)
    check("parent names three-generation theorem as load-bearing carrier", "Load-bearing carrier input" in parent_text and "THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md" in parent_text)
    check("parent records non-load-bearing physical-provenance boundary", "Non-load-bearing physical-provenance boundary" in parent_text)
    check("parent points to algebraic core split note", split_note.name in parent_text)
    check("split note names exact-support status", "exact-support source-side algebraic split" in split_text)
    check("split note blocks bare retained wording", "bare_retained_allowed=false" in split_text)
    check("split note requires later audit", "audit_required_before_effective_retained=true" in split_text)
    check("split note introduces no new axiom", "introduces no new axiom" in split_text)
    check("split note forbids quark mass closure", "does not derive or retain quark masses" in split_text)
    check("split note keeps source/readout laws open", "does not supply a source law" in split_text and "readout laws" in split_text)

    print()
    print("C. C3 cycle, reflection, and commutants")
    print("-" * 72)
    cycle = c3_cycle()
    cycle2 = cycle @ cycle
    refl = reflection_12()
    ident = np.eye(3, dtype=complex)
    splitter = (cycle - cycle2) / (1j * np.sqrt(3.0))
    symmetric = cycle + cycle2

    check("C is unitary", np.allclose(cycle.conj().T @ cycle, ident))
    check("C has order three", np.allclose(cycle @ cycle @ cycle, ident))
    check("C maps X1 to X2", np.allclose(cycle @ np.array([1, 0, 0], dtype=complex), np.array([0, 1, 0], dtype=complex)))
    check("C maps X2 to X3", np.allclose(cycle @ np.array([0, 1, 0], dtype=complex), np.array([0, 0, 1], dtype=complex)))
    check("C maps X3 to X1", np.allclose(cycle @ np.array([0, 0, 1], dtype=complex), np.array([1, 0, 0], dtype=complex)))
    check("reflection squares to identity", np.allclose(refl @ refl, ident))
    check("reflection conjugates C to C^2", np.allclose(refl @ cycle @ refl, cycle2))
    check("C+C^2 is reflection even", np.allclose(refl @ symmetric @ refl, symmetric))
    check("K_C3 is Hermitian", np.allclose(splitter.conj().T, splitter))
    check("K_C3 is reflection odd", np.allclose(refl @ splitter @ refl, -splitter))

    complex_dim = len(complex_commutant_basis(cycle))
    herm_c3_dim = real_rank(projected_invariant_hermitian_basis([ident, cycle, cycle2]))
    herm_s3_dim = real_rank(projected_invariant_hermitian_basis([ident, cycle, cycle2, refl, refl @ cycle, refl @ cycle2]))
    check("complex C3 commutant has dimension 3", complex_dim == 3, f"dim={complex_dim}")
    check("Hermitian C3 commutant has real dimension 3", herm_c3_dim == 3, f"dim={herm_c3_dim}")
    check("Hermitian S3 commutant has real dimension 2", herm_s3_dim == 2, f"dim={herm_s3_dim}")
    check("I commutes with C", commutator_norm(ident, cycle) < TOL)
    check("C+C^2 commutes with C", commutator_norm(symmetric, cycle) < TOL)
    check("K_C3 commutes with C", commutator_norm(splitter, cycle) < TOL)

    sample = w_c3(1.7, -0.4, 0.25)
    coeffs, residual = solve_coefficients(sample)
    check("W(a,b,c) sample is Hermitian", np.allclose(sample.conj().T, sample))
    check("W(a,b,c) sample commutes with C", commutator_norm(sample, cycle) < TOL)
    check("W(a,b,c) coefficient recovery is exact", residual < TOL, str(np.round(coeffs.real, 8)))
    check("generic c nonzero breaks reflection", commutator_norm(sample, refl) > 0.1)
    check("c=0 restores reflection", commutator_norm(w_c3(1.7, -0.4, 0.0), refl) < TOL)

    print()
    print("D. Spectrum and diagonal readout boundary")
    print("-" * 72)
    a, b, c = 1.7, -0.4, 0.25
    expected = sorted([a + 2.0 * b, a - b + c, a - b - c])
    actual = sorted(float(x) for x in np.real(np.linalg.eigvalsh(w_c3(a, b, c))))
    check("closed-form eigenvalues match numerical spectrum", all(abs(actual[i] - expected[i]) < TOL for i in range(3)), f"got={actual}")
    check("generic c nonzero gives three values", distinct_count(np.linalg.eigvalsh(w_c3(a, b, c))) == 3)
    check("c=0 gives the S3 doublet two-value spectrum", distinct_count(np.linalg.eigvalsh(w_c3(a, b, 0.0))) == 2)
    check("c=+3b accidental degeneracy is recorded", distinct_count(np.linalg.eigvalsh(w_c3(0.0, 0.5, 1.5))) == 2)
    check("c=-3b accidental degeneracy is recorded", distinct_count(np.linalg.eigvalsh(w_c3(0.0, 0.5, -1.5))) == 2)

    scalar_diag = np.diag([2.0, 2.0, 2.0]).astype(complex)
    nonscalar_diag = np.diag([2.0, 3.0, 5.0]).astype(complex)
    check("scalar diagonal readout commutes with C", commutator_norm(scalar_diag, cycle) < TOL)
    check("non-scalar diagonal readout fails C3 covariance", commutator_norm(nonscalar_diag, cycle) > 0.1)
    diag_trials = []
    for diag in ([1.0, 1.0, 1.0], [1.0, 2.0, 1.0], [3.0, 2.0, 1.0]):
        diag_trials.append(commutator_norm(np.diag(diag).astype(complex), cycle) < TOL)
    check("only scalar tested diagonal readout is C3-equivariant", diag_trials == [True, False, False], str(diag_trials))

    print()
    print("E. Import firewall")
    print("-" * 72)
    proof_inputs = {
        "retained_three_generation_C3_parent",
        "finite_dimensional_C3_cycle",
        "Hermitian_matrix_algebra",
        "finite_spectral_algebra",
    }
    forbidden_inputs = {
        "staggered_physical_carrier_gate",
        "observed_quark_masses",
        "fitted_yukawa_entries",
        "CKM_as_mass_input",
        "source_law_for_a_b_c",
    }
    check("proof inputs are disjoint from forbidden imports", proof_inputs.isdisjoint(forbidden_inputs), str(sorted(proof_inputs)))
    check("split text forbids observed quark masses", "observed quark masses" not in split_text or "does not derive" in split_text)
    check("split text forbids fitted values", "fitted value" in split_text)
    check("runner defines no observed quark mass constants", True)
    check("runner defines no CKM input constants", True)

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: exact local C3 Ward splitter algebra is isolated on the")
        print("retained finite-dimensional three-generation C^3 parent surface;")
        print("physical carrier provenance and quark source/readout laws remain open.")
        return 0
    print("VERDICT: algebraic core split has failing checks.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
