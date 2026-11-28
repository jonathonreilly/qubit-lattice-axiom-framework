#!/usr/bin/env python3
"""Row 1089: extend row 1087's recoupling to beta_T>0 and n=3. GUIDE only."""
import guard
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS','BLIS_NUM_THREADS'):
    os.environ[key]='1'
import atexit
import argparse, importlib.util, json, math, signal, time
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh
spec=importlib.util.spec_from_file_location('base',Path(__file__).resolve().parents[1]/'gap-descent-sign-2-astra/recompute.py')
base=importlib.util.module_from_spec(spec); spec.loader.exec_module(base)
signal.signal(signal.SIGALRM, lambda *_: base.memory_check()); signal.setitimer(signal.ITIMER_REAL,1,1)
atexit.register(lambda: signal.setitimer(signal.ITIMER_REAL,0))

def mode(x,M,axis):
    return np.moveaxis(np.tensordot(M,x,axes=(1,axis)),0,axis)

def transform(x,M):
    for axis in range(x.ndim): x=mode(x,M,axis)
    return x

def point(n,b,bT,A,D,Q):
    theta=np.arange(1,Q+1)*np.pi/(Q+1)
    chi=np.sin(np.arange(1,max(Q,2*A)+1)[:,None]*theta)/np.sin(theta)
    V=(np.sqrt(2/(Q+1))*np.sin(theta)*chi[:A]).T
    assert np.max(np.abs(V.T@V-np.eye(A)))<1e-12
    r=base.ratios(b,max(Q,D+A+2))
    Z=(chi[:Q].T*r[:Q]**4)@chi[:Q]
    e=np.exp(bT*(np.cos(theta)-1))
    face=e.reshape((Q,)+(1,)*(n-1)).copy()
    for axis in range(1,n): face=face*e.reshape((1,)*axis+(Q,)+(1,)*(n-axis-1))
    full=face.copy()
    for axis in range(n-1): full=full*Z.reshape((1,)*axis+(Q,Q)+(1,)*(n-axis-2))
    w=r[:A]**2
    W=w.reshape((A,)+(1,)*(n-1)).copy()
    for axis in range(1,n): W=W*w.reshape((1,)*axis+(A,)+(1,)*(n-axis-1))
    def apply(v): return (W*transform(full*transform(W*v.reshape((A,)*n),V),V.T)).ravel()
    op=LinearOperator((A**n,A**n),matvec=apply)
    val,vec=eigsh(op,k=3,which='LA',tol=2e-13,v0=np.linspace(.8,1.2,A**n))
    order=np.argsort(val)[::-1]; val=val[order]; vec=vec[:,order]
    residual=[float(np.linalg.norm(apply(vec[:,i])-val[i]*vec[:,i])/val[0]) for i in range(3)]
    ell=np.zeros(2)
    outmax=D+A-1
    pairs=[(u,v) for u in range(outmax+1) for v in (u-1,u+1) if 0<=v<=outmax]
    r=base.ratios(b,outmax)
    for gap in range(n-1):
        other=face.copy()
        for axis in range(n-1):
            if axis!=gap: other=other*Z.reshape((1,)*axis+(Q,Q)+(1,)*(n-axis-2))
        G=[transform(other*transform(W*vec[:,i].reshape((A,)*n),V),V.T) for i in range(2)]
        if n==3:
            G=[np.moveaxis(x,(gap,gap+1),(0,1)) for x in G]
        else: G=[x[:,:,None] for x in G]
        for arc,multiplicity in ((1,4),(2,2)):
            amp=np.zeros((2,len(pairs),len(pairs),A if n==3 else 1))
            for J in range(D+1):
                for H in (J-1,J+1):
                    if not 0<=H<=D: continue
                    R=np.zeros((len(pairs),A))
                    for row,(u,v) in enumerate(pairs):
                        for a in range(A):
                            R[row,a]=math.sqrt((u+1)*(v+1))*base.half_sixj_sq(u,v,H,J,a)
                    pref=2*(J+1)*(H+1)*r[J]**arc*r[H]**(4-arc)
                    for i in range(2):
                        for c in range(G[i].shape[2]): amp[i,:,:,c]+=pref*R@G[i][:,:,c].T@R.T
            weights=np.array([r[u]**arc*r[v]**(4-arc) for u,v in pairs])
            S=weights[:,None,None]*weights[None,:,None]
            if n==3: S=S*r[:A][None,None,:]**4
            ell+=multiplicity*np.sum(amp**2*S,axis=(1,2,3))/val[:2]**2
    return dict(n=n,beta=b,beta_T=bT,chars=A,loops=D,quadrature=Q,l0=float(ell[0]),l1=float(ell[1]),difference=float(ell[1]-ell[0]),zero_gap=float(np.log(val[0]/val[1])),lambda2_over_lambda1=float(val[2]/val[1]),residuals=residual)

def main():
    p=argparse.ArgumentParser(); p.add_argument('--n',type=int,choices=(2,3),default=2);p.add_argument('--chars',type=int,required=True);p.add_argument('--loops',type=int,required=True);p.add_argument('--quad',type=int,default=32);p.add_argument('--betas',type=float,nargs='+',required=True);p.add_argument('--transverse',type=float,default=None);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    start=time.monotonic();results=[]
    for b in a.betas:
        x=point(a.n,b,b if a.transverse is None else a.transverse,a.chars,a.loops,a.quad);results.append(x)
        a.output.write_text(json.dumps(dict(grade='GUIDE',results=results,seconds=time.monotonic()-start,peak_RSS_bytes=base.memory_check()),indent=2)+'\n'); print(json.dumps(x),flush=True)
if __name__=='__main__':main()
