#!/usr/bin/env python3
"""Route B energy-sector obstruction to an abelian local Gauss constraint.

Can energy conservation be promoted to an ABELIAN local constraint the way
charge is?  In the charge sector, local charge densities commute at all
separations; that abelian Gauss algebra is the algebraic source of the
long-range field.  Energy densities do not commute.  This runner computes that
local obstruction exactly in the same normal-ordered fermionic algebra used by
scripts/noether_source_current_classification_2026_07_08.py, then identifies
the sector pulled in by the candidate constraint algebra: the energy-current
sector, the lattice shadow of the hypersurface-deformation algebra.

Companion note:
ENERGY_GAUSS_CONSTRAINT_OBSTRUCTION_ROUTE_B_NOTE_2026-07-08.md.

No gravitational dynamics are derived here; no audit status is set.

Design concerns are explicit rather than hidden:
- The auxiliary eta bookkeeping is algebraically inert because
  [eta_k, matter] = [eta_k, eta_l] = 0, so [G_n, G_m] = [h_n, h_m].
- The current construction uses the standard crossing-current partial sum
  j_n = -i sum_{a <= n-1, b >= n} [h_a, h_b], truncated only by locality.
- The projection check is a finite 8-site, degree <= 6 coefficient-basis
  check over the imported monomial/operator conventions; it is not used as an
  exact identity proof.
"""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path
import sys
import time

import numpy as np
import scipy.linalg as sla
import scipy.sparse as sp


sys.dont_write_bytecode = True

RNG_SEED = 20260708
CELL_SITES = 2
DENSE_SITES = 8
CHECK_TOL = 1.0e-12
CLEAN_TOL = 1.0e-14
ANGLE_GATE = 0.3
NONCENTRAL_GATE = 0.1
PROJECTION_WINDOW = 8
PROJECTION_DEGREE = 6


def import_classification_runner():
    path = Path(__file__).with_name("noether_source_current_classification_2026_07_08.py")
    spec = importlib.util.spec_from_file_location("noether_source_current_classification_2026_07_08", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load noether source/current classification runner")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


eng = import_classification_runner()


def add_scaled(accum, op, scale: complex) -> None:
    eng.op_add_scaled(accum, op, scale)


def translate_op(op, delta_sites: int):
    out = {}
    for key, coeff in op.items():
        eng.op_add(out, eng.translate_key(key, delta_sites), coeff)
    return out


def h_cell(c, n: int, *, part: str = "total"):
    return translate_op(eng.build_h_density(c, part=part), CELL_SITES * n)


def q_site(n: int):
    out = {}
    eng.add_number(out, eng.mode(n, "a"), 1.0)
    eng.add_number(out, eng.mode(n, "b"), 1.0)
    return out


def identity_op():
    return {eng.identity_key(): 1.0 + 0.0j}


def density_only(op):
    return {key: coeff for key, coeff in op.items() if key[0] == key[1]}


def commutator(left, right):
    out = {}
    for l_key, l_coeff in left.items():
        if abs(l_coeff) <= CLEAN_TOL:
            continue
        for r_key, r_coeff in right.items():
            if abs(r_coeff) <= CLEAN_TOL:
                continue
            scale = l_coeff * r_coeff
            for key, coeff in eng.commutator_key_items(l_key, r_key):
                eng.op_add(out, key, scale * coeff)
    return out


def op_difference(left, right):
    out = {}
    add_scaled(out, left, 1.0)
    add_scaled(out, right, -1.0)
    return out


def op_linear(terms):
    out = {}
    for scale, op in terms:
        add_scaled(out, op, scale)
    return out


def coeff_l2(op) -> float:
    return math.sqrt(sum(float(abs(coeff) ** 2) for coeff in op.values()))


def op_sites(op) -> list[int]:
    sites: set[int] = set()
    for key in op:
        if key == eng.identity_key():
            continue
        sites.update(eng.key_sites(key))
    return sorted(sites)


def op_width(op) -> int:
    sites = op_sites(op)
    return 0 if not sites else max(sites) - min(sites) + 1


def shift_min_site_to_zero(op):
    sites = op_sites(op)
    if not sites:
        return op
    return translate_op(op, -min(sites))


def sparse_max_abs(matrix: sp.spmatrix) -> float:
    coo = matrix.tocoo()
    return float(np.max(np.abs(coo.data))) if coo.nnz else 0.0


def sparse_frobenius(matrix: sp.spmatrix) -> float:
    csr = matrix.tocsr()
    return float(np.linalg.norm(csr.data)) if csr.nnz else 0.0


def hs_norm_8(op, cache) -> float:
    return sparse_frobenius(eng.operator_sparse(op, DENSE_SITES, cache))


def dense_vs_symbolic_commutator_error(left, right, symbolic, cache) -> float:
    left_mat = eng.operator_sparse(left, DENSE_SITES, cache)
    right_mat = eng.operator_sparse(right, DENSE_SITES, cache)
    sym_mat = eng.operator_sparse(symbolic, DENSE_SITES, cache)
    diff = left_mat @ right_mat - right_mat @ left_mat - sym_mat
    diff.eliminate_zeros()
    return sparse_max_abs(diff)


def noncentral_eigen_spread(op) -> float:
    local = shift_min_site_to_zero(op)
    sites = op_sites(local)
    if not sites:
        return 0.0
    n_sites = max(sites) + 1
    mat = eng.operator_sparse(local, n_sites, {})
    hermitian = (-1.0j * mat).toarray()
    hermitian = (hermitian + hermitian.conjugate().T) * 0.5
    evals = sla.eigvalsh(hermitian, check_finite=False).real
    centered = evals - float(np.mean(evals))
    rms = math.sqrt(float(np.mean(evals * evals)))
    return math.sqrt(float(np.mean(centered * centered))) / max(rms, np.finfo(float).tiny)


def crossing_current(c, n: int):
    out = {}
    for a in range(n - 3, n):
        for b in range(n, n + 4):
            add_scaled(out, commutator(h_cell(c, a), h_cell(c, b)), -1.0j)
    return out


def energy_divergence(c, n: int):
    out = {}
    hn = h_cell(c, n)
    for m in range(n - 3, n + 4):
        add_scaled(out, commutator(h_cell(c, m), hn), -1.0j)
    return out


def finite_window_ok(op, *, window: int = PROJECTION_WINDOW, degree: int = PROJECTION_DEGREE) -> bool:
    for key in op:
        if key == eng.identity_key():
            continue
        sites = eng.key_sites(key)
        if not sites:
            continue
        if min(sites) < 0 or max(sites) >= window:
            return False
        if eng.key_degree(key) > degree:
            return False
    return True


def coefficient_angle(vector_op, span_ops) -> tuple[float, bool]:
    all_ops = [vector_op, *span_ops]
    window_ok = all(finite_window_ok(op) for op in all_ops)
    keys = sorted({key for op in all_ops for key, coeff in op.items() if abs(coeff) > CLEAN_TOL})
    if not keys:
        return math.pi / 2.0, window_ok
    index = {key: idx for idx, key in enumerate(keys)}
    vec = np.zeros(len(keys), dtype=np.complex128)
    for key, coeff in vector_op.items():
        if abs(coeff) > CLEAN_TOL:
            vec[index[key]] = coeff
    cols = []
    for op in span_ops:
        col = np.zeros(len(keys), dtype=np.complex128)
        for key, coeff in op.items():
            if abs(coeff) > CLEAN_TOL:
                col[index[key]] = coeff
        if np.linalg.norm(col) > CLEAN_TOL:
            cols.append(col)
    norm = float(np.linalg.norm(vec))
    if norm <= CLEAN_TOL or not cols:
        return math.pi / 2.0, window_ok
    mat = np.column_stack(cols)
    q, singular, _ = sla.svd(mat, full_matrices=False, check_finite=False)
    rank = int(np.count_nonzero(singular > 1.0e-12))
    if rank == 0:
        return math.pi / 2.0, window_ok
    q = q[:, :rank]
    residual = vec - q @ (q.conjugate().T @ vec)
    sin_theta = float(np.linalg.norm(residual) / norm)
    return float(math.asin(np.clip(sin_theta, 0.0, 1.0))), window_ok


def local_projection_report(c, j_op):
    h_base = eng.build_h_density(c)
    span_hq = [identity_op()]
    span_hq.extend(q_site(site) for site in range(PROJECTION_WINDOW))
    for cell in range(3):
        span_hq.append(translate_op(h_base, CELL_SITES * cell))

    angle_hq, basis_ok_hq = coefficient_angle(j_op, span_hq)

    span_with_currents = list(span_hq)
    for species in ("a", "b"):
        current_base = eng.build_current_operator(species, c)
        for cell in range(3):
            span_with_currents.append(translate_op(current_base, CELL_SITES * cell))
    angle_current, basis_ok_current = coefficient_angle(j_op, span_with_currents)
    return angle_hq, angle_current, angle_hq - angle_current, basis_ok_hq and basis_ok_current


def check_charge(c):
    q_ops = [q_site(n) for n in range(6)]
    charge_abelian = True
    for n in range(6):
        for m in range(6):
            if commutator(q_ops[n], q_ops[m]):
                charge_abelian = False

    qh_norms = []
    for site in range(6):
        for cell in range(3):
            qh_norms.append(coeff_l2(commutator(q_site(site), h_cell(c, cell))))
    nonzero = [norm for norm in qh_norms if norm > CLEAN_TOL]
    return charge_abelian, len(nonzero), (min(nonzero) if nonzero else 0.0), max(qh_norms)


def check_energy(c, cache):
    c01 = commutator(h_cell(c, 0), h_cell(c, 1))
    locality_ok = True
    self_ok = True
    for n in range(6):
        for m in range(6):
            if abs(n - m) > 3:
                continue
            cnm = commutator(h_cell(c, n), h_cell(c, m))
            if n == m and cnm:
                self_ok = False
            if abs(n - m) >= 2 and cnm:
                locality_ok = False
    norm = hs_norm_8(c01, cache)
    dense_error = dense_vs_symbolic_commutator_error(h_cell(c, 0), h_cell(c, 1), c01, cache)
    spread = noncentral_eigen_spread(c01)
    return c01, norm, locality_ok, self_ok, dense_error, spread


def check_current(c, cache):
    j1 = crossing_current(c, 1)
    j2 = crossing_current(c, 2)
    d1 = energy_divergence(c, 1)
    continuity_error = op_linear([(1.0, d1), (-1.0, j1), (1.0, j2)])
    j_norm = hs_norm_8(j1, cache)
    angle_hq, angle_current, angle_drop, basis_ok = local_projection_report(c, j1)
    return j1, j_norm, not continuity_error, op_width(j1), angle_hq, angle_current, angle_drop, basis_ok


def check_controls(c, cache):
    free_c = eng.free_like(c)
    free_c01 = commutator(h_cell(free_c, 0), h_cell(free_c, 1))
    free_norm = hs_norm_8(free_c01, cache)

    single_a = commutator(h_cell(c, 0, part="a"), h_cell(c, 1, part="a"))
    single_b = commutator(h_cell(c, 0, part="b"), h_cell(c, 1, part="b"))
    single_a_norm = hs_norm_8(single_a, cache)
    single_b_norm = hs_norm_8(single_b, cache)

    diag_base = density_only(eng.build_h_density(c))
    diag_abelian = True
    for n in range(6):
        for m in range(6):
            if abs(n - m) <= 3 and commutator(translate_op(diag_base, CELL_SITES * n), translate_op(diag_base, CELL_SITES * m)):
                diag_abelian = False
    return free_norm, single_a_norm, single_b_norm, diag_abelian


def main() -> int:
    started = time.time()
    verdict = "MACHINERY-FAIL"
    notes: list[str] = []
    cache = {}

    try:
        rng = np.random.default_rng(RNG_SEED)
        c = eng.random_couplings(rng)

        charge_ok, qh_nonzero, qh_min, qh_max = check_charge(c)
        c01, c01_norm, locality_ok, self_ok, dense_error, spread = check_energy(c, cache)
        j1, j_norm, continuity_ok, j_width, angle_hq, angle_current, angle_drop, projection_ok = check_current(c, cache)
        free_norm, single_a_norm, single_b_norm, diag_abelian = check_controls(c, cache)

        machinery_ok = (
            charge_ok
            and locality_ok
            and self_ok
            and dense_error <= CHECK_TOL
            and continuity_ok
            and projection_ok
            and diag_abelian
        )
        unexpected = (
            c01_norm <= CHECK_TOL
            or spread <= NONCENTRAL_GATE
            or angle_hq <= ANGLE_GATE
            or free_norm <= CHECK_TOL
            or j_norm <= CHECK_TOL
        )

        if machinery_ok and not unexpected:
            verdict = "ABELIAN-OBSTRUCTED"
        elif machinery_ok and unexpected:
            verdict = "UNEXPECTED-CLOSURE"

        curr_dominated = angle_current < ANGLE_GATE
        print(f"CHARGE q_abelian={'ok' if charge_ok else 'FAIL'} qh_l2_nonzero={qh_nonzero} qh_l2_minmax=({qh_min:.3e},{qh_max:.3e})")
        print(
            "ENERGY-OBSTRUCTION "
            f"C01_hs8={c01_norm:.6e} locality_d>=2={'ok' if locality_ok else 'FAIL'} self={'ok' if self_ok else 'FAIL'} "
            f"dense_err={dense_error:.1e} G01_hs8={c01_norm:.6e} noncentral_spread={spread:.3f}"
        )
        print(
            "CURRENT-CLOSURE "
            f"j_hs8={j_norm:.6e} div_exact={'ok' if continuity_ok else 'FAIL'} width={j_width} "
            f"angle_hq={angle_hq:.3f} angle_hqJ={angle_current:.3f} drop={angle_drop:.3f} "
            f"curr_dominated={'yes' if curr_dominated else 'no'}"
        )
        print(
            "CONTROLS "
            f"free_C01_hs8={free_norm:.6e} single_C01_hs8=({single_a_norm:.3e},{single_b_norm:.3e}) "
            f"diag_abelian={'ok' if diag_abelian else 'FAIL'} obstruction-is-kinetic"
        )
        print("SPEC-NOTE eta-auxiliary-only; current=crossing-partial-sum; projection=8site-degree<=6-coeff-basis")
        print(f"TOTAL {verdict} elapsed={time.time() - started:.2f}s seed={RNG_SEED}")
        return 0 if verdict == "ABELIAN-OBSTRUCTED" else 1
    except Exception as exc:
        notes.append(f"{type(exc).__name__}:{exc}")
        print("CHARGE blocked")
        print("ENERGY-OBSTRUCTION blocked")
        print("CURRENT-CLOSURE blocked")
        print("CONTROLS blocked")
        print("SPEC-NOTE " + "|".join(notes))
        print(f"TOTAL MACHINERY-FAIL elapsed={time.time() - started:.2f}s seed={RNG_SEED}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
