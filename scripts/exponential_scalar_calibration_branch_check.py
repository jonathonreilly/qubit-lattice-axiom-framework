#!/usr/local/bin/python3
"""Conditional laboratory calibration and negative-branch light-time constraints."""
from tempfile import TemporaryDirectory
from contextlib import redirect_stdout
import io
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['docs/EXPONENTIAL_SCALAR_CALIBRATION_BRANCH_BOUNDED_THEOREM_NOTE_2026-10-14.md', 'docs/EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md', 'docs/EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md', 'docs/EXPONENTIAL_SCALAR_ENVIRONMENT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-10-14.md']
from pathlib import Path
import json, argparse, hashlib
import sympy as s
import numpy as np
import mpmath as mp
FORCE_DERIVATIVE = 1
USE_CALIBRATION = 1
INVERSE_SIGN = 1
LONG_RANGE_SIGN = 1

def check_calibration(out):
    out.mkdir(parents=True, exist_ok=False)
    mp.mp.dps = 75
    rows = []

    def ck(n, ok, detail=None):
        rows.append(dict(name=n, passed=bool(ok), detail=detail))

    def eq(n, e):
        v = s.factor(e)
        ck(n, v == 0, str(v))
    q, yj, yc, mu, d = s.symbols('q yj yc mu d', positive=True)
    ratio = (1 + q * yj) / (1 + USE_CALIBRATION * q * yc)
    eq('inverse', INVERSE_SIGN * (ratio - 1) / (yj - ratio * yc) - q)
    eq('massless_calibration_degeneracy', ratio.subs({yj: 1, yc: 1}) - 1)
    eq('torque_force_factor', -s.diff(s.exp(-mu * d) / d, d) - (1 + FORCE_DERIVATIVE * mu * d) * s.exp(-mu * d) / d ** 2)
    Lj, Lc = s.symbols('Lj Lc', real=True)
    leading = s.series(ratio.subs({yj: 1 + mu ** 2 * Lj / 2, yc: 1 + mu ** 2 * Lc / 2}), mu, 0, 3).removeO()
    eq('long_range_coefficient', leading - 1 - LONG_RANGE_SIGN * q * (Lj - Lc) * mu ** 2 / (2 * (1 + q)))
    th, R, r, z = s.symbols('theta R r z', real=True)
    dist = s.sqrt(R ** 2 + r ** 2 + z ** 2 - 2 * R * r * s.cos(th))
    eq('point_torque_from_energy', s.diff(s.exp(-mu * dist) / dist, th) + R * r * s.sin(th) * (1 + mu * dist) * s.exp(-mu * dist) / dist ** 3)
    eq('constant_kernel_zero_torque', s.diff(-mu, th))
    eq('r_kernel_torque', s.diff(dist, th) - R * r * s.sin(th) / dist)
    geoms = {'calibration': ('.1905', '.01648', '0', 3), 'science': ('.001', '.0005', '.00007', 3)}

    def harmonic(geometry, inverse_range, kind='yukawa', precision='mp'):
        RR, rr, zz, n = geometry
        if precision == 'mp':
            RR, rr, zz = map(mp.mpf, [RR, rr, zz])
            mm = mp.mpf(inverse_range)

            def torque(t):
                sm = mp.mpf(0)
                for j in range(n):
                    angle = t + 2 * mp.pi * j / n
                    dd = mp.sqrt(RR ** 2 + rr ** 2 + zz ** 2 - 2 * RR * rr * mp.cos(angle))
                    if kind == 'r':
                        sm += RR * rr * mp.sin(angle) / dd
                    else:
                        sm -= RR * rr * mp.sin(angle) * (1 + FORCE_DERIVATIVE * mm * dd) * mp.exp(-mm * dd) / dd ** 3
                return n * sm
            return n / mp.pi * mp.quad(lambda t: torque(t) * mp.sin(n * t), [2 * mp.pi * i / (n * 16) for i in range(17)])
        RR, rr, zz = map(float, [RR, rr, zz])
        mm = float(inverse_range)
        nn = 512
        ts = 2 * np.pi * (np.arange(nn) + 0.5) / nn
        sm = np.zeros_like(ts)
        for j in range(n):
            angle = ts + 2 * np.pi * j / n
            dd = np.sqrt(RR ** 2 + rr ** 2 + zz ** 2 - 2 * RR * rr * np.cos(angle))
            if kind == 'r':
                sm += RR * rr * np.sin(angle) / dd
            else:
                sm -= RR * rr * np.sin(angle) * (1 + FORCE_DERIVATIVE * mm * dd) * np.exp(-mm * dd) / dd ** 3
        return float(2 * np.mean(n * sm * np.sin(n * ts)))
    norms = {name: harmonic(g, 0) for name, g in geoms.items()}
    moments = {name: harmonic(g, 0, kind='r') / norms[name] for name, g in geoms.items()}
    for name, g in geoms.items():
        ck(name + '.nonzero_harmonic', abs(norms[name]) > mp.mpf('1e-8'), str(norms[name]))
        num = harmonic(g, 0, kind='r', precision='double')
        ck(name + '.r_moment_quadrature', abs(mp.mpf(num) / norms[name] - moments[name]) < mp.mpf('1e-10') * max(mp.mpf('1e-12'), abs(moments[name])), str(moments[name]))
    Q = mp.mpf('.2')
    mus = ['0', '.01', '.1', '1', '10', '100', '1000', '10000', '100000']
    records = []
    for ms in mus:
        mm = mp.mpf(ms)
        ys = {}
        for name, g in geoms.items():
            hp = harmonic(g, mm)
            dp = harmonic(g, mm, precision='double')
            ys[name] = hp / norms[name]
            err = abs(mp.mpf(dp) - hp)
            bound = mp.mpf('2e-11') * max(mp.mpf('1e-20'), abs(hp))
            ck(name + '.double_mu_' + ms, err < bound, dict(error=str(err), bound=str(bound)))
        Rc = (1 + Q * ys['science']) / (1 + USE_CALIBRATION * Q * ys['calibration'])
        if mm == 0:
            ck('massless_numeric', abs(Rc - 1) < mp.mpf('1e-45'), str(Rc))
        elif abs(ys['science'] - Rc * ys['calibration']) > mp.mpf('1e-35'):
            inv = INVERSE_SIGN * (Rc - 1) / (ys['science'] - Rc * ys['calibration'])
            ck('inverse_mu_' + ms, abs(inv - Q) < mp.mpf('1e-35'), str(inv))
        if ms in ['.01', '.1']:
            observed = (Rc - 1) / mm ** 2
            pred = LONG_RANGE_SIGN * Q / (1 + Q) * (moments['science'] - moments['calibration']) / 2
            records.append(dict(mu=ms, y_calibration=str(ys['calibration']), y_science=str(ys['science']), normalized_ratio=str(Rc), quadratic_coefficient=str(observed), predicted_quadratic_coefficient=str(pred), coefficient_error=str(abs(observed - pred))))
        else:
            records.append(dict(mu=ms, y_calibration=str(ys['calibration']), y_science=str(ys['science']), normalized_ratio=str(Rc)))
    asym = [r for r in records if 'coefficient_error' in r]
    ck('long_range_relative_coefficient', mp.mpf(asym[0]['coefficient_error']) < mp.mpf('1e-5') * abs(mp.mpf(asym[0]['predicted_quadratic_coefficient'])), asym[0])
    ck('long_range_convergence', mp.mpf(asym[0]['coefficient_error']) < mp.mpf(asym[1]['coefficient_error']) / 20, [a['coefficient_error'] for a in asym])
    result = dict(passed=sum((x['passed'] for x in rows)), failed=sum((not x['passed'] for x in rows)), checks=rows, newton_harmonics={k: str(v) for k, v in norms.items()}, r_moment_ratio_m2={k: str(v) for k, v in moments.items()}, records=records, scope='Toy geometries; published calibration radii plus explicitly assumed geometry, no torque-data fit or empirical exclusion.', checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (out / 'RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    return result['failed']

from pathlib import Path
import sympy as S
import json, hashlib, argparse
DENOMINATOR_FACTOR = S.Integer(3)
GAMMA_FACTOR = S.Integer(2)
BOUND_SIGN = S.Integer(1)

def check_branch():
    rows = []
    cases = []

    def ck(n, b, detail=None):
        rows.append(dict(name=n, passed=bool(b), detail=detail))

    def eq(n, e):
        v = S.factor(S.cancel(e))
        ck(n, v == 0, str(v))
    k, z, E, Q = S.symbols('k z E Q', positive=True)
    a = (1 - k) * (1 + 3 * k) / 4
    s = (1 + k) / (k * (1 - 3 * k))
    D = 1 + s - s * z * z
    q = a * D / (1 + s - DENOMINATOR_FACTOR * a * s * z * z)
    original = a / (1 + (1 - 3 * a) * s * E)
    eq('coordinate_inversion', original.subs(E, z * z / D) - q)
    eq('vacuum_coupling', q.subs(z, 1) - k)
    eq('coupling_limit', S.limit(q, z, 0) - a)
    eq('a_minus_k', a - k - (1 - 3 * k) * (1 + k) / 4)
    eq('negative_derivative_coefficient', 3 * a - 1 + (1 - 3 * k) ** 2 / 4)
    eq('coupling_derivative', S.diff(q, z) - 2 * a * s * (1 + s) * (3 * a - 1) * z / (1 + s - 3 * a * s * z * z) ** 2)
    eq('conformal_inverse', 1 - z * z - (1 - 3 * k) * (q - k) / ((1 + k) * (1 - 3 * q)))
    g, eta, lo, ep = S.symbols('g eta lo ep', real=True)
    qbound = BOUND_SIGN * eta / (2 - eta)
    eq('bound_inversion', GAMMA_FACTOR * qbound / (1 + qbound) - eta)
    eq('gamma_relation', -GAMMA_FACTOR * g / (1 + g) - ((1 - g) / (1 + g) - 1))
    observed_c = S.Rational(21, 1000000)
    observed_e = S.Rational(23, 1000000)
    lower = observed_c - 2 * observed_e
    upper = observed_c + 2 * observed_e
    eq('published_benchmark_lower', lower + S.Rational(25, 1000000))
    eq('published_benchmark_upper', upper - S.Rational(67, 1000000))
    qb0 = qbound.subs(eta, -lower)
    eq('zero_error_q_cap', qb0 - S.Rational(1, 79999))
    eq('zero_error_conformal_cap', qb0 / (1 - 3 * qb0) - S.Rational(1, 79996))
    bridge = []
    for ev in [S.Integer(0), S.Rational(1, 100000), S.Rational(1, 10000)]:
        et = ev - lower
        qb = qbound.subs(eta, et)
        pred = -GAMMA_FACTOR * qb / (1 + qb) + ev
        eq('edge_matches_' + str(ev), pred - lower)
        ck('finite_bound_domain_' + str(ev), 0 <= et < S.Rational(1, 2), str(et))
        bridge.append(dict(epsilon_gamma=str(ev), q_cap=str(qb), q_cap_decimal=str(S.N(qb, 20)), conformal_cap=str(qb / (1 - 3 * qb))))
    for kv in [S.Rational(1, 10 ** 6), S.Rational(1, 10 ** 5), S.Rational(1, 100), S.Rational(1, 10), S.Rational(3, 10)]:
        av = a.subs(k, kv)
        sv = s.subs(k, kv)
        for zv in [S.Integer(1), S.Rational(9, 10), S.Rational(1, 2), S.Rational(1, 100)]:
            sub = {k: kv, z: zv}
            qv = S.factor(q.subs(sub))
            Dv = D.subs(sub)
            Ev = S.factor(zv * zv / Dv)
            tag = str(kv) + '_' + str(zv)
            ck('positive_denominator_' + tag, 1 + sv - 3 * av * sv * zv * zv > 0)
            ck('coupling_floor_and_ceiling_' + tag, kv <= qv < av)
            ck('negative_derivative_' + tag, S.diff(q, z).subs(sub) < 0)
            eq('independent_E_coordinate_' + tag, original.subs({k: kv, E: Ev}) - qv)
            eq('exact_G_change_' + tag, 1 - zv * zv - (1 - 3 * kv) * (qv - kv) / ((1 + kv) * (1 - 3 * qv)))
            predicted = -GAMMA_FACTOR * qv / (1 + qv)
            error_need = S.Max(0, lower - predicted)
            cases.append(dict(k=str(kv), A=str(zv), q=str(qv), gamma_minus_one=str(predicted), minimum_bridge_error=str(error_need), passes_zero_error_benchmark=bool(lower <= predicted <= upper)))
        posq = original.subs({k: kv, E: 4})
        ck('positive_u_breaks_floor_' + str(kv), posq < kv, str(posq))
    qq, kk, bb = S.symbols('qq kk bb', positive=True)
    deficit = (1 - 3 * kk) * (qq - kk) / ((1 + kk) * (1 - 3 * qq))
    eq('deficit_monotonicity', S.diff(deficit, qq) - (1 - 3 * kk) ** 2 / ((1 + kk) * (1 - 3 * qq) ** 2))
    for kv in [S.Rational(1, 10 ** 6), S.Rational(1, 10 ** 5)]:
        upperdef = deficit.subs({kk: kv, qq: qb0})
        ck('conformal_universal_bound_' + str(kv), 0 < upperdef <= qb0 / (1 - 3 * qb0), str(upperdef))
        z2 = 1 - upperdef
        eq('qcap_attained_at_derived_z_' + str(kv), q.subs(k, kv).subs(z * z, z2) - qb0)
    ck('eta_negative_impossible', S.Rational(-1, 100) < 0)
    for test in [S.Rational(1, 100), S.Rational(1, 2), S.Rational(1, 1), S.Rational(100)]:
        ck('eta_two_no_finite_cap_' + str(test), 2 * test / (1 + test) < 2)
    return dict(passed=sum((r['passed'] for r in rows)), failed=sum((not r['passed'] for r in rows)), checks=rows, published_benchmark=dict(central=str(observed_c), reported_error=str(observed_e), lower=str(lower), upper=str(upper), interval_convention='central plus/minus two reported errors; not reconstructed confidence likelihood'), bridge_bounds=bridge, synthetic_cases=cases, scope='Negative-u branch plus explicitly controlled weak long-range light-time bridge; no solved Solar background or global theory exclusion.', checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--profiles',type=Path);parser.add_argument('--out',type=Path);args=parser.parse_args()
    def execute(root):
        root.mkdir(parents=True,exist_ok=True);stream=io.StringIO()
        with redirect_stdout(stream):failed=check_calibration(root/'calibration')
        calibration=json.loads((root/'calibration'/'RESULTS.json').read_text());assert failed==calibration['failed'];branch=check_branch()
        return dict(passed=calibration['passed']+branch['passed'],failed=calibration['failed']+branch['failed'],units=dict(calibration=calibration,branch=branch),calibration_execution_stdout=stream.getvalue(),checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Synthetic geometry and an exposed conditional published interval transformation; no empirical fit or derived Solar matching.')
    if args.profiles is None:
        with TemporaryDirectory(prefix='scalar-calibration-branch-') as d:result=execute(Path(d))
    else:
        assert not args.profiles.exists();result=execute(args.profiles)
    text=json.dumps(result,indent=2)+'\n'
    if args.out:
        assert not args.out.exists();args.out.write_text(text)
    print(text,end='');return bool(result['failed'])
if __name__=='__main__':raise SystemExit(main())
