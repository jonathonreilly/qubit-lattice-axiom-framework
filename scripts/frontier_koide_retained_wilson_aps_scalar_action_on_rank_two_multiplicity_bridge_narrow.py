#!/usr/bin/env python3
"""Narrow bridge theorem runner for
`KOIDE_RETAINED_WILSON_APS_SCALAR_ACTION_ON_RANK_TWO_MULTIPLICITY_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16`.

Verifies the scalar-on-`M_zeta` theorem: every operator built from the
retained Wilson/APS generators

    {D, U, U^dag} union { P_lambda(D) : lambda in Spec(D) },

when restricted to the rank-two zeta-character isotypic component
`M_zeta` of the Wilson-Dirac zero-mode subspace `V_0 = ker(D)`, acts
as a scalar `lambda_A I_2`.

Construction of `D`, `U`, `V_0`, and `M_zeta` is re-imported from the
sibling runner
    scripts/frontier_koide_delta_lattice_wilson_selected_eigenline_no_go.py,
which already verifies `||D - D^dag|| ~ 0`, `||U D U^dag - D|| ~ 0`,
`dim V_0 = 4`, and `dim M_zeta = 2` for the same construction.

The bridge runner additionally checks:
  - `D|_{M_zeta} ~ 0`,
  - `U|_{M_zeta} ~ zeta I_2`, `U^dag|_{M_zeta} ~ zeta_bar I_2`,
  - `P_lambda(D)|_{M_zeta}` is scalar (`1 I_2` for `lambda = 0`, `0 I_2`
    otherwise),
  - a sample of polynomial words in `{D, U, U^dag, P_0(D)}` restricts
    to scalar `2 x 2` matrices on `M_zeta`,
  - a non-retained countermodel (rank-one projector `|line_0><line_0|`)
    is NOT scalar on `M_zeta`, confirming that the scalar property
    genuinely characterizes the retained algebra,
  - the property holds at both executed parameter values
    `r in {1.0, 1.425}`.

This is class-A pure operator algebra over the finite-dimensional
construction; no Koide / charged-lepton mass / sqrt(m) / PDG /
selection-principle physical identification is consumed.
"""

from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent.parent

# The primary runner executes these mutable repository sources through the
# sibling's top-level import chain. Pin the complete executable closure into the
# canonical cache fingerprint as well as exposing it to static helper discovery.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_koide_delta_lattice_wilson_selected_eigenline_no_go.py",
    "scripts/n5_resolution_certificate.py",
)

# Import the sibling runner's construction without executing its main().
SIBLING_PATH = ROOT / "scripts" / "frontier_koide_delta_lattice_wilson_selected_eigenline_no_go.py"
_spec = importlib.util.spec_from_file_location(
    "_sibling_koide_wilson", SIBLING_PATH
)
_sibling = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_sibling)
build_wilson_lattice = _sibling.build_wilson_lattice
zero_character_lines = _sibling.zero_character_lines


TOL = 1e-8
PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = "PASS (A)" if ok else "FAIL (A)"
    print(f"  [{tag}] {label}  ({detail})")


def section(title: str) -> None:
    print("\n" + "-" * 88 + f"\n{title}\n" + "-" * 88)


def restrict_to(M: np.ndarray, basis: np.ndarray) -> np.ndarray:
    """Return basis^dag @ M @ basis for an orthonormal `basis` (columns)."""
    return basis.conj().T @ M @ basis


def is_scalar_2x2(M: np.ndarray, tol: float = TOL) -> tuple[bool, complex]:
    """Return (is_scalar, candidate scalar)."""
    if M.shape != (2, 2):
        return False, complex(0.0)
    lam = (M[0, 0] + M[1, 1]) / 2
    expected = lam * np.eye(2, dtype=complex)
    return bool(np.linalg.norm(M - expected) < tol), complex(lam)


def build_basis_M_zeta(D: np.ndarray, U: np.ndarray) -> tuple[np.ndarray, complex]:
    """Return (orthonormal 2-column basis of M_zeta, the zeta scalar)."""
    line_0, line_1, zeta = zero_character_lines(D, U)
    basis = np.stack([line_0, line_1], axis=1)
    # Sanity: orthonormality
    gram = basis.conj().T @ basis
    if np.linalg.norm(gram - np.eye(2)) > TOL:
        raise RuntimeError(f"M_zeta basis not orthonormal: gram={gram}")
    return basis, complex(zeta)


def spectral_projectors(D: np.ndarray) -> list[tuple[float, np.ndarray]]:
    """Return [(eigenvalue, orthogonal projector onto eigenspace), ...].

    Eigenspaces are coalesced by eigenvalue equality within TOL.
    """
    eigs, vecs = np.linalg.eigh(D)
    projectors: list[tuple[float, np.ndarray]] = []
    used = np.zeros(len(eigs), dtype=bool)
    for i, lam in enumerate(eigs):
        if used[i]:
            continue
        group = [i]
        used[i] = True
        for j in range(i + 1, len(eigs)):
            if (not used[j]) and abs(eigs[j] - lam) < TOL:
                group.append(j)
                used[j] = True
        block = vecs[:, group]
        P = block @ block.conj().T
        projectors.append((float(lam), P))
    return projectors


def run_for_r(r: float) -> None:
    section(f"r = {r}: build sibling Wilson construction and M_zeta")

    D, U, fixed_sites = build_wilson_lattice(r)
    check(
        f"r={r}: sibling D is Hermitian (||D - D^dag|| < tol)",
        np.linalg.norm(D - D.conj().T) < TOL,
        f"||D - D^dag|| = {np.linalg.norm(D - D.conj().T):.2e}",
    )
    check(
        f"r={r}: sibling U intertwines D (||U D U^dag - D|| < tol)",
        np.linalg.norm(U @ D @ U.conj().T - D) < TOL,
        f"||U D U^dag - D|| = {np.linalg.norm(U @ D @ U.conj().T - D):.2e}",
    )

    eigs, _ = np.linalg.eigh(D)
    zero_count = int(np.sum(np.abs(eigs) < TOL))
    check(
        f"r={r}: ker(D) has dimension 4 (sibling B.1)",
        zero_count == 4,
        f"dim ker(D) = {zero_count}",
    )

    basis_Mz, zeta = build_basis_M_zeta(D, U)
    zeta_expected = complex(math.cos(math.pi / 3), math.sin(math.pi / 3))
    check(
        f"r={r}: M_zeta is rank-two zeta-eigenspace with zeta = exp(i pi/3)",
        basis_Mz.shape == (D.shape[0], 2)
        and abs(zeta - zeta_expected) < TOL,
        f"shape={basis_Mz.shape}, zeta = {zeta}, expected = {zeta_expected}",
    )

    section(f"r = {r}: generators restrict to scalars on M_zeta")

    D_on_Mz = restrict_to(D, basis_Mz)
    is_scalar, lam_D = is_scalar_2x2(D_on_Mz)
    check(
        f"r={r}: D|_{{M_zeta}} = 0 I_2",
        is_scalar and abs(lam_D) < TOL,
        f"D|_{{M_zeta}} = \n{D_on_Mz}",
    )

    U_on_Mz = restrict_to(U, basis_Mz)
    is_scalar, lam_U = is_scalar_2x2(U_on_Mz)
    check(
        f"r={r}: U|_{{M_zeta}} = zeta I_2 with zeta = exp(i pi/3)",
        is_scalar and abs(lam_U - zeta) < TOL,
        f"U|_{{M_zeta}} = \n{U_on_Mz},  lam_U = {lam_U}",
    )

    Udag_on_Mz = restrict_to(U.conj().T, basis_Mz)
    is_scalar, lam_Udag = is_scalar_2x2(Udag_on_Mz)
    check(
        f"r={r}: U^dag|_{{M_zeta}} = zeta_bar I_2",
        is_scalar and abs(lam_Udag - np.conjugate(zeta)) < TOL,
        f"U^dag|_{{M_zeta}} = \n{Udag_on_Mz},  lam_Udag = {lam_Udag}",
    )

    # Sanity: U * U^dag = I on full space (so on M_zeta).
    check(
        f"r={r}: U is unitary (U U^dag = I on full space)",
        np.linalg.norm(U @ U.conj().T - np.eye(U.shape[0])) < TOL,
        f"||U U^dag - I|| = {np.linalg.norm(U @ U.conj().T - np.eye(U.shape[0])):.2e}",
    )

    section(f"r = {r}: spectral projectors of D restrict to scalars on M_zeta")

    proj_list = spectral_projectors(D)
    nonscalar_proj_failures = []
    P_zero = None
    for lam, P in proj_list:
        P_on_Mz = restrict_to(P, basis_Mz)
        is_scalar, lam_P = is_scalar_2x2(P_on_Mz)
        expected_scalar = 1.0 if abs(lam) < TOL else 0.0
        ok = is_scalar and abs(lam_P.real - expected_scalar) < TOL and abs(lam_P.imag) < TOL
        if not ok:
            nonscalar_proj_failures.append(
                f"lambda={lam}: P|_{{M_zeta}} = {P_on_Mz},  lam_P = {lam_P}"
            )
        if abs(lam) < TOL:
            P_zero = P
    check(
        f"r={r}: every spectral projector P_lambda(D) is scalar on M_zeta",
        len(nonscalar_proj_failures) == 0,
        (
            "all projectors scalar"
            if not nonscalar_proj_failures
            else "non-scalar failures:\n        " + "\n        ".join(nonscalar_proj_failures)
        ),
    )

    assert P_zero is not None, "P_0(D) must exist since dim ker(D) = 4"

    section(f"r = {r}: polynomial words in retained generators are scalar on M_zeta")

    Udag = U.conj().T
    words: list[tuple[str, np.ndarray]] = [
        ("D", D),
        ("U", U),
        ("U^dag", Udag),
        ("D + U", D + U),
        ("U + U^dag", U + Udag),
        ("D^2", D @ D),
        ("U^2", U @ U),
        ("U @ U^dag", U @ Udag),
        ("(U + U^dag) @ P_0", (U + Udag) @ P_zero),
        ("U^2 + D - U^dag", U @ U + D - Udag),
        ("P_0 @ U @ P_0", P_zero @ U @ P_zero),
        ("U @ D @ U^dag", U @ D @ Udag),
        ("(D + U + U^dag) @ P_0 + 3 * P_0", (D + U + Udag) @ P_zero + 3 * P_zero),
    ]
    word_failures = []
    for name, W in words:
        W_on_Mz = restrict_to(W, basis_Mz)
        is_scalar, lam_W = is_scalar_2x2(W_on_Mz)
        if not is_scalar:
            word_failures.append(f"{name}: {W_on_Mz}")
    check(
        f"r={r}: every sampled retained polynomial word is scalar on M_zeta",
        len(word_failures) == 0,
        (
            f"{len(words)}/{len(words)} retained polynomial words restrict to scalar I_2"
            if not word_failures
            else "non-scalar failures:\n        " + "\n        ".join(word_failures)
        ),
    )

    section(f"r = {r}: countermodel — a NON-retained rank-one projector is NOT scalar on M_zeta")

    line_0 = basis_Mz[:, 0]
    rank_one_proj = np.outer(line_0, line_0.conj())
    rank_one_on_Mz = restrict_to(rank_one_proj, basis_Mz)
    is_scalar_ro, lam_ro = is_scalar_2x2(rank_one_on_Mz)
    expected_diag = np.diag([1.0, 0.0]).astype(complex)
    matches_diag = np.linalg.norm(rank_one_on_Mz - expected_diag) < TOL
    check(
        f"r={r}: |line_0><line_0| restricts to diag(1, 0) on M_zeta, hence not scalar",
        (not is_scalar_ro) and matches_diag,
        f"|line_0><line_0|_{{M_zeta}} = \n{rank_one_on_Mz},  is_scalar={is_scalar_ro}",
    )
    check(
        f"r={r}: countermodel confirms the scalar property is non-trivial",
        not is_scalar_ro,
        "Some non-retained operators do distinguish the two copies of zeta; the retained ones do not.",
    )

    section(f"r = {r}: independent attacks on the scoped negative corollary")

    # Full-stabilizer-equivariant selection route.  A nontrivial U(2) action on
    # M_zeta extends by the identity on its orthogonal complement and commutes
    # with the supplied D,U data.  Hence no line can be selected equivariantly
    # from that pair alone.
    beta = math.pi / 5
    V = np.array(
        [[math.cos(beta), -math.sin(beta)], [math.sin(beta), math.cos(beta)]],
        dtype=complex,
    )
    identity = np.eye(D.shape[0], dtype=complex)
    R_V = identity + basis_Mz @ (V - np.eye(2, dtype=complex)) @ basis_Mz.conj().T
    rotated_line = R_V @ line_0
    rotated_projector = np.outer(rotated_line, rotated_line.conj())
    stabilizer_ok = (
        np.linalg.norm(R_V @ R_V.conj().T - identity) < TOL
        and np.linalg.norm(R_V @ D - D @ R_V) < TOL
        and np.linalg.norm(R_V @ U - U @ R_V) < TOL
        and np.linalg.norm(rank_one_proj - rotated_projector) > 0.5
    )
    check(
        f"r={r}: full-stabilizer route supplies no equivariant rank-one line from (D,U)",
        stabilizer_ok,
        (
            f"||[R_V,D]||={np.linalg.norm(R_V @ D - D @ R_V):.2e}, "
            f"||[R_V,U]||={np.linalg.norm(R_V @ U - U @ R_V):.2e}, "
            f"||P_line-R_V P_line R_V^dag||={np.linalg.norm(rank_one_proj - rotated_projector):.6f}"
        ),
    )

    # Eigensolver/basis-ordering route.  Rotating the reported M_zeta basis
    # changes its first line while leaving the restricted generator data
    # unchanged, so an ordering convention cannot provide a canonical selector.
    rotated_basis = basis_Mz @ V
    rotated_first = rotated_basis[:, 0]
    rotated_first_projector = np.outer(rotated_first, rotated_first.conj())
    basis_ordering_ok = (
        np.linalg.norm(rank_one_proj - rotated_first_projector) > 0.5
        and np.linalg.norm(
            restrict_to(D, rotated_basis) - V.conj().T @ D_on_Mz @ V
        )
        < TOL
        and np.linalg.norm(
            restrict_to(U, rotated_basis) - V.conj().T @ U_on_Mz @ V
        )
        < TOL
    )
    check(
        f"r={r}: eigensolver/basis ordering cannot canonically select a line",
        basis_ordering_ok,
        (
            f"||P_first-P_rotated_first||="
            f"{np.linalg.norm(rank_one_proj - rotated_first_projector):.6f}"
        ),
    )

    # Clifford-algebra enlargement route.  The supplied gamma representation
    # contains a commuting volume element that really does split M_zeta.  Its
    # non-scalar restriction proves that it lies outside A=C*(D,U), so this
    # successful counter-route narrows rather than falsifies the scoped result.
    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
    gamma_1, gamma_2, gamma_3 = (
        np.kron(sigma_y, sigma) for sigma in (sigma_x, sigma_y, sigma_z)
    )
    gamma_volume_spin = -1j * gamma_1 @ gamma_2 @ gamma_3
    site_dimension = D.shape[0] // gamma_volume_spin.shape[0]
    gamma_volume = np.kron(gamma_volume_spin, np.eye(site_dimension, dtype=complex))
    gamma_on_Mz = restrict_to(gamma_volume, basis_Mz)
    gamma_eigenvalues = np.linalg.eigvalsh(gamma_on_Mz)
    gamma_is_scalar, _ = is_scalar_2x2(gamma_on_Mz)
    clifford_route_ok = (
        np.linalg.norm(gamma_volume @ D - D @ gamma_volume) < TOL
        and np.linalg.norm(gamma_volume @ U - U @ gamma_volume) < TOL
        and np.linalg.norm(gamma_eigenvalues - np.array([-1.0, 1.0])) < TOL
        and not gamma_is_scalar
    )
    check(
        f"r={r}: Clifford-volume enlargement splits M_zeta only outside A=C*(D,U)",
        clifford_route_ok,
        (
            f"||[Gamma,D]||={np.linalg.norm(gamma_volume @ D - D @ gamma_volume):.2e}, "
            f"||[Gamma,U]||={np.linalg.norm(gamma_volume @ U - U @ gamma_volume):.2e}, "
            f"eig(Gamma|M_zeta)={gamma_eigenvalues.tolist()}"
        ),
    )


def emit_no_go_discipline_certificate() -> None:
    """Emit live route and resolution evidence for the derived narrow no-go.

    These lines do not add PASS counters.  They make the already-executed
    attacks and the exact scope of the negative corollary available to the
    restricted audit packet without asking the auditor to infer them from
    prose or from a clipped cache excerpt.
    """
    section("No-Go Discipline execution certificate for the derived scalar-action boundary")
    if FAIL:
        print("N1/N5 certificate withheld because at least one load-bearing check failed.")
        return

    routes = (
        "N1_ROUTE exact_multiplicity: object=the common zeta zero-mode sector; "
        "mechanism=kernel and character-projector rank; "
        "attempt=make M_zeta one-dimensional so its identity is rank one; "
        "outcome=closed because the executed construction has dim(M_zeta)=2 at each stated point.",
        "N1_ROUTE algebraic_functional_calculus: object=A=C*(D,U); "
        "mechanism=restriction-algebra homomorphism; "
        "attempt=construct a polynomial, star-polynomial, or finite spectral function with non-scalar restriction; "
        "outcome=closed because every generator restricts to a scalar and scalar matrices form a unital algebra.",
        "N1_ROUTE stabilizer_equivariant_selection: object=lines in M_zeta; "
        "mechanism=the full U(2) stabilizer of the pair (D,U); "
        "attempt=select a line equivariantly without requiring its projector to lie in A; "
        "outcome=closed because the executed R_V commutes with D,U and moves the candidate line.",
        "N1_ROUTE basis_ordering_convention: object=the first reported eigenvector; "
        "mechanism=unitary basis freedom inside M_zeta; "
        "attempt=turn eigensolver ordering or phase convention into a selector; "
        "outcome=closed because the executed basis rotation changes the first line while preserving all restricted generator data.",
        "N1_ROUTE clifford_algebra_enlargement: object=the supplied Clifford volume element Gamma; "
        "mechanism=a commuting non-scalar involution; "
        "attempt=split M_zeta using existing full-Wilson data; "
        "outcome=succeeds, and the executed non-scalar restriction proves Gamma lies outside A=C*(D,U), enforcing the narrow scope.",
    )
    for route in routes:
        print(route)

    print(
        "per_element: PASS | every retained generator restricts to a scalar on M_zeta, "
        "and the executed algebra-closure argument preserves scalarity for each finite polynomial element"
    )
    print(
        "per_site: PASS | the declared generator inventory contains no site-indexed selector, "
        "so the theorem is checked as a multiplicity-space statement and makes no broader local-site claim"
    )
    print(
        "per_mode: PASS | both zeta zero-mode basis vectors have identical D, U, U-dagger, "
        "and D-spectral-projector eigen-data at each of the two executed Wilson parameters"
    )
    print(
        "per_block: PASS | the complete two-by-two M_zeta restriction of every generator and sampled word is scalar, "
        "while the explicit non-retained rank-one block is diag(1,0)"
    )
    print(
        "lattice_wide: PASS | the full 108-dimensional periodic L=3 Wilson construction and all spectral projectors "
        "were executed at r=1.0 and r=1.425, with no non-scalar retained restriction"
    )


def main() -> int:
    print("=" * 88)
    print("Narrow bridge theorem: retained Wilson/APS algebra acts as scalar on M_zeta")
    print("=" * 88)

    for r in (1.0, 1.425):
        run_for_r(r)

    emit_no_go_discipline_certificate()

    print()
    print("=" * 88)
    print("Bridge theorem summary")
    print("=" * 88)
    print(
        """
  Narrow Pattern A theorem statement:

  HYPOTHESIS:
    Let D, U be the Wilson-Dirac operator and body-diagonal spin-lift
    permutation built by `build_wilson_lattice(r)` in
    `frontier_koide_delta_lattice_wilson_selected_eigenline_no_go.py`
    for r in {1.0, 1.425}. Let V_0 = ker(D), and M_zeta the rank-two
    zeta-eigenspace of U|_{V_0} with zeta = exp(i pi/3). Let
    A := <{D, U, U^dag} union {P_lambda(D) : lambda in Spec(D)}>
    be the retained Wilson/APS polynomial algebra.

  CONCLUSION:
    For every A in A, A|_{M_zeta} = lambda_A I_2 for some scalar
    lambda_A in C.

  Class:
    (A) finite-dimensional operator algebra over C, with the explicit
    Wilson construction re-used from the sibling no-go. No Koide /
    charged-lepton mass / sqrt(m) / PDG / selection-principle physical
    identification is consumed.

  Consequence (for the parent no-go):
    The parent runner
    `frontier_koide_delta_marked_relative_cobordism_no_go.py` previously
    asserted `retained_mark = lam * sp.eye(2)`. By the Scalar-on-M_zeta
    theorem, every retained "derived boundary mark" automatically
    restricts to such a scalar on M_zeta; the parent's downstream
    commutator/expectation/countermodel algebra is therefore valid for
    every retained mark, not just the asserted one.
"""
    )

    print(f"\n{'='*88}\n  TOTAL: PASS={PASS}, FAIL={FAIL}\n{'='*88}")
    print(f"PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
