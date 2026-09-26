#!/usr/bin/env python3
"""Direct finite-generator probe for growing immutable six-content records.

Exploratory author computation: supplied stochastic model, no physical or
thermodynamic identification. Site code 0 is vacancy, 1..6 are signed axes.
"""
from __future__ import annotations
import argparse
from itertools import product
from pathlib import Path
import json
import time
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply

AXES=np.array([[0,0,0],[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],dtype=float)


def neutral_weights(p=3.0,q=1.0,r=2.0):
    W=np.ones((7,7),float)
    c=6/(p+q+4*r)
    for a in range(1,7):
        for b in range(1,7):
            W[a,b]=c*(p if a==b else q if (a-1)^1==b-1 else r)
    return W


def direct_generator(n,edges,W,epsilon):
    states=np.array(list(product(range(7),repeat=n)),dtype=np.int8)
    powers=7**np.arange(n-1,-1,-1,dtype=np.int64)
    nb=[tuple(b if a==x else a for a,b in edges if x in (a,b)) for x in range(n)]
    rows=[];cols=[];data=[]
    for idx,s in enumerate(states):
        total=0.
        for x in range(n):
            if s[x]!=0:continue
            for a in range(1,7):
                rate=epsilon
                for y in nb[x]:rate*=W[a,s[y]]
                rows.append(idx);cols.append(idx+a*powers[x]);data.append(rate);total+=rate
        old=np.prod([W[s[x],s[y]] for x,y in edges])
        for x,y in edges:
            if (s[x]==0)==(s[y]==0):continue
            t=s.copy();t[x],t[y]=s[y],s[x]
            new=np.prod([W[t[u],t[v]] for u,v in edges])
            rate=new/(old+new)
            dest=idx+(int(s[y])-int(s[x]))*powers[x]+(int(s[x])-int(s[y]))*powers[y]
            rows.append(idx);cols.append(dest);data.append(rate);total+=rate
        rows.append(idx);cols.append(idx);data.append(-total)
    Q=coo_matrix((data,(rows,cols)),shape=(len(states),len(states))).tocsr()
    assert np.max(np.abs(np.asarray(Q.sum(axis=1))))<1e-11
    return states,Q,nb


def birth_moment_identities(states,Q,nb,W,epsilon):
    n=states.shape[1];N=np.count_nonzero(states,axis=1)
    M=AXES[states].sum(axis=1)
    birth_N=np.zeros(len(states));birth_M=np.zeros_like(M);birth_M2=np.zeros(len(states))
    for idx,s in enumerate(states):
        for x in range(n):
            if s[x]!=0:continue
            for a in range(1,7):
                rate=epsilon*np.prod([W[a,s[y]] for y in nb[x]])
                birth_N[idx]+=rate
                birth_M[idx]+=rate*AXES[a]
                birth_M2[idx]+=rate*(2*np.dot(M[idx],AXES[a])+1)
    assert np.max(abs(Q@N-birth_N))<1e-10
    assert np.max(abs(Q@M-birth_M))<1e-10
    assert np.max(abs(Q@np.sum(M*M,axis=1)-birth_M2))<1e-10
    return N,M


def initial_law(states,rho):
    one=np.array([1-rho]+[rho/6]*6)
    alpha=np.prod(one[states],axis=1)
    M=AXES[states].sum(axis=1)
    derivative=3*M[:,0]*alpha/rho
    assert abs(alpha.sum()-1)<1e-12 and abs(derivative.sum())<1e-12
    assert abs(derivative@M[:,0]-states.shape[1])<1e-11
    return alpha,derivative


def probe(p,q,r,epsilon,rho0,tau_max=4.,steps=21):
    start=time.monotonic()
    n=4;edges=((0,1),(1,2),(2,3),(0,3));z=2
    W=neutral_weights(p,q,r)
    states,Q,nb=direct_generator(n,edges,W,epsilon)
    N,M=birth_moment_identities(states,Q,nb,W,epsilon)
    alpha,derivative=initial_law(states,rho0)
    theta=6*(p-q)/(p+q+4*r)
    exact_density_slope=float(alpha@(Q@N)/n)
    exact_response_slope=float(derivative@(Q@M[:,0])/n)
    assert abs(exact_density_slope-6*epsilon*(1-rho0))<1e-10
    assert abs(exact_response_slope-epsilon*(1-rho0)*z*theta)<1e-10
    normal_slope=exact_response_slope-exact_density_slope/rho0
    assert abs(normal_slope-epsilon*(1-rho0)*(z*theta-6/rho0))<1e-10
    # tau=6 epsilon t makes the uniform-weight vacancy decay rate one.
    scaled=Q.T/(6*epsilon)
    initial=np.column_stack((alpha,derivative))
    evolved=expm_multiply(scaled,initial,start=0,stop=tau_max,num=steps,endpoint=True,traceA=scaled.diagonal().sum())
    M2=np.sum(M*M,axis=1)
    lowest_phase=np.exp(2j*np.pi*np.arange(n)/n)
    F=np.einsum('sxi,x->si',AXES[states],lowest_phase)
    F2=np.sum(abs(F)**2,axis=1)
    bond=np.array([sum(np.dot(AXES[s[x]],AXES[s[y]]) for x,y in edges) for s in states])
    adjacent=np.array([sum(s[x]!=0 and s[y]!=0 for x,y in edges) for s in states])
    rows=[]
    for tau,dist in zip(np.linspace(0,tau_max,steps),evolved):
        law,slope=dist.T
        assert abs(law.sum()-1)<1e-9 and law.min()>-1e-11
        assert abs(slope.sum())<1e-9 and abs(slope@N)<1e-8
        density=law@N/n
        response=slope@M[:,0]/n
        rows.append({'tau':float(tau),'density':float(density),'absolute_orientation_response':float(response),'per_record_response_gain':float(rho0*response/density),'S0_per_record':float(law@M2/(law@N)),'Smin_per_record':float(law@F2/(law@N)),'bond_alignment_given_pair':float(law@bond/(law@adjacent)),'iid_closure_response_gain':float(rho0/density*np.exp(z*theta*(density-rho0)/6))})
        if p==q==r:
            assert abs(density-(1-(1-rho0)*np.exp(-tau)))<1e-9
            assert abs(response-1)<1e-9
            assert abs(rows[-1]['S0_per_record']-1)<1e-9
            assert abs(rows[-1]['Smin_per_record']-1)<1e-9
    return {'graph':'cycle4','vertices':n,'edges':edges,'weights_raw':[p,q,r],'epsilon':epsilon,'rho0':rho0,'theta_vector':theta,'normalization':'ratio of expectations E[M]/E[N], linearized at zero uniform bias; not E[M/N]','initial_density_slope':exact_density_slope,'initial_absolute_response_slope':exact_response_slope,'initial_per_record_gain_slope':normal_slope,'generator_states':len(states),'generator_nonzeros':Q.nnz,'elapsed_sec':time.monotonic()-start,'rows':rows}


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--epsilon',type=float,default=.1)
    ap.add_argument('--rho0',type=float,default=.25)
    ap.add_argument('--p',type=float,default=3.)
    ap.add_argument('--q',type=float,default=1.)
    ap.add_argument('--r',type=float,default=2.)
    args=ap.parse_args()
    result=probe(args.p,args.q,args.r,args.epsilon,args.rho0)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
    for row in result['rows'][::5]:print(json.dumps(row))
