#!/usr/local/bin/python3
"""Finite measured-input error certificates for paired gravity readouts."""
from contextlib import redirect_stdout
from tempfile import TemporaryDirectory
import io,zlib,base64
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['docs/EXPONENTIAL_SCALAR_PAIRED_GRAVITY_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-10-14.md', 'docs/EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md', 'docs/EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md', 'docs/EXPONENTIAL_SCALAR_CALIBRATED_GRAVITY_TURNING_BOUNDED_THEOREM_NOTE_2026-10-14.md']
from pathlib import Path
import argparse, json, hashlib, itertools
import sympy as S
import mpmath as mp
H_GAMMA_FACTOR = 2
INVERSE_SIGN = 1
CROSS_FACTOR = 1
DENOMINATOR_GATE = True

def check_certificate(out):
    out.mkdir(parents=True, exist_ok=False)
    checks = []
    rows = []
    exact = []

    def ck(n, b, d=None):
        checks.append({'name': n, 'passed': bool(b), 'detail': d})

    def eq(n, e):
        v = S.factor(S.cancel(e))
        ck(n, v == 0, str(v))
    k, q, e = S.symbols('k q e', positive=True)
    a = (1 - k) * (1 + 3 * k) / 4
    s = (1 + k) / (k * (1 - 3 * k))
    J = 1 + (1 - 3 * a) * s * e
    qq = a / J
    A2 = (1 + s) * e / (1 + s * e)
    G = A2 * (1 + qq) / (1 + k)
    gamma = (1 - qq) / (1 + qq)
    eq('original_action_affine_force', G * (H_GAMMA_FACTOR * gamma - 1) - 4 * (a - qq) / (1 + k) ** 2)
    eq('gamma_to_coupling', (1 - gamma) / (1 + gamma) - qq)
    eq('old_inverse_intercept', 1 / (1 - 3 * a) - 4 / (1 - 3 * k) ** 2)
    a0, p, x, y = S.symbols('a0 p x y', real=True)
    h1 = p * (a0 - x)
    h2 = p * (a0 - y)
    eq('two_epoch_inverse', INVERSE_SIGN * (y * h1 - x * h2) / (h1 - h2) - a0)
    z = S.symbols('z', real=True)
    h3 = p * (a0 - z)
    eq('third_epoch_residual', (y - x) * (h3 - h1) - (h2 - h1) * (z - x))
    dh, dn, aa, hh, nn = S.symbols('dh dn aa hh nn', real=True)
    eq('measured_ratio_error', (nn + dn) / (hh + dh) - nn / hh - (dn - nn / hh * dh) / (hh + dh))
    gh, ga, eg, ea = S.symbols('gh ga eg ea', positive=True)
    eq('finite_H_product_cross', (gh + eg) * (2 * (ga + ea) - 1) - gh * (2 * ga - 1) - ((2 * ga - 1) * eg + 2 * gh * ea + 2 * CROSS_FACTOR * eg * ea))
    mp.mp.dps = 100
    tol = mp.mpf('1e-50')

    def fields(kk, u, scale):
        av = (1 - kk) * (1 + 3 * kk) / 4
        sv = (1 + kk) / (kk * (1 - 3 * kk))
        ee = mp.exp(2 * mp.sqrt(av) * u)
        ff = 1 + sv * ee
        jj = 1 + (1 - 3 * av) * sv * ee
        qv = av / jj
        az = (1 + sv) * ee / ff
        return (scale * az * (1 + qv) / (1 + kk), (1 - qv) / (1 + qv), qv)

    def measured(Gh, gah, eG, ega):
        qh = (1 - gah) / (1 + gah)
        Hh = Gh * (H_GAMMA_FACTOR * gah - 1)
        eqv = 2 * ega / ((1 + gah) * (1 + gah - ega))
        eh = abs(2 * gah - 1) * eG + 2 * abs(Gh) * ega + 2 * CROSS_FACTOR * eG * ega
        return (qh, Hh, eqv, eh)

    def infer(ms):
        q1, h1, eq1, eh1 = ms[0]
        q2, h2, eq2, eh2 = ms[1]
        D = h1 - h2
        eD = eh1 + eh2
        if DENOMINATOR_GATE and abs(D) <= eD:
            return None
        if D == 0:
            return None
        N = q2 * h1 - q1 * h2
        ahat = INVERSE_SIGN * N / D
        eN = abs(q2) * eh1 + abs(h1) * eq2 + eq2 * eh1 + abs(q1) * eh2 + abs(h2) * eq1 + eq1 * eh2
        bound = (eN + abs(ahat) * eD) / (abs(D) - eD)
        return (ahat, bound, D, eD)

    def residual(ms):
        q1, h1, eq1, eh1 = ms[0]
        q2, h2, eq2, eh2 = ms[1]
        q3, h3, eq3, eh3 = ms[2]
        Q21 = q2 - q1
        Q31 = q3 - q1
        H21 = h2 - h1
        H31 = h3 - h1
        eQ21 = eq2 + eq1
        eQ31 = eq3 + eq1
        eH21 = eh2 + eh1
        eH31 = eh3 + eh1
        zz = Q21 * H31 - H21 * Q31
        ez = abs(Q21) * eH31 + abs(H31) * eQ21 + CROSS_FACTOR * eQ21 * eH31 + abs(H21) * eQ31 + abs(Q31) * eH21 + CROSS_FACTOR * eH21 * eQ31
        return (zz, ez)

    def fmt(x):
        return mp.nstr(x, 65)
    scales = [mp.mpf(1) / 7, mp.mpf(1), mp.mpf(13)]
    signs = list(itertools.product([-1, 0, 1], repeat=2))
    scale_reference = {}
    for ki, kk in enumerate([mp.mpf(1) / 100, mp.mpf(1) / 10, mp.mpf(3) / 10]):
        av = (1 - kk) * (1 + 3 * kk) / 4
        for scale in scales:
            true = [fields(kk, u, scale) for u in [mp.mpf(-1) / 2, mp.mpf(0), mp.mpf(2) / 5]]
            zero = [measured(g, ga, mp.mpf(0), mp.mpf(0)) for g, ga, qv in true]
            iv = infer(zero)
            ck('exact_inverse_' + str((ki, scale)), iv is not None and abs(iv[0] - av) < tol)
            zz, ez = residual(zero)
            ck('exact_third_' + str((ki, scale)), abs(zz) < tol)
            for ai, bi in signs:
                sg = [ai, bi, -ai]
                sa = [bi, -ai, -bi]
                ms = []
                inp = []
                pass_bounds = True
                for i, (g, ga, qv) in enumerate(true):
                    eG = abs(g) * mp.mpf('1e-8')
                    ega = mp.mpf('1e-8')
                    Gh = g + sg[i] * eG
                    gah = ga + sa[i] * ega
                    m = measured(Gh, gah, eG, ega)
                    ms.append(m)
                    qh, hh, eqv, eh = m
                    Htrue = g * (2 * ga - 1)
                    pass_bounds = pass_bounds and abs(qh - qv) <= eqv + tol and (abs(hh - Htrue) <= eh + tol)
                    inp.append({'G_true': fmt(g), 'gamma_true': fmt(ga), 'G_measured': fmt(Gh), 'gamma_measured': fmt(gah), 'eG': fmt(eG), 'egamma': fmt(ega), 'q_measured': fmt(qh), 'H_measured': fmt(hh), 'eq': fmt(eqv), 'eH': fmt(eh)})
                tag = str((ki, fmt(scale), ai, bi))
                ck('all_six_input_bounds_' + tag, pass_bounds)
                iv = infer(ms)
                ck('separation_gate_' + tag, iv is not None)
                ah, eb, D, eD = iv
                ck('finite_a_certificate_' + tag, abs(ah - av) <= eb + tol)
                lo, hi = (ah - eb, ah + eb)
                good = mp.mpf(1) / 4 < lo < hi < mp.mpf(1) / 3
                ck('physical_a_interval_' + tag, good)
                kl = (1 - 2 * mp.sqrt(1 - 3 * lo)) / 3 if good else mp.nan
                kh = (1 - 2 * mp.sqrt(1 - 3 * hi)) / 3 if good else mp.nan
                ck('k_interval_contains_true_' + tag, good and kl <= kk <= kh)
                zval, zerr = residual(ms)
                ck('third_residual_inside_certificate_' + tag, abs(zval) <= zerr + tol)
                key = (ki, ai, bi)
                values = (ah, eb, zval / scale, zerr / scale)
                if key not in scale_reference:
                    scale_reference[key] = values
                else:
                    ck('common_scale_certificate_invariant_' + tag, all((abs(x - y) < tol for x, y in zip(values, scale_reference[key]))))
                rows.append({'k': fmt(kk), 'calibration': fmt(scale), 'signs': [ai, bi], 'inputs': inp, 'a_hat': fmt(ah), 'a_error_bound': fmt(eb), 'k_interval': [fmt(kl), fmt(kh)], 'Z_hat': fmt(zval), 'Z_error_bound': fmt(zerr), 'role': 'synthetic calibration1-2 and separate synthetic epoch3; finite correlated noise controls, not observed holdout'})
            damaged = [measured(g, ga + (mp.mpf('1e-3') if i == 2 else 0), abs(g) * mp.mpf('1e-8'), mp.mpf('1e-8')) for i, (g, ga, qv) in enumerate(true)]
            dz, de = residual(damaged)
            ck('third_data_damage_rejected_' + str((ki, scale)), abs(dz) > de)
            exact.append({'k': fmt(kk), 'calibration': fmt(scale), 'altered_third_residual': fmt(dz), 'error_bound': fmt(de), 'first_two_not_refit': True})
    unresolved = [(mp.mpf('.1'), mp.mpf(1), mp.mpf('.01'), mp.mpf('.1')), (mp.mpf('.11'), mp.mpf('1.01'), mp.mpf('.01'), mp.mpf('.1'))]
    ck('unresolved_nonzero_denominator_rejected', infer(unresolved) is None)
    ck('identical_epochs_rejected', infer([unresolved[0], unresolved[0]]) is None)
    r = {'passed': sum((c['passed'] for c in checks)), 'failed': sum((not c['passed'] for c in checks)), 'checks': checks, 'noise_cases': rows, 'third_epoch_data_damages': exact, 'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'scope': 'Conditional finite measured-input certificate. No real dataset, confidence interval, action/state or absolute scale derivation.'}
    (out / 'RESULTS.json').write_text(json.dumps(r, indent=2) + '\n')
    print(json.dumps({'passed': r['passed'], 'failed': r['failed'], 'noise_cases': len(rows), 'failed_checks': [c for c in checks if not c['passed']]}, indent=2))
    return r['failed']

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--profiles',type=Path);parser.add_argument('--out',type=Path);args=parser.parse_args()
    def execute(root):
        root.mkdir(parents=True,exist_ok=True);captured=io.StringIO()
        with redirect_stdout(captured):failed=check_certificate(root/'certificate')
        unit=json.loads((root/'certificate'/'RESULTS.json').read_text());assert failed==unit['failed']
        raw=json.dumps(unit,sort_keys=True,separators=(',',':')).encode()
        payload=dict(codec='zlib-base64-json-v1',uncompressed_bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),data=base64.b64encode(zlib.compress(raw,9)).decode('ascii'))
        restored=zlib.decompress(base64.b64decode(payload['data']));assert len(restored)==payload['uncompressed_bytes'] and hashlib.sha256(restored).hexdigest()==payload['sha256'] and json.loads(restored)==unit
        return dict(passed=unit['passed'],failed=unit['failed'],complete_unit_payload=payload,unit_stdout=captured.getvalue(),checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Finite measured-input deterministic certificate; all complete result data included losslessly. No empirical fit, Gaussian confidence statement or action/state/scale derivation.')
    if args.profiles is None:
        with TemporaryDirectory(prefix='scalar-paired-gravity-certificate-') as d:result=execute(Path(d))
    else:
        assert not args.profiles.exists();result=execute(args.profiles)
    text=json.dumps(result,indent=2)+'\n'
    if args.out:
        assert not args.out.exists();args.out.write_text(text)
    print(text,end='');return bool(result['failed'])
if __name__=='__main__':raise SystemExit(main())
