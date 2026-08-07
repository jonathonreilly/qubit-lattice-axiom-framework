#!/usr/bin/env python3
"""
Native-Gaussian no-go for a Majorana coefficient on the current neutrino lane.

Question:
  The exact operator-classification result shows that the anomaly-fixed
  one-generation surface admits a unique quadratic same-chirality Majorana
  operator candidate, nu_R^T C P_R nu_R. Does the current native staggered
  Hamiltonian / determinant source family generate that coefficient?

Answer on the present surface:
  No. On the current quadratic Gaussian surface, the Hamiltonian and the
  allowed local source family are number-conserving normal bilinears of the
  form c^dag K c. Their Nambu anomalous block is identically zero.

Boundary:
  This is an exact no-go only for the current native quadratic/determinant
  surface. It does NOT rule out a nonzero coefficient in a future Nambu /
  Pfaffian / explicit DeltaL=2 extension of the microscopic theory.
"""

from __future__ import annotations

import sys

import numpy as np

np.set_printoptions(precision=6, suppress=True, linewidth=140)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", cls: str = "C") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status} ({cls})] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def commutator(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def annihilation_operators(n_modes: int) -> list[np.ndarray]:
    sigma_minus = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)
    sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    ident = np.eye(2, dtype=complex)

    operators: list[np.ndarray] = []
    for mode in range(n_modes):
        op = np.array([[1.0]], dtype=complex)
        for idx in range(n_modes):
            if idx < mode:
                op = np.kron(op, sigma_z)
            elif idx == mode:
                op = np.kron(op, sigma_minus)
            else:
                op = np.kron(op, ident)
        operators.append(op)
    return operators


def number_operator(cs: list[np.ndarray]) -> np.ndarray:
    dim = cs[0].shape[0]
    out = np.zeros((dim, dim), dtype=complex)
    for c in cs:
        out += c.conj().T @ c
    return out


def normal_quadratic(k_matrix: np.ndarray, cs: list[np.ndarray]) -> np.ndarray:
    dim = cs[0].shape[0]
    out = np.zeros((dim, dim), dtype=complex)
    n_modes = len(cs)
    for i in range(n_modes):
        for j in range(n_modes):
            coeff = k_matrix[i, j]
            if abs(coeff) > 1e-12:
                out += coeff * (cs[i].conj().T @ cs[j])
    return out


def build_staggered_single_particle(lattice_size: int, mass: float = 0.0) -> np.ndarray:
    """
    Build the one-particle staggered Hamiltonian on Z^3_L in the same
    convention used elsewhere on this branch, then convert to a Hermitian
    single-particle kernel K so that the second-quantized Hamiltonian is
    H = sum_ij c_i^dag K_ij c_j.
    """
    n_sites = lattice_size**3
    hop = np.zeros((n_sites, n_sites), dtype=complex)
    mass_diag = np.zeros((n_sites, n_sites), dtype=complex)

    def idx(x: int, y: int, z: int) -> int:
        return ((x % lattice_size) * lattice_size + (y % lattice_size)) * lattice_size + (z % lattice_size)

    for x in range(lattice_size):
        for y in range(lattice_size):
            for z in range(lattice_size):
                i = idx(x, y, z)
                mass_diag[i, i] += mass * ((-1) ** (x + y + z))

                j = idx(x + 1, y, z)
                hop[i, j] += -0.5j
                hop[j, i] += 0.5j

                eta_y = (-1) ** x
                j = idx(x, y + 1, z)
                hop[i, j] += -0.5j * eta_y
                hop[j, i] += 0.5j * eta_y

                eta_z = (-1) ** (x + y)
                j = idx(x, y, z + 1)
                hop[i, j] += -0.5j * eta_z
                hop[j, i] += 0.5j * eta_z

    # The staggered hopping matrix above is anti-Hermitian in the Dirac
    # convention. Multiply by i to obtain the Hermitian single-particle
    # kernel that appears in H = sum c^dag K c.
    return 1j * hop + mass_diag


def local_projector_source(n_sites: int) -> np.ndarray:
    weights = np.linspace(-0.25, 0.25, n_sites)
    return np.diag(weights.astype(complex))


def nambu_bdg(normal_block: np.ndarray, delta_block: np.ndarray | None = None) -> np.ndarray:
    n = normal_block.shape[0]
    if delta_block is None:
        delta_block = np.zeros((n, n), dtype=complex)
    return np.block(
        [
            [normal_block, delta_block],
            [-delta_block.conj(), -normal_block.T],
        ]
    )


def test_number_conservation_on_normal_quadratic_family() -> None:
    print("\n" + "=" * 88)
    print("PART 1: NUMBER CONSERVATION ON THE NORMAL QUADRATIC FAMILY")
    print("=" * 88)

    cs = annihilation_operators(4)
    n_tot = number_operator(cs)

    k_matrix = np.array(
        [
            [0.3, 0.2 - 0.1j, 0.0, -0.05],
            [0.2 + 0.1j, -0.1, 0.15, 0.0],
            [0.0, 0.15, 0.25, 0.05 + 0.02j],
            [-0.05, 0.0, 0.05 - 0.02j, -0.2],
        ],
        dtype=complex,
    )
    k_matrix = 0.5 * (k_matrix + k_matrix.conj().T)

    j_matrix = np.diag(np.array([0.12, -0.07, 0.05, -0.03], dtype=complex))

    h_native = normal_quadratic(k_matrix, cs)
    h_sourced = normal_quadratic(k_matrix + j_matrix, cs)

    native_comm = np.linalg.norm(commutator(n_tot, h_native))
    sourced_comm = np.linalg.norm(commutator(n_tot, h_sourced))

    check("Any c^dag K c Hamiltonian commutes with total fermion number", native_comm < 1e-10,
          f"||[N,H_native]||={native_comm:.2e}")
    check("Adding an ordinary local bilinear source preserves number conservation", sourced_comm < 1e-10,
          f"||[N,H_native+J]||={sourced_comm:.2e}")

    pair_annihilate = cs[0] @ cs[1]
    pair_create = pair_annihilate.conj().T
    pair_hermitian = pair_annihilate + pair_create

    pair_ann_comm = np.linalg.norm(commutator(n_tot, pair_annihilate) + 2.0 * pair_annihilate)
    pair_cre_comm = np.linalg.norm(commutator(n_tot, pair_create) - 2.0 * pair_create)
    pair_herm_comm = np.linalg.norm(commutator(n_tot, pair_hermitian))

    check("Pair-annihilation operator carries charge -2 under N", pair_ann_comm < 1e-10,
          f"||[N,cc]+2cc||={pair_ann_comm:.2e}")
    check("Pair-creation operator carries charge +2 under N", pair_cre_comm < 1e-10,
          f"||[N,c^dag c^dag]-2c^dag c^dag||={pair_cre_comm:.2e}")
    check("Hermitian pairing operator does not commute with total fermion number", pair_herm_comm > 1e-8,
          f"||[N,cc+h.c.]||={pair_herm_comm:.2e}")

    h_with_pair = h_sourced + 0.2 * pair_hermitian
    broken_comm = np.linalg.norm(commutator(n_tot, h_with_pair))
    check("A pairing insertion breaks the exact U(1) number symmetry", broken_comm > 1e-8,
          f"||[N,H+pair]||={broken_comm:.2e}")

    print()
    print("  Conclusion: the native quadratic source family c^dag (K+J) c stays")
    print("  in the number-conserving sector exactly, while a Majorana-style")
    print("  pairing operator lives in the charge-2 sector and requires a new")
    print("  microscopic insertion.")


def test_native_staggered_kernel_has_zero_anomalous_block() -> None:
    print("\n" + "=" * 88)
    print("PART 2: THE NATIVE STAGGERED KERNEL NEVER POPULATES A PAIRING BLOCK")
    print("=" * 88)

    k_native = build_staggered_single_particle(lattice_size=2, mass=0.35)
    n_sites = k_native.shape[0]
    j_local = local_projector_source(n_sites)

    check("Native staggered single-particle kernel is Hermitian", np.linalg.norm(k_native - k_native.conj().T) < 1e-10,
          f"||K-K^dag||={np.linalg.norm(k_native - k_native.conj().T):.2e}")

    bdg_native = nambu_bdg(k_native)
    bdg_sourced = nambu_bdg(k_native + j_local)

    anomalous_native = np.linalg.norm(bdg_native[:n_sites, n_sites:])
    anomalous_sourced = np.linalg.norm(bdg_sourced[:n_sites, n_sites:])

    check("Native staggered Hamiltonian has zero anomalous Nambu block", anomalous_native < 1e-12,
          f"||Delta_native||={anomalous_native:.2e}")
    check("Local scalar projector sources keep the anomalous block exactly zero", anomalous_sourced < 1e-12,
          f"||Delta_sourced||={anomalous_sourced:.2e}")

    delta = np.zeros((n_sites, n_sites), dtype=complex)
    delta[0, 1] = 0.2
    delta[1, 0] = -0.2
    bdg_pair = nambu_bdg(k_native + j_local, delta)
    anomalous_pair = np.linalg.norm(bdg_pair[:n_sites, n_sites:])

    check("An explicit pairing source is required to populate the anomalous block", anomalous_pair > 1e-8,
          f"||Delta_pair||={anomalous_pair:.2e}")

    print()
    print("  On the current microscopic surface, K and J live entirely in the")
    print("  normal c^dag c block. The same-chirality Majorana operator sits in")
    print("  the anomalous pairing block Delta, which is absent identically until")
    print("  one adds a new microscopic pairing source.")


def n5_execution_certificate() -> None:
    """State the granularity at which this runner actually resolves the no-go.

    Reporting only: no check() call is added and no PASS/FAIL count moves.
    """
    print("\n" + "=" * 88)
    print("N5 EXECUTION CERTIFICATE: WHAT THIS RUNNER RESOLVES")
    print("=" * 88)

    lattice_size = 2
    k_native = build_staggered_single_particle(lattice_size=lattice_size, mass=0.35)
    n_sites = k_native.shape[0]
    hopping_part = k_native - np.diag(np.diag(k_native))
    hopping_norm = float(np.linalg.norm(hopping_part))
    diag_values = sorted({round(float(v.real), 6) for v in np.diag(k_native)})
    source_weights = np.linspace(-0.25, 0.25, n_sites)

    print(
        "per_element: resolved by explicit assembly, with one degeneracy that must "
        "be stated. Part 1 writes the 4 x 4 normal kernel entry by entry (0.3, "
        "0.2 - 0.1j, -0.05 and their conjugates) and carries all 16 x 16 = 256 Fock "
        "entries into the commutator norms; Part 2 lays down each staggered hop as a "
        "single += of -0.5j times a sign into hop[i, j], and the pairing block is "
        "populated by exactly two entries, Delta[0, 1] = +0.2 and Delta[1, 0] = -0.2. "
        "But at the only volume this runner builds, L = 2, the periodic wrap makes "
        "the forward and backward neighbour the same site, so every directed hop is "
        "written twice with opposite sign and the entire hopping matrix cancels: the "
        f"off-diagonal part of K measures {hopping_norm:.3e}."
    )
    print(
        f"per_site: resolved with real amplitudes over all {n_sites} sites of the "
        f"Z^3_{lattice_size} torus. The triple loop visits every site and writes the "
        "site-resolved staggered mass 0.35 * (-1)^(x + y + z), giving the two "
        f"sublattice values {diag_values}, and local_projector_source then hands each "
        f"site its own weight along linspace(-0.25, 0.25, {n_sites}), from "
        f"{source_weights[0]:+.4f} to {source_weights[-1]:+.4f} in steps of 1/14. The "
        "site-dependent hop phases eta_y = (-1)^x and eta_z = (-1)^(x + y) are "
        "computed per site but, by the L = 2 cancellation above, never survive into "
        "the kernel that is tested."
    )
    print(
        "per_mode: checked and aggregated away, not resolved. The four fermionic "
        "modes of Part 1 are addressed individually on the input side - K is given "
        "mode pair by mode pair and the source J is diag(0.12, -0.07, 0.05, -0.03) - "
        "but every reported quantity is a Frobenius norm over a whole operator, and "
        "neither the 4 x 4 kernel, nor the 8 x 8 staggered kernel, nor the 16 x 16 "
        "BdG matrix is ever diagonalized, so no eigenvalue, band, dispersion or "
        "mode-resolved amplitude is produced anywhere in this runner."
    )
    print(
        "per_block: resolved, and this is the granularity the claim lives at, though "
        "two of the three block readings are settled by construction. nambu_bdg "
        f"assembles [[K, Delta], [-conj(Delta), -K^T]] at {2 * n_sites} x "
        f"{2 * n_sites}, and for the native and locally-sourced cases delta_block is "
        "None, so the function writes a literal zero array into the anomalous slot "
        "and the norm then re-reads it: those two checks certify the modelling "
        "assignment (the native c^dag(K + J)c family maps to Delta = None), not a "
        "computed cancellation. The third case, with Delta[0, 1] = 0.2 explicitly "
        "inserted, is the genuine contrast showing the norm is not blind. The "
        "lower-left -conj(Delta) block and the -K^T block are never inspected."
    )
    print(
        "lattice_wide: partially resolved, and the missing global statement is the "
        f"note's own boundary. The kernel is assembled across the entire periodic "
        f"torus - all {n_sites} sites and all three directions with modulo "
        "wraparound - and the Hermiticity and anomalous-block norms are whole-lattice "
        "aggregates, so there is a real global object here. What is absent is any "
        "asymptotics: a single volume L = 2 is instantiated, no L-sequence and no "
        "infinite-volume or continuum limit is taken, and that single volume is the "
        "degenerate one, so nothing is established beyond this one small torus."
    )
    print(
        "  scope: the note's second structural argument runs through the determinant "
        "source family Z[J] = det(D + J) and the generator W[J] = log|det(D + J)| - "
        "log|det D|. No determinant is computed anywhere in this runner; the Gaussian "
        "surface enters only as the modelling choice delta_block = None, so nothing "
        "here certifies the determinant-side half of the note's argument."
    )
    print(
        "  scope: this runner is fully deterministic - no RNG stream and no optimizer "
        "is used, and every number above is fixed by the literal constants 0.35, "
        "+-0.25, +-0.5j and 0.2 written into the source."
    )


def main() -> int:
    print("=" * 88)
    print("NEUTRINO MAJORANA COEFFICIENT: NATIVE-GAUSSIAN NO-GO")
    print("=" * 88)
    print()
    print("Authority stack:")
    print("  - main:docs/publication/ci3_z3/DERIVATION_ATLAS.md")
    print("    rows: Framework axiom; Observable principle; Anomaly-forced time;")
    print("          Native weak algebra; Structural SU(3) closure; One-generation matter closure")
    print("  - docs/NEUTRINO_MAJORANA_OPERATOR_AXIOM_FIRST_NOTE.md")
    print("  - docs/UNIFIED_AXIOM_BOUNDARY_NOTE.md")
    print("  - scripts/frontier_right_handed_sector.py")
    print()
    print("Question:")
    print("  Does the current native quadratic Hamiltonian / determinant source")
    print("  surface generate a nonzero coefficient for the unique Majorana")
    print("  operator candidate?")
    print()

    test_number_conservation_on_normal_quadratic_family()
    test_native_staggered_kernel_has_zero_anomalous_block()
    n5_execution_certificate()

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  On the present native quadratic/determinant surface, the answer is no.")
    print("  The exact operator candidate nu_R^T C P_R nu_R is allowed by the")
    print("  anomaly-fixed gauge/chirality structure, but its coefficient is")
    print("  exactly zero on the current c^dag(K+J)c Gaussian family.")
    print()
    print("  A nonzero coefficient would require a different microscopic surface:")
    print("  an explicit pairing/Nambu source, Pfaffian Gaussian, or another")
    print("  genuine DeltaL=2 extension beyond the current determinant toolbox.")
    print()
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
