#!/usr/bin/env python3
"""Compare simulations with full 2401-state four-ring correlation functions."""
from pathlib import Path
from itertools import product
import hashlib
import json
import numpy as np
import scipy.sparse as sparse
from scipy.sparse.linalg import expm_multiply
from context_exchange_sim import run, FIELDS, VECTORS

HERE=Path(__file__).resolve().parent


def exact(probabilities,u,coupling,floor):
    states=np.array(list(product(range(7),repeat=4)),dtype=int)
    index={tuple(s):i for i,s in enumerate(states)}
    rows=[];cols=[];rates=[]
    for i,state in enumerate(states):
        for x in range(4):
            l,a,b,r=state[[(x-1)%4,x,(x+1)%4,(x+2)%4]]
            # Independently assembled scalar forward state transitions.
            delta_v=int(VECTORS[a,0])-int(VECTORS[b,0])
            delta_n=int(a!=0)-int(b!=0)
            h=u*delta_v+coupling*(delta_v*(int(l!=0)+int(r!=0))
                                   +delta_n*(int(VECTORS[l,0])+int(VECTORS[r,0])))
            rate=floor+max(h,0)
            target=state.copy();target[x],target[(x+1)%4]=b,a
            j=index[tuple(target)]
            rows.extend([i,i]);cols.extend([j,i]);rates.extend([rate,-rate])
    Q=sparse.coo_matrix((rates,(rows,cols)),shape=(len(states),len(states))).tocsr()
    mu=np.prod(np.asarray(probabilities)[states],axis=1)
    assert abs(mu.sum()-1)<1e-12
    assert np.max(abs(Q@np.ones(len(states))))<1e-12
    stationary=float(np.max(abs(Q.T@mu)))
    assert stationary<1e-12
    times=np.linspace(0,5,21)
    modes=np.array([[1],[2]])
    phases=np.exp(-2j*np.pi*np.arange(4)[:,None]*np.array([1,2])[None,:]/4)/2
    observable=np.empty((len(states),4),dtype=complex)
    for mode in range(2):
        for a in range(2):
            observable[:,2*mode+a]=FIELDS[states,a]@phases[:,mode]
    evolved=expm_multiply(Q,observable,start=0,stop=5,num=len(times),endpoint=True)
    correlations=np.empty((len(times),2,2,2),dtype=complex)
    for mode in range(2):
        for a in range(2):
            for b in range(2):
                correlations[:,mode,a,b]=evolved[:,:,2*mode+a]@(mu*observable[:,2*mode+b].conj())
    return times,modes,correlations,stationary


def main():
    directory=HERE/'context_exchange_calibration'
    directory.mkdir(exist_ok=True)
    cases=[('flat',0.,0.,.2,[.5]+[1/12]*6,2026092120),
           ('context_isotropic',-1.,1.,.05,[.5]+[1/12]*6,2026092121),
           ('context_biased',-1.,1.,.05,(np.array([5,1,2,3,4,5,6])/26).tolist(),2026092122)]
    receipt={'plan':'Three predeclared four-ring cases; 8192 paths each; density/vx auto and cross correlations at both nonzero conjugacy classes and 21 times.',
             'gate':'maximum estimated standardized real/imaginary discrepancy <5.5; stochastic sanity check, not rigorous confidence certification',
             'cases':cases,'simulator_sha256':hashlib.sha256((HERE/'context_exchange_sim.py').read_bytes()).hexdigest(),
             'calibrator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (directory/'PLAN.json').write_text(json.dumps(receipt,indent=2)+'\n')
    results=[]
    for name,u,coupling,floor,probabilities,seed in cases:
        times,modes,target,stationary=exact(probabilities,u,coupling,floor)
        raw,stats,seeds,metadata=run([4],modes,probabilities,times,8192,seed,
                                    u,coupling,floor,0,0.,4)
        raw=raw[:,:,:,:2]
        differences=[];standardized=[]
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
                    differences.append(np.max(abs(delta)))
        maximum=float(max(standardized))
        passed=maximum<5.5
        np.savez_compressed(directory/f'{name}.npz',fields=raw,statistics=stats,seeds=seeds,
                            exact=target,estimated=estimates,standard_errors=errors,
                            times=times,modes=modes)
        result={'case':name,'passed':passed,'max_estimated_SE':maximum,
                'max_absolute_discrepancy':float(max(differences)),
                'exact_stationarity_residual':stationary,'metadata':metadata}
        (directory/f'{name}.json').write_text(json.dumps(result,indent=2)+'\n')
        results.append(result)
        print(json.dumps({k:v for k,v in result.items() if k!='metadata'}),flush=True)
    receipt['results']=results
    receipt['all_predeclared_gates_passed']=all(x['passed'] for x in results)
    (HERE/'CONTEXT_SIMULATION_CALIBRATION.json').write_text(json.dumps(receipt,indent=2)+'\n')
    assert receipt['all_predeclared_gates_passed']


if __name__=='__main__':
    main()
