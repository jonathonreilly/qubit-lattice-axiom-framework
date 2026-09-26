#!/usr/bin/env python3
"""Stable per-case whole-trajectory analysis for the declared later screens."""
from pathlib import Path
import argparse
import hashlib
import json
import numpy as np
from analyze_context_exchange import fit, GROUPS

HERE=Path(__file__).resolve().parent


def analyze(directory,case,seed):
    name=case['case'];path=directory/f'{name}.npz'
    metadata=json.loads(path.with_suffix('.json').read_text())
    if metadata['epsilon']!=0: return None
    rawsha=hashlib.sha256(path.read_bytes()).hexdigest()
    assert rawsha==case['raw_npz_sha256']
    source=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    fit_source=hashlib.sha256((HERE/'analyze_context_exchange.py').read_bytes()).hexdigest()
    resultpath=directory/f'{name}_stationary_analysis.json'
    if resultpath.exists():
        saved=json.loads(resultpath.read_text())
        assert saved['raw_npz_sha256']==rawsha and saved['analysis_source_sha256']==source
        assert saved['fit_source_sha256']==fit_source and saved['base_seed']==seed
        return saved
    rho=1-metadata['probabilities'][0]
    reference=case.get('reference_speed',1/np.sqrt(6))
    data=np.load(path);fields=data['fields'];times=data['times'];vectors=data['wavevectors']
    n=len(fields)
    name_seed=int.from_bytes(hashlib.sha256(name.encode()).digest()[:4],'little')
    rng=np.random.default_rng(np.random.SeedSequence([seed,name_seed]))
    resamples=rng.multinomial(n,np.full(n,1/n),size=4000)/n
    density=fields[:,:,:,0]/np.sqrt(rho*(1-rho))
    unit=vectors/np.linalg.norm(vectors,axis=1)[:,None]
    longitudinal=np.einsum('ntmi,mi->ntm',fields[:,:,:,1:4],unit)/np.sqrt(rho/3)
    plus=(density+longitudinal)/np.sqrt(2);minus=(density-longitudinal)/np.sqrt(2)
    normal_correlations=.5*(plus*plus[:,0,:].conj()[:,None,:]
                              +(minus*minus[:,0,:].conj()[:,None,:]).conj())
    density_correlations=density*density[:,0,:].conj()[:,None,:]
    record={'case':name,'rho':rho,'reference_speed':reference,'groups':{},'trajectories':n,
            'raw_npz_sha256':rawsha,'analysis_source_sha256':source,'fit_source_sha256':fit_source,
            'base_seed':seed,'name_seed':name_seed,
            'uncertainty':'4000 complete-path bootstrap samples; symmetry modes averaged within each path; pointwise percentile intervals',
            'fit_scope':'Complex damped exponential over first predicted half-period; 1000 complete-path bootstrap refits. Conditional fit intervals omit model error.'}
    saved={}
    for group,indices in GROUPS.items():
        k=float(np.linalg.norm(vectors[indices[0]]));theta=times*k*reference
        dc=density_correlations[:,:,indices].mean(axis=2).real
        nc=normal_correlations[:,:,indices].mean(axis=2)
        dm=dc.mean(axis=0);nm=nc.mean(axis=0)
        bd=resamples@dc;bn=resamples@nc
        dci=np.quantile(bd,[.025,.975],axis=0)
        nrci=np.quantile(bn.real,[.025,.975],axis=0)
        nici=np.quantile(bn.imag,[.025,.975],axis=0)
        j=int(np.argmin(abs(theta-np.pi)));selection=theta<=np.pi+1e-12
        parameters,okay,residual=fit(times[selection],nm[selection],k,[1,reference,.7])
        fitted=[];failures=0
        for b in range(1000):
            values,success,_=fit(times[selection],bn[b,selection],k,parameters)
            fitted.append(values);failures+=int(not success)
        pci=np.quantile(np.asarray(fitted),[.025,.975],axis=0)
        record['groups'][group]={'wave_number':k,'initial_density_correlation':float(dm[0]),
            'predicted_first_minimum_sample_time':float(times[j]),'predicted_first_minimum_sample_theta':float(theta[j]),
            'density_at_that_time':float(dm[j]),'density_pointwise_95_interval':dci[:,j].tolist(),
            'complex_fit':{'amplitude':float(parameters[0]),'speed':float(parameters[1]),'damping':float(parameters[2]),
                'pointwise_bootstrap_parameter_intervals':pci.T.tolist(),'optimizer_success':okay,
                'bootstrap_optimizer_failures':failures,'maximum_component_residual':residual,'observation_count':int(selection.sum())}}
        for key,value in {'theta':theta,'density_mean':dm,'density_ci':dci,'normal_mean':nm,
                          'normal_real_ci':nrci,'normal_imag_ci':nici,'fit_samples':np.asarray(fitted),
                          'fit_parameters':parameters}.items(): saved[f'{group}_{key}']=value
    outnpz=directory/f'{name}_stationary_analysis.npz'
    np.savez_compressed(outnpz,times=times,**saved)
    record['analysis_npz_sha256']=hashlib.sha256(outnpz.read_bytes()).hexdigest()
    resultpath.write_text(json.dumps(record,indent=2)+'\n')
    return record


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--directory',type=Path,required=True)
    parser.add_argument('--seed',type=int,required=True)
    args=parser.parse_args()
    cases=json.loads((args.directory/'COMPLETED_CASES.json').read_text())
    summary=[]
    for case in cases:
        result=analyze(args.directory,case,args.seed)
        if result is not None:
            summary.append(result)
            print(json.dumps({'case':result['case'],'reference_speed':result['reference_speed'],
                'groups':result['groups']}),flush=True)
    (args.directory/'STATIONARY_ANALYSIS.json').write_text(json.dumps(summary,indent=2)+'\n')


if __name__=='__main__': main()
