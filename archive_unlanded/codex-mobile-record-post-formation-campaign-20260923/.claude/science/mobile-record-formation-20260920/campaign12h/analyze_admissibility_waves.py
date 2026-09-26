#!/usr/bin/env python3
"""Compare complete-path averages with the frozen, unfitted nonlinear PDE.

Pointwise intervals describe Monte Carlo sampling only. They are not joint
confidence bands and contain neither continuum truncation nor finite-size bias.
"""
from pathlib import Path
import hashlib,json
import numpy as np

HERE=Path(__file__).resolve().parent
DEST=HERE/'admissibility_wave_screen'
SEED=2026092232


def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def analyze(case,plan,reference):
    name=case['case'];path=DEST/f'{name}.npz'
    assert sha(path)==case['raw_sha256']
    metadata=json.loads(path.with_suffix('.json').read_text())
    assert sha(path.with_suffix('.json'))==case['metadata_sha256']
    assert metadata['source_sha256']==plan['simulator_sha256']
    j=metadata['birth_j'];L=metadata['sides'][0]
    targetpath=HERE/'admissibility_wave_continuum_targets'/f'j{int(10*j):02d}.npz'
    ref=next(row for row in reference['cases'] if row['j']==j)
    assert sha(targetpath)==ref['raw_sha256']
    output=DEST/f'{name}_continuum_analysis.json'
    identities=dict(raw_sha256=sha(path),metadata_sha256=sha(path.with_suffix('.json')),
        target_sha256=sha(targetpath),analysis_sha256=sha(Path(__file__)),
        target_source_sha256=reference['source_sha256'],plan_sha256=sha(DEST/'PLAN.json'))
    if output.exists():
        old=json.loads(output.read_text());assert old['identities']==identities
        return old
    data=np.load(path);target=np.load(targetpath)
    times=data['times']/L;prediction=target['fields']
    assert np.max(np.abs(times-target['times']))<1e-13
    fields=data['fields']/np.sqrt(L**3);n=len(fields)
    assert fields.shape[1:]==prediction.shape==(65,4,6)
    assert metadata['density_modulation']==dict(amplitude=.04,mode=[1,0,0])
    assert plan['density_amplitude']==.04 and abs(L*metadata['epsilon']-.04)<1e-14
    assert metadata['u']==0 and metadata['E']==.5 and metadata['floor_or_K']==.05
    name_seed=int.from_bytes(hashlib.sha256(name.encode()).digest()[:4],'little')
    rng=np.random.default_rng(np.random.SeedSequence([SEED,name_seed]))
    weights=rng.multinomial(n,np.full(n,1/n),size=4000)/n
    average=fields.mean(axis=0);se=fields.std(axis=0,ddof=1)/np.sqrt(n)
    bootstrap=(weights@fields.reshape(n,-1)).reshape((4000,)+prediction.shape)
    real_interval=np.quantile(bootstrap.real,[.025,.975],axis=0)
    imag_interval=np.quantile(bootstrap.imag,[.025,.975],axis=0)
    chosen=[('mean_density',0,0,'real'),('density_mode1',1,0,'real'),
            ('longitudinal_mode1',1,1,'imag'),('density_mode2',2,0,'real'),
            ('mean_quadrupole_xx_minus_yy',0,4,'real'),
            ('quadrupole_mode2',2,4,'real')]
    summaries={}
    for label,mode,field,part in chosen:
        values=getattr(fields[:,:,mode,field],part)
        mean=getattr(average[:,mode,field],part)
        truth=getattr(prediction[:,mode,field],part)
        interval=(real_interval if part=='real' else imag_interval)[:,:,mode,field]
        standard_error=values.std(axis=0,ddof=1)/np.sqrt(n)
        difference=mean-truth
        # Time indices depend only on the already frozen continuum target.
        index=int(np.argmin(truth)) if label=='density_mode1' else int(np.argmax(abs(truth-truth[0])))
        summaries[label]=dict(mode=mode,field=field,component=part,
            rms_deviation=float(np.sqrt(np.mean(difference**2))),
            maximum_absolute_deviation=float(np.max(abs(difference))),
            largest_sampling_se=float(np.max(standard_error)),
            target_selected_time=float(times[index]),target_at_time=float(truth[index]),
            mean_at_time=float(mean[index]),pointwise_95_interval=interval[:,index].tolist(),
            target_at_final_time=float(truth[-1]),mean_at_final_time=float(mean[-1]),
            final_pointwise_95_interval=interval[:,-1].tolist())
    # A paired complete-path bootstrap for the joint first-mode RMS discrepancy.
    target_components=np.stack((prediction[:,1,0].real,prediction[:,1,1].imag),axis=-1)
    boot_components=np.stack((bootstrap[:,:,1,0].real,bootstrap[:,:,1,1].imag),axis=-1)
    rms_samples=np.sqrt(np.mean((boot_components-target_components)**2,axis=(1,2)))
    firstmode=np.stack((average[:,1,0].real,average[:,1,1].imag),axis=-1)
    result=dict(case=name,side=L,j=j,trajectories=n,identities=identities,
        base_seed=SEED,name_seed=name_seed,bootstrap_resamples=4000,summaries=summaries,
        joint_density_longitudinal_mode1_rms=float(np.sqrt(np.mean((firstmode-target_components)**2))),
        joint_rms_pointwise_bootstrap_interval=np.quantile(rms_samples,[.025,.975]).tolist(),
        initial_density_mode1_target=.02,initial_density_mode1_measured=float(average[0,1,0].real),
        maximum_absolute_unforced_transverse_mean=float(np.max(abs(average[:,:,2:4]))),
        scope='Unfitted full six-species nonlinear continuum comparison. Complete-path percentile intervals are pointwise Monte Carlo uncertainty only; no PDE existence, finite-size error bound or convergence proof is inferred.')
    archive=DEST/f'{name}_continuum_analysis.npz'
    np.savez_compressed(archive,times=times,mean=average,target=prediction,
        real_interval=real_interval,imag_interval=imag_interval,
        sampling_standard_error_real=fields.real.std(axis=0,ddof=1)/np.sqrt(n),
        sampling_standard_error_imag=fields.imag.std(axis=0,ddof=1)/np.sqrt(n),
        joint_rms_bootstrap=rms_samples)
    result['analysis_npz_sha256']=sha(archive)
    output.write_text(json.dumps(result,indent=2)+'\n')
    return result


def main():
    plan=json.loads((DEST/'PLAN.json').read_text())
    ref=json.loads((HERE/'ADMISSIBILITY_WAVE_CONTINUUM_TARGETS.json').read_text())
    assert ref['source_sha256']==sha(HERE/'admissibility_wave_continuum.py')
    results=[]
    for case in json.loads((DEST/'COMPLETED_CASES.json').read_text()):
        if case['status']!='completed': continue
        result=analyze(case,plan,ref);results.append(result)
        print(json.dumps({key:result[key] for key in ['case','side','j','trajectories',
            'joint_density_longitudinal_mode1_rms','summaries']}),flush=True)
    (DEST/'CONTINUUM_ANALYSIS.json').write_text(json.dumps(results,indent=2)+'\n')


if __name__=='__main__': main()
