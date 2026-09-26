#!/usr/bin/env python3
"""Whole-trajectory uncertainty for the empty-start finite spectra."""
from pathlib import Path
import hashlib
import json
import numpy as np

HERE = Path(__file__).resolve().parent
SOURCE = HERE/'empty_spectrum'
RESAMPLES = 4000
SEED = 720925


def scalar_interval(value, draws):
    return {'estimate':float(value),'bootstrap_95_percentile':np.quantile(draws,[.025,.975]).tolist()}


def interpolate_curves(curves, target):
    density = curves[:,:,0]
    valid = (density[:,0] <= target) & (density[:,-1] >= target)
    hi = np.argmax(density >= target,axis=1)
    hi = np.maximum(hi,1); lo = hi-1; row = np.arange(len(curves))
    left,right = curves[row,lo],curves[row,hi]
    fraction = (target-left[:,0])/(right[:,0]-left[:,0])
    return left+(right-left)*fraction[:,None],lo,hi,fraction,valid


def spectral_bootstrap(raw_spectrum, counts, lo, hi, fraction):
    n,_,ns,nc = raw_spectrum.shape
    result = np.empty((len(counts),ns,nc))
    for index in np.unique(lo):
        rows = np.flatnonzero(lo == index)
        assert np.all(hi[rows] == index+1)
        left = (counts[rows]@raw_spectrum[:,index].reshape(n,-1)/n).reshape(len(rows),ns,nc)
        right = (counts[rows]@raw_spectrum[:,index+1].reshape(n,-1)/n).reshape(len(rows),ns,nc)
        result[rows] = left+(right-left)*fraction[rows,None,None]
    return result


def report_one(path,rng):
    meta = json.loads(path.read_text())
    with np.load(path.with_suffix('.npz')) as data:
        # Only the vector spectrum and vector spatial correlation are used.
        # Connected density zero modes require centering before interpolation.
        spectral = data['spectra'][...,[0,2]]
        raw = data['raw'][...,[0,1,2,3,4,10,6]]
        taus = data['taus']; labels = data['shell_squared_radius']
    n,nt,nc = raw.shape
    counts = rng.multinomial(n,np.full(n,1/n),size=RESAMPLES)
    boot = (counts@raw.reshape(n,-1)/n).reshape(RESAMPLES,nt,nc)
    mean = raw.mean(axis=0); mean_spec = spectral.mean(axis=0)
    out = {key:meta[key] for key in ('side','vertices','raw_weights','epsilon','mobility','replicates')}
    out['case'] = path.stem; out['rows'] = []
    targets = [('fixed_tau',2.)]+[('ensemble_density',x) for x in (.75,.9,.95)]
    for kind,target in targets:
        if kind == 'fixed_tau':
            step = int(np.flatnonzero(np.isclose(taus,target))[0])
            estimate,draws = mean[step],boot[:,step]
            spec_estimate = mean_spec[step]
            spec_draws = (counts@spectral[:,step].reshape(n,-1)/n).reshape(RESAMPLES,len(labels),2)
            lo = np.full(RESAMPLES,step-1); hi = np.full(RESAMPLES,step)
            est_lo = step-1; est_hi = step
            estimated_tau = target; tau_draws = np.full(RESAMPLES,target)
        else:
            full,one_lo,one_hi,one_fraction,good = interpolate_curves(mean[None],target)
            draws,lo,hi,fraction,valid = interpolate_curves(boot,target)
            if not good[0] or not np.all(valid):
                out['rows'].append({kind:target,'status':'not_bracketed_in_every_resample',
                                    'valid_resamples':int(valid.sum())})
                continue
            estimate = full[0]; est_lo,est_hi = int(one_lo[0]),int(one_hi[0])
            spec_estimate = mean_spec[est_lo]+one_fraction[0]*(mean_spec[est_hi]-mean_spec[est_lo])
            spec_draws = spectral_bootstrap(spectral,counts,lo,hi,fraction)
            estimated_tau = taus[est_lo]+one_fraction[0]*(taus[est_hi]-taus[est_lo])
            tau_draws = taus[lo]+fraction*(taus[hi]-taus[lo])
        rho = estimate[0]; rho_draws = draws[:,0]
        structure = spec_estimate[:,0]/rho
        structure_draws = spec_draws[:,:,0]/rho_draws[:,None]
        correlation = spec_estimate[:,1]
        correlation_draws = spec_draws[:,:,1]
        dt = (taus[est_hi]-taus[est_lo])/(6*meta['epsilon'])
        activity = (mean[est_hi,5]-mean[est_lo,5])/dt
        indices = np.arange(RESAMPLES)
        activity_draws = (boot[indices,hi,5]-boot[indices,lo,5])*6*meta['epsilon']/(taus[hi]-taus[lo])
        row = {kind:target,'density':scalar_interval(rho,rho_draws),
               'tau':scalar_interval(estimated_tau,tau_draws),
               'successful_hops_per_site_per_time_in_neighboring_time_bin':scalar_interval(activity,activity_draws),
               'activity_tau_bin':[float(taus[est_lo]),float(taus[est_hi])],
               'bond_alignment_given_pair':scalar_interval(estimate[3]/estimate[4],draws[:,3]/draws[:,4]),
               'S0_per_record':scalar_interval(structure[0],structure_draws[:,0]),
               'Smin_per_record':scalar_interval(structure[1],structure_draws[:,1]),
               'squared_integer_radius':labels.tolist(),
               'wave_number_magnitude':(2*np.pi*np.sqrt(labels)/meta['side']).tolist(),
               'spatial_separation':np.sqrt(labels).tolist(),
               'vector_structure_per_record':structure.tolist(),
               'vector_structure_pointwise_95':np.quantile(structure_draws,[.025,.975],axis=0).tolist(),
               'vector_pair_correlation':correlation.tolist(),
               'vector_pair_correlation_pointwise_95':np.quantile(correlation_draws,[.025,.975],axis=0).tolist(),
               'largest_sample_mean_structure_shell':int(labels[np.argmax(structure)])}
        out['rows'].append(row)
    out['input_sha256'] = {f.suffix:hashlib.sha256(f.read_bytes()).hexdigest() for f in (path,path.with_suffix('.npz'))}
    return out


if __name__ == '__main__':
    rng = np.random.default_rng(SEED)
    paths = sorted(SOURCE.glob('L*_p*_mobility*_eps*.json'))
    assert len(paths) == 13,len(paths)
    cases = []
    for path in paths:
        result = report_one(path,rng); cases.append(result)
        row = next(x for x in result['rows'] if x.get('ensemble_density') == .9)
        print(result['case'],json.dumps({k:row.get(k) for k in ('tau','S0_per_record',
            'Smin_per_record','successful_hops_per_site_per_time_in_neighboring_time_bin',
            'largest_sample_mean_structure_shell')}),flush=True)
    output = {'scope':'Exploratory finite-volume spectra; pointwise whole-trajectory intervals, no phase or masslessness conclusion.',
              'bootstrap_resamples':RESAMPLES,'bootstrap_seed':SEED,
              'density_matching':'Ensemble-curve inversion, repeated within every bootstrap. Interpolation error is separate.',
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cases':cases}
    (HERE/'EMPTY_SPECTRUM_ANALYSIS.json').write_text(json.dumps(output,indent=2)+'\n')
