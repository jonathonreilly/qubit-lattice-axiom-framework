#!/usr/bin/env python3
"""Conditional response audit of the public Ross processed-data estimator.

Port the published MATLAB operations explicitly; do not execute downloaded code.
This is not a raw-data reproduction. Quantile, filter, and calibration ambiguities
are retained as named variants rather than selected against the paper's result.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

import numpy as np
import scipy
from scipy.io import loadmat
from scipy.signal import cheby1, detrend, freqz, sosfiltfilt

RUNS = [6891, 6893, 6895, 6896, 6897, 6900, 6903, 6904, 6905,
        6923, 6925, 6926, 6927, 6930, 6931, 6936, 6939, 6949, 6950,
        6954, 6955, 6956, 6958, 6962, 6964]
MASS_KG = 38.72e-3/2
ARM_M = 3.77e-2/2
CORRECTION = np.exp(1j*53.69*np.pi/180)/.9958
SIDEREAL_DAY = 86164.0905
TT_FREQUENCY = .457120e-3
SPRING = 3.78e-5*(2*np.pi*6.8567e-4)**2
THERMAL = np.sqrt(4*1.38064852e-23*293*SPRING/1.13e5)


def nearest(grid, value):
    """Match MATLAB min(abs(grid-value)), including a first-index tie."""
    right = np.clip(np.searchsorted(grid, value), 0, len(grid)-1)
    left = np.maximum(right-1, 0)
    return np.where(abs(grid[left]-value) <= abs(grid[right]-value), left, right)


def daylight(grid):
    # All comparisons use the old RHS vector in the source assignment.
    return grid - ((grid > 307.042).astype(float)
                   + (grid < 69.082) + (grid < 433.041)
                   + (grid > 671.041))/24


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--source-dir', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    runtime = args.source_dir.parent
    deadline = json.loads((runtime/'DEADLINE.json').read_text())
    assert datetime.now(timezone.utc).timestamp() < deadline['deadline_epoch']
    assert not any((runtime/s).exists() for s in ['STOP_REQUESTED', 'USER_STOP_REQUESTED'])
    root = args.source_dir/'eotwash'
    manifest = json.loads((root/'manifest.json').read_text())
    # Manifest shape is documented in the downloaded package.
    source_rows = manifest.get('files', manifest.get('sources', []))
    assert source_rows
    for row in source_rows:
        name = row.get('path', row.get('file'))
        assert hashlib.sha256((root/name).read_bytes()).hexdigest() == row['sha256']

    arrays, run_slices, counts = [], [], []
    start = 0
    for f, run in enumerate(RUNS, 1):
        raw = loadmat(root/'Fits'/f'run{run}Fits.mat')['out']
        mask = raw[3]/THERMAL < 3.77
        a = raw[:, mask].copy()
        a[0] %= 31556926
        if f >= 10:
            a[0] += 31556926
        sign = 1 if f < 3 or 13 < f < 20 else -1
        arrays.append(np.vstack([a, np.full(a.shape[1], sign)]))
        run_slices.append(slice(start, start+a.shape[1]))
        start += a.shape[1]
        counts.append({'run':run, 'raw':raw.shape[1], 'thermal_retained':a.shape[1], 'sign':sign})
    data = np.concatenate(arrays, axis=1)

    def per_run_detrend(z):
        answer = np.empty_like(z)
        for sl in run_slices:
            answer[sl] = detrend(z[sl], type='linear')
        return answer

    zraw = data[1]+1j*data[2]
    zd = per_run_detrend(zraw)
    # MATLAB default "midpoint" quantile = Hyndman-Fan type 5 / NumPy hazen.
    limits = [np.percentile(a, [5,95], method='hazen') for a in [zd.real, zd.imag]]
    keep = ((zd.real > limits[0][0]) & (zd.real < limits[0][1]) &
            (zd.imag > limits[1][0]) & (zd.imag < limits[1][1]))
    times, signs = data[0,keep], data[4,keep]
    torques = CORRECTION*signs*zd[keep]
    samp_f = 1/(times[4]-times[3])
    basis = np.loadtxt(root/'Basis Functions'/'sunVectMin.out')
    sun_samp_f = 1/np.diff(basis[:2,0])[0]/86400
    factor = int(np.floor(sun_samp_f/samp_f))
    days_samples = int(np.floor(samp_f*SIDEREAL_DAY))
    windows = np.floor((times-times[0])/86400/2).astype(int)
    segments = [np.where(windows==index)[0] for index in range(windows[-1]+1)]
    segments = [index for index in segments if len(index) >= days_samples/4]

    order_diagnostics=[]
    for order in [8,7,6,5,4]:
        b,a=cheby1(order,.05,.8/factor)
        h=freqz(b,a,[np.pi*.8/factor])[1][0]
        order_diagnostics.append({'order':order, 'cutoff_amplitude':abs(h),
                                  'cutoff_error_from_target':abs(abs(h)-10**(-.05/20))})
    auto_order = next(r['order'] for r in order_diagnostics if r['cutoff_error_from_target'] <= 1e-6)

    def estimate(y, x):
        # Source uses x column, y row, hence both apostrophes conjugate.
        return np.array([np.vdot(x[j], (y[j]-y[j].mean()).conj()) /
                         np.vdot(x[j], x[j]) for j in segments])

    def summarize(a, mass=MASS_KG):
        fm=a/(ARM_M*mass)*1e15
        return {'inphase_fm_s2':float(fm.real.mean()),
                'inphase_sem_fm_s2':float(fm.real.std(ddof=1)/np.sqrt(len(fm))),
                'quadrature_fm_s2':float(fm.imag.mean()),
                'quadrature_sem_fm_s2':float(fm.imag.std(ddof=1)/np.sqrt(len(fm))),
                'n_segments':len(fm)}

    variants=[]
    # Named, predeclared alternatives: stable order 8, rounded-coefficient
    # cutoff-tested order, and one lower order. No selection by agreement.
    for order in sorted({8,auto_order,max(1,auto_order-1)}, reverse=True):
        sos=cheby1(order,.05,.8/factor,output='sos')
        filtered=sosfiltfilt(sos,basis,axis=0)
        # MATLAB IIR decimate aligns the last point, SciPy aligns the first.
        offset=(len(basis)-1)%factor
        decimated=filtered[offset::factor]
        grid=daylight(decimated[:,0])
        assert np.all(np.diff(grid)>0), 'Nearest interpolation assumes monotonic grid'
        ids=nearest(grid,times/86400)
        x=decimated[ids,1]+1j*decimated[ids,2]
        amplitudes=estimate(torques,x)
        last=segments[-1][-1]
        shadowed_mass=abs(grid[ids[last]]-times[last]/86400)

        # Inject at the first released amplitude stage, before per-run trend
        # removal. Freeze both observed cuts: this is the conditional linear
        # transfer, not the nonlinear raw-data estimator's total response.
        allids=nearest(grid,data[0]/86400)
        allx=decimated[allids,1]+1j*decimated[allids,2]
        transfer=[]
        for amp in [1.,1j]:
            torq=allx.conj()*np.conj(amp)*(ARM_M*MASS_KG)*1e-15
            raw_injection=torq/(CORRECTION*data[4])
            processed=CORRECTION*signs*per_run_detrend(raw_injection)[keep]
            recovered=estimate(processed,x)/(ARM_M*MASS_KG)*1e15
            transfer.append([float(recovered.real.mean()),float(recovered.imag.mean())])
        transfer=np.array(transfer).T
        # Per-window mean removal alone has a closed exact attenuation.
        attenuation=np.array([1-abs(x[j].mean())**2/np.mean(abs(x[j])**2) for j in segments])
        mean_only=estimate(x.conj()*(ARM_M*MASS_KG)*1e-15,x)/(ARM_M*MASS_KG)*1e15
        assert np.max(abs(mean_only.real-attenuation))<2e-14
        assert np.max(abs(mean_only.imag))<2e-14
        variants.append({'filter_order':order, 'decimation_end_offset':offset,
                         'physical_mass_normalization':summarize(amplitudes),
                         'literal_source_m_alias_days':float(shadowed_mass),
                         'literal_source_m_alias_normalization':summarize(amplitudes,shadowed_mass),
                         'conditional_transfer_2x2':transfer.tolist(),
                         'mean_removal_only_response':float(attenuation.mean()),
                         'mean_removal_response_range':[float(attenuation.min()),float(attenuation.max())],
                         'segment_inphase_torques_Nm':amplitudes.real.tolist(),
                         'segment_quadrature_torques_Nm':amplitudes.imag.tolist()})
    out={'status':'conditional processed-data port; exact MATLAB reproduction not established',
         'created_at':datetime.now(timezone.utc).isoformat(),
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'python_numpy_scipy':[np.__version__,scipy.__version__],
         'data_manifest':manifest,
         'run_counts':counts,'thermal_surviving':data.shape[1],
         'amplitude_surviving':int(keep.sum()),'decimation_factor':factor,
         'sample_interval_s':1/samp_f,'thermal_Nm':float(THERMAL),
         'physical_mass_kg':MASS_KG,'lever_arm_m':ARM_M,
         'cutoff_tests':order_diagnostics,'cutoff_test_auto_order':auto_order,
         'variants':variants,
         'limits':['No raw data: first-stage torque fit and data-dependent selection response unavailable.',
                   'MATLAB version/filter coefficient rounding and actual executed calibration variable state unavailable.',
                   'Public source reassigns m in [m,minI]=min(...); literal and physical-mass normalizations are separately reported.',
                   'Injection uses the published unit-direction basis, without solar inverse-square annual amplitude or first-stage averaging.',
                   'Cuts are fixed at observed data; this is a local conditional transfer, not a corrected published measurement.'],
         'checks':['All downloaded fit/basis source hashes verified.',
                   'Mean-removal transfer agrees with exact projection identity for every segment.']}
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print('Selected amplitudes / segments:',int(keep.sum()),len(segments),'q=',factor)
    print('Filter cutoff checks:',order_diagnostics)
    for row in variants:
        print('order',row['filter_order'],row['physical_mass_normalization'])
        print('m alias',row['literal_source_m_alias_days'],row['literal_source_m_alias_normalization'])
        print('transfer',row['conditional_transfer_2x2'])
    print('Checks: source hashes and exact mean projection passed. MATLAB reproduction UNRESOLVED.')


if __name__=='__main__':
    main()
