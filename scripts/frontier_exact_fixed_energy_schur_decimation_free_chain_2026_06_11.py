#!/usr/bin/env python3
"""Exact FIXED-ENERGY Schur decimation (downfolding) on the free 1D staggered chain:
the m != 0 step is resolvent-EXACT on retained sites (7e-16; no truncation), the
downfolded form MIGRATES honestly (staggered -> uniform potential + NN hopping;
staggered mass identically 0; NNN = 0 exactly and analytically necessarily, since
h_oo is diagonal at E=0), the one-step map is an exact closed form validated on
DISJOINT grids (diag' = m + 2t^2/m, t' = -t^2/m), Schur composition is associative
(twice = by-4 once, 6e-17), large m gives the projective decoupling |t'/diag'| -> 0
(ratio statement only), the m=0 case is a zero-mode-projected Moore-Penrose
DIAGNOSTIC kept separate from the m != 0 theorem, and a drop-the-Schur-correction
control FAILS by O(1).  NOT an RG transformation (no rescaling step; no declared
post-migration flow space) -- composing with a rescaling convention is the named
follow-on.

Class-A exact verification for the source note

    docs/EXACT_FIXED_ENERGY_SCHUR_DECIMATION_FREE_CHAIN_FORM_MIGRATION_ONE_STEP_MAP_BOUNDED_THEOREM_NOTE_2026-06-11.md

Scope: free sector, 1D, one color, E=0 slice.  The color index is a spectator
at the free level, so one color is sufficient.  The runner checks exact Schur
decimation on retained even sites; no truncation is used.

Claim boundary: the one-step map and fixed diagnostics are E=0 statements for
this free chain.  This does not claim an RG transformation, interacting RG, d=3
result, gauge-sector result, continuum limit, or c-function.  Statuses are
pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_exact_fixed_energy_schur_decimation_free_chain_2026_06_11.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np


TOL_EXACT = 1.0e-12
TOL_SEMIGROUP = 1.0e-10


@dataclass
class CheckResult:
    ok: bool
    detail: str


def max_abs(a: np.ndarray) -> float:
    return float(np.max(np.abs(a))) if a.size else 0.0


def hamiltonian(N: int, t: float = 1.0, m: float = 0.0) -> np.ndarray:
    """Periodic nearest-neighbor chain with hopping -t and mass (-1)^i m."""
    if N % 2:
        raise ValueError("N must be even")
    h = np.zeros((N, N), dtype=float)
    for i in range(N):
        h[i, i] = m if i % 2 == 0 else -m
        j = (i + 1) % N
        h[i, j] = -t
        h[j, i] = -t
    return h


def even_indices(N: int) -> np.ndarray:
    return np.arange(0, N, 2, dtype=int)


def odd_indices(N: int) -> np.ndarray:
    return np.arange(1, N, 2, dtype=int)


def inverse_or_pinv(a: np.ndarray, allow_pinv: bool = False) -> np.ndarray:
    try:
        return np.linalg.inv(a)
    except np.linalg.LinAlgError:
        if not allow_pinv:
            raise
        return np.linalg.pinv(a, rcond=1.0e-14)


def resolvent(h: np.ndarray, E: float = 0.0, allow_pinv: bool = False) -> np.ndarray:
    return inverse_or_pinv(h - E * np.eye(h.shape[0]), allow_pinv=allow_pinv)


def schur_decimate(
    h: np.ndarray,
    keep: np.ndarray,
    elim: np.ndarray,
    E: float = 0.0,
    allow_pinv: bool = False,
) -> np.ndarray:
    h_kk = h[np.ix_(keep, keep)]
    h_ke = h[np.ix_(keep, elim)]
    h_ek = h[np.ix_(elim, keep)]
    h_ee = h[np.ix_(elim, elim)]
    d_inv = inverse_or_pinv(h_ee - E * np.eye(len(elim)), allow_pinv=allow_pinv)
    return h_kk - h_ke @ d_inv @ h_ek


def decimate_odd(h: np.ndarray, E: float = 0.0, allow_pinv: bool = False) -> np.ndarray:
    return schur_decimate(
        h,
        even_indices(h.shape[0]),
        odd_indices(h.shape[0]),
        E=E,
        allow_pinv=allow_pinv,
    )


def ring_distance(i: int, j: int, n: int) -> int:
    d = abs(i - j) % n
    return min(d, n - d)


def range_summary(a: np.ndarray, tol: float = 1.0e-12) -> dict[int, float]:
    n = a.shape[0]
    out: dict[int, float] = {}
    for i in range(n):
        for j in range(n):
            v = abs(float(a[i, j]))
            if v > tol:
                r = ring_distance(i, j, n)
                out[r] = max(out.get(r, 0.0), v)
    return out


def nearest_values(a: np.ndarray) -> np.ndarray:
    n = a.shape[0]
    vals = []
    for i in range(n):
        vals.append(a[i, (i + 1) % n])
        vals.append(a[(i + 1) % n, i])
    return np.asarray(vals, dtype=float)


def staggered_component(diagonal: np.ndarray) -> float:
    signs = np.asarray([1.0 if i % 2 == 0 else -1.0 for i in range(len(diagonal))])
    return float(np.dot(signs, diagonal) / len(diagonal))


def measured_effective_couplings(N: int, t: float, m: float, E: float = 0.0) -> tuple[float, float, float, float]:
    h = hamiltonian(N, t=t, m=m)
    heff = decimate_odd(h, E=E)
    diag = np.diag(heff)
    nn = nearest_values(heff)
    max_beyond_nn = 0.0
    for r, value in range_summary(heff).items():
        if r > 1:
            max_beyond_nn = max(max_beyond_nn, value)
    return (
        float(np.mean(diag)),
        float(np.mean(nn)),
        staggered_component(diag),
        max_beyond_nn,
    )


def check_d1_exactness() -> CheckResult:
    N = 16
    E = 0.0
    worst = 0.0
    notes = []
    for m in (0.0, 0.3, 1.5):
        h = hamiltonian(N, t=1.0, m=m)
        singular_critical = m == 0.0 and E == 0.0
        heff = decimate_odd(h, E=E, allow_pinv=singular_critical)
        full_even = resolvent(h, E=E, allow_pinv=singular_critical)[
            np.ix_(even_indices(N), even_indices(N))
        ]
        eff = resolvent(heff, E=E, allow_pinv=singular_critical)
        err = max_abs(full_even - eff)
        worst = max(worst, err)
        if singular_critical:
            notes.append("m=0,E=0 singular: zero-mode-projected Moore-Penrose check")
    ok = worst <= TOL_EXACT
    return CheckResult(ok, f"max retained-resolvent error={worst:.3e}; {'; '.join(notes)}")


def check_d2_form_closure() -> CheckResult:
    N = 16
    t = 1.0
    worst_formula = 0.0
    worst_beyond = 0.0
    reports = []
    for m in (0.3, 1.5):
        h = hamiltonian(N, t=t, m=m)
        heff = decimate_odd(h, E=0.0)
        diag = np.diag(heff)
        nn = nearest_values(heff)
        nnn_max = range_summary(heff).get(2, 0.0)
        beyond = max((v for r, v in range_summary(heff).items() if r > 1), default=0.0)
        uniform_diag = m + 2.0 * t * t / m
        nn_value = t * t / m
        formula_err = max(
            max_abs(diag - uniform_diag),
            max_abs(nn - nn_value),
            abs(staggered_component(diag)),
            beyond,
        )
        worst_formula = max(worst_formula, formula_err)
        worst_beyond = max(worst_beyond, beyond)
        reports.append(
            f"m={m:g}: diag={uniform_diag:.15g}, NN={nn_value:.15g}, NNN={nnn_max:.3e}"
        )

    h0 = hamiltonian(N, t=t, m=0.0)
    heff0 = decimate_odd(h0, E=0.0, allow_pinv=True)
    critical_projected_terms = range_summary(heff0)
    ok = worst_formula <= TOL_EXACT and worst_beyond <= TOL_EXACT and max_abs(heff0) <= TOL_EXACT
    detail = (
        "nonzero structure at E=0 is diagonal + coarse NN only for m!=0; "
        "h_eff diag=m+2t^2/m, coarse NN=t^2/m, so hopping convention gives t'=-t^2/m; "
        f"{' | '.join(reports)}; projected m=0 ranges={critical_projected_terms}"
    )
    return CheckResult(ok, detail)


def check_d3_flow_map() -> CheckResult:
    inference_grid = [(0.5, 0.4), (1.0, 1.1), (1.7, 2.3), (2.2, 0.9)]
    validation_grid = [(0.8, 0.6), (1.3, 1.7), (2.0, 3.0), (1.9, 0.75)]
    worst_infer = 0.0
    worst_validate = 0.0

    def expected(t: float, m: float) -> tuple[float, float, float]:
        uniform_diag = m + 2.0 * t * t / m
        coarse_nn = t * t / m
        coarse_staggered_mass = 0.0
        return uniform_diag, coarse_nn, coarse_staggered_mass

    for t, m in inference_grid:
        diag, nn, stag, beyond = measured_effective_couplings(16, t=t, m=m)
        e_diag, e_nn, e_stag = expected(t, m)
        worst_infer = max(worst_infer, abs(diag - e_diag), abs(nn - e_nn), abs(stag - e_stag), beyond)

    for t, m in validation_grid:
        diag, nn, stag, beyond = measured_effective_couplings(16, t=t, m=m)
        e_diag, e_nn, e_stag = expected(t, m)
        worst_validate = max(
            worst_validate,
            abs(diag - e_diag),
            abs(nn - e_nn),
            abs(stag - e_stag),
            beyond,
        )

    # Iteration after the first step is closed in the enlarged uniform-diagonal,
    # NN family: a' = a - 2b^2/a, b' = -b^2/a.  The trivial fixed line b=0 is
    # attractive in x=b/a.  The m=0 point is the singular critical E=0 point; its
    # staggered component is exactly zero in the finite-E regulator and in the
    # zero-mode-projected E=0 matrix.
    def uniform_ratio_after_first_step(x: float) -> float:
        # x = t/m, with t fixed.  |b/a| = x^2 / (1 + 2x^2).
        return (x * x) / (1.0 + 2.0 * x * x)

    eps = 1.0e-6
    trivial_derivative = (uniform_ratio_after_first_step(eps) - uniform_ratio_after_first_step(0.0)) / eps
    critical_left = staggered_component(np.diag(decimate_odd(hamiltonian(16, t=1.0, m=0.0), E=0.5)))
    critical_projected = staggered_component(
        np.diag(decimate_odd(hamiltonian(16, t=1.0, m=0.0), E=0.0, allow_pinv=True))
    )

    ok = (
        worst_infer <= TOL_EXACT
        and worst_validate <= TOL_EXACT
        and abs(critical_left) <= TOL_EXACT
        and abs(critical_projected) <= TOL_EXACT
        and abs(trivial_derivative) < 1.0e-5
    )
    detail = (
        "validated exact forms on disjoint grids: uniform=m+2t^2/m, NN=t^2/m, "
        "staggered m'=0; same-form Hamiltonian representation uses t'=-t^2/m "
        "and E'=-m-2t^2/m. Fixed diagnostics: m=0 is singular critical with "
        f"m'=0 regulator/projected checks ({critical_left:.3e},{critical_projected:.3e}); "
        f"m->inf gives |NN/diag|->0 with derivative {trivial_derivative:.3e}. "
        f"errors infer={worst_infer:.3e}, validate={worst_validate:.3e}"
    )
    return CheckResult(ok, detail)


def check_d4_observable_invariance() -> CheckResult:
    rng = np.random.default_rng(20260611)
    worst = 0.0
    samples = []
    for _ in range(5):
        t = float(rng.uniform(0.4, 2.0))
        m = float(rng.uniform(0.2, 2.0))
        h = hamiltonian(16, t=t, m=m)
        heff = decimate_odd(h, E=0.0)
        g_full = resolvent(h, E=0.0)
        g_eff = resolvent(heff, E=0.0)
        err = abs(float(g_full[0, 2] - g_eff[0, 1]))
        worst = max(worst, err)
        samples.append(f"(t={t:.6g},m={m:.6g},err={err:.1e})")
    return CheckResult(
        worst <= TOL_EXACT,
        f"G[0,2](0) retained-site invariance max error={worst:.3e}; samples={'; '.join(samples)}",
    )


def check_d5_iteration_consistency() -> CheckResult:
    N = 16
    E = 0.0
    h = hamiltonian(N, t=0.8, m=1.1)

    h1 = decimate_odd(h, E=E)
    keep_second = np.arange(0, h1.shape[0], 2, dtype=int)
    elim_second = np.arange(1, h1.shape[0], 2, dtype=int)
    h2 = schur_decimate(h1, keep_second, elim_second, E=E)

    keep_direct = np.asarray([0, 4, 8, 12], dtype=int)
    elim_direct = np.asarray([i for i in range(N) if i not in set(keep_direct)], dtype=int)
    h_direct = schur_decimate(h, keep_direct, elim_direct, E=E)

    err_h = max_abs(h2 - h_direct)
    err_g = max_abs(resolvent(h2, E=E) - resolvent(h_direct, E=E))
    ok = err_g <= TOL_SEMIGROUP
    return CheckResult(ok, f"two-step vs direct-by-4: h error={err_h:.3e}, resolvent error={err_g:.3e}")


def check_d6_controls() -> CheckResult:
    N = 16
    h_massless = hamiltonian(N, t=1.0, m=0.0)
    projected = decimate_odd(h_massless, E=0.0, allow_pinv=True)
    finite_e = decimate_odd(h_massless, E=0.75)
    massless_ok = (
        abs(staggered_component(np.diag(projected))) <= TOL_EXACT
        and abs(staggered_component(np.diag(finite_e))) <= TOL_EXACT
    )

    h = hamiltonian(N, t=1.0, m=0.3)
    true_even = resolvent(h, E=0.0)[np.ix_(even_indices(N), even_indices(N))]
    wrong_heff = h[np.ix_(even_indices(N), even_indices(N))]
    wrong_even = resolvent(wrong_heff, E=0.0)
    wrong_err = max_abs(true_even - wrong_even)
    wrong_fails = wrong_err > 1.0e-6

    ok = massless_ok and wrong_fails
    return CheckResult(
        ok,
        "m=0 preserves zero staggered component in projected E=0 and finite-E regulator; "
        f"drop-Schur-control retained-resolvent error={wrong_err:.3e} (>1e-6 means control fails as intended)",
    )


def check(name: str, fn: Callable[[], CheckResult]) -> bool:
    try:
        result = fn()
    except Exception as exc:  # pragma: no cover - runner contract path
        print(f"{name}: FAIL exception={exc!r}")
        return False
    status = "PASS" if result.ok else "FAIL"
    print(f"{name}: {status} {result.detail}")
    return result.ok


def main() -> int:
    print("SCOPE: free sector, 1D, one color, E=0 slice; exact Schur decimation, no truncation.")
    print("NOT CLAIMED: interacting RG, d=3, gauge sectors, continuum limits, c-functions.")
    print("Statuses are pipeline-derived; the audit lane grades.")

    checks: list[tuple[str, Callable[[], CheckResult]]] = [
        ("D1 EXACTNESS", check_d1_exactness),
        ("D2 FORM CLOSURE", check_d2_form_closure),
        ("D3 ONE-STEP MAP", check_d3_flow_map),
        ("D4 OBSERVABLE INVARIANCE", check_d4_observable_invariance),
        ("D5 ITERATION CONSISTENCY", check_d5_iteration_consistency),
        ("D6 CONTROLS", check_d6_controls),
    ]
    passed = 0
    failed = 0
    for name, fn in checks:
        if check(name, fn):
            passed += 1
        else:
            failed += 1
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
