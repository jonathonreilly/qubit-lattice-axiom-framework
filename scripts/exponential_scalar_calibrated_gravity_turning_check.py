#!/usr/local/bin/python3
"""Ideal force-calibrated scalar gravity: turning point and inverse limits."""
from contextlib import redirect_stdout
from tempfile import TemporaryDirectory
import io
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['docs/EXPONENTIAL_SCALAR_CALIBRATED_GRAVITY_TURNING_BOUNDED_THEOREM_NOTE_2026-10-14.md', 'docs/EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md', 'docs/EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md']
from pathlib import Path
import argparse, hashlib, json
import sympy as S
import mpmath as mp
SCALAR_FORCE_FACTOR = 1
DEFICIT_FACTOR = 4
CANONICAL_FACTOR = 1
ACCEPT_ALL_ROOTS = False

def check_turning(out):
    out.mkdir(parents=True, exist_ok=False)
    checks = []
    cases = []
    near = []
    windows = []

    def ck(name, passed, detail=None):
        checks.append(dict(name=name, passed=bool(passed), detail=detail))

    def eq(name, x):
        v = S.factor(S.cancel(x))
        ck(name, v == 0, str(v))
    k, q, E = S.symbols('k q E', positive=True)
    a = (1 - k) * (1 + 3 * k) / 4
    s = (1 + k) / (k * (1 - 3 * k))
    F = 1 + s * E
    J = 1 + (1 - 3 * a) * s * E
    K = J / F ** 2
    qq = a / J
    AA = (1 + s) * E / F
    inverseA = 4 * (a - q) / ((1 + k) * (1 - 3 * q))
    eq('conformal_elimination', inverseA.subs(q, qq) - AA)
    force = AA * (1 + SCALAR_FORCE_FACTOR * qq) / (1 + k)
    deficit = 1 - DEFICIT_FACTOR * (q - k) ** 2 / ((1 + k) ** 2 * (1 - 3 * q))
    eq('calibrated_square_deficit', force - deficit.subs(q, qq))
    eq('vacuum_calibrated_reference', force.subs(E, 1) - 1)
    beta = S.sqrt(a / J)
    dd = a * (1 - 3 * a) * s * E * F / J ** 2
    Du = lambda f: 2 * S.sqrt(a) * E * S.diff(f, E)
    logDu = S.factor(Du(force) / force)
    canonical_formula = 2 * beta * (1 - dd / (1 + qq))
    eq('canonical_log_derivative_squared', (CANONICAL_FACTOR * logDu) ** 2 / K - canonical_formula ** 2)
    eq('vacuum_first_derivative', logDu.subs(E, 1))
    eq('vacuum_beta_derivative', dd.subs(E, 1) - (1 + k))
    logD2 = Du(logDu) / K - Du(K) * logDu / (2 * K * K)
    eq('vacuum_canonical_curvature', CANONICAL_FACTOR * logD2.subs(E, 1) + 32 * k / (1 - 3 * k))
    dq = (a - q) * (1 - 3 * q) / (1 - 3 * a)
    eq('eliminated_beta_derivative', dq.subs(q, qq) - dd)
    eq('derivative_factorization', 1 - dq / (1 + q) - (q - k) * (2 - 3 * (q + k)) / ((1 - 3 * a) * (1 + q)))
    C, delta = S.symbols('C delta', nonnegative=True)
    for sign in [-1, 1]:
        root = (-3 * C + sign * S.sqrt(9 * C * C + 4 * C * (1 - 3 * k))) / 2
        eq('two_root_polynomial_' + str(sign), root * root + 3 * C * root - C * (1 - 3 * k))
    t, v = S.symbols('t v', real=True)
    Gt = deficit.subs(q, k + v * t)
    eq('time_crossing_first_derivative', S.diff(Gt, t).subs(t, 0))
    eq('time_crossing_second_derivative', S.diff(Gt, t, 2).subs(t, 0) + 32 * k / (1 - 3 * k) * (v * v / (4 * k * (1 + k) ** 2)))
    mp.mp.dps = 130
    tol = mp.mpf('1e-55')
    for kk in [mp.mpf(1) / 100, mp.mpf(1) / 10, mp.mpf(3) / 10]:
        av = (1 - kk) * (1 + 3 * kk) / 4
        sv = (1 + kk) / (kk * (1 - 3 * kk))
        alpha = mp.sqrt(av)

        def pars(u):
            ee = mp.exp(2 * alpha * u)
            ff = 1 + sv * ee
            jj = 1 + (1 - 3 * av) * sv * ee
            return ((1 + sv) * ee / ff, av / jj, jj / (ff * ff), av * (1 - 3 * av) * sv * ee * ff / (jj * jj))

        def gforce(u):
            az, qv, _, _ = pars(u)
            return az * (1 + SCALAR_FORCE_FACTOR * qv) / (1 + kk)
        for u in [mp.mpf(-1), mp.mpf('-.1'), mp.mpf(0), mp.mpf('.1'), mp.mpf(1)]:
            az, qv, kv, dv = pars(u)
            gv = gforce(u)
            deficitv = 1 - DEFICIT_FACTOR * (qv - kk) ** 2 / ((1 + kk) ** 2 * (1 - 3 * qv))
            derivative = CANONICAL_FACTOR * mp.diff(lambda z: mp.log(gforce(z)), u) / mp.sqrt(kv)
            predicted = 2 * mp.sqrt(qv) * (1 - dv / (1 + qv))
            tag = str((kk, u))
            ck('direct_force_identity_' + tag, abs(gv - deficitv) < tol)
            ck('direct_signed_derivative_' + tag, abs(derivative - predicted) < tol, str(derivative - predicted))
            ck('maximum_and_positivity_' + tag, gv > 0 and gv <= 1 + tol)
            DD = 1 - gv
            cv = max(mp.mpf(0), DD) * (1 + kk) ** 2 / 4
            roots = [kk + (-3 * cv + sgn * mp.sqrt(9 * cv * cv + 4 * cv * (1 - 3 * kk))) / 2 for sgn in [-1, 1]]
            admissible = [x for x in roots if ACCEPT_ALL_ROOTS or 0 < x < av]
            ck('inverse_recovers_original_' + tag, any((abs(x - qv) < tol for x in admissible)))
            ck('inverse_domains_' + tag, all((0 < x < av for x in admissible)))
            cases.append(dict(k=str(kk), u=str(u), q=str(qv), A2=str(az), Gforce_over_Gref=str(gv), log_field_derivative=str(derivative), inverse_roots=[str(x) for x in roots], admissible_roots=[str(x) for x in admissible]))
        for side in [-1, 1]:
            residuals = []
            for magnitude in [mp.mpf('.001'), mp.mpf('.000001')]:
                u = side * magnitude
                chi = mp.quad(lambda z: mp.sqrt(pars(z)[2]), [0, u])
                ratio = (1 - gforce(u)) / (chi * chi)
                limit = 16 * kk / (1 - 3 * kk)
                residual = abs(ratio / limit - 1)
                residuals.append(residual)
                near.append(dict(k=str(kk), u=str(u), chi=str(chi), deficit_over_chi2=str(ratio), limit=str(limit), relative_difference=str(residual)))
            ck('canonical_quadratic_convergence_' + str((kk, side)), residuals[1] < residuals[0] / 100)
        cv = mp.mpf('.99') * (1 + kk) ** 2 / 4
        roots = [kk + (-3 * cv + sgn * mp.sqrt(9 * cv * cv + 4 * cv * (1 - 3 * kk))) / 2 for sgn in [-1, 1]]
        admitted = [x for x in roots if ACCEPT_ALL_ROOTS or 0 < x < av]
        ck('large_deficit_root_rejection_' + str(kk), len(admitted) == 1 and all((0 < x < av for x in admitted)))
        for velocity in [mp.mpf('1e-5'), mp.mpf('1e-6')]:
            length = mp.mpf(1)
            gap = 1 - 3 * kk
            gg = lambda tt: 1 - DEFICIT_FACTOR * (velocity * tt) ** 2 / ((1 + kk) ** 2 * (gap - 3 * velocity * tt))
            bare = lambda tt: 4 * (av - kk - velocity * tt) / ((1 + kk) ** 2 * (gap - 3 * velocity * tt))
            slope = mp.quad(lambda tt: tt * gg(tt), [-length / 2, 0, length / 2]) / (length ** 3 / 12)
            bare_slope = mp.quad(lambda tt: tt * bare(tt), [-length / 2, 0, length / 2]) / (length ** 3 / 12)
            leading = -mp.mpf(9) * velocity ** 3 * length ** 2 / (5 * (1 + kk) ** 2 * gap ** 2)
            xi = 3 * abs(velocity) * length / (2 * gap)
            remainder = xi * xi / (1 - xi * xi)
            tag = str((kk, velocity))
            ck('window_cubic_slope_bound_' + tag, abs(slope / leading - 1) <= remainder + tol)
            ck('window_bare_not_calibrated_slope_' + tag, abs(slope) < abs(bare_slope) * mp.mpf('1e-5'))
            ck('window_stays_in_domain_' + tag, 0 < kk - velocity / 2 < kk + velocity / 2 < av)
            windows.append(dict(k=str(kk), q_velocity=str(velocity), length=str(length), fitted_calibrated_slope=str(slope), fitted_bare_slope=str(bare_slope), cubic_leading_slope=str(leading), relative_remainder_bound=str(remainder), role='chosen synthetic q trajectory; not a solved cosmology, orbital likelihood or selected phase'))
    result = dict(passed=sum((x['passed'] for x in checks)), failed=sum((not x['passed'] for x in checks)), checks=checks, cases=cases, canonical_near_vacuum=near, synthetic_windows=windows, checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), scope='Ideal weak long-range force calibration only; no ephemeris fit, realized ambient state, unrestricted speed or absolute scale prediction.')
    (out / 'RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(passed=result['passed'], failed=result['failed'], cases=len(cases), failed_checks=[x for x in checks if not x['passed']]), indent=2))
    return result['failed']

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--profiles',type=Path);parser.add_argument('--out',type=Path);args=parser.parse_args()
    def execute(root):
        root.mkdir(parents=True,exist_ok=True);captured=io.StringIO()
        with redirect_stdout(captured):failed=check_turning(root/'turning')
        unit=json.loads((root/'turning'/'RESULTS.json').read_text());assert failed==unit['failed']
        return dict(passed=unit['passed'],failed=unit['failed'],units={'turning':unit},unit_stdout={'turning':captured.getvalue()},checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Ideal weak slowly varying common-background long-range force calibration. No orbital fit, selected background or trajectory, arbitrary speed, action or scale.')
    if args.profiles is None:
        with TemporaryDirectory(prefix='scalar-calibrated-gravity-turning-') as d:result=execute(Path(d))
    else:
        assert not args.profiles.exists();result=execute(args.profiles)
    text=json.dumps(result,indent=2)+'\n'
    if args.out:
        assert not args.out.exists();args.out.write_text(text)
    print(text,end='');return bool(result['failed'])
if __name__=='__main__':raise SystemExit(main())
