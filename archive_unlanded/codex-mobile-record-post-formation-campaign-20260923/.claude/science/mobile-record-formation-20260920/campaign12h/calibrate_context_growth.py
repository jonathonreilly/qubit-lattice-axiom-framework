#!/usr/bin/env python3
"""Independent finite generator check of context exchanges with insertion."""
from pathlib import Path
from itertools import product
import hashlib
import json
import numpy as np
import scipy.sparse as sparse
from scipy.sparse.linalg import expm_multiply
from scipy.stats import binom
from context_exchange_sim import run, FIELDS, VECTORS

HERE=Path(__file__).resolve().parent


def exact(probabilities, epsilon):
    states=np.array(list(product(range(7),repeat=4)),dtype=int)
    index={tuple(s):i for i,s in enumerate(states)}
    rows=[];cols=[];rates=[]
    for i,state in enumerate(states):
        for x in range(4):
            l,a,b,r=state[[(x-1)%4,x,(x+1)%4,(x+2)%4]]
            delta_v=int(VECTORS[a,0])-int(VECTORS[b,0])
            delta_n=int(a!=0)-int(b!=0)
            h=-delta_v+delta_v*(int(l!=0)+int(r!=0))+delta_n*(int(VECTORS[l,0])+int(VECTORS[r,0]))
            rate=.05+max(h,0)
            target=state.copy();target[x],target[(x+1)%4]=b,a
            j=index[tuple(target)]
            rows.extend([i,i]);cols.extend([j,i]);rates.extend([rate,-rate])
            if state[x]==0:
                for label in range(1,7):
                    target=state.copy();target[x]=label
                    j=index[tuple(target)]
                    rows.extend([i,i]);cols.extend([j,i]);rates.extend([epsilon,-epsilon])
    Q=sparse.coo_matrix((rates,(rows,cols)),shape=(len(states),len(states))).tocsr()
    mu=np.prod(np.asarray(probabilities)[states],axis=1)
    assert abs(mu.sum()-1)<1e-12
    assert np.max(abs(Q@np.ones(len(states))))<1e-12
    times=np.linspace(0,5,21);modes=np.array([[1],[2]])
    phases=np.exp(-2j*np.pi*np.arange(4)[:,None]*np.array([1,2])[None,:]/4)/2
    observable=np.empty((len(states),4),dtype=complex)
    for mode in range(2):
        for a in range(2): observable[:,2*mode+a]=FIELDS[states,a]@phases[:,mode]
    evolved=expm_multiply(Q,observable,start=0,stop=5,num=len(times),endpoint=True)
    correlations=np.empty((len(times),2,2,2),dtype=complex)
    for mode in range(2):
        for a in range(2):
            for b in range(2):
                correlations[:,mode,a,b]=evolved[:,:,2*mode+a]@(mu*observable[:,2*mode+b].conj())
    forward=expm_multiply(Q.T,mu,start=0,stop=5,num=len(times),endpoint=True)
    error=0.
    for t,law in zip(times,forward):
        pt=np.array(probabilities,dtype=float)
        pt[0]=probabilities[0]*np.exp(-6*epsilon*t)
        pt[1:]+=(probabilities[0]-pt[0])/6
        error=max(error,float(np.max(abs(law-np.prod(pt[states],axis=1)))))
    assert error<2e-12
    return times,modes,correlations,error


def main():
    directory=HERE/'context_growth_calibration';directory.mkdir(exist_ok=True)
    cases=[('isotropic',[.5]+[1/12]*6,2026092160),
           ('biased',(np.array([5,1,2,3,4,5,6])/26).tolist(),2026092161)]
    receipt={'plan_sha256':hashlib.sha256((HERE/'CONTEXT_EXCHANGE_GROWTH_PLAN.md').read_bytes()).hexdigest(),
             'gate':'maximum estimated standardized real/imaginary correlation discrepancy <5.5; stochastic sanity check, not rigorous confidence certification',
             'cases':cases,'simulator_sha256':hashlib.sha256((HERE/'context_exchange_sim.py').read_bytes()).hexdigest(),
             'calibrator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    planpath=directory/'PLAN.json'
    if planpath.exists(): raise RuntimeError('Refusing to overwrite existing calibration')
    planpath.write_text(json.dumps(receipt,indent=2)+'\n')
    results=[];epsilon=.08
    for name,probabilities,seed in cases:
        times,modes,target,product_error=exact(probabilities,epsilon)
        raw,stats,seeds,metadata=run([4],modes,probabilities,times,8192,seed,
                                    -1.,1.,.05,0,epsilon,4)
        raw=raw[:,:,:,:2];standardized=[]
        estimates=np.empty_like(target);errors=np.empty(target.shape+(2,))
        for a in range(2):
            for b in range(2):
                values=raw[:,:,:,a]*raw[:,0,:,b].conj()[:,None,:]
                estimates[:,:,a,b]=values.mean(axis=0)
                for component,transform in enumerate([np.real,np.imag]):
                    sample=transform(values)
                    err=sample.std(axis=0,ddof=1)/np.sqrt(len(sample))
                    errors[:,:,a,b,component]=err
                    delta=sample.mean(axis=0)-transform(target[:,:,a,b])
                    standardized.append(np.max(abs(delta)/np.maximum(err,1e-12)))
        p0final=probabilities[0]*np.exp(-6*epsilon*times[-1])
        frequencies=np.bincount(stats[:,5].astype(int),minlength=5)/len(stats)
        binomial=binom.pmf(np.arange(5),4,p0final)
        variance=np.maximum(binomial*(1-binomial)/len(stats),1e-24)
        count_max=float(np.max(abs(frequencies-binomial)/np.sqrt(variance)))
        maximum=float(max(standardized));passed=maximum<5.5
        np.savez_compressed(directory/f'{name}.npz',fields=raw,statistics=stats,seeds=seeds,
                            exact=target,estimated=estimates,standard_errors=errors,
                            times=times,modes=modes)
        result={'case':name,'passed':passed,'max_estimated_SE':maximum,
                'exact_product_evolution_residual':product_error,
                'final_vacancy_count_frequencies':frequencies.tolist(),
                'exact_final_vacancy_binomial':binomial.tolist(),
                'vacancy_count_max_standardized_residual':count_max,
                'metadata':metadata}
        (directory/f'{name}.json').write_text(json.dumps(result,indent=2)+'\n')
        results.append(result)
        print(json.dumps({k:v for k,v in result.items() if k!='metadata'}),flush=True)
    receipt['results']=results;receipt['all_predeclared_gates_passed']=all(x['passed'] for x in results)
    (HERE/'CONTEXT_GROWTH_CALIBRATION.json').write_text(json.dumps(receipt,indent=2)+'\n')
    assert receipt['all_predeclared_gates_passed']


if __name__=='__main__': main()
