#!/usr/bin/env python3
"""Synthetic exact-geometry and finite-error controls; no apparatus specification."""
from pathlib import Path
import hashlib,json,math
import numpy as np
from probe_context_echo_v2 import step,latitude,transport,gamma,axis,I

def connector_loop(beta,N,rot):
    pts=[rot@a for a in latitude(beta,N)];z=np.array([0.,0.,1.]);x=np.array([1.,0.,0.])
    return [z,x]+pts+[pts[0],x,z]

def main():
    rows=[]
    def ck(name,value,**kw):
        assert bool(value),name
        rows.append(dict(name=name,passed=True,**kw))
    flip=np.diag([1.,-1.,-1.]);ctx=np.array([.2,-.3,.7]);kap=.37;cases=0
    for N in [4,8,16,32]:
        for ba in [.001,.2,.7,1.4]:
            ga=gamma(ba,N);bb=np.arccos(np.tan((np.pi+ga/2)/N)/np.tan(np.pi/N))
            A=connector_loop(ba,N,np.eye(3));B=connector_loop(bb,N,np.eye(3))+connector_loop(bb,N,flip)[1:]
            assert min(1+np.dot(a,b) for path in [A,B] for a,b in zip(path,path[1:]))>=1-1e-14,'uniform edge gap'
            ua,wa=transport(A,ctx,0);ub,wb=transport(B,ctx,0);va,_=transport(A,ctx,kap);vb,_=transport(B,ctx,kap)
            assert np.linalg.norm(ua-ub)<2e-12 and np.linalg.norm(wb)<2e-12,'connector-preserved reference'
            assert abs(va[0,0]/vb[0,0]-np.exp(-1j*kap*np.dot(ctx,wa)/2))<2e-12,'connector-preserved context'
            cases+=1
    ck('uniform-gap connectors preserve matched paths',cases==16,cases=cases)
    rng=np.random.default_rng(19877);ratios=[]
    for _ in range(1000):
        a=rng.normal(size=3);a/=np.linalg.norm(a);b=rng.normal(size=3);b/=np.linalg.norm(b)
        if np.dot(a,b)<-.9:continue
        ap=a+.002*rng.normal(size=3);ap/=np.linalg.norm(ap);bp=b+.002*rng.normal(size=3);bp/=np.linalg.norm(bp)
        ea=np.linalg.norm(a-ap);eb=np.linalg.norm(b-bp);eta=min(1+np.dot(a,b),1+np.dot(ap,bp));bound=np.sqrt(2)*(ea+eb)/np.sqrt(eta)
        actual=np.linalg.norm(step(a,b,ctx,0)-step(ap,bp,ctx,0),2)
        assert actual<=bound+1e-13,'pair sensitivity'
        ratios.append(actual/bound)
    ck('pair operator sensitivity',len(ratios)>900,cases=len(ratios),maximum_fraction=max(ratios))
    N=16;ba=np.pi/3;ga=gamma(ba,N);bb=np.arccos(np.tan((np.pi+ga/2)/N)/np.tan(np.pi/N));paths=[connector_loop(ba,N,np.eye(3)),connector_loop(bb,N,np.eye(3))+connector_loop(bb,N,flip)[1:]]
    ratios=[]
    for path in paths:
        reference,W=transport(path,ctx,0)
        for _ in range(100):
            pert=[]
            for i,a in enumerate(path):
                v=a if i in [0,len(path)-1] else a+.0001*rng.normal(size=3);v=v/np.linalg.norm(v);pert.append(v)
            actual,Wp=transport(pert,ctx,0);errors=[np.linalg.norm(a-b) for a,b in zip(path,pert)];sbound=0
            for j in range(len(path)-1):
                eta=min(1+np.dot(path[j],path[j+1]),1+np.dot(pert[j],pert[j+1]));sbound+=np.sqrt(2)*(errors[j]+errors[j+1])/np.sqrt(eta)
            assert np.linalg.norm(actual-reference,2)<=sbound+1e-13,'path telescoping'
            assert abs(np.angle(actual[0,0]/reference[0,0]))<=np.arcsin(sbound)+1e-13,'phase disk bound'
            assert np.linalg.norm(Wp-W)<=sum(errors[j]+errors[j+1] for j in range(len(path)-1))+1e-13,'cross sum sensitivity'
            ratios.append(np.linalg.norm(actual-reference,2)/sbound)
    ck('full-path and phase error certificates',len(ratios)==200,cases=len(ratios),maximum_fraction=max(ratios))
    drift_ratios=[]
    for path in paths:
        base,W=transport(path,ctx,kap)
        for _ in range(100):
            U=I.copy();sumtheta=0;bound=0;delta=.001
            for a,b in zip(path,path[1:]):
                dv=rng.normal(size=3);dv=delta*dv/np.linalg.norm(dv);n=ctx+dv;U=step(a,b,n,kap)@U;sumtheta+=kap*np.dot(dv,np.cross(a,b))/2;bound+=abs(kap)*delta*np.linalg.norm(np.cross(a,b))/2
            actual=np.angle(U[0,0]/base[0,0])
            assert abs(actual+sumtheta)<1e-12 and abs(actual)<=bound+1e-13,'context drift certificate'
            drift_ratios.append(abs(actual)/bound)
    ck('edge context drift accounting',len(drift_ratios)==200,cases=len(drift_ratios),maximum_fraction=max(drift_ratios))
    delta=1e-5;SA=(N+4)*2*np.sqrt(2)*delta/np.sqrt(1-2*delta);SB=2*SA;phase_bound=np.arcsin(SA)+np.arcsin(SB);W=N*np.sin(ba)**2*np.sin(2*np.pi/N)
    ck('synthetic planning values',SA<1 and SB<1,N=N,vertex_error=delta,geometric_coefficient=W,reference_phase_error_bound=phase_bound)
    note=Path(__file__).with_name('NETWORK_EVOLUTION_BLOCK14_v1.md');helper=Path(__file__).with_name('probe_context_echo_v2.py')
    print(json.dumps({'summary':{'passed':len(rows),'failed':0},'checks':rows,'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'helper_sha256':hashlib.sha256(helper.read_bytes()).hexdigest(),'empirical_validation':False},indent=2,sort_keys=True))
if __name__=='__main__':main()
