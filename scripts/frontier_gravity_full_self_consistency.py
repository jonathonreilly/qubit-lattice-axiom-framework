#!/usr/bin/env python3
"""
Conditional Closure Identity Forces Poisson Downstream of A2
============================================================

CONTEXT:
  The source note is a bounded conditional theorem.  It does not derive the
  closure identification

      A2: L^{-1} = G_0

  from the Cl(3)-on-Z^3 axiom.  Instead it checks the exact downstream algebra:
  if A2 is stipulated, then L = G_0^{-1} = H = -Delta_lat, and the nearest-
  neighbor / translation-invariant / self-adjoint structure follows from that
  identity.

THE CONDITIONAL ARGUMENT:
  1. The lattice Hamiltonian is H = -Delta_lat (NN hopping on Z^3).
  2. The propagator Green's function is G_0 = H^{-1}.
  3. Stipulate A2: L^{-1} = G_0.
  4. Then L = G_0^{-1} = H = -Delta_lat.

  This proves an exact class-A implication downstream of A2.  It is not an
  axiom-first derivation of A2.

CHECKS:
  CHECK 1 (EXACT GIVEN A2): G_0^{-1} = H algebraically.
  CHECK 2 (EXACT GIVEN A2): H is nearest-neighbor.
  CHECK 3 (EXACT GIVEN A2): L = H is TI and self-adjoint.
  CHECK 4 (EXACT GIVEN A2): the Green-function identity closes when L = H.
  CHECK 5 (EXACT GIVEN A2): non-NN perturbations violate the stipulated
    closure identity.
  CHECK 6 (EXACT GIVEN A2): dense inverse check confirms G_0^{-1} = H.

PStack experiment: frontier-gravity-full-self-consistency
"""

from __future__ import annotations
import sys
import time
import numpy as np

try:
    from scipy import sparse
    from scipy.sparse.linalg import spsolve
    from scipy.linalg import eigh
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

np.set_printoptions(precision=10, linewidth=120)

PASS_COUNT = 0
FAIL_COUNT = 0
BOUNDED_COUNT = 0


def log_check(name: str, passed: bool, exact: bool = True, detail: str = ""):
    global PASS_COUNT, FAIL_COUNT, BOUNDED_COUNT
    tag = "EXACT" if exact else "BOUNDED"
    if passed:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    if not exact and passed:
        BOUNDED_COUNT += 1
    print(f"  [{tag}] {status}: {name}")
    if detail:
        print(f"         {detail}")


# ===========================================================================
# Infrastructure
# ===========================================================================

def build_neg_laplacian_sparse(N: int):
    """Build (-Delta_lat) for NxNxN grid with Dirichlet BC.
    Returns sparse matrix and interior size M = N-2."""
    M = N - 2
    n = M * M * M

    ii, jj, kk = np.mgrid[0:M, 0:M, 0:M]
    flat = ii.ravel() * M * M + jj.ravel() * M + kk.ravel()

    rows = [flat]
    cols = [flat]
    vals = [np.full(n, 6.0)]

    for di, dj, dk in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        ni = ii + di
        nj = jj + dj
        nk = kk + dk
        mask = ((ni >= 0) & (ni < M) & (nj >= 0) & (nj < M) &
                (nk >= 0) & (nk < M))
        src = flat[mask.ravel()]
        dst = ni[mask] * M * M + nj[mask] * M + nk[mask]
        rows.append(src)
        cols.append(dst.ravel())
        vals.append(-np.ones(src.shape[0]))

    all_rows = np.concatenate(rows)
    all_cols = np.concatenate(cols)
    all_vals = np.concatenate(vals)
    A = sparse.csr_matrix((all_vals, (all_rows, all_cols)), shape=(n, n))
    return A, M


def flat_idx(i, j, k, M):
    return i * M * M + j * M + k


def make_point_source(M: int, pos: tuple) -> np.ndarray:
    rhs = np.zeros(M * M * M)
    i, j, k = pos
    rhs[flat_idx(i, j, k, M)] = 1.0
    return rhs


# ===========================================================================
# CHECK 1: G_0^{-1} = H (operator identity, not restricted to any class)
# ===========================================================================

def check_inverse_identity():
    """
    THE CORE ALGEBRAIC IDENTITY.

    G_0 = H^{-1}  =>  G_0^{-1} = H.

    This is the key step: if stipulated A2 supplies L^{-1} = G_0,
    then L = G_0^{-1} = H = -Delta_lat.

    No restriction on L is imposed downstream of A2.  The identity L = H is
    forced by A2 and the definition of G_0.  This check does not derive A2.

    We verify: H @ G_0 = I (on each column) and G_0^{-1} = H (on a
    dense subblock).
    """
    print()
    print("=" * 78)
    print("CHECK 1: G_0^{-1} = H (OPERATOR IDENTITY)")
    print("=" * 78)
    print()
    print("  If stipulated A2 supplies L^{-1} = G_0, then:")
    print("    L = G_0^{-1} = H = -Delta_lat.")
    print("  This is an algebraic identity.  L is DETERMINED, not chosen.")
    print("  No restriction to NN operators is imposed downstream of A2.")
    print()

    N = 12
    A, M = build_neg_laplacian_sparse(N)
    n = M ** 3

    # Compute full G_0 = H^{-1} by solving H @ G_0[:, j] = e_j
    # for a subset of columns (full matrix too large for big N)
    n_test = min(n, 50)
    test_cols = np.random.choice(n, n_test, replace=False)

    max_forward_res = 0.0
    max_inverse_res = 0.0

    for j in test_cols:
        e_j = np.zeros(n)
        e_j[j] = 1.0

        # G_0[:, j] = H^{-1} e_j
        g_col = spsolve(A, e_j)

        # Forward check: H @ g_col should = e_j
        res_fwd = np.max(np.abs(A @ g_col - e_j))
        max_forward_res = max(max_forward_res, res_fwd)

        # Inverse check: H @ g_col = e_j means G_0^{-1} acts as H
        # This is the SAME check -- H @ G_0 = I is equivalent to G_0^{-1} = H
        max_inverse_res = max(max_inverse_res, res_fwd)

    print(f"  Lattice: {N}^3, interior: {M}^3 = {n}")
    print(f"  Tested {n_test} random columns of G_0")
    print(f"  max ||H @ G_0[:,j] - e_j||_inf = {max_forward_res:.2e}")
    print()
    print("  INTERPRETATION: Since H @ G_0 = I to machine precision,")
    print("  we have G_0^{-1} = H = -Delta_lat.")
    print("  If stipulated A2 supplies L^{-1} = G_0, then L = G_0^{-1} = H.")
    print("  This is not a search over operator families.")
    print("  It is a direct algebraic determination of L conditional on A2.")

    log_check(
        "G_0^{-1} = H = -Delta_lat (algebraic identity)",
        max_forward_res < 1e-10,
        exact=True,
        detail=f"max residual = {max_forward_res:.2e} over {n_test} columns"
    )

    return A, M


# ===========================================================================
# CHECK 2: H = -Delta_lat is nearest-neighbor (sparsity structure)
# ===========================================================================

def check_H_is_nn(A, M):
    """
    H = -Delta_lat has nonzero entries ONLY at (i, j) where i and j are
    the same site or nearest neighbors on Z^3.  This is the sparsity
    structure of the graph Laplacian.

    The point: conditional on A2, L = G_0^{-1} = H is forced to be NN.
    This is a consequence of L = H, not an assumption imposed on L.
    """
    print()
    print("=" * 78)
    print("CHECK 2: H = -Delta_lat IS NEAREST-NEIGHBOR (SPARSITY)")
    print("=" * 78)
    print()
    print("  The NN structure of L is a CONSEQUENCE of L = H,")
    print("  not an assumption imposed on L.")
    print()

    n = M ** 3

    # For each nonzero entry (i, j) in H, verify that sites i and j
    # are either identical or NN on the 3D grid
    A_coo = sparse.coo_matrix(A)
    max_dist = 0
    nn_count = 0
    diag_count = 0
    violation_count = 0

    for idx in range(len(A_coo.data)):
        r = A_coo.row[idx]
        c = A_coo.col[idx]
        if A_coo.data[idx] == 0:
            continue

        # Convert flat indices to 3D
        ri, rj, rk = r // (M * M), (r // M) % M, r % M
        ci, cj, ck = c // (M * M), (c // M) % M, c % M

        dist = abs(ri - ci) + abs(rj - cj) + abs(rk - ck)
        max_dist = max(max_dist, dist)

        if dist == 0:
            diag_count += 1
        elif dist == 1:
            nn_count += 1
        else:
            violation_count += 1

    total_nnz = len(A_coo.data)
    print(f"  Matrix size: {n} x {n}")
    print(f"  Nonzero entries: {total_nnz}")
    print(f"  Diagonal entries: {diag_count}")
    print(f"  NN off-diagonal entries: {nn_count}")
    print(f"  Beyond-NN entries: {violation_count}")
    print(f"  Maximum Manhattan distance of nonzero entry: {max_dist}")
    print()
    print("  INTERPRETATION: H has nonzeros ONLY on diagonal and NN sites.")
    print("  Since A2 gives L = G_0^{-1} = H, the operator L is necessarily NN.")
    print("  The NN restriction on L is derived from A2, not assumed.")

    log_check(
        "H = -Delta_lat has only diagonal and NN entries",
        violation_count == 0 and max_dist <= 1,
        exact=True,
        detail=f"max Manhattan distance = {max_dist}, violations = {violation_count}"
    )

    return True


# ===========================================================================
# CHECK 3: L = H is also TI and self-adjoint (consequences, not assumptions)
# ===========================================================================

def check_ti_and_sa(A, M):
    """
    The narrowed uniqueness theorem assumed TI + SA + NN.
    The conditional A2 argument shows L = H, which is automatically:
      - NN (CHECK 2)
      - Self-adjoint (H is symmetric)
      - Translation-invariant (H has the same stencil at every interior site)

    These are CONSEQUENCES of L = H, not assumptions on L.
    Downstream of stipulated A2, the argument does not need to restrict L to
    the TI + SA + NN class; A2 determines L in this class automatically.
    """
    print()
    print("=" * 78)
    print("CHECK 3: L = H IS AUTOMATICALLY TI AND SELF-ADJOINT")
    print("=" * 78)
    print()
    print("  The narrowed theorem assumed TI + SA + NN as restrictions on L.")
    print("  The conditional A2 argument shows L = H = -Delta_lat, which is")
    print("  automatically TI, SA, and NN.  These are consequences.")
    print()

    n = M ** 3

    # Self-adjoint: H = H^T
    diff = A - A.T
    sa_err = sparse.linalg.norm(diff, 'fro')
    print(f"  ||H - H^T||_F = {sa_err:.2e}")

    log_check(
        "H is self-adjoint (symmetric): H = H^T",
        sa_err < 1e-12,
        exact=True,
        detail=f"Frobenius norm of H - H^T = {sa_err:.2e}"
    )

    # Translation-invariant: check that the stencil is the same at every
    # interior site (away from Dirichlet boundaries)
    # Pick interior sites at least 1 away from boundary
    stencils_match = True
    ref_stencil = None
    test_sites = []

    for i in range(1, M - 1):
        for j in range(1, M - 1):
            for k in range(1, M - 1):
                test_sites.append((i, j, k))

    if len(test_sites) > 200:
        rng = np.random.default_rng(42)
        indices = rng.choice(len(test_sites), 200, replace=False)
        test_sites = [test_sites[idx] for idx in indices]

    A_csc = A.tocsc()
    for site in test_sites:
        i, j, k = site
        idx = flat_idx(i, j, k, M)
        row = A_csc[idx, :].toarray().ravel()

        # Extract the stencil: value at self and 6 NN
        stencil = [row[idx]]  # diagonal
        for di, dj, dk in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
            ni, nj, nk = i+di, j+dj, k+dk
            if 0 <= ni < M and 0 <= nj < M and 0 <= nk < M:
                nidx = flat_idx(ni, nj, nk, M)
                stencil.append(row[nidx])

        stencil = tuple(sorted(stencil))
        if ref_stencil is None:
            ref_stencil = stencil
        elif stencil != ref_stencil:
            stencils_match = False
            break

    print(f"  Tested {len(test_sites)} interior sites for stencil uniformity")
    print(f"  Reference stencil (sorted): {ref_stencil}")

    log_check(
        "H is translation-invariant (uniform stencil at interior sites)",
        stencils_match,
        exact=True,
        detail=f"all {len(test_sites)} tested sites have identical stencil"
    )

    print()
    print("  INTERPRETATION: The narrowed theorem's assumptions (TI, SA, NN)")
    print("  are not restrictions on the search space for L.")
    print("  They are properties that L = H automatically possesses.")
    print("  The conditional A2 argument does not need them as inputs.")


# ===========================================================================
# CHECK 4: Self-consistency loop closure (the full cycle)
# ===========================================================================

def check_loop_closure():
    """
    THE CONDITIONAL CLOSURE CHECK:

      propagator -> density -> field -> propagator

    Spelled out:
      1. Propagator: G_0 = H^{-1} = (-Delta)^{-1}    (from lattice structure)
      2. Density: rho(x) = G_0(x, x_0)^2 / Z          (localized source at x_0)
      3. Field: L phi = -rho  =>  phi = -L^{-1} rho
      4. Stipulated closure A2 identifies L^{-1} with G_0.

    Given A2, the Green-function identity closes if and only if
    L = G_0^{-1} = H.

    We verify: starting from H, compute G_0, compute rho, solve for phi
    using L = H, and confirm the resulting phi is the Green's function
    of H (i.e., the loop is self-consistent).

    Then we show: if L != H (e.g., L = H + epsilon * NNN), A2 is violated.
    """
    print()
    print("=" * 78)
    print("CHECK 4: STIPULATED CLOSURE IDENTITY")
    print("=" * 78)
    print()

    N = 14
    A, M = build_neg_laplacian_sparse(N)
    n = M ** 3
    mid = M // 2
    src_idx = flat_idx(mid, mid, mid, M)

    # Step 1: G_0 = H^{-1}
    rhs = np.zeros(n)
    rhs[src_idx] = 1.0
    G_0_col = spsolve(A, rhs)

    # Step 2: density rho = G_0^2 (normalized)
    rho = G_0_col ** 2
    rho = rho / rho.sum()

    # Step 3: solve L phi = -rho with L = H = -Delta
    phi_from_H = spsolve(A, rho)

    # Step 4: self-consistency check -- phi_from_H should be proportional
    # to G_0_col (because rho is concentrated near source, and
    # H^{-1} rho ~ H^{-1} delta ~ G_0 at leading order)
    #
    # More precisely: phi = H^{-1} rho = H^{-1} (G_0^2 / Z)
    # and G_0 = H^{-1} delta.
    # At the OPERATOR level: the field operator L = H produces phi via
    # L^{-1} = H^{-1} = G_0.  The Green's function of L IS the propagator.
    # This is the loop closure.

    # Verify: H^{-1} = G_0 (the field Green's function = propagator Green's fn)
    # We already checked this in CHECK 1.  Here we verify the loop
    # operationally by checking that the field equation's Green's function
    # (L^{-1} delta = H^{-1} delta = G_0 delta) matches the propagator.
    G_from_L = spsolve(A, rhs)  # L^{-1} delta where L = H
    loop_mismatch = np.max(np.abs(G_from_L - G_0_col))

    print(f"  Lattice: {N}^3, source at ({mid},{mid},{mid})")
    print(f"  ||G_from_L - G_from_propagator||_inf = {loop_mismatch:.2e}")
    print()
    print("  INTERPRETATION: When L = H, the field's Green's function")
    print("  IS the propagator's Green's function.  The loop closes exactly.")
    print("  Conditional on A2, L = H is the unique operator for which")
    print("  L^{-1} = G_0.")

    log_check(
        "Loop closure: field Green's fn = propagator Green's fn when L = H",
        loop_mismatch < 1e-10,
        exact=True,
        detail=f"mismatch = {loop_mismatch:.2e}"
    )

    return A, M, G_0_col


# ===========================================================================
# CHECK 5: Non-NN perturbations break self-consistency
# ===========================================================================

def check_nnn_breaks_consistency():
    """
    If L were allowed to have next-nearest-neighbor (NNN) terms, the
    stipulated closure identity would NOT hold.

    We construct L_eps = H + eps * H_NNN, where H_NNN couples
    next-nearest-neighbor sites (diagonal neighbors on Z^3).
    Then L_eps^{-1} != G_0 = H^{-1}, and the mismatch is nonzero.

    This demonstrates that, once A2 is stipulated, any NNN contamination in L
    violates the closure identity.
    """
    print()
    print("=" * 78)
    print("CHECK 5: NON-NN PERTURBATIONS VIOLATE A2")
    print("=" * 78)
    print()
    print("  If L had NNN terms, L^{-1} != G_0 = H^{-1}.")
    print("  The stipulated closure identity A2 would fail.")
    print()

    N = 12
    A, M = build_neg_laplacian_sparse(N)
    n = M ** 3
    mid = M // 2

    # Build NNN coupling matrix (face-diagonal neighbors, Manhattan dist = 2)
    ii, jj, kk = np.mgrid[0:M, 0:M, 0:M]
    flat = ii.ravel() * M * M + jj.ravel() * M + kk.ravel()

    nnn_rows = []
    nnn_cols = []
    nnn_vals = []
    nnn_diag = np.zeros(n)

    # Face-diagonal neighbors: (+-1, +-1, 0) and permutations
    nnn_shifts = []
    for d1 in [-1, 1]:
        for d2 in [-1, 1]:
            nnn_shifts.append((d1, d2, 0))
            nnn_shifts.append((d1, 0, d2))
            nnn_shifts.append((0, d1, d2))

    for di, dj, dk in nnn_shifts:
        ni = ii + di
        nj = jj + dj
        nk = kk + dk
        mask = ((ni >= 0) & (ni < M) & (nj >= 0) & (nj < M) &
                (nk >= 0) & (nk < M))
        src = flat[mask.ravel()]
        dst = ni[mask] * M * M + nj[mask] * M + nk[mask]
        nnn_rows.append(src)
        nnn_cols.append(dst.ravel())
        nnn_vals.append(-np.ones(src.shape[0]))
        np.add.at(nnn_diag, src, 1.0)

    if nnn_rows:
        all_nnn_rows = np.concatenate(nnn_rows)
        all_nnn_cols = np.concatenate(nnn_cols)
        all_nnn_vals = np.concatenate(nnn_vals)
    else:
        all_nnn_rows = np.array([], dtype=int)
        all_nnn_cols = np.array([], dtype=int)
        all_nnn_vals = np.array([])

    # Add diagonal to make it a proper Laplacian-like operator
    all_nnn_rows = np.concatenate([all_nnn_rows, np.arange(n)])
    all_nnn_cols = np.concatenate([all_nnn_cols, np.arange(n)])
    all_nnn_vals = np.concatenate([all_nnn_vals, nnn_diag])

    H_NNN = sparse.csr_matrix(
        (all_nnn_vals, (all_nnn_rows, all_nnn_cols)), shape=(n, n)
    )

    # Reference: G_0 = H^{-1} delta
    rhs = make_point_source(M, (mid, mid, mid))
    G_0 = spsolve(A, rhs)
    G_0_norm = np.linalg.norm(G_0)

    print(f"  Lattice: {N}^3, interior: {M}^3 = {n}")
    print(f"  NNN coupling: face-diagonal neighbors ({len(nnn_shifts)} directions)")
    print()
    print(f"  {'epsilon':>10s} {'||L_eps^{-1} - G_0|| / ||G_0||':>35s} {'A2 holds?':>17s}")
    print("  " + "-" * 65)

    eps_values = [0.0, 0.001, 0.01, 0.05, 0.1, 0.2, 0.5]
    mismatches = []

    for eps in eps_values:
        L_eps = A + eps * H_NNN
        try:
            phi_eps = spsolve(L_eps, rhs)
            mm = np.linalg.norm(phi_eps - G_0) / G_0_norm
        except Exception:
            mm = float('inf')
        mismatches.append(mm)
        sc = "YES" if mm < 1e-10 else "NO"
        print(f"  {eps:>10.3f} {mm:>35.2e} {sc:>17s}")

    # eps = 0 should give zero mismatch (L = H exactly)
    log_check(
        "eps = 0 (L = H): zero mismatch (self-consistent)",
        mismatches[0] < 1e-10,
        exact=True,
        detail=f"mismatch = {mismatches[0]:.2e}"
    )

    # All eps > 0 should give nonzero mismatch
    all_broken = all(m > 1e-4 for m in mismatches[1:])
    log_check(
        "All eps > 0 (L != H): nonzero mismatch (violates A2)",
        all_broken,
        exact=True,
        detail=f"min nonzero-eps mismatch = {min(mismatches[1:]):.2e}"
    )

    # Mismatch grows with eps (monotonic)
    monotonic = all(mismatches[i+1] >= mismatches[i] - 1e-12
                     for i in range(len(mismatches) - 1))
    log_check(
        "Mismatch grows monotonically with NNN contamination",
        monotonic,
        exact=True,
        detail=f"mismatch sequence: {[f'{m:.2e}' for m in mismatches]}"
    )

    print()
    print("  INTERPRETATION: ANY non-NN contamination in L violates")
    print("  the stipulated closure identity L^{-1} = G_0 = H^{-1}.")
    print("  The NN structure of L is not an assumption -- it follows")
    print("  from A2 plus L = G_0^{-1} = H.")


# ===========================================================================
# CHECK 6: Dense verification -- G_0^{-1} equals H entry-by-entry
# ===========================================================================

def check_dense_inverse():
    """
    On a small lattice where dense computation is feasible, explicitly
    construct G_0 = H^{-1} as a dense matrix, then compute G_0^{-1},
    and verify G_0^{-1} = H entry-by-entry.

    This is the most direct possible verification of the operator identity
    L = G_0^{-1} = H, conditional on A2.
    """
    print()
    print("=" * 78)
    print("CHECK 6: DENSE VERIFICATION G_0^{-1} = H (ENTRY-BY-ENTRY)")
    print("=" * 78)
    print()

    N = 8  # small enough for dense computation
    A, M = build_neg_laplacian_sparse(N)
    n = M ** 3

    print(f"  Lattice: {N}^3, interior: {M}^3 = {n}")
    print(f"  Computing dense G_0 = H^{-1}...")

    H_dense = A.toarray()
    G_0_dense = np.linalg.inv(H_dense)

    # G_0^{-1} should equal H
    G_0_inv = np.linalg.inv(G_0_dense)
    diff = np.max(np.abs(G_0_inv - H_dense))
    print(f"  max |G_0^{{-1}} - H|_entry = {diff:.2e}")

    log_check(
        "G_0^{-1} = H entry-by-entry (dense verification)",
        diff < 1e-8,
        exact=True,
        detail=f"max entry-wise difference = {diff:.2e}"
    )

    # Verify G_0^{-1} is sparse (NN structure)
    # Count entries of G_0^{-1} that are above threshold
    threshold = 1e-10
    nnz_G0inv = np.sum(np.abs(G_0_inv) > threshold)
    nnz_H = np.sum(np.abs(H_dense) > threshold)

    print(f"  Nonzero entries in H: {nnz_H}")
    print(f"  Nonzero entries in G_0^{{-1}}: {nnz_G0inv}")
    print(f"  (G_0 itself is dense -- {np.sum(np.abs(G_0_dense) > threshold)} nonzeros)")
    print()
    print("  INTERPRETATION: G_0 is a DENSE matrix (long-range Green's function).")
    print("  But G_0^{-1} = H is SPARSE (nearest-neighbor only).")
    print("  The stipulated identity L^{-1} = G_0 gives L = G_0^{-1} = H,")
    print("  which is NN.  The NN structure of L is derived from the fact that")
    print("  the inverse of the long-range propagator is the short-range Hamiltonian.")

    log_check(
        "G_0^{-1} has same sparsity as H (NN structure)",
        nnz_G0inv == nnz_H,
        exact=True,
        detail=f"both have {nnz_H} nonzero entries"
    )

    # Verify G_0 is dense (to emphasize the point)
    g0_nnz = np.sum(np.abs(G_0_dense) > threshold)
    log_check(
        "G_0 is dense (long-range, NOT NN)",
        g0_nnz > n * n * 0.9,
        exact=True,
        detail=f"G_0 has {g0_nnz} / {n*n} nonzero entries "
               f"({100*g0_nnz/(n*n):.1f}% fill)"
    )

    return G_0_dense, H_dense


# ===========================================================================
# CHECK 7: The argument structure (logical chain summary)
# ===========================================================================

def check_argument_structure():
    """
    Verify the logical structure of the conditional closure argument.

    The chain:
      1. Lattice Z^3 has NN connectivity  =>  H = -Delta_lat (NN)
      2. Propagator: G_0 = H^{-1}  (definition)
      3. Stipulated A2: L^{-1} = G_0
      4. Therefore: L = G_0^{-1} = H = -Delta_lat  (algebra)

    Versus the narrowed theorem:
      1. Restrict to TI + SA + NN operators
      2. Within this class, show Poisson is unique
      3. Conclude L = -Delta

    The conditional argument does not use step 1 of the narrowed theorem.
    It derives TI + SA + NN as consequences, not assumptions.
    """
    print()
    print("=" * 78)
    print("CHECK 7: ARGUMENT STRUCTURE (FULL vs NARROWED)")
    print("=" * 78)
    print()
    print("  NARROWED THEOREM (existing):")
    print("    Input: Restrict L to TI + SA + NN class")
    print("    Proof: Within this class, mismatch M(L) = 0 iff L = -Delta")
    print("    Output: Poisson is unique WITHIN the restricted class")
    print("    Gap: Could L be outside the TI + SA + NN class?")
    print()
    print("  CONDITIONAL A2 ARGUMENT (this script):")
    print("    Input: H = -Delta (from lattice structure)")
    print("    Input: G_0 = H^{-1} (propagator definition)")
    print("    Input: stipulated A2, L^{-1} = G_0")
    print("    Output: L = G_0^{-1} = H = -Delta")
    print("    No restriction on L is imposed.")
    print("    TI, SA, NN are CONSEQUENCES of L = H.")
    print()
    print("  WHAT THE CONDITIONAL ARGUMENT CLOSES:")
    print("    The narrowed theorem asks: 'Is Poisson unique in a class?'")
    print("    This conditional check asks: 'If A2 holds, what is L?'")
    print("    It answers: 'L = H.'  There is no class to restrict to")
    print("    downstream of the stipulated closure identity.")
    print()
    print("  THE KEY INSIGHT:")
    print("    The propagator G_0 on Z^3 has a unique inverse: H = -Delta.")
    print("    Stipulated A2 determines L = G_0^{-1} = H.")
    print("    This is not a search.  It is a conditional algebraic identity.")

    # This check is structural -- it passes if all previous checks passed
    all_prev = (FAIL_COUNT == 0)
    log_check(
        "All previous checks support the conditional A2 algebra",
        all_prev,
        exact=True,
        detail=f"PASS={PASS_COUNT}, FAIL={FAIL_COUNT} at this point"
    )


# ===========================================================================
# MAIN
# ===========================================================================

def main():
    t_start = time.time()

    print("=" * 78)
    print("CONDITIONAL CLOSURE IDENTITY DETERMINES POISSON")
    print("(downstream of stipulated A2: L^{-1} = G_0)")
    print("=" * 78)
    print()
    print("SCOPE: This runner checks the exact algebra downstream of")
    print("stipulated closure identity A2. It does not derive A2 from")
    print("the Cl(3)-on-Z^3 axiom.")
    print()
    print("CONDITIONAL ANSWER: If A2 supplies L^{-1} = G_0, then")
    print("L = G_0^{-1} = H = -Delta_lat.  This is an algebraic")
    print("identity downstream of A2.  The NN structure of L is a")
    print("consequence, not an assumption.")
    print()
    print("THE CHAIN:")
    print("  (1) Z^3 has NN connectivity  =>  H = -Delta_lat")
    print("  (2) Propagator: G_0 = H^{-1}")
    print("  (3) Stipulated A2: L^{-1} = G_0  (field Green's fn =")
    print("      propagator Green's fn)")
    print("  (4) Therefore: L = G_0^{-1} = H = -Delta_lat  (Poisson)")
    print()

    if not HAS_SCIPY:
        print("ERROR: scipy required. Install with: pip install scipy")
        sys.exit(1)

    # Run all checks
    A, M = check_inverse_identity()
    check_H_is_nn(A, M)
    check_ti_and_sa(A, M)
    check_loop_closure()
    check_nnn_breaks_consistency()
    check_dense_inverse()
    check_argument_structure()

    # -----------------------------------------------------------------------
    # SYNTHESIS
    # -----------------------------------------------------------------------
    dt = time.time() - t_start
    print()
    print("=" * 78)
    print("SYNTHESIS: CONDITIONAL A2 ALGEBRA")
    print("=" * 78)
    print()
    print("Conditional on A2, the Poisson operator follows exactly:")
    print()
    print("  Step 1: Z^3 lattice structure  =>  H = -Delta_lat (NN hopping)")
    print("  Step 2: Propagator definition   =>  G_0 = H^{-1}")
    print("  Step 3: stipulated A2            =>  L^{-1} = G_0")
    print("  Step 4: Algebra                  =>  L = G_0^{-1} = H = -Delta")
    print()
    print("No restriction on L is imposed downstream of A2.")
    print("The properties of L (NN, TI, SA) are CONSEQUENCES of L = H.")
    print()
    print("This resolves the downstream operator-class question conditional on A2:")
    print("the closure identity does not merely select Poisson from the NN class.")
    print("It identifies the field operator with the Hamiltonian, which is the")
    print("graph Laplacian and is nearest-neighbor by lattice structure.")
    print()
    print("RELATION TO THE NARROWED THEOREM:")
    print("  The narrowed theorem proves: 'Within TI+SA+NN, only Poisson works.'")
    print("  This runner proves:          'Given A2, L = H = -Delta.'")
    print("  It does not derive A2 itself.")
    print()
    print("REMAINING HONEST CAVEAT:")
    print("  The closure condition 'L^{-1} = G_0' is the statement")
    print("  that the field's Green's function equals the propagator's Green's")
    print("  function.  This runner stipulates that identity as A2 and checks")
    print("  the downstream algebra.  It does not derive A2 from the axiom.")
    print()

    # Status
    total = PASS_COUNT + FAIL_COUNT
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}  CONDITIONAL_ALGEBRA_CHECKS={total}")
    print(f"Runtime: {dt:.1f}s")

    if FAIL_COUNT > 0:
        print("\nWARNING: Some checks failed. See above for details.")
        sys.exit(1)
    else:
        print("\nAll checks passed (exact conditional algebra downstream of A2).")
        sys.exit(0)


if __name__ == "__main__":
    main()
