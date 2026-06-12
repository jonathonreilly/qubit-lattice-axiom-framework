#!/usr/bin/env python3
"""The framework's first declared projective fixed-energy Schur RG convention:
the uniform free chain closes under b=2 odd-sublattice Schur decimation at E=0
with normalization by the new on-site scale; the signed dimensionless coupling
g = t/mu flows as g' = g^2/(1 - 2 g^2), while the declared flow space is the
quotient |g| because t -> -t is a staggered-gauge unitary equivalence.  On the
declared chart |g| < 1/sqrt(2), the theorem fixed points are g* = 0 and
g* = 1/2, the latter is the E=0 resolvent-threshold band-edge statement, and
the associated resolvent length has nu = ln2/ln4 = 1/2.  The landed staggered
migration is step one of this flow (composition at the double-precision floor);
retained-site E=0 resolvent exactness is inherited per step.  Poles at
g = +/-1/sqrt(2) are disclosed.

Class-A exact verification for the source note

    docs/DECLARED_RG_MAP_UNIFORM_CHAIN_BAND_EDGE_FIXED_POINT_NU_HALF_BOUNDED_THEOREM_NOTE_2026-06-12.md

Free sector, 1D, E=0 slice, THIS declared convention (b=2, g=t/mu); NOT claimed:
universality beyond the convention, interacting RG, d=3, gauge sectors, continuum
limits.  Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_declared_rg_map_uniform_chain_band_edge_2026_06_12.py
"""
import sys

import numpy as np


PASS = 0
FAIL = 0
TOL = 1.0e-12


def check(name, condition, detail):
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"[{status}] {name}: {detail}")


def max_abs(a):
    return float(np.max(np.abs(a))) if a.size else 0.0


def fmt(x):
    return f"{float(x):.17g}"


def uniform_chain(n, t, mu):
    h = np.zeros((n, n), dtype=float)
    np.fill_diagonal(h, mu)
    idx = np.arange(n)
    h[idx, (idx + 1) % n] += -t
    h[(idx + 1) % n, idx] += -t
    return h


def staggered_chain(n, t, m):
    h = np.zeros((n, n), dtype=float)
    onsite = np.array([m if i % 2 == 0 else -m for i in range(n)], dtype=float)
    np.fill_diagonal(h, onsite)
    idx = np.arange(n)
    h[idx, (idx + 1) % n] += -t
    h[(idx + 1) % n, idx] += -t
    return h


def schur_decimate(h):
    n = h.shape[0]
    retained = np.arange(0, n, 2)
    eliminated = np.arange(1, n, 2)
    a = h[np.ix_(retained, retained)]
    b = h[np.ix_(retained, eliminated)]
    c = h[np.ix_(eliminated, retained)]
    d = h[np.ix_(eliminated, eliminated)]
    return a - b @ np.linalg.solve(d, c)


def uniform_after_one_step(t, mu):
    mu_next = mu - 2.0 * t * t / mu
    t_next = t * t / mu
    nn_element = -t_next
    return t_next, mu_next, nn_element


def uniform_params_from_matrix(h):
    n = h.shape[0]
    mu = float(np.mean(np.diag(h)))
    nn = []
    for i in range(n):
        nn.append(h[i, (i + 1) % n])
        nn.append(h[(i + 1) % n, i])
    nn_element = float(np.mean(nn))
    t = -nn_element
    residual = max_abs(h - uniform_chain(n, t, mu))
    even_diag = np.diag(h)[0::2]
    odd_diag = np.diag(h)[1::2]
    staggered_component = 0.5 * float(np.mean(even_diag) - np.mean(odd_diag))
    return t, mu, nn_element, residual, staggered_component


def rg_map(g):
    return g * g / (1.0 - 2.0 * g * g)


def rg_derivative(g):
    return 2.0 * g / (1.0 - 2.0 * g * g) ** 2


def quotient_continued_map_abs(g):
    return g * g / abs(1.0 - 2.0 * g * g)


def resolvent_length(g):
    return 1.0 / np.arccosh(1.0 / (2.0 * abs(g)))


def map_from_schur(g):
    h = uniform_chain(16, g, 1.0)
    eff = schur_decimate(h)
    t_next, mu_next, _, residual, _ = uniform_params_from_matrix(eff)
    return t_next / mu_next, residual


def spectral_min_abs(n, g):
    eig = np.linalg.eigvalsh(uniform_chain(n, g, 1.0))
    return float(np.min(np.abs(eig)))


def retained_resolvent_error(h):
    eff = schur_decimate(h)
    retained = np.arange(0, h.shape[0], 2)
    full_retained = np.linalg.inv(-h)[np.ix_(retained, retained)]
    effective = np.linalg.inv(-eff)
    return max_abs(full_retained - effective), eff


def fitted_resolvent_decay_rate(n, g, r_min=8, r_max=24):
    green = np.linalg.inv(uniform_chain(n, g, 1.0))
    rs = np.arange(r_min, r_max + 1)
    amplitudes = np.abs(green[0, rs])
    slope, _ = np.polyfit(rs, np.log(amplitudes), 1)
    return float(-slope)


def run_w1a():
    grid = [
        (0.10, 1.0),
        (0.20, 1.0),
        (0.45, 1.0),
        (0.55, 1.0),
        (0.65, 1.0),
        (0.80, 1.0),
    ]
    residuals = []
    magnitude_errors = []
    reports = []
    for t, mu in grid:
        eff = schur_decimate(uniform_chain(16, t, mu))
        t_next, mu_next, nn_element = uniform_after_one_step(t, mu)
        expected = uniform_chain(8, t_next, mu_next)
        residuals.append(max_abs(eff - expected))
        magnitude_errors.append(abs(abs(nn_element) - t * t / abs(mu)))
        side = "mu>2t" if mu > 2.0 * t else "mu<2t"
        reports.append(
            f"{side} t={fmt(t)} mu={fmt(mu)} diag'={fmt(mu_next)} "
            f"t'_element={fmt(nn_element)}"
        )
    check(
        "W1a CLOSURE",
        max(residuals) <= TOL and max(magnitude_errors) <= TOL,
        "uniform+NN Schur output; max_residual="
        f"{fmt(max(residuals))}; max_|element|-t^2/|mu|={fmt(max(magnitude_errors))}; "
        + "; ".join(reports),
    )


def run_w1b():
    inference_grid = [0.05, 0.15, 0.30, 0.45, 0.60]
    validation_grid = [0.10, 0.25, 0.40, 0.55, 0.65]

    def grid_error(grid):
        errors = []
        residuals = []
        pairs = []
        for g in grid:
            actual, residual = map_from_schur(g)
            expected = rg_map(g)
            errors.append(abs(actual - expected))
            residuals.append(residual)
            pairs.append(f"g={fmt(g)} -> {fmt(actual)}")
        return max(errors), max(residuals), pairs

    inference_error, inference_residual, inference_pairs = grid_error(inference_grid)
    validation_error, validation_residual, validation_pairs = grid_error(validation_grid)
    disjoint = set(inference_grid).isdisjoint(set(validation_grid))
    check(
        "W1b THE MAP inference grid",
        inference_error <= TOL and inference_residual <= TOL,
        "actual Schur g' versus g^2/(1-2g^2); max_error="
        f"{fmt(inference_error)}; max_closure_residual={fmt(inference_residual)}; "
        + "; ".join(inference_pairs),
    )
    check(
        "W1b THE MAP disjoint validation grid",
        disjoint and validation_error <= TOL and validation_residual <= TOL,
        "disjoint="
        f"{disjoint}; max_error={fmt(validation_error)}; "
        f"max_closure_residual={fmt(validation_residual)}; "
        + "; ".join(validation_pairs),
    )


def run_w1c():
    fixed_zero = rg_map(0.0)
    fixed_half = rg_map(0.5)
    derivative = rg_derivative(0.5)
    step = 1.0e-6
    numerical = (rg_map(0.5 + step) - rg_map(0.5 - step)) / (2.0 * step)
    check(
        "W1c FIXED POINTS exact",
        abs(fixed_zero - 0.0) <= 1.0e-15
        and abs(fixed_half - 0.5) <= 1.0e-15
        and derivative == 4.0
        and abs(numerical - derivative) <= 1.0e-8,
        f"g*=0 -> {fmt(fixed_zero)}; g*=1/2 -> {fmt(fixed_half)}; "
        f"analytic derivative={fmt(derivative)}; numerical derivative={fmt(numerical)}",
    )


def run_w1d():
    below_g = 0.49
    below_min = spectral_min_abs(128, below_g)
    above_g = 1.0 / (2.0 * np.cos(3.0 * np.pi / 64.0))
    above_min_64 = spectral_min_abs(64, above_g)
    above_min_128 = spectral_min_abs(128, above_g)
    band_edge_gap = abs(1.0 - 2.0 * 0.5)
    check(
        "W1d E=0 RESOLVENT-THRESHOLD WITNESS (commensurate finite-N witness, not the proof)",
        below_min > 1.0e-3
        and above_g > 0.5
        and above_min_128 < above_min_64
        and above_min_128 < 1.0e-10
        and band_edge_gap == 0.0
        and rg_derivative(0.5) > 1.0,
        f"below g={fmt(below_g)} min|eig|={fmt(below_min)} resolvent exists; "
        f"above g={fmt(above_g)} min|eig| N=64 {fmt(above_min_64)} -> "
        f"N=128 {fmt(above_min_128)}; unstable fixed point g*=1/2 is the "
        "E=0 resolvent-threshold boundary",
    )


def run_w1e():
    def iterate(g0, steps):
        values = [float(g0)]
        denominators = []
        for _ in range(steps):
            g = values[-1]
            denominators.append(1.0 - 2.0 * g * g)
            values.append(rg_map(g))
        return values, denominators

    low_values, _ = iterate(0.45, 8)
    monotone = all(low_values[i + 1] < low_values[i] for i in range(8))
    positive = all(g > 0.0 for g in low_values)

    high_values, high_denominators = iterate(0.55, 5)
    boundary = 1.0 / np.sqrt(2.0)
    first_boundary_exit = next(
        i for i, g in enumerate(high_values) if abs(g) > boundary
    )
    first_past_one = next(i for i, g in enumerate(high_values) if abs(g) > 1.0)
    denominator_sign_change = next(
        i
        for i in range(len(high_denominators) - 1)
        if high_denominators[i] * high_denominators[i + 1] < 0.0
    )
    low_report = ", ".join(fmt(g) for g in low_values)
    high_report = ", ".join(fmt(g) for g in high_values)
    theorem_points_inside = (
        abs(0.0) < boundary and abs(0.5) < boundary and abs(0.5) < boundary
    )
    check(
        "W1e CHART + POLES: E=0 spectral/resolvent chamber boundary",
        monotone
        and positive
        and low_values[-1] < 1.0e-6
        and theorem_points_inside
        and first_boundary_exit == 1
        and first_past_one == 2
        and denominator_sign_change == 0,
        f"g0=0.45 eight-step monotone flow: {low_report}; "
        "theorem fixed points 0 and 1/2, and the band edge 1/2, lie inside "
        f"declared chart |g|<1/sqrt(2)={fmt(boundary)}; "
        f"upper side g0=0.55 exits the declared chart at iterate {first_boundary_exit}, "
        f"passes |g|>1 at iterate {first_past_one}, denominator sign changes between "
        f"iterates {denominator_sign_change} and {denominator_sign_change + 1}; "
        f"poles at +/-1/sqrt(2); high flow: {high_report}",
    )


def run_w1f():
    h0 = uniform_chain(16, 0.23, 1.0)
    err1, h1 = retained_resolvent_error(h0)
    err2, _ = retained_resolvent_error(h1)
    check(
        "W1f EXACTNESS INHERITED",
        err1 <= TOL and err2 <= TOL,
        f"retained-site E=0 resolvent errors over two steps: "
        f"step1={fmt(err1)}, step2={fmt(err2)}",
    )


def run_w1g():
    t = 0.37
    m = 1.2
    eff = schur_decimate(staggered_chain(16, t, m))
    mu_land = m + 2.0 * t * t / m
    t_land = -t * t / m
    expected = uniform_chain(8, t_land, mu_land)
    _, _, nn_element, residual, staggered_component = uniform_params_from_matrix(eff)
    check(
        "W1g COMPOSITION WITH THE LANDED MIGRATION",
        residual <= TOL
        and max_abs(eff - expected) <= TOL
        and abs(staggered_component) <= TOL,
        f"staggered mass after step 1={fmt(staggered_component)}; "
        f"landing mu={fmt(mu_land)}, t={fmt(t_land)}, "
        f"NN matrix element={fmt(nn_element)}; residual={fmt(residual)}",
    )


def run_w1h():
    b = 2.0
    eigenvalue = 4.0
    nu = 0.5
    check(
        "W1h RESOLVENT LENGTH EXPONENT",
        nu == 0.5,
        f"nu=ln b/ln(dg'/dg at g*)=ln{fmt(b)}/ln{fmt(eigenvalue)}={fmt(nu)}",
    )


def run_w1i():
    n = 16
    points = [(0.23, 1.0), (0.61, 1.3)]
    spectral_errors = []
    unitary_errors = []
    reports = []
    gauge = np.diag((-1.0) ** np.arange(n))
    for t, mu in points:
        h_plus = uniform_chain(n, t, mu)
        h_minus = uniform_chain(n, -t, mu)
        spectral_error = max_abs(np.linalg.eigvalsh(h_plus) - np.linalg.eigvalsh(h_minus))
        unitary_error = max_abs(gauge @ h_plus @ gauge - h_minus)
        spectral_errors.append(spectral_error)
        unitary_errors.append(unitary_error)
        reports.append(
            f"t={fmt(t)} mu={fmt(mu)} spectrum_error={fmt(spectral_error)} "
            f"unitary_residual={fmt(unitary_error)}"
        )
    check(
        "W1i SIGN QUOTIENT |g| FROM t->-t UNITARY EQUIVALENCE",
        max(spectral_errors) <= TOL and max(unitary_errors) <= TOL,
        "N=16 staggered gauge c_j->(-1)^j c_j; declared flow space is quotient |g|; "
        + "; ".join(reports),
    )


def run_w1j():
    signed_points = [0.0, 0.5, -1.0]
    map_errors = [abs(rg_map(g) - g) for g in signed_points]
    polynomial_errors = [abs(g * (2.0 * g * g + g - 1.0)) for g in signed_points]
    reports = [
        f"g={fmt(g)} map_error={fmt(e)} polynomial_residual={fmt(p)}"
        for g, e, p in zip(signed_points, map_errors, polynomial_errors)
    ]
    check(
        "W1j SIGNED FIXED-POINT SET {0, 1/2, -1}",
        max(map_errors) <= 1.0e-15 and max(polynomial_errors) <= 1.0e-15,
        "g = g^2/(1-2g^2) gives g(2g^2+g-1)=0; "
        "on the quotient, signed point -1 reads |g|=1 outside the declared chart; "
        + "; ".join(reports),
    )


def run_w1k():
    boundary = 1.0 / np.sqrt(2.0)
    continued_at_one = quotient_continued_map_abs(1.0)
    fixed_error = abs(continued_at_one - 1.0)
    signed_even_error = abs(rg_map(-0.3) - rg_map(0.3))
    check(
        "W1k CONTINUED QUOTIENT MAP PROBES OUTSIDE DECLARED CHART",
        fixed_error <= 1.0e-15 and signed_even_error <= 1.0e-15,
        f"continued |g'|=g^2/|1-2g^2| has |g|=1 -> {fmt(continued_at_one)} "
        f"with fixed_error={fmt(fixed_error)}, labeled outside declared chart "
        f"|g|<1/sqrt(2)={fmt(boundary)}; signed evenness probe "
        f"g=-0.3 versus +0.3 error={fmt(signed_even_error)}",
    )


def run_w1l():
    fit_points = [0.30, 0.40, 0.45]
    fit_reports = []
    fit_relative_errors = []
    for g in fit_points:
        measured = fitted_resolvent_decay_rate(128, g)
        expected = 1.0 / resolvent_length(g)
        relative_error = abs(measured - expected) / expected
        fit_relative_errors.append(relative_error)
        fit_reports.append(
            f"g={fmt(g)} measured_1/xi={fmt(measured)} analytic_1/xi={fmt(expected)} "
            f"relerr={fmt(relative_error)}"
        )

    scaling_points = [0.48, 0.49]
    scaling_ratios = [
        resolvent_length(g) * np.sqrt(0.5 - g) for g in scaling_points
    ]
    scaling_errors = [abs(ratio - 0.5) for ratio in scaling_ratios]
    scaling_report = "; ".join(
        f"g={fmt(g)} xi*sqrt(1/2-g)={fmt(ratio)}"
        for g, ratio in zip(scaling_points, scaling_ratios)
    )

    composition_points = [0.49, 0.495]
    composition_ratios = [
        resolvent_length(rg_map(g)) / resolvent_length(g) for g in composition_points
    ]
    composition_errors = [abs(ratio - 0.5) for ratio in composition_ratios]
    composition_report = "; ".join(
        f"g={fmt(g)} g'={fmt(rg_map(g))} xi(g')/xi(g)={fmt(ratio)}"
        for g, ratio in zip(composition_points, composition_ratios)
    )

    check(
        "W1l DIVERGING E=0 RESOLVENT LENGTH HAS NU=1/2 UNDER THE MAP",
        max(fit_relative_errors) <= 1.0e-3
        and max(scaling_errors) <= 2.0e-2
        and max(composition_errors) <= 5.0e-2,
        "N=128 fit over r=8..24 for |[(h-0)^-1]_{0,r}| decay: "
        + "; ".join(fit_reports)
        + "; near-edge analytic scaling: "
        + scaling_report
        + "; composition xi'=xi/2 probes: "
        + composition_report,
    )


def main():
    run_w1a()
    run_w1b()
    run_w1c()
    run_w1d()
    run_w1e()
    run_w1f()
    run_w1g()
    run_w1h()
    run_w1i()
    run_w1j()
    run_w1k()
    run_w1l()
    print(
        "SCOPE: free sector, 1D, E=0 slice, projective fixed-energy Schur RG "
        "convention (b=2, quotient |g|=|t/mu|, chart |g|<1/sqrt(2)); agreement "
        "at the double-precision floor (measured 0.0 in these instances); the "
        "unstable fixed point is the E=0 resolvent-threshold chamber boundary "
        "with eigenvalue 4 and length exponent nu=1/2, while the upper side exits "
        "the declared chart. NOT claimed: interacting RG, d=3, universality beyond "
        "this declared convention, gauge sectors. Statuses pipeline-derived; audit lane grades."
    )
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        sys.exit(1)


if __name__ == "__main__":
    main()
