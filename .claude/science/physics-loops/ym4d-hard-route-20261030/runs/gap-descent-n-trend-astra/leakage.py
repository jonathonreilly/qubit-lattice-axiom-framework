#!/usr/bin/env python3
"""Row 1090. Row 1089 leakage with streamed quadrature and pair Gram forms.
GUIDE only. All character/spin labels are doubled. No truncation certificate.
"""
import os, sys
from pathlib import Path
sys.dont_write_bytecode = True
PREV = Path(__file__).resolve().parents[1] / 'gap-descent-window-astra'
sys.path.insert(0, str(PREV))
import guard
import importlib.util, atexit, signal, math, time, json, argparse
import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh
spec = importlib.util.spec_from_file_location('prior_leakage', PREV/'leakage.py')
prior = importlib.util.module_from_spec(spec); spec.loader.exec_module(prior)
base = prior.base
# Synchronous RSS checks do not inject SIGALRM into BLAS kernels.
signal.setitimer(signal.ITIMER_REAL,0)

# Contract one site at a time. Only two adjacent quadrature axes are live.
# Work in blocks of the combined spectator index; no Q**n tensor is made.
def chain(x, V, e, Z, omit=-1, block=1024):
    base.memory_check()
    A=x.shape[0]; n=x.ndim; Q=len(e)
    t=(V@x.reshape(A,-1)).reshape((Q,)+(A,)*(n-1))
    t*=e.reshape((Q,)+(1,)*(n-1))
    for gap in range(n-1):
        # Move previous character outputs behind the two live sites.
        z=np.moveaxis(t,(gap,gap+1),(0,1)).reshape(Q,A,-1)
        del t
        out=np.empty((A,Q,z.shape[-1]))
        kernel=np.ones_like(Z) if gap==omit else Z
        for start in range(0,z.shape[-1],block):
            chunk=z[:,:,start:start+block]
            # q,r,s <- q,a,s times V[r,a]
            y=np.einsum('ras,qa->rqs',chunk,V,optimize=True)
            y*=kernel[:,:,None]*e[None,:,None]
            out[:,:,start:start+block]=(V.T@y.reshape(Q,-1)).reshape(A,Q,-1)
        # out axes: previous site, new live site, previous outputs, remaining inputs
        t=np.moveaxis(out.reshape((A,Q)+(A,)*(n-2)),(0,1),(gap,gap+1))
        del z,out
        base.memory_check()
    return prior.mode(t,V.T,n-1)


def gram(b,A,D,want_factors=False):
    outmax=D+A-1; pairs=[(u,v) for u in range(outmax+1) for v in (u-1,u+1) if 0<=v<=outmax]
    r=base.ratios(b,outmax); result=np.zeros((A*A,A*A));factors=[]
    for arc,multiplicity in ((1,4),(2,2)):
        B=np.zeros((len(pairs),len(pairs),A,A))
        for J in range(D+1):
            for H in (J-1,J+1):
                if not 0<=H<=D:continue
                R=np.array([[math.sqrt((u+1)*(v+1))*base.half_sixj_sq(u,v,H,J,a) for a in range(A)] for u,v in pairs])
                pref=2*(J+1)*(H+1)*r[J]**arc*r[H]**(4-arc)
                B+=pref*np.einsum('ua,vb->uvab',R,R)
        weights=np.array([r[u]**arc*r[v]**(4-arc) for u,v in pairs])
        B*=np.sqrt(weights[:,None,None,None]*weights[None,:,None,None])
        B=B.reshape(len(pairs)**2,A*A)
        result+=multiplicity*(B.T@B)
        if want_factors:factors.append((multiplicity,B.copy()))
    return (result,factors) if want_factors else result


def estimate(n,A,Q,ncv=12):
    # eigsh basis, retained vectors/work, two streamed-frontier buffers, small blocks.
    return int(8*A**n*(ncv+9+3*Q/A)+80_000_000)


def point(n,b,bT,A,D,Q,ncv=12,diagnose=False):
    start=time.monotonic(); predicted=estimate(n,A,Q,ncv)
    if predicted>1_950_000_000:raise MemoryError(f'preallocation estimate {predicted} bytes exceeds 1.95 GB')
    theta=np.arange(1,Q+1)*np.pi/(Q+1)
    chi=np.sin(np.arange(1,max(Q,2*A)+1)[:,None]*theta)/np.sin(theta)
    V=(np.sqrt(2/(Q+1))*np.sin(theta)*chi[:A]).T
    assert np.max(np.abs(V.T@V-np.eye(A)))<1e-12
    r=base.ratios(b,max(Q,D+A+2));Z=(chi[:Q].T*r[:Q]**4)@chi[:Q]
    e=np.exp(bT*(np.cos(theta)-1)); w=r[:A]**2
    W=w.reshape((A,)+(1,)*(n-1)).copy()
    for axis in range(1,n):W=W*w.reshape((1,)*axis+(A,)+(1,)*(n-axis-1))
    calls=0
    def apply(v):
        nonlocal calls
        calls+=1
        base.memory_check()
        return (W*chain(W*v.reshape((A,)*n),V,e,Z)).ravel()
    op=LinearOperator((A**n,A**n),matvec=apply,dtype=float)
    attempts=[]
    for seed in (1090,1091,1092):
        val,vec=eigsh(op,k=3,ncv=ncv,which='LA',tol=2e-13,v0=W.ravel()*np.random.default_rng(seed).standard_normal(A**n))
        order=np.argsort(val)[::-1];val=val[order];vec=vec[:,order]
        residual=[float(np.linalg.norm(apply(vec[:,i])-val[i]*vec[:,i])/val[0]) for i in range(3)]
        attempts.append({'seed':seed,'initial':'kinetic-weighted random','ncv':ncv,'residuals':residual,'eigenvalues':val.tolist()})
        if max(residual)<1e-10:break
        print('REJECTED_EIGENPAIRS',json.dumps(attempts[-1]),flush=True)
        del val,vec
    else:raise RuntimeError(f'all eigensolver attempts failed: {attempts}')
    want_direct=diagnose or n>=6
    norms=[float(np.linalg.norm(vec[:,i])) for i in range(3)]
    parity=[]
    if want_direct:
        for i in range(3):
            v=vec[:,i].reshape((A,)*n);mirror=np.transpose(v,tuple(reversed(range(n))))
            parity.append({'even_defect':float(np.linalg.norm(v-mirror)),'odd_defect':float(np.linalg.norm(v+mirror))})
    if want_direct:H,factors=gram(b,A,D,True)
    else:H=gram(b,A,D)
    ell=np.zeros(2);per_gap=[];direct_gaps=[];g_norms=[]
    for gap in range(n-1):
        contribution=[];direct_contribution=[];gn=[]
        for i in range(2):
            G=chain(W*vec[:,i].reshape((A,)*n),V,e,Z,omit=gap)
            # spectator squared kinetic weight is r[a]**4, so multiply G by r[a]**2.
            for axis in range(n):
                if axis not in (gap,gap+1):G*=w.reshape((1,)*axis+(A,)+(1,)*(n-axis-1))
            G=np.moveaxis(G,(gap,gap+1),(0,1)).reshape(A*A,-1)
            norm=0.
            for s in range(0,G.shape[1],8192):
                part=G[:,s:s+8192];norm+=float(np.sum(part*(H@part)))
            contribution.append(norm/val[i]**2)
            if want_direct:
                gn.append(float(np.linalg.norm(G)))
                direct=0.
                for mult,B in factors:
                    for j in range(0,G.shape[1],512):
                        amplitude=B@G[:,j:j+512];direct+=mult*float(np.sum(amplitude**2))
                direct_contribution.append(direct/val[i]**2)
            del part,G
            base.memory_check()
        ell+=contribution;per_gap.append(contribution);direct_gaps.append(direct_contribution);g_norms.append(gn)
    direct_gram_error=max((abs(a-b) for g,h in zip(per_gap,direct_gaps) for a,b in zip(g,h)),default=0.)
    if direct_gram_error>1e-9:raise RuntimeError(f'direct/Gram norm discrepancy {direct_gram_error}')
    reflection_error=max(abs(per_gap[j][i]-per_gap[-1-j][i]) for j in range(n-1) for i in (0,1))
    if reflection_error>1e-9 and not diagnose:
        print('REJECTED_REFLECTION',json.dumps({'n':n,'beta':b,'cutoff':[A,D,Q],'per_gap':per_gap,'error':reflection_error}),flush=True)
        raise RuntimeError('charged-gap reflection diagnostic failed')
    return dict(n=n,beta=b,beta_T=bT,chars=A,loops=D,quadrature=Q,memory_guard='synchronous peak-RSS checks',ncv=ncv,reflection_error=reflection_error,direct_gram_error=direct_gram_error,diagnostic_only=diagnose,vector_norms=norms,vector_reflection_defects=parity,direct_gaps=direct_gaps,g_norms=g_norms,
                l0=float(ell[0]),l1=float(ell[1]),difference=float(ell[1]-ell[0]),
                zero_gap=float(np.log(val[0]/val[1])),lambda2_over_lambda1=float(val[2]/val[1]),
                eigenvalues=val.tolist(),residuals=residual,per_gap=per_gap,
                solver_attempts=attempts,matvecs=calls,seconds=time.monotonic()-start,peak_RSS_bytes=base.memory_check(),estimated_bytes=predicted)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--n',type=int,required=True);p.add_argument('--beta',type=float,required=True)
    p.add_argument('--diagnose',action='store_true');p.add_argument('--cutoff',type=int,nargs=3,default=[10,12,32]);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();x=point(a.n,a.beta,a.beta,*a.cutoff,diagnose=a.diagnose);a.output.write_text(json.dumps(x,indent=2)+'\n');print(json.dumps(x),flush=True)
