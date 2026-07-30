#!/usr/bin/env python3
"""Pattern A narrow runner for `CLIFFORD_CHIRALITY_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10`.

Verifies the standalone Clifford-algebra fact (Lawson--Michelsohn, *Spin
Geometry*, Ch. I, Prop. 3.3): in `Cl(p, q)` with `n = p + q` generators
`gamma_1, ..., gamma_n` satisfying `gamma_mu^2 = +/- I` and
`{gamma_mu, gamma_nu} = 0` for `mu != nu`, the volume element

    omega = gamma_1 gamma_2 ... gamma_n

obeys

    omega gamma_mu = (-1)^(n-1) gamma_mu omega

(equivalently, `[omega, gamma_mu] = 0` when `n` is odd, and
`{omega, gamma_mu} = 0` when `n` is even).

Therefore:
  - `n` EVEN: a chirality involution `gamma_5` proportional to `omega`
    (after a possible scalar phase fixing `gamma_5^2 = +I`) ANTICOMMUTES
    with every generator. The canonical Z_2 grading has an internal
    square-one implementer.
  - `n` ODD: any element proportional to `omega` COMMUTES with every
    generator (omega is central). Inside the Clifford algebra Cl(n)
    itself, no nonzero element anticommutes with every generator. The
    canonical even/odd Z_2 grading still exists, but it has no internal
    square-one implementer. An ambient matrix carrier may contain an
    anticommuter outside the represented internal Clifford span.

This is class-A pure linear/Clifford algebra. No SM gauge content, no
anomaly trace, no temporal direction, no single-clock evolution
hypothesis is consumed. T1--T2 are abstract Clifford-algebra statements.
T3 separately assumes that the total algebra is `Cl(d_s, d_t)` and uses
only the accepted Lattice premise `Z^3`, hence `d_s = 3`. The result is
specialised to this conditional setting only at the end.

Verification proceeds in six parts:

  Part 1 -- Build explicit Cl(n) generators in even and odd dimensions
            n in {1, 2, 3, 4, 5, 6} via the standard tower
                Cl(0) = C, Cl(1) = C[sigma_1],
                Cl(2k) = Cl(2k-2) tensor M_2(C),
                Cl(2k+1) = Cl(2k) tensor C[sigma_3-extension].
            Check {gamma_mu, gamma_nu} = 2 delta_{mu nu} I in a
            deterministic finite matrix smoke test.

  Part 2 -- Compute omega = gamma_1 ... gamma_n and verify
                omega gamma_mu = (-1)^(n-1) gamma_mu omega
            for each generator and each dimension.

  Part 3 -- Show that for n ODD, no element of the represented internal
            Clifford span anticommutes with all gamma_mu. This statement
            is deliberately narrower than a claim about every matrix in
            the ambient endomorphism algebra.

  Part 4 -- For n EVEN and every finite signature choice, exhibit
            gamma_5 := i^{n(n-1)/2+q} omega and verify gamma_5^2 = +I
            and {gamma_5, gamma_mu} = 0 for every mu, where q counts
            negative-square generators.

  Part 5 -- Conditionally take the total algebra as Cl(d_s, d_t), then
            specialise with the accepted Lattice premise d_s = 3. The
            chirality involution requires d_s + d_t even, hence d_t odd.

  Part 6 -- Execute current-cycle N1/N5/N7 probes, including an external
            ambient-carrier steelman and its verified internal boundary.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from itertools import combinations, product
from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np

AUDIT_TIMEOUT_SEC = 120
NOTE_PATH = "docs/CLIFFORD_CHIRALITY_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md"
AUDIT_INPUT_PATHS = (
    "docs/CLIFFORD_CHIRALITY_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md",
    "scripts/clifford_chirality_dimension_n7_independent_check.py",
)

if TYPE_CHECKING:
    # Static audit-packet registration only. The independent N7 helper is run
    # by the audit orchestrator on its own authenticated stdout surface.
    import clifford_chirality_dimension_n7_independent_check as _n7_helper

np.set_printoptions(precision=12, suppress=True, linewidth=120)

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        tag = "FAIL (A)"
    msg = f"  [{tag}] {label}"
    if detail:
        msg += f"  ({detail})"
    print(msg)


def section(title: str) -> None:
    print("\n" + "-" * 88 + f"\n{title}\n" + "-" * 88)


# ----------------------------------------------------------------------------
# Pauli matrices and Cl(n) construction
# ----------------------------------------------------------------------------
I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)


def kron_list(matrices):
    out = matrices[0]
    for M in matrices[1:]:
        out = np.kron(out, M)
    return out


def build_cl_generators(n: int):
    """Return n generators of Cl(n,0) in a faithful complex matrix carrier.

    Construction (standard staggered tower):
      n = 1: [sx]
      n = 2: [sx, sy]
      n = 3: [sx kron I, sz kron sx, sz kron sz]
      n = 4: [sx kron I kron I, sz kron sx kron I, sz kron sz kron sx, sz kron sz kron sy]
      n in {5, 6, ...}: extend by alternating tensor pattern.

    All generators square to +I and pairwise anticommute. We construct
    enough cases for Part 1 (n in {1, ..., 6}).
    """
    if n == 1:
        return [sx.astype(complex)]
    if n == 2:
        return [sx.astype(complex), sy.astype(complex)]
    if n == 3:
        return [
            kron_list([sx, I2]),
            kron_list([sz, sx]),
            kron_list([sz, sz]),
        ]
    if n == 4:
        return [
            kron_list([sx, I2, I2]),
            kron_list([sz, sx, I2]),
            kron_list([sz, sz, sx]),
            kron_list([sz, sz, sy]),
        ]
    if n == 5:
        return [
            kron_list([sx, I2, I2]),
            kron_list([sz, sx, I2]),
            kron_list([sz, sz, sx]),
            kron_list([sz, sz, sy]),
            kron_list([sy, I2, I2]),
        ]
    if n == 6:
        return [
            kron_list([sx, I2, I2, I2]),
            kron_list([sz, sx, I2, I2]),
            kron_list([sz, sz, sx, I2]),
            kron_list([sz, sz, sz, sx]),
            kron_list([sz, sz, sz, sy]),
            kron_list([sy, I2, I2, I2]),
        ]
    raise NotImplementedError(f"n = {n} not constructed")


def anticommutator(A, B):
    return A @ B + B @ A


def commutator(A, B):
    return A @ B - B @ A


# ============================================================================
section("Part 1: Cl(n) generators with {g_mu, g_nu} = 2 delta_{mu nu} I")
# ============================================================================
for n in (1, 2, 3, 4, 5, 6):
    gens = build_cl_generators(n)
    dim = gens[0].shape[0]
    eye = np.eye(dim, dtype=complex)
    ok = True
    detail = ""
    for mu in range(n):
        if not np.allclose(gens[mu] @ gens[mu], eye):
            ok = False
            detail = f"g_{mu}^2 != I at n={n}"
            break
        for nu in range(mu + 1, n):
            if not np.allclose(anticommutator(gens[mu], gens[nu]), 0):
                ok = False
                detail = f"non-zero anticommutator g_{mu} g_{nu} at n={n}"
                break
        if not ok:
            break
    check(
        f"n={n}: {n} generators of Cl(n, 0) on C^{dim} satisfy CAR",
        ok,
        detail or f"dim = {dim}",
    )


# ============================================================================
section("Part 2: volume element identity omega g_mu = (-1)^(n-1) g_mu omega")
# ============================================================================
for n in (1, 2, 3, 4, 5, 6):
    gens = build_cl_generators(n)
    dim = gens[0].shape[0]
    omega = gens[0].copy()
    for mu in range(1, n):
        omega = omega @ gens[mu]
    sign = (-1) ** (n - 1)  # +1 if n odd; -1 if n even
    ok = True
    parity = "odd" if n % 2 == 1 else "even"
    expected_relation = "commutes" if n % 2 == 1 else "anticommutes"
    for mu in range(n):
        lhs = omega @ gens[mu]
        rhs = sign * (gens[mu] @ omega)
        if not np.allclose(lhs, rhs):
            ok = False
            break
    check(
        f"n={n} ({parity}): omega {expected_relation} with every g_mu",
        ok,
        detail=f"omega ({expected_relation} for n={parity})",
    )


# ============================================================================
section("Part 3: n ODD => no element OF THE CLIFFORD ALGEBRA Cl(n) anticommutes")
# ============================================================================
# Inside the Clifford algebra Cl(n) itself, every element M is a unique
# complex linear combination of the 2^n basis products of distinct
# generators g_{i_1} g_{i_2} ... g_{i_r} (r = 0, 1, ..., n).
#
# A degree-r product anticommutes with g_mu iff exactly r of {1, ..., n}
# (excluding mu) appear in its index set, modulo a parity sign. The
# precise rule is:
#   g_{i_1} ... g_{i_r} commutes with g_mu  iff  ((mu ∈ index set) XOR (r odd))
#   = False, i.e., (r is even AND mu not in index set) OR (r is odd AND mu in index set).
# Equivalently: a degree-r product anticommutes with g_mu iff
#   (r is odd AND mu NOT in index set) OR (r is even AND mu in index set).
#
# For an element M = sum_S c_S g_S to anticommute with EVERY g_mu, the
# coefficients must satisfy the appropriate parity constraints
# simultaneously for every mu = 1, ..., n. We solve this linear system.

def clifford_basis(gens):
    """All ordered products of distinct generators (length 0 ... n)."""
    n = len(gens)
    basis = []
    labels = []
    indexsets = []
    for r in range(n + 1):
        for idx in combinations(range(n), r):
            if r == 0:
                M = np.eye(gens[0].shape[0], dtype=complex)
                lab = "I"
            else:
                M = gens[idx[0]].copy()
                for j in idx[1:]:
                    M = M @ gens[j]
                lab = "g" + "".join(str(k + 1) for k in idx)
            basis.append(M)
            labels.append(lab)
            indexsets.append(set(idx))
    return basis, labels, indexsets


def solve_anticommute_in_clifford_algebra(gens):
    """Return (sol_dim, basis_dim) where sol_dim is the dimension of the
    set {M in Cl(n) | {M, g_mu} = 0 for all mu = 1, ..., n}. We work in
    the 2^n-dim Clifford basis (NOT the full M_{2^k}(C) ambient matrix
    space).
    """
    n = len(gens)
    basis, labels, indexsets = clifford_basis(gens)
    B = len(basis)  # = 2^n
    # Build linear constraints. For each mu and each basis element b_S of
    # degree r:
    #   {b_S, g_mu} = (sign_S_mu) * (b_S g_mu + g_mu b_S)
    # We compute the anticommutator directly and project back onto the
    # Clifford basis.
    #
    # Easiest: for each basis element, compute its anticommutator with g_mu
    # (a 2^k x 2^k matrix), then test whether each entry-pair is zero
    # entrywise. Linear system: c · A_mu = 0 where A_mu is constructed by
    # mapping each basis element to its anticommutator's vec.
    dim = gens[0].shape[0]
    constraint_rows = []
    for mu in range(n):
        g = gens[mu]
        # The anticommutator of basis element b_S with g_mu is a
        # 2^k x 2^k matrix; flatten to vector.
        for entry in range(dim * dim):
            row = np.zeros(B, dtype=complex)
            for j, b in enumerate(basis):
                ac = b @ g + g @ b
                row[j] = ac.flat[entry]
            if np.any(np.abs(row) > 1e-12):
                constraint_rows.append(row)
    if constraint_rows:
        L = np.array(constraint_rows, dtype=complex)
        rank = np.linalg.matrix_rank(L, tol=1e-10)
        return B - rank, B
    return B, B


def flattened_span_rank(matrices):
    """Rank of matrices treated as vectors in the ambient matrix algebra."""
    columns = np.column_stack([matrix.reshape(-1) for matrix in matrices])
    return int(np.linalg.matrix_rank(columns, tol=1e-10))


def solve_ambient_anticommutant(gens):
    """Nullity of {X,g_mu}=0 over the full ambient matrix algebra."""
    dim = gens[0].shape[0]
    matrix_units = []
    for row in range(dim):
        for column in range(dim):
            unit = np.zeros((dim, dim), dtype=complex)
            unit[row, column] = 1
            matrix_units.append(unit)
    constraint_columns = []
    for unit in matrix_units:
        constraint_columns.append(
            np.concatenate(
                [(unit @ generator + generator @ unit).reshape(-1) for generator in gens]
            )
        )
    system = np.column_stack(constraint_columns)
    return dim * dim - int(np.linalg.matrix_rank(system, tol=1e-10))


def find_external_pauli_anticommuter(gens):
    """Search Pauli tensor words for an anticommuter outside internal Cl(n)."""
    dim = gens[0].shape[0]
    qubits = int(round(np.log2(dim)))
    identity = np.eye(dim, dtype=complex)
    basis, _, _ = clifford_basis(gens)
    internal_rank = flattened_span_rank(basis)
    for factors in product((I2, sx, sy, sz), repeat=qubits):
        candidate = kron_list(list(factors))
        if np.allclose(candidate, identity):
            continue
        if not np.allclose(candidate @ candidate, identity):
            continue
        if not all(np.allclose(anticommutator(candidate, generator), 0) for generator in gens):
            continue
        augmented_rank = flattened_span_rank([*basis, candidate])
        if augmented_rank == internal_rank + 1:
            return candidate, internal_rank, augmented_rank
    return None, internal_rank, internal_rank


for n in (1, 3, 5):
    gens = build_cl_generators(n)
    sol_dim, basis_dim = solve_anticommute_in_clifford_algebra(gens)
    represented_rank = flattened_span_rank(clifford_basis(gens)[0])
    # For n odd, no element of Cl(n) anticommutes with every generator.
    check(
        f"n={n} (odd): {{M in Cl(n) | {{M, g_mu}}=0 forall mu}} = {{0}} inside Cl(n)",
        represented_rank == basis_dim == 2**n and sol_dim == 0,
        detail=(
            f"numerical span rank = {represented_rank} = 2^{n}; "
            f"sol_dim = {sol_dim}"
        ),
    )

# Sanity: in even dimension, gamma_5 = i^{n(n-1)/2} omega itself spans a
# 1-dim solution INSIDE Cl(n).
for n in (2, 4, 6):
    gens = build_cl_generators(n)
    sol_dim, basis_dim = solve_anticommute_in_clifford_algebra(gens)
    represented_rank = flattened_span_rank(clifford_basis(gens)[0])
    check(
        f"n={n} (even): {{M in Cl(n) | {{M, g_mu}}=0 forall mu}} is exactly 1-dim (= span of gamma_5)",
        represented_rank == basis_dim == 2**n and sol_dim == 1,
        detail=(
            f"numerical span rank = {represented_rank} = 2^{n}; "
            f"sol_dim = {sol_dim}"
        ),
    )


# ============================================================================
section("Part 4: n EVEN => gamma_5 := i^{n(n-1)/2+q} omega for every signature")
# ============================================================================
for n in (2, 4, 6):
    positive_gens = build_cl_generators(n)
    dim = positive_gens[0].shape[0]
    eye = np.eye(dim, dtype=complex)
    exponent_without_signature = n * (n - 1) // 2
    ok_sq = True
    ok_ac = True
    signature_count = 0
    for signature in product((1, -1), repeat=n):
        gens = [
            generator if eta == 1 else 1j * generator
            for generator, eta in zip(positive_gens, signature)
        ]
        q = sum(eta == -1 for eta in signature)
        omega = gens[0].copy()
        for generator in gens[1:]:
            omega = omega @ generator
        expected_omega_square = (-1) ** (exponent_without_signature + q) * eye
        gamma5 = (1j) ** (exponent_without_signature + q) * omega
        ok_sq &= (
            np.allclose(omega @ omega, expected_omega_square)
            and np.allclose(gamma5 @ gamma5, eye)
        )
        ok_ac &= all(
            np.allclose(anticommutator(gamma5, generator), 0)
            for generator in gens
        )
        signature_count += 1
    check(
        f"n={n}: omega^2=(-1)^(n(n-1)/2+q)I and gamma_5^2=+I",
        ok_sq,
        detail=f"all {signature_count} signatures; phase i^(n(n-1)/2+q)",
    )
    check(
        f"n={n}: {{gamma_5, g_mu}} = 0 for every mu and signature",
        ok_ac,
    )


# ============================================================================
section("Part 5: conditional Cl(d_s,d_t) specialisation with Lattice d_s=3")
# ============================================================================
# The accepted Lattice premise fixes the spatial substrate to Z^3, hence d_s=3.
# This part separately assumes that the total algebra is Cl(d_s,d_t).
# For a chirality involution to exist, d_s + d_t must be even.
# Therefore d_t must have the opposite parity to d_s.
# d_s = 3 is odd, so d_t must be ODD.
d_s = 3
allowed_d_t = [d for d in range(1, 8) if (d_s + d) % 2 == 0]
forbidden_d_t = [d for d in range(1, 8) if (d_s + d) % 2 == 1]
check(
    "conditional Cl(d_s,d_t) with Lattice d_s=3 requires d_t odd",
    allowed_d_t == [1, 3, 5, 7] and forbidden_d_t == [2, 4, 6],
    detail=f"allowed d_t = {allowed_d_t}; forbidden d_t = {forbidden_d_t}",
)
# Selecting one value from the allowed odd set is outside this runner. The
# axis-conditional sister note and the Craig--Weinstein/Tegmark literature are
# orientation only; none is consumed as a load-bearing d_t=1 derivation here.
print()
print("  Out-of-scope reminder: this narrow theorem only forces d_t to")
print("  be ODD. It supplies no selection of d_t = 1. The axis-conditional")
print("  sister note and the Craig--Weinstein/Tegmark literature are")
print("  non-load-bearing orientation only.")


# ============================================================================
section("Part 6: current-cycle N1/N5/N7 candidate evidence")
# ============================================================================
# N1 route 1: full arbitrary-coefficient kernel, including cancellation.
coefficient_cancellation_ok = True
for n in (1, 3, 5):
    gens = build_cl_generators(n)
    basis, _, _ = clifford_basis(gens)
    sol_dim, basis_dim = solve_anticommute_in_clifford_algebra(gens)
    coefficient_cancellation_ok &= (
        flattened_span_rank(basis) == basis_dim == 2**n and sol_dim == 0
    )

# Downstream normalization check. It consumes route 1 and is not counted as
# an independent N1 family.
zero_normalization_ok = True
for n in (1, 3, 5):
    gens = build_cl_generators(n)
    dim = gens[0].shape[0]
    zero = np.zeros((dim, dim), dtype=complex)
    sol_dim, _ = solve_anticommute_in_clifford_algebra(gens)
    zero_normalization_ok &= (
        all(np.allclose(anticommutator(zero, generator), 0) for generator in gens)
        and not np.allclose(zero @ zero, np.eye(dim, dtype=complex))
        and sol_dim == 0
    )

# N1 route 2: central invertible odd volume.
central_volume_ok = True
for n in (1, 3, 5):
    gens = build_cl_generators(n)
    omega = gens[0].copy()
    for generator in gens[1:]:
        omega = omega @ generator
    central_volume_ok &= (
        all(np.allclose(commutator(omega, generator), 0) for generator in gens)
        and abs(np.linalg.det(omega)) > 1e-10
        and (-1) ** n == -1
    )

# Finite parity enumeration of route 1. It is a subordinate smoke test rather
# than an independent route.
parity_witness_ok = True
parity_witness_count = 0
for n in range(1, 16, 2):
    for mask in range(1 << n):
        degree = mask.bit_count()
        if degree % 2:
            witness_mu = next(mu for mu in range(n) if mask & (1 << mu))
        else:
            witness_mu = next(mu for mu in range(n) if not mask & (1 << mu))
        delta = int(bool(mask & (1 << witness_mu)))
        parity_witness_ok &= (degree - delta) % 2 == 0
        parity_witness_count += 1

# N1 route 3 and N7: hostile alternate ambient carrier.
external_carrier_ok = True
external_carrier_cases = []
external_by_n = {}
for n in (1, 3, 5):
    gens = build_cl_generators(n)
    external, internal_rank, augmented_rank = find_external_pauli_anticommuter(gens)
    case_ok = external is not None and augmented_rank == internal_rank + 1
    external_carrier_ok &= case_ok
    external_by_n[n] = external
    external_carrier_cases.append((n, internal_rank, augmented_rank))

# N1 route 4: extension by an anticommuting square-one generator. The
# universal property would give a nonzero unital map Cl_{n+1}(C) -> Cl_n(C).
# The even source algebra is simple, so the map would be injective, contrary
# to 2^(n+1) > 2^n. The finite tower checks the associated dimension doubling.
extension_dimension_ok = True
extension_dimension_cases = []
for n in (1, 3, 5):
    gens = build_cl_generators(n)
    basis, _, _ = clifford_basis(gens)
    external = external_by_n[n]
    if external is None:
        extension_dimension_ok = False
        extension_dimension_cases.append((n, 0, 0))
        continue
    internal_rank = flattened_span_rank(basis)
    extended_rank = flattened_span_rank(
        [*basis, *[external @ basis_element for basis_element in basis]]
    )
    extension_dimension_ok &= (
        internal_rank == 2**n
        and extended_rank == 2 ** (n + 1)
        and extended_rank > internal_rank
    )
    extension_dimension_cases.append((n, internal_rank, extended_rank))

# N1 route 5: global two-summand structure. The odd grade automorphism
# exchanges the central volume idempotents, whereas inner automorphisms fix
# the center pointwise. The faithful carriers test the nonzero idempotents and
# their exchange by the external grade implementer.
central_idempotent_ok = True
central_idempotent_cases = []
for n in (1, 3, 5):
    gens = build_cl_generators(n)
    external = external_by_n[n]
    dim = gens[0].shape[0]
    identity = np.eye(dim, dtype=complex)
    omega = gens[0].copy()
    for generator in gens[1:]:
        omega = omega @ generator
    normalized_volume = (1j) ** (n * (n - 1) // 2) * omega
    idempotent_plus = (identity + normalized_volume) / 2
    idempotent_minus = (identity - normalized_volume) / 2
    basis, _, _ = clifford_basis(gens)
    plus_rank = int(np.linalg.matrix_rank(idempotent_plus, tol=1e-10))
    minus_rank = int(np.linalg.matrix_rank(idempotent_minus, tol=1e-10))
    case_ok = (
        external is not None
        and np.allclose(external @ external, identity)
        and np.allclose(normalized_volume @ normalized_volume, identity)
        and all(
            np.allclose(commutator(normalized_volume, basis_element), 0)
            for basis_element in basis
        )
        and plus_rank > 0
        and minus_rank > 0
        and np.allclose(external @ idempotent_plus @ external, idempotent_minus)
        and np.allclose(external @ idempotent_minus @ external, idempotent_plus)
    )
    central_idempotent_ok &= case_ok
    central_idempotent_cases.append((n, plus_rank, minus_rank))

# Signature rephasing is a convention robustness check subordinate to route 1.
signature_rephase_ok = True
signature_rephase_cases = 0
for n in (1, 3, 5):
    positive_gens = build_cl_generators(n)
    dim = positive_gens[0].shape[0]
    identity = np.eye(dim, dtype=complex)
    for signature in product((1, -1), repeat=n):
        signed_gens = [
            generator if eta == 1 else 1j * generator
            for generator, eta in zip(positive_gens, signature)
        ]
        squares_ok = all(
            np.allclose(generator @ generator, eta * identity)
            for generator, eta in zip(signed_gens, signature)
        )
        pairs_ok = all(
            np.allclose(anticommutator(signed_gens[mu], signed_gens[nu]), 0)
            for mu in range(n)
            for nu in range(mu + 1, n)
        )
        basis, _, _ = clifford_basis(signed_gens)
        sol_dim, basis_dim = solve_anticommute_in_clifford_algebra(signed_gens)
        signature_rephase_ok &= (
            squares_ok
            and pairs_ok
            and flattened_span_rank(basis) == basis_dim == 2**n
            and sol_dim == 0
        )
        signature_rephase_cases += 1

route_results = {
    "coefficient-cancellation": coefficient_cancellation_ok,
    "central-volume": central_volume_ok,
    "external-matrix-carrier": external_carrier_ok,
    "extension-dimension": extension_dimension_ok,
    "central-idempotent-exchange": central_idempotent_ok,
}
for route_id, ok in route_results.items():
    check(f"N1 live route {route_id}", ok)
check(
    "N1 subordinate normalization/parity/signature checks",
    zero_normalization_ok and parity_witness_ok and signature_rephase_ok,
    detail=(
        f"{parity_witness_count} subset cases; "
        f"{signature_rephase_cases} odd-signature cases"
    ),
)


N5_SCAN_PHRASES = (
    "absent", "cannot", "does not", "fails", "impossible", "no nonzero",
    "no-go", "obstruction", "requires a new axiom", "rule out",
    "rules out", "structurally undecidable", "unavailable", "is not", "are not",
)


def normalized_text(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().casefold())


def current_n5_phrase_groups() -> list[dict[str, object]]:
    """Generate current source phrase-group IDs and exact locators."""
    lines = Path(NOTE_PATH).read_text(encoding="utf-8").splitlines()
    grouped: dict[tuple[str, str], list[tuple[int, str]]] = {}
    for phrase in N5_SCAN_PHRASES:
        pattern = r"\b" + re.escape(phrase).replace(r"\ ", r"\s+") + r"\b"
        occurrence_index = 0
        for line_index, line in enumerate(lines):
            for _match in re.finditer(pattern, line, re.IGNORECASE):
                occurrence_index += 1
                locator = line.strip()
                if len(normalized_text(locator)) < 12:
                    start = max(0, line_index - 1)
                    stop = min(len(lines), line_index + 2)
                    locator = " ".join(
                        part.strip() for part in lines[start:stop] if part.strip()
                    )
                group_id = hashlib.sha256(
                    normalized_text(locator).encode("utf-8")
                ).hexdigest()[:16]
                grouped.setdefault((normalized_text(phrase), group_id), []).append(
                    (occurrence_index, locator)
                )
    result = []
    for (phrase, group_id), items in sorted(grouped.items()):
        ordered = sorted(items)
        payload = json.dumps(ordered, ensure_ascii=False, separators=(",", ":"))
        result.append(
            {
                "phrase": phrase,
                "group_id": group_id,
                "occurrence_count": len(ordered),
                "locator_sha256": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
                "locator": ordered[0][1],
            }
        )
    return result


# N5 binds the one deliberately retained negative-boundary phrase to five
# separately evaluated resolutions. Broader readings are actively falsified.
phrase_groups = current_n5_phrase_groups()
phrase_manifest_ok = (
    len(phrase_groups) == 1
    and phrase_groups[0]["phrase"] == "no nonzero"
    and phrase_groups[0]["occurrence_count"] == 1
)
check(
    "N5 source phrase manifest has one exact boundary group",
    phrase_manifest_ok,
    detail=f"groups={[(g['phrase'], g['group_id']) for g in phrase_groups]}",
)

per_site_nullity = solve_ambient_anticommutant([sx, sy, sz])
per_mode_has_anticommuter = (
    np.allclose(anticommutator(sy, sx), 0)
    and np.allclose(sy @ sy, I2)
)
block_gens = build_cl_generators(3)
block_external = external_by_n[3]
per_block_countercontrol = False
lattice_wide_countercontrol = False
if block_external is not None:
    block_identity = np.eye(block_gens[0].shape[0], dtype=complex)
    per_block_countercontrol = (
        np.allclose(block_external @ block_external, block_identity)
        and all(
            np.allclose(anticommutator(block_external, generator), 0)
            for generator in block_gens
        )
        and flattened_span_rank(
            [*clifford_basis(block_gens)[0], block_external]
        ) == 2**3 + 1
    )
    lattice_generators = [np.kron(I2, generator) for generator in block_gens]
    lattice_candidate = np.kron(I2, block_external)
    lattice_identity = np.eye(lattice_candidate.shape[0], dtype=complex)
    lattice_internal_basis = [
        np.kron(I2, basis_element)
        for basis_element in clifford_basis(block_gens)[0]
    ]
    lattice_wide_countercontrol = (
        np.allclose(lattice_candidate @ lattice_candidate, lattice_identity)
        and all(
            np.allclose(anticommutator(lattice_candidate, generator), 0)
            for generator in lattice_generators
        )
        and flattened_span_rank([*lattice_internal_basis, lattice_candidate])
        == flattened_span_rank(lattice_internal_basis) + 1
    )

n5_controls = {
    "per_element": (
        coefficient_cancellation_ok,
        "CLOSED_AT_CLAIMED_SCOPE",
        "faithful internal coefficient kernels have nullity zero for odd n=1,3,5",
    ),
    "per_site": (
        per_site_nullity == 0,
        "FINITE_SPECIALIZATION_CLOSED",
        f"one-site Pauli ambient common anticommutant has nullity {per_site_nullity}",
    ),
    "per_mode": (
        per_mode_has_anticommuter,
        "COUNTEREXAMPLE_TO_BROADER_READING",
        "sigma_y is a square-one anticommuter for the single sigma_x mode",
    ),
    "per_block": (
        per_block_countercontrol,
        "COUNTEREXAMPLE_TO_BROADER_READING",
        "the doubled faithful odd carrier has an external block anticommuter",
    ),
    "lattice_wide": (
        lattice_wide_countercontrol,
        "COUNTEREXAMPLE_TO_BROADER_READING",
        "a two-site lift has an ambient anticommuter outside its internal span",
    ),
}
for resolution_class, (ok, _disposition, description) in n5_controls.items():
    check(f"N5 live {resolution_class} control", ok, detail=description)

n5_controls_ok = phrase_manifest_ok and all(
    result[0] for result in n5_controls.values()
)

if all(route_results.values()) and n5_controls_ok:
    print(
        "  N1_ROUTE route_id=coefficient-cancellation; route_class=algebraic_rearrangement; "
        "honesty_marker=ATTEMPTED; disposition=CLOSED; mechanism=arbitrary coefficient "
        "cancellation in the simultaneous anticommutator algebra; attempt=solve the stacked "
        "full coefficient kernel after certifying the 2^n monomial span is faithful; "
        "outcome=odd internal nullity is zero for n=1,3,5"
    )
    print(
        "  N1_ROUTE route_id=central-volume; route_class=symmetry_or_representation; "
        "honesty_marker=ATTEMPTED; disposition=CLOSED; mechanism=central invertible odd volume "
        "representation; attempt=verify centrality and invertibility while an all-generator "
        "anticommuter crosses an odd product with negative sign; outcome=commuting and "
        "anticommuting with invertible omega forces M=0"
    )
    print(
        "  N1_ROUTE route_id=external-matrix-carrier; route_class=alternate_carrier_or_sector; "
        "honesty_marker=ATTEMPTED; disposition=CLOSED; mechanism=alternate ambient matrix "
        "carrier outside the internal Clifford span; attempt=search Pauli tensor words for an "
        "involution that anticommutes with every odd generator and raises the internal span "
        f"rank; outcome=external witnesses found outside Cl(n), cases={external_carrier_cases}"
    )
    print(
        "  N1_ROUTE route_id=extension-dimension; route_class=numerical_or_finite_case; "
        "honesty_marker=ATTEMPTED; disposition=CLOSED; mechanism=finite dimension-doubling "
        "test of universal extension by an anticommuting square-one generator; "
        "attempt=compare the faithful Cl_n span with the span after adjoining the candidate "
        "and candidate-times-basis products; outcome="
        f"ranks double from 2^n to 2^(n+1), cases={extension_dimension_cases}"
    )
    print(
        "  N1_ROUTE route_id=central-idempotent-exchange; "
        "route_class=topology_or_global_structure; honesty_marker=ATTEMPTED; "
        "disposition=CLOSED; mechanism=global semisimple-algebra structure through two "
        "nonzero central volume idempotents; attempt=test that the grade automorphism "
        "exchanges the central summands while internal conjugation fixes the center; "
        f"outcome=nonzero exchanged idempotents, cases={central_idempotent_cases}"
    )
    print(
        "  N1_SUBCHECK zero-square-normalization is downstream of the zero kernel; "
        f"generic-parity-witness covers {parity_witness_count} finite subset cases; "
        f"signature-rephasing covers {signature_rephase_cases} convention cases; "
        "none is counted as an independent N1 route"
    )

    for group in phrase_groups:
        locator = str(group["locator"]).replace(";", ",")
        print(
            "  N5_GROUP "
            f"group_id={group['group_id']}; phrase={group['phrase']}; "
            f"occurrence_count={group['occurrence_count']}; "
            f"locator_sha256={group['locator_sha256']}; locator={locator}"
        )
        for resolution_class, (
            _ok,
            disposition,
            description,
        ) in n5_controls.items():
            print(
                "  N5_RESOLUTION "
                f"group={group['group_id']} {resolution_class}: "
                f"live_test=PASS; disposition={disposition}; {description}"
            )

    print(
        "  N7_STEELMAN_ARGUMENT mechanism=alternate ambient matrix carrier outside the "
        "internal Clifford span; attempt=search Pauli tensor words for an involution that "
        "anticommutes with every odd generator and raises the internal span rank; argument=a "
        "hostile reviewer can defeat any claim about all represented operators by doubling "
        "the odd carrier and adjoining the missing even-tower generator, so only a verified "
        "internal-span boundary can support the theorem."
    )
    print(
        "  N7_PRIMARY_DISPOSITION no nonzero M in Cl(n) satisfies (5) internal wall remains "
        "properly scoped after the ambient-carrier attack; the independent helper must "
        "reauthenticate the span-rank separation on a distinct execution surface."
    )


# ============================================================================
section("Narrow theorem summary")
# ============================================================================
print(
    """
  Narrow Pattern A theorem statement:

  HYPOTHESIS:
    Let n = p + q and let g_1, ..., g_n be n generators of Cl(p, q) over C
    satisfying g_mu^2 = +/- I and {g_mu, g_nu} = 0 for mu != nu.

  CONCLUSION (volume-element identity):
    omega := g_1 g_2 ... g_n satisfies
        omega g_mu = (-1)^(n-1) g_mu omega
    for every generator g_mu.

  CONCLUSION (chirality dichotomy):
    (a) n EVEN  =>  if q generators have negative square, then
                    gamma_5 := i^{n(n-1)/2+q} omega satisfies
                    gamma_5^2 = +I and {gamma_5, g_mu} = 0 for every mu;
                    the canonical Z_2 grading has an internal implementer.

    (b) n ODD   =>  no element M of the internal Clifford algebra satisfies
                    M^2 = +I together with {M, g_mu} = 0 for every mu;
                    the canonical grading has no internal implementer.

  CONCLUSION (conditional framework specialisation):
    If the total algebra is Cl(d_s, d_t), existence of an internal
    chirality involution requires d_s + d_t even. The accepted Lattice
    premise fixes d_s = 3, so this condition forces d_t to be ODD:
    d_t in {1, 3, 5, ...}.

  Audit-lane class:
    (A) -- pure Clifford-algebra fact with a symbolic proof and deterministic
    numerical matrix smoke tests on n=1,...,6.

  Out of scope:
    -- gauge-anomaly arithmetic (Tr[Y], Tr[Y^3], etc.);
    -- choice of d_t = 1 over d_t in {3, 5, ...};
    -- single-clock codimension-1 evolution structure;
    -- ABJ anomaly-to-inconsistency implication;
    -- physical Standard-Model fermion content;
    -- emergent Lorentz boost covariance.
"""
)


print(f"\n{'='*88}\n  TOTAL: PASS={PASS}, FAIL={FAIL}\n{'='*88}")
sys.exit(1 if FAIL > 0 else 0)
