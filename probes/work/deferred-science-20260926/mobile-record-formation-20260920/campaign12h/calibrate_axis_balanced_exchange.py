#!/usr/bin/env python3
"""Full finite-generator calibration, including all six fields and births."""
from pathlib import Path
from itertools import product
import hashlib
import json
import numpy as np
import scipy.sparse as sparse
from scipy.sparse.linalg import expm_multiply
from axis_balanced_exchange_sim import run, FIELDS, VECTORS

HERE=Path(__file__).resolve().parent


def exact(probabilities,epsilon):
    states=np.array(list(product(range(7),repeat=4)),dtype=int)
    index={tuple(s):i for i,s in enumerate(states)}
    rows=[];cols=[];rates=[]
    feature=np.array([0,-1,-1,2,2,2,2])
    f=np.array([0,1,-1,0,0,0,0])
    for i,state in enumerate(states):
        for x in range(4):
            l,a,b,r=state[[(x-1)%4,x,(x+1)%4,(x+2)%4]]
            h=.5*((f[a]-f[b])*(feature[l]+feature[r])+(feature[a]-feature[b])*(f[l]+f[r]))
            rate=.05+max(h,0.)
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
    assert abs(mu.sum()-1)<1e-12 and np.max(abs(Q@np.ones(len(states))))<1e-12
    times=np.linspace(0,5,21);modes=np.array([[1],[2]])
    phases=np.exp(-2j*np.pi*np.arange(4)[:,None]*np.array([1,2])[None,:]/4)/2
    observable=np.empty((len(states),12),dtype=complex)
    for mode in range(2):
        for a in range(6): observable[:,6*mode+a]=FIELDS[states,a]@phases[:,mode]
    evolved=expm_multiply(Q,observable,start=0,stop=5,num=len(times),endpoint=True)
    correlations=np.empty((len(times),2,6,6),dtype=complex)
    for mode in range(2):
        correlations[:,mode]=np.einsum('tsa,sb,s->tab',evolved[:,:,6*mode:6*mode+6],
                                        observable[:,6*mode:6*mode+6].conj(),mu)
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
    directory=HERE/'axis_balanced_calibration';directory.mkdir(exist_ok=True)
    cases=[('rho025',[.75]+[1/24]*6,0.,2026092170),
           ('rho050',[.5]+[1/12]*6,0.,2026092171),
           ('rho075',[.25]+[1/8]*6,0.,2026092172),
           ('biased',(np.array([5,1,2,3,4,5,6])/26).tolist(),0.,2026092173),
           ('births',[.5]+[1/12]*6,.08,2026092174)]
    receipt={'plan_sha256':hashlib.sha256((HERE/'AXIS_BALANCED_SIMULATION_PLAN.md').read_bytes()).hexdigest(),
             'gate':'maximum estimated standardized real/imaginary correlation discrepancy <5.5, exact product residual <2e-12, and every-path count/Fourier audit',
             'cases':cases,'simulator_sha256':hashlib.sha256((HERE/'axis_balanced_exchange_sim.py').read_bytes()).hexdigest(),
             'calibrator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    planpath=directory/'PLAN.json'
    if planpath.exists(): raise RuntimeError('Refusing to overwrite existing calibration')
    planpath.write_text(json.dumps(receipt,indent=2)+'\n')
    results=[]
    for name,probabilities,epsilon,seed in cases:
        times,modes,target,product_error=exact(probabilities,epsilon)
        raw,stats,seeds,metadata=run([4],modes,probabilities,times,8192,seed,
                                    0.,.5,.05,0,epsilon,2)
        standardized=[];estimates=np.empty_like(target);errors=np.empty(target.shape+(2,))
        for a in range(6):
            for b in range(6):
                values=raw[:,:,:,a]*raw[:,0,:,b].conj()[:,None,:]
                estimates[:,:,a,b]=values.mean(axis=0)
                for component,transform in enumerate([np.real,np.imag]):
                    sample=transform(values);err=sample.std(axis=0,ddof=1)/np.sqrt(len(sample))
                    errors[:,:,a,b,component]=err
                    delta=sample.mean(axis=0)-transform(target[:,:,a,b])
                    standardized.append(np.max(abs(delta)/np.maximum(err,1e-12)))
        maximum=float(max(standardized));passed=maximum<5.5 and product_error<2e-12
        np.savez_compressed(directory/f'{name}.npz',fields=raw,statistics=stats,seeds=seeds,
                            exact=target,estimated=estimates,standard_errors=errors,
                            times=times,modes=modes)
        result={'case':name,'passed':passed,'max_estimated_SE':maximum,
                'exact_product_evolution_residual':product_error,'metadata':metadata}
        (directory/f'{name}.json').write_text(json.dumps(result,indent=2)+'\n')
        results.append(result)
        print(json.dumps({k:v for k,v in result.items() if k!='metadata'}),flush=True)
    receipt['results']=results;receipt['all_predeclared_gates_passed']=all(x['passed'] for x in results)
    (HERE/'AXIS_BALANCED_SIMULATION_CALIBRATION.json').write_text(json.dumps(receipt,indent=2)+'\n')
    assert receipt['all_predeclared_gates_passed']


if __name__=='__main__': main()
