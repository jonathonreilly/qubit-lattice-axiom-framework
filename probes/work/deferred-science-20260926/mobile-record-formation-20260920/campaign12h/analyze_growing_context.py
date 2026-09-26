#!/usr/bin/env python3
"""Growing homogeneous product: full six-species response and path bootstrap.

The continuum target is not an exact finite-lattice correlation. No stationary
speed is fitted. The response matrix retains both quadrupole degrees of freedom.
"""
from pathlib import Path
import argparse
import hashlib
import json
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm

HERE=Path(__file__).resolve().parent
VECTORS=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],dtype=float)
TRANSFORM=np.vstack((np.ones(6),VECTORS.T,
    VECTORS[:,0]**2-VECTORS[:,1]**2,
    VECTORS[:,0]**2+VECTORS[:,1]**2-2*VECTORS[:,2]**2))
GROUPS={'axis':[0,1,2],'face':[3,4,5,6,7,8],'body':[9,10,11,12]}


def probabilities(t,p_initial,beta):
    p0=1-p_initial.sum()
    return p_initial+p0*(-np.expm1(-6*beta*t))/6


def current(p,axis,model,u=-1.,coupling=1.,alpha=1.):
    f=VECTORS[:,axis];rho=p.sum();g=p@f
    if model=='occupation':
        F=u+2*coupling*rho;G=2*coupling*(1-rho)-F
        return p*(F*f+G*g)
    s=2-3*f*f;S=p@s
    return alpha*p*(S*f+(s-2*S)*g)


def jacobian(p,axis,model,u=-1.,coupling=1.,alpha=1.):
    f=VECTORS[:,axis];rho=p.sum();g=p@f
    if model=='occupation':
        F=u+2*coupling*rho;G=2*coupling*(1-rho)-F
        return np.diag(F*f+G*g)+p[:,None]*(2*coupling*f[:,None]-4*coupling*g+G*f[None,:])
    s=2-3*f*f;S=p@s
    return alpha*(np.diag(S*f+(s-2*S)*g)+p[:,None]*(
        f[:,None]*s[None,:]+(s[:,None]-2*S)*f[None,:]-2*g*s[None,:]))


def susceptibility(p): return np.diag(p)-np.outer(p,p)


def target(times,K,p_initial,beta,model,u=-1.,coupling=1.,alpha=1.):
    def rhs(t,flat):
        p=probabilities(t,p_initial,beta)
        A=sum(K[i]*jacobian(p,i,model,u,coupling,alpha) for i in range(3))
        B=-1j*A-beta*np.ones((6,6))
        return (B@flat.reshape(6,6)).ravel()
    solution=solve_ivp(rhs,(times[0],times[-1]),np.eye(6,dtype=complex).ravel(),
        t_eval=times,method='DOP853',rtol=1e-11,atol=1e-13)
    assert solution.success
    return solution.y.T.reshape(-1,6,6)


def controls():
    rng=np.random.default_rng(2026092192);jacerr=entropyerr=lyaperr=0.
    for model in ('occupation','balanced'):
        for _ in range(20):
            p=rng.dirichlet(np.ones(7))[1:];C=susceptibility(p);beta=.07
            for axis in range(3):
                A=jacobian(p,axis,model)
                numeric=np.column_stack([(current(p+1e-6*np.eye(6)[b],axis,model)
                    -current(p-1e-6*np.eye(6)[b],axis,model))/(2e-6) for b in range(6)])
                jacerr=max(jacerr,float(np.max(abs(A-numeric))))
                entropyerr=max(entropyerr,float(np.max(abs(A@C-C@A.T))))
                B=-1j*A-beta*np.ones((6,6));p0=1-p.sum()
                derivative=beta*p0*(np.eye(6)-p[:,None]-p[None,:])
                lyaperr=max(lyaperr,float(np.max(abs(B@C+C@B.conj().T+beta*p0*np.eye(6)-derivative))))
    assert jacerr<1e-8 and entropyerr<1e-13 and lyaperr<1e-13
    p=np.full(6,1/12);times=np.linspace(0,2.5,41);K=2*np.pi*np.array([1,1,1])
    stationary=target(times,K,p,0.,'occupation')
    A=sum(K[i]*jacobian(p,i,'occupation') for i in range(3))
    constant_error=max(float(np.max(abs(stationary[j]-expm(-1j*A*t)))) for j,t in enumerate(times))
    assert constant_error<2e-10
    balanced=target(times,K,p,.04,'balanced')
    normK=np.linalg.norm(K);direction=K/normK
    field=np.vstack((np.ones(6),VECTORS@direction));right=field.T@np.linalg.inv(field@field.T)
    def reduced_rhs(t,flat):
        rho=probabilities(t,p,.04).sum()
        B=np.array([[-.24,-1j*normK*2*rho*(1-rho)],[-1j*normK*2*rho/3,0.]])
        return (B@flat.reshape(2,2)).ravel()
    reduced=solve_ivp(reduced_rhs,(0,times[-1]),np.eye(2,dtype=complex).ravel(),
        t_eval=times,method='DOP853',rtol=1e-12,atol=1e-14)
    reduced_error=float(np.max(abs(np.einsum('ab,tbc,cd->tad',field,balanced,right)
        -reduced.y.T.reshape(-1,2,2))))
    assert reduced_error<2e-10
    return {'max_finite_difference_jacobian_error':jacerr,'max_entropy_symmetry_residual':entropyerr,
        'max_growing_covariance_Lyapunov_residual':lyaperr,'stationary_matrix_exponential_error':constant_error,
        'balanced_full_six_vs_closed_two_field_error':reduced_error,
        'scope':'Deterministic response controls, not a microscopic limit theorem or simulation goodness-of-fit test.'}


def analyze(directory,case,seed):
    name=case['case'];path=directory/f'{name}.npz'
    meta=json.loads(path.with_suffix('.json').read_text())
    if meta['epsilon']==0: return None
    model='balanced' if meta.get('context_feature') else 'occupation'
    assert 'balanced' not in name or model=='balanced'
    source=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    rawsha=hashlib.sha256(path.read_bytes()).hexdigest();assert rawsha==case['raw_npz_sha256']
    output=directory/f'{name}_growing_analysis.json'
    if output.exists():
        old=json.loads(output.read_text())
        assert old['source_sha256']==source and old['raw_npz_sha256']==rawsha and old['base_seed']==seed
        return old
    data=np.load(path);fields=data['fields'];times=data['times'];vectors=data['wavevectors'];n=len(fields)
    L=meta['sides'][0];assert meta['sides']==[L]*3
    tau=times/L;beta=L*meta['epsilon'];p=np.asarray(meta['probabilities'][1:]);C0=susceptibility(p)
    rho=p.sum();assert np.max(abs(p-rho/6))<1e-12
    predictions=[]
    for vector in vectors:
        M=target(tau,L*vector,p,beta,model,meta['u'],meta['E'],2*meta['E'])
        predictions.append(np.einsum('ab,tbc,cd,de->tae',TRANSFORM,M,C0,TRANSFORM.T))
    predictions=np.stack(predictions,axis=1)
    direction=vectors/np.linalg.norm(vectors,axis=1)[:,None]
    density=fields[:,:,:,0]/np.sqrt(rho*(1-rho))
    longitudinal=np.einsum('ntmi,mi->ntm',fields[:,:,:,1:4],direction)/np.sqrt(rho/3)
    observables={'density':density*density[:,0,:].conj()[:,None,:],
        'longitudinal':longitudinal*longitudinal[:,0,:].conj()[:,None,:],
        'density_to_longitudinal':longitudinal*density[:,0,:].conj()[:,None,:],
        'longitudinal_to_density':density*longitudinal[:,0,:].conj()[:,None,:]}
    theoretical={'density':predictions[:,:,0,0]/(rho*(1-rho)),
        'longitudinal':np.einsum('mi,tmij,mj->tm',direction,predictions[:,:,1:4,1:4],direction)/(rho/3),
        'density_to_longitudinal':np.einsum('mi,tmi->tm',direction,predictions[:,:,1:4,0])/np.sqrt(rho**2*(1-rho)/3),
        'longitudinal_to_density':np.einsum('tmj,mj->tm',predictions[:,:,0,1:4],direction)/np.sqrt(rho**2*(1-rho)/3)}
    name_seed=int.from_bytes(hashlib.sha256(name.encode()).digest()[:4],'little')
    rng=np.random.default_rng(np.random.SeedSequence([seed,name_seed]))
    resamples=rng.multinomial(n,np.full(n,1/n),size=4000)/n
    saved={'times':times,'macro_times':tau,'full_six_field_target':predictions}
    record={'case':name,'model':model,'side':L,'trajectories':n,'microscopic_per_label_birth_rate':meta['epsilon'],
        'macroscopic_per_label_birth_rate':beta,'raw_npz_sha256':rawsha,'source_sha256':source,
        'base_seed':seed,'name_seed':name_seed,'groups':{},
        'interpretation':'Unfitted six-field Euler reaction-current target, compared with finite-lattice data. Differences include finite-size damping and noise; these intervals do not make the target an exact finite-size law.',
        'uncertainty':'4000 complete-path bootstrap samples, symmetry modes averaged within a path; pointwise percentile intervals.'}
    for group,indices in GROUPS.items():
        record['groups'][group]={}
        for observable,raw in observables.items():
            samples=raw[:,:,indices].mean(axis=2);mean=samples.mean(axis=0)
            bs=resamples@samples;ci_real=np.quantile(bs.real,[.025,.975],axis=0)
            ci_imag=np.quantile(bs.imag,[.025,.975],axis=0)
            theory=theoretical[observable][:,indices].mean(axis=1)
            se_real=samples.real.std(axis=0,ddof=1)/np.sqrt(n)
            se_imag=samples.imag.std(axis=0,ddof=1)/np.sqrt(n)
            record['groups'][group][observable]={'max_absolute_mean_minus_continuum':float(np.max(abs(mean-theory))),
                'RMS_mean_minus_continuum':float(np.sqrt(np.mean(abs(mean-theory)**2))),
                'time_of_continuum_density_minimum':float(tau[np.argmin(theoretical['density'][:,indices].mean(axis=1).real)])}
            if observable=='density':
                j=int(np.argmin(theory.real))
                record['groups'][group][observable].update({'density_at_continuum_minimum':float(mean[j].real),
                    'pointwise_95_interval_at_that_time':ci_real[:,j].tolist(),
                    'continuum_density_at_that_time':float(theory[j].real)})
            prefix=f'{group}_{observable}'
            for key,value in {'mean':mean,'ci_real':ci_real,'ci_imag':ci_imag,'theory':theory,
                              'se_real':se_real,'se_imag':se_imag}.items(): saved[f'{prefix}_{key}']=value
    stats=data['statistics'];V=L**3;p0_final=(1-rho)*np.exp(-6*beta*tau[-1])
    final=stats[:,5]/V
    record['birth_counts']={'exact_final_vacancy_fraction':float(p0_final),
        'mean_final_vacancy_fraction':float(final.mean()),'estimated_SE':float(final.std(ddof=1)/np.sqrt(n)),
        'mean_births_per_site':float(np.mean(stats[:,3]/V))}
    outnpz=directory/f'{name}_growing_analysis.npz';np.savez_compressed(outnpz,**saved)
    record['analysis_npz_sha256']=hashlib.sha256(outnpz.read_bytes()).hexdigest()
    output.write_text(json.dumps(record,indent=2)+'\n');return record


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--directory',type=Path,required=True)
    parser.add_argument('--seed',type=int,default=2026092193);args=parser.parse_args()
    checks=controls();print(json.dumps({'controls':checks}),flush=True)
    cases=json.loads((args.directory/'COMPLETED_CASES.json').read_text());summary=[]
    for case in cases:
        result=analyze(args.directory,case,args.seed)
        if result:
            summary.append(result);print(json.dumps(result),flush=True)
    (args.directory/'GROWING_ANALYSIS.json').write_text(json.dumps({'controls':checks,'cases':summary},indent=2)+'\n')


if __name__=='__main__': main()
