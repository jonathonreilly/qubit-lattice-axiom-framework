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
     size at which those builders are defined. Each class supplies its own field phi;
     rho = H_0 phi is then the microscopic source of that field, j_micro is built from
     that rho alone, and S^-1 j_micro is compared against phi|_t taken from the class.

The gates below are of two kinds. The rejectors are designed to fail if the implemented
object were wrong; the below-tolerance gates are exact algebraic identities of the
three-block elimination and therefore gate the implementation rather than the physics.
The reference trace f_true comes from a separate splu factorisation and solve of the
same H_0 -- a second elimination of the same discretisation, not a second
discretisation. No gate here can detect a j reconstructed from the target trace, since
j_micro = S f_true identically; trace-independence is a property of which arguments the
construction reads -- independent_boundary_source takes rho and the operator blocks,
never a trace -- and is established by inspection of the source, not by a number.
"""

from __future__ import annotations

import contextlib
import io
from dataclasses import dataclass

from _frontier_loader import load_frontier

import numpy as np
import scipy.sparse as sparse
from scipy.sparse.linalg import spsolve, splu


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
dtn = load_frontier("dtn_shell", "frontier_discrete_dtn_shell_kernel.py")
# The two source classes named by the row this runner supports. Their modules may print
# at import; only the import is silenced, and exceptions still propagate.
with contextlib.redirect_stdout(io.StringIO()):
    same_source = load_frontier("same_source_metric", "frontier_same_source_metric_ansatz_scan.py")
    coarse = load_frontier("coarse_grained", "frontier_coarse_grained_exterior_law.py")


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


def build_blocks(size: int, cutoff_radius: float) -> Blocks:
    trace_idx, bulk_idx = dtn.exterior_sets(size, cutoff_radius)
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


def audited_row_source_classes(blk: Blocks) -> dict[str, tuple[np.ndarray, np.ndarray]]:
    """The two source classes named by the audited row, at their native size 15.

    Returns label -> (rho, f_true_class). The field `phi` is built by the class's own
    script; `rho := H_0 phi` is therefore the microscopic source of that field, and
    `f_true_class := phi|_t` is ground truth taken from the class, not from any solve
    performed here. Empty at sizes other than CLASS_SIZE, where the builders are not
    defined.
    """
    if blk.size != CLASS_SIZE:
        return {}

    with contextlib.redirect_stdout(io.StringIO()):
        grids = {
            "exact local O_h class": same_source.build_best_phi_grid(),
            "exact finite-rank class": coarse.build_finite_rank_phi_grid(),
        }

    classes: dict[str, tuple[np.ndarray, np.ndarray]] = {}
    for label, phi_grid in grids.items():
        # Exact inverse of how both builders write the grid; the xchk gate verifies it.
        phi_flat = np.ascontiguousarray(phi_grid[1:-1, 1:-1, 1:-1]).reshape(-1)
        classes[label] = (blk.H0 @ phi_flat, phi_flat[blk.idx_t])
    return classes


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

    # ---- checks 4e/4f: stationarity rerun on the row's own source classes ----
    # Size CLASS_SIZE only; empty elsewhere, where the class builders are undefined.
    class_data: list[tuple[str, np.ndarray, np.ndarray]] = []
    for gid, (label, (rho_c, f_true_c)) in zip("ef", audited_row_source_classes(blk).items()):
        j_class = independent_boundary_source(rho_c, blk)
        f_pred_c = np.linalg.solve(blk.S, j_class)
        err = rel_inf(f_pred_c, f_true_c)
        xchk = rel_inf(true_trace_from_full_solve(rho_c, blk), f_true_c)
        rho_t = float(np.max(np.abs(rho_c[blk.idx_t])))
        rho_b = float(np.max(np.abs(rho_c[blk.idx_b])))
        class_data.append((label, j_class, f_true_c))
        gate_e = (
            f"stationarity rerun on the {label}, size {CLASS_SIZE} only: err < {RECON_TOL:.0e} "
            f"vs f_true = phi|_t from the class, self-guard xchk < {RECON_TOL:.0e} "
            "(full solve of rho = H_0 phi)"
        )
        gate_f = (
            f"same on the {label}, size {CLASS_SIZE} only: "
            f"err < {RECON_TOL:.0e}, xchk < {RECON_TOL:.0e}"
        )
        record(
            f"4{gid}",
            gate_e if gid == "e" else gate_f,
            err < RECON_TOL and xchk < RECON_TOL,
            (
                f"err={err:.6e} xchk={xchk:.6e} rho_t={rho_t:.6e} rho_b={rho_b:.6e} "
                f"f_inf={float(np.max(np.abs(f_true_c))):.6e}"
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
            f"same on the {label}, size {CLASS_SIZE} only: rel > {REJECT_TOL:.0e}",
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
        "detect a j reconstructed from the target trace, since j_micro = S f_true identically;\n"
        "trace-independence is a property of which arguments the construction reads\n"
        "(independent_boundary_source takes rho and the operator blocks, never a trace),\n"
        "established by inspection of the source, not by a number.\n"
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
