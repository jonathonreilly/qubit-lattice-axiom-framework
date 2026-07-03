"""Scalar-i versus real generation structure under a supplied conjugation.

This runner is intentionally narrow.  It assumes a supplied readout context
with a supplied entrywise conjugation K(X)=conj(X).  It does not claim that the
Record axiom supplies that context, the central-sector decomposition, or K/CPT.

The finite checks separate two sectors and keep the cited generation
orientation object labeled:

* scalar-i / phase data: K-odd under entrywise conjugation;
* real generation complex-structure data J_cs: K-even under the same
  conjugation;
* labeled Vandermonde orientation sign: K-odd under the induced
  delta -> -delta map, so it is not part of the K-even J_cs sector.

No measured values, fitted selectors, dynamics, or probability rules enter.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


def K(matrix: np.ndarray) -> np.ndarray:
    """Supplied entrywise conjugation in the chosen basis."""
    return np.conjugate(matrix)


def k_parity(matrix: np.ndarray, tol: float = 1e-12) -> str:
    if np.allclose(K(matrix), -matrix, atol=tol):
        return "odd"
    if np.allclose(K(matrix), matrix, atol=tol):
        return "even"
    return "mixed"


def born_triple(delta: float) -> np.ndarray:
    lambdas = np.array(
        [1.0 + np.sqrt(2.0) * np.cos(delta + 2.0 * np.pi * k / 3.0) for k in range(3)],
        dtype=float,
    )
    weights = lambdas * lambdas
    return weights / float(np.sum(weights))


def labeled_vandermonde(weights: np.ndarray) -> float:
    return float((weights[0] - weights[1]) * (weights[1] - weights[2]) * (weights[2] - weights[0]))


def source_note_guardrail() -> tuple[bool, str]:
    note = Path(
        "docs/SCALAR_I_AND_REAL_GENERATION_STRUCTURE_K_PARITY_SEPARATION_BOUNDED_NOTE_2026-06-08.md"
    ).read_text(encoding="utf-8")
    required = [
        "supplied entrywise conjugation",
        "Record does not supply",
        "does not derive `r`",
    ]
    forbidden = [
        "global " + "Record",
        "Tier-A " + "floor",
        "single scalar-i = " + "Record",
        "licenses value " + "computation",
    ]
    missing = [phrase for phrase in required if phrase not in note]
    present_forbidden = [phrase for phrase in forbidden if phrase in note]
    ok = not missing and not present_forbidden
    detail = f"missing={missing}; forbidden_present={present_forbidden}"
    return ok, detail


def main() -> int:
    print("Scalar-i and real J_cs structure K-parity separation")
    print("=" * 72)

    I2 = np.eye(2, dtype=complex)
    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)

    central_i = 1j * I2
    volume = sigma_x @ sigma_y @ sigma_z
    tensor_i_left = np.kron(central_i, I2)
    tensor_i_right = np.kron(I2, central_i)

    check(
        "Cl(3,0) volume product equals central scalar i I_2",
        np.allclose(volume, central_i),
        f"||sigma_x sigma_y sigma_z - i I_2|| = {np.linalg.norm(volume - central_i):.3e}",
    )

    check(
        "tensor placement shares the same central scalar i",
        np.allclose(tensor_i_left, tensor_i_right)
        and np.allclose(tensor_i_left, 1j * np.eye(4)),
        f"||left-right|| = {np.linalg.norm(tensor_i_left - tensor_i_right):.3e}",
    )

    scalar_cluster = {
        "i I_2": central_i,
        "sigma_y": sigma_y,
        "volume": volume,
        "tensor i": tensor_i_left,
    }
    parities = {name: k_parity(matrix) for name, matrix in scalar_cluster.items()}
    check(
        "scalar-i cluster is K-odd under the supplied entrywise conjugation",
        all(parity == "odd" for parity in parities.values()),
        ", ".join(f"{name}:{parity}" for name, parity in parities.items()),
    )

    C = np.array(
        [[0, 1, 0], [0, 0, 1], [1, 0, 0]],
        dtype=complex,
    )
    I3 = np.eye(3, dtype=complex)
    a = 1.0
    b_abs = 1.0 / np.sqrt(2.0)
    delta = 0.2222
    b = b_abs * np.exp(1j * delta)
    M_delta = a * I3 + b * C + np.conjugate(b) * (C @ C)
    b_neg = b_abs * np.exp(-1j * delta)
    M_neg_delta = a * I3 + b_neg * C + np.conjugate(b_neg) * (C @ C)
    phase_conjugates = np.allclose(K(M_delta), M_neg_delta)
    spectrum_even = np.allclose(
        np.sort(np.linalg.eigvalsh(M_delta)),
        np.sort(np.linalg.eigvalsh(M_neg_delta)),
    )
    check(
        "Hermitian C_3 circulant phase conjugates by delta -> -delta with spectrum fixed as a multiset",
        phase_conjugates and spectrum_even,
        f"K(M_delta)=M_-delta: {phase_conjugates}; spectra match: {spectrum_even}",
    )

    P_triv = np.ones((3, 3), dtype=complex) / 3.0
    J_cs = (C - C @ C) / np.sqrt(3.0)
    jcs_real = np.allclose(J_cs.imag, 0.0)
    jcs_even = k_parity(J_cs) == "even"
    jcs_complex_structure = np.allclose(J_cs @ J_cs, -(I3 - P_triv))
    check(
        "J_cs is real, K-even, and squares to -(I-P_triv) on the doublet",
        jcs_real and jcs_even and jcs_complex_structure,
        f"real={jcs_real}; K-parity={k_parity(J_cs)}; square identity={jcs_complex_structure}",
    )

    p_delta = born_triple(delta)
    p_neg_delta = born_triple(-delta)
    labeled_delta = labeled_vandermonde(p_delta)
    labeled_neg_delta = labeled_vandermonde(p_neg_delta)
    labeled_orientation_odd = np.isclose(labeled_neg_delta, -labeled_delta, atol=1e-12)
    check(
        "labeled generation Vandermonde orientation is K-odd under induced delta -> -delta",
        labeled_orientation_odd and np.sign(labeled_delta) == -np.sign(labeled_neg_delta),
        f"Delta(+delta)={labeled_delta:.8f}; Delta(-delta)={labeled_neg_delta:.8f}",
    )

    sorted_delta = np.sort(np.linalg.eigvalsh(M_delta).real)
    sorted_neg_delta = np.sort(np.linalg.eigvalsh(M_neg_delta).real)
    sorted_v_delta = labeled_vandermonde(sorted_delta)
    sorted_v_neg_delta = labeled_vandermonde(sorted_neg_delta)
    check(
        "sorted-spectrum discriminant is a K-even multiset control, not the labeled orientation",
        np.isclose(sorted_v_delta, sorted_v_neg_delta, atol=1e-12),
        f"sorted_Delta(+delta)={sorted_v_delta:.8f}; sorted_Delta(-delta)={sorted_v_neg_delta:.8f}",
    )

    scalar_i_sector_odd = all(parity == "odd" for parity in parities.values()) and phase_conjugates
    real_generation_jcs_sector_even = jcs_even
    check(
        "scalar-i phase data and real J_cs structure lie in different K-parity sectors",
        scalar_i_sector_odd and real_generation_jcs_sector_even and labeled_orientation_odd,
        (
            f"scalar-i sector K-odd={scalar_i_sector_odd}; "
            f"J_cs sector K-even={real_generation_jcs_sector_even}; "
            f"labeled Vandermonde K-odd={labeled_orientation_odd}"
        ),
    )

    guardrail_ok, guardrail_detail = source_note_guardrail()
    check(
        "source note keeps supplied-K and Record-boundary guardrails",
        guardrail_ok,
        guardrail_detail,
    )

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
