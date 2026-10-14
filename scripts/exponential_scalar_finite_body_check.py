#!/usr/local/bin/python3
"""Conditional finite held-body bounds, uniqueness and scalar-only stability."""
from contextlib import redirect_stdout
from tempfile import TemporaryDirectory
import io
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['docs/EXPONENTIAL_SCALAR_FINITE_BODY_BOUNDED_THEOREM_NOTE_2026-10-14.md', 'docs/EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md', 'docs/EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md', 'docs/EXPONENTIAL_SCALAR_ENVIRONMENT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-10-14.md']
from pathlib import Path
import argparse, json, hashlib, itertools
import numpy as np
import sympy as S
from scipy.integrate import solve_bvp, quad, cumulative_simpson
from scipy.optimize import brentq
FB_COMPARISON_SIGN = 1
FB_KINETIC_FACTOR = 2
FB_BOOTSTRAP_SIGN = -1

def check_excursion(out, algebra_only=False):
    out.mkdir(parents=True, exist_ok=False)
    rows = []
    cases = []

    def ck(n, b, detail=None):
        rows.append(dict(name=n, passed=bool(b), detail=detail))

    def eq(n, e):
        v = S.factor(S.cancel(e))
        ck(n, v == 0, str(v))
    k, E, z, u, nu = S.symbols('k E z u nu', positive=True)
    a = (1 - k) * (1 + 3 * k) / 4
    alpha = S.sqrt(a)
    s = (1 + k) / (k * (1 - 3 * k))
    F = 1 + s * E
    J = 1 + (1 - 3 * a) * s * E
    K = J / F ** 2
    A = S.sqrt((1 + s) * E / F)
    q = a / J
    beta_chi = S.factor(2 * alpha * E * S.diff(S.sqrt(q), E) / S.sqrt(K))
    beta_chi_rational = -a * (1 - 3 * a) * s * E * F / J ** 2
    eq('canonical_beta_derivative_squared', beta_chi ** 2 - beta_chi_rational ** 2)
    eq('vacuum_beta_derivative', beta_chi_rational.subs(E, 1) + (1 + k))
    D = 1 + s - s * z * z
    qz = a * D / (1 + s - 3 * a * s * z * z)
    eq('canonical_beta_derivative_A', z * S.diff(qz, z) / 2 + (1 + k) * z * z * (1 - 3 * qz) ** 2 / (1 - 3 * k) ** 2)
    eq('original_E_to_A_derivative', beta_chi_rational.subs(E, z * z / D) - z * S.diff(qz, z) / 2)
    phi, L, beta0, W = S.symbols('P L beta0 W', positive=True)
    wb = FB_COMPARISON_SIGN * beta0 * phi / (1 + FB_BOOTSTRAP_SIGN * L * phi)
    eq('bootstrap_supremum_solution', wb - beta0 * phi - L * phi * wb)
    eq('integrated_coupling_bound', beta0 * wb + L * wb ** 2 / 2 - beta0 ** 2 * phi * (1 - L * phi / 2) / (1 - L * phi) ** 2)
    eq('rest_source_normalization', S.Rational(1, FB_KINETIC_FACTOR) - S.Rational(1, 2))
    radius, rho, Q, r = S.symbols('R rho Q r', positive=True)
    G = 1 / (8 * S.pi * Q)
    mass = 4 * S.pi * rho * radius ** 3 / 3
    surf = G * mass / radius
    potential = rho / (FB_KINETIC_FACTOR * Q) * (3 * radius ** 2 - r * r) / 6
    eq('sphere_center_potential', potential.subs(r, 0) - 3 * surf / 2)
    eq('sphere_surface_potential', potential.subs(r, radius) - surf)
    eq('sphere_poisson', -(S.diff(potential, r, 2) + 2 * S.diff(potential, r) / r) - rho / (2 * Q))
    ck('comparison_positive_witness', wb.subs({beta0: 1, phi: S.Rational(1, 10), L: 1}) > 0)
    eu = S.exp(2 * alpha * u)
    fu = 1 + s * eu
    ju = 1 + (1 - 3 * a) * s * eu
    ku = ju / fu ** 2
    au = S.sqrt((1 + s) * eu / fu)
    U = S.Rational(3, 2) + S.Rational(3, 2) * s * (eu - 1) ** 2 / fu ** 2 + nu * (1 + s) * u * u / (2 * fu ** 2)
    Up = S.diff(U, u)
    Upp = S.diff(U, u, 2)
    Ap = S.diff(au, u)
    Kp = S.diff(ku, u)
    vacratio = 4 * (3 + 3 * k + nu) / (1 - 3 * k)
    eq('vacuum_mass_normalization', Upp.subs(u, 0) / ku.subs(u, 0) - vacratio)
    expected_up = 6 * alpha * s * (1 + s) * eu * (eu - 1) / fu ** 3 + nu * (1 + s) * u * (1 - 2 * alpha * u * s * eu / fu) / fu ** 2
    eq('negative_branch_potential_sign_decomposition', Up - expected_up)
    for kv in [S.Rational(1, 100), S.Rational(1, 10), S.Rational(3, 10)]:
        for ev in [S.Rational(1, 1000), S.Rational(1, 10), S.Integer(1)]:
            bv = S.factor(beta_chi_rational.subs({k: kv, E: ev}))
            qv = q.subs({k: kv, E: ev})
            ck('lipschitz_' + str(kv) + '_' + str(ev), 0 <= -bv <= 1 + kv, str(bv))
            ck('coupling_branch_' + str(kv) + '_' + str(ev), kv <= qv < a.subs(k, kv))
        for uv in [-20.0, -1.0, -0.01]:
            vv = float(Up.subs({k: kv, u: uv, nu: S.Rational(1, 10000)}))
            ck('potential_opposes_shift_' + str(kv) + '_' + str(uv), vv < 0, vv)
    if not algebra_only:
        for index, (kv, compact, muv) in enumerate(itertools.product([0.01, 0.1, 0.3], [0.0001, 0.01], [0.1, 1.0, 10.0])):
            nv = 0.0001
            sub = {k: kv, nu: nv}
            fun = S.lambdify(u, [ku.subs(sub), Kp.subs(sub), au.subs(sub), Ap.subs(sub), Up.subs(sub)], 'numpy')
            K0 = float(ku.subs({**sub, u: 0}))
            beta_v = np.sqrt(kv)
            mratio = float(vacratio.subs(sub))
            hv2 = muv * muv / mratio
            c0 = 3 * compact * (2 / FB_KINETIC_FACTOR)
            boundP = 1.5 * compact
            Lv = 1 + kv
            wbound = FB_COMPARISON_SIGN * beta_v * boundP / (1 + FB_BOOTSTRAP_SIGN * Lv * boundP)
            lnbound = kv * boundP * (1 - Lv * boundP / 2) / (1 - Lv * boundP) ** 2

            def linear(rs, inside):
                v = muv * rs
                pref = beta_v * c0 / muv ** 2
                if inside:
                    sh = np.ones_like(v)
                    dsh = np.zeros_like(v)
                    mask = v != 0
                    sh[mask] = np.sinh(v[mask]) / v[mask]
                    dsh[mask] = muv * (v[mask] * np.cosh(v[mask]) - np.sinh(v[mask])) / v[mask] ** 2
                    ch = -pref * (1 - (1 + muv) * np.exp(-muv) * sh)
                    cp = pref * (1 + muv) * np.exp(-muv) * dsh
                else:
                    ch = -pref * (muv * np.cosh(muv) - np.sinh(muv)) * np.exp(-v) / v
                    cp = -ch * (muv + 1 / rs)
                return (ch, cp)

            def solve(domain):
                span = domain - 1
                scale = max(abs(float(linear(np.array([0.0]), True)[0][0] / np.sqrt(K0))), 1e-30)

                def rhs(t, y):
                    y = scale * y
                    ki, kpi, ai, api, upi = fun(y[0])
                    ko, kpo, ao, apo, upo = fun(y[2])
                    re = 1 + span * t
                    return np.vstack([y[1], (hv2 * upi + c0 * api) / ki - kpi * y[1] ** 2 / (2 * ki), span * y[3], span * (hv2 * upo / ko - kpo * y[3] ** 2 / (2 * ko) - 2 * y[3] / re)]) / scale

                def bc(ya, yb):
                    return np.array([ya[1], yb[2], yb[0] - ya[2], yb[1] - ya[3]])
                ts = np.linspace(0, 1, 301)
                ci, di = linear(ts, True)
                co, do = linear(1 + span * ts, False)
                guess = np.array([ci, di, co, do]) / np.sqrt(K0) / scale
                sing = np.zeros((4, 4))
                sing[1, 1] = -2
                sol = solve_bvp(rhs, bc, ts, guess, S=sing, tol=1e-08, max_nodes=20000)
                evaluator = sol.sol
                sol.sol = lambda t: scale * evaluator(t)
                sol.y = scale * sol.y
                sol.physical_field_scale = scale
                return (sol, bc, span)
            domain = max(10.0, 12 / muv)
            sol, bc, span = solve(domain)
            ref, bc2, span2 = solve(1.5 * domain)
            ck('bvp_success_' + str(index), sol.success and ref.success, dict(first=sol.message, refined=ref.message, nodes=[len(sol.x), len(ref.x)], physical_field_scales=[sol.physical_field_scale, ref.physical_field_scale]))
            ck('boundary_residual_' + str(index), float(np.max(np.abs(bc(sol.y[:, 0], sol.y[:, -1])))) < 1e-08)
            ck('collocation_residual_' + str(index), float(np.max(sol.rms_residuals)) < 1e-07, float(np.max(sol.rms_residuals)))
            ri = np.linspace(0, 1, 1001)
            ro = np.geomspace(1, domain, 2001)
            yi = sol.sol(ri)
            yo = sol.sol((ro - 1) / span)
            us = np.r_[yi[0], yo[2, 1:]]
            ups = np.r_[yi[1], yo[3, 1:]]
            rs = np.r_[ri, ro[1:]]
            ch = np.array([quad(lambda v: np.sqrt(float(fun(v)[0])), 0, float(uv), epsabs=1e-14, epsrel=1e-11)[0] for uv in us])
            kap, kapp, aval, apval, upval = fun(us)
            bv = apval / (aval * np.sqrt(kap))
            w = -ch
            ck('negative_solution_' + str(index), float(np.max(us)) < 2e-08, float(np.max(us)))
            ck('global_compactness_bound_' + str(index), float(np.max(w)) <= wbound + 2e-08, dict(max_w=float(np.max(w)), bound=wbound))
            qbound = kv / (1 - Lv * boundP) ** 2
            ck('q_bootstrap_bound_' + str(index), float(np.max(bv * bv)) <= qbound + 2e-08, dict(max_q=float(np.max(bv * bv)), bound=qbound))
            ck('conformal_bound_' + str(index), float(np.max(-np.log(aval))) <= lnbound + 2e-08, dict(max_deficit=float(np.max(-np.log(aval))), bound=lnbound))
            vi = c0 * (3 - ri * ri) / 6
            vo = c0 / (3 * ro)
            V = np.r_[vi, vo[1:]]
            ck('pointwise_comparison_' + str(index), float(np.max(w - np.sqrt((1 - kv) * (1 + 3 * kv) / 4) * V)) < 2e-08)
            ki, kpi, ai, api, upi = fun(yi[0])
            ko, kpo, ao, apo, upo = fun(yo[2])
            fi = ri ** 2 * (hv2 * upi + c0 * api) / np.sqrt(ki)
            fo = ro ** 2 * hv2 * upo / np.sqrt(ko)
            int_i = cumulative_simpson(fi, x=ri, initial=0)
            int_o = int_i[-1] + cumulative_simpson(fo, x=ro, initial=0)
            flux = rs ** 2 * np.sqrt(kap) * ups
            integral = np.r_[int_i, int_o[1:]]
            ferr = float(np.max(np.abs(flux - integral)) / (beta_v * c0 / 3))
            ck('independent_flux_residual_' + str(index), ferr < 1e-07, ferr)
            yir = ref.sol(ri)
            yor = ref.sol((ro - 1) / span2)
            uref = np.r_[yir[0], yor[2, 1:]]
            domainerr = float(np.max(np.abs(us - uref)) / (1e-20 + np.max(np.abs(uref))))
            ck('domain_refinement_' + str(index), domainerr < 1e-05, domainerr)

            def stationary(uv):
                kk, kp, aa, app, upp = fun(uv)
                return hv2 * upp + c0 * app
            grid = -np.geomspace(1000.0, 1e-10, 2001)
            roots = []
            for left, right in zip(grid[:-1], grid[1:]):
                if stationary(left) * stationary(right) < 0:
                    root = brentq(stationary, left, right, xtol=1e-13)
                    disp = -quad(lambda v: np.sqrt(float(fun(v)[0])), 0, root, epsabs=1e-12)[0]
                    roots.append(dict(u=root, canonical_displacement=disp, violates_necessary_body_bound=bool(disp > wbound + 2e-08)))
            filename = 'profile_' + str(index) + '.npz'
            np.savez_compressed(out / filename, r=rs, u=us, du=ups, chi=ch, A=aval, beta=bv, flux=flux, integral_flux=integral, refined_u=uref, Newton_magnitude=V)
            cases.append(dict(index=index, k=kv, nu=nv, Phi_surface=compact, mu_vac_R=muv, Hv_R_squared=hv2, cR=c0, domain=domain, central_u=float(us[0]), central_w=float(w[0]), max_q=float(np.max(bv * bv)), w_bound=wbound, lnA_bound=lnbound, flux_relative_error=ferr, domain_relative_error=domainerr, sampled_stationary_roots=roots, root_search_scope='Sign brackets on specified finite grid only; not exhaustive', profile=filename, profile_sha256=hashlib.sha256((out / filename).read_bytes()).hexdigest()))
    result = dict(passed=sum((x['passed'] for x in rows)), failed=sum((not x['passed'] for x in rows)), checks=rows, cases=cases, algebra_only=algebra_only, checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), scope='Conditional flat held-particle body with vacuum boundary; synthetic discretization checks, not a measured environment or global GR solution.')
    (out / 'RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(passed=result['passed'], failed=result['failed'], cases=len(cases), failed_checks=[x for x in rows if not x['passed']]), indent=2))
    return result['failed']

from pathlib import Path
import argparse, json, hashlib
import numpy as np
import sympy as S
SF_SPHERE_COEFFICIENT = S.Rational(2, 5)
SF_ENVELOPE_COEFFICIENT = 12
SF_HESSIAN_CONNECTION_SIGN = -1

def check_surface(source, out, algebra_only=False):
    out.mkdir(parents=True, exist_ok=False)
    rows = []
    cases = []
    bindings = []

    def ck(name, passed, detail=None):
        rows.append(dict(name=name, passed=bool(passed), detail=detail))

    def eq(name, expression):
        value = S.factor(S.cancel(expression))
        ck(name, value == 0, str(value))
    a, s, E, u, nu, Hv2 = S.symbols('a s E u nu Hv2', positive=True)
    alpha = S.sqrt(a)
    F = 1 + s * E
    J = 1 + (1 - 3 * a) * s * E
    K = J / F ** 2
    derivative = lambda f: S.diff(f, u) + 2 * alpha * E * S.diff(f, E)
    Ubase = S.Rational(3, 2) + S.Rational(3, 2) * s * (E - 1) ** 2 / F ** 2
    Ureg = nu * (1 + s) * u ** 2 / (2 * F ** 2)
    U = Ubase + Ureg
    Up = derivative(U)
    Upp = derivative(Up)
    Kp = derivative(K)
    base_second = 12 * a * s * (1 + s) * E * (2 * E - 1 + s * E * (2 - E)) / F ** 4
    reg_second = nu * (1 + s) * (1 / F ** 2 - 8 * alpha * s * E * u / F ** 3 - 4 * a * s * E * u ** 2 / F ** 3 + 12 * a * s * s * E * E * u * u / F ** 4)
    eq('base_second_derivative', derivative(derivative(Ubase)) - base_second)
    eq('regulator_second_derivative', derivative(derivative(Ureg)) - reg_second)
    eq('kinetic_monotonicity', S.diff(K, E) + s * (1 + 3 * a + (1 - 3 * a) * s * E) / F ** 3)
    exact_hessian = derivative(Up / S.sqrt(K)) / S.sqrt(K)
    hessian = Upp / K + SF_HESSIAN_CONNECTION_SIGN * Kp * Up / (2 * K * K)
    eq('canonical_connection_normalization', exact_hessian - hessian)
    R, r, c = S.symbols('R r c', positive=True)
    V = c * (3 * R * R - r * r) / 6
    eq('sphere_source_integral', S.integrate(r * r * V, (r, 0, R)) / (c * R ** 3 / 3) - SF_SPHERE_COEFFICIENT * R ** 2)
    Umax, Fmin, K0 = S.symbols('Umax Fmin K0', positive=True)
    envelope = Hv2 / K0 * (SF_ENVELOPE_COEFFICIENT * a * s * (1 + s) ** 2 / Fmin ** 4 + nu * (1 + s) * (1 / Fmin ** 2 + 8 * alpha * s * Umax / Fmin ** 3 + 12 * a * s * s * Umax ** 2 / Fmin ** 4))
    eq('vacuum_envelope_equals_actual_mass', envelope.subs({Umax: 0, Fmin: 1 + s, K0: K.subs(E, 1)}) - Hv2 * exact_hessian.subs({E: 1, u: 0}))
    ck('surface_flux_attraction_sign', SF_SPHERE_COEFFICIENT > 0)
    k = S.symbols('k', positive=True)
    ak = (1 - k) * (1 + 3 * k) / 4
    sk = (1 + k) / (k * (1 - 3 * k))
    eq('candidate_vacuum_mass', exact_hessian.subs({E: 1, u: 0, a: ak, s: sk}) - 4 * (3 + 3 * k + nu) / (1 - 3 * k))
    if not algebra_only:
        src = source / 'RESULTS.json'
        data = json.loads(src.read_text())
        bindings.append(dict(path=str(src), sha256=hashlib.sha256(src.read_bytes()).hexdigest()))
        ck('source_result_no_failed_checks', data['failed'] == 0)
        ck('source_case_count', len(data['cases']) == 18)
        for case in data['cases']:
            idx = case['index']
            path = source / case['profile']
            sha = hashlib.sha256(path.read_bytes()).hexdigest()
            ck('profile_identity_' + str(idx), sha == case['profile_sha256'])
            bindings.append(dict(path=str(path), sha256=sha))
            with np.load(path, allow_pickle=False) as zz:
                p = {n: zz[n] for n in zz.files}
            kv = case['k']
            av = float(ak.subs(k, kv))
            sv = float(sk.subs(k, kv))
            nv = case['nu']
            hv = case['Hv_R_squared']
            subs = {a: av, s: sv, nu: nv}
            kval0 = float(K.subs({**subs, E: 1}))
            L = 1 + kv
            P = 1.5 * case['Phi_surface']
            wb = np.sqrt(kv) * P / (1 - L * P)
            umax = wb / np.sqrt(kval0)
            emin = np.exp(-2 * np.sqrt(av) * umax)
            fmin = 1 + sv * emin
            B = kv * P * (1 - L * P / 2) / (1 - L * P) ** 2
            mbar = float(envelope.subs({**subs, Hv2: hv, K0: kval0, Umax: umax, Fmin: fmin}))
            lower = max(0.0, kv * np.exp(-B) - float(SF_SPHERE_COEFFICIENT) * kv * mbar / (1 - L * P))
            upper = kv / (1 - L * P) ** 2
            hits = np.where(p['r'] == 1.0)[0]
            ck('unique_surface_point_' + str(idx), len(hits) == 1)
            j = int(hits[0])
            eta = float(p['beta'][j] * p['flux'][j] / case['Phi_surface'])
            ck('surface_lower_' + str(idx), eta >= lower - 2e-08, dict(eta=eta, lower=lower))
            ck('surface_upper_' + str(idx), eta <= upper + 2e-08, dict(eta=eta, upper=upper))
            grid = np.linspace(-umax, 0, 1001)
            hfun = S.lambdify(u, (hv * hessian).subs(subs).subs(E, S.exp(2 * np.sqrt(av) * u)), 'numpy')
            Hess = np.asarray(hfun(grid))
            peak = float(np.max(Hess))
            ck('sampled_hessian_envelope_' + str(idx), peak <= mbar * (1 + 2e-08), dict(maximum=peak, envelope=mbar))
            Kfun = S.lambdify(u, K.subs(subs).subs(E, S.exp(2 * np.sqrt(av) * u)), 'numpy')
            ck('kinetic_lower_bound_' + str(idx), float(np.min(Kfun(grid))) >= kval0 * (1 - 2e-08))
            ck('pointwise_bootstrap_' + str(idx), float(np.max(-p['chi'] - np.sqrt(kv) * p['Newton_magnitude'] / (1 - L * P))) <= 2e-08)
            forces = p['beta'][j:] * p['flux'][j:] / case['Phi_surface']
            ck('exterior_nonnegative_' + str(idx), float(np.min(forces)) >= -2e-08)
            ck('exterior_nonincreasing_' + str(idx), float(np.max(np.diff(forces))) <= 2e-08)
            rec = dict(index=idx, k=kv, Phi_surface=case['Phi_surface'], mu_vac_R=case['mu_vac_R'], P=P, Umax=umax, Mbar_R_squared=mbar, surface_eta=eta, lower=lower, upper=upper, lower_informative=bool(lower > 0), profile_sha256=sha, hessian_sample_peak=peak)
            cases.append(rec)
            np.savez_compressed(out / ('hessian_' + str(idx) + '.npz'), u=grid, Y_chichi=Hess, Mbar_squared=mbar)
    result = dict(passed=sum((x['passed'] for x in rows)), failed=sum((not x['passed'] for x in rows)), checks=rows, cases=cases, source_bindings=bindings, algebra_only=algebra_only, checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), scope='Exact conditional radial flat held-source force bound; profile checks reuse exposed synthetic cases, not independent observed tests. Numerical Hessian samples do not prove a supremum.')
    (out / 'RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(passed=result['passed'], failed=result['failed'], cases=len(cases), informative_lower_bounds=sum((x['lower_informative'] for x in cases)), failed_checks=[x for x in rows if not x['passed']]), indent=2))
    return result['failed']

from pathlib import Path
import argparse, json, hashlib
import sympy as S
import numpy as np
import mpmath as mp
UN_CONNECTION_SIGN = -1
UN_KATO_SIGN = 1
UN_DENOMINATOR_SIGN = -1
UN_GROUND_SIGN = -1

def check_uniqueness(source, out, algebra_only=False):
    out.mkdir(parents=True, exist_ok=False)
    rows = []
    cases = []
    bindings = []

    def ck(n, b, d=None):
        rows.append(dict(name=n, passed=bool(b), detail=d))

    def eq(n, e):
        v = S.factor(S.cancel(e))
        ck(n, v == 0, str(v))
    a, s, E, u, nu = S.symbols('a s E u nu', positive=True)
    alpha = S.sqrt(a)
    b = 1 - 3 * a
    F = 1 + s * E
    J = 1 + b * s * E
    K = J / F ** 2
    D = lambda f: S.diff(f, u) + 2 * alpha * E * S.diff(f, E)
    hessian = lambda f: D(D(f)) / K + UN_CONNECTION_SIGN * D(K) * D(f) / (2 * K * K)
    ub = S.Rational(3, 2) + S.Rational(3, 2) * s * (E - 1) ** 2 / F ** 2
    g = u / F
    ur = nu * (1 + s) * g * g / 2
    hb = 6 * a * s * (1 + s) * E * (2 * J * (2 * E - 1 + s * E) - b * s * E * (E - 1) * F) / (F * F * J * J)
    gp = (1 - 2 * alpha * s * E * u / F) / S.sqrt(J)
    gpp = -2 * alpha * s * E / J * (1 + 2 * alpha * u / F) - alpha * b * s * E * F / (J * J) * (1 - 2 * alpha * s * E * u / F)
    eq('base_hessian_factorization', hessian(ub) - hb)
    eq('regulator_g_first_squared', D(g) ** 2 / K - gp ** 2)
    eq('regulator_g_second', hessian(g) - gpp)
    eq('regulator_hessian_factorization', hessian(ur) - nu * (1 + s) * (gp * gp + g * gpp))
    L, P, R, Beta = S.symbols('L P R Beta', positive=True)
    bound = Beta * R / (1 + UN_DENOMINATOR_SIGN * L * P)
    eq('difference_source_contraction', bound - (Beta * R + UN_KATO_SIGN * L * P * bound))
    ck('kato_upper_sign', UN_KATO_SIGN > 0)
    vv, cv, grad2 = S.symbols('V c grad2', positive=True)
    laplog = -cv / vv - grad2 / vv ** 2
    eq('ground_state_integration_by_parts', grad2 / vv ** 2 + laplog - UN_GROUND_SIGN * cv / vv)
    eq('quadratic_form_gradient_coefficient', 1 + UN_DENOMINATOR_SIGN * L * P - (1 - L * P))
    k = S.symbols('k', positive=True)
    ak = (1 - k) * (1 + 3 * k) / 4
    sk = (1 + k) / (k * (1 - 3 * k))
    beta = S.sqrt(a / J)
    beta_chi = -a * b * s * E * F / J ** 2
    AA = S.sqrt((1 + s) * E / F)
    matter = AA * (a / J + beta_chi)
    for kv in [S.Rational(1, 100), S.Rational(1, 10), S.Rational(3, 10)]:
        for ev in [S.Rational(1, 2), S.Rational(3, 5), S.Rational(9, 10), S.Integer(1)]:
            av = ak.subs(k, kv)
            sv = sk.subs(k, kv)
            uv = S.log(ev) / (2 * S.sqrt(av))
            sub = {a: av, s: sv, E: ev, u: uv, nu: S.Rational(1, 10000)}
            tag = str(kv) + '_' + str(ev)
            h1 = float(hb.subs(sub))
            h2 = float((nu * (1 + s) * (gp * gp + g * gpp)).subs(sub))
            ck('base_convex_' + tag, h1 > 0, h1)
            ck('regulator_convex_' + tag, h2 > 0, h2)
            ck('regulator_gpp_' + tag, float(gpp.subs(sub)) < 0)
            ck('matter_one_sided_' + tag, float(matter.subs(sub)) >= -float(1 + kv))
    if not algebra_only:
        mp.mp.dps = 65
        for slope in [mp.mpf('0.1'), mp.mpf('1'), mp.mpf('10')]:
            f = lambda r: mp.exp(-slope * r * r)
            df = lambda r: -2 * slope * r * f(r)
            V = lambda r: (3 - r * r) / 6 if r <= 1 else 1 / (3 * r)
            Vp = lambda r: -r / 3 if r <= 1 else -1 / (3 * r * r)
            left = mp.quad(lambda r: r * r * (df(r) - f(r) * Vp(r) / V(r)) ** 2, [0, 1, mp.inf])
            grad = mp.quad(lambda r: r * r * df(r) ** 2, [0, 1, mp.inf])
            weighted = mp.quad(lambda r: r * r * f(r) ** 2 / V(r), [0, 1])
            mass = mp.quad(lambda r: r * r * f(r) ** 2, [0, 1])
            Pval = mp.mpf('.5')
            err = abs(left - (grad + UN_GROUND_SIGN * weighted))
            ck('radial_ground_identity_' + str(slope), err < mp.mpf('1e-55'), str(err))
            ck('radial_source_form_bound_' + str(slope), mass <= Pval * grad)
        src = source / 'RESULTS.json'
        data = json.loads(src.read_text())
        bindings.append(dict(path=str(src), sha256=hashlib.sha256(src.read_bytes()).hexdigest()))
        for row in data['cases']:
            kv = row['k']
            av = float(ak.subs(k, kv))
            sv = float(sk.subs(k, kv))
            sub = {a: av, s: sv, nu: row['nu']}
            K0 = float(K.subs({**sub, E: 1}))
            Pval = 1.5 * row['Phi_surface']
            LP = (1 + kv) * Pval
            umax = np.sqrt(kv) * Pval / (1 - LP) / np.sqrt(K0)
            criterion = 2 * np.sqrt(av) * umax
            ok = bool(LP < 1 and criterion <= np.log(2))
            ck('recorded_body_meets_uniqueness_' + str(row['index']), ok, dict(LP=LP, criterion=criterion, ceiling=float(np.log(2))))
            grid = np.linspace(-umax, 0, 1001)
            fun = S.lambdify(u, hessian(ub + ur).subs(sub).subs(E, S.exp(2 * np.sqrt(av) * u)), 'numpy')
            hv = row['Hv_R_squared']
            ys = hv * fun(grid)
            minimum = float(np.min(ys))
            ck('sampled_positive_hessian_' + str(row['index']), minimum > 0, minimum)
            np.savez_compressed(out / ('convexity_' + str(row['index']) + '.npz'), u=grid, Y_chichi=ys)
            cases.append(dict(index=row['index'], k=kv, P=Pval, LP=LP, twice_alpha_Umax=criterion, criterion_met=ok, sampled_hessian_minimum=minimum, interpretation='Sample supplements the analytic proof; it is not a certified global eigenvalue or numerical minimum.'))
    result = dict(passed=sum((r['passed'] for r in rows)), failed=sum((not r['passed'] for r in rows)), checks=rows, cases=cases, source_bindings=bindings, algebra_only=algebra_only, checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), scope='Conditional unique negative static held-source solution and scalar-only linear stability; no matter/metric stability or settling.')
    (out / 'RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(passed=result['passed'], failed=result['failed'], cases=len(cases), failed_checks=[r for r in rows if not r['passed']]), indent=2))
    return result['failed']

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--profiles',type=Path);parser.add_argument('--out',type=Path);args=parser.parse_args()
    def execute(root):
        root.mkdir(parents=True,exist_ok=True);units={};streams={}
        for name,fn in [('excursion',check_excursion),('surface',check_surface),('uniqueness',check_uniqueness)]:
            captured=io.StringIO()
            with redirect_stdout(captured):
                if name=='excursion':failed=fn(root/name)
                else:failed=fn(root/'excursion',root/name)
            result=json.loads((root/name/'RESULTS.json').read_text())
            assert failed==result['failed'];units[name]=result;streams[name]=captured.getvalue()
        return dict(passed=sum(z['passed'] for z in units.values()),failed=sum(z['failed'] for z in units.values()),units=units,unit_stdout=streams,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Conditional flat static held-source model, derived force bracket and scalar-only stability. No observed fit, full-metric solution or realized-state selector.')
    if args.profiles is None:
        with TemporaryDirectory(prefix='scalar-finite-body-') as d:result=execute(Path(d))
    else:
        assert not args.profiles.exists();result=execute(args.profiles)
    text=json.dumps(result,indent=2)+'\n'
    if args.out:
        assert not args.out.exists();args.out.write_text(text)
    print(text,end='');return bool(result['failed'])
if __name__=='__main__':raise SystemExit(main())
