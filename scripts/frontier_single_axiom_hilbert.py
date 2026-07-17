#!/usr/bin/env python3
"""Scope-narrowed operational checks for a local tensor-product Hilbert packet.

This runner verifies consequences after four explicit conditions are supplied:

1. local factor dimensions;
2. a Hermitian Hamiltonian with stipulated local support;
3. the Born p=2 readout;
4. the rule that Hamiltonian support on factors defines graph edges.

It does not derive those inputs from a bare Hilbert-space axiom, reduce the
current framework axiom ledger, or prove a monotone graph-distance decay law.
Test 4's valid support is the participation-ratio/spread contrast between a
supplied chain-local Hamiltonian and a dense nonlocal control on the same
factorized Hilbert space and normalized computational-basis outcome space. The
two generators are
centered and matched to the same RMS energy before propagation.

PStack experiment: single-axiom-hilbert
"""

from __future__ import annotations

import math
import time
import sys

import numpy as np

try:
    from scipy import sparse
    from scipy.sparse.linalg import expm_multiply
    from scipy.linalg import expm
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False


# ============================================================================
# Utilities
# ============================================================================

def kron_list(ops: list[np.ndarray]) -> np.ndarray:
    """Tensor product of a list of operators."""
    result = ops[0]
    for op in ops[1:]:
        result = np.kron(result, op)
    return result


def random_hermitian(d: int, rng: np.random.Generator) -> np.ndarray:
    """Random d x d Hermitian matrix."""
    A = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    return (A + A.conj().T) / 2.0


def random_local_hamiltonian(n_sites: int, d: int, edges: list[tuple[int, int]],
                              rng: np.random.Generator,
                              coupling_strength: float = 1.0) -> np.ndarray:
    """Build a Hamiltonian on n_sites qudits (dimension d) with given interaction edges.

    H = sum_{(i,j) in edges} h_ij  (random 2-local terms)
    + sum_i h_i  (random 1-local terms)
    """
    D = d ** n_sites
    H = np.zeros((D, D), dtype=complex)
    I_d = np.eye(d)

    # Single-site terms
    for i in range(n_sites):
        h_local = random_hermitian(d, rng) * 0.5
        ops = [I_d] * n_sites
        ops[i] = h_local
        H += kron_list(ops)

    # Two-site interaction terms
    for (i, j) in edges:
        # Random interaction on sites i, j
        h_pair = random_hermitian(d * d, rng) * coupling_strength
        # Embed into full space
        # Build by acting on sites i and j
        ops_list = []
        for row in range(d * d):
            for col in range(d * d):
                if abs(h_pair[row, col]) < 1e-15:
                    continue
                ri, rj = divmod(row, d)
                ci, cj = divmod(col, d)
                ops = [I_d] * n_sites
                site_op_i = np.zeros((d, d), dtype=complex)
                site_op_i[ri, ci] = 1.0
                site_op_j = np.zeros((d, d), dtype=complex)
                site_op_j[rj, cj] = 1.0
                ops[i] = site_op_i
                ops[j] = site_op_j
                H += h_pair[row, col] * kron_list(ops)

    return H


def match_centered_rms_energy(
    H: np.ndarray, target_rms_energy: float = 1.0
) -> tuple[np.ndarray, float]:
    """Remove the global energy origin and match the RMS generator scale.

    For dimension ``D``, the centered RMS energy is

        sqrt(Tr(H_c^dagger H_c) / D),
        H_c = H - Tr(H) I / D.

    The trace shift changes only the propagator's global phase.  Dividing by
    this RMS energy gives local and dense Hamiltonians the same typical
    dimensionless evolution scale without matching either matrix entrywise.
    """
    D = H.shape[0]
    if H.shape != (D, D):
        raise ValueError("Hamiltonian must be square")
    if target_rms_energy <= 0.0:
        raise ValueError("target_rms_energy must be positive")

    hermiticity_residual = np.linalg.norm(H - H.conj().T, ord="fro")
    if hermiticity_residual > 1e-10:
        raise ValueError(f"Hamiltonian is not Hermitian: residual={hermiticity_residual}")

    H_centered = H - (np.trace(H) / D) * np.eye(D, dtype=complex)
    rms_energy = float(np.linalg.norm(H_centered, ord="fro") / np.sqrt(D))
    if not np.isfinite(rms_energy) or rms_energy <= 0.0:
        raise ValueError("Hamiltonian has no finite nonzero centered RMS energy")

    return H_centered * (target_rms_energy / rms_energy), rms_energy


def normalized_basis_probabilities(
    H: np.ndarray, source_state: np.ndarray, t: float
) -> tuple[np.ndarray, float]:
    """Propagate and return one normalized distribution over basis outcomes."""
    amplitudes = expm(-1j * H * t) @ source_state
    probabilities = np.abs(amplitudes) ** 2
    total = float(np.sum(probabilities))
    normalization_error = abs(total - 1.0)
    if normalization_error > 1e-10:
        raise ValueError(f"Unitary outcome probabilities are not normalized: sum={total}")
    return probabilities / total, normalization_error


def participation_ratio(probabilities: np.ndarray) -> float:
    """Effective number of populated mutually exclusive outcomes."""
    if probabilities.ndim != 1:
        raise ValueError("Participation-ratio input must be one-dimensional")
    if np.min(probabilities) < -1e-15:
        raise ValueError("Participation-ratio input contains negative probabilities")
    if abs(float(np.sum(probabilities)) - 1.0) > 1e-10:
        raise ValueError("Participation-ratio input must be normalized")
    return float(1.0 / np.sum(probabilities ** 2))


# ============================================================================
# Test 1: Derive the graph from the Hamiltonian's tensor product support
# ============================================================================

def extract_interaction_graph(H: np.ndarray, n_sites: int, d: int,
                               threshold: float = 1e-6) -> set[tuple[int, int]]:
    """Extract which pairs of sites interact by examining the Hamiltonian.

    Uses operator decomposition: expand H in a product basis of local operators.
    If any coefficient involves non-identity operators on both sites i and j,
    then (i,j) is an edge.
    """
    D = d ** n_sites
    I_d = np.eye(d, dtype=complex)
    edges = set()

    # Build a basis of traceless Hermitian operators for each site
    # (generalized Pauli matrices). Together with I/sqrt(d), these form
    # an orthonormal basis under Tr(A^dag B) / d.
    local_basis = _hermitian_basis(d)  # includes identity as first element

    for si in range(n_sites):
        for sj in range(si + 1, n_sites):
            # Check if H has any component acting non-trivially on BOTH si and sj
            has_interaction = _check_two_site_interaction_v2(
                H, n_sites, d, si, sj, local_basis, threshold)
            if has_interaction:
                edges.add((si, sj))

    return edges


def _hermitian_basis(d: int) -> list[np.ndarray]:
    """Orthonormal Hermitian basis for d x d matrices under Tr(A^dag B)."""
    basis = [np.eye(d, dtype=complex) / np.sqrt(d)]

    # Off-diagonal symmetric
    for i in range(d):
        for j in range(i + 1, d):
            M = np.zeros((d, d), dtype=complex)
            M[i, j] = 1.0
            M[j, i] = 1.0
            basis.append(M / np.sqrt(2))

    # Off-diagonal antisymmetric
    for i in range(d):
        for j in range(i + 1, d):
            M = np.zeros((d, d), dtype=complex)
            M[i, j] = -1j
            M[j, i] = 1j
            basis.append(M / np.sqrt(2))

    # Diagonal traceless
    for k in range(1, d):
        M = np.zeros((d, d), dtype=complex)
        for i in range(k):
            M[i, i] = 1.0
        M[k, k] = -k
        M /= np.sqrt(k * (k + 1))
        basis.append(M)

    return basis


def _check_two_site_interaction_v2(H: np.ndarray, n_sites: int, d: int,
                                    site_i: int, site_j: int,
                                    local_basis: list[np.ndarray],
                                    threshold: float) -> bool:
    """Check if H has a genuine 2-site interaction between site_i and site_j.

    Compute coefficient c_{ab} = Tr(H * (... x sigma_a^{(i)} x ... x sigma_b^{(j)} x ...))
    where all other sites get identity. If any c_{ab} with a >= 1 AND b >= 1 is nonzero,
    there's a 2-site interaction.
    """
    D = d ** n_sites
    I_d = np.eye(d, dtype=complex)
    n_basis = len(local_basis)

    interaction_norm_sq = 0.0

    # Only check non-identity x non-identity components
    for a in range(1, n_basis):
        for b in range(1, n_basis):
            # Build the full operator: I x ... x sigma_a^(i) x ... x sigma_b^(j) x ... x I
            ops = [I_d / np.sqrt(d)] * n_sites  # normalized identity on each site
            ops[site_i] = local_basis[a]
            ops[site_j] = local_basis[b]
            full_op = kron_list(ops)

            # Coefficient
            coeff = np.trace(H @ full_op)
            interaction_norm_sq += abs(coeff) ** 2

    return np.sqrt(interaction_norm_sq) > threshold


def test_graph_emergence():
    """Test 1: recover the supplied support graph."""
    print("=" * 70)
    print("TEST 1: Graph support recovery under the supplied extraction rule")
    print("=" * 70)

    rng = np.random.default_rng(42)
    results = []

    for trial in range(5):
        n_sites = 5
        d = 2  # qubits

        # Random graph on 5 sites (subset of all edges)
        all_edges = [(i, j) for i in range(n_sites) for j in range(i+1, n_sites)]
        n_edges = rng.integers(3, len(all_edges) + 1)
        chosen_indices = rng.choice(len(all_edges), size=n_edges, replace=False)
        input_edges = set(all_edges[k] for k in chosen_indices)

        # Build Hamiltonian with exactly these edges
        H = random_local_hamiltonian(n_sites, d, list(input_edges), rng)

        # Extract graph from Hamiltonian
        recovered_edges = extract_interaction_graph(H, n_sites, d)

        match = (input_edges == recovered_edges)
        results.append(match)

        print(f"  Trial {trial+1}: {len(input_edges)} input edges, "
              f"{len(recovered_edges)} recovered, match={match}")
        if not match:
            missing = input_edges - recovered_edges
            extra = recovered_edges - input_edges
            if missing:
                print(f"    Missing: {missing}")
            if extra:
                print(f"    Extra: {extra}")

    success_rate = sum(results) / len(results)
    print(f"\n  Graph recovery rate: {success_rate:.0%} ({sum(results)}/{len(results)})")
    print(f"  PASS: graph support is recovered under the supplied extraction rule" if success_rate == 1.0
          else f"  PARTIAL: {success_rate:.0%} exact recovery")
    return success_rate


# ============================================================================
# Test 2: supplied Born p=2 readout gives I_3 = 0.
# ============================================================================

def compute_I3_hilbert(dim: int, n_trials: int, rng: np.random.Generator) -> list[float]:
    """Compute third-order interference I_3 in standard Hilbert space.

    For a 3-slit experiment: I_3 = P_123 - P_12 - P_13 - P_23 + P_1 + P_2 + P_3
    In quantum mechanics with Born rule, I_3 = 0 identically.
    """
    I3_values = []
    for _ in range(n_trials):
        # Random state in dim-dimensional Hilbert space
        psi = rng.standard_normal(dim) + 1j * rng.standard_normal(dim)
        psi /= np.linalg.norm(psi)

        # Random detection state
        phi = rng.standard_normal(dim) + 1j * rng.standard_normal(dim)
        phi /= np.linalg.norm(phi)

        # Three orthogonal slits (projectors onto subspaces)
        # Use first 3 basis vectors as slit projectors
        P = [np.zeros((dim, dim), dtype=complex) for _ in range(3)]
        for k in range(3):
            if k < dim:
                e = np.zeros(dim, dtype=complex)
                e[k] = 1.0
                P[k] = np.outer(e, e.conj())

        # Probabilities: P_S = |<phi|P_S|psi>|^2 where P_S = sum of projectors in S
        def prob(projectors):
            P_total = sum(projectors)
            amplitude = phi.conj() @ P_total @ psi
            return abs(amplitude) ** 2

        P_123 = prob([P[0], P[1], P[2]])
        P_12 = prob([P[0], P[1]])
        P_13 = prob([P[0], P[2]])
        P_23 = prob([P[1], P[2]])
        P_1 = prob([P[0]])
        P_2 = prob([P[1]])
        P_3 = prob([P[2]])

        I3 = P_123 - P_12 - P_13 - P_23 + P_1 + P_2 + P_3
        I3_values.append(abs(I3))

    return I3_values


def compute_I3_pnorm(p: float, dim: int, n_trials: int,
                      rng: np.random.Generator) -> list[float]:
    """Compute I_3 analog in a p-norm probability theory.

    In standard QM, probability = |amplitude|^2 (p=2).
    For p != 2, define probability = |amplitude|^p / normalization.
    This violates the Born rule and generically gives I_3 != 0.
    """
    I3_values = []
    for _ in range(n_trials):
        psi = rng.standard_normal(dim) + 1j * rng.standard_normal(dim)
        psi /= np.linalg.norm(psi)

        phi = rng.standard_normal(dim) + 1j * rng.standard_normal(dim)
        phi /= np.linalg.norm(phi)

        P = [np.zeros((dim, dim), dtype=complex) for _ in range(3)]
        for k in range(3):
            if k < dim:
                e = np.zeros(dim, dtype=complex)
                e[k] = 1.0
                P[k] = np.outer(e, e.conj())

        def prob_p(projectors):
            P_total = sum(projectors)
            amplitude = phi.conj() @ P_total @ psi
            return abs(amplitude) ** p

        P_123 = prob_p([P[0], P[1], P[2]])
        P_12 = prob_p([P[0], P[1]])
        P_13 = prob_p([P[0], P[2]])
        P_23 = prob_p([P[1], P[2]])
        P_1 = prob_p([P[0]])
        P_2 = prob_p([P[1]])
        P_3 = prob_p([P[2]])

        I3 = P_123 - P_12 - P_13 - P_23 + P_1 + P_2 + P_3
        I3_values.append(abs(I3))

    return I3_values


def test_born_rule():
    """Test 2: Born p=2 readout and three tested nonquadratic controls."""
    print("\n" + "=" * 70)
    print("TEST 2: Born p=2 readout gives I_3 = 0; tested nonquadratic controls are nonzero")
    print("=" * 70)

    rng = np.random.default_rng(123)
    dim = 8
    n_trials = 200

    # Hilbert space (p=2): I_3 should be zero
    I3_hilbert = compute_I3_hilbert(dim, n_trials, rng)
    mean_hilbert = np.mean(I3_hilbert)
    max_hilbert = np.max(I3_hilbert)

    print(f"\n  Hilbert space (Born rule, p=2):")
    print(f"    mean |I_3| = {mean_hilbert:.2e}")
    print(f"    max  |I_3| = {max_hilbert:.2e}")
    print(f"    {'PASS' if max_hilbert < 1e-10 else 'FAIL'}: I_3 = 0 to machine precision")

    # p-norm theories: I_3 should be nonzero
    print(f"\n  Non-Hilbert p-norm theories:")
    p_values = [1.5, 3.0, 4.0]
    p_norm_results = {}
    for p in p_values:
        I3_p = compute_I3_pnorm(p, dim, n_trials, rng)
        mean_p = np.mean(I3_p)
        max_p = np.max(I3_p)
        p_norm_results[p] = mean_p
        nonzero = mean_p > 1e-6
        print(f"    p={p:.1f}: mean |I_3| = {mean_p:.4e}, max = {max_p:.4e}  "
              f"{'PASS (nonzero)' if nonzero else 'unexpected zero'}")

    all_nonzero = all(v > 1e-6 for v in p_norm_results.values())
    born_auto = max_hilbert < 1e-10

    print(f"\n  Summary: supplied Born p=2 readout gives I_3 = 0: {born_auto}")
    print(f"  Summary: tested p in {{1.5, 3, 4}} gives nonzero sampled I_3: {all_nonzero}")
    return born_auto and all_nonzero


# ============================================================================
# Test 3: Hermitian/unitary toy evolution versus fixed dephasing control.
# ============================================================================

def propagator_unitary(H: np.ndarray, source: int, t: float) -> np.ndarray:
    """Compute propagator G(i, source) = <i|e^{-iHt}|source> (unitary)."""
    D = H.shape[0]
    psi0 = np.zeros(D, dtype=complex)
    psi0[source] = 1.0
    U = expm(-1j * H * t)
    return U @ psi0


def propagator_lindblad(H: np.ndarray, source: int, t: float,
                         gamma: float, n_steps: int = 50) -> np.ndarray:
    """Compute propagator under Lindblad (non-unitary) evolution.

    drho/dt = -i[H, rho] + gamma * sum_k (L_k rho L_k^dag - {L_k^dag L_k, rho}/2)

    Uses simple Euler integration of the master equation.
    Returns diagonal of rho (probabilities at each site).
    """
    D = H.shape[0]
    rho = np.zeros((D, D), dtype=complex)
    rho[source, source] = 1.0

    dt = t / n_steps

    # Lindblad operators: dephasing in computational basis
    L_ops = []
    for k in range(D):
        L = np.zeros((D, D), dtype=complex)
        L[k, k] = 1.0
        L_ops.append(L)

    for _ in range(n_steps):
        # Hamiltonian part
        comm = -1j * (H @ rho - rho @ H)

        # Lindblad dissipator
        dissipator = np.zeros_like(rho)
        for L in L_ops:
            Ld = L.conj().T
            LdL = Ld @ L
            dissipator += gamma * (L @ rho @ Ld - 0.5 * (LdL @ rho + rho @ LdL))

        rho += dt * (comm + dissipator)

        # Ensure trace preservation
        rho /= np.trace(rho)

    return np.real(np.diag(rho))


def test_unitarity():
    """Test 3: Hermitian/unitary evolution versus fixed dephasing control."""
    print("\n" + "=" * 70)
    print("TEST 3: Hermitian generator is unitary; fixed strong-dephasing control changes the profile")
    print("=" * 70)

    if not HAS_SCIPY:
        print("  SKIP: scipy required")
        return False

    rng = np.random.default_rng(77)

    # 1D chain with 8 sites, nearest-neighbor hopping
    n_sites = 8
    H = np.zeros((n_sites, n_sites), dtype=complex)
    for i in range(n_sites - 1):
        H[i, i+1] = -1.0
        H[i+1, i] = -1.0

    # Add a "gravitational" potential (1/r from center)
    center = n_sites // 2
    for i in range(n_sites):
        r = abs(i - center)
        if r > 0:
            H[i, i] = -0.5 / r  # attractive potential

    source = 0
    t = 2.0

    # Unitary propagator
    G_unitary = propagator_unitary(H, source, t)
    prob_unitary = np.abs(G_unitary) ** 2

    # Check unitarity: probabilities sum to 1
    norm_unitary = np.sum(prob_unitary)
    print(f"\n  Unitary evolution:")
    print(f"    Probability conservation: sum = {norm_unitary:.10f}")
    print(f"    Probability profile: [{', '.join(f'{p:.4f}' for p in prob_unitary)}]")

    # Check gravitational attraction: more probability near center
    attracted = prob_unitary[center] > prob_unitary[0] + prob_unitary[-1]
    print(f"    Probability at center > edges: {attracted}")

    # Lindblad (non-unitary) propagator at various damping rates
    print(f"\n  Lindblad dephasing control (non-unitary open-system evolution):")
    gammas = [0.0, 0.1, 0.5, 1.0, 2.0]
    for gamma in gammas:
        prob_lindblad = propagator_lindblad(H, source, t, gamma, n_steps=200)
        norm_l = np.sum(prob_lindblad)
        center_excess = prob_lindblad[center] - (prob_lindblad[0] + prob_lindblad[-1]) / 2

        print(f"    gamma={gamma:.1f}: norm={norm_l:.4f}, "
              f"center_excess={center_excess:+.4f}, "
              f"profile=[{', '.join(f'{p:.3f}' for p in prob_lindblad)}]")

    # Key test: at strong damping, the particle localizes at the source,
    # not at the toy attraction center.
    prob_strong = propagator_lindblad(H, source, t, gamma=2.0, n_steps=200)
    attraction_works_unitary = prob_unitary[center] > prob_unitary[source]
    attraction_broken_lindblad = prob_strong[source] > prob_strong[center]

    print(f"\n  Unitary: probability migrates toward toy attraction center: "
          f"{attraction_works_unitary}")
    print(f"  Fixed gamma=2 control: source probability > toy-center probability: "
          f"{attraction_broken_lindblad}")
    probability_conserved = abs(norm_unitary - 1.0) < 1e-10
    passed = (
        probability_conserved
        and attraction_works_unitary
        and attraction_broken_lindblad
    )
    print("  PASS: fixed unitary/strong-dephasing toy contrast" if passed
          else "  FAIL: fixed unitary/strong-dephasing control semantics")

    return passed


# ============================================================================
# Test 4: matched-scale local-H versus dense-control localization support.
# ============================================================================

def test_matched_scale_localization():
    """Test 4: local support gives a bounded fixed-seed localization contrast.

    Compare:
    (a) the factorized space H_space = H_1 x H_2 x ... x H_N with a
        chain-local Hamiltonian;
    (b) the same factorized 64-dimensional space with a dense random
        Hamiltonian that does not respect the chain-local support restriction.

    Both propagators start from the same state, use centered generators with
    identical RMS energy, and are represented by normalized distributions on
    the same 64 mutually exclusive computational-basis outcomes.  The pass
    criterion retains the existing 2x participation-ratio contrast.  No
    monotone graph-distance claim is made.
    """
    print("\n" + "=" * 70)
    print("TEST 4: Matched-scale local H gives bounded localization support")
    print("=" * 70)

    if not HAS_SCIPY:
        print("  SKIP: scipy required")
        return False

    rng = np.random.default_rng(999)

    # --- (a) Tensor product space: 1D chain of 6 qubits ---
    n_sites = 6
    d = 2
    D = d ** n_sites  # 64-dimensional

    # Local Hamiltonian on 1D chain
    edges_chain = [(i, i+1) for i in range(n_sites - 1)]
    H_local_raw = random_local_hamiltonian(
        n_sites, d, edges_chain, rng, coupling_strength=0.5
    )

    # Dense control on the same C^64 outcome space.  It shares the supplied
    # factor labels for a like-for-like readout, but not the chain-local
    # Hamiltonian support restriction.
    H_dense_raw = random_hermitian(D, rng)

    target_rms_energy = 1.0
    H_local, local_rms_before = match_centered_rms_energy(
        H_local_raw, target_rms_energy
    )
    H_dense, dense_rms_before = match_centered_rms_energy(
        H_dense_raw, target_rms_energy
    )
    local_rms_after = float(np.linalg.norm(H_local, ord="fro") / np.sqrt(D))
    dense_rms_after = float(np.linalg.norm(H_dense, ord="fro") / np.sqrt(D))

    # Same initial outcome and same dimensionless evolution time.
    source_state = np.zeros(D, dtype=complex)
    source_state[0] = 1.0  # |000000>
    t = 1.0
    probs_local, local_normalization_error = normalized_basis_probabilities(
        H_local, source_state, t
    )
    probs_dense, dense_normalization_error = normalized_basis_probabilities(
        H_dense, source_state, t
    )

    print("\n  Common comparison contract:")
    print(f"    Outcome space: {D} mutually exclusive computational-basis outcomes")
    print(f"    Initial state: |{'0' * n_sites}>; dimensionless time: {t:.1f}")
    print(
        "    Centered RMS energy before matching: "
        f"local={local_rms_before:.6f}, dense={dense_rms_before:.6f}"
    )
    print(
        "    Centered RMS energy after matching:  "
        f"local={local_rms_after:.12f}, dense={dense_rms_after:.12f}"
    )
    print(
        "    Probability normalization error:    "
        f"local={local_normalization_error:.3e}, dense={dense_normalization_error:.3e}"
    )

    # PR = 1 / sum_z p(z)^2 on the same normalized 64-outcome space.
    PR_local = participation_ratio(probs_local)
    PR_dense = participation_ratio(probs_dense)

    print("\n  Participation ratio on the common outcome space:")
    print(f"    Chain-local Hamiltonian: PR = {PR_local:.4f} / {D} outcomes")
    print(f"    Dense nonlocal control:  PR = {PR_dense:.4f} / {D} outcomes")

    # --- Summary ---
    same_outcome_space = probs_local.shape == probs_dense.shape == (D,)
    normalized = max(local_normalization_error, dense_normalization_error) < 1e-10
    scale_matched = max(
        abs(local_rms_after - target_rms_energy),
        abs(dense_rms_after - target_rms_energy),
        abs(local_rms_after - dense_rms_after),
    ) < 1e-12
    spread_ratio = PR_dense / PR_local
    contrast_pass = spread_ratio > 2.0
    passed = same_outcome_space and normalized and scale_matched and contrast_pass

    print(f"\n  Spread ratio (dense/local): {spread_ratio:.4f}x")
    print(f"  Same 64-outcome space: {same_outcome_space}")
    print(f"  Both distributions normalized: {normalized}")
    print(f"  Centered RMS energies matched: {scale_matched}")
    print(f"  Existing >2x spread criterion: {contrast_pass}")
    print("  PASS: bounded matched-scale localization contrast" if passed
          else "  FAIL: common-space matched-scale localization contract")

    return passed


# ============================================================================
# Synthesis: explicit-condition operational support.
# ============================================================================

def synthesis(t1: float, t2: bool, t3: bool, t4: bool):
    """Print the explicit-condition synthesis of all four tests."""
    print("\n" + "=" * 70)
    print("SYNTHESIS: What the explicit-condition packet supports")
    print("=" * 70)

    print(f"""
  Supplied packet:
    local factor dimensions + Hermitian local H + Born p=2 readout
    + support-as-edges extraction rule

  Test 1 — Support graph recovered:            {'PASS' if t1 == 1.0 else 'PARTIAL'}
    The adjacency graph is recovered from the supplied Hamiltonian support
    under the supplied extraction rule.

  Test 2 — Born p=2 readout check:              {'PASS' if t2 else 'FAIL'}
    I_3 = 0 under the supplied p=2 readout.
    The tested p in {{1.5, 3, 4}} controls give nonzero sampled I_3.

  Test 3 — Hermitian/unitary control:           {'PASS' if t3 else 'FAIL'}
    The supplied Hermitian H gives unitary evolution; the fixed gamma=2
    dephasing control leaves more probability at the source than at the center.

  Test 4 — Bounded localization contrast:       {'PASS' if t4 else 'FAIL'}
    On the same normalized 64-outcome space and at matched centered RMS
    energy, the supplied chain-local H is less spread than a dense nonlocal
    control. The fixed sample does not prove monotone graph-distance decay.

  Conclusion:
    The runner supports the bounded operational consequences of the explicit
    conditions. It does not derive the local Hamiltonian, locality restriction,
    Born readout, or support-as-edges rule from a bare Hilbert-space axiom,
    and it does not reduce the current framework axiom ledger.
""")


# ============================================================================
# Main
# ============================================================================

def main() -> int:
    print("SCOPE-NARROWED LOCAL TENSOR PRODUCT HILBERT SUPPORT")
    print("Bounded operational checks under explicit conditions.\n")

    t0 = time.time()

    t1 = test_graph_emergence()
    t2 = test_born_rule()
    t3 = test_unitarity()
    t4 = test_matched_scale_localization()

    synthesis(t1, t2, t3, t4)

    elapsed = time.time() - t0
    print(f"Total runtime: {elapsed:.1f}s")
    all_pass = t1 == 1.0 and t2 and t3 and t4
    print(f"OVERALL: {'PASS' if all_pass else 'FAIL'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
