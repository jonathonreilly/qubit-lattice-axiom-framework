#!/usr/bin/env python3
"""Whole-trajectory bootstrap of the declared stationary correlation screen."""
from pathlib import Path
import hashlib
import json
import numpy as np
from scipy.optimize import least_squares

HERE=Path(__file__).resolve().parent
GROUPS={'axis':[0,1,2],'face':[3,4,5,6,7,8],'body':[9,10,11,12]}


def fit(times, values, k, initial=None):
    def residual(parameters):
        amplitude, speed, damping=parameters
        predicted=amplitude*np.exp(-damping*k*k*times-1j*speed*k*times)
        error=predicted-values
        return np.r_[error.real,error.imag]
    solution=least_squares(residual, [1,1/np.sqrt(6),.7] if initial is None else initial,
                           bounds=([0,0,0],[3,2,12]),max_nfev=400,
                           ftol=1e-9,xtol=1e-9,gtol=1e-9)
    return solution.x, bool(solution.success), float(np.max(abs(residual(solution.x))))


def main():
    directory=HERE/'context_exchange_screen'
    completed=json.loads((directory/'COMPLETED_CASES.json').read_text())
    assert len(completed)==5
    rng=np.random.default_rng(2026092140)
    summary={'scope':'Finite stationary lattices under a supplied context-dependent exchange generator; no microscopic hydrodynamic theorem.',
             'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'uncertainty':'4000 complete-trajectory bootstrap resamples; intervals are pointwise percentiles. Symmetry-related modes are averaged within a path first.',
             'fit_scope':'Exploratory complex-exponential fits over the first predicted half-period, chosen for interpretability after the first two raw screens; 1000 whole-path bootstrap refits. These are phenomenological and can be systematically biased.',
             'reference_speed':float(1/np.sqrt(6)),'cases':[]}
    for case in completed:
        name=case['case'];path=directory/f'{name}.npz'
        assert hashlib.sha256(path.read_bytes()).hexdigest()==case['raw_npz_sha256']
        data=np.load(path);fields=data['fields'];times=data['times'];vectors=data['wavevectors']
        n=len(fields);resamples=rng.multinomial(n,np.full(n,1/n),size=4000)/n
        normalized_density=fields[:,:,:,0]*2
        unit=vectors/np.linalg.norm(vectors,axis=1)[:,None]
        normalized_longitudinal=np.einsum('ntmi,mi->ntm',fields[:,:,:,1:4],unit)*np.sqrt(6)
        plus=(normalized_density+normalized_longitudinal)/np.sqrt(2)
        minus=(normalized_density-normalized_longitudinal)/np.sqrt(2)
        normal_correlations=.5*(plus*plus[:,0,:].conj()[:,None,:]
                                  +(minus*minus[:,0,:].conj()[:,None,:]).conj())
        density_correlations=normalized_density*normalized_density[:,0,:].conj()[:,None,:]
        record={'case':name,'groups':{},'trajectories':n}
        saved={}
        for group,indices in GROUPS.items():
            k=float(np.linalg.norm(vectors[indices[0]]))
            theta=times*k/np.sqrt(6)
            density=density_correlations[:,:,indices].mean(axis=2).real
            normal=normal_correlations[:,:,indices].mean(axis=2)
            density_mean=density.mean(axis=0);normal_mean=normal.mean(axis=0)
            bd=resamples@density;bn=resamples@normal
            dci=np.quantile(bd,[.025,.975],axis=0)
            nrci=np.quantile(bn.real,[.025,.975],axis=0)
            nici=np.quantile(bn.imag,[.025,.975],axis=0)
            j=int(np.argmin(abs(theta-np.pi)))
            selection=theta<=np.pi+1e-12
            parameters,okay,residual=fit(times[selection],normal_mean[selection],k)
            fitted=[];failures=0
            for b in range(1000):
                values,success,_=fit(times[selection],bn[b,selection],k,parameters)
                fitted.append(values);failures+=int(not success)
            pci=np.quantile(np.asarray(fitted),[.025,.975],axis=0)
            r={'wave_number':k,'initial_density_correlation':float(density_mean[0]),
               'predicted_first_minimum_sample_time':float(times[j]),
               'predicted_first_minimum_sample_theta':float(theta[j]),
               'density_at_that_time':float(density_mean[j]),
               'density_pointwise_95_interval':dci[:,j].tolist(),
               'complex_fit':{'amplitude':float(parameters[0]),'speed':float(parameters[1]),
                              'damping':float(parameters[2]),'pointwise_bootstrap_parameter_intervals':pci.T.tolist(),
                              'optimizer_success':okay,'bootstrap_optimizer_failures':failures,
                              'maximum_component_residual':residual,
                              'observation_count':int(selection.sum())}}
            record['groups'][group]=r
            for key,value in {'theta':theta,'density_mean':density_mean,'density_ci':dci,
                              'normal_mean':normal_mean,'normal_real_ci':nrci,'normal_imag_ci':nici,
                              'fit_samples':np.asarray(fitted),'fit_parameters':parameters}.items():
                saved[f'{group}_{key}']=value
        if name=='flat_symmetric_L16':
            theory=np.exp(-.1*np.sum(1-np.cos(vectors),axis=1)[None,:]*times[:,None])
            maximum=0.
            for group,indices in GROUPS.items():
                values=density_correlations[:,:,indices].mean(axis=2).real
                mean=values.mean(axis=0);se=values.std(axis=0,ddof=1)/np.sqrt(n)
                target=theory[:,indices].mean(axis=1)
                maximum=max(maximum,float(np.max(abs(mean-target)/np.maximum(se,1e-12))))
            record['flat_diffusion_control_max_estimated_SE']=maximum
        np.savez_compressed(directory/f'{name}_analysis.npz',times=times,**saved)
        summary['cases'].append(record)
        (HERE/'CONTEXT_EXCHANGE_SCREEN_ANALYSIS.json').write_text(json.dumps(summary,indent=2)+'\n')
        print(json.dumps(record),flush=True)


if __name__=='__main__':
    main()
