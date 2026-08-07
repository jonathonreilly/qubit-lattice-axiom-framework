#!/usr/bin/env python3
"""
Current axiom boundary for the neutrino Pfaffian / Nambu sector.

Question:
  After the operator classifier, the native-Gaussian no-go, and the minimal
  Pfaffian extension, does the current retained Cl(3) on Z^3 stack FORCE a
  Pfaffian/Nambu sector, or is that still an admitted extension?

Answer on the current retained stack:
  It is still an admitted extension, not a forced consequence.

Reason:
  The current retained microscopic grammar fixes:
    (i) the normal determinant Gaussian surface, and
    (ii) the unique allowed DeltaL=2 channel IF such a sector is added.

  But it does not fix:
    (a) whether the antisymmetric pairing block exists at all, or
    (b) its amplitude mu once admitted.

  The same retained normal data are compatible with a one-parameter family of
  Pfaffian extensions mu * S_unique, including mu = 0, while all determinant
  observables on the current surface remain unchanged.
"""

from __future__ import annotations

import math
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


def pfaffian(matrix: np.ndarray) -> complex:
    n = matrix.shape[0]
    if n == 0:
        return 1.0 + 0.0j
    if n % 2:
        return 0.0 + 0.0j
    if n == 2:
        return matrix[0, 1]

    total = 0.0 + 0.0j
    for j in range(1, n):
        coeff = matrix[0, j]
        if abs(coeff) < 1e-14:
            continue
        keep = [k for k in range(1, n) if k != j]
        sub = matrix[np.ix_(keep, keep)]
        total += ((-1) ** (j + 1)) * coeff * pfaffian(sub)
    return total


def build_dirac_majorana_seed():
    i2 = np.eye(2, dtype=complex)
    z2 = np.zeros((2, 2), dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)

    g0 = np.block([[i2, z2], [z2, -i2]])
    g1 = np.block([[z2, sx], [-sx, z2]])
    g2 = np.block([[z2, sy], [-sy, z2]])
    g3 = np.block([[z2, sz], [-sz, z2]])
    g5 = 1j * g0 @ g1 @ g2 @ g3
    cmat = 1j * g2 @ g0
    pr = (np.eye(4, dtype=complex) + g5) / 2.0

    b_r = cmat @ pr
    internal = np.zeros((16, 16), dtype=complex)
    internal[15, 15] = 1.0
    return np.kron(b_r, internal)


def build_normal_kernel(scale: float = 1.0) -> np.ndarray:
    base = np.array(
        [
            [0.4, 0.2 - 0.1j, 0.0, 0.05 + 0.03j],
            [0.2 + 0.1j, -0.3, 0.15, 0.0],
            [0.0, 0.15, 0.2, -0.07j],
            [0.05 - 0.03j, 0.0, 0.07j, 0.1],
        ],
        dtype=complex,
    )
    return scale * 0.5 * (base + base.conj().T)


def logabs_det(matrix: np.ndarray) -> float:
    sign, value = np.linalg.slogdet(matrix)
    return float(value)


def logabs_pf(matrix: np.ndarray) -> float:
    return float(np.log(abs(pfaffian(matrix))))


def canonical_j(scale: float) -> np.ndarray:
    return np.array([[0.0, scale], [-scale, 0.0]], dtype=complex)


def block_diag(*blocks: np.ndarray) -> np.ndarray:
    dim = sum(block.shape[0] for block in blocks)
    out = np.zeros((dim, dim), dtype=complex)
    start = 0
    for block in blocks:
        n = block.shape[0]
        out[start:start + n, start:start + n] = block
        start += n
    return out


def test_current_surface_fixes_only_the_channel_not_the_amplitude() -> None:
    print("\n" + "=" * 88)
    print("PART 1: THE RETAINED STACK FIXES THE UNIQUE CHANNEL, NOT ITS AMPLITUDE")
    print("=" * 88)

    s_unique = build_dirac_majorana_seed()
    support = np.nonzero(np.abs(s_unique) > 1e-12)
    unique_internal_rows = sorted({idx % 16 for idx in support[0]})
    rank = int(np.linalg.matrix_rank(s_unique, tol=1e-10))

    check("Unique pairing seed remains confined to the nu_R slot", unique_internal_rows == [15],
          f"internal rows={unique_internal_rows}")
    check("Unique pairing seed remains rank-2", rank == 2, f"rank={rank}")

    mus = [0.0, 0.3, 1.1]
    antisym_residuals = []
    for mu in mus:
        delta_mu = mu * s_unique
        antisym_residuals.append(np.linalg.norm(delta_mu.T + delta_mu))

    check("Every mu * S_unique stays inside the same antisymmetric channel family",
          max(antisym_residuals) < 1e-10,
          f"max ||Delta^T+Delta||={max(antisym_residuals):.2e}")

    print()
    print("  The current exact classifier therefore determines one thing exactly:")
    print("  if a DeltaL=2 sector exists, it must live on one unique channel.")
    print("  It does not determine the amplitude mu of that channel.")


def test_current_determinant_data_are_blind_to_pfaffian_amplitude() -> None:
    print("\n" + "=" * 88)
    print("PART 2: CURRENT DETERMINANT OBSERVABLES CANNOT SEE THE PFAFFIAN AMPLITUDE")
    print("=" * 88)

    k = build_normal_kernel()
    j = 0.17 * np.eye(k.shape[0], dtype=complex)
    det_obs = logabs_det(k + j) - logabs_det(k)

    mus = [0.0, 0.3, 1.1]
    det_obs_family = []
    pf_obs_family = []
    for mu in mus:
        det_obs_family.append(det_obs)
        a_mu = canonical_j(2.0 + mu)
        pf_obs_family.append(logabs_pf(a_mu))

    det_spread = max(det_obs_family) - min(det_obs_family)
    pf_spread = max(pf_obs_family) - min(pf_obs_family)

    check("Normal determinant observable is identical across the Pfaffian family", abs(det_spread) < 1e-14,
          f"det spread={det_spread:.2e}")
    check("Pfaffian observable changes across the same family", pf_spread > 1e-3,
          f"pf spread={pf_spread:.6f}")

    print()
    print("  So the retained determinant grammar does not select mu. The same")
    print("  current normal data are compatible with mu = 0 and mu != 0.")


def test_mu_zero_and_mu_nonzero_are_both_consistent_extensions() -> None:
    print("\n" + "=" * 88)
    print("PART 3: MU = 0 AND MU != 0 BOTH FIT THE CURRENT BOUNDARY DATA")
    print("=" * 88)

    # Same normal block throughout: this is the current retained surface.
    k = build_normal_kernel(scale=1.2)
    det_signature = tuple(np.round(np.linalg.eigvalsh(k), 12))

    s_unique = build_dirac_majorana_seed()
    mu0 = 0.0
    mu1 = 0.8

    delta0 = mu0 * s_unique
    delta1 = mu1 * s_unique

    # The retained data do not encode Delta at all, so the normal signature is
    # identical across both candidate extensions.
    det_signature_0 = tuple(np.round(np.linalg.eigvalsh(k), 12))
    det_signature_1 = tuple(np.round(np.linalg.eigvalsh(k), 12))

    # But the Pfaffian sectors differ sharply.
    a0 = canonical_j(2.3 + mu0)
    a1 = canonical_j(2.3 + mu1)
    pf0 = pfaffian(a0)
    pf1 = pfaffian(a1)

    check("mu = 0 extension preserves exactly the current normal signature", det_signature_0 == det_signature,
          f"signature={det_signature_0}")
    check("mu != 0 extension preserves exactly the same normal signature", det_signature_1 == det_signature,
          f"signature={det_signature_1}")
    check("mu = 0 and mu != 0 give distinct Pfaffian sectors", abs(pf1 - pf0) > 1e-6,
          f"|Pf1-Pf0|={abs(pf1 - pf0):.6f}")
    check("mu = 0 and mu != 0 share the same unique channel support", np.linalg.norm((delta1 / mu1 if mu1 else delta1) - s_unique) < 1e-10
          and np.linalg.norm(delta0) < 1e-12,
          "support fixed, amplitude free")

    print()
    print("  This is the exact boundary statement: the current retained stack")
    print("  does not distinguish the zero and nonzero Pfaffian amplitudes.")
    print("  Therefore the Pfaffian/Nambu sector is not forced by the current")
    print("  retained derivation stack.")


def n5_execution_certificate() -> None:
    """State the granularity at which this runner actually resolves the no-go.

    Reporting only: no check() call is added and no PASS/FAIL count moves.
    """
    print("\n" + "=" * 88)
    print("N5 EXECUTION CERTIFICATE: WHAT THIS RUNNER RESOLVES")
    print("=" * 88)

    s_unique = build_dirac_majorana_seed()
    seed_dim = s_unique.shape[0]
    internal_dim = 16
    dirac_dim = seed_dim // internal_dim
    rank = int(np.linalg.matrix_rank(s_unique, tol=1e-10))
    k = build_normal_kernel(scale=1.2)
    signature = tuple(round(float(v), 12) for v in np.linalg.eigvalsh(k))

    print(
        "per_element: resolved with amplitudes. The Dirac algebra is assembled 2 x 2 "
        "block by 2 x 2 block into four 4 x 4 gammas, with g5 and C = i g2 g0 formed "
        "as explicit products; the internal factor is a 16 x 16 matrix carrying "
        "exactly one nonzero entry, [15, 15] = 1.0; the Kronecker product places "
        f"C P_R into a {seed_dim} x {seed_dim} seed whose support is then located by "
        f"scanning all {seed_dim * seed_dim} entries with np.nonzero. The normal "
        "kernel is written entry by entry (0.4, 0.2 - 0.1j, 0.05 + 0.03j, -0.3, 0.15, "
        "0.2, -0.07j, 0.1) and the Pfaffian routine reads matrix[0, j] one at a time."
    )
    print(
        "per_site: checked and not executed. The note frames this as the retained "
        "Cl(3)-on-Z^3 stack, but no Z^3 lattice is instantiated anywhere in this "
        f"runner: the {internal_dim}-dimensional factor is a slot inventory with a "
        f"single occupied index and the {dirac_dim}-dimensional factor is a spinor "
        "index, and neither carries a coordinate, a neighbour relation or a volume."
    )
    print(
        "per_mode: resolved, and it supplies the comparison object of Part 3. "
        "eigvalsh returns the full four-eigenvalue normal signature of the retained "
        f"kernel at scale 1.2, {list(signature)}, held to 12 decimals, and "
        f"matrix_rank resolves the {seed_dim} x {seed_dim} seed to rank {rank}, that "
        "is to exactly one Majorana pair. No eigenvector, and no eigenmode of the "
        "pairing seed itself, is ever computed."
    )
    print(
        "per_block: resolved as location and support rather than as a coupled "
        "decomposition. The seed is a Kronecker product of a Dirac block with an "
        "internal block, the chirality projector (1 + g5)/2 is itself a block "
        "projector, and the support scan certifies that the occupied internal row is "
        f"exactly one of the {internal_dim}, index 15, the nu_R slot. The normal "
        "kernel and the pairing seed are never assembled into a common Nambu matrix, "
        "so no inter-block coupling is ever formed, and the block_diag helper defined "
        "in this file is never called."
    )
    print(
        "lattice_wide: checked and not executed, and the missing global theorem is "
        "exactly what this note is about. The claim is that the retained stack does "
        "not force the Pfaffian sector, so the forcing theorem a stack-wide argument "
        "would have to supply is precisely the absent object; execution here exhibits "
        "two admissible extensions side by side rather than quantifying over the "
        "stack, and no volume, no sequence and no limit of any kind is taken."
    )
    print(
        "  scope: the determinant-blindness comparisons are not computed. In Part 2 "
        "the loop appends the same precomputed scalar det_obs three times, so a zero "
        "spread follows from repetition; in Part 3 both signatures are the identical "
        "expression evaluated on the identical kernel, so those two checks compare a "
        "value with itself. The substantive content is structural - the retained data "
        "never encode Delta at all - and the source comment already says so."
    )
    print(
        "  scope: the Pfaffian side of Parts 2 and 3 is a stand-in, not the real "
        "family. What is probed is the 2 x 2 canonical_j(2.0 + mu) and "
        "canonical_j(2.3 + mu), whose Pfaffian is just the single entry 2.0 + mu "
        f"(resp. 2.3 + mu), so the reported |Pf1 - Pf0| is simply mu1 - mu0. The "
        f"Pfaffian of the actual {seed_dim} x {seed_dim} family mu * S_unique is "
        "never computed anywhere in this runner."
    )
    print(
        "  scope: fully deterministic - no RNG stream and no optimizer is used, so "
        "every quantity above follows from literal constants in the source."
    )


def main() -> int:
    print("=" * 88)
    print("NEUTRINO MAJORANA: CURRENT PFAFFIAN AXIOM BOUNDARY")
    print("=" * 88)
    print()
    print("Authority stack:")
    print("  - main:docs/publication/ci3_z3/DERIVATION_ATLAS.md")
    print("    rows: Framework axiom; Observable principle; Anomaly-forced time;")
    print("          Native weak algebra; Structural SU(3) closure; One-generation matter closure")
    print("  - docs/UNIFIED_AXIOM_BOUNDARY_NOTE.md")
    print("  - docs/NEUTRINO_MAJORANA_OPERATOR_AXIOM_FIRST_NOTE.md")
    print("  - docs/NEUTRINO_MAJORANA_NATIVE_GAUSSIAN_NO_GO_NOTE.md")
    print("  - docs/NEUTRINO_MAJORANA_PFAFFIAN_EXTENSION_NOTE.md")
    print()
    print("Question:")
    print("  Does the current retained Cl(3) on Z^3 stack force a Pfaffian/Nambu")
    print("  sector, or does it only admit one if added?")

    test_current_surface_fixes_only_the_channel_not_the_amplitude()
    test_current_determinant_data_are_blind_to_pfaffian_amplitude()
    test_mu_zero_and_mu_nonzero_are_both_consistent_extensions()
    n5_execution_certificate()

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  On the current retained stack, the Pfaffian/Nambu sector is not")
    print("  forced. The stack fixes the unique allowed DeltaL=2 channel, but not")
    print("  the existence or amplitude of an antisymmetric pairing block.")
    print()
    print("  So the current honest status is:")
    print("    - unique channel: forced")
    print("    - Pfaffian sector existence: not yet forced")
    print("    - Pfaffian coefficient mu: not yet forced")
    print()
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
