#!/usr/bin/env python3
"""Independent boundary source from the microscopic source: the Schur bridge theorem.

What this runner establishes, on the zero-Dirichlet interior grid of a size-cubed
box with 6-NN negative Laplacian H_0:

  1. The three-block partition (I, t, b) of the interior sites -- strictly interior
     region I, shell trace t, exterior bulk b -- satisfies H_Ib = 0 exactly, because
     any exterior site adjacent to a non-exterior site is classified into t. This is
     verified numerically, not assumed.

  2. For an arbitrary microscopic source rho, the field phi solving H_0 phi = rho has
     its shell trace f = phi_t determined by the exact two-sided trace equation

         S f = j_micro
         S       = H_tt - H_tI H_II^{-1} H_It - H_tb H_bb^{-1} H_bt
         j_micro = rho_t - H_tI H_II^{-1} rho_I - H_tb H_bb^{-1} rho_b

     where j_micro is a functional of rho and the lattice operator alone. It never
     references f, never references a harmonic extension, and is never reconstructed
     from the target trace.

  3. S is symmetric positive definite, so f is the unique minimiser of
         I_R(g ; j_micro) = 1/2 g^T S g - j_micro^T g
     and grad I_R(f) = S f - j_micro = 0 carries predictive content.

  4. S = Lambda_R - H_tI H_II^{-1} H_It, where Lambda_R = H_tt - H_tb H_bb^{-1} H_bt
     is the exterior-only Schur complement. The interior Schur term is not negligible
     on this family, and pairing j_micro with Lambda_R alone fails to reproduce f.

  5. Exhibit: pairing Lambda_R with a source built as the trace flux of the harmonic
     extension of a trace vector g reproduces Lambda_R g identically for an ARBITRARY
     g, so the associated gradient residual vanishes for any trace whatsoever and
     therefore encodes no stationarity information about the physical configuration.

  6. Stationarity is rerun on the two source classes named by the audited row -- the
     exact local O_h class and the exact finite-rank class -- at size 15, the only
     size at which those builders are defined. For each class, the microscopic action
         A phi = eta,     A = H_0 - P W P^T,     eta = P m
     is assembled from the supplied support operator W and bare source m before any
     boundary trace is read. Eliminating I and b from A gives S_A f = j_A(eta).
     S_A^-1 j_A is then compared against phi|_t from the class's existing builder and
     against a separate full solve of A phi = eta.

The gates below are of two kinds. The rejectors are designed to fail if the implemented
object were wrong; the below-tolerance gates are exact algebraic identities of the
three-block elimination and therefore gate the implementation rather than the physics.
For the prescribed-rho checks, the reference trace f_true comes from a separate splu
factorisation and solve of the same H_0 -- a second elimination of the same
discretisation, not a second discretisation. For the two named classes, the bare-source
action route and the existing field builders are distinct code paths. No numerical gate
alone can detect a source reconstructed from a target trace; trace-independence is a
property of which arguments the construction reads and is established by inspection of
the source, with the full-action and existing-builder comparisons guarding consistency.
"""

from __future__ import annotations

import contextlib
import io
from dataclasses import dataclass

from _frontier_loader import load_frontier

import numpy as np
import scipy.sparse as sparse
from scipy.sparse.linalg import eigsh, spsolve, splu


SEED = 20260725
SIZES = (13, 15, 17)
CUTOFF_RADIUS = 4.0
CLASS_SIZE = 15

RECON_TOL = 1e-9
REJECT_TOL = 1e-3
MOVE_TOL = 1e-6


@dataclass
class Check:
    size: int
    gid: str
    ok: bool
    detail: str


CHECKS: list[Check] = []
# gid -> gate statement, including the quantity measured and the tolerance it must meet.
# Printed once as a legend; per-size lines then carry only the measured numbers, which
# keeps the whole report inside the audit packet's cached-stdout excerpt window.
GATES: dict[str, str] = {}
_CURRENT_SIZE = 0


def record(gid: str, gate: str, ok: bool, detail: str) -> None:
    GATES.setdefault(gid, gate)
    CHECKS.append(Check(size=_CURRENT_SIZE, gid=gid, ok=ok, detail=detail))


finite_rank = load_frontier("finite_rank_metric", "frontier_finite_rank_gravity_residual.py")
# The two source classes named by the row this runner supports. Their modules may print
# at import; only the import is silenced, and exceptions still propagate.
with contextlib.redirect_stdout(io.StringIO()):
    same_source = load_frontier("same_source_metric", "frontier_same_source_metric_ansatz_scan.py")
    coarse = load_frontier("coarse_grained", "frontier_coarse_grained_exterior_law.py")


# Dynamic Python imports are mutable repository inputs to the cached result. Keeping
# this literal list complete makes helper changes invalidate the source-pinned cache.
AUDIT_INPUT_PATHS = (
    "scripts/_frontier_loader.py",
    "scripts/frontier_finite_rank_gravity_residual.py",
    "scripts/frontier_same_source_metric_ansatz_scan.py",
    "scripts/frontier_coarse_grained_exterior_law.py",
)


def rel_inf(a: np.ndarray, b: np.ndarray) -> float:
    """Relative inf-norm distance of a from b."""
    denom = float(np.max(np.abs(b)))
    if denom == 0.0:
        return float(np.max(np.abs(a - b)))
    return float(np.max(np.abs(a - b))) / denom


@dataclass
class Blocks:
    """Operator-only data. Deliberately contains no field, trace or solution."""

    size: int
    interior: int
    n: int
    H0: sparse.csr_matrix
    idx_I: np.ndarray
    idx_t: np.ndarray
    idx_b: np.ndarray
    H_tt: np.ndarray
    H_tI: np.ndarray
    H_It: np.ndarray
    H_tb: np.ndarray
    H_bt: np.ndarray
    lu_II: object
    lu_bb: object
    lu_H0: object
    S: np.ndarray
    S_joint: np.ndarray
    Lambda_R: np.ndarray


@dataclass
class MicroscopicActionClass:
    """A supplied source class written before any boundary trace is solved."""

    label: str
    A: sparse.csr_matrix
    eta: np.ndarray
    support: np.ndarray
    normalization: str


def exterior_sets(size: int, cutoff_radius: float) -> tuple[np.ndarray, np.ndarray]:
    """Spell out the parent DtN runner's exterior classification locally."""
    center = (size - 1) / 2.0
    i, j, k = np.mgrid[0:size, 0:size, 0:size]
    radii = np.sqrt((i - center) ** 2 + (j - center) ** 2 + (k - center) ** 2)
    ext_full = np.zeros((size, size, size), dtype=bool)
    ext_full[1:-1, 1:-1, 1:-1] = (
        radii[1:-1, 1:-1, 1:-1] > cutoff_radius + 1e-12
    )

    interior = size - 2
    trace: list[int] = []
    bulk: list[int] = []
    neighbours = (
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    )
    for ii in range(1, size - 1):
        for jj in range(1, size - 1):
            for kk in range(1, size - 1):
                if not ext_full[ii, jj, kk]:
                    continue
                is_trace = any(
                    not ext_full[ii + di, jj + dj, kk + dk]
                    for di, dj, dk in neighbours
                )
                idx = finite_rank.flat_idx(ii - 1, jj - 1, kk - 1, interior)
                (trace if is_trace else bulk).append(idx)
    return np.asarray(trace, dtype=int), np.asarray(bulk, dtype=int)


def build_blocks(size: int, cutoff_radius: float) -> Blocks:
    trace_idx, bulk_idx = exterior_sets(size, cutoff_radius)
    H0, interior = finite_rank.build_neg_laplacian_sparse(size)
    n = interior ** 3
    idx_I = np.setdiff1d(np.arange(n), np.concatenate([trace_idx, bulk_idx]))

    H_tt = H0[trace_idx][:, trace_idx].toarray()
    H_tI = H0[trace_idx][:, idx_I].toarray()
    H_It = H0[idx_I][:, trace_idx].toarray()
    H_tb = H0[trace_idx][:, bulk_idx].toarray()
    H_bt = H0[bulk_idx][:, trace_idx].toarray()

    lu_II = splu(H0[idx_I][:, idx_I].tocsc())
    lu_bb = splu(H0[bulk_idx][:, bulk_idx].tocsc())
    lu_H0 = splu(H0.tocsc())

    # Theorem form: two one-sided Schur terms.
    S = H_tt - H_tI @ lu_II.solve(H_It) - H_tb @ lu_bb.solve(H_bt)

    # One joint Schur complement onto t over X = I union b, from a single factorisation
    # of H_XX. Its agreement with S is the numerical content of the block decoupling
    # H_Ib = 0: the two one-sided eliminations only reproduce the joint one when H_Ib
    # vanishes, so this comparison, unlike the split spelling below, can fail.
    idx_X = np.concatenate([idx_I, bulk_idx])
    H_tX = H0[trace_idx][:, idx_X].toarray()
    H_Xt = H0[idx_X][:, trace_idx].toarray()
    lu_XX = splu(H0[idx_X][:, idx_X].tocsc())
    S_joint = H_tt - H_tX @ lu_XX.solve(H_Xt)
    del H_tX, H_Xt, lu_XX

    # Exterior-only Schur complement, built exactly as
    # scripts/frontier_oh_schur_boundary_action.py builds it.
    if bulk_idx.size:
        X_sparse = spsolve(H0[bulk_idx][:, bulk_idx].tocsc(), H0[bulk_idx][:, trace_idx].tocsc())
        Lambda_R = np.asarray(H_tt - H_tb @ X_sparse)
    else:
        Lambda_R = H_tt.copy()

    return Blocks(
        size=size,
        interior=interior,
        n=n,
        H0=H0,
        idx_I=idx_I,
        idx_t=trace_idx,
        idx_b=bulk_idx,
        H_tt=H_tt,
        H_tI=H_tI,
        H_It=H_It,
        H_tb=H_tb,
        H_bt=H_bt,
        lu_II=lu_II,
        lu_bb=lu_bb,
        lu_H0=lu_H0,
        S=S,
        S_joint=S_joint,
        Lambda_R=Lambda_R,
    )


def independent_boundary_source(rho: np.ndarray, blk: Blocks) -> np.ndarray:
    """j_micro from the microscopic source alone.

    `rho` is the ONLY field argument. Nothing about the target trace, the solved
    field, or any harmonic extension enters here.
    """
    return (
        rho[blk.idx_t]
        - blk.H_tI @ blk.lu_II.solve(rho[blk.idx_I])
        - blk.H_tb @ blk.lu_bb.solve(rho[blk.idx_b])
    )


def boundary_source_variant(rho: np.ndarray, blk: Blocks, drop: str) -> np.ndarray:
    """Deliberately incomplete boundary sources, used only by the rejector gates."""
    term_t = rho[blk.idx_t]
    term_I = blk.H_tI @ blk.lu_II.solve(rho[blk.idx_I])
    term_b = blk.H_tb @ blk.lu_bb.solve(rho[blk.idx_b])
    if drop == "bulk":
        return term_t - term_I
    if drop == "interior":
        return term_t - term_b
    if drop == "trace":
        return -term_I - term_b
    raise ValueError(f"unknown dropped term: {drop}")


def true_trace_from_full_solve(rho: np.ndarray, blk: Blocks) -> np.ndarray:
    """Ground truth: solve the full n-site system and read off the shell trace."""
    phi = blk.lu_H0.solve(rho)
    return phi[blk.idx_t]


def harmonic_extension_trace_flux(g: np.ndarray, blk: Blocks) -> np.ndarray:
    """The previous construction, rebuilt directly.

    Extend an arbitrary trace vector `g` harmonically into the exterior bulk,
    leave the strictly interior region at zero, apply the full lattice operator
    and read the result on the shell. This is `(H_0 u_g)|_t`.
    """
    u = np.zeros(blk.n, dtype=float)
    u[blk.idx_t] = g
    if blk.idx_b.size:
        u[blk.idx_b] = blk.lu_bb.solve(-(blk.H_bt @ g))
    return (blk.H0 @ u)[blk.idx_t]


def build_sources(blk: Blocks) -> dict[str, np.ndarray]:
    rng = np.random.default_rng(SEED)
    n = blk.n

    centre = (blk.size - 1) // 2
    centre_flat = finite_rank.flat_idx(centre - 1, centre - 1, centre - 1, blk.interior)
    if centre_flat not in set(blk.idx_I.tolist()):
        raise RuntimeError("grid centre is not in the strictly interior region I")

    point = np.zeros(n, dtype=float)
    point[centre_flat] = 1.0

    interior_only = np.zeros(n, dtype=float)
    interior_only[blk.idx_I] = rng.standard_normal(blk.idx_I.size)

    bulk_only = np.zeros(n, dtype=float)
    bulk_only[blk.idx_b] = rng.standard_normal(blk.idx_b.size)

    mixed = np.zeros(n, dtype=float)
    mixed[blk.idx_I] = rng.standard_normal(blk.idx_I.size)
    mixed[blk.idx_t] = rng.standard_normal(blk.idx_t.size)
    mixed[blk.idx_b] = rng.standard_normal(blk.idx_b.size)

    return {
        "point source at centre": point,
        "random source in I": interior_only,
        "random source in b": bulk_only,
        "random source on I, t, b": mixed,
    }


def support_interaction(
    n: int, support: np.ndarray, W: np.ndarray
) -> sparse.csr_matrix:
    """Embed the supplied support operator W as P W P^T without a dense n x n P."""
    support = np.asarray(support, dtype=int)
    rows = np.repeat(support, support.size)
    cols = np.tile(support, support.size)
    out = sparse.csr_matrix((W.reshape(-1), (rows, cols)), shape=(n, n))
    out.eliminate_zeros()
    return out


def embed_support_source(n: int, support: np.ndarray, m: np.ndarray) -> np.ndarray:
    """Embed the supplied bare source m as eta = P m."""
    eta = np.zeros(n, dtype=float)
    eta[np.asarray(support, dtype=int)] = np.asarray(m, dtype=float)
    return eta


def trace_from_grid(phi_grid: np.ndarray, blk: Blocks) -> np.ndarray:
    """Read the class builder's interior field in the common flat-site convention."""
    phi_flat = np.ascontiguousarray(phi_grid[1:-1, 1:-1, 1:-1]).reshape(-1)
    if phi_flat.shape != (blk.n,):
        raise RuntimeError("source-class grid does not match the size-15 lattice")
    return phi_flat[blk.idx_t]


def audited_row_action_classes(
    blk: Blocks,
) -> dict[str, tuple[MicroscopicActionClass, np.ndarray]]:
    """Construct the audited row's two microscopic actions before reading a trace.

    The existing class builders are used only for the final reference traces. The
    matrices A and bare sources eta below are assembled directly from the source-class
    action data. In particular, neither eta nor the action Schur source is obtained by
    applying H_0 to a returned target field.
    """
    if blk.size != CLASS_SIZE:
        return {}

    # Exact local O_h class. These are the supplied class parameters in
    # same_source.build_best_phi_grid; the final equality against that builder is a
    # stale-parameter guard. Its amplitude convention max(phi|support)=0.35 is an
    # explicit normalization input. Computing that scalar uses only H_0, W and m,
    # before any shell trace is read.
    centre = blk.interior // 2
    support_oh = np.array(
        [
            finite_rank.flat_idx(
                centre + int(v[0]),
                centre + int(v[1]),
                centre + int(v[2]),
                blk.interior,
            )
            for v in same_source.SUPPORT_COORDS
        ],
        dtype=int,
    )
    W_oh = same_source.build_commutant_operator(
        0.0698, 0.0499, -0.0070, 0.0642, 0.1056
    )
    m_oh = same_source.build_invariant_source(0.8247, 0.2271)
    support_rhs = np.zeros((blk.n, support_oh.size), dtype=float)
    support_rhs[support_oh, np.arange(support_oh.size)] = 1.0
    G0P_oh = blk.lu_H0.solve(support_rhs)
    GS_oh = G0P_oh[support_oh, :]
    q_eff_oh = np.linalg.solve(np.eye(support_oh.size) - W_oh @ GS_oh, m_oh)
    phi_unscaled_oh = G0P_oh @ q_eff_oh
    scale_oh = 0.35 / float(np.max(phi_unscaled_oh[support_oh]))
    eta_oh = embed_support_source(blk.n, support_oh, scale_oh * m_oh)
    A_oh = blk.H0 - support_interaction(blk.n, support_oh, W_oh)

    # Broader finite-rank class. finite_rank_setup exposes the action data directly;
    # the imported full-field builder below follows a separate full-matrix solve.
    (
        class_size,
        H0_fr,
        interior_fr,
        support_fr_raw,
        _G0P_fr,
        _GS_fr,
        W_fr,
        m_fr,
    ) = finite_rank.finite_rank_setup()
    if class_size != blk.size or interior_fr != blk.interior:
        raise RuntimeError("finite-rank source class is not on the size-15 lattice")
    H0_delta = H0_fr - blk.H0
    H0_delta.eliminate_zeros()
    if H0_delta.nnz:
        raise RuntimeError("finite-rank source class uses a different H_0")
    support_fr = np.asarray(support_fr_raw, dtype=int)
    eta_fr = embed_support_source(blk.n, support_fr, m_fr)
    A_fr = blk.H0 - support_interaction(blk.n, support_fr, W_fr)

    with contextlib.redirect_stdout(io.StringIO()):
        f_oh = trace_from_grid(same_source.build_best_phi_grid(), blk)
        f_fr = trace_from_grid(coarse.build_finite_rank_phi_grid(), blk)

    return {
        "exact local O_h class": (
            MicroscopicActionClass(
                label="exact local O_h class",
                A=A_oh.tocsr(),
                eta=eta_oh,
                support=support_oh,
                normalization=f"max(phi|support)=0.35; source scale={scale_oh:.9e}",
            ),
            f_oh,
        ),
        "exact finite-rank class": (
            MicroscopicActionClass(
                label="exact finite-rank class",
                A=A_fr.tocsr(),
                eta=eta_fr,
                support=support_fr,
                normalization="bare source masses supplied by finite_rank_setup",
            ),
            f_fr,
        ),
    }


def action_boundary_equation(
    action: MicroscopicActionClass, blk: Blocks
) -> tuple[np.ndarray, np.ndarray, float, float, np.ndarray]:
    """Eliminate I and b from A phi = eta and return S_A, j_A and crosschecks."""
    A = action.A
    A_tt = A[blk.idx_t][:, blk.idx_t].toarray()
    A_tI = A[blk.idx_t][:, blk.idx_I].toarray()
    A_It = A[blk.idx_I][:, blk.idx_t].toarray()
    A_tb = A[blk.idx_t][:, blk.idx_b].toarray()
    A_bt = A[blk.idx_b][:, blk.idx_t].toarray()
    lu_AII = splu(A[blk.idx_I][:, blk.idx_I].tocsc())
    lu_Abb = splu(A[blk.idx_b][:, blk.idx_b].tocsc())
    S_A = (
        A_tt
        - A_tI @ lu_AII.solve(A_It)
        - A_tb @ lu_Abb.solve(A_bt)
    )
    j_A = (
        action.eta[blk.idx_t]
        - A_tI @ lu_AII.solve(action.eta[blk.idx_I])
        - A_tb @ lu_Abb.solve(action.eta[blk.idx_b])
    )
    min_eig_A = float(
        eigsh(
            0.5 * (A + A.T),
            k=1,
            which="SA",
            v0=np.ones(blk.n, dtype=float),
            return_eigenvectors=False,
        )[0]
    )
    min_eig_S = float(np.min(np.linalg.eigvalsh(0.5 * (S_A + S_A.T))))
    f_full = splu(A.tocsc()).solve(action.eta)[blk.idx_t]
    return S_A, j_A, min_eig_A, min_eig_S, f_full


def run_size(size: int) -> None:
    global _CURRENT_SIZE
    _CURRENT_SIZE = size

    blk = build_blocks(size, CUTOFF_RADIUS)

    # ---- check 1: separation lemma and partition integrity -------------------
    nnz_Ib = int(blk.H0[blk.idx_I][:, blk.idx_b].nnz)
    nnz_bI = int(blk.H0[blk.idx_b][:, blk.idx_I].nnz)
    nnz_tI = int(np.count_nonzero(blk.H_tI))
    nnz_tb = int(np.count_nonzero(blk.H_tb))
    counts_ok = (blk.idx_I.size + blk.idx_t.size + blk.idx_b.size) == blk.n
    disjoint_ok = (
        np.intersect1d(blk.idx_I, blk.idx_t).size == 0
        and np.intersect1d(blk.idx_I, blk.idx_b).size == 0
        and np.intersect1d(blk.idx_t, blk.idx_b).size == 0
    )
    t_coords = np.unravel_index(blk.idx_t, (blk.interior,) * 3)
    on_box = np.zeros(blk.idx_t.size, dtype=bool)
    for axis_coord in t_coords:
        on_box |= (axis_coord == 0) | (axis_coord == blk.interior - 1)
    t_box = int(np.count_nonzero(on_box))
    record(
        "1",
        "separation lemma: nnz(H_Ib)=nnz(H_bI)=0, blocks disjoint and summing to n, both "
        "eliminations non-vacuous (nnz(H_tI)>0, nnz(H_tb)>0). t_box = sites of t on the box's "
        "outermost interior layer, box artefact not shell",
        nnz_Ib == 0 and nnz_bI == 0 and counts_ok and disjoint_ok and nnz_tI > 0 and nnz_tb > 0,
        (
            f"nnz_Ib={nnz_Ib} nnz_bI={nnz_bI} |I|={blk.idx_I.size} |t|={blk.idx_t.size} "
            f"|b|={blk.idx_b.size} sum={blk.idx_I.size + blk.idx_t.size + blk.idx_b.size} "
            f"n={blk.n} disjoint={disjoint_ok} nnz_tI={nnz_tI} nnz_tb={nnz_tb} t_box={t_box}"
        ),
    )

    # ---- check 2: S is symmetric positive definite ---------------------------
    sym_err = float(np.max(np.abs(blk.S - blk.S.T)))
    min_eig = float(np.min(np.linalg.eigvalsh(0.5 * (blk.S + blk.S.T))))
    record(
        "2",
        "S is SPD: sym = ||S - S^T||_inf < 1e-09, lambda_min(S) > 0",
        sym_err < 1e-9 and min_eig > 0.0,
        f"sym={sym_err:.6e} lambda_min={min_eig:.9e}",
    )

    # ---- check 3: separation lemma numerically, plus solver agreement --------
    # joint carries the separation lemma. split compares two spellings of the same
    # elimination through the same factorisations, so it is not an independent route.
    interior_term = blk.H_tI @ blk.lu_II.solve(blk.H_It)
    split_resid = float(np.max(np.abs(blk.S - (blk.Lambda_R - interior_term))))
    joint_resid = float(np.max(np.abs(blk.S - blk.S_joint)))
    interior_mag = float(np.max(np.abs(interior_term)))
    lambda_gap = float(np.max(np.abs(blk.S - blk.Lambda_R)))
    record(
        "3",
        "joint = ||S - S_joint||_inf < 1e-09 IS the separation lemma's numerical content "
        "(S_joint: one Schur complement onto t over I u b). split = ||S - (Lambda_R - "
        "interior)||_inf < 1e-09 is one elimination spelled two ways, not an "
        "independent route. interior = ||H_tI H_II^-1 H_It||_inf, gap = ||S - Lambda_R||_inf",
        split_resid < 1e-9 and joint_resid < 1e-9,
        (
            f"split={split_resid:.6e} joint={joint_resid:.6e} "
            f"interior={interior_mag:.6e} gap={lambda_gap:.6e}"
        ),
    )

    # ---- check 4: predictive reconstruction ---------------------------------
    sources = build_sources(blk)
    f_true_store: dict[str, np.ndarray] = {}
    f_pred_store: dict[str, np.ndarray] = {}
    for gid, (label, rho) in zip("abcd", sources.items()):
        f_true = true_trace_from_full_solve(rho, blk)
        j_micro = independent_boundary_source(rho, blk)
        f_pred = np.linalg.solve(blk.S, j_micro)
        err = rel_inf(f_pred, f_true)
        f_true_store[label] = f_true
        f_pred_store[label] = f_pred
        lead = "reconstruction from rho alone" if gid == "a" else "same"
        record(
            f"4{gid}",
            f"{lead}, {label}: err < {RECON_TOL:.0e}",
            err < RECON_TOL,
            f"err={err:.6e} f_inf={float(np.max(np.abs(f_true))):.6e}",
        )

    # ---- checks 4e/4f: stationarity from the row's microscopic actions --------
    # Size CLASS_SIZE only; empty elsewhere, where the class builders are undefined.
    class_data: list[tuple[str, np.ndarray, np.ndarray]] = []
    for gid, (label, (action, f_true_class)) in zip(
        "ef", audited_row_action_classes(blk).items()
    ):
        S_A, j_A, min_eig_A, min_eig_S_A, f_full_A = action_boundary_equation(action, blk)
        f_pred_c = np.linalg.solve(S_A, j_A)
        err = rel_inf(f_pred_c, f_true_class)
        xchk = rel_inf(f_full_A, f_true_class)
        A_asym = action.A - action.A.T
        sym_A = (
            float(np.max(np.abs(A_asym.data)))
            if A_asym.nnz
            else 0.0
        )
        sym_S_A = float(np.max(np.abs(S_A - S_A.T)))
        support_in_I = np.setdiff1d(action.support, blk.idx_I).size == 0
        sep_nnz = int(
            action.A[blk.idx_I][:, blk.idx_b].nnz
            + action.A[blk.idx_b][:, blk.idx_I].nnz
        )
        eta_t = float(np.max(np.abs(action.eta[blk.idx_t])))
        eta_b = float(np.max(np.abs(action.eta[blk.idx_b])))
        class_data.append((label, j_A, f_true_class))
        gate_e = (
            f"microscopic-action stationarity on the {label}, size {CLASS_SIZE} only: "
            "A = H_0 - P W P^T and eta = P m are assembled before any trace; "
            f"support subset I, separation exact, sym(A), sym(S_A) < {RECON_TOL:.0e}, "
            "lambda_min(A), lambda_min(S_A)>0, "
            f"err < {RECON_TOL:.0e} vs f_true from the existing class builder, "
            f"full-action xchk < {RECON_TOL:.0e}"
        )
        gate_f = (
            f"same microscopic-action construction on the {label}, size {CLASS_SIZE} only: "
            f"support subset I, separation exact, A and S_A positive, err < {RECON_TOL:.0e}, "
            f"full-action xchk < {RECON_TOL:.0e}"
        )
        record(
            f"4{gid}",
            gate_e if gid == "e" else gate_f,
            (
                err < RECON_TOL
                and xchk < RECON_TOL
                and support_in_I
                and sep_nnz == 0
                and eta_t == 0.0
                and eta_b == 0.0
                and sym_A < RECON_TOL
                and sym_S_A < RECON_TOL
                and min_eig_A > 0.0
                and min_eig_S_A > 0.0
            ),
            (
                f"err={err:.6e} xchk={xchk:.6e} support_in_I={support_in_I} "
                f"sep_nnz={sep_nnz} eta_t={eta_t:.1e} eta_b={eta_b:.1e} "
                f"sym_A={sym_A:.1e} sym_SA={sym_S_A:.1e} "
                f"lambda_min_A={min_eig_A:.9e} lambda_min_SA={min_eig_S_A:.9e} "
                f"f_inf={float(np.max(np.abs(f_true_class))):.6e}; "
                f"{action.normalization}"
            ),
        )

    mixed_label = "random source on I, t, b"
    rho_mixed = sources[mixed_label]
    f_true_mixed = f_true_store[mixed_label]
    f_pred_mixed = f_pred_store[mixed_label]
    j_micro_mixed = independent_boundary_source(rho_mixed, blk)

    # ---- check 5: dropped-term rejectors ------------------------------------
    for gid, (drop, human) in zip("abc", (
        ("bulk", "drop the -H_tb H_bb^-1 rho_b term"),
        ("interior", "drop the -H_tI H_II^-1 rho_I term"),
        ("trace", "drop the rho_t term"),
    )):
        j_var = boundary_source_variant(rho_mixed, blk, drop)
        f_var = np.linalg.solve(blk.S, j_var)
        err = rel_inf(f_var, f_true_mixed)
        lead_5 = "rejector, " if gid == "a" else "same, "
        record(
            f"5{gid}",
            f"{lead_5}{human}: err > {REJECT_TOL:.0e}",
            err > REJECT_TOL,
            f"err={err:.6e}",
        )

    # ---- check 6: wrong-operator rejector -----------------------------------
    f_alt = np.linalg.solve(blk.Lambda_R, j_micro_mixed)
    err_alt = rel_inf(f_alt, f_true_mixed)
    record(
        "6a",
        "rejector, Lambda_R alone is not the stationarity operator: "
        f"err of Lambda_R^-1 j_micro > {REJECT_TOL:.0e}",
        err_alt > REJECT_TOL,
        f"err={err_alt:.6e}",
    )
    for gid, (label, j_class, f_true_c) in zip("bc", class_data):
        err_alt_c = rel_inf(np.linalg.solve(blk.Lambda_R, j_class), f_true_c)
        record(
            f"6{gid}",
            f"same on the {label}, size {CLASS_SIZE} only: err > {REJECT_TOL:.0e}",
            err_alt_c > REJECT_TOL,
            f"err={err_alt_c:.6e}",
        )

    # ---- check 7: tautology exhibit -----------------------------------------
    rng_taut = np.random.default_rng(SEED + 1)
    g_random = rng_taut.standard_normal(blk.idx_t.size)
    j_taut_random = harmonic_extension_trace_flux(g_random, blk)
    taut_resid = float(np.max(np.abs(blk.Lambda_R @ g_random - j_taut_random)))
    record(
        "7a",
        "TAUTOLOGY EXHIBIT (deliberate): resid = ||Lambda_R g - (H_0 u_g)|_t||_inf < 1e-09 for an "
        "ARBITRARY trace g (scale = ||Lambda_R g||_inf); it vanishes for any g, so it "
        "fixes no trace",
        taut_resid < 1e-9,
        (
            f"resid={taut_resid:.6e} "
            f"scale={float(np.max(np.abs(blk.Lambda_R @ g_random))):.6e}"
        ),
    )

    j_taut_phys = harmonic_extension_trace_flux(f_true_mixed, blk)
    taut_vs_micro = rel_inf(j_taut_phys, j_micro_mixed)
    record(
        "7b",
        "j_taut(f_true) - j_micro = H_tI H_II^-1 H_It f_true exactly, so rel = that difference / "
        f"||j_micro||_inf measures the interior Schur term's relative size; rel > {REJECT_TOL:.0e}",
        taut_vs_micro > REJECT_TOL,
        f"rel={taut_vs_micro:.6e}",
    )
    for gid, (label, j_class, f_true_c) in zip("cd", class_data):
        rel_c = rel_inf(harmonic_extension_trace_flux(f_true_c, blk), j_class)
        record(
            f"7{gid}",
            f"same action-interior correction on the {label}, size {CLASS_SIZE} only: "
            f"rel > {REJECT_TOL:.0e}",
            rel_c > REJECT_TOL,
            f"rel={rel_c:.6e}",
        )

    # ---- check 8: source-perturbation consistency ---------------------------
    rng_pert = np.random.default_rng(SEED + 2)
    delta_rho = np.zeros(blk.n, dtype=float)
    delta_rho[blk.idx_I] = 1e-3 * rng_pert.standard_normal(blk.idx_I.size)
    rho_pert = rho_mixed + delta_rho

    j_pert = independent_boundary_source(rho_pert, blk)
    f_pred_pert = np.linalg.solve(blk.S, j_pert)
    f_true_pert = true_trace_from_full_solve(rho_pert, blk)
    err_pert = rel_inf(f_pred_pert, f_true_pert)
    record(
        "8a",
        f"rho perturbed inside I: err of the new prediction < {RECON_TOL:.0e}",
        err_pert < RECON_TOL,
        f"err={err_pert:.6e}",
    )

    moved = rel_inf(f_pred_pert, f_pred_mixed)
    record(
        "8b",
        f"the perturbation moved f_pred: moved = err of f_pred' vs f_pred > {MOVE_TOL:.0e}",
        moved > MOVE_TOL,
        f"moved={moved:.6e}",
    )


def main() -> int:
    print("Independent boundary source from the microscopic source: Schur bridge theorem")
    print(f"seed={SEED}  sizes={SIZES}  cutoff_radius={CUTOFF_RADIUS}")
    print()

    for size in SIZES:
        run_size(size)

    print(
        "LEGEND  err = rel ||x - x_ref||_inf / ||x_ref||_inf; x = S^-1 j_micro(rho) and x_ref =\n"
        "f_true in 4a-4f, f_inf = ||f_true||_inf. ||.||_inf of a matrix = max |entry|, not the\n"
        "induced norm. Below tolerance: 2, 3, 4a-4f, 7a, 8a -- exact algebraic identities of the\n"
        "three-block elimination, gating the implementation, not the physics. Above a floor:\n"
        "5a-5c, 6a-6c, 7b-7d, 8b -- these with gate 1 carry the contingent content. No gate can\n"
        "by itself detect a source reconstructed from the target trace. Source independence is\n"
        "a property of which arguments the construction reads: 4a-4d use prescribed rho;\n"
        "4e-4f assemble A and eta from W/m before reading the class-builder trace. This is\n"
        "established by source inspection; full/action and builder comparisons guard consistency.\n"
        "GATES (once per size unless the gate text says otherwise)"
    )
    for gid, gate in GATES.items():
        print(f"  {gid:>3}  {gate}")
    print()

    print("RESULTS")
    for size in SIZES:
        print(f"  size={size}")
        for c in CHECKS:
            if c.size == size:
                print(f"   {c.gid:>3}  {'ok  ' if c.ok else 'FAIL'} {c.detail}")
    print()

    n_pass = sum(c.ok for c in CHECKS)
    n_fail = sum(not c.ok for c in CHECKS)
    if n_fail:
        print("FAILING CHECKS")
        for c in CHECKS:
            if not c.ok:
                print(f"  size={c.size} gid={c.gid}")
                print(f"    gate:   {GATES[c.gid]}")
                print(f"    result: {c.detail}")
        print()
    print(f"TOTAL: PASS={n_pass} FAIL={n_fail}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
