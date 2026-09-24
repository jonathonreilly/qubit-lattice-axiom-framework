#!/usr/bin/env python3
"""Complete charge matrices and complete finite-spin ring Gauss sectors.

This independently assembles matrices from site transitions, not path_engine.
Cube Fourier fibers are operator controls, never normalizable flux inputs.
"""
from pathlib import Path
from itertools import combinations
import argparse, datetime, hashlib, json, sys, traceback
sys.dont_write_bytecode=True
import numpy as np
from scipy.linalg import eigh

HERE=Path(__file__).resolve().parent
checks=[]
def check(name,value):
    checks.append({'name':name,'passed':bool(value)})
    if not value: raise AssertionError(name)

def charge_words(n,N,Q):
    negatives=(N-Q)//2
    assert negatives>=0 and 2*negatives==N-Q
    for occupied in combinations(range(n),N):
        for minus in combinations(occupied,negatives):
            yield tuple(-1 if x in minus else 1 if x in occupied else 0 for x in range(n))

def geometry(n):
    if n==8:
        A=(0,3,5,6)
        edges=tuple((x,y) for x in range(n) for y in range(x+1,n) if (x^y).bit_count()==1)
    else:
        A=tuple(range(0,n,2));edges=tuple(sorted({tuple(sorted((x,(x+1)%n))) for x in range(n)}))
    return A,edges

def ring_basis(n,N,S):
    A,edges=geometry(n)
    states=[]
    for q in charge_words(n,N,len(A)):
        for t in range(-S,S+1):
            flux={};flow=t
            for x in range(n-1):
                flow+=q[x]-int(x in A)
                flux[(x,x+1)]=flow
            flux[(0,n-1)]=-t
            E=tuple(flux[e] for e in edges)
            if max(map(abs,E))<=S: states.append((q,E))
    return states

def matrices(n,N,S=None,powers=None):
    A,edges=geometry(n);neigh={a:tuple(y if a==x else x for x,y in edges if a in (x,y)) for a in A}
    basis=[(q,None) for q in charge_words(n,N,len(A))] if S is None else ring_basis(n,N,S)
    index={state:i for i,state in enumerate(basis)};size=len(basis)
    Fs=[];Cs=np.zeros((size,size),complex)
    for a in A:
        F=np.zeros((size,size),complex);dinfty=np.zeros(size);ds=np.zeros(size);gate=np.zeros(size)
        for col,(q,E) in enumerate(basis):
            gate[col]=int(all(q[c] for c in A if c!=a and set(neigh[a])&set(neigh[c])))
            if not q[a]: continue
            for b in neigh[a]:
                if q[b]: continue
                dinfty[col]+=1
                e=edges.index(tuple(sorted((a,b))));shift=-q[a] if a<b else q[a]
                qq=list(q);qq[b],qq[a]=qq[a],0
                if S is None:
                    weight=(1j)**(shift*(powers[e] if powers else 0));EE=None
                else:
                    if abs(E[e]+shift)>S: continue
                    weight=np.sqrt(1-E[e]*(E[e]+shift)/(S*(S+1)))
                    f=list(E);f[e]+=shift;EE=tuple(f)
                ds[col]+=abs(weight)**2
                F[index[(tuple(qq),EE)],col]+=weight
        Fs.append(F)
        block=F.conj().T@F+np.diag(dinfty-ds)
        check(f'matrix n={n} N={N} S={S} center={a} commuting occupancy gate',np.max(np.abs(block*gate[None,:]-gate[:,None]*block))<1e-12)
        Cs+=block*gate[None,:]
    Fsum=sum(Fs);T=-(Fsum+Fsum.conj().T)
    grades=np.array([sum(q[a]==0 for a in A) for q,E in basis]);W=np.diag(grades)
    P=np.flatnonzero(grades==0)
    return {'n':n,'A':A,'edges':edges,'basis':basis,'index':index,'F':Fsum,'Fs':Fs,'T':T,'C':Cs,'W':W,'grades':grades,'P':P,'S':S,'powers':powers}

def jump(pre,post,edge,sign):
    J=np.zeros((len(post['basis']),len(pre['basis'])),complex)
    x,y=pre['edges'][edge];a=x if x in pre['A'] else y;S=pre['S']
    for col,(q,E) in enumerate(pre['basis']):
        if q[x] or q[y]:continue
        for sigma in (-1,1) if sign is None else (sign,):
            lower=sigma if a==x else -sigma
            qq=list(q);qq[x],qq[y]=lower,-lower
            if S is None:
                weight=(1j)**(lower*(pre['powers'][edge] if pre['powers'] else 0));EE=None
            else:
                if abs(E[edge]+lower)>S:continue
                weight=np.sqrt(1-E[edge]*(E[edge]+lower)/(S*(S+1)))
                f=list(E);f[edge]+=lower;EE=tuple(f)
            J[post['index'][(tuple(qq),EE)],col]+=weight
    return J

def canonical(model,eps):
    h=model['W']+eps*model['T']+eps*eps*model['C']
    eigen,V=eigh(h);rank=len(model['P']);Q=V[:,:rank]@V[:,:rank].conj().T
    E=np.eye(len(eigen))[:,model['P']];overlap=E.conj().T@Q@E
    d,u=eigh(overlap);assert np.min(d)>.5
    isometry=Q@E@((u/d[None,:]**.5)@u.conj().T)
    check(f'canonical rank={rank} dim={len(eigen)} eps={eps} isometry',np.max(np.abs(isometry.conj().T@isometry-np.eye(rank)))<5e-12)
    if rank<len(eigen):check(f'canonical rank={rank} dim={len(eigen)} eps={eps} separated',eigen[rank]>.5 and np.max(np.abs(eigen[:rank]))<.4)
    return h,eigen,V,isometry

def coefficients(pre,post,J,x):
    A=pre['T']@x
    Z=pre['T']@A;Z=np.where(pre['grades']==2,Z,0)
    B=-J@A
    R=.5*J@Z+post['T']@B;R=np.where(post['grades']==1,R,0)
    n=np.vdot(B,B).real
    M=pre['T'][:,pre['P']].conj().T@pre['T'][:,pre['P']]
    Delta=pre['C'][np.ix_(pre['P'],pre['P'])]-M
    Mp=post['T'][:,post['P']].conj().T@post['T'][:,post['P']]
    Deltap=post['C'][np.ix_(post['P'],post['P'])]-Mp
    mu=np.vdot(B[post['P']],Deltap@B[post['P']]).real/n
    return B,R,n,np.vdot(R,R).real/n,mu,Delta,Deltap

def run(attempt):
    result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'status':'running','checks':checks}
    out=HERE/f'MATRIX_RESULTS_{attempt}.json'
    if out.exists():raise FileExistsError(out)
    try:
        cube_rows=[]
        for phases in (tuple([0]*12),tuple(range(12))):
            pre=matrices(8,4,powers=phases);post=matrices(8,6,powers=phases)
            x=np.zeros(len(pre['basis']),complex);x[pre['P'][0]]=1
            signs=(-1,1,None);Js={sign:jump(pre,post,0,sign) for sign in signs}
            coeffs={sign:coefficients(pre,post,Js[sign],x) for sign in signs}
            for sign in signs:
                B,R,w,ell,mu,*_=coeffs[sign]
                check(f'cube fiber {phases} sign={sign} derived leakage',abs(ell-{-1:1,1:2,None:1.5}[sign])<1e-12)
                check(f'cube fiber {phases} sign={sign} marked-center identity',np.linalg.norm(R+post['Fs'][0]@B)<1e-12)
            for eps in (.04,.02,.01,.005):
                hin,evin,Vin,uin=canonical(pre,eps);hout,evout,Vout,uout=canonical(post,eps)
                d=uin[:,0]
                for sign in signs:
                    J=Js[sign];y=J@d;weight=np.vdot(y,y).real;phi=y/np.sqrt(weight)
                    hy=hout@phi;mean=np.vdot(phi,hy).real;second=np.vdot(hy,hy).real
                    high=1-np.linalg.norm(uout.conj().T@phi)**2
                    ell=coeffs[sign][3]
                    row={'phase_powers':phases,'epsilon':eps,'sign':sign,'intensity_over_kappa':weight/eps**2,'epsilon2_mean_over_delta':mean/eps**2,'epsilon6_variance_over_delta2':(second-mean**2)/eps**2,'high_weight_over_epsilon2':high/eps**2,'derived_leakage':ell}
                    if eps==.005:
                        check(f'cube final small-epsilon mean sign={sign} phase={phases}',abs(row['epsilon2_mean_over_delta']-ell)<.025)
                        check(f'cube final small-epsilon variance sign={sign} phase={phases}',abs(row['epsilon6_variance_over_delta2']-ell)<.025)
                    cube_rows.append(row)
        result['complete_cube_fourier_fiber_rows']=cube_rows

        ring_rows=[]
        for n in (4,6):
            for S,flux in ((1,0),(2,1),(4,2)):
                pre=matrices(n,len(geometry(n)[0]),S=S);post=matrices(n,len(geometry(n)[0])+2,S=S)
                q=tuple(int(x in pre['A']) for x in range(n));E=tuple(-flux if e==(0,n-1) else flux for e in pre['edges'])
                state=(q,E);source=pre['index'][state];x=np.eye(len(pre['basis']))[:,source]
                pcol=list(pre['P']).index(source)
                J=jump(pre,post,0,1);B,R,w,ell,mu,Delta,Deltap=coefficients(pre,post,J,x)
                check(f'ring {n} S={S} complete-matrix leakage zero',np.linalg.norm(R)<1e-12)
                if n==4:
                    check(f'four-ring S={S} entire post Hamiltonian exactly zero',np.max(np.abs(post['W']))==0 and np.max(np.abs(post['T']))==0 and np.max(np.abs(post['C']))==0)
                for eps in (.04,.02,.01,.005):
                    hin,evin,Vin,uin=canonical(pre,eps);hout,evout,Vout,uout=canonical(post,eps)
                    d=uin[:,pcol];y=J@d;weight=np.vdot(y,y).real;phi=y/np.sqrt(weight)
                    hy=hout@phi;mean=np.vdot(phi,hy).real;second=np.vdot(hy,hy).real
                    initial=np.vdot(d,hin@d).real
                    # Direct norm of the high projection avoids subtracting 1.
                    high=np.linalg.norm(Vout[:,len(post['P']):].conj().T@phi)**2
                    row={'sites':n,'S':S,'flux':flux,'epsilon':eps,'pre_dimension':len(pre['basis']),'post_dimension':len(post['basis']),'intensity_over_kappa':weight/eps**2,'epsilon2_initial_mean_over_delta':initial/eps**2,'epsilon2_post_mean_over_delta':mean/eps**2,'predicted_post_scaled_mean':mu,'epsilon6_variance_over_delta2':(second-mean**2)/eps**2,'epsilon2_variance_over_delta2':(second-mean**2)/eps**6,'high_weight_over_epsilon6':high/eps**6}
                    if eps==.005:check(f'ring {n} S={S} scaled mean asymptotic',abs(mean/eps**2-mu)<.02)
                    ring_rows.append(row)
        result['complete_physical_ring_rows']=ring_rows
        result['status']='completed'
    except Exception as exc:
        result['status']='failed';result['exception']=repr(exc);result['traceback']=traceback.format_exc();raise
    finally:
        result['summary']={'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks)}
        out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'result':str(out),'status':result['status'],**result['summary']}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--attempt',required=True);run(p.parse_args().attempt)
