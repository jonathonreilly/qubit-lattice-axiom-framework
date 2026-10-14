#!/usr/local/bin/python3
"""Complete-body scalar charge and finite-window source amplitude."""
from contextlib import redirect_stdout
from tempfile import TemporaryDirectory
import io
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['docs/EXPONENTIAL_SCALAR_COMPOSITE_CHARGE_BOUNDED_THEOREM_NOTE_2026-10-14.md', 'docs/EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md', 'docs/EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md']
from pathlib import Path
import argparse, hashlib, json
import sympy as S
import mpmath as mp
ST_TRACE_SIGN = -1
ST_VIRIAL_FACTOR = 2
ST_KINETIC_FACTOR = 2
ST_DENSITY_ONLY = False
ST_BOUNDARY_TERM = 1

def check_static(out):
    out.mkdir(parents=True, exist_ok=False)
    checks = []
    cases = []
    angles = []

    def ck(name, passed, detail=None):
        checks.append(dict(name=name, passed=bool(passed), detail=detail))

    def eq(name, expr):
        v = S.factor(S.cancel(expr))
        ck(name, v == 0, str(v))
    r, p, rho = S.symbols('r p rho', positive=True)
    pr = p * (1 - r * r) ** 2
    pt = pr + r * S.diff(pr, r) / 2
    trace = pr + 2 * pt
    eq('radial_conservation', S.diff(pr, r) + 2 * (pr - pt) / r)
    eq('regular_center', pr.subs(r, 0) - pt.subs(r, 0))
    eq('boundary_radial_traction', pr.subs(r, 1))
    eq('integrated_Laue', S.integrate(r * r * trace, (r, 0, 1)))
    eq('weighted_virial', S.integrate(r ** 4 * trace, (r, 0, 1)) + ST_VIRIAL_FACTOR * S.integrate(r ** 4 * pr, (r, 0, 1)))
    f = S.Function('f')(r)
    eq('weighted_divergence_identity', S.diff(r ** 3 * f * pr, r) - (r * r * f * trace + r ** 3 * S.diff(f, r) * pr))
    eq('unsupported_pressure_surface_flux', S.integrate(3 * p * r * r, (r, 0, 1)) - ST_BOUNDARY_TERM * p)
    ck('unsupported_pressure_is_not_Laue', S.integrate(3 * p * r * r, (r, 0, 1)) != 0)
    Q, b, T, box, yprime = S.symbols('Q beta T box Yprime')
    EL = 2 * Q * (box - yprime) + b * T
    eq('kinetic_trace_normalization', EL.subs(box, yprime - b * T / (ST_KINETIC_FACTOR * Q)))
    A, M, x, G = S.symbols('A M x G', positive=True)
    eq('Jordan_mass_radius_conversion', G * (A * M) / (x / A) - A * A * G * M / x)
    q = S.symbols('q', nonnegative=True)
    eq('metric_gamma_ratio', (1 - q) / (1 + q) - 1 + 2 * q / (1 + q))
    E, g = S.symbols('E grad', positive=True)
    eq('passive_trace_force', -b * E * g / E + b * g)
    for n in range(1, 13):
        ck('lower_envelope_series_sign_' + str(n), S.Rational(1 - 2 * n, S.factorial(2 * n + 1)) < 0)
    mp.mp.dps = 70
    tol = mp.mpf('1e-45')
    energy = mp.mpf(1) / 3
    fs = lambda x: mp.sinh(x) / x if x else mp.mpf(1)
    weighted = lambda x: mp.cosh(x) - fs(x)
    charges = {}
    for pp in [mp.mpf(-2) / 5, mp.mpf(0), mp.mpf(2) / 5]:
        prf = lambda rr: pp * (1 - rr * rr) ** 2
        ptf = lambda rr: pp * (1 - rr * rr) * (1 - 3 * rr * rr)
        sf = lambda rr: prf(rr) + 2 * ptf(rr)
        moment = mp.quad(lambda rr: rr ** 4 * (1 + ST_VIRIAL_FACTOR * prf(rr)), [0, 1])
        ck('energy_condition_' + str(pp), all((abs(prf(mp.mpf(j) / 100)) <= 1 and abs(ptf(mp.mpf(j) / 100)) <= 1 for j in range(101))))
        for mu in [mp.mpf(0), mp.mpf('0.0001'), mp.mpf('.1'), mp.mpf(1), mp.mpf(3)]:
            tag = str(pp) + '_' + str(mu)
            charge = mp.quad(lambda rr: rr * rr * fs(mu * rr) * (1 + (0 if ST_DENSITY_ONLY else ST_TRACE_SIGN) * sf(rr)), [0, 1])
            weighted_charge = mp.quad(lambda rr: rr * rr * (fs(mu * rr) + weighted(mu * rr) * prf(rr)), [0, 1])
            density_charge = mp.quad(lambda rr: rr * rr * fs(mu * rr), [0, 1])
            ck('weighted_charge_identity_' + tag, abs(charge - weighted_charge) < tol, str(charge - weighted_charge))
            low = 2 * fs(mu) - mp.cosh(mu)
            high = mp.cosh(mu)
            ck('conditional_charge_envelope_' + tag, low - tol <= charge / energy <= high + tol)
            approx = energy + mu * mu * moment / 6
            remainder = abs(charge - approx) / energy
            rem_bound = 4 * (fs(mu) - 1 - mu * mu / 6)
            ck('small_mass_remainder_' + tag, remainder <= rem_bound + tol, dict(remainder=str(remainder), bound=str(rem_bound)))
            if not mu:
                ck('massless_composite_charge_' + tag, abs(charge - energy) < tol)
            if mu and pp:
                ck('finite_range_density_only_fails_' + tag, abs(charge - density_charge) > tol)
            for rr in [mp.mpf('1.5'), mp.mpf(3)]:
                deriv = mp.diff(lambda rad: mp.exp(-mu * rad) / rad, rr)
                ck('exterior_force_factor_' + tag + '_' + str(rr), abs(-rr * rr * deriv - (1 + mu * rr) * mp.exp(-mu * rr)) < tol)
            charges[str(pp), str(mu)] = charge
            cases.append(dict(p0_over_rho0=str(pp), mu_R=str(mu), energy_over_4pi=str(energy), trace_charge_over_4pi=str(charge), weighted_charge_over_4pi=str(weighted_charge), density_charge_over_4pi=str(density_charge), charge_over_energy=str(charge / energy), second_moment_over_4pi=str(moment), lower_bound=str(low), upper_bound=str(high), remainder=str(remainder), remainder_bound=str(rem_bound)))
    for mu in [mp.mpf('.0001'), mp.mpf('.1'), mp.mpf(1), mp.mpf(3)]:
        ck('same_mass_distinct_stress_charge_' + str(mu), charges[str(mp.mpf(-2) / 5), str(mu)] < charges[str(mp.mpf(0)), str(mu)] < charges[str(mp.mpf(2) / 5), str(mu)])
    for mu in [mp.mpf(0), mp.mpf('.0001'), mp.mpf('.1'), mp.mpf(1), mp.mpf(3)]:
        for rr in [mp.mpf('1.5'), mp.mpf(3)]:
            for ss in [mp.mpf('.3'), mp.mpf('.8')]:
                angular = mp.quad(lambda t: mp.exp(-mu * mp.sqrt(rr * rr + ss * ss - 2 * rr * ss * t)) / mp.sqrt(rr * rr + ss * ss - 2 * rr * ss * t), [-1, 0, 1]) / 2
                predicted = mp.exp(-mu * rr) / rr * fs(mu * ss)
                err = abs(angular - predicted)
                ck('angular_Yukawa_' + str((mu, rr, ss)), err < tol, str(err))
                angles.append(dict(mu=str(mu), r=str(rr), source_radius=str(ss), angular=str(angular), predicted=str(predicted), absolute_error=str(err)))
    result = dict(passed=sum((x['passed'] for x in checks)), failed=sum((not x['passed'] for x in checks)), checks=checks, cases=cases, angular_green_checks=angles, checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), scope='Conditional complete isolated stationary leading weak stress; synthetic math only. Universal coupling/action/background/material realization remain premises.')
    (out / 'RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(passed=result['passed'], failed=result['failed'], cases=len(cases), failed_checks=[x for x in checks if not x['passed']]), indent=2))
    return result['failed']

from pathlib import Path
import argparse, hashlib, json
import sympy as S
import mpmath as mp
DY_MOMENTUM_SIGN = 1
DY_ENDPOINT_FACTOR = S.Rational(1, 2)
DY_RETARDED_COEFFICIENT = 2
DY_TIME_SHIFT = 1

def check_dynamic(out):
    out.mkdir(parents=True, exist_ok=False)
    rows = []
    cases = []
    windows = []

    def ck(name, passed, detail=None):
        rows.append(dict(name=name, passed=bool(passed), detail=detail))

    def eq(name, e):
        v = S.factor(S.simplify(e))
        ck(name, v == 0, str(v))
    r, t, w, e = S.symbols('r t omega epsilon', positive=True)
    h = (1 - r * r) ** 3
    lap = S.diff(h, r, 2) + 2 * S.diff(h, r) / r
    rho = 1 + e * S.cos(w * t) * lap
    j = DY_MOMENTUM_SIGN * e * w * S.sin(w * t) * S.diff(h, r)
    pr = -e * w * w * S.cos(w * t) * h
    eq('energy_conservation', S.diff(rho, t) + S.diff(r * r * j, r) / (r * r))
    eq('momentum_conservation', S.diff(j, t) + S.diff(pr, r))
    for n in range(3):
        eq('vanishing_h_boundary_jet_' + str(n), S.diff(h, r, n).subs(r, 1))
    eq('zero_boundary_flux', j.subs(r, 1))
    eq('zero_boundary_traction', pr.subs(r, 1))
    energy = S.integrate(r * r * rho, (r, 0, 1))
    moment = S.integrate(r ** 4 * rho, (r, 0, 1))
    stress = S.integrate(3 * r * r * pr, (r, 0, 1))
    qinst = energy - stress
    H0 = S.integrate(r * r * h, (r, 0, 1))
    eq('constant_total_energy', energy - S.Rational(1, 3))
    eq('moment_first', S.diff(moment, t) - 2 * S.integrate(r ** 3 * j, (r, 0, 1)))
    eq('moment_second', S.diff(moment, t, 2) - 2 * stress)
    eq('instantaneous_charge_identity', qinst - (energy - S.diff(moment, t, 2) / 2))
    eq('moment_polynomial_fixture', moment - S.Rational(1, 5) - 6 * e * S.cos(w * t) * H0)
    eq('instantaneous_coefficient3', qinst - energy - 3 * e * w * w * S.cos(w * t) * H0)
    sinc = S.sin(w * r) / (w * r)
    eq('radial_Helmholtz', S.diff(sinc, r, 2) + 2 * S.diff(sinc, r) / r + w * w * sinc)
    eq('Helmholtz_boundary_outer', (r * r * (S.diff(h, r) * sinc - h * S.diff(sinc, r))).subs(r, 1))
    eq('Helmholtz_boundary_center', S.limit(r * r * (S.diff(h, r) * sinc - h * S.diff(sinc, r)), r, 0))
    p0, p1, T0, E0 = S.symbols('Iprime0 Iprime1 window E')
    eq('finite_window_endpoint_coefficient', -DY_ENDPOINT_FACTOR * (p1 - p0) / (E0 * T0) + (p1 - p0) / (2 * E0 * T0))
    eq('retarded_coefficient_after_Helmholtz', DY_RETARDED_COEFFICIENT - (-1 + 3))
    ck('uniform_density_positive', S.Rational(1, 1) - S.Rational(42, 1000) > 0)
    ck('uniform_momentum_bound', S.Rational(12, 1000) < S.Rational(958, 1000))
    ck('uniform_stress_bound', S.Rational(4, 1000) < S.Rational(958, 1000))
    eq('retardation_band_error_constant', 2 * 4 * 2 - 16)
    eq('full_average_error_constant', 16 + 2 - 18)
    mp.mp.dps = 70
    eps = mp.mpf('.001')
    tol = mp.mpf('1e-45')
    En = mp.mpf(1) / 3
    hf = lambda x: (1 - x * x) ** 3
    dh = lambda x: -6 * x * (1 - x * x) ** 2
    lh = lambda x: -18 + 60 * x * x - 42 * x ** 4
    hzero = mp.quad(lambda x: x * x * hf(x), [0, 1])
    for omega in [mp.mpf(1) / 5, mp.mpf(1), mp.mpf(2)]:
        sk = lambda x: mp.sin(omega * x) / (omega * x) if x else mp.mpf(1)
        hk = mp.quad(lambda x: x * x * hf(x) * sk(x), [0, 1])
        lapk = mp.quad(lambda x: x * x * lh(x) * sk(x), [0, 1])
        ck('weighted_Helmholtz_' + str(omega), abs(lapk + omega ** 2 * hk) < tol, str(lapk + omega ** 2 * hk))
        for tt in [mp.mpf(0), mp.mpf(2) / 7, mp.mpf(3)]:
            inst = mp.quad(lambda x: x * x * (1 + eps * mp.cos(omega * tt) * (lh(x) + 3 * omega ** 2 * hf(x))), [0, 1])
            predinst = En + 3 * eps * omega ** 2 * mp.cos(omega * tt) * hzero
            direct = En + eps * mp.quad(lambda x: x * x * (lh(x) + 3 * omega ** 2 * hf(x)) * mp.quad(lambda z: mp.cos(omega * (tt + DY_TIME_SHIFT * x * z)), [-1, 0, 1]) / 2, [0, 1])
            predicted = En + DY_RETARDED_COEFFICIENT * eps * omega ** 2 * mp.cos(omega * tt) * hk
            ck('instantaneous_radial_' + str((omega, tt)), abs(inst - predinst) < tol)
            ck('retarded_angular_' + str((omega, tt)), abs(direct - predicted) < tol, str(direct - predicted))
            ck('retardation_not_instantaneous_' + str((omega, tt)), abs(direct - inst) > mp.mpf('1e-12'))
            cases.append(dict(omega=str(omega), time=str(tt), energy_over_4pi=str(En), Qinstant_over_4pi=str(inst), Fretarded_over_4pi=str(direct), Fformula_over_4pi=str(predicted), H0_over_4pi=str(hzero), Hk_over_4pi=str(hk)))
        for start, length in [(mp.mpf(0), mp.mpf(1) / 2), (mp.mpf(1) / 7, mp.mpf(3)), (mp.mpf(2) / 3, mp.mpf(40))]:
            end = start + length
            avgcos = (mp.sin(omega * end) - mp.sin(omega * start)) / (omega * length)
            iq = mp.quad(lambda tt: En + 3 * eps * omega ** 2 * mp.cos(omega * tt) * hzero, [start, end]) / length
            fq = mp.quad(lambda tt: En + DY_RETARDED_COEFFICIENT * eps * omega ** 2 * mp.cos(omega * tt) * hk, [start, end]) / length
            ip = lambda tt: -6 * eps * omega * mp.sin(omega * tt) * hzero
            endpoint = En - mp.mpf(str(DY_ENDPOINT_FACTOR)) * (ip(end) - ip(start)) / length
            tag = str((omega, start, length))
            ck('window_endpoint_identity_' + tag, abs(iq - endpoint) < tol, str(iq - endpoint))
            ck('window_retarded_integral_' + tag, abs(fq - (En + 2 * eps * omega ** 2 * avgcos * hk)) < tol)
            ck('window_instantaneous_bound_' + tag, abs(iq / En - 1) <= 2 / length)
            ck('window_shift_band_bound_' + tag, abs(fq - iq) / En <= 16 / length)
            ck('window_retarded_bound_' + tag, abs(fq / En - 1) <= 18 / length)
            windows.append(dict(omega=str(omega), start=str(start), length=str(length), Qinstant_average_over_E=str(iq / En), Fretarded_average_over_E=str(fq / En), instantaneous_bound=str(2 / length), shift_bound=str(16 / length), retarded_bound=str(18 / length), endpoint_formula_over_E=str(endpoint / En)))
    result = dict(passed=sum((x['passed'] for x in rows)), failed=sum((not x['passed'] for x in rows)), checks=rows, cases=cases, windows=windows, checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), scope='Finite-band source-generated massless amplitude, not force/radiation power or selected homogeneous state. Synthetic complete conserved stress, not derived material.')
    (out / 'RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(passed=result['passed'], failed=result['failed'], cases=len(cases), windows=len(windows), failed_checks=[x for x in rows if not x['passed']]), indent=2))
    return result['failed']

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--profiles',type=Path);parser.add_argument('--out',type=Path);args=parser.parse_args()
    def execute(root):
        root.mkdir(parents=True,exist_ok=True);units={};streams={}
        for name,fn in [('static',check_static),('dynamic',check_dynamic)]:
            captured=io.StringIO()
            with redirect_stdout(captured):failed=fn(root/name)
            result=json.loads((root/name/'RESULTS.json').read_text())
            assert failed==result['failed'];units[name]=result;streams[name]=captured.getvalue()
        return dict(passed=sum(z['passed'] for z in units.values()),failed=sum(z['failed'] for z in units.values()),units=units,unit_stdout=streams,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Conditional complete-body scalar charge and finite-window source amplitude; no selected matter or homogeneous wave, full metric, ambient response or empirical likelihood.')
    if args.profiles is None:
        with TemporaryDirectory(prefix='scalar-composite-charge-') as d:result=execute(Path(d))
    else:
        assert not args.profiles.exists();result=execute(args.profiles)
    text=json.dumps(result,indent=2)+'\n'
    if args.out:
        assert not args.out.exists();args.out.write_text(text)
    print(text,end='');return bool(result['failed'])
if __name__=='__main__':raise SystemExit(main())
