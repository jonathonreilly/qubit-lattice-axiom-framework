"""SU(3) Wigner intertwiner engine — Block 1 of the cube-closure campaign.

Block 1 deliverable: explicit Clebsch-Gordan decomposition of the SU(3)
adjoint tensor product

    (1,1) ⊗ (1,1) = (0,0) ⊕ 2·(1,1) ⊕ (3,0) ⊕ (0,3) ⊕ (2,2)
                  = 1   ⊕ 8   ⊕ 8    ⊕ 10    ⊕ 10̄  ⊕ 27
                    (dimensions: 1 + 8 + 8 + 10 + 10 + 27 = 64 ✓)

via quadratic-Casimir + exchange + cubic-Casimir diagonalization on
V_(1,1) ⊗ V_(1,1) = C^8 ⊗ C^8.

This is Block 1 of the multi-block plan to build the full SU(3) Wigner-
Racah machinery needed for the L_s=3 cube tensor-network contraction.

Algorithm:
  1. Construct Gell-Mann basis {λ_a, a=1..8} of 3x3 traceless Hermitian
     matrices.
  2. Construct SU(3) structure constants f_abc (antisymmetric) and
     d_abc (symmetric).
  3. Construct adjoint generators T^a_(b,c) = -i f_(abc) as 8x8 matrices.
  4. Compute quadratic Casimir C_2 = Σ_a T^a T^a on the tensor product
     V_(1,1) ⊗ V_(1,1):
       C_2_total = (Σ_a (T^a ⊗ I + I ⊗ T^a)^2)
  5. Compute exchange operator E swapping the two factors of V ⊗ V.
  6. Construct C_3_total and diagonalize
       H = C_2_total + α E + β C_3_total.
  7. Construct spectral projectors for all six simultaneous
     (C_2, E, C_3) clusters.
  8. Independently reconstruct the same projectors as invariant
     polynomials in C_2, E, and C_3.

Validation:
  V1: 6 distinct fusion channels with dimensions {1, 8, 8, 10, 10, 27}.
  V2: total dimension 64.
  V3: orthonormal basis: <e_i, e_j> = δ_ij.
  V4: projectors are Hermitian, idempotent, pairwise orthogonal, complete,
      and have ranks 1,8,8,10,10,27.
  V5: each projector has the expected scalar (C_2,E,C_3) data.
  V6: the canonical cubic-Casimir convention is anchored independently on
      fundamental and antifundamental matrices.
  V7: D(g)⊗D(g) commutes with C_3 and every channel projector for multiple
      deterministic independently seeded SU(3) elements.
  V8: hostile controls reject swapped 10/10bar labels and a C_2+E-only
      rank-20 decuplet-pair projector.

Cluster note: this is SU(3) representation theory, NOT in the
gauge_vacuum_plaquette family. It is a new infrastructure deliverable
serving downstream lattice gauge work.

Forbidden imports: none (pure SU(3) rep theory).

Run:
    python3 scripts/frontier_su3_wigner_intertwiner_engine.py
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, List, Tuple

import numpy as np


OPERATOR_TOL = 1.0e-10
EIGENVALUE_TOL = 1.0e-8
EQUIVARIANCE_TOL = 1.0e-10
SU3_TEST_SEEDS = (11, 29, 47, 83, 101)


@dataclass(frozen=True)
class ChannelSpec:
    """Exact simultaneous (C2, exchange, C3) data for one 8⊗8 channel."""

    key: str
    dynkin: Tuple[int, int]
    name: str
    dimension: int
    c2: float
    exchange: float
    c3: float

    def h_eigenvalue(self, alpha: float, beta: float) -> float:
        return self.c2 + alpha * self.exchange + beta * self.c3


CHANNEL_SPECS = (
    ChannelSpec("1", (0, 0), "singlet", 1, 0.0, +1.0, 0.0),
    ChannelSpec("8_a", (1, 1), "antisymmetric adjoint", 8, 3.0, -1.0, 0.0),
    ChannelSpec("8_s", (1, 1), "symmetric adjoint", 8, 3.0, +1.0, 0.0),
    ChannelSpec("10", (3, 0), "decuplet", 10, 6.0, -1.0, +9.0),
    ChannelSpec("10bar", (0, 3), "antidecuplet", 10, 6.0, -1.0, -9.0),
    ChannelSpec("27", (2, 2), "27-plet", 27, 8.0, +1.0, 0.0),
)


# ===========================================================================
# Section A. Gell-Mann basis and SU(3) structure constants.
# ===========================================================================

def gellmann_basis() -> List[np.ndarray]:
    """SU(3) Gell-Mann matrices, normalized so Tr[λ_a λ_b] = 2 δ_(ab).

    Returns the standard 8 Gell-Mann matrices in the order:
      λ_1, λ_2, λ_3 (SU(2) sigma in upper 2x2)
      λ_4, λ_5 (off-diagonal 1-3)
      λ_6, λ_7 (off-diagonal 2-3)
      λ_8 (Cartan / hypercharge-like)
    """
    l = [None] * 8
    l[0] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    l[1] = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    l[2] = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    l[3] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    l[4] = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    l[5] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    l[6] = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    l[7] = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / math.sqrt(3)
    return l


def structure_constants() -> Tuple[np.ndarray, np.ndarray]:
    """Compute SU(3) structure constants:
      [λ_a/2, λ_b/2] = i f_abc (λ_c/2)         (antisymmetric)
      {λ_a/2, λ_b/2} = (1/3) δ_ab I + d_abc (λ_c/2)  (symmetric, traceless part)

    Returns (f_abc, d_abc) as (8, 8, 8) arrays.

    Computed numerically from the Gell-Mann basis via:
      f_abc = (1/(4i)) Tr[λ_c [λ_a, λ_b]]
      d_abc = (1/4)   Tr[λ_c {λ_a, λ_b}]
    """
    lam = gellmann_basis()
    n = 8
    f = np.zeros((n, n, n), dtype=float)
    d = np.zeros((n, n, n), dtype=float)
    for a in range(n):
        for b in range(n):
            comm = lam[a] @ lam[b] - lam[b] @ lam[a]
            anti = lam[a] @ lam[b] + lam[b] @ lam[a]
            for c in range(n):
                f_val = (1.0 / (4j)) * np.trace(lam[c] @ comm)
                d_val = (1.0 / 4.0) * np.trace(lam[c] @ anti)
                f[a, b, c] = float(f_val.real)
                d[a, b, c] = float(d_val.real)
    return f, d


# ===========================================================================
# Section B. Adjoint generators and Casimirs.
# ===========================================================================

def adjoint_generators(f: np.ndarray) -> List[np.ndarray]:
    """Adjoint representation generators T^a_(b,c) = -i f_(abc).

    Returns list of 8 Hermitian 8x8 matrices satisfying [T^a, T^b] = i f_abc T^c.
    """
    n = 8
    T = []
    for a in range(n):
        Ta = np.zeros((n, n), dtype=complex)
        for b in range(n):
            for c in range(n):
                Ta[b, c] = -1j * f[a, b, c]
        T.append(Ta)
    return T


def adjoint_casimir(T: List[np.ndarray]) -> np.ndarray:
    """Quadratic Casimir on (1,1) adjoint: C_2 = Σ_a T^a T^a.

    For SU(3) (1,1) adjoint, eigenvalue C_2 = 3 (standard convention with
    Tr[λ_a λ_b] = 2 δ_ab).
    """
    n = 8
    C = np.zeros((n, n), dtype=complex)
    for Ta in T:
        C = C + Ta @ Ta
    return C


def cubic_casimir(T: List[np.ndarray], d: np.ndarray) -> np.ndarray:
    """Cubic Casimir C_3 = Σ_(abc) d_(abc) T^a T^b T^c.

    For SU(3), C_3 takes opposite signs on conjugate irreps: e.g.,
    C_3((3,0)) = -C_3((0,3)) (decuplet vs antidecuplet).

    On self-conjugate irreps (e.g., (0,0), (1,1), (2,2)), C_3 vanishes.
    """
    n_generators = len(T)
    dim = T[0].shape[0]
    C = np.zeros((dim, dim), dtype=complex)
    for a in range(n_generators):
        for b in range(n_generators):
            for c in range(n_generators):
                if d[a, b, c] != 0:
                    C = C + d[a, b, c] * T[a] @ T[b] @ T[c]
    return C


def tensor_product_cubic_casimir(T: List[np.ndarray], d: np.ndarray
                                   ) -> np.ndarray:
    """Total cubic Casimir on V_(1,1) ⊗ V_(1,1):

      C_3_total = Σ_(abc) d_(abc) (T^a ⊗ I + I ⊗ T^a)
                                    (T^b ⊗ I + I ⊗ T^b)
                                    (T^c ⊗ I + I ⊗ T^c)

    Acts as a SU(3)-invariant operator distinguishing irreps with
    different C_3 eigenvalues.
    """
    n = 8
    I8 = np.eye(n, dtype=complex)
    # Total generators on V ⊗ V
    T_tot = [np.kron(Ta, I8) + np.kron(I8, Ta) for Ta in T]
    dim = n * n
    C = np.zeros((dim, dim), dtype=complex)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if d[a, b, c] != 0:
                    C = C + d[a, b, c] * T_tot[a] @ T_tot[b] @ T_tot[c]
    return C


def tensor_product_casimir(T: List[np.ndarray]) -> np.ndarray:
    """Total Casimir C_2 on V_(1,1) ⊗ V_(1,1):

      C_total = Σ_a (T^a ⊗ I + I ⊗ T^a)^2
              = Σ_a (T^a)^2 ⊗ I + 2 (T^a ⊗ T^a) + I ⊗ (T^a)^2
              = C ⊗ I + 2 Σ_a (T^a ⊗ T^a) + I ⊗ C

    Returns 64x64 matrix.
    """
    n = 8
    I8 = np.eye(n, dtype=complex)
    C = adjoint_casimir(T)
    # C ⊗ I + I ⊗ C
    C_total = np.kron(C, I8) + np.kron(I8, C)
    # 2 Σ_a (T^a ⊗ T^a)
    for Ta in T:
        C_total = C_total + 2.0 * np.kron(Ta, Ta)
    return C_total


def exchange_operator(dim: int) -> np.ndarray:
    """Exchange operator E on V ⊗ V swapping the two factors.

    E |i⟩ ⊗ |j⟩ = |j⟩ ⊗ |i⟩
    Matrix elements: E_(ij,kl) = δ_(i,l) δ_(j,k)
    """
    E = np.zeros((dim * dim, dim * dim), dtype=complex)
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                for l in range(dim):
                    if i == l and j == k:
                        E[i * dim + j, k * dim + l] = 1.0
    return E


# ===========================================================================
# Section C. CG decomposition via simultaneous diagonalization.
# ===========================================================================

def random_su3(seed: int = 42) -> np.ndarray:
    """Generate a random SU(3) element via QR decomposition + det adjustment."""
    rng = np.random.default_rng(seed)
    M = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    Q, R = np.linalg.qr(M)
    diag_R = np.diag(R)
    Q = Q * (diag_R / np.abs(diag_R))
    Q = Q / (np.linalg.det(Q) ** (1.0 / 3.0))
    return Q


def adjoint_matrix(g: np.ndarray, lam: List[np.ndarray]) -> np.ndarray:
    """Compute D^(1,1)(g) = (1/2) Tr[λ_a g λ_b g†]_(a,b) (8x8)."""
    g_dag = g.conj().T
    n = 8
    D = np.zeros((n, n), dtype=complex)
    for a in range(n):
        for b in range(n):
            D[a, b] = 0.5 * np.trace(lam[a] @ g @ lam[b] @ g_dag)
    return D


def cg_decomposition(C_total: np.ndarray, E: np.ndarray,
                       C3_total: np.ndarray | None = None
                       ) -> Tuple[np.ndarray, np.ndarray, Tuple[float, float]]:
    """Diagonalize H = C_2_total + α E + β C_3_total to separate all 6
    fusion channels in (1,1) ⊗ (1,1).

    Without C_3, the (3,0) and (0,3) channels (both 10-dim) have the same
    C_2 eigenvalue (=6) and the same exchange eigenvalue, forming a 20-dim
    block. C_3 distinguishes them (opposite signs since they're conjugate).

    Returns (eigenvalues, eigenvectors_basis, (alpha, beta)).
    """
    alpha = math.sqrt(2)  # irrational; lifts C_2/E degeneracy
    beta = math.sqrt(3) / 7.0  # small irrational; lifts (3,0)/(0,3) degeneracy
    H = C_total + alpha * E
    if C3_total is not None:
        H = H + beta * C3_total
    H_sym = (H + H.conj().T) / 2.0
    eigvals, eigvecs = np.linalg.eigh(H_sym)
    return eigvals, eigvecs, (alpha, beta)


def canonical_su3_casimirs(p: int, q: int) -> Tuple[Fraction, Fraction]:
    """Canonical SU(3) Casimirs for Dynkin label (p,q).

    The generators use t_a = λ_a/2, with Tr(t_a t_b) = δ_ab/2:

      C2(p,q) = (p² + q² + pq + 3p + 3q) / 3
      C3(p,q) = (p-q)(2p+q+3)(p+2q+3) / 18.

    This convention gives C3(1,0)=+10/9 and C3(3,0)=+9.
    """
    c2 = Fraction(p * p + q * q + p * q + 3 * p + 3 * q, 3)
    c3 = Fraction(
        (p - q) * (2 * p + q + 3) * (p + 2 * q + 3),
        18,
    )
    return c2, c3


def spectral_channel_projectors(
    eigvals: np.ndarray,
    eigvecs: np.ndarray,
    alpha: float,
    beta: float,
    tol: float = EIGENVALUE_TOL,
) -> Dict[str, np.ndarray]:
    """Build the six H-spectral projectors and match them to exact channels."""
    projectors: Dict[str, np.ndarray] = {}
    claimed_indices: set[int] = set()
    for spec in CHANNEL_SPECS:
        target = spec.h_eigenvalue(alpha, beta)
        indices = np.where(np.abs(eigvals - target) < tol)[0]
        if len(indices) != spec.dimension:
            raise ValueError(
                f"{spec.key}: expected {spec.dimension} H eigenvectors near "
                f"{target:.12f}, found {len(indices)}"
            )
        overlap = claimed_indices.intersection(int(i) for i in indices)
        if overlap:
            raise ValueError(f"{spec.key}: overlapping H cluster indices {overlap}")
        claimed_indices.update(int(i) for i in indices)
        basis = eigvecs[:, indices]
        projectors[spec.key] = basis @ basis.conj().T
    if len(claimed_indices) != len(eigvals):
        raise ValueError(
            f"channel matching covered {len(claimed_indices)} of {len(eigvals)} vectors"
        )
    return projectors


def lagrange_spectral_projector(
    operator: np.ndarray,
    target: float,
    spectrum: Tuple[float, ...],
) -> np.ndarray:
    """Evaluate the Lagrange polynomial selecting one exact eigenvalue."""
    ident = np.eye(operator.shape[0], dtype=complex)
    projector = ident.copy()
    for other in spectrum:
        if other == target:
            continue
        projector = projector @ ((operator - other * ident) / (target - other))
    return (projector + projector.conj().T) / 2.0


def invariant_polynomial_projectors(
    C_total: np.ndarray,
    E: np.ndarray,
    C3_total: np.ndarray,
) -> Dict[str, np.ndarray]:
    """Independent channel projectors as exact commuting-operator polynomials.

    This construction does not use H or its eigenvectors.  It uses the exact
    C2 spectrum {0,3,6,8}, exchange parity, and the C3=±9 split inside C2=6.
    """
    ident = np.eye(C_total.shape[0], dtype=complex)
    c2_spectrum = (0.0, 3.0, 6.0, 8.0)
    p_c2 = {
        value: lagrange_spectral_projector(C_total, value, c2_spectrum)
        for value in c2_spectrum
    }
    p_sym = (ident + E) / 2.0
    p_asym = (ident - E) / 2.0
    p_c3_plus = (ident + C3_total / 9.0) / 2.0
    p_c3_minus = (ident - C3_total / 9.0) / 2.0
    raw = {
        "1": p_c2[0.0] @ p_sym,
        "8_a": p_c2[3.0] @ p_asym,
        "8_s": p_c2[3.0] @ p_sym,
        "10": p_c2[6.0] @ p_asym @ p_c3_plus,
        "10bar": p_c2[6.0] @ p_asym @ p_c3_minus,
        "27": p_c2[8.0] @ p_sym,
    }
    return {
        key: (projector + projector.conj().T) / 2.0
        for key, projector in raw.items()
    }


def observed_scalar(
    projector: np.ndarray,
    operator: np.ndarray,
    dimension: int,
) -> Tuple[float, float]:
    """Return the block trace-average and scalar-action residual."""
    scalar = float(np.real(np.trace(projector @ operator)) / dimension)
    residual = float(np.max(np.abs(operator @ projector - scalar * projector)))
    return scalar, residual


def expected_su3_casimirs() -> Dict[Tuple[int, int], float]:
    """Standard SU(3) Casimir eigenvalues C_2((p,q)) = (p^2 + q^2 + pq)/3 + p + q.

    With the normalization Tr[λ_a λ_b] = 2 δ_(ab), the Casimir
    eigenvalues for irreps are:
      C_2((0,0)) = 0
      C_2((1,0)) = 4/3
      C_2((1,1)) = 3
      C_2((3,0)) = 6
      C_2((0,3)) = 6
      C_2((2,2)) = 8
    """
    return {(p, q): float(canonical_su3_casimirs(p, q)[0])
            for p in range(5) for q in range(5)}


# ===========================================================================
# Section D. Driver + validation.
# ===========================================================================

def driver() -> int:
    print("=" * 78)
    print("SU(3) Wigner Intertwiner Engine — Block 1: (1,1) ⊗ (1,1) CG")
    print("=" * 78)
    print()

    pass_count = 0
    fail_count = 0

    def record(label: str, passed: bool) -> None:
        nonlocal pass_count, fail_count
        marker = "PASS" if passed else "FAIL"
        print(f"  {marker}: {label}")
        if passed:
            pass_count += 1
        else:
            fail_count += 1

    # ===== Section A: build basis + structure constants =====
    print("--- Section A: Gell-Mann basis + structure constants ---")
    lam = gellmann_basis()
    f, d = structure_constants()
    f_asym = max(
        float(np.max(np.abs(f + np.transpose(f, axes))))
        for axes in ((1, 0, 2), (2, 1, 0), (0, 2, 1))
    )
    d_sym = max(
        float(np.max(np.abs(d - np.transpose(d, axes))))
        for axes in ((1, 0, 2), (2, 1, 0), (0, 2, 1))
    )
    print(f"  f antisymmetry error: {f_asym:.3e}")
    print(f"  d symmetry error:     {d_sym:.3e}")
    expected_f = {(0, 1, 2): 1.0,
                  (2, 3, 4): 0.5,  # f_345 = 1/2
                  (3, 4, 7): math.sqrt(3) / 2.0}  # f_458 = sqrt(3)/2
    max_standard_delta = 0.0
    print("  Standard structure constant values:")
    for (a, b, c), expected in expected_f.items():
        actual = f[a, b, c]
        delta = abs(actual - expected)
        max_standard_delta = max(max_standard_delta, delta)
        marker = "OK" if delta < 1e-10 else "BAD"
        print(f"    f[{a+1}{b+1}{c+1}] = {actual:.6f}  (expected {expected:.6f})  [{marker}]")
    record(
        "structure constants have the required permutation symmetries and normalization.",
        f_asym < OPERATOR_TOL
        and d_sym < OPERATOR_TOL
        and max_standard_delta < OPERATOR_TOL,
    )
    print()

    # ===== Section B: adjoint generators + Casimir =====
    print("--- Section B: adjoint generators + canonical Casimir convention ---")
    T = adjoint_generators(f)
    herm_errors = max(np.max(np.abs(Ta - Ta.conj().T)) for Ta in T)
    comm_errors = 0.0
    for a in range(8):
        for b in range(8):
            comm = T[a] @ T[b] - T[b] @ T[a]
            expected = sum(1j * f[a, b, c] * T[c] for c in range(8))
            comm_errors = max(comm_errors, np.max(np.abs(comm - expected)))
    print(f"  T^a Hermiticity error:       {herm_errors:.3e}")
    print(f"  Lie algebra commutator error: {comm_errors:.3e}")
    record(
        "adjoint generators are Hermitian and satisfy [T^a,T^b]=i f_abc T^c.",
        herm_errors < OPERATOR_TOL and comm_errors < OPERATOR_TOL,
    )

    C2_adj = adjoint_casimir(T)
    eigvals_C2 = np.linalg.eigvalsh((C2_adj + C2_adj.conj().T) / 2.0)
    c2_adj_err = float(np.max(np.abs(eigvals_C2 - 3.0)))
    c3_adj = cubic_casimir(T, d)
    c3_adj_err = float(np.max(np.abs(c3_adj)))
    print(f"  C_2((1,1)) scalar error from 3: {c2_adj_err:.3e}")
    print(f"  C_3((1,1)) scalar error from 0: {c3_adj_err:.3e}")
    record(
        "adjoint Casimirs match C2(1,1)=3 and C3(1,1)=0.",
        c2_adj_err < OPERATOR_TOL and c3_adj_err < OPERATOR_TOL,
    )
    print()

    print("  Independent cubic-Casimir sign anchor:")
    fundamental = [matrix / 2.0 for matrix in lam]
    antifundamental = [-matrix.conj() for matrix in fundamental]
    c2_fund = sum(matrix @ matrix for matrix in fundamental)
    c2_antifund = sum(matrix @ matrix for matrix in antifundamental)
    c3_fund = cubic_casimir(fundamental, d)
    c3_antifund = cubic_casimir(antifundamental, d)
    c2_10, c3_10 = canonical_su3_casimirs(3, 0)
    c2_10bar, c3_10bar = canonical_su3_casimirs(0, 3)
    formula_err = max(
        float(np.max(np.abs(c2_fund - (4.0 / 3.0) * np.eye(3)))),
        float(np.max(np.abs(c2_antifund - (4.0 / 3.0) * np.eye(3)))),
        float(np.max(np.abs(c3_fund - (10.0 / 9.0) * np.eye(3)))),
        float(np.max(np.abs(c3_antifund + (10.0 / 9.0) * np.eye(3)))),
    )
    print("    Formula: C3(p,q)=(p-q)(2p+q+3)(p+2q+3)/18")
    print("    direct fundamental matrices:     C3(1,0)  = +10/9")
    print("    direct antifundamental matrices: C3(0,1)  = -10/9")
    print(f"    formula decuplet:     (C2,C3)=({c2_10},{c3_10})")
    print(f"    formula antidecuplet: (C2,C3)=({c2_10bar},{c3_10bar})")
    record(
        "fundamental matrices anchor the formula sign, so (3,0) has C3=+9 and (0,3) has C3=-9.",
        formula_err < OPERATOR_TOL
        and c2_10 == 6
        and c2_10bar == 6
        and c3_10 == 9
        and c3_10bar == -9,
    )
    print()

    # ===== Section C: tensor product commuting operators =====
    print("--- Section C: tensor-product commuting operators ---")
    C_total = tensor_product_casimir(T)
    E = exchange_operator(8)
    C3_total = tensor_product_cubic_casimir(T, d)
    ident64 = np.eye(64, dtype=complex)
    hermitian_err = max(
        float(np.max(np.abs(operator - operator.conj().T)))
        for operator in (C_total, E, C3_total)
    )
    e_err = float(np.max(np.abs(E @ E - ident64)))
    operator_comm_err = max(
        float(np.max(np.abs(C_total @ E - E @ C_total))),
        float(np.max(np.abs(C_total @ C3_total - C3_total @ C_total))),
        float(np.max(np.abs(E @ C3_total - C3_total @ E))),
    )
    print(f"  max Hermiticity error:             {hermitian_err:.3e}")
    print(f"  exchange involution ||E²-I||_max:  {e_err:.3e}")
    print(f"  max pairwise commutator error:      {operator_comm_err:.3e}")
    record(
        "C2, exchange, and C3 are numerically Hermitian commuting operators with E²=I.",
        hermitian_err < OPERATOR_TOL
        and e_err < OPERATOR_TOL
        and operator_comm_err < OPERATOR_TOL,
    )
    print()

    # ===== Section D: CG decomposition via diagonalization =====
    print("--- Section D: CG decomposition via simultaneous diagonalization ---")
    eigvals, eigvecs, (alpha, beta) = cg_decomposition(C_total, E, C3_total)
    projectors = spectral_channel_projectors(eigvals, eigvecs, alpha, beta)
    print("  Diagonalizing H = C_2_total + α E + β C_3_total")
    print(f"  α = sqrt(2) = {alpha:.6f}, β = sqrt(3)/7 = {beta:.6f}")
    overlap = eigvecs.conj().T @ eigvecs
    overlap_err = float(np.max(np.abs(overlap - ident64)))
    actual_pattern = sorted(spec.dimension for spec in CHANNEL_SPECS)
    expected_pattern = [1, 8, 8, 10, 10, 27]
    print(f"  six matched dimensions: {actual_pattern}; total={sum(actual_pattern)}")
    print(f"  eigensolver orthonormality ||V†V-I||_max: {overlap_err:.3e}")
    record(
        "floating-point H spectrum has six separated clusters with ranks 1,8,8,10,10,27.",
        actual_pattern == expected_pattern and sum(actual_pattern) == 64,
    )
    record(
        "the returned floating-point CG eigenbasis is orthonormal within tolerance.",
        overlap_err < OPERATOR_TOL,
    )
    print()

    # ===== Section E: executable six-channel identification =====
    print("--- Section E: simultaneous-channel spectral projectors ---")
    max_projector_herm = 0.0
    max_projector_idem = 0.0
    max_scalar_residual = 0.0
    computed_ranks = []
    observed_c3: Dict[str, float] = {}
    for spec in sorted(CHANNEL_SPECS, key=lambda item: item.h_eigenvalue(alpha, beta)):
        projector = projectors[spec.key]
        rank = int(np.linalg.matrix_rank(projector, tol=EIGENVALUE_TOL))
        computed_ranks.append(rank)
        herm_err = float(np.max(np.abs(projector - projector.conj().T)))
        idem_err = float(np.max(np.abs(projector @ projector - projector)))
        c2_obs, c2_res = observed_scalar(projector, C_total, spec.dimension)
        e_obs, e_res = observed_scalar(projector, E, spec.dimension)
        c3_obs, c3_res = observed_scalar(projector, C3_total, spec.dimension)
        observed_c3[spec.key] = c3_obs
        expected_residual = max(
            float(np.max(np.abs(C_total @ projector - spec.c2 * projector))),
            float(np.max(np.abs(E @ projector - spec.exchange * projector))),
            float(np.max(np.abs(C3_total @ projector - spec.c3 * projector))),
        )
        max_projector_herm = max(max_projector_herm, herm_err)
        max_projector_idem = max(max_projector_idem, idem_err)
        max_scalar_residual = max(
            max_scalar_residual,
            c2_res,
            e_res,
            c3_res,
            expected_residual,
        )
        h_observed = c2_obs + alpha * e_obs + beta * c3_obs
        print(
            f"  {spec.key:>5} ({spec.dynkin[0]},{spec.dynkin[1]}) "
            f"rank={rank:>2}: H={h_observed: .7f}, "
            f"observed (C2,E,C3)=({c2_obs: .8f},{e_obs:+.8f},{c3_obs:+.8f}); "
            f"expected=({spec.c2:g},{spec.exchange:+g},{spec.c3:+g})"
        )
    record(
        "all six spectral projectors are Hermitian, idempotent, have the expected ranks, and carry the expected scalar (C2,E,C3) data.",
        sorted(computed_ranks) == expected_pattern
        and max_projector_herm < OPERATOR_TOL
        and max_projector_idem < OPERATOR_TOL
        and max_scalar_residual < OPERATOR_TOL,
    )

    pairwise_orth_err = 0.0
    for i, left in enumerate(CHANNEL_SPECS):
        for right in CHANNEL_SPECS[i + 1:]:
            pairwise_orth_err = max(
                pairwise_orth_err,
                float(np.max(np.abs(projectors[left.key] @ projectors[right.key]))),
            )
    completeness_err = float(
        np.max(
            np.abs(
                sum((projectors[spec.key] for spec in CHANNEL_SPECS), np.zeros_like(E))
                - ident64
            )
        )
    )
    print(f"  max pairwise projector product: {pairwise_orth_err:.3e}")
    print(f"  completeness ||ΣP-I||_max:      {completeness_err:.3e}")
    record(
        "the six projectors are pairwise orthogonal and complete.",
        pairwise_orth_err < OPERATOR_TOL and completeness_err < OPERATOR_TOL,
    )
    print()

    # ===== Section F: independent invariant-polynomial construction =====
    print("--- Section F: independent invariant-polynomial projectors ---")
    polynomial_projectors = invariant_polynomial_projectors(C_total, E, C3_total)
    polynomial_match_err = max(
        float(np.max(np.abs(polynomial_projectors[spec.key] - projectors[spec.key])))
        for spec in CHANNEL_SPECS
    )
    polynomial_complete_err = float(
        np.max(
            np.abs(
                sum(
                    (polynomial_projectors[spec.key] for spec in CHANNEL_SPECS),
                    np.zeros_like(E),
                )
                - ident64
            )
        )
    )
    print(f"  max |P_polynomial-P_eigensolver|: {polynomial_match_err:.3e}")
    print(f"  polynomial completeness error:    {polynomial_complete_err:.3e}")
    record(
        "independent commuting-operator polynomials reproduce all six eigensolver projectors.",
        polynomial_match_err < OPERATOR_TOL
        and polynomial_complete_err < OPERATOR_TOL,
    )
    print()

    # ===== Section G: hostile controls =====
    print("--- Section G: hostile controls ---")
    swapped_10_error = abs(observed_c3["10"] - (-9.0))
    swapped_10bar_error = abs(observed_c3["10bar"] - (+9.0))
    coarse_eigvals, coarse_eigvecs, _ = cg_decomposition(C_total, E, None)
    coarse_target = 6.0 - alpha
    coarse_indices = np.where(np.abs(coarse_eigvals - coarse_target) < EIGENVALUE_TOL)[0]
    coarse_basis = coarse_eigvecs[:, coarse_indices]
    coarse_projector = coarse_basis @ coarse_basis.conj().T
    coarse_rank = int(np.linalg.matrix_rank(coarse_projector, tol=EIGENVALUE_TOL))
    coarse_c3_eigenvalues = np.linalg.eigvalsh(
        (coarse_basis.conj().T @ C3_total @ coarse_basis
         + (coarse_basis.conj().T @ C3_total @ coarse_basis).conj().T)
        / 2.0
    )
    coarse_unique_clusters = len(set(np.round(coarse_eigvals, 8)))
    coarse_c3_min = float(np.min(coarse_c3_eigenvalues))
    coarse_c3_max = float(np.max(coarse_c3_eigenvalues))
    print(
        "  old swapped-label residuals: "
        f"10→C3=-9 gives {swapped_10_error:.1f}; "
        f"10bar→C3=+9 gives {swapped_10bar_error:.1f}"
    )
    print(
        "  C2+E-only decuplet projector: "
        f"rank={coarse_rank}, C3 range=[{coarse_c3_min:.8f},{coarse_c3_max:.8f}], "
        f"total clusters={coarse_unique_clusters}"
    )
    record(
        "hostile controls reject the old swapped labels and reject C2+E as a six-channel identifier.",
        swapped_10_error > 17.0
        and swapped_10bar_error > 17.0
        and coarse_rank == 20
        and abs(coarse_c3_min + 9.0) < OPERATOR_TOL
        and abs(coarse_c3_max - 9.0) < OPERATOR_TOL
        and coarse_unique_clusters == 5,
    )
    print()

    # ===== Section H: deterministic numerical equivariance witnesses =====
    print("--- Section H: deterministic SU(3) equivariance witnesses ---")
    max_group_definition_err = 0.0
    max_operator_equivariance_err = 0.0
    max_projector_equivariance_err = 0.0
    for seed in SU3_TEST_SEEDS:
        g = random_su3(seed=seed)
        group_err = max(
            float(np.max(np.abs(g.conj().T @ g - np.eye(3)))),
            abs(np.linalg.det(g) - 1.0),
        )
        D = adjoint_matrix(g, lam)
        DD = np.kron(D, D)
        c2_comm = float(np.max(np.abs(DD @ C_total - C_total @ DD)))
        e_comm = float(np.max(np.abs(DD @ E - E @ DD)))
        c3_comm = float(np.max(np.abs(DD @ C3_total - C3_total @ DD)))
        channel_comm = {
            spec.key: float(
                np.max(np.abs(DD @ projectors[spec.key] - projectors[spec.key] @ DD))
            )
            for spec in CHANNEL_SPECS
        }
        max_group_definition_err = max(max_group_definition_err, group_err)
        max_operator_equivariance_err = max(
            max_operator_equivariance_err, c2_comm, e_comm, c3_comm
        )
        max_projector_equivariance_err = max(
            max_projector_equivariance_err, *channel_comm.values()
        )
        channel_text = " ".join(
            f"{spec.key}={channel_comm[spec.key]:.2e}" for spec in CHANNEL_SPECS
        )
        print(
            f"  seed={seed:>3}: C2={c2_comm:.2e} E={e_comm:.2e} "
            f"C3={c3_comm:.2e}; {channel_text}"
        )
    record(
        "five independently seeded deterministic SU(3) samples commute with C2, E, C3, and every channel projector within the explicit tolerance.",
        max_group_definition_err < EQUIVARIANCE_TOL
        and max_operator_equivariance_err < EQUIVARIANCE_TOL
        and max_projector_equivariance_err < EQUIVARIANCE_TOL,
    )
    print(f"  equivariance tolerance: {EQUIVARIANCE_TOL:.1e}")
    print(
        "  Boundary: these are finite floating-point implementation witnesses; "
        "the all-g statement follows analytically from Casimir invariance, "
        "factor-swap invariance, and spectral-polynomial functional calculus."
    )
    print()

    # ===== Summary =====
    print("=" * 78)
    print(f"SUMMARY: THEOREM PASS={pass_count} FAIL={fail_count}")
    print("=" * 78)
    print()
    print("Headline:")
    print(f"  SU(3) (1,1) ⊗ (1,1) decomposed into {len(CHANNEL_SPECS)} fusion channels")
    print(f"  with dimensions {actual_pattern} = {sum(actual_pattern)} total.")
    print("  Correct cubic convention: 10=(3,0) has C3=+9 and H≈6.8127;")
    print("                            10bar=(0,3) has C3=-9 and H≈2.3589.")
    print()
    print("Block 1 deliverable: six executable spectral projectors plus a")
    print("floating-point orthonormal CG basis. Exact block invariance is supplied")
    print("by the analytic commuting-operator identities, not by numerical precision.")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(driver())
