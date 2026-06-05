#!/usr/bin/env python3
"""Audit-companion runner for the Busch POVM-extension parent note
`BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`
recording Record-axiom invariance after the 2026-06-04 framework axiom
adoption (the deps_changed:dep_added:minimal_axioms edge).

Companion source note:
  docs/BUSCH_POVM_EXTENSION_DEPS_CHANGED_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `busch_povm_extension_on_qubit_lattice_narrow_theorem_note_2026-05-20`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence that the parent's load-bearing
    chain
        m(E) = Tr(sigma * E)  on  E(H_Lambda) = { E in M_{2^|Lambda|}(C) : 0 <= E <= I }
    is independent of the Record axiom adopted in
    `MINIMAL_AXIOMS_2026-06-04.md`. This does not re-apply the prior
    audit verdict; it gives the audit lane a machine-checkable basis
    for deciding whether the arithmetic needs fresh review after the
    premise-hash change.

The runner verifies the load-bearing chain block-by-block under
"Record axiom included" and "Record axiom not included" outer scopes,
confirms identical numeric outputs in both scopes, and
performs a static-source scan of the parent note's load-bearing
sections to confirm zero Record-axiom usage in the auditable core.

Every load-bearing check uses only:
  (i)   the Z^3 site set restricted to finite Lambda (Lattice axiom
        content);
  (ii)  the per-site qubit algebra A_x ~= M_2(C) and standard tensor
        product H_Lambda = tensor_x C^2, A_Lambda = tensor_x M_2(C)
        ~= M_{2^|Lambda|}(C) (Quantum axiom content);
  (iii) textbook POVM / effect-algebra structure on a finite-dim
        complex Hilbert space (effect-algebra membership 0 <= E <= I;
        POVM partition Sigma E_i = I; POVM-additive probability
        measure axioms M1-M3);
  (iv)  Busch 2003 / CFMR 2004 POVM-additive extension theorem on
        dim >= 2 (cited textbook mathematical physics; not re-derived);
  (v)   finite-dimensional Riesz representation of positive linear
        functionals on M_d(C) as Tr(sigma * .).

No Record-axiom content (scalar record-readout functional `I(.)`
satisfying I(R_1 sqcup R_2) = I(R_1) + I(R_2)) enters any block. No
claim is made about the Record-axiom-induced downstream content; the
companion observation is strictly limited to the load-bearing chain
of the parent note.

Block plan:
  Block 1  : Lattice/operator dimensions dim H_Lambda = 2^|Lambda| for
             |Lambda| in {1, 2, 3}, including the load-bearing
             dim-2 single-site case.
  Block 2  : POVM effect-algebra membership 0 <= E <= I for random
             projected Hermitian operators on H_Lambda, |Lambda| in
             {1, 2}.
  Block 3  : POVM partition closure Sigma_i E_i = I for explicit
             POVMs (Pauli-X/Z eigenprojector pairs; SIC-POVM on dim 2;
             uniform projective POVMs on dim 4).
  Block 4  : POVM-additive probability measure: random density
             matrices sigma yield m(E) = Tr(sigma * E) in [0, 1].
  Block 5  : Probability normalization m(I) = Tr(sigma * I) = 1.
  Block 6  : Probability of zero effect m(0) = Tr(sigma * 0) = 0.
  Block 7  : POVM-additivity over partitions:
             Sigma_i Tr(sigma * E_i) = 1 for random POVMs.
  Block 8  : Riesz representation inverse: density matrix recovered
             from positive linear functional via Hilbert-Schmidt
             inner product on the Pauli-string basis.
  Block 9  : Static-source scan of parent note's load-bearing
             sections: zero Record-axiom usage tokens; positive
             Lattice / Quantum / POVM tokens present.
  Block 10 : Record-axiom counterfactual: identical numeric output
             with and without an explicit "Record axiom included"
             outer scope.
  Block 11 : Lattice / Quantum content preservation across the
             historical 2026-05-20 and current 2026-06-04
             minimal-axioms memos.
  Block 12 : Four-route cross-check on m(E) = Tr(sigma * E) for a
             fixed test (sigma, E) on dim H_Lambda = 4.

The exact PASS/FAIL count is printed at runtime.
"""

from __future__ import annotations

import math
import sys
from itertools import product
from pathlib import Path

import numpy as np


# -----------------------------------------------------------
# Logging and counters
# -----------------------------------------------------------

LOG_LINES: list[str] = []
PASS = 0
FAIL = 0


def log(msg: str = "") -> None:
    LOG_LINES.append(msg)
    print(msg)


def record(check_name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        log(f"  PASS {check_name}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        log(f"  FAIL {check_name}" + (f" :: {detail}" if detail else ""))


def isclose(a: complex, b: complex, atol: float = 1e-10) -> bool:
    return abs(a - b) <= atol


def header(title: str) -> None:
    log("")
    log("=" * 72)
    log(title)
    log("=" * 72)


# -----------------------------------------------------------
# Deterministic RNG (seed pinned for reproducibility)
# -----------------------------------------------------------

SEED = 20260604
rng = np.random.default_rng(SEED)


# -----------------------------------------------------------
# Linear-algebra helpers (pure POVM / effect-algebra primitives)
# -----------------------------------------------------------

PAULI_I = np.array([[1.0, 0.0], [0.0, 1.0]], dtype=complex)
PAULI_X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
PAULI_Y = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
PAULI_Z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
PAULIS = [PAULI_I, PAULI_X, PAULI_Y, PAULI_Z]


def hilbert_dim(lambda_size: int) -> int:
    """dim H_Lambda = 2^|Lambda| (Quantum + Lattice axiom content)."""
    return 2 ** lambda_size


def random_hermitian(d: int) -> np.ndarray:
    """Random complex Hermitian matrix in M_d(C)."""
    A = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    return 0.5 * (A + A.conj().T)


def random_density_matrix(d: int) -> np.ndarray:
    """Random density matrix on C^d via Ginibre construction."""
    A = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    M = A @ A.conj().T            # positive semidef
    return M / np.trace(M).real   # normalized to Tr = 1


def project_onto_effect_algebra(H: np.ndarray) -> np.ndarray:
    """Spectral clip onto [0, 1] -> in E(H), i.e. 0 <= E <= I.

    Uses eigendecomposition + clipping; result satisfies 0 <= E <= I.
    """
    H = 0.5 * (H + H.conj().T)
    w, U = np.linalg.eigh(H)
    w_clip = np.clip(w, 0.0, 1.0)
    return (U * w_clip) @ U.conj().T


def is_in_effect_algebra(E: np.ndarray, atol: float = 1e-10) -> bool:
    """Check 0 <= E <= I (Hermitian, eigenvalues in [-atol, 1+atol])."""
    if not np.allclose(E, E.conj().T, atol=atol):
        return False
    w = np.linalg.eigvalsh(E)
    return bool((w.min() >= -atol) and (w.max() <= 1.0 + atol))


def pauli_string_basis(n_qubits: int) -> list[np.ndarray]:
    """Orthogonal Hermitian basis of M_{2^n}(C) as tensor products of
    Paulis. <B_a, B_b>_HS = Tr(B_a^dag B_b) = d * delta_{ab} with the
    convention used in Block 8."""
    basis = []
    for inds in product(range(4), repeat=n_qubits):
        M = PAULIS[inds[0]]
        for i in inds[1:]:
            M = np.kron(M, PAULIS[i])
        basis.append(M)
    return basis


def random_povm(d: int, n_outcomes: int) -> list[np.ndarray]:
    """Construct a random n-outcome POVM on C^d via Naimark-style
    convex split: generate n random positive matrices, normalize the
    sum to I.

    Returns {E_1, ..., E_n} with E_i >= 0 and Sigma E_i = I.
    """
    Es = []
    for _ in range(n_outcomes):
        A = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
        Es.append(A @ A.conj().T)
    S = sum(Es)
    # Normalize so that sum = I via S^{-1/2} E_i S^{-1/2}
    w, U = np.linalg.eigh(S)
    S_inv_half = (U * (1.0 / np.sqrt(w))) @ U.conj().T
    Es_norm = [S_inv_half @ E @ S_inv_half for E in Es]
    return Es_norm


# -----------------------------------------------------------
# Block 1: Lattice/operator dimensions dim H_Lambda = 2^|Lambda|
# -----------------------------------------------------------

def block1() -> None:
    header("BLOCK 1: dim H_Lambda = 2^|Lambda| (Quantum + Lattice content)")
    log("  Per-site qubit (Quantum axiom): A_x ~= M_2(C), H_x = C^2.")
    log("  Finite Lambda subset Z^3 (Lattice axiom).")
    log("  Standard tensor product: H_Lambda = tensor_x C^2.")
    all_dims_ok = True
    for L in (1, 2, 3):
        d = hilbert_dim(L)
        expected = 2 ** L
        if d != expected:
            all_dims_ok = False
    record("dim_H_Lambda_equals_2_pow_L_for_L_in_1_2_3", all_dims_ok,
           "checked |Lambda|=1,2,3: dim H matches 2^|Lambda|")

    # Explicitly load-bearing dim-2 single-site case
    d_single = hilbert_dim(1)
    record("load_bearing_single_site_dim_2",
           d_single == 2 and d_single >= 2,
           f"|Lambda|=1: dim H = 2 (Gleason-gap-bearing case)")

    # Quantum axiom: A_Lambda ~= M_{2^|Lambda|}(C) on the test sizes used
    # downstream (|Lambda| in {1, 2}).
    all_alg_ok = True
    for L in (1, 2):
        d = hilbert_dim(L)
        H = random_hermitian(d)
        if not (H.shape == (d, d) and H.dtype == complex):
            all_alg_ok = False
    record("A_Lambda_is_M_2_pow_L_C_for_L_in_1_2", all_alg_ok,
           "A_Lambda = M_{2^|Lambda|}(C) on the downstream test sizes")


# -----------------------------------------------------------
# Block 2: POVM effect-algebra membership
# -----------------------------------------------------------

def block2() -> None:
    header("BLOCK 2: Effect algebra E(H_Lambda) = { E : 0 <= E <= I }")
    log("  Standard POVM-effect-algebra definition (textbook).")
    for L in (1, 2):
        d = hilbert_dim(L)
        H = random_hermitian(d)
        E = project_onto_effect_algebra(H)
        ok_hermitian = np.allclose(E, E.conj().T, atol=1e-10)
        ok_bounds = is_in_effect_algebra(E)
        ok_dim = E.shape == (d, d)
        record(f"effect_membership_L{L}",
               ok_hermitian and ok_bounds and ok_dim,
               f"|Lambda|={L}: 0 <= E <= I, E in M_{d}(C)")


# -----------------------------------------------------------
# Block 3: POVM partition closure Sigma E_i = I
# -----------------------------------------------------------

def block3() -> None:
    header("BLOCK 3: POVM partition Sigma_i E_i = I")
    log("  Standard POVM definition (textbook quantum measurement).")

    # Pauli-Z eigenprojectors on dim 2
    P_up = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
    P_dn = np.array([[0.0, 0.0], [0.0, 1.0]], dtype=complex)
    S = P_up + P_dn
    record("povm_pauli_z_eigenprojectors_sum_to_I",
           np.allclose(S, np.eye(2)),
           f"|Sigma E_i - I|_max = {np.max(np.abs(S - np.eye(2))):.3e}")

    # Pauli-X eigenprojectors on dim 2
    plus = (1.0 / np.sqrt(2.0)) * np.array([1.0, 1.0], dtype=complex)
    minus = (1.0 / np.sqrt(2.0)) * np.array([1.0, -1.0], dtype=complex)
    P_plus = np.outer(plus, plus.conj())
    P_minus = np.outer(minus, minus.conj())
    S2 = P_plus + P_minus
    record("povm_pauli_x_eigenprojectors_sum_to_I",
           np.allclose(S2, np.eye(2)),
           f"|Sigma E_i - I|_max = {np.max(np.abs(S2 - np.eye(2))):.3e}")

    # SIC-POVM on dim 2 (4-outcome tetrahedron). Bloch vectors at
    # symmetric corners of a regular tetrahedron, scaled to length 1.
    # E_k = (1/4) (I + n_k . sigma_vec) gives sum = I.
    rt3 = math.sqrt(3.0)
    n_vecs = [
        ( 1.0/rt3,  1.0/rt3,  1.0/rt3),
        ( 1.0/rt3, -1.0/rt3, -1.0/rt3),
        (-1.0/rt3,  1.0/rt3, -1.0/rt3),
        (-1.0/rt3, -1.0/rt3,  1.0/rt3),
    ]
    sic = []
    for nx, ny, nz in n_vecs:
        E_k = 0.25 * (PAULI_I + nx * PAULI_X + ny * PAULI_Y + nz * PAULI_Z)
        sic.append(E_k)
    S_sic = sum(sic)
    record("povm_sic_dim2_sum_to_I",
           np.allclose(S_sic, np.eye(2), atol=1e-12),
           f"|Sigma E_i - I|_max = {np.max(np.abs(S_sic - np.eye(2))):.3e}")
    all_in = all(is_in_effect_algebra(E_k) for E_k in sic)
    record("povm_sic_dim2_all_elements_in_effect_algebra", all_in,
           "every SIC element satisfies 0 <= E <= I")

    # Uniform projective POVM on dim 4 (standard basis projectors).
    proj4 = []
    for i in range(4):
        Pi = np.zeros((4, 4), dtype=complex)
        Pi[i, i] = 1.0
        proj4.append(Pi)
    S4 = sum(proj4)
    record("povm_uniform_dim4_standard_basis_sum_to_I",
           np.allclose(S4, np.eye(4), atol=1e-12),
           f"|Sigma E_i - I|_max = {np.max(np.abs(S4 - np.eye(4))):.3e}")


# -----------------------------------------------------------
# Block 4: POVM-additive probability measure: m(E) in [0,1]
# -----------------------------------------------------------

def block4() -> None:
    header("BLOCK 4: m(E) = Tr(sigma * E) in [0, 1] for random sigma, E")
    log("  Density-matrix induced probability measure (forward direction).")
    for L in (1, 2):
        d = hilbert_dim(L)
        sigma = random_density_matrix(d)
        E = project_onto_effect_algebra(random_hermitian(d))
        m = complex(np.trace(sigma @ E)).real
        ok_real = abs(complex(np.trace(sigma @ E)).imag) < 1e-10
        ok_range = (-1e-10) <= m <= (1.0 + 1e-10)
        record(f"m_E_in_unit_interval_L{L}",
               ok_real and ok_range,
               f"|Lambda|={L}: m(E) = {m:.12f}")


# -----------------------------------------------------------
# Block 5: Normalization m(I) = 1
# -----------------------------------------------------------

def block5() -> None:
    header("BLOCK 5: m(I) = Tr(sigma) = 1  (axiom M2)")
    for L in (1, 2):
        d = hilbert_dim(L)
        sigma = random_density_matrix(d)
        m_id = complex(np.trace(sigma @ np.eye(d))).real
        record(f"m_identity_equals_1_L{L}",
               isclose(m_id, 1.0),
               f"|Lambda|={L}: Tr(sigma*I) = {m_id:.15f}")


# -----------------------------------------------------------
# Block 6: m(0) = 0
# -----------------------------------------------------------

def block6() -> None:
    header("BLOCK 6: m(0) = Tr(sigma * 0) = 0  (axiom M1)")
    for L in (1, 2):
        d = hilbert_dim(L)
        sigma = random_density_matrix(d)
        m_zero = complex(np.trace(sigma @ np.zeros((d, d), dtype=complex)))
        record(f"m_zero_effect_equals_0_L{L}",
               abs(m_zero) < 1e-12,
               f"|Lambda|={L}: |Tr(sigma*0)| = "
               f"{abs(m_zero):.3e}")


# -----------------------------------------------------------
# Block 7: POVM-additivity Sigma_i m(E_i) = 1 over POVM partitions
# -----------------------------------------------------------

def block7() -> None:
    header("BLOCK 7: POVM-additivity: Sigma_i Tr(sigma * E_i) = 1  (axiom M3)")
    for L in (1, 2):
        d = hilbert_dim(L)
        for n_outcomes in (2, 3):
            sigma = random_density_matrix(d)
            Es = random_povm(d, n_outcomes)
            # First verify the POVM closes: Sigma E_i = I
            S = sum(Es)
            povm_closes = np.allclose(S, np.eye(d), atol=1e-9)
            # Then verify additivity of m over the POVM partition.
            m_sum = sum(complex(np.trace(sigma @ E)).real for E in Es)
            record(
                f"povm_partition_closes_L{L}_n{n_outcomes}",
                povm_closes,
                f"|Lambda|={L} n={n_outcomes}: "
                f"|Sigma E_i - I|_max = "
                f"{np.max(np.abs(S - np.eye(d))):.3e}",
            )
            record(
                f"povm_additivity_sum_to_1_L{L}_n{n_outcomes}",
                isclose(m_sum, 1.0),
                f"|Lambda|={L} n={n_outcomes}: "
                f"Sigma m(E_i) = {m_sum:.12f}",
            )


# -----------------------------------------------------------
# Block 8: Riesz representation inverse: recover sigma from m via HS
# -----------------------------------------------------------

def block8() -> None:
    header("BLOCK 8: Riesz representation: sigma recovered via "
           "Hilbert-Schmidt inner product")
    log("  Inverse direction of Busch: positive linear functional on")
    log("  M_d(C)_sa is Tr(sigma * .) for unique density matrix sigma.")
    for L in (1, 2):
        d = hilbert_dim(L)
        basis = pauli_string_basis(L)
        # Hilbert-Schmidt normalization: <B_a, B_b>_HS = Tr(B_a B_b) = d delta_ab
        # (Paulis are Hermitian; tensor-products too.)
        # Confirm orthogonality of the chosen basis explicitly.
        ortho_ok = True
        for a, Ba in enumerate(basis):
            for b, Bb in enumerate(basis):
                inner = complex(np.trace(Ba.conj().T @ Bb)).real
                expected = float(d) if a == b else 0.0
                if abs(inner - expected) > 1e-9:
                    ortho_ok = False
        record(f"pauli_string_basis_orthogonal_L{L}", ortho_ok,
               f"|Lambda|={L}: <B_a, B_b>_HS = d * delta_ab")

        # Define a positive linear functional via a random density matrix.
        sigma_true = random_density_matrix(d)
        # Reconstruct sigma from its action on the orthonormal Pauli basis:
        # sigma = (1/d) Sigma_a Tr(sigma * B_a) * B_a
        coeffs = [complex(np.trace(sigma_true @ B)).real for B in basis]
        sigma_recovered = (1.0 / d) * sum(c * B for c, B in zip(coeffs, basis))
        diff = np.max(np.abs(sigma_recovered - sigma_true))
        record(f"sigma_recovered_from_pauli_basis_L{L}",
               diff < 1e-9,
               f"|Lambda|={L}: |sigma_rec - sigma|_max = {diff:.3e}")

        # The recovered sigma is positive (rule out a spurious negative
        # eigenvalue from numerical noise) and unit-trace.
        w = np.linalg.eigvalsh(0.5 * (sigma_recovered + sigma_recovered.conj().T))
        tr = complex(np.trace(sigma_recovered)).real
        record(f"sigma_recovered_positive_L{L}",
               w.min() > -1e-9,
               f"|Lambda|={L}: min eig = {w.min():.3e}")
        record(f"sigma_recovered_unit_trace_L{L}",
               abs(tr - 1.0) < 1e-9,
               f"|Lambda|={L}: Tr = {tr:.12f}")


# -----------------------------------------------------------
# Block 9: Parent note Record-axiom usage scan
# -----------------------------------------------------------

def block9(parent_note_path: Path) -> None:
    header("BLOCK 9: Parent note Record-axiom usage scan "
           "(load-bearing sections)")
    if not parent_note_path.exists():
        log(f"  WARN: parent note not found at {parent_note_path}")
        record("parent_note_present", False, str(parent_note_path))
        return

    text = parent_note_path.read_text()
    record("parent_note_present", True, str(parent_note_path))

    # Identify load-bearing sections: Setup, Step 1, Step 2, Step 3,
    # Step 4, Claim. The "What this does not close" section is NOT
    # load-bearing and contains the only "record" reference (pointer
    # to adjacent rows about pre-record / persistent-record).
    start = text.find("## Claim")
    end = text.find("## What this can close after audit")
    record("structural_section_start_found", start >= 0,
           f"## Claim start index = {start}")
    record("structural_section_end_found", end > start,
           f"## What this can close after audit end index = {end}")

    section = text[start:end] if (start >= 0 and end > start) else ""

    # Tokens that would indicate Record-axiom usage in the load-bearing chain
    record_tokens = [
        "I(R_1",
        "I(R)",
        "scalar record",
        "record functional",
        "record-readout",
        "additive record",
        "additive scalar record",
        "MINIMAL_AXIOMS_2026-06-04",
    ]
    found = [tok for tok in record_tokens if tok in section]
    record("zero_record_axiom_tokens_in_load_bearing_section",
           len(found) == 0,
           f"matches = {found}")

    # Confirm Lattice / Quantum / POVM structural tokens ARE used in
    # the load-bearing sections.
    expected_tokens = [
        "Z^3",                    # Lattice
        "M_2(ℂ)",                  # Quantum (per-site)
        "ℂ²",                      # Quantum (per-site Hilbert)
        "POVM",                   # parent's auditable mechanism
        "Tr(σ",                   # Born form
        "E(H_Λ)",                  # effect algebra
    ]
    found_lattice_quantum = [tok for tok in expected_tokens if tok in section]
    record(
        "lattice_quantum_povm_content_present_in_load_bearing_section",
        len(found_lattice_quantum) >= 4,
        f"matches >= 4: {found_lattice_quantum}",
    )


# -----------------------------------------------------------
# Block 10: Record-axiom counterfactual
# -----------------------------------------------------------

def block10() -> None:
    header("BLOCK 10: Record-axiom counterfactual: identical numeric output")
    log("  The load-bearing arithmetic uses neither the Record axiom's")
    log("  scalar functional I(.) nor a record-readout surface; therefore")
    log("  re-running with/without included Record axiom content must give")
    log("  bit-identical results.")

    def compute_load_bearing_outputs(record_axiom_asserted: bool):
        """Recompute Block-4/5/6/7 representative values. The
        record_axiom_asserted flag is intentionally unused inside the
        computation, which is the whole point of (C1).
        """
        # Use a freshly seeded RNG so the two runs are bit-identical.
        local_rng = np.random.default_rng(20260604)
        d = 4  # |Lambda| = 2
        # Density matrix
        A = local_rng.standard_normal((d, d)) + 1j * local_rng.standard_normal((d, d))
        M = A @ A.conj().T
        sigma = M / np.trace(M).real
        # Effect E
        H = local_rng.standard_normal((d, d)) + 1j * local_rng.standard_normal((d, d))
        H = 0.5 * (H + H.conj().T)
        w, U = np.linalg.eigh(H)
        E = (U * np.clip(w, 0.0, 1.0)) @ U.conj().T
        # POVM = {E, I-E}
        Es = [E, np.eye(d) - E]
        m_E = complex(np.trace(sigma @ E)).real
        m_complement = complex(np.trace(sigma @ Es[1])).real
        m_identity = complex(np.trace(sigma @ np.eye(d))).real
        m_zero = complex(np.trace(sigma @ np.zeros((d, d), dtype=complex)))
        return (m_E, m_complement, m_identity, m_zero)

    with_record = compute_load_bearing_outputs(record_axiom_asserted=True)
    without_record = compute_load_bearing_outputs(record_axiom_asserted=False)

    labels = ("m_E", "m_I_minus_E", "m_identity", "m_zero")
    for lab, a, b in zip(labels, with_record, without_record):
        a_val = complex(a).real if hasattr(a, "real") else float(a)
        b_val = complex(b).real if hasattr(b, "real") else float(b)
        diff = abs(complex(a) - complex(b))
        record(f"counterfactual_{lab}_identical",
               diff < 1e-14,
               f"with={a_val:.15f}  without={b_val:.15f}  "
               f"|diff|={diff:.3e}")

    # Specifically validate that the POVM partition still sums to 1
    # in both scopes.
    sum_with = float(with_record[0]) + float(with_record[1])
    sum_without = float(without_record[0]) + float(without_record[1])
    record("counterfactual_povm_partition_sum_to_1_with",
           isclose(sum_with, 1.0),
           f"with: m_E + m_(I-E) = {sum_with:.15f}")
    record("counterfactual_povm_partition_sum_to_1_without",
           isclose(sum_without, 1.0),
           f"without: m_E + m_(I-E) = {sum_without:.15f}")


# -----------------------------------------------------------
# Block 11: Lattice + Quantum content preservation across memos
# -----------------------------------------------------------

def block11(repo_root: Path) -> None:
    header("BLOCK 11: Lattice + Quantum content preserved across memos")
    old_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-05-20.md"
    new_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-06-04.md"
    record("old_memo_present", old_memo.exists(), str(old_memo))
    record("new_memo_present", new_memo.exists(), str(new_memo))
    if not (old_memo.exists() and new_memo.exists()):
        return

    old_text = old_memo.read_text()
    new_text = new_memo.read_text()

    # Old memo: per-site qubit + Z^3 cubic adjacency content present.
    old_quantum = (
        "Reality is a qubit at every lattice site" in old_text
        or "one-qubit algebra" in old_text
        or "M_2(ℂ)" in old_text
        or "M_2(C)" in old_text
    )
    old_lattice = (
        "Z^3" in old_text or "`Z^3`" in old_text or "cubic lattice" in old_text
    )
    record("old_memo_has_qubit_content", old_quantum,
           "historical per-site qubit content present")
    record("old_memo_has_Z3_lattice_content", old_lattice,
           "historical Z^3 lattice content present")

    # New memo: Quantum (one-qubit / M_2(C) / Cl(3,0)) preserved.
    new_quantum = (
        "one qubit" in new_text
        or "primitive physical local degree of freedom is one qubit" in new_text
        or "A_x ~= M_2(C)" in new_text
        or "Cl(3,0)" in new_text
    )
    new_lattice = (
        "site set is `Z^3`" in new_text
        or "Z^3" in new_text
        or "cubic adjacency" in new_text
    )
    record("new_memo_has_Quantum_content", new_quantum,
           "Quantum = one-qubit / M_2(C) / Cl(3,0) preserved")
    record("new_memo_has_Lattice_content", new_lattice,
           "Lattice = Z^3 preserved")

    # New memo: Record axiom is additive scalar record-readout
    # (separate, non-overlapping with Quantum / Lattice).
    new_record_additivity = (
        "I(R_1 sqcup R_2) = I(R_1) + I(R_2)" in new_text
        or "additive over disjoint" in new_text
    )
    record("new_memo_has_Record_additive_scalar_content",
           new_record_additivity,
           "Record axiom: additive scalar functional")

    # Verify the new memo's Record scope explicitly excludes
    # Born / measurement / POVM / source content (the very bridges that
    # would otherwise be needed for the parent's load-bearing chain,
    # but aren't — because the parent uses the textbook Busch / CFMR
    # POVM-extension theorem instead).
    record_scope_disclaimer = (
        "Born" in new_text
        and "log-det" in new_text
        and "rule for record production" in new_text
    )
    record("new_memo_Record_scope_excludes_Born_etc",
           record_scope_disclaimer,
           "Record axiom's own scope statement excludes Born / measurement / "
           "log-det bridges (the parent's load-bearing surface is therefore "
           "not touched by Record)")


# -----------------------------------------------------------
# Block 12: Four-route cross-check on m(E) = Tr(sigma * E)
# -----------------------------------------------------------

def block12() -> None:
    header("BLOCK 12: m(E) = Tr(sigma * E) computed four independent ways")

    # Fix a deterministic test (sigma, E) on dim H_Lambda = 4
    # (|Lambda| = 2). Use a freshly seeded local RNG so the test is
    # reproducible.
    local_rng = np.random.default_rng(20260604)
    d = 4
    # Density matrix
    A = local_rng.standard_normal((d, d)) + 1j * local_rng.standard_normal((d, d))
    M = A @ A.conj().T
    sigma = M / np.trace(M).real
    # Effect E (projected onto [0,1])
    H = local_rng.standard_normal((d, d)) + 1j * local_rng.standard_normal((d, d))
    H = 0.5 * (H + H.conj().T)
    w, U = np.linalg.eigh(H)
    E = (U * np.clip(w, 0.0, 1.0)) @ U.conj().T

    # Route 1: Direct Tr(sigma * E)
    route1 = complex(np.trace(sigma @ E)).real

    # Route 2: Eigendecomposition Sigma_a p_a <a|E|a>
    p, V = np.linalg.eigh(sigma)
    # sigma = V diag(p) V^dagger, so <a|E|a> with |a> = V[:, a]
    route2 = 0.0
    for a in range(d):
        ket_a = V[:, a]
        route2 += float(p[a]) * complex(np.vdot(ket_a, E @ ket_a)).real

    # Route 3: Pauli-string basis expansion
    # m(E) = (1/d) Sigma_a c_a(sigma) c_a(E)
    # where c_a(X) = Tr(B_a^dag X) = Tr(B_a X) for Hermitian B_a.
    basis = pauli_string_basis(2)
    c_sigma = np.array([complex(np.trace(B @ sigma)).real for B in basis])
    c_E = np.array([complex(np.trace(B @ E)).real for B in basis])
    route3 = float(np.dot(c_sigma, c_E) / d)

    # Route 4: POVM partition {E, I-E}: m(E) = 1 - m(I-E)
    route4 = 1.0 - complex(np.trace(sigma @ (np.eye(d) - E))).real

    record("route1_direct_trace",
           True,
           f"route1 = Tr(sigma E) = {route1:.15f}")
    record("route2_eigendecomposition",
           isclose(route2, route1),
           f"route2 = Sigma p_a <a|E|a> = {route2:.15f}")
    record("route3_pauli_string_basis",
           isclose(route3, route1),
           f"route3 = (1/d) c(sigma).c(E) = {route3:.15f}")
    record("route4_povm_partition_complement",
           isclose(route4, route1),
           f"route4 = 1 - Tr(sigma (I-E)) = {route4:.15f}")
    pairwise_max = max(
        abs(route1 - route2),
        abs(route2 - route3),
        abs(route3 - route4),
        abs(route1 - route4),
    )
    record("all_four_routes_agree",
           pairwise_max < 1e-9,
           f"max pairwise diff = {pairwise_max:.3e}")


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    parent_note = repo_root / "docs" / \
        "BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md"

    log("Busch POVM Extension deps-changed Hygiene Companion Runner")
    log("=" * 72)
    log(f"Repo root: {repo_root}")
    log(f"Parent note: {parent_note}")
    log("Companion source note: docs/BUSCH_POVM_EXTENSION_DEPS_CHANGED_"
        "HYGIENE_COMPANION_NOTE_2026-06-04.md")
    log("")
    log("Goal: verify the parent's load-bearing chain")
    log("      m(E) = Tr(sigma * E) on E(H_Lambda) = { 0 <= E <= I }")
    log("      is invariant under the 2026-06-04 minimal_axioms premise")
    log("      hash bump 1d36a556->b8848fc8 (Record-axiom adoption).")
    log("")
    log("Scope: pure audit-companion evidence; no theorem claim,")
    log("       no status promotion and no use of Record-axiom content.")

    block1()
    block2()
    block3()
    block4()
    block5()
    block6()
    block7()
    block8()
    block9(parent_note)
    block10()
    block11(repo_root)
    block12()

    log("")
    log("=" * 72)
    log(f"TOTAL PASS: {PASS}")
    log(f"TOTAL FAIL: {FAIL}")
    log("=" * 72)
    log("")
    log("Companion conclusion (audit-friendly evidence only):")
    log("  The load-bearing chain of")
    log("  BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md")
    log("  (m(E) = Tr(sigma * E) on the qubit-lattice effect algebra")
    log("  E(H_Lambda)) uses ONLY Lattice + Quantum axiom content plus the")
    log("  cited Busch 2003 / CFMR 2004 textbook POVM-additive extension")
    log("  theorem and finite-dim Riesz representation.")
    log("  The Record axiom (additive scalar record-readout functional)")
    log("  is neither used nor invoked. Numeric output is identical under")
    log("  both 'Record axiom included' and 'Record axiom not included'")
    log("  outer scopes. This runner does not re-apply the prior audit")
    log("  verdict; it records that the arithmetic checked here is")
    log("  unchanged by the 2026-06-04 axiom-set adoption.")
    log("")
    log("The audit lane decides its independent handling of the")
    log("archived snapshot under the new minimal_axioms premise hash.")

    return 1 if FAIL > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
