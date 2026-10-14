#!/usr/local/bin/python3
"""Conditional local density dynamics and finite-window inverse; synthetic checks."""
from contextlib import redirect_stdout
from tempfile import TemporaryDirectory
import io
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['docs/EXPONENTIAL_SCALAR_DYNAMICAL_INVERSE_BOUNDED_THEOREM_NOTE_2026-10-14.md', 'docs/EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md', 'docs/EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md', 'docs/EXPONENTIAL_SCALAR_DENSITY_INVERSE_BOUNDED_THEOREM_NOTE_2026-10-14.md']
from pathlib import Path
import json, hashlib, argparse
import sympy as s
import numpy as np
from scipy.linalg import expm
from scipy.integrate import solve_ivp
DR_FORCE_SIGN = s.Integer(1)
DR_KINETIC_FACTOR = s.Integer(2)
DR_MASS_SHIFT = s.Integer(0)
DR_GRAVITY_SIGN = s.Integer(1)

def check_dynamics(output_dir):
    checks = []

    def eq(name, e):
        v = s.factor(s.cancel(s.together(e)))
        checks.append(dict(name=name, passed=v == 0, residual=str(v)))

    def ck(name, ok, detail=None):
        checks.append(dict(name=name, passed=bool(ok), detail=detail))
    Q, rho, beta, vs, x, m2 = s.symbols('Q rho beta vs2 k2 M2', positive=True)
    X, Xt, Xr, Zt, Zr = s.symbols('X Xt Xr Zt Zr', real=True)
    Xtt, Xrr, Ztt, Zrr, Zx = s.symbols('Xtt Xrr Ztt Zrr Zx', real=True)
    c = rho / (DR_KINETIC_FACTOR * Q)
    q = beta ** 2
    g = c * q
    L = Q * (Xt ** 2 - Xr ** 2 - m2 * X ** 2) + rho * Zt ** 2 / 2 - rho * vs * Zr ** 2 / 2 + rho * beta * X * Zr
    ELX = 2 * Q * Xtt - 2 * Q * Xrr - s.diff(L, X)
    ELZ = rho * Ztt - rho * vs * Zrr + rho * beta * Xr
    eq('scalar_EL_and_actual_kinetic', ELX / (2 * Q) - (Xtt - Xrr + m2 * X - c * beta * Zr))
    eq('fluid_EL_continuity', ELZ / rho - (Ztt - vs * Zrr + beta * Xr))
    eq('cross_derivative_reciprocity', s.diff(L, X, Zr) - rho * beta)
    eq('kinetic_energy_density_normalization', s.diff(L, Xt, 2) - 2 * Q)
    eq('stationary_energy_linear_cancellation', rho * (s.Symbol('delta') + beta * X) - rho * beta * X - rho * s.Symbol('delta'))
    y = s.symbols('omega2', real=True)
    mass = m2 + DR_MASS_SHIFT * c * q
    for gravity in [0, 1]:
        a = x + mass
        b = vs * x - DR_GRAVITY_SIGN * gravity * c
        mat = s.Matrix([[a - y, DR_FORCE_SIGN * c * beta], [beta * x, b - y]])
        det = (x + m2 - y) * (vs * x - gravity * rho / (2 * Q) - y) - rho / (2 * Q) * q * x
        eq('full_coupled_determinant_' + str(gravity), mat.det() - det)
        canonical = s.diag(1, s.sqrt(x / c))
        M = canonical.inv() * (mat + y * s.eye(2)) * canonical
        eq('canonical_symmetry_' + str(gravity), M[0, 1] - M[1, 0])
        eq('canonical_off_diagonal_' + str(gravity), M[0, 1] - beta * s.sqrt(c * x))
        peff = -x / (b - y)
        eq('eliminate_density_response_' + str(gravity), (b - y) * beta * peff + beta * x)
        eq('scalar_schur_complement_' + str(gravity), mat.det() / (b - y) - (a - y - c * q * x / (b - y)))
        eq('acoustic_pole_not_a_coupled_pole_' + str(gravity), mat.det().subs(y, b) + g * x)
        tr = a + b
        dis = (a - b) ** 2 + 4 * g * x
        eq('root_discriminant_' + str(gravity), tr ** 2 - 4 * mat.det().subs(y, 0) - dis)
        yp = (tr + s.sqrt(dis)) / 2
        ym = (tr - s.sqrt(dis)) / 2
        eq('root_plus_' + str(gravity), mat.det().subs(y, yp))
        eq('root_minus_' + str(gravity), mat.det().subs(y, ym))
        eq('sum_of_roots_' + str(gravity), yp + ym - tr)
        eq('product_of_roots_' + str(gravity), yp * ym - mat.det().subs(y, 0))
        gamma2 = s.symbols('gamma2', positive=True)
        eq('growth_equation_' + str(gravity), mat.det().subs(y, -gamma2) / (a + gamma2) - (gamma2 + vs * x - DR_GRAVITY_SIGN * gravity * c - g * x / (a + gamma2)))
    peff = -x / (vs * x - y)
    eq('high_frequency_particle_density', s.limit(peff, y, s.oo))
    eq('static_compressional_response', peff.subs(y, 0) + 1 / vs)
    ck('static_compressional_response_is_not_three', s.simplify(peff.subs(y, 0) - 3).is_negative)
    eq('dust_static_division_has_pole', s.limit(vs * peff.subs(y, 0), vs, 0) + 1)
    B = s.symbols('B', positive=True)
    bound = 2 * vs / (1 + 3 * vs)
    eq('all_wavelength_susceptibility_threshold', vs * (2 / B - 3) - 1 - (1 + 3 * vs) * (bound - B) / B)
    eq('fixed_metric_determinant', ((x + m2) * (vs * x) - g * x) / x - (vs * (x + m2) - g))
    eq('threshold_equality_positive_finite_k', (vs * (x + m2) - g).subs(m2, g / vs) - vs * x)
    P = vs * x ** 2 + (vs * mass - c * (1 + q)) * x - c * mass
    eq('Jeans_polynomial', P - ((x + mass) * (vs * x - DR_GRAVITY_SIGN * c) - g * x))
    eq('Jeans_lower_endpoint', s.factor(P.subs(x, c / vs)) + c * c * q / vs)
    eq('Jeans_upper_endpoint', s.factor(P.subs(x, c * (1 + q) / vs)) - c * mass * q)
    ck('Jeans_lower_endpoint_strict', (-c * c * q / vs).is_negative)
    ck('Jeans_upper_endpoint_strict', (c * m2 * q).is_positive)
    ck('Jeans_root_product_negative', (-c * m2 / vs).is_negative)
    upper = c * (1 + q)
    gamma2 = s.symbols('gamma2', positive=True)
    rate = c - vs * x + g * x / (x + m2 + gamma2)
    eq('growth_ceiling_positive_remainder', upper - rate - (vs * x + g * (m2 + gamma2) / (x + m2 + gamma2)))
    ck('strict_growth_ceiling', s.simplify(vs * x + g * (m2 + gamma2) / (x + m2 + gamma2)).is_positive)
    eps = s.symbols('epsilon', positive=True)
    eq('candidate_q_envelope', (s.Rational(4, 3) * c - upper).subs(q, s.Rational(1, 3) - eps) - c * eps)
    A = s.symbols('A', positive=True)
    detE = (x + m2 - y) * (vs * x - c - y) - c * q * x
    detJ = (x / A ** 2 + m2 / A ** 2 - y / A ** 2) * (vs * x / A ** 2 - c / A ** 2 - y / A ** 2) - c / A ** 2 * q * (x / A ** 2)
    eq('frame_dispersion_scaling', detJ - detE / A ** 4)
    Xd, Dd, D = s.symbols('Xd Dd D', real=True)
    a = x + m2
    b = vs * x - c
    off = beta * s.sqrt(c * x)
    energy = Xd ** 2 + Dd ** 2 + a * X ** 2 + b * D ** 2 + 2 * off * X * D
    edot = s.diff(energy, X) * Xd + s.diff(energy, D) * Dd + s.diff(energy, Xd) * (-a * X - off * D) + s.diff(energy, Dd) * (-b * D - off * X)
    eq('canonical_energy_conservation', edot)
    cases = []
    out = Path(output_dir)
    out.mkdir(exist_ok=True)
    config = [(0, 0.01, 0.2, 0.05, 0.4), (0, 0.04, 0.2, 4.0, 0.3), (0, 0.04, 0.2, 4.0, 4.0), (0, 0.01, 0.2, 0.05, 8.0), (1, 0.01, 0.2, 0.05, 0.4), (1, 0.04, 0.2, 4.0, 3.0), (1, 0.04, 0.2, 4.0, 8.0), (1, 0.01, 0.2, 0.05, 14.0)]
    for idx, (grav, cs, qv, mv, kv) in enumerate(config):
        cv = 1.0
        bbeta = np.sqrt(qv)
        xx = kv * kv
        ccode = cv * 2 / float(DR_KINETIC_FACTOR)
        masscode = mv + float(DR_MASS_SHIFT) * ccode * qv
        aa = xx + masscode
        bb = cs * xx - float(DR_GRAVITY_SIGN) * grav * ccode
        O = np.array([[0, 0, 1, 0], [0, 0, 0, 1], [-aa, -float(DR_FORCE_SIGN) * ccode * bbeta, 0, 0], [-bbeta * xx, -bb, 0, 0]], float)
        init = np.array([1.0, -0.7, 0.11, -0.03]) * 1e-05
        ts = np.linspace(0, 3, 241)
        sol = solve_ivp(lambda t, z: O @ z, (ts[0], ts[-1]), init, t_eval=ts, method='DOP853', rtol=2e-13, atol=1e-18)
        direct = sol.y.T
        reference = np.array([expm(O * t) @ init for t in ts])
        err = float(np.max(abs(direct - reference)) / (1e-08 + np.max(abs(reference))))
        ck('ODE_matrix_exponential_' + str(idx), sol.success and err < 2e-08, dict(error=err, solver_message=sol.message))
        truea = xx + mv
        trueb = cs * xx - grav * cv
        freq = np.linalg.eigvalsh(np.array([[truea, bbeta * np.sqrt(cv * xx)], [bbeta * np.sqrt(cv * xx), trueb]]))
        predicted = np.array([(truea + trueb - np.sqrt((truea - trueb) ** 2 + 4 * cv * qv * xx)) / 2, (truea + trueb + np.sqrt((truea - trueb) ** 2 + 4 * cv * qv * xx)) / 2])
        ck('coupled_eigenfrequency_' + str(idx), np.max(abs(freq - predicted)) < 5e-13, dict(eigenvalues=freq.tolist(), formula=predicted.tolist()))
        ode_ev = np.linalg.eigvals(O)
        ck('ODE_dispersion_roots_' + str(idx), max((min((abs(-ev * ev - f) for ev in ode_ev)) for f in freq)) < 5e-11)
        if grav:
            xj = (cv * (1 + qv) - cs * mv + np.sqrt((cs * mv - cv * (1 + qv)) ** 2 + 4 * cs * cv * mv)) / (2 * cs)
            ck('Jeans_threshold_bracket_' + str(idx), cv / cs < xj < cv * (1 + qv) / cs, xj)
            ck('Jeans_threshold_classifies_mode_' + str(idx), bool(freq[0] > 0) == bool(xx > xj))
        else:
            xj = None
            ck('fixed_metric_threshold_classifies_mode_' + str(idx), bool(freq[0] > 0) == bool(cs * (xx + mv) > cv * qv))
        gamma_sq = max(0.0, -float(freq[0]))
        ceiling = cv * (1 + qv if grav else qv)
        ck('growth_rate_envelope_' + str(idx), gamma_sq < ceiling, dict(gamma_squared=gamma_sq, ceiling=ceiling))
        dd = np.sqrt(cv / xx) * direct[:, 1]
        ddot = np.sqrt(cv / xx) * direct[:, 3]
        terms = np.array([direct[:, 2] ** 2, ddot ** 2, truea * direct[:, 0] ** 2, trueb * dd ** 2, 2 * bbeta * np.sqrt(cv * xx) * direct[:, 0] * dd])
        en = terms.sum(axis=0)
        drift = float(np.max(abs(en - en[0])) / (1e-20 + np.max(abs(terms).sum(axis=0))))
        ck('numerical_conservative_energy_' + str(idx), drift < 3e-10, drift)
        path = out / ('profile_' + str(idx) + '.npz')
        assert not path.exists()
        np.savez_compressed(path, t=ts, state=direct, exact_reference=reference, canonical_energy=en, frequency_squared=freq, ode_matrix=O, initial_state=init)
        cases.append(dict(index=idx, gravity=grav, cs_squared=cs, q=qv, M_squared=mv, k=kv, cR=cv, profile=str(path.name), profile_sha256=hashlib.sha256(path.read_bytes()).hexdigest(), frequency_squared=freq.tolist(), Jeans_k_squared=xj, growth_squared=gamma_sq, ODE_error=err, energy_drift=drift))
    return dict(passed=sum((a['passed'] for a in checks)), failed=sum((not a['passed'] for a in checks)), checks=checks, synthetic_cases=cases, scope='Specified nonrelativistic local material and optional Newtonian patch only; no empirical fit or selected equilibrium/initial state.')

from pathlib import Path
import argparse, datetime, hashlib, json, math
import mpmath as mp
import numpy as np
import sympy as s
from scipy.special import roots_legendre
WI_IBP_SIGN = 1
WI_TIME_POWER = 2
WI_GRAVITY_SIGN = 1
WI_MASS_SHIFT = 0

def check_weak(out):
    out.mkdir(parents=True, exist_ok=False)
    mp.mp.dps = 65
    checks = []

    def ck(name, passed, detail=None):
        checks.append(dict(name=name, passed=bool(passed), detail=detail))

    def exact(name, expr):
        z = s.simplify(expr)
        ck(name, z == 0, str(z))

    def num(name, value, bound):
        ck(name, abs(value) < bound, dict(error=str(value), bound=str(bound)))
    x, m, c, q, v, h, z, T = s.symbols('x m c q v h z T', positive=True)
    beta = s.symbols('beta', positive=True)
    a = x + m
    b = v * x - h * c
    K = s.Matrix([[a, c * beta], [x * beta, b]])
    C2 = a + b
    C0 = a * b - c * q * x
    exact('coupled_characteristic', K.charpoly(z).as_expr().subs(K.charpoly(z).gen, z).subs(beta ** 2, q) - (z ** 2 - C2 * z + C0))
    for i, e in enumerate(K * K - C2 * K + (a * b - c * beta ** 2 * x) * s.eye(2)):
        exact('all_readout_eliminant_' + str(i), e)
    mm = C2 - (1 + v) * x + WI_GRAVITY_SIGN * h * c + WI_MASS_SHIFT * c * q
    qq = ((x + mm) * b - C0) / (c * x)
    exact('mass_inverse', mm - m)
    exact('coupling_inverse', qq - q)
    u2, u0 = s.symbols('u2 u0')
    exact('clock_power', T ** 2 * C2 / T ** WI_TIME_POWER - C2)
    tau = s.symbols('tau', real=True)
    P = tau ** 4 * (1 - tau) ** 4
    kernels = []
    bounds = []
    for j, w in enumerate([s.S.Zero, 8 * s.pi]):
        psi = P * s.cos(w * tau)
        for n in range(4):
            for end in [0, 1]:
                exact('kernel_boundary_%s_%s_%s' % (j, n, end), s.diff(psi, tau, n).subs(tau, end))
        funcs = {}
        nums = {}
        kb = {}
        for r in [0, 2, 4]:
            expr = s.diff(psi, tau, r)
            funcs[r] = s.lambdify(tau, expr, 'mpmath')
            nums[r] = s.lambdify(tau, expr, 'numpy')
            envelope = 0
            for ell in range(r + 1):
                poly = s.Poly(s.diff(P, tau, ell), tau)
                coeff_sum = sum((abs(coef) / s.Integer(power[0] + 1) for power, coef in poly.terms()))
                envelope += s.binomial(r, ell) * abs(w) ** (r - ell) * coeff_sum
            kb[r] = mp.mpf(str(s.N(envelope, 70)))
            ck('positive_kernel_bound_%s_%s' % (j, r), kb[r] > 0, str(envelope))
        kernels.append((funcs, nums))
        bounds.append(kb)
    C = mp.mpf(1)
    V = mp.mpf('.04')
    M = mp.mpf(4)
    Q = mp.mpf('.2')
    H = mp.mpf(1)
    duration = mp.mpf(3)
    amplitude = mp.mpf('1e-5')
    epsilon = mp.mpf('1e-17')

    def coeff(k, Mval=M, Qval=Q):
        xx = k * k
        aa = xx + Mval
        bb = V * xx - H * C
        return (aa + bb, aa * bb - C * Qval * xx)

    def make(k, A, B, phase, physical=False, single=False):
        xx = k * k
        aa = xx + M
        bb = V * xx - H * C
        disc = mp.sqrt((aa - bb) ** 2 + 4 * C * Q * xx)
        ys = [(aa + bb - disc) / 2, (aa + bb + disc) / 2]
        ck('synthetic_stable_k_' + str(k), all((y > 0 for y in ys)), [str(y) for y in ys])
        omg = [mp.sqrt(y) * duration for y in ys]
        mult = [1 + 3 * (bb - y) / xx if physical else mp.mpf(1) for y in ys]

        def f(t):
            return amplitude * (A * mult[0] * mp.cos(omg[0] * t + phase) + (0 if single else B * mult[1] * mp.sin(omg[1] * t + phase)))

        def fn(t, r=0):
            return float(amplitude) * (float(A * mult[0]) * float(omg[0]) ** r * np.cos(float(omg[0]) * t + float(phase) + r * np.pi / 2) + (0 if single else float(B * mult[1]) * float(omg[1]) ** r * np.sin(float(omg[1]) * t + float(phase) + r * np.pi / 2)))
        return (f, fn, ys, omg)
    grid = [mp.mpf(i) / 8 for i in range(9)]
    gx, gw = roots_legendre(256)
    gx = (gx + 1) / 2
    gw = gw / 2

    def features(f, fn, label):
        result = []
        double = []
        for j, (funcs, nums) in enumerate(kernels):
            row = {r: mp.quad(lambda t: f(t) * funcs[r](t), grid) for r in [0, 2, 4]}
            nr = {r: float(np.sum(gw * fn(gx, r) * nums[0](gx))) for r in [0, 2, 4]}
            for r in [0, 2, 4]:
                num(label + '.gauss_%s_%s' % (j, r), mp.mpf(nr[r]) - row[r], mp.mpf('3e-12') * max(mp.mpf('1e-12'), abs(row[r])))
            result.append(row)
            double.append(nr)
        return (result, double)

    def infer(rows, k):
        D = mp.matrix([[WI_IBP_SIGN * r[2], r[0]] for r in rows])
        zz = mp.matrix([-r[4] for r in rows])
        u = mp.lu_solve(D, zz)
        cc2 = u[0] / duration ** WI_TIME_POWER
        cc0 = u[1] / duration ** 4
        xx = k * k
        mass = cc2 - (1 + V) * xx + WI_GRAVITY_SIGN * H * C + WI_MASS_SHIFT * C * Q
        coupling = ((xx + mass) * (V * xx - H * C) - cc0) / (C * xx)
        return (D, u, mass, coupling)
    norm = lambda mat: max((sum((abs(mat[i, j]) for j in range(mat.cols))) for i in range(mat.rows)))
    cases = []
    inferred = []
    choices = [('1', '.7', '.2'), ('.3', '-.5', '.9'), ('2', '-1', '-.4')]
    for case, choice in enumerate(choices):
        k = mp.mpf(8)
        A, B, phase = map(mp.mpf, choice)
        f, fn, ys, omg = make(k, A, B, phase)
        rows, dr = features(f, fn, 'case' + str(case))
        D, u, mass, coupling = infer(rows, k)
        cc2, cc0 = coeff(k)
        for j, row in enumerate(rows):
            num('case%s.weak_equation_%s' % (case, j), row[4] + duration ** 2 * cc2 * row[2] + duration ** 4 * cc0 * row[0], mp.mpf('1e-55'))
        num('case%s.mass' % case, mass - M, mp.mpf('1e-48'))
        num('case%s.q' % case, coupling - Q, mp.mpf('1e-48'))
        ck('case%s.rank' % case, abs(mp.det(D)) > mp.mpf('1e-30'), str(mp.det(D)))
        fd = lambda t: f(t) + epsilon * mp.sin(13 * mp.pi * t)
        fdn = lambda t, r=0: fn(t, r) + float(epsilon) * (13 * np.pi) ** r * np.sin(13 * np.pi * t + r * np.pi / 2)
        nr, ndr = features(fd, fdn, 'noise' + str(case))
        Dh, uh, mh, qh = infer(nr, k)
        d = epsilon * max((bb[2] + bb[0] for bb in bounds))
        e = epsilon * max((bb[4] for bb in bounds))
        ni = norm(Dh ** (-1))
        eta = ni * d
        E = ni * (e + d * norm(uh)) / (1 - eta)
        ck('case%s.eta' % case, eta < 1, str(eta))
        ck('case%s.error_certificate' % case, norm(uh - u) <= E, dict(actual=str(norm(uh - u)), bound=str(E)))
        mb = E / duration ** 2
        qb = (abs(V * k * k - H * C) / duration ** 2 + 1 / duration ** 4) * E / (C * k * k)
        ck('case%s.mass_certificate' % case, abs(mh - M) <= mb, dict(actual=str(mh - M), bound=str(mb)))
        ck('case%s.q_certificate' % case, abs(qh - Q) <= qb, dict(actual=str(qh - Q), bound=str(qb)))
        ts = np.linspace(0, 1, 2049)
        np.savez_compressed(out / ('profile_%s.npz' % case), tau=ts, readout=fn(ts), noisy=fdn(ts))
        cases.append(dict(choice=choice, frequencies=[str(y) for y in ys], features=[{str(r): str(row[r]) for r in row} for row in rows], double_features=dr, noisy_features=[{str(r): str(row[r]) for r in row} for row in nr], D=[[str(D[i, j]) for j in range(2)] for i in range(2)], u=[str(vv) for vv in u], mass=str(mass), q=str(coupling), condition_inf=str(norm(D) * norm(D ** (-1))), eta=str(eta), coefficient_error_bound=str(E), mass_error_bound=str(mb), q_error_bound=str(qb)))
        inferred.append((mass, coupling))
    f, fn, ys, omg = make(mp.mpf(8), mp.mpf(1), mp.mpf('.7'), mp.mpf('.2'), physical=True)
    physical, physical_double = features(f, fn, 'physical_density')
    _, _, mphys, qphys = infer(physical, mp.mpf(8))
    num('physical_density.mass', mphys - M, mp.mpf('1e-48'))
    num('physical_density.q', qphys - Q, mp.mpf('1e-48'))
    f, fn, ys, omg = make(mp.mpf(8), mp.mpf(1), mp.mpf(0), mp.mpf('.2'), single=True)
    single, sd = features(f, fn, 'single_mode')
    DS = mp.matrix([[r[2], r[0]] for r in single])
    for j, row in enumerate(single):
        num('single_mode.dependency_' + str(j), row[2] + omg[0] ** 2 * row[0], mp.mpf('1e-55'))
    num('single_mode.relative_det', mp.det(DS) / norm(DS) ** 2, mp.mpf('1e-50'))
    k = mp.mpf(11)
    f, fn, ys, omg = make(k, mp.mpf('.6'), mp.mpf('-.8'), mp.mpf('.3'))
    validation, vd = features(f, fn, 'reserved')
    pred2, pred0 = coeff(k, *inferred[0])
    truth2, truth0 = coeff(k)
    num('reserved.C2', pred2 - truth2, mp.mpf('1e-48'))
    num('reserved.C0', pred0 - truth0, mp.mpf('1e-45'))
    for j, row in enumerate(validation):
        num('reserved.weak_residual_' + str(j), row[4] + duration ** 2 * pred2 * row[2] + duration ** 4 * pred0 * row[0], mp.mpf('1e-50'))
    ts = np.linspace(0, 1, 2049)
    np.savez_compressed(out / 'reserved_profile.npz', tau=ts, readout=fn(ts))
    result = dict(passed=sum((r['passed'] for r in checks)), failed=sum((not r['passed'] for r in checks)), checks=checks, cases=cases, kernel_bounds=[{str(k): str(v) for k, v in b.items()} for b in bounds], physical_density_inverse=dict(mass=str(mphys), q=str(qphys)), single_mode_relative_det=str(mp.det(DS) / norm(DS) ** 2), reserved=dict(k='11', predicted_C2=str(pred2), predicted_C0=str(pred0), features=[{str(r): str(row[r]) for r in row} for row in validation]), scope='Synthetic protocol; exact calibrated constant model. Error bound does not certify floating quadrature or an experiment.', checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (out / 'RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(passed=result['passed'], failed=result['failed'], cases=[{k: v for k, v in row.items() if k in ['mass', 'q', 'condition_inf', 'eta', 'mass_error_bound', 'q_error_bound']} for row in cases]), indent=2))
    return result['failed']

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--profiles',type=Path)
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    def execute(root):
        root.mkdir(parents=True,exist_ok=True)
        dynamics=check_dynamics(root/'dynamics')
        captured=io.StringIO()
        with redirect_stdout(captured):
            failed=check_weak(root/'weak_inverse')
        weak=json.loads((root/'weak_inverse'/'RESULTS.json').read_text())
        assert failed==weak['failed']
        result=dict(passed=dynamics['passed']+weak['passed'],failed=dynamics['failed']+weak['failed'],units=dict(dynamics=dynamics,weak_inverse=weak),weak_execution_stdout=captured.getvalue(),checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Exact specified local quadratic model and calibrated finite-window inverse; no real-data fit or state/action selection.')
        return result
    if args.profiles is None:
        with TemporaryDirectory(prefix='scalar-density-inverse-') as d:result=execute(Path(d))
    else:
        assert not args.profiles.exists();result=execute(args.profiles)
    text=json.dumps(result,indent=2)+'\n'
    if args.out:
        assert not args.out.exists();args.out.write_text(text)
    print(text,end='')
    return bool(result['failed'])
if __name__=='__main__':raise SystemExit(main())
