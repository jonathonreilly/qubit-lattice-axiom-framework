#!/usr/bin/env python3
"""Continuous-time local simulator for the supplied mobile-record birth law.

Every undirected edge proposes a hop at rate one. Null proposals are retained;
births use their exact total hazard and conditional content weights. No sweep
clock, normalized birth replacement, deletion or occupied-color swaps.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from numba import njit

AXES=np.array([[0,0,0],[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],dtype=np.int64)


def geometry(side,dim):
    shape=(side,)*dim;n=side**dim
    coords=np.array(list(np.ndindex(shape)),dtype=np.int64)
    nb=np.empty((n,2*dim),np.int64);edges=[]
    for x,c in enumerate(coords):
        for axis in range(dim):
            for k,step in enumerate((-1,1)):
                t=c.copy();t[axis]=(t[axis]+step)%side
                y=np.ravel_multi_index(tuple(t),shape)
                nb[x,2*axis+k]=y
                if step==1:edges.append((x,y))
    balls=[]
    for x in range(n):
        found={x,*nb[x]}
        for y in nb[x]:found.update(nb[y])
        balls.append(sorted(found))
    maxball=max(map(len,balls));ball=np.full((n,maxball),-1,np.int64)
    for x,v in enumerate(balls):ball[x,:len(v)]=v
    phase=np.exp(2j*np.pi*coords/side)
    return nb,np.array(edges,np.int64),ball,phase


def weights(p,q,r):
    W=np.ones((7,7),float);scale=6/(p+q+4*r)
    for a in range(1,7):
        for b in range(1,7):
            W[a,b]=scale*(p if a==b else q if ((a-1)^1)==b-1 else r)
    return W


@njit(cache=True)
def birth_values(s,x,nb,W):
    out=np.zeros(6)
    if s[x]!=0:return out
    for a in range(1,7):
        v=1.
        for k in range(nb.shape[1]):v*=W[a,s[nb[x,k]]]
        out[a-1]=v
    return out


@njit(cache=True)
def fenwick_add(tree,x,delta):
    x+=1
    while x<len(tree):
        tree[x]+=delta;x+=x&-x


@njit(cache=True)
def fenwick_total(tree):
    x=len(tree)-1;out=0.
    while x>0:
        out+=tree[x];x-=x&-x
    return out


@njit(cache=True)
def fenwick_select(tree,target):
    x=0;step=1
    while 2*step<len(tree):step*=2
    while step:
        y=x+step
        if y<len(tree) and tree[y]<=target:
            target-=tree[y];x=y
        step//=2
    return x


@njit(cache=True)
def refresh(s,x,y,nb,W,rates,tree):
    # Only vacancies at a changed site or its neighbors change birth hazard.
    touched=np.empty(2+2*nb.shape[1],np.int64);nt=0
    for b in (x,y):
        if b<0:continue
        for k in range(-1,nb.shape[1]):
            a=b if k==-1 else nb[b,k]
            duplicate=False
            for j in range(nt):
                if touched[j]==a:duplicate=True;break
            if not duplicate:
                touched[nt]=a;nt+=1
    for k in range(nt):
        a=touched[k];new=birth_values(s,a,nb,W).sum()
        fenwick_add(tree,a,new-rates[a]);rates[a]=new


@njit(cache=True)
def observe(s,M0,nb,edges,ball,phase,W,epsilon,theta):
    n=len(s);dim=phase.shape[1];N=0;M=np.zeros(3)
    fourier=np.zeros((dim,3),np.complex128)
    birthN=0.;birthM=np.zeros(3);pairs=0.;align=0.;p2=0.;residual_abs=0.
    for x in range(n):
        a=s[x]
        if a:
            N+=1
            for i in range(3):
                M[i]+=AXES[a,i]
                for d in range(dim):fourier[d,i]+=AXES[a,i]*phase[x,d]
        local_n=0
        for k in range(ball.shape[1]):
            y=ball[x,k]
            if y>=0 and s[y]:local_n+=1
        if local_n>=2:p2+=1
        bv=birth_values(s,x,nb,W);birthN+=bv.sum()
        drift=np.zeros(3)
        for c in range(1,7):
            for i in range(3):
                b=bv[c-1]*AXES[c,i];birthM[i]+=b;drift[i]+=epsilon*b
        adjacent=np.zeros(3)
        for k in range(nb.shape[1]):
            y=nb[x,k];b=s[y]
            for i in range(3):adjacent[i]+=AXES[b,i]
            if (a==0)==(b==0):continue
            source=x if a else y;dest=y if a else x;content=s[source]
            old=1.;new=1.
            for t in range(nb.shape[1]):
                old*=W[content,s[nb[source,t]]]
                u=nb[dest,t]
                if u!=source:new*=W[content,s[u]]
            rate=new/(old+new)
            for i in range(3):drift[i]+=rate*(AXES[b,i]-AXES[a,i])
        for i in range(3):
            predicted=.5*(adjacent[i]-nb.shape[1]*AXES[a,i])+epsilon*theta*adjacent[i]
            residual_abs+=abs(drift[i]-predicted)
    for k in range(len(edges)):
        x,y=edges[k]
        if s[x] and s[y]:
            pairs+=1
            for i in range(3):align+=AXES[s[x],i]*AXES[s[y],i]
    score_increment=0.;m2=0.;smin=0.;variance_birth=0.
    for i in range(3):
        score_increment+=(M[i]-M0[i])*M0[i]
        m2+=M[i]*M[i]
        variance_birth+=2*M[i]*birthM[i]
    for d in range(dim):
        for i in range(3):smin+=abs(fourier[d,i])**2/dim
    return np.array([N/n,m2/n,smin/n,align/len(edges),pairs/len(edges),score_increment/n,birthN/n,(variance_birth+birthN)*epsilon/n,p2/n,residual_abs/(3*n)])


@njit(cache=True)
def trajectory(seed,nb,edges,ball,phase,W,epsilon,rho0,taus,theta,max_events):
    np.random.seed(seed);n=len(nb);s=np.zeros(n,np.int64);M0=np.zeros(3);N=0
    for x in range(n):
        if np.random.random()<rho0:
            a=1+np.random.randint(6);s[x]=a;N+=1
            for i in range(3):M0[i]+=AXES[a,i]
    rates=np.zeros(n);tree=np.zeros(n+1)
    for x in range(n):
        rates[x]=birth_values(s,x,nb,W).sum();fenwick_add(tree,x,rates[x])
    out=np.zeros((len(taus),12));t=0.;hops=0;events=0
    for kt in range(len(taus)):
        target=taus[kt]/(6*epsilon)
        while t<target and N<n:
            totalB=fenwick_total(tree);R=len(edges)+epsilon*totalB
            wait=-np.log(max(np.random.random(),1e-300))/R
            if t+wait>target:t=target;break
            t+=wait;events+=1
            if events>max_events:raise RuntimeError('declared per-trajectory event budget exceeded')
            choose=np.random.random()*R
            if choose<len(edges):
                k=np.random.randint(len(edges));x,y=edges[k]
                if (s[x]==0)==(s[y]==0):continue
                if s[x]==0:x,y=y,x
                a=s[x];old=1.;new=1.
                for k in range(nb.shape[1]):
                    old*=W[a,s[nb[x,k]]]
                    u=nb[y,k]
                    if u!=x:new*=W[a,s[u]]
                if np.random.random()<new/(old+new):
                    s[y]=a;s[x]=0;hops+=1;refresh(s,x,y,nb,W,rates,tree)
            else:
                x=fenwick_select(tree,np.random.random()*totalB)
                if x>=n or s[x]!=0:raise RuntimeError('invalid birth-hazard selection')
                bv=birth_values(s,x,nb,W);a=0;u=np.random.random()*bv.sum();partial=0.
                for k in range(6):
                    partial+=bv[k]
                    if u<partial:a=k+1;break
                if a==0:raise RuntimeError('invalid content selection')
                s[x]=a;N+=1;refresh(s,x,-1,nb,W,rates,tree)
        if N==n:t=target
        assert abs(fenwick_total(tree)-rates.sum())<1e-7*max(1.,rates.sum())
        out[kt,:10]=observe(s,M0,nb,edges,ball,phase,W,epsilon,theta)
        out[kt,10]=hops/n;out[kt,11]=events/n
    return out


COLS=['density','M2_per_site','Smin_per_site','bond_alignment_per_edge','occupied_pairs_per_edge','response_score_increment_per_site','hazard_per_site','M2_drift_per_site','radius_two_multiple_probability','mean_absolute_component_residual','cumulative_hops_per_site','cumulative_proposals_per_site']


def run(side,dim,p,q,r,epsilon,rho0,reps,seed,out,steps=21,tau_max=4.):
    nb,edges,ball,phase=geometry(side,dim);W=weights(p,q,r);theta=6*(p-q)/(p+q+4*r)
    taus=np.linspace(0,tau_max,steps)
    began=time.monotonic();raw=np.empty((reps,steps,len(COLS)))
    for k in range(reps):
        raw[k]=trajectory(seed+k,nb,edges,ball,phase,W,epsilon,rho0,taus,theta,20_000_000)
    mean=raw.mean(axis=0);se=raw.std(axis=0,ddof=1)/np.sqrt(reps)
    rows=[]
    for t,mu,err in zip(taus,mean,se):
        rho=mu[0];chi=1+mu[5]/rho0
        rows.append({'tau':float(t),**{key:float(v) for key,v in zip(COLS,mu)},'se':{key:float(v) for key,v in zip(COLS,err)},'absolute_orientation_response':float(chi),'per_record_response_gain':float(rho0*chi/rho),'S0_per_record':float(mu[1]/rho),'Smin_per_record':float(mu[2]/rho),'bond_alignment_given_pair':float(mu[3]/mu[4])})
    meta={'side':side,'dimension':dim,'vertices':side**dim,'raw_weights':[p,q,r],'normalized_weights':W.tolist(),'epsilon':epsilon,'rho0':rho0,'replicates':reps,'seed_start':seed,'seed_end':seed+reps-1,'tau_definition':'6 epsilon t','columns':COLS,'elapsed_sec':time.monotonic()-began,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(meta,indent=2)+'\n')
    np.savez_compressed(out.with_suffix('.npz'),raw=raw,taus=taus)
    print(json.dumps({k:v for k,v in meta.items() if k not in ('rows','normalized_weights')},indent=2))
    for row in rows[::max(1,steps//4)]:
        print(json.dumps({k:row[k] for k in ('tau','density','absolute_orientation_response','per_record_response_gain','S0_per_record','Smin_per_record','bond_alignment_given_pair','radius_two_multiple_probability','cumulative_hops_per_site')}))
    return meta,raw


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    for name,default in (('side',4),('dim',1),('reps',8192),('seed',20260920),('steps',21)):
        ap.add_argument('--'+name,type=int,default=default)
    for name,default in (('p',3.),('q',1.),('r',2.),('epsilon',.1),('rho0',.25),('tau-max',4.)):
        ap.add_argument('--'+name,type=float,default=default)
    ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
    run(a.side,a.dim,a.p,a.q,a.r,a.epsilon,a.rho0,a.reps,a.seed,a.out,a.steps,a.tau_max)
