"""Conditional supplied-rate population transfer; no optimizer reproduction.
Numerical/integrity checks do not test empirical proximity or grant scientific status.
"""
from pathlib import Path
import argparse
import hashlib
import json
import numpy as np
from preparation_transfer_independent_2026_09_27 import propagate as independent_propagate, reconstruct as independent_readout

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = [
    "scripts/preparation_transfer_independent_2026_09_27.py",
    "data/preparation_transfer_2026_09_27/CALIBRATION_INPUTS.json",
    "data/preparation_transfer_2026_09_27/FROZEN_TARGET_PREDICTIONS.json",
    "data/preparation_transfer_2026_09_27/NO_DECAY_CONTROL.json",
    "data/preparation_transfer_2026_09_27/PREDICTION_FREEZE.json",
    "data/preparation_transfer_2026_09_27/PROTOCOL.md",
    "data/preparation_transfer_2026_09_27/SEQUENTIAL_CONTROL_INPUTS.json",
    "data/preparation_transfer_2026_09_27/SEQUENTIAL_CONTROL_PROTOCOL.md",
    "data/preparation_transfer_2026_09_27/SEQUENTIAL_EVALUATION.json",
    "data/preparation_transfer_2026_09_27/SEQUENTIAL_FROZEN_PREDICTIONS.json",
    "data/preparation_transfer_2026_09_27/SEQUENTIAL_PREDICTION_FREEZE.json",
    "data/preparation_transfer_2026_09_27/SOURCE_ELIGIBILITY.json",
    "data/preparation_transfer_2026_09_27/SOURCE_ELIGIBILITY.md",
    "data/preparation_transfer_2026_09_27/SOURCE_IDENTITIES.json",
    "data/preparation_transfer_2026_09_27/TARGET_ACCESS_RELEASE.json",
    "data/preparation_transfer_2026_09_27/calibration_fits.json",
    "data/preparation_transfer_2026_09_27/calibration_raw.npz",
    "data/preparation_transfer_2026_09_27/echo_FROZEN_PREDICTIONS.json",
    "data/preparation_transfer_2026_09_27/echo_PREDICTION_FREEZE.json",
    "data/preparation_transfer_2026_09_27/echo_PROTOCOL.md",
    "data/preparation_transfer_2026_09_27/echo_SOURCE_ELIGIBILITY.json",
    "data/preparation_transfer_2026_09_27/echo_SOURCE_ELIGIBILITY.md",
    "data/preparation_transfer_2026_09_27/echo_SOURCE_IDENTITIES.json",
    "data/preparation_transfer_2026_09_27/echo_TARGET_ACCESS_RELEASE.json",
    "data/preparation_transfer_2026_09_27/echo_evaluation.json",
    "data/preparation_transfer_2026_09_27/echo_raw.npz",
    "data/preparation_transfer_2026_09_27/evaluation.json",
    "data/preparation_transfer_2026_09_27/historical_calibrate_and_freeze.txt",
    "data/preparation_transfer_2026_09_27/historical_echo_evaluate_frozen.txt",
    "data/preparation_transfer_2026_09_27/historical_echo_freeze_predictions.txt",
    "data/preparation_transfer_2026_09_27/historical_evaluate_frozen.txt",
    "data/preparation_transfer_2026_09_27/historical_sequential_control.txt",
    "data/preparation_transfer_2026_09_27/provenance.json",
    "data/preparation_transfer_2026_09_27/ramsey_raw.npz",
    "data/preparation_transfer_2026_09_27/sequential_control_fits.json"
]
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/preparation_transfer_2026_09_27"
PROVENANCE_SHA = "2775422eac8bf64bddb794e005c089bd456da17c64b103f353b021709eefbb0c"


def closed(rates, times_s, initial, swap=False):
    """Column populations, rates per microsecond; instantaneous ideal 1/2 swap."""
    times = np.asarray(times_s) * 1e6
    a, c, direct = rates
    b = c + direct
    def step(t, u):
        difference = b - a
        if difference == 0:
            transfer = t * np.exp(-a * t)
        elif difference > 0:
            transfer = np.exp(-a * t) * (-np.expm1(-difference * t)) / difference
        else:
            transfer = np.exp(-b * t) * np.expm1(difference * t) / difference
        u2 = u[..., 2] * np.exp(-b * t)
        u1 = u[..., 1] * np.exp(-a * t) + u[..., 2] * c * transfer
        return np.stack([1-u1-u2, u1, u2], axis=-1)
    if swap:
        half = step(times / 2, np.asarray(initial))
        return step(times / 2, half[..., [0, 2, 1]])
    return step(times, np.asarray(initial))


def barycentric(iq):
    """Reconstruct every stored point using the final three reference centroids."""
    out = []
    for gate in iq:
        matrix = np.vstack([gate[-3:].T, np.ones(3)])
        out.append(np.linalg.solve(matrix, np.vstack([gate.T, np.ones(len(gate))])).T)
    return np.array(out)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mutation', choices=['identity', 'units', 'initialprep', 'readout', 'membership', 'swap'])
    args = parser.parse_args()
    checks = []
    def check(label, condition):
        if not bool(condition):
            raise ValueError(label)
        checks.append(label)
    def close(label, actual, expected, tolerance=2e-10):
        a, b = np.asarray(actual), np.asarray(expected)
        check(label, a.shape == b.shape and np.all(np.isfinite(a)) and np.max(np.abs(a-b)) <= tolerance)
    def read(name):
        return json.loads((DATA / name).read_text())
    raw = (DATA/'provenance.json').read_bytes()
    if args.mutation == 'identity':
        raw += b' '
    check('provenance identity', hashlib.sha256(raw).hexdigest() == PROVENANCE_SHA)
    provenance = json.loads(raw)
    for name, digest in sorted(provenance['files'].items()):
        check('input identity '+name, hashlib.sha256((DATA/name).read_bytes()).hexdigest() == digest)
    acquisitions = {}
    for label, filename, count, gates in [('calibration','calibration_raw.npz',197,61),('ramsey','ramsey_raw.npz',380,31),('echo','echo_raw.npz',246,61)]:
        with np.load(DATA/filename, allow_pickle=False) as z:
            iq, t, g = z['raw_IQ'], z['times_s'], z['gates_V']
            mask, refs = z['genuine_mask'].copy(), z['reference_indices']
        if args.mutation == 'membership' and label == 'calibration':
            mask[-1] = True
        check(label+' shape/finite', iq.shape == (gates,count+3,2) and t.shape == (count+3,) and g.shape == (gates,) and np.all(np.isfinite(iq)) and np.all(np.isfinite(t)) and np.all(np.diff(t)>0))
        check(label+' semantic reference exclusion', np.array_equal(mask,np.arange(count+3)<count) and np.array_equal(refs,np.arange(count,count+3)))
        pop = barycentric(iq)
        if args.mutation == 'readout':
            pop[...,1] *= 0.9
        close(label+' independent affine QR readout',pop,independent_readout(iq))
        close(label+' reference identity', pop[:,-3:],np.broadcast_to(np.eye(3),(gates,3,3)))
        close(label+' population sum',pop.sum(axis=-1),np.ones((gates,count+3)))
        acquisitions[label] = dict(times=t[mask],gates=g,pop=pop[:,mask],outside_simplex_fraction=float(np.mean(np.any((pop[:,mask]<0)|(pop[:,mask]>1),axis=-1))))
    close('exact calibration/target gate map', acquisitions['calibration']['gates'][::2],acquisitions['ramsey']['gates'],0)
    # Declared toy controls include zero and degenerate rates; no experimental targets.
    for rates in ([0,0,0],[.2,.1,.1],[.07,.11,.0084]):
        times=np.array([0,1e-8,1e-6,2e-5])
        for initial in ([0,0,1],[0,.5,.5]):
            for swap in (False,True):
                actual=closed(rates,times,initial,swap and args.mutation!='swap')
                close('independent population propagation '+str((rates,initial,swap)), actual,independent_propagate(rates,times,initial,swap=swap))
    results=[]
    for model, fitfile, predfile, evalfile, starts in [
        ('three_rate','calibration_fits.json','FROZEN_TARGET_PREDICTIONS.json','evaluation.json',[[.05,.1,.05],[.2,.2,.2],[1,.1,1]]),
        ('sequential','sequential_control_fits.json','SEQUENTIAL_FROZEN_PREDICTIONS.json','SEQUENTIAL_EVALUATION.json',[[.05,.1],[.2,.2],[1,.1]])]:
        fits=read(fitfile)['fits']; predictions=read(predfile); evaluation=read(evalfile)['results']
        check(model+' exact three starts',len(fits)==3 and [r['start'] for r in fits]==starts)
        close(model+' frozen target times',predictions['target_times_s'],acquisitions['ramsey']['times'],0)
        close(model+' frozen target gates',predictions['target_gates_V'],acquisitions['ramsey']['gates'],0)
        check(model+' complete predictions',len(predictions['predictions'])==3 and len(evaluation)==3)
        best=min(range(3),key=lambda i:fits[i]['cost'])
        for i, fit in enumerate(fits):
            name=model+'/'+str(i);rates=np.array(fit['rates_per_us'])
            check(name+' supplied return/status/bounds',fit['status']=='returned' and fit['success'] is True and rates.shape==(3,) and np.all(np.isfinite(rates)) and np.all((rates>=0)&(rates<=10)) and np.isfinite(fit['optimality']))
            if model=='sequential':check(name+' removed direct channel',rates[2]==0)
            pred=predictions['predictions'][i];anchor=evaluation[i]
            check(name+' start mapping',fit['start']==pred['start']==anchor['start'])
            check(name+' calibration-only selection',pred['selected_by_training_cost']==(i==best))
            close(name+' snapshot rate mapping',rates,pred['rates_per_us'],0)
            r = rates * (1e-6 if args.mutation=='units' else 1)
            cal=closed(r,acquisitions['calibration']['times'],[0,0,1])
            residual=cal[None,:,:]-acquisitions['calibration']['pop']
            cost=float(np.sum(residual**2)/2)
            close(name+' saved calibration cost',cost,fit['cost'],2e-9)
            initial=[0,0,1] if args.mutation=='initialprep' else [0,.5,.5]
            target=closed(r,acquisitions['ramsey']['times'],initial)
            close(name+' independent all calibration times',cal,independent_propagate(rates,acquisitions['calibration']['times'],[0,0,1]))
            close(name+' independent all target times',target,independent_propagate(rates,acquisitions['ramsey']['times'],[0,.5,.5]))
            population=target[:,1:].sum(axis=1)
            close(name+' frozen target predictions',population,pred['target_Pexc'])
            delta=population[None,:]-acquisitions['ramsey']['pop'][...,1:].sum(axis=-1)
            rms=float(np.sqrt(np.mean(delta**2)));mean=float(delta.mean())
            close(name+' saved descriptive RMS',rms,anchor['rms'])
            close(name+' saved descriptive mean',mean,anchor['mean_residual'])
            results.append(dict(model=model,start=fit['start'],rates_per_us=rates.tolist(),selected_by_calibration_cost=i==best,calibration_cost=cost,calibration_rms=float(np.sqrt(np.mean(residual**2))),target_rms=rms,target_mean_residual=mean,target_max_abs=float(abs(delta).max()),target_count=delta.size,optimizer_message=fit['message'],optimality=fit['optimality'],jacobian_singular_values=fit['jacobian_singular_values']))
    echo_predictions=read('echo_FROZEN_PREDICTIONS.json')
    echo_evaluation=read('echo_evaluation.json')
    close('Echo frozen times',echo_predictions['times_s'],acquisitions['echo']['times'],0)
    close('Echo frozen gates',echo_predictions['gates_V'],acquisitions['echo']['gates'],0)
    close('Echo calibration gate match',acquisitions['echo']['gates'],acquisitions['calibration']['gates'],0)
    key=lambda r:(r['model'],tuple(r['start']),r['swap'])
    expected={(('full' if r['model']=='three_rate' else 'sequential'),tuple(r['start']),swap) for r in results for swap in [False,True]}
    echo_rows=echo_predictions['predictions']; echo_anchors=echo_evaluation['results']
    check('Echo exact twelve frozen keys',len(echo_rows)==12 and {key(r) for r in echo_rows}==expected)
    check('Echo exact twelve comparison keys',len(echo_anchors)==12 and {key(r) for r in echo_anchors}==expected)
    echo_results=[]
    for row in echo_rows:
        label='Echo/'+str(key(row))
        supplied=next(r for r in results if ('full' if r['model']=='three_rate' else 'sequential')==row['model'] and r['start']==row['start'])
        close(label+' unchanged calibration rates',row['rates_per_us'],supplied['rates_per_us'],0)
        target=closed(row['rates_per_us'],acquisitions['echo']['times'],[0,.5,.5],swap=row['swap'])
        close(label+' independent all times',target,independent_propagate(row['rates_per_us'],acquisitions['echo']['times'],[0,.5,.5],swap=row['swap']))
        population=target[:,1:].sum(axis=-1)
        close(label+' frozen whole curve',population,row['Pexc'])
        delta=population[None,:]-acquisitions['echo']['pop'][...,1:].sum(axis=-1)
        anchor=next(r for r in echo_anchors if key(r)==key(row))
        rms=float(np.sqrt(np.mean(delta**2)));mean=float(delta.mean())
        close(label+' saved descriptive RMS',rms,anchor['rms'])
        close(label+' saved descriptive mean',mean,anchor['mean_residual'])
        close(label+' saved per-gate RMS',np.sqrt(np.mean(delta**2,axis=1)),anchor['per_gate_rms'])
        close(label+' saved mean residual by time',delta.mean(axis=0),anchor['mean_residual_by_time'])
        echo_results.append(dict(model=row['model'],start=row['start'],swap=row['swap'],target_rms=rms,target_mean_residual=mean,target_max_abs=float(abs(delta).max()),target_count=delta.size,first_last_prediction=population[[0,-1]].tolist(),selected_by_calibration_cost=supplied['selected_by_calibration_cost']))
    close('Echo saved observed endpoints',acquisitions['echo']['pop'][...,1:].sum(axis=-1).mean(axis=0)[[0,-1]],echo_evaluation['observed_first_last_mean'])
    no_decay=1-acquisitions['ramsey']['pop'][...,1:].sum(axis=-1)
    baseline=float(np.sqrt(np.mean(no_decay**2)))
    close('saved no-decay descriptive RMS',baseline,read('NO_DECAY_CONTROL.json')['rms'])
    scientific=['echo_raw.npz','echo_FROZEN_PREDICTIONS.json','echo_evaluation.json','calibration_raw.npz','ramsey_raw.npz','calibration_fits.json','sequential_control_fits.json','FROZEN_TARGET_PREDICTIONS.json','SEQUENTIAL_FROZEN_PREDICTIONS.json','evaluation.json','SEQUENTIAL_EVALUATION.json','NO_DECAY_CONTROL.json']
    print(json.dumps(dict(scope='Conditional classical-rate/Lindblad-population transfer, supplied six rate snapshots. No optimizer reproduction, coherence test, statistical preference, native TOE or experimental error-bar claim.',echo_scope='All twelve fixed-rate swap/no-swap transfers retained, including the large Echo mismatch. No target fit or factor-of-two retuning. Total-time and instantaneous-pulse conventions are conditional.',scientific_reads=scientific,integrity_reads=['provenance.json']+sorted(provenance['files']),checks=checks,results=results,echo_results=echo_results,no_decay_rms=baseline,outside_simplex={k:v['outside_simplex_fraction'] for k,v in acquisitions.items()}),sort_keys=True,indent=2,allow_nan=False))
    print('TOTAL: PASS='+str(len(checks))+' FAIL=0')


if __name__ == '__main__':
    main()
