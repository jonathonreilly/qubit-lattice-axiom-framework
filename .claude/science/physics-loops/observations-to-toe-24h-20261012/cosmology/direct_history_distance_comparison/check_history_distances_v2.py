#!/usr/bin/env python3
"""Fixed completed histories versus previously exposed processed SN data."""
from pathlib import Path
import argparse, gzip, hashlib, importlib.util, io, json
import numpy as np
from scipy.integrate import cumulative_simpson, quad
from scipy.interpolate import PchipInterpolator
from scipy.linalg import cho_factor, cho_solve

HERE = Path(__file__).resolve().parent
IC = HERE.parent/'direct_thermal_matter_bridge'
CO = HERE.parent/'direct_expansion_reconstruction'
CHECKS = []


def check(name, good, **data):
    CHECKS.append(dict(name=name, passed=bool(good), **data))


def close(name, actual, expected, tolerance):
    error = float(np.max(np.abs(np.asarray(actual)-expected)))
    check(name, np.isfinite(error) and error <= tolerance,
          maximum_absolute_error=error, tolerance=tolerance)


def inputs():
    manifest = json.loads((CO/'PRIMARY_DATA.json').read_text())
    raw = {}
    for key in ['table', 'covariance']:
        item = manifest['files'][key]
        compressed = (CO/item['local_gzip']).read_bytes()
        raw[key] = gzip.decompress(compressed)
        check('primary.'+key, hashlib.sha256(compressed).hexdigest()==item['gzip_sha256']
              and hashlib.sha256(raw[key]).hexdigest()==item['raw_sha256'])
    table = np.genfromtxt(io.BytesIO(raw['table']), names=True, dtype=None, encoding='utf-8')
    flat = np.fromstring(raw['covariance'].decode('ascii'), sep=' ')
    size = int(flat[0]); check('covariance.dimension', size==len(table) and len(flat)==1+size*size)
    matrix = flat[1:].reshape(size, size)
    covariance = (matrix+matrix.T)/2
    z = np.asarray(table['zHD'], float)
    chosen = np.flatnonzero((table['IS_CALIBRATOR']==0)&(z>=.0233)&(z<=1.5))
    z = z[chosen]; zh = np.asarray(table['zHEL'], float)[chosen]
    mag = np.asarray(table['m_b_corr'], float)[chosen]
    c = covariance[np.ix_(chosen, chosen)]
    low = np.flatnonzero(z<.1); transfer = np.flatnonzero(z>=.1)
    old = json.loads((CO/'evidence_v1/RESULTS.json').read_text())['processed_data']
    check('partition.counts', (len(chosen),len(low),len(transfer))==(1358,405,953))
    for name, actual, key in [('selection',chosen,'original_selected_row_indices_zero_based'),
                              ('calibration',low,'calibration_indices_in_selection'),
                              ('transfer',transfer,'transfer_indices_in_selection')]:
        check('partition.exact.'+name, np.array_equal(actual,old[key]))
    for name, actual in [('zHD',z),('zHEL',zh),('m_b_corr',mag)]:
        close('primary.exposed_values.'+name,actual,old[name],0.)
    return table, chosen, z, zh, mag, c, low, transfer, old


def main(freeze, output):
    for item in json.loads(freeze.read_text())['inputs']:
        check('source.'+item['path'],hashlib.sha256(Path(item['path']).read_bytes()).hexdigest()==item['sha256'])
    spec = importlib.util.spec_from_file_location('history_fluid_input',IC/'check_thermal_matter_bridge_v3.py')
    model = importlib.util.module_from_spec(spec);spec.loader.exec_module(model)
    table, chosen, z, zh, mag, covariance, low, transfer, old = inputs()
    cll = covariance[np.ix_(low,low)]; ctl = covariance[np.ix_(transfer,low)]
    ctt = covariance[np.ix_(transfer,transfer)]
    fl = cho_factor(cll,lower=True); fa = cho_factor(covariance,lower=True)
    one = np.ones(len(low)); qone = cho_solve(fl,one)
    intercept_variance = 1/(one@qone)
    gain = cho_solve(fl,ctl.T).T; v = np.ones(len(transfer))-gain@one
    schur = ctt-gain@ctl.T+intercept_variance*np.outer(v,v)
    schur = (schur+schur.T)/2; fs = cho_factor(schur,lower=True)
    check('covariance.positive', all(np.min(np.diag(f[0]))>0 for f in [fl,fa,fs]))
    prediction_hash = hashlib.sha256(np.asarray(schur,dtype='<f8').tobytes()).hexdigest()
    check('covariance.exact_previous',prediction_hash==old['prediction_covariance_sha256_float64_C_order'])

    def score(shape):
        dl = mag[low]-shape[low]; intercept = intercept_variance*(qone@dl)
        rl = dl-intercept; pred = shape[transfer]+gain@dl+v*intercept
        rt = mag[transfer]-pred; chi_l = rl@cho_solve(fl,rl); chi_t = rt@cho_solve(fs,rt)
        oa = np.ones(len(z)); da = mag-shape
        ma = (oa@cho_solve(fa,da))/(oa@cho_solve(fa,oa)); ra = da-ma
        chi_a = ra@cho_solve(fa,ra)
        high = np.flatnonzero((z>=.3)&(z<=1.)); weights = np.zeros(len(z))
        weights[high] = 1/len(high); weights[low] = -1/len(low)
        return dict(intercept_calibration_only=float(intercept),
                    intercept_standard_error=float(np.sqrt(intercept_variance)),
                    calibration_chi2=float(chi_l),conditional_transfer_chi2=float(chi_t),
                    full_profile_identity_only=float(chi_a),
                    decomposition_absolute_error=float(abs(chi_l+chi_t-chi_a)),
                    high_minus_low_residual_mag=float(weights@(mag-shape)),
                    high_minus_low_standard_error_mag=float(np.sqrt(weights@covariance@weights)),
                    shape=shape.tolist(),prediction_transfer=pred.tolist(),
                    residual_calibration=rl.tolist(),residual_transfer=rt.tolist())

    ref_integral = np.array([quad(lambda x:1/np.sqrt(.3*(1+x)**3+.7),0,zi,
                                  epsabs=1e-12,epsrel=1e-12)[0] for zi in z])
    reference_shape = 5*np.log10((1+zh)*ref_integral)
    reference = score(reference_shape)
    old_reference = old['fixed_curves']['supplied_LCDM_0.3']
    close('reference.shape',reference_shape,old_reference['shape_all_selected'],2e-11)
    for key in ['intercept_calibration_only','calibration_chi2','conditional_transfer_chi2']:
        close('reference.'+key,reference[key],old_reference[key],2e-8)
    histories = json.loads((IC/'evidence_v3/histories/RESULTS.json').read_text())['histories']
    ids = ['split_k0.01','equal_k0.01','split_k1e-05','equal_k1e-05','split_k1e-06','equal_k1e-06']
    models = []; control_z = [.0233,.05,.1,.2,.3,.5,.8,1.,1.5]
    for case_id in ids:
        history = next(x for x in histories if x['case']['id']==case_id)
        check(case_id+'.complete',history['success'] and len(history['rows'])==241)
        cfg = history['configuration']; case = history['case']; rows = history['rows']
        nj = np.array([r['NJ'] for r in rows]); logr = np.log([r['Hratio'] for r in rows])
        check(case_id+'.monotone_clock',np.min(np.diff(nj))>0)
        cubic = PchipInterpolator(nj,logr,extrapolate=False)
        ending = cfg['Ntotal']; hnow = rows[-1]['HJ2']
        # Independently derive the physical clock from the primitive scalar state.
        # Compare the actual interpolation input logr, not just the stored Hratio.
        raw_ratios = []
        for j, row in enumerate(rows):
            u, pu = row['state'][0], row['state'][3]
            raw_A = np.exp(np.sqrt(cfg['a'])*u)
            raw_F = 1+cfg['s']*raw_A**2
            raw_B2 = (1+cfg['s'])*raw_A**2/raw_F
            raw_alpha_B = np.sqrt(cfg['a'])/raw_F
            physical_rate = 1+raw_alpha_B*pu
            hj2_from_clock = row['H2']*physical_rate**2/raw_B2
            close(case_id+f'.physical_clock.HJ2.{j}',
                  row['HJ2']/hj2_from_clock, 1., 3e-12)
            close(case_id+f'.physical_clock.NJprime.{j}',
                  row['NJprime'], physical_rate, 3e-12)
            raw_ratios.append(np.sqrt(hj2_from_clock/row['HGR2']))
            close(case_id+f'.interpolation_physical_clock.{j}',
                  np.exp(logr[j])/raw_ratios[-1], 1., 3e-12)
        close(case_id+'.normalization_physical_clock',
              hnow/(rows[-1]['HGR2']*raw_ratios[-1]**2), 1., 3e-12)

        def inverse_e(redshift, linear=False):
            N = ending-np.log1p(redshift); L = cfg['Lf']-np.log1p(redshift)
            g = model.gas(float(L),256,case.get('massless_neutrinos',False),case.get('ideal_gas',False))
            rho = cfg['rho_di']*np.exp(-3*g['NJ'])+g['rho_gas']
            href2 = 1+2*(1+cfg['k'])*cfg['Rstar']*rho/3
            lr = np.interp(N,nj,logr) if linear else cubic(N)
            return float(np.sqrt(hnow/href2)*np.exp(-lr))

        check(case_id+'.late_interval_covered',ending-np.log(2.5)>nj[0] and abs(ending-nj[-1])<2e-9)
        for zi in [0.,*control_z]:
            g = model.gas(float(cfg['Lf']-np.log1p(zi)),256)
            close(case_id+'.entropy_clock.'+str(zi),g['NJ'],ending-np.log1p(zi),2e-9)
        grids = []
        for count in [513,1025]:
            grid = np.linspace(0,1.5,count); integrand = np.array([inverse_e(v) for v in grid])
            check(case_id+f'.positive.{count}',np.isfinite(integrand).all() and np.min(integrand)>0)
            integral = cumulative_simpson(integrand,x=grid,initial=0.)
            distance = PchipInterpolator(grid,integral,extrapolate=False)
            grids.append((grid,distance,5*np.log10((1+zh)*distance(z))))
        close(case_id+'.grid_magnitude',grids[0][2],grids[1][2],2e-5)
        adaptive = []
        for zi in control_z:
            direct = quad(inverse_e,0,zi,epsabs=2e-11,epsrel=2e-11,limit=150)[0]
            delta = 5*np.log10(grids[-1][1](zi)/direct)
            close(case_id+'.adaptive.'+str(zi),delta,0.,2e-5)
            adaptive.append(dict(z=zi,integral=direct,grid_minus_adaptive_mag=float(delta)))
        grid = grids[-1][0]
        li = cumulative_simpson([inverse_e(v,True) for v in grid],x=grid,initial=0.)
        linear_shape = 5*np.log10((1+zh)*PchipInterpolator(grid,li,extrapolate=False)(z))
        interpolation_error = float(np.max(abs(grids[-1][2]-linear_shape)))
        check(case_id+'.interpolation_diagnostic',interpolation_error<=2e-3,
              maximum_shape_difference_mag=interpolation_error,tolerance=2e-3)
        shape = grids[-1][2]; outcome = score(shape)
        check(case_id+'.quadratic_identity',outcome['decomposition_absolute_error']<2e-8)
        models.append(dict(case=case_id,parameters=case,history_configuration=cfg,
                           trajectory_status='Independently reproduced full path' if case_id=='equal_k0.01' else
                           'Parent completed path; independent instantaneous readouts checked; full-path limitations remain',
                           calibration_rows=len(low),exposed_transfer_rows=len(transfer),
                           interpolation_difference_mag=interpolation_error,adaptive_controls=adaptive,
                           maximum_shape_difference_from_reference_mag=float(np.max(abs(shape-reference_shape))),
                           conditional_transfer_chi2_difference_from_reference=outcome['conditional_transfer_chi2']-reference['conditional_transfer_chi2'],
                           **outcome))
    result = dict(scope='Fixed-parameter, previously exposed processed-data development comparison; no blind test or p-value.',
                  selected_rows=chosen.tolist(),selected_CID=np.asarray(table['CID']).astype(str)[chosen].tolist(),
                  zHD=z.tolist(),zHEL=zh.tolist(),m_b_corr=mag.tolist(),calibration_indices=low.tolist(),
                  transfer_indices=transfer.tolist(),prediction_covariance_sha256=prediction_hash,
                  reference=reference,models=models,checks=CHECKS,
                  counts=dict(passed=sum(x['passed'] for x in CHECKS),failed=sum(not x['passed'] for x in CHECKS),total=len(CHECKS)))
    output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(counts=result['counts'],models=[{k:v for k,v in x.items() if k in
          ['case','calibration_chi2','conditional_transfer_chi2','interpolation_difference_mag','high_minus_low_residual_mag']}
          for x in models])),flush=True)
    return bool(result['counts']['failed'])


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--freeze',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    raise SystemExit(main(args.freeze,args.out))
