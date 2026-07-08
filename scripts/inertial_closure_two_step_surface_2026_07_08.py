#!/usr/bin/env python3
"""Inertial closure checks on the free staggered two-step transfer surface.

Companion runner for
INERTIAL_CLOSURE_WIDTH_INDEPENDENT_ACCELERATION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md.

Declared imports checked here:
- I-DYN: two-step transfer surface with
  E(p)=arcsinh(sqrt(m^2 + sum_mu sin^2 p_mu)).
- I-MASS: inertial coefficient M_I(m)=m*sqrt(1+m^2).
- I-TIME: centroid velocity is the exact band velocity.
- I-EXT: weak linear probe coupled to conserved Q-density, coefficient free;
  explicitly NOT the mass-weighted -m*phi coupling.

The main legs use the exact momentum-shift gauge for a uniform weak force:
canonical momentum density is unchanged and the physical band momentum is
p - g*t*e_3 on the torus.  No position-space evolution is needed there.
"""

import numpy as np
import scipy.sparse.linalg as spla
import sympy as sp


D = 3
GH_N_3D = 48
GH_N_1D = 96
# Gated legs run at masses whose curvature window admits the declared widths;
# m = 0.2 (near-gapless) and the historical narrow widths are reported as
# out-of-window context, which is itself T4 content (the window closes as
# m -> 0).
M_GATED = (0.5, 1.0, 2.0)
M_CONTEXT = (0.2,)
G_SWEEP = (1.0e-4, 2.0e-4, 4.0e-4)
SIGMA_X_WINDOW = (3.0, 4.5, 6.0, 9.0, 12.0)
SIGMA_X_HISTORICAL = (0.5, 1.0, 1.5)
M0_SIGMA_X_SWEEP = (0.5, 1.0, 1.5)
CROSS_M_SWEEP = (0.5, 1.0)
CROSS_SIGMA_X_SWEEP = (3.0, 6.0)
T_MAIN = 80.0
T_CROSS = 80.0
P_STAR_CAP = np.pi / 4.0
N_CROSS = 256


def p_star(m: float) -> float:
    """Mass-dependent curvature window certified by this runner: the
    second-order Taylor control of E_33 is used only for |q|_inf <= p_*(m),
    with p_*(m) shrinking linearly as the gap closes."""
    if m <= 0.0:
        return 0.0
    return float(min(P_STAR_CAP, 0.6 * m))
PASS_COUNT = 0
FAIL_COUNT = 0
FLAGS: list[str] = []
_HERMITE_CACHE: dict[int, tuple[np.ndarray, np.ndarray]] = {}
_GRID3_CACHE: dict[float, tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]] = {}
_GRID1_CACHE: dict[float, tuple[np.ndarray, np.ndarray]] = {}
_H0_CACHE: dict[float, np.ndarray] = {}


class SlopeResult:
    def __init__(self, measured: float, predicted: float, rel_residual: float, intercept: float, r2: float):
        self.measured = float(measured)
        self.predicted = float(predicted)
        self.rel_residual = float(rel_residual)
        self.intercept = float(intercept)
        self.r2 = float(r2)


class WindowRun:
    def __init__(self, label: str, m: float, sigma_x: float, g: float, t_max: float):
        self.label = label
        self.m = float(m)
        self.sigma_x = float(sigma_x)
        self.g = float(g)
        self.t_max = float(t_max)


WINDOW_RUNS: list[WindowRun] = []


def report(num: int, name: str, condition: bool, residual: float, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    PASS_COUNT += int(ok)
    FAIL_COUNT += int(not ok)
    line = f"CHECK-{num:02d} {name}: {'PASS' if ok else 'FAIL'} residual={residual:.3e}"
    if detail:
        line += f" {detail}"
    print(line)


def note_flag(text: str) -> None:
    if text not in FLAGS:
        FLAGS.append(text)


def sigma_p_from_x(sigma_x: float) -> float:
    return 1.0 / (2.0 * sigma_x)


def dispersion(m: float, p: tuple[float, ...]) -> float:
    """Authority dispersion: E = arcsinh(sqrt(m^2 + sum_mu sin^2 p_mu))."""
    s2 = sum(np.sin(component) ** 2 for component in p)
    return float(np.arcsinh(np.sqrt(m * m + s2)))


def inertial_mass(m: float) -> float:
    return float(m * np.sqrt(1.0 + m * m))


def energy3(m: float, p1: np.ndarray, p2: np.ndarray, p3: np.ndarray) -> np.ndarray:
    s2 = np.sin(p1) ** 2 + np.sin(p2) ** 2 + np.sin(p3) ** 2
    return np.arcsinh(np.sqrt(m * m + s2))


def velocity3_component(
    m: float, p1: np.ndarray, p2: np.ndarray, p3: np.ndarray, axis: int
) -> np.ndarray:
    sins = (np.sin(p1), np.sin(p2), np.sin(p3))
    coss = (np.cos(p1), np.cos(p2), np.cos(p3))
    s2 = sins[0] ** 2 + sins[1] ** 2 + sins[2] ** 2
    root = np.sqrt(m * m + s2)
    denom = root * np.sqrt(1.0 + m * m + s2)
    numer = sins[axis] * coss[axis]
    return np.divide(numer, denom, out=np.zeros_like(numer), where=denom > 0.0)


def energy1(m: float, p: np.ndarray) -> np.ndarray:
    return np.arcsinh(np.sqrt(m * m + np.sin(p) ** 2))


def velocity1(m: float, p: np.ndarray) -> np.ndarray:
    s = np.sin(p)
    s2 = s * s
    root = np.sqrt(m * m + s2)
    denom = root * np.sqrt(1.0 + m * m + s2)
    return np.divide(s * np.cos(p), denom, out=np.zeros_like(p), where=denom > 0.0)


def hermite_base(n: int) -> tuple[np.ndarray, np.ndarray]:
    if n in _HERMITE_CACHE:
        return _HERMITE_CACHE[n]
    nodes, weights = np.polynomial.hermite.hermgauss(n)
    value = (nodes.astype(float), (weights / np.sqrt(np.pi)).astype(float))
    _HERMITE_CACHE[n] = value
    return value


def gaussian_grid3(sigma_p: float) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    key = round(float(sigma_p), 15)
    if key in _GRID3_CACHE:
        return _GRID3_CACHE[key]
    nodes, weights = hermite_base(GH_N_3D)
    p = np.sqrt(2.0) * sigma_p * nodes
    p1, p2, p3 = np.meshgrid(p, p, p, indexing="ij")
    w1, w2, w3 = np.meshgrid(weights, weights, weights, indexing="ij")
    value = (p1.ravel(), p2.ravel(), p3.ravel(), (w1 * w2 * w3).ravel())
    _GRID3_CACHE[key] = value
    return value


def gaussian_grid1(sigma_p: float) -> tuple[np.ndarray, np.ndarray]:
    key = round(float(sigma_p), 15)
    if key in _GRID1_CACHE:
        return _GRID1_CACHE[key]
    nodes, weights = hermite_base(GH_N_1D)
    value = (np.sqrt(2.0) * sigma_p * nodes, weights)
    _GRID1_CACHE[key] = value
    return value


def fit_slope_through_g(g_values: tuple[float, ...], accel_values: list[float]) -> tuple[float, float, float]:
    g_arr = np.array(g_values, dtype=float)
    a_arr = np.array(accel_values, dtype=float)
    slope, intercept = np.polyfit(g_arr, a_arr, 1)
    pred = slope * g_arr + intercept
    ss_res = float(np.sum((a_arr - pred) ** 2))
    ss_tot = float(np.sum((a_arr - float(np.mean(a_arr))) ** 2))
    r2 = 1.0 if ss_tot == 0.0 else 1.0 - ss_res / ss_tot
    return float(slope), float(intercept), float(r2)


def displacement3_delta(m: float, sigma_x: float, g: float, t_max: float) -> float:
    sigma_p = sigma_p_from_x(sigma_x)
    p1, p2, p3, weights = gaussian_grid3(sigma_p)
    e_initial = energy3(m, p1, p2, p3)
    e_shifted = energy3(m, p1, p2, p3 - g * t_max)
    v_free = velocity3_component(m, p1, p2, p3, 2)
    forced_displacement = np.sum(weights * ((e_initial - e_shifted) / g))
    free_displacement = t_max * np.sum(weights * v_free)
    return float(forced_displacement - free_displacement)


def slope_result3(m: float, sigma_x: float, t_max: float, label: str = "3d-gated") -> SlopeResult:
    accel_values = []
    for g in G_SWEEP:
        WINDOW_RUNS.append(WindowRun(label, m, sigma_x, g, t_max))
        delta = displacement3_delta(m, sigma_x, g, t_max)
        accel_values.append(2.0 * delta / (t_max * t_max))
    measured, intercept, r2 = fit_slope_through_g(G_SWEEP, accel_values)
    predicted = -1.0 / inertial_mass(m)
    rel = abs(measured - predicted) / abs(predicted)
    return SlopeResult(measured, predicted, rel, intercept, r2)


def displacement1_delta_momentum(m: float, sigma_x: float, g: float, t_max: float) -> float:
    sigma_p = sigma_p_from_x(sigma_x)
    p, weights = gaussian_grid1(sigma_p)
    e_initial = energy1(m, p)
    e_shifted = energy1(m, p - g * t_max)
    v_free = velocity1(m, p)
    forced_displacement = np.sum(weights * ((e_initial - e_shifted) / g))
    free_displacement = t_max * np.sum(weights * v_free)
    return float(forced_displacement - free_displacement)


def slope_result1_momentum(m: float, sigma_x: float, t_max: float) -> tuple[float, float, float]:
    accel_values = []
    for g in G_SWEEP:
        accel_values.append(2.0 * displacement1_delta_momentum(m, sigma_x, g, t_max) / (t_max * t_max))
    return fit_slope_through_g(G_SWEEP, accel_values)


_FOURTH_DERIV_CACHE: dict[str, object] = {}
_BOUND_CACHE: dict[float, tuple[float, float, float, float]] = {}


def _curvature_toolkit():
    """Sympy-exact E_33 and the two independent fourth derivatives at 0."""
    if _FOURTH_DERIV_CACHE:
        return (
            _FOURTH_DERIV_CACHE["e33"],
            _FOURTH_DERIV_CACHE["d4_ax"],
            _FOURTH_DERIV_CACHE["d4_mx"],
        )
    m_s = sp.symbols("m", positive=True)
    p1_s, p2_s, p3_s = sp.symbols("p1 p2 p3", real=True)
    E = sp.asinh(sp.sqrt(m_s**2 + sp.sin(p1_s) ** 2 + sp.sin(p2_s) ** 2 + sp.sin(p3_s) ** 2))
    E33 = sp.diff(E, p3_s, 2)
    at0 = {p1_s: 0, p2_s: 0, p3_s: 0}
    d4_ax = sp.simplify(sp.diff(E, p3_s, 4).subs(at0))
    d4_mx = sp.simplify(sp.diff(E, p1_s, 2, p3_s, 2).subs(at0))
    e33_fn = sp.lambdify((m_s, p1_s, p2_s, p3_s), E33, "numpy")
    d4_ax_fn = sp.lambdify(m_s, d4_ax, "numpy")
    d4_mx_fn = sp.lambdify(m_s, d4_mx, "numpy")
    _FOURTH_DERIV_CACHE.update(
        {"e33": e33_fn, "d4_ax": d4_ax_fn, "d4_mx": d4_mx_fn, "d4_ax_expr": d4_ax, "d4_mx_expr": d4_mx}
    )
    return e33_fn, d4_ax_fn, d4_mx_fn


def bound_constants(m: float) -> tuple[float, float, float, float]:
    """Return (C4_win, A_iso, osc_term, rest_coeff) for mass m.

    C4_win   = (1/2) M_I sup_{|q|_inf <= p_*(m)} ||Hess E_33(q)||_2 (numeric),
    A_iso    = (1/2) M_I |d4_ax + 2 d4_mx| (isotropic per-axis-variance
               collapse coefficient; sympy-exact fourth derivatives),
    osc_term = M_I * (max - min of E_33 over the BZ) for the T3' tail addend,
    rest_coeff = (1/2) M_I |d4_ax| (the note's closed-form lower bound).
    """
    key = round(float(m), 15)
    if key in _BOUND_CACHE:
        return _BOUND_CACHE[key]
    e33_fn, d4_ax_fn, d4_mx_fn = _curvature_toolkit()
    mi = inertial_mass(m)
    ps = p_star(m)
    h = 2.0e-3

    def e33(q1: float, q2: float, q3: float) -> float:
        return float(e33_fn(m, q1, q2, q3))

    def hess_norm(q: np.ndarray) -> float:
        H = np.zeros((3, 3))
        base = e33(*q)
        for a in range(3):
            ea = np.zeros(3)
            ea[a] = h
            H[a, a] = (e33(*(q + ea)) - 2.0 * base + e33(*(q - ea))) / (h * h)
            for b in range(a + 1, 3):
                eb = np.zeros(3)
                eb[b] = h
                H[a, b] = H[b, a] = (
                    e33(*(q + ea + eb)) - e33(*(q + ea - eb)) - e33(*(q - ea + eb)) + e33(*(q - ea - eb))
                ) / (4.0 * h * h)
        return float(np.max(np.abs(np.linalg.eigvalsh(H))))

    # Seed the sup with the exact rest-point Hessian eigenvalues
    # (Hess E_33(0) = diag(d4_mx, d4_mx, d4_ax), known symbolically), so the
    # finite-difference scan can only raise the sup, never lose the exact
    # rest-point value to truncation error.
    sup_hess = max(abs(float(d4_ax_fn(m))), abs(float(d4_mx_fn(m))))
    axis = np.linspace(-ps, ps, 9)
    for q1 in axis:
        for q2 in axis:
            for q3 in axis:
                sup_hess = max(sup_hess, hess_norm(np.array([q1, q2, q3])))
    bz_axis = np.linspace(-np.pi, np.pi, 21)
    B1, B2, B3 = np.meshgrid(bz_axis, bz_axis, bz_axis, indexing="ij")
    e33_bz = e33_fn(m, B1, B2, B3)
    osc_term = mi * float(np.max(e33_bz) - np.min(e33_bz))
    c4_win = 0.5 * mi * sup_hess
    a_iso = 0.5 * mi * abs(float(d4_ax_fn(m)) + 2.0 * float(d4_mx_fn(m)))
    rest_coeff = 0.5 * mi * abs(float(d4_ax_fn(m)))
    value = (c4_win, a_iso, osc_term, rest_coeff)
    _BOUND_CACHE[key] = value
    return value


def gaussian_tail_mass(sigma_p: float, ps: float, shift3: float) -> float:
    from scipy.special import erf

    def phi(z: float) -> float:
        return 0.5 * (1.0 + float(erf(z / np.sqrt(2.0))))

    def p_in(center: float) -> float:
        return max(0.0, phi((ps - center) / sigma_p) - phi((-ps - center) / sigma_p))

    return 1.0 - p_in(0.0) * p_in(0.0) * p_in(shift3)


def t3_bound(m: float, sigma_p: float, g: float, t_max: float) -> tuple[float, float]:
    """Return (window_bound, eps_tail) of T3/T3' for one run."""
    c4_win, _, osc_term, _ = bound_constants(m)
    window_part = c4_win * (3.0 * sigma_p * sigma_p + (g * t_max) ** 2)
    eps_tail = osc_term * gaussian_tail_mass(sigma_p, p_star(m), abs(g) * t_max)
    return window_part, eps_tail


def qualifies(m: float, sigma_x: float, g: float, t_max: float) -> bool:
    sigma_p = sigma_p_from_x(sigma_x)
    return 3.0 * sigma_p + abs(g) * t_max <= p_star(m)


def check_01_exact_momentum_law() -> None:
    g_sym, t_sym = sp.symbols("g t", real=True)
    symbolic_resid = sp.simplify((-g_sym * t_sym) - (-g_sym * t_sym))
    max_numeric = 0.0
    for sigma_x in SIGMA_X_WINDOW + SIGMA_X_HISTORICAL:
        sigma_p = sigma_p_from_x(sigma_x)
        nodes, weights = hermite_base(GH_N_1D)
        p = np.sqrt(2.0) * sigma_p * nodes
        mean_p = float(np.sum(weights * p))
        for g in G_SWEEP:
            for t in (0.0, 0.25 * T_MAIN, T_MAIN):
                expected = -g * t
                measured = mean_p - g * t
                max_numeric = max(max_numeric, abs(measured - expected), abs(mean_p))
    condition = symbolic_resid == 0 and max_numeric <= 1e-14
    report(
        1,
        "EXACT-MOMENTUM-LAW",
        condition,
        max_numeric,
        "symbolic_residual={} gauge=momentum-shift canonical_rho_fixed physical_p=p-g*t*e3".format(
            symbolic_resid
        ),
    )


def check_02_slope_vs_prediction() -> dict[float, dict[float, SlopeResult]]:
    """Gated: window-qualifying runs must satisfy the T3/T3' bound.

    The gate is bound-compliance, not a flat tolerance: T3 asserts
    |rel_resid| <= C4_win (3 sigma_p^2 + (g t)^2) + eps_tail for
    window-supported/Gaussian packets, and each mass must admit at least one
    informative run (bound <= 0.25) so compliance is not vacuous.
    Out-of-window runs (near-gapless m, historical narrow widths) are
    reported as context: T3 makes no claim there, and T4 explains why.
    """
    results: dict[float, dict[float, SlopeResult]] = {}
    worst_excess = 0.0
    min_r2 = 1.0
    sign_ok = True
    informative_ok = True
    g_max = max(G_SWEEP)

    for m in M_GATED:
        results[m] = {}
        min_bound_for_m = float("inf")
        for sigma_x in SIGMA_X_WINDOW:
            if not qualifies(m, sigma_x, g_max, T_MAIN):
                result = slope_result3(m, sigma_x, T_MAIN, label="3d-context")
                print(
                    "  CHECK-02 m={:.3g} sigma_x={:.3g} slope={:.10e} pred={:.10e} "
                    "rel_resid={:.3e} r2={:.8f} OUT-OF-WINDOW (3sigma_p+|g|t > p_*(m); T3 makes no claim)".format(
                        m, sigma_x, result.measured, result.predicted, result.rel_residual, result.r2
                    )
                )
                continue
            result = slope_result3(m, sigma_x, T_MAIN, label="3d-gated")
            results[m][sigma_x] = result
            sigma_p = sigma_p_from_x(sigma_x)
            window_part, eps_tail = t3_bound(m, sigma_p, g_max, T_MAIN)
            bound = window_part + eps_tail
            min_bound_for_m = min(min_bound_for_m, bound)
            excess = result.rel_residual / bound if bound > 0 else float("inf")
            worst_excess = max(worst_excess, excess)
            min_r2 = min(min_r2, result.r2)
            sign_ok = sign_ok and np.sign(result.measured) == np.sign(result.predicted)
            print(
                "  CHECK-02 m={:.3g} sigma_x={:.3g} slope={:.10e} pred={:.10e} "
                "rel_resid={:.3e} T3_bound={:.3e} eps_tail={:.3e} resid/bound={:.4f} r2={:.8f}".format(
                    m,
                    sigma_x,
                    result.measured,
                    result.predicted,
                    result.rel_residual,
                    bound,
                    eps_tail,
                    excess,
                    result.r2,
                )
            )
        if min_bound_for_m > 0.25:
            informative_ok = False
            note_flag(f"CHECK-02 no informative window run (bound <= 0.25) exists for m={m}")

    for m in M_CONTEXT:
        for sigma_x in SIGMA_X_WINDOW + SIGMA_X_HISTORICAL:
            result = slope_result3(m, sigma_x, T_MAIN, label="3d-context")
            print(
                "  CHECK-02 m={:.3g} sigma_x={:.3g} slope={:.10e} pred={:.10e} rel_resid={:.3e} "
                "OUT-OF-WINDOW (near-gapless: p_*({:.3g})={:.3f} admits none of the declared widths)".format(
                    m, sigma_x, result.measured, result.predicted, result.rel_residual, m, p_star(m)
                )
            )
    for m in M_GATED:
        for sigma_x in SIGMA_X_HISTORICAL:
            result = slope_result3(m, sigma_x, T_MAIN, label="3d-context")
            print(
                "  CHECK-02 m={:.3g} sigma_x={:.3g} slope={:.10e} pred={:.10e} rel_resid={:.3e} "
                "OUT-OF-WINDOW (historical 2026-04-07 width; reported for continuity)".format(
                    m, sigma_x, result.measured, result.predicted, result.rel_residual
                )
            )

    condition = sign_ok and min_r2 >= 0.999 and worst_excess <= 1.05 and informative_ok
    if worst_excess > 1.05:
        note_flag("CHECK-02 a window-qualifying run violates the T3/T3' bound")
    report(
        2,
        "SLOPE-VS-T3-BOUND",
        condition,
        worst_excess,
        f"worst_resid/bound={worst_excess:.4f} min_r2={min_r2:.8f} gate=bound-compliance+informative",
    )
    return results


def check_03_residual_collapse(results: dict[float, dict[float, SlopeResult]]) -> None:
    """Gated: on window-qualifying widths the residual collapses as
    sigma_p^2 with the ISOTROPIC fourth-derivative coefficient
    A_iso = (1/2) M_I |d4_ax + 2 d4_mx| (per-axis variance), which includes
    the transverse cross-derivatives the on-axis-only formula misses."""
    _curvature_toolkit()
    d4_ax_expr = _FOURTH_DERIV_CACHE["d4_ax_expr"]
    d4_mx_expr = _FOURTH_DERIV_CACHE["d4_mx_expr"]
    all_alpha_ok = True
    all_coeff_ok = True
    worst_alpha_resid = 0.0
    worst_coeff_log_ratio = 0.0

    print(f"  CHECK-03 sympy_d4_axial={d4_ax_expr}")
    print(f"  CHECK-03 sympy_d4_mixed={d4_mx_expr}")
    for m in M_GATED:
        widths = sorted(results[m].keys())
        if len(widths) < 3:
            all_alpha_ok = False
            note_flag(f"CHECK-03 fewer than 3 window-qualifying widths for m={m}")
            continue
        # Collapse residuals are measured at the SMALLEST probe strength so
        # the (g t)^2 window-drift term (which does not scale with sigma)
        # cannot floor the fit, and modeled as rel = A x + B x^2 in
        # x = sigma_p^2: the quadratic term is the T3 leading order, the
        # quartic term absorbs the genuine higher-order Taylor content that a
        # pure log-log fit misreads as a lowered exponent.
        g_small = min(G_SWEEP)
        sigma_ps = np.array([sigma_p_from_x(sigma_x) for sigma_x in widths], dtype=float)
        rels = []
        for sigma_x in widths:
            a_small = 2.0 * displacement3_delta(m, sigma_x, g_small, T_MAIN) / (T_MAIN * T_MAIN)
            a_pred = -g_small / inertial_mass(m)
            rels.append(abs(a_small / a_pred - 1.0))
        rels = np.array(rels, dtype=float)
        x = sigma_ps**2
        design = np.column_stack([x, x * x])
        coeffs, *_ = np.linalg.lstsq(design, rels, rcond=None)
        a_fit, b_fit = float(coeffs[0]), float(coeffs[1])
        alpha, _ = np.polyfit(np.log(sigma_ps), np.log(np.maximum(rels, 1e-300)), 1)
        _, a_iso, _, _ = bound_constants(m)
        log_ratio = abs(np.log(a_fit / a_iso)) if a_fit > 0.0 and a_iso > 0.0 else float("inf")
        coeff_ok = log_ratio <= np.log(2.0)
        all_coeff_ok = all_coeff_ok and coeff_ok
        alpha_ok = a_fit > 0.0
        all_alpha_ok = all_alpha_ok and alpha_ok
        worst_alpha_resid = max(worst_alpha_resid, abs(alpha - 2.0) if np.isfinite(alpha) else float("inf"))
        worst_coeff_log_ratio = max(worst_coeff_log_ratio, log_ratio)
        print(
            "  CHECK-03 m={:.3g} widths={} A={:.10e} B={:.6e} A_iso_pred={:.10e} A/A_iso={:.6f} "
            "loglog_alpha_context={:.6f}".format(
                m, widths, a_fit, b_fit, a_iso, a_fit / a_iso if a_iso > 0.0 else float("nan"), alpha
            )
        )

    if not all_alpha_ok:
        note_flag("CHECK-03 leading collapse coefficient is not positive on window-qualifying widths")
    if not all_coeff_ok:
        note_flag("CHECK-03 fitted coefficient departs from the isotropic prediction by more than 2x")
    report(
        3,
        "RESIDUAL-COLLAPSE",
        all_alpha_ok and all_coeff_ok,
        worst_coeff_log_ratio,
        f"model=A*sigma_p^2+B*sigma_p^4 gate=|log(A/A_iso)|<=log2 worst_log_A_over_Aiso={worst_coeff_log_ratio:.3e}",
    )


def check_04_m0_control() -> None:
    slopes = []
    for sigma_x in M0_SIGMA_X_SWEEP:
        accel_values = []
        for g in G_SWEEP:
            WINDOW_RUNS.append(WindowRun("m0", 0.0, sigma_x, g, T_MAIN))
            delta = displacement3_delta(0.0, sigma_x, g, T_MAIN)
            accel_values.append(2.0 * delta / (T_MAIN * T_MAIN))
        measured, intercept, r2 = fit_slope_through_g(G_SWEEP, accel_values)
        slopes.append(measured)
        print(
            "  CHECK-04 m=0 sigma_x={:.3g} slope={:.10e} intercept={:.3e} r2={:.8f}".format(
                sigma_x, measured, intercept, r2
            )
        )

    slopes_arr = np.array(slopes, dtype=float)
    rel_spread = float((np.max(slopes_arr) - np.min(slopes_arr)) / np.mean(np.abs(slopes_arr)))
    condition = rel_spread > 0.50
    if condition:
        note_flag("CHECK-04 m=0 reproduces width-split behavior, so the closure is singular at m=0")
    report(
        4,
        "M0-CONTROL",
        condition,
        rel_spread,
        "slopes(widths 0.5/1.0/1.5)={:.6e}/{:.6e}/{:.6e} historical_2026-04-07=-73.45/-7.05/-18.28".format(
            slopes[0], slopes[1], slopes[2]
        ),
    )


def check_05_window_bloch() -> None:
    """Gated over the 3d-gated runs only: those must sit inside p_*(m) with
    t << t_Bloch. Context runs (m0 control, historical widths, near-gapless
    m, 1d cross-check) are printed with their margins but deliberately sit
    where T3 makes no claim."""
    all_inside = True
    all_bloch = True
    min_margin = float("inf")
    max_bloch_ratio = 0.0
    gated_count = 0
    for run in WINDOW_RUNS:
        sigma_p = sigma_p_from_x(run.sigma_x)
        ps = p_star(run.m)
        occupied_radius = abs(run.g) * run.t_max + 3.0 * sigma_p
        margin = ps - occupied_radius
        t_bloch = 2.0 * np.pi / abs(run.g)
        bloch_ratio = run.t_max / t_bloch
        gated = run.label == "3d-gated"
        if gated:
            gated_count += 1
            all_inside = all_inside and margin >= 0.0
            all_bloch = all_bloch and bloch_ratio < 0.10
            min_margin = min(min_margin, margin)
            max_bloch_ratio = max(max_bloch_ratio, bloch_ratio)
        print(
            "  CHECK-05 label={} m={:.3g} sigma_x={:.3g} g={:.1e} t_max={:.3g} "
            "|g|t+3sigma_p={:.6f} p_star(m)={:.6f} margin={:.6f} t/t_Bloch={:.6e} {}".format(
                run.label,
                run.m,
                run.sigma_x,
                run.g,
                run.t_max,
                occupied_radius,
                ps,
                margin,
                bloch_ratio,
                ("GATED-" + ("OK" if margin >= 0.0 and bloch_ratio < 0.10 else "BAD")) if gated else "CONTEXT",
            )
        )

    condition = gated_count > 0 and all_inside and all_bloch
    if not condition:
        note_flag("CHECK-05 a gated run violates its p_*(m) window or the Bloch bound")
    residual = max(max(0.0, -min_margin), max(0.0, max_bloch_ratio - 0.10)) if gated_count else float("inf")
    report(
        5,
        "WINDOW/BLOCH",
        condition,
        residual,
        f"gated_runs={gated_count} min_gated_margin={min_margin:.6e} max_t_over_tBloch={max_bloch_ratio:.6e}",
    )


def check_08_bound_constants() -> None:
    """Prints the T3/T3' constants per gated mass and verifies numerically
    that the note's closed-form rest-point coefficient lower-bounds the
    window constant C4_win."""
    all_ok = True
    worst = 0.0
    for m in M_GATED:
        c4_win, a_iso, osc_term, rest_coeff = bound_constants(m)
        ok = c4_win >= rest_coeff * (1.0 - 1.0e-6)
        all_ok = all_ok and ok
        worst = max(worst, rest_coeff - c4_win)
        print(
            "  CHECK-08 m={:.3g} C4_win={:.6e} rest_point_coeff={:.6e} A_iso={:.6e} "
            "M_I*osc_BZ(E33)={:.6e} p_star={:.4f} {}".format(
                m, c4_win, rest_coeff, a_iso, osc_term, p_star(m), "OK" if ok else "BAD"
            )
        )
    report(
        8,
        "BOUND-CONSTANTS",
        all_ok,
        max(0.0, worst),
        "gate=C4_win>=rest_point_coeff (note's closed form is a valid lower bound)",
    )


def spectral_h0_1d(m: float) -> np.ndarray:
    key = round(float(m), 15)
    if key in _H0_CACHE:
        return _H0_CACHE[key]
    momenta = 2.0 * np.pi * np.fft.fftfreq(N_CROSS)
    e_values = energy1(m, momenta)
    basis = np.eye(N_CROSS, dtype=complex)
    h0 = np.fft.ifft(e_values[:, None] * np.fft.fft(basis, axis=0), axis=0)
    h0 = 0.5 * (h0 + h0.conj().T)
    _H0_CACHE[key] = h0
    return h0


def centered_x_grid(n: int) -> np.ndarray:
    return np.arange(n, dtype=float) - 0.5 * (n - 1)


def gaussian_packet_x(sigma_x: float) -> np.ndarray:
    x = centered_x_grid(N_CROSS)
    psi = np.exp(-(x * x) / (4.0 * sigma_x * sigma_x)).astype(complex)
    psi /= np.sqrt(np.sum(np.abs(psi) ** 2))
    return psi


def centroid_x(psi: np.ndarray) -> float:
    x = centered_x_grid(N_CROSS)
    prob = np.abs(psi) ** 2
    return float(np.sum(x * prob))


def edge_probability(psi: np.ndarray) -> float:
    x = centered_x_grid(N_CROSS)
    prob = np.abs(psi) ** 2
    return float(np.sum(prob[np.abs(x) > 0.75 * np.max(np.abs(x))]))


def bulk_potential_x() -> np.ndarray:
    x = centered_x_grid(N_CROSS)
    limit = 0.75 * np.max(np.abs(x))
    return np.clip(x, -limit, limit)


def position_space_slope(m: float, sigma_x: float, t_max: float) -> tuple[float, float, float, float]:
    x_probe = bulk_potential_x()
    psi0 = gaussian_packet_x(sigma_x)
    h0 = spectral_h0_1d(m)
    psi_free = spla.expm_multiply((-1.0j * t_max) * h0, psi0)
    free_centroid = centroid_x(psi_free)
    max_edge = edge_probability(psi_free)
    accel_values = []
    for g in G_SWEEP:
        WINDOW_RUNS.append(WindowRun("1d-x", m, sigma_x, g, t_max))
        h = h0 + np.diag(g * x_probe)
        psi_g = spla.expm_multiply((-1.0j * t_max) * h, psi0)
        max_edge = max(max_edge, edge_probability(psi_g))
        delta = centroid_x(psi_g) - free_centroid
        accel_values.append(2.0 * delta / (t_max * t_max))
    slope, intercept, r2 = fit_slope_through_g(G_SWEEP, accel_values)
    return slope, intercept, r2, max_edge


def check_06_position_space_cross_check() -> None:
    max_rel = 0.0
    min_r2 = 1.0
    max_edge = 0.0
    all_ok = True
    for m in CROSS_M_SWEEP:
        for sigma_x in CROSS_SIGMA_X_SWEEP:
            x_slope, x_intercept, x_r2, edge = position_space_slope(m, sigma_x, T_CROSS)
            p_slope, p_intercept, p_r2 = slope_result1_momentum(m, sigma_x, T_CROSS)
            rel = abs(x_slope - p_slope) / max(abs(p_slope), np.finfo(float).eps)
            max_rel = max(max_rel, rel)
            min_r2 = min(min_r2, x_r2, p_r2)
            max_edge = max(max_edge, edge)
            all_ok = all_ok and rel <= 0.05 and edge <= 1.0e-6
            print(
                "  CHECK-06 m={:.3g} sigma_x={:.3g} position_slope={:.10e} "
                "momentum_slope={:.10e} rel={:.3e} x_intercept={:.3e} p_intercept={:.3e} "
                "r2_x={:.8f} r2_p={:.8f} edge_prob={:.3e}".format(
                    m,
                    sigma_x,
                    x_slope,
                    p_slope,
                    rel,
                    x_intercept,
                    p_intercept,
                    x_r2,
                    p_r2,
                    edge,
                )
            )
    if not all_ok:
        note_flag("CHECK-06 1D position-space evolution differs from the momentum-gauge prediction")
    report(
        6,
        "POSITION-SPACE-CROSS-CHECK",
        all_ok,
        max_rel,
        f"max_rel={max_rel:.3e} min_r2={min_r2:.8f} max_edge_prob={max_edge:.3e}",
    )


def check_07_transverse_drift() -> None:
    max_drift = 0.0
    for m in M_GATED:
        for sigma_x in SIGMA_X_WINDOW:
            sigma_p = sigma_p_from_x(sigma_x)
            p1, p2, p3, weights = gaussian_grid3(sigma_p)
            for g in G_SWEEP:
                shifted_p3 = p3 - g * T_MAIN
                v1 = np.sum(weights * velocity3_component(m, p1, p2, shifted_p3, 0))
                v2 = np.sum(weights * velocity3_component(m, p1, p2, shifted_p3, 1))
                max_drift = max(max_drift, abs(float(v1)), abs(float(v2)))
    report(
        7,
        "TRANSVERSE-DRIFT",
        max_drift <= 1.0e-12,
        max_drift,
        "symmetry=rho_even_in_p1_p2_and_E_even_in_p1_p2",
    )


def main() -> int:
    print("INERTIAL CLOSURE ON THE FREE STAGGERED TWO-STEP TRANSFER SURFACE")
    print("d=3, U=1, E(p)=arcsinh(sqrt(m^2+sum_mu sin^2 p_mu)), force gauge p->p-g*t*e3")
    check_01_exact_momentum_law()
    slope_results = check_02_slope_vs_prediction()
    check_03_residual_collapse(slope_results)
    check_04_m0_control()
    check_06_position_space_cross_check()
    check_05_window_bloch()
    check_07_transverse_drift()
    check_08_bound_constants()
    flag_text = "; ".join(FLAGS) if FLAGS else "none"
    print("SUMMARY:")
    print(f"FLAGS: {flag_text}")
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
