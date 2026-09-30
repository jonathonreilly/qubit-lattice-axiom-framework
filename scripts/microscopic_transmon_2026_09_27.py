"""Portable supplied-snapshot comparator, with no circuit-parameter refit.
Retrospective conditional imported model; numerical checks are not empirical
acceptance, uncertainty certification, microscopic identification or TOE evidence.
"""
from pathlib import Path
import argparse
import hashlib
import json
import numpy as np
from scipy.linalg import eigh
from microscopic_transmon_independent_2026_09_27 import solve as independent_solve

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    'scripts/microscopic_transmon_independent_2026_09_27.py',
    'data/microscopic_transmon_2026_09_27/fits.json',
    'data/microscopic_transmon_2026_09_27/raw_transfer_fits.json',
    'data/microscopic_transmon_2026_09_27/harmonic_ablation_fits.json',
    'data/microscopic_transmon_2026_09_27/PROTOCOL.md',
    'data/microscopic_transmon_2026_09_27/HARMONIC_ABLATION_PROTOCOL.md',
    'data/microscopic_transmon_2026_09_27/calibration.json',
    'data/microscopic_transmon_2026_09_27/targets.json',
    'data/microscopic_transmon_2026_09_27/cosine_control.json',
    'data/microscopic_transmon_2026_09_27/independent_anchors.json',
    'data/microscopic_transmon_2026_09_27/provenance.json',
    'data/microscopic_transmon_2026_09_27/REFERENCE_CORRECTED_PROTOCOL.md',
    'data/microscopic_transmon_2026_09_27/historical/HARMONIC_ABLATION_PROTOCOL.md',
    'data/microscopic_transmon_2026_09_27/historical/SCOPE.json',
    'data/microscopic_transmon_2026_09_27/historical/calibration.json',
    'data/microscopic_transmon_2026_09_27/historical/harmonic_ablation_fits.json',
    'data/microscopic_transmon_2026_09_27/historical/independent_anchors.json',
    'data/microscopic_transmon_2026_09_27/historical/raw_transfer_fits.json',
)
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/microscopic_transmon_2026_09_27'

def endpoint(p, q, spatial=True, mutation=None, N=20, M=16, K=9):
    ec, js, alpha, omega, g, tau, psi = p
    phi = 2*np.pi*np.arange(8192)/8192
    v = 4*np.sin(phi/2)**2/(1+np.sqrt(1-tau*np.sin(phi/2)**2))
    c = np.fft.rfft(v).real/len(phi)
    c /= -2*c[1] if mutation != 'normalization' else -c[1]
    n = np.arange(-N, N+1, dtype=float)
    d = (n[:, None]-n).astype(int)
    m = abs(d)
    scale = m if spatial and mutation != 'field' else np.ones_like(m)
    ht = c[m]*js/2*((1+alpha)*np.sinc(scale*.15/.8)
           +(1-alpha)*np.sinc(scale*.15/(.8*256/178))*np.exp(1j*d*psi))
    ht[np.diag_indices_from(ht)] = 4*ec*(n-q)**2
    e, u = eigh(ht, subset_by_index=[0, M-1])
    charge = u.conj().T@((n-q)[:, None]*u)
    a = np.diag(np.sqrt(np.arange(1, K)), 1)
    gg = g*1.1 if mutation == 'coupling' else g
    h = np.diag((e-e[0]+omega*np.arange(K)[:, None]).ravel())+gg*np.kron(a+a.T, charge)
    en, vec = eigh(h)
    labels = [0, 1, 2, 3, M]
    weights = abs(vec[labels])**2
    ix = weights.argmax(axis=1)
    if len(set(ix)) != 5:
        raise ValueError('nonunique dressed labels')
    return en[ix[1:]]-en[ix[0]], float(weights[np.arange(5), ix].min())

def predict(p, spatial, mutation=None):
    a, wa = endpoint(p, 0, spatial, mutation)
    b, wb = endpoint(p, .5, spatial, mutation)
    d = abs(a-b)
    if mutation == 'split':
        d /= 2
    return (a+b)/2, d, min(wa, wb)

def main(mutation=None):
    checks = []
    def check(name, condition):
        good = bool(condition)
        checks.append((name, good))
        print(('PASS ' if good else 'FAIL ')+name, flush=True)
        if not good:
            raise ValueError(name)
    def read(name):
        return json.loads((DATA/name).read_text())
    provenance = read('provenance.json')
    for name, digest in provenance['included_sha256'].items():
        payload = (DATA/name).read_bytes()
        if mutation == 'data' and name == 'fits.json':
            payload += b'corruption'
        check('data identity '+name, hashlib.sha256(payload).hexdigest() == digest)
    cal = read('calibration.json')
    raw_quality = {'raw_period_'+str(r['initial_period_V']): r for r in cal['raw_fit_quality']}
    check('corrected raw source membership/status',
          cal['raw_source_membership']['IQ_residual_count'] == 16430
          and cal['raw_source_membership']['delay_count_per_gate'] == 265
          and set(raw_quality) == {'raw_period_0.15', 'raw_period_0.22', 'raw_period_0.3'}
          and raw_quality['raw_period_0.15']['success'] is False
          and all(raw_quality[k]['success'] is True for k in ['raw_period_0.22', 'raw_period_0.3']))
    families = [('source', read('fits.json'), True),
                ('raw', read('raw_transfer_fits.json'), True),
                ('ablation', read('harmonic_ablation_fits.json'), False)]
    expected = {'source': {'archive', 'processed'},
                'raw': {'raw_period_0.15', 'raw_period_0.22', 'raw_period_0.3'},
                'ablation': {'raw_period_0.15', 'raw_period_0.22', 'raw_period_0.3'}}
    results = []
    for family, rows, spatial in families:
        keys = [(r['case'], r['initial_tau']) for r in rows]
        want = {(case, t) for case in expected[family] for t in (None, .01, .1, .4)}
        check(family+' exact keys', len(keys) == len(set(keys)) and set(keys) == want)
        for r in rows:
            name = family+'/'+r['case']+'/'+str(r['initial_tau'])
            p = np.asarray(r['params'])
            check(name+' supplied status/bounds', r['status'] == 'returned' and r['success'] is True
                  and p.shape == (7,) and np.isfinite(p).all() and .1 <= p[0] <= .7
                  and 2 <= p[1] <= 150 and 0 <= p[5] <= .95
                  and abs(p[2]-(256*257-178*143)/(256*257+178*143)) < 1e-15
                  and p[3] == cal['Omega_GHz'] and p[4] == cal['G_GHz'] and p[6] == np.pi
                  and (r['initial_tau'] is not None or p[5] == 0))
            y = np.asarray(cal['calibration_Hz'][r['case']])*1e-9
            check(name+' calibration separation', np.isfinite(y).all() and np.array_equal(y, r['calibration_GHz']))
            m, d, w = predict(p, spatial, mutation)
            check(name+' saved spectra', np.isfinite(m).all() and np.isfinite(d).all()
                  and np.max(abs(m-r['mean_GHz'])) < 1e-8 and np.max(abs(d-r['full_dispersion_GHz'])) < 1e-8 and w > .98)
            residual = [(m[0]-y[0])*1000, (m[1]-m[0]-y[1])*1000]
            if r['initial_tau'] is not None:
                residual.append(float(np.log(d[0]/y[2])))
            check(name+' supplied calibration residual', np.max(abs(np.array(residual)-r['residual'])) < 1e-5
                  and abs(np.dot(residual, residual)/2-r['cost']) < 1e-8)
            results.append(dict(family=family, case=r['case'], initial_tau=r['initial_tau'], params=p.tolist(),
                                mean_GHz=m.tolist(), full_dispersion_GHz=d.tolist(), min_weight=w,
                                recalculated_residual=residual, supplied_optimality=r['optimality'],
                                circuit_fit_success=r['success'],
                                raw_calibration_quality=raw_quality.get(r['case']),
                                input_role=('nonconverged raw-calibration diagnostic' if r['case']=='raw_period_0.15'
                                            else 'supplied calibration snapshot')))
    check('all32 retained', len(results) == 32)
    bykey = {(r['family'], r['case'], r['initial_tau']): r for r in results}
    paired = []
    for case in sorted(expected['raw']):
        for t in (None, .01, .1, .4):
            a, b = [bykey[(f, case, t)] for f in ('raw', 'ablation')]
            dm = (np.array(b['mean_GHz'])-a['mean_GHz'])*1e6
            dd = (np.array(b['full_dispersion_GHz'])-a['full_dispersion_GHz'])*1e6
            if t is None:
                check(case+' cosine ablation identity', max(abs(dm).max(), abs(dd).max()) < .001)
            paired.append(dict(case=case, initial_tau=t, ablation_minus_spatial_mean_kHz=dm.tolist(),
                               ablation_minus_spatial_dispersion_kHz=dd.tolist()))
    for old in read('cosine_control.json'):
        r = bykey[('source', old['case'], None)]
        ec, js, alpha, omega, g, tau, psi = r['params']
        ej = js*((1+alpha)*np.sinc(.15/.8)-(1-alpha)*np.sinc(.15/(.8*256/178)))/2
        check(old['case']+' cosine scale map', abs(ej-old['params'][1]) < 1e-8
              and np.max(abs(np.array(r['mean_GHz'])-old['mean_GHz'][:4])) < 1e-8)
    independent = []
    anchors = read('independent_anchors.json')['rows']
    for family, mode in [('raw', 'spatial'), ('ablation', 'ablation')]:
        r = bykey[(family, 'raw_period_0.3', .01)]
        levels = []
        for N, K, grid in [(22, 12, 4096), (28, 16, 16384)]:
            ends = [independent_solve(r['params'], q, N, K, grid, mode) for q in (0, .5)]
            f = np.array([v['gaps_GHz'] for v in ends]); m = f.mean(axis=0); d = abs(f[0]-f[1])
            if mutation == 'independent':
                m[2] += 1e-5
            check(family+' independent direct basis '+str(N), np.max(abs(m-r['mean_GHz'][:3])) < 1e-8
                  and np.max(abs(d-r['full_dispersion_GHz'][:3])) < 1e-8)
            levels.append(dict(N=N, K=K, grid=grid, endpoints=ends, means_GHz=m.tolist(), dispersion_GHz=d.tolist()))
        anchor = next(a for a in anchors if a['mode'] == mode)['cases'][-1]
        check(family+' independent reviewed anchor', np.max(abs(np.array(levels[-1]['means_GHz'])-anchor['means_GHz'])) < 1e-8)
        check(family+' independent cutoff', np.max(abs(np.array(levels[0]['means_GHz'])-levels[1]['means_GHz'])) < 1e-8
              and np.max(abs(np.array(levels[0]['dispersion_GHz'])-levels[1]['dispersion_GHz'])) < 1e-8)
        independent.append(dict(family=family, levels=levels))
    # Evaluation targets enter only after all supplied-parameter numerical checks.
    target = read('targets.json')
    check('evaluation identity', target['timestamp'] == '20220729-173536-429-b495bf'
          and target['processed']['timestamps'] == target['timestamp']
          and {t['start_width_MHz'] for t in target['raw']['fits']} == {1, 3, 6}
          and len(target['raw']['fits']) == 3
          and all(t['success'] is True and np.isfinite(t['center_Hz']) and t['center_Hz'] > 0 for t in target['raw']['fits'])
          and all(np.isfinite(float(target['processed'][k])) and float(target['processed'][k]) > 0 for k in ['f_center', 'charge_dispersion']))
    for r in results:
        r['processed03_center_error_MHz'] = (r['mean_GHz'][2]*1e9-float(target['processed']['f_center']))/1e6
        r['processed03_dispersion_error_MHz'] = (r['full_dispersion_GHz'][2]*1e9-float(target['processed']['charge_dispersion']))/1e6
        r['raw03_center_errors_MHz'] = [(r['mean_GHz'][2]*1e9-t['center_Hz'])/1e6 for t in target['raw']['fits']]
    print(json.dumps(dict(scope='retrospective supplied calibration snapshots; current raw24 use source-corrected265-delay data; raw_period_0.15 is a nonconverged raw-calibration diagnostic, distinct from circuit fit success; historical267 arrays excluded from current comparisons; no optimizer or extraction rerun; no empirical acceptance gate; raw03 center only',
                          read_inventory=dict(
                              scientific_inputs=['data/microscopic_transmon_2026_09_27/'+n for n in
                                  ['fits.json', 'raw_transfer_fits.json', 'harmonic_ablation_fits.json',
                                   'calibration.json', 'targets.json', 'cosine_control.json', 'independent_anchors.json']],
                              integrity_inputs=['data/microscopic_transmon_2026_09_27/provenance.json']+
                                  ['data/microscopic_transmon_2026_09_27/'+n for n in sorted(provenance['included_sha256'])],
                              note='Scientific data are also read as bytes for integrity checks; protocols are integrity-only runtime reads. The independent helper is imported executable code in AUDIT_INPUT_PATHS.'),
                          results=results, matched_ablation=paired, independent=independent), allow_nan=False))
    print(f'TOTAL: PASS={len(checks)} FAIL=0')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mutation', choices=['data', 'split', 'normalization', 'field', 'coupling', 'independent'])
    args = parser.parse_args()
    try:
        main(args.mutation)
    except Exception as exc:
        print('FAIL '+str(exc))
        print('TOTAL: PASS=0 FAIL=1')
        raise SystemExit(1)
