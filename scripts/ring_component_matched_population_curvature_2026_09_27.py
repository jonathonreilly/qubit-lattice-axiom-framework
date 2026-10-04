#!/usr/bin/env python3
"""Rebuild and reproduce the fixed matched finite-population curvature diagnostic.

Every population/scheme uses the same specified canonical state and exact same
seed protocol. This is a reproduction of a completed fixed design, not a fresh
statistical confirmation. Full replica covariance is used; SE is descriptive.
No private data, input arrays or observed laboratory values are read.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
import json,time,hashlib,argparse
import numpy as np
import ring_matched_population_kernel_2026_09_27 as kernel
import ring_matched_population_reference_2026_09_27 as reference
import finite_projection_mixed_curvature_2026_09_27 as target_parent

AUDIT_TIMEOUT_SEC = 14400
AUDIT_INPUT_PATHS = ('docs/FINITE_PROJECTION_MIXED_ENERGY_AND_CURVATURE_TARGET_BOUNDED_THEOREM_NOTE_2026-09-27.md', 'docs/RING_COMPONENT_MATCHED_POPULATION_CURVATURE_DIAGNOSTIC_BOUNDED_THEOREM_NOTE_2026-09-27.md', 'scripts/finite_projection_mixed_curvature_2026_09_27.py', 'scripts/ring_matched_population_kernel_2026_09_27.py', 'scripts/ring_matched_population_reference_2026_09_27.py')


def summarize(A,ref):
    R=len(A)
    assert A.shape==(1024,4,2,3)
    weights=np.array([15.,-16.,1.])/(9*8*.15**2);chi=A@weights
    schemes=['common','per_field']
    target=np.array(ref['curvature_targets'])
    # All covariances use complete independent replicate units; never treat walkers or ages as iid.
    covE=np.cov(A.reshape(R,24),rowvar=False,ddof=1);covC=np.cov(chi.reshape(R,8),rowvar=False,ddof=1)
    transform=np.kron(np.eye(8),weights.reshape(1,3));assert np.max(np.abs(transform@covE@transform.T-covC))<1e-11

    def stat(x):
     x=np.asarray(x);return {'mean':float(x.mean()),'replicate_sd':float(x.std(ddof=1)),'mean_se_diagnostic':float(x.std(ddof=1)/np.sqrt(R))}
    rows=[]
    for pi,pop in enumerate([64,128,256,512]):
     for si,scheme in enumerate(schemes):
      row={'population':pop,'scheme':scheme,**stat(chi[:,pi,si]),'finite_age_reference':float(target[si]),'bias_from_reference':stat(chi[:,pi,si]-target[si]),'energy_mean':A[:,pi,si].mean(axis=0).tolist(),'energy_mean_covariance':(covE[(2*pi+si)*3:(2*pi+si+1)*3,(2*pi+si)*3:(2*pi+si+1)*3]/R).tolist()}
      idx=2*pi+si;naive=weights**2@np.diag(covE[idx*3:(idx+1)*3,idx*3:(idx+1)*3])/R
      row['curvature_mean_variance_with_covariance']=float(covC[idx,idx]/R);row['curvature_mean_variance_if_field_covariances_omitted']=float(naive)
      rows.append(row)
    wint=np.array([-.5,.5,1.]);wpred=np.array([-9/28,13/28,6/7]);x=1/np.array([64,128,256,512][:3],float);X=np.stack([np.ones(3),x],axis=1)
    assert np.allclose(np.linalg.pinv(X)[0],wint,atol=1e-14)
    assert np.allclose(np.array([1.,1/512])@np.linalg.pinv(X),wpred,atol=1e-14)
    fit=[]
    for si,scheme in enumerate(schemes):
     intercept=chi[:,:3,si]@wint;prediction=chi[:,:3,si]@wpred
     fit.append({'scheme':scheme,'fixed_fit_populations':[64,128,256,512][:3],'intercept_weights':wint.tolist(),'heldout_prediction_weights':wpred.tolist(),'intercept':stat(intercept),'intercept_minus_finite_age_reference':stat(intercept-target[si]),'heldout_population':512,'heldout_prediction':stat(prediction),'heldout_minus_prediction_paired':stat(chi[:,3,si]-prediction)})
    paired=[{'population':p,'per_field_minus_common':stat(chi[:,j,1]-chi[:,j,0]),'finite_age_reference_difference':float(target[1]-target[0])} for j,p in enumerate([64,128,256,512])]
    return {'replicates':R,'rows':rows,'paired_scheme_differences':paired,'fixed_fit_and_heldout':fit,
            'replicate_energy_covariance':covE.tolist(),'replicate_curvature_covariance':covC.tolist(),
            'replica_summary_sha256':hashlib.sha256(A.tobytes()).hexdigest()}


def calculate(keep_raw=None):
    ice,canon,hv,H,states,F,nf=reference.build()
    ref=reference.reference(H,F,nf)
    if keep_raw is not None:
        keep_raw.mkdir(parents=True,exist_ok=False)
    pops=[64,128,256,512];fields=[0.,.15,.30];R=1024;T=2000
    A=np.empty((R,4,2,3));t=time.monotonic()
    for rep in range(R):
        energies=np.empty((4,2,3,T));logmeans=np.empty_like(energies)
        for pi,pop in enumerate(pops):
            for si in range(2):
                rng=np.random.default_rng(1940000+rep)
                pr=kernel.Projector(ice,np.ones(ice.np_,bool),.2,0.,np.zeros((1,ice.nl),complex),1930000+rep)
                for fi,field in enumerate(fields):
                    guide=.15 if si==0 else field
                    summary,res=kernel.energy_run(pr,[canon],pop,T,.015,500,rng,field*hv,.5*guide*hv,Lcs=(0,))
                    assert res['therm']==500 and res['e'].shape==(T,) and res['lwbar'].shape==(T,)
                    assert np.all(np.isfinite(res['e'])) and np.all(np.isfinite(res['lwbar']))
                    assert abs(summary[0][0]-res['e'][500:].mean())<1e-12
                    energies[pi,si,fi]=res['e'];logmeans[pi,si,fi]=res['lwbar']
        A[rep]=energies[:,:,:,500:].mean(axis=-1)
        if keep_raw is not None:
            np.savez(keep_raw/f'replicate-{rep:03d}.npz',energies=energies,logmean_weights=logmeans,populations=pops,fields=fields,numba_seed=1930000+rep,numpy_seed=1940000+rep)
        if (rep+1)%16==0:print(json.dumps({'completed_replicates':rep+1,'fixed_total':R}),flush=True)
    # Match the earlier completed manifest's deterministic filename order.
    indices=sorted(range(R),key=lambda j:f'replicate-{j:03d}.npz')
    A=A[indices]
    out=summarize(A,ref)
    out.update({'reference':ref,'component_states':len(states),'component_nnz':H.nnz,'population_grid':pops,
                'fields':fields,'generations':T,'retained_indices':[500,2000],'elapsed_seconds':time.monotonic()-t,
                'scope':'Fixed finite numerical diagnostic; same-design reproduction, descriptive replica SE, no certified coverage, population-limit or physical inference.',
                'raw_arrays_retained':keep_raw is not None})
    return out


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--retain-raw',type=Path);args=parser.parse_args()
    print(json.dumps(calculate(args.retain_raw),indent=2),flush=True)
