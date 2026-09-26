#!/usr/bin/env python3
"""Prespecified trajectory bootstrap, including ensemble-density inversion."""
from pathlib import Path
import hashlib
import json
import numpy as np

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'volume_followup'
RESAMPLES = 4000
SEED = 720921


def density_match(means, taus, target, epsilon):
    """Each row is a bootstrap ensemble curve, never a stopped trajectory."""
    density = means[:, :, 0]
    valid = (density[:, 0] <= target) & (density[:, -1] >= target)
    curves = means[valid]
    if not len(curves):
        return np.empty((0, means.shape[-1])), np.empty(0), np.empty(0), valid
    hi = np.argmax(curves[:, :, 0] >= target, axis=1)
    hi = np.maximum(hi, 1)
    lo = hi - 1
    row = np.arange(len(curves))
    left, right = curves[row, lo], curves[row, hi]
    fraction = (target-left[:, 0])/(right[:, 0]-left[:, 0])
    values = left+(right-left)*fraction[:, None]
    time = taus[lo]+fraction*(taus[hi]-taus[lo])
    hop_rate = (right[:, 10]-left[:, 10])*6*epsilon/(taus[hi]-taus[lo])
    assert np.allclose(values[:, 0], target)
    return values, time, hop_rate, valid


def transforms(values, rho0):
    return {
        'density': values[..., 0],
        'normalized_response_gain': (rho0+values[..., 5])/values[..., 0],
        'S0_per_record': values[..., 1]/values[..., 0],
        'Smin_per_record': values[..., 2]/values[..., 0],
        'Smin_minus_S0_per_record': (values[..., 2]-values[..., 1])/values[..., 0],
        'bond_alignment_given_pair': values[..., 3]/values[..., 4],
        'radius_two_multiple_probability': values[..., 8],
        'mean_absolute_component_residual': values[..., 9],
    }


def interval(estimate, draws):
    return {'estimate': float(estimate),
            'bootstrap_95_percentile': np.quantile(draws, [.025, .975]).tolist()}


def analyze(path, rng):
    meta = json.loads(path.read_text())
    with np.load(path.with_suffix('.npz')) as stored:
        raw, taus = stored['raw'], stored['taus']
    n, nt, nc = raw.shape
    # Multinomial counts resample whole trajectories without a huge 4-D array.
    counts = rng.multinomial(n, np.full(n, 1/n), size=RESAMPLES)
    boot = (counts @ raw.reshape(n, -1)/n).reshape(RESAMPLES, nt, nc)
    mean = raw.mean(axis=0)
    out = {'case': path.stem, 'vertices': meta['vertices'],
           'replicates': n, 'rho0': meta['rho0'], 'epsilon': meta['epsilon'],
           'raw_weights': meta['raw_weights'], 'rows': []}
    fixed = int(np.flatnonzero(np.isclose(taus, 2))[0])
    sets = [('fixed_tau', 2., mean[fixed], boot[:, fixed], None, None)]
    for target in (.75, .9, .95):
        est, est_t, est_hops, good = density_match(mean[None], taus, target, meta['epsilon'])
        draws, times, hops, valid = density_match(boot, taus, target, meta['epsilon'])
        if not good[0] or not np.all(valid):
            out['rows'].append({'ensemble_density': target,
                                'status': 'not_bracketed_in_every_resample',
                                'valid_resamples': int(valid.sum())})
            continue
        sets.append(('ensemble_density', target, est[0], draws,
                     interval(est_t[0], times), interval(est_hops[0], hops)))
    for kind, target, est, draws, time, hops in sets:
        row = {kind: target}
        e, b = transforms(est, meta['rho0']), transforms(draws, meta['rho0'])
        row.update({key: interval(e[key], b[key]) for key in e})
        if time is not None:
            row['interpolated_tau'] = time
            row['successful_hops_per_site_per_time'] = hops
        else:
            dt = (taus[fixed]-taus[fixed-1])/(6*meta['epsilon'])
            row['successful_hops_per_site_per_time'] = interval(
                (mean[fixed, 10]-mean[fixed-1, 10])/dt,
                (boot[:, fixed, 10]-boot[:, fixed-1, 10])/dt)
        out['rows'].append(row)
    out['input_sha256'] = {f.suffix: hashlib.sha256(f.read_bytes()).hexdigest()
                           for f in (path, path.with_suffix('.npz'))}
    return out


if __name__ == '__main__':
    rng = np.random.default_rng(SEED)
    paths = sorted(SOURCE.glob('L*_p*_eps*_rho*.json'))
    assert len(paths) == 24, len(paths)
    results = []
    for path in paths:
        row = analyze(path, rng)
        results.append(row)
        target = next(x for x in row['rows'] if x.get('ensemble_density') == .9)
        print(row['case'], json.dumps({key: target.get(key) for key in
            ('normalized_response_gain', 'S0_per_record', 'Smin_per_record',
             'successful_hops_per_site_per_time')}), flush=True)
    (HERE/'FOLLOWUP_ANALYSIS.json').write_text(json.dumps({
        'scope': 'Finite-volume confirmation of a selected exploratory contrast; pointwise intervals, no phase inference.',
        'bootstrap_resamples': RESAMPLES, 'bootstrap_seed': SEED,
        'density_matching': 'Invert interpolated ensemble mean density separately in each whole-trajectory bootstrap; time-grid error is not in the intervals.',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'cases': results}, indent=2)+'\n')
