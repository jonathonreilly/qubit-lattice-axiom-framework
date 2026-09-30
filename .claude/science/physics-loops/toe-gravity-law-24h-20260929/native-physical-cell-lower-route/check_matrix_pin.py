#!/usr/bin/env python3
"""New literal controls; no import of an earlier native builder.

Exact Gaussian-integer Fourier Gram comparisons use quarter-turn momenta.
Finite matrix controls corroborate, but do not prove, the asymptotic argument.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
import itertools as it
import json
import hashlib
import time
import resource
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
RUNTIME=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
def guard():
    assert time.time()<json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
    assert not (RUNTIME/'STOP_REQUESTED.json').exists()
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<200*1024**2

E=[tuple(int(i==j) for i in range(3)) for j in range(3)]
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def scale(c,a): return tuple(c*x for x in a)
D=[scale(2,e) for e in E]+[add(E[i],scale(s,E[j])) for i in range(3) for j in range(i+1,3) for s in (1,-1)]
def word(u,v,sign=1):
    diff=add(v,neg(u))
    if diff in D: return {(u,D.index(diff)):sign}
    return {(v,D.index(neg(diff))):sign}
def combine(*parts):
    out={}
    for c,p in parts:
        for key,v in p.items(): out[key]=out.get(key,0)+c*v
    return {k:v for k,v in out.items() if v}
def shift(row,x): return {(add(a,x),d):v for (a,d),v in row.items()}
AX=[word(neg(e),e) for e in E]
PLANES=[]
for i in range(3):
    for j in range(i+1,3):
        PLANES.append([word(scale(s,E[i]),scale(t,E[j]),s*t) for s in (1,-1) for t in (1,-1)])

def row_program(mu,tau):
    """Return real literal rows and weights for twelve times actual energy."""
    sos=[(8*mu,combine(*[(1,r) for r in AX]))]
    for p in PLANES:
        sos += [(3*mu,combine((1,p[i]),(-1,p[j]))) for i in range(4) for j in range(i+1,4)]
    collect=[(6*tau,combine((1,AX[0]),(-1,AX[1]))),
             (2*tau,combine((1,AX[0]),(1,AX[1]),(-2,AX[2])))]
    collect += [(3*tau,combine(*[(1,r) for r in p])) for p in PLANES]
    return sos,collect

def fourier(row,k):
    f=np.zeros(9,dtype=complex)
    for (x,d),v in row.items(): f[d]+=v*(1j)**(sum(a*b for a,b in zip(k,x))%4)
    return f
def gram(v): return np.outer(v.conj(),v)

def exact_symbols():
    comparisons=0
    for mu,tau in ((1,1),(3,2),(12,1)):
        sos,collect=row_program(mu,tau)
        for k in it.product(range(4),repeat=3):
            ell=sum(abs((1j)**q-1)**2 for q in k)
            ell=int(round(ell))
            actual=sum(c*gram(fourier(r,k)) for c,r in sos)
            actual+=sum(c*ell*gram(fourier(r,k)) for c,r in collect)
            v=np.array([(1j)**((-q)%4) for q in k])
            expected=np.zeros((9,9),complex)
            expected[:3,:3]=12*tau*ell*np.eye(3)+(8*mu-4*tau*ell)*gram(v)
            index=3
            for i in range(3):
                for j in range(i+1,3):
                    r=np.array([-s*((1j)**((-s*k[j])%4)+(1j)**((-k[i])%4)) for s in (1,-1)])
                    expected[index:index+2,index:index+2]=24*mu*np.eye(2)+(3*tau*ell-3*mu)*gram(r)
                    index+=2
            # All entries are exactly represented Gaussian integers, no tolerance.
            assert np.array_equal(actual,expected),(mu,tau,k,actual-expected)
            assert np.array_equal(actual.real,np.rint(actual.real))
            assert np.array_equal(actual.imag,np.rint(actual.imag))
            comparisons+=81
    return {'exact_Gaussian_integer_entries':comparisons,'momenta_per_coupling':64,'couplings':[[1,1],[3,2],[12,1]]}

def soft():
    u=np.zeros((9,5))
    u[:3,0]=np.array([1,-1,0])/np.sqrt(2)
    u[:3,1]=np.array([1,1,-2])/np.sqrt(6)
    for j in range(3):u[3+2*j:5+2*j,2+j]=np.array([-1,1])/np.sqrt(2)
    return u

def cell(L,eps=.25,mu=1.,tau=1.):
    sites=list(it.product(range(L),repeat=3));si={x:i for i,x in enumerate(sites)}
    n=9*len(sites);K=np.zeros((n,n));rows=0
    def put(row,c):
        nonlocal rows
        if not row or any(x not in si for x,d in row):return
        inds=[9*si[x]+d for x,d in row];v=np.array(list(row.values()))
        K[np.ix_(inds,inds)]+=c*np.outer(v,v);rows+=1
    sos,collect=row_program(mu,tau)
    for x in it.product(range(-2,L+2),repeat=3):
        for c,r in sos: put(shift(r,x),(1-eps)*c/12)
        for c,r in collect:
            for e in E: put(shift(combine((1,shift(r,e)),(-1,r)),x),(1-eps)*c/12)
    a=min(tau,mu/12)
    for x in sites:
        for e in E:
            y=add(x,e)
            if y in si:
                for d in range(9):put({(x,d):-1,(y,d):1},eps*a)
    U=soft();const=np.tile(U,(len(sites),1))/np.sqrt(len(sites))
    assert np.linalg.norm(K@const)<1e-10
    values,vectors=np.linalg.eigh(K)
    assert np.sum(np.abs(values)<1e-9)==5
    assert values[5]>=eps*a/(14*L*L)*(1-1e-9)
    # Solve on exactly the known complement rather than inverting small zeros.
    Hinv=(vectors[:,5:]/values[5:])@vectors[:,5:].T
    pins=[(L//2,)*3] if L==3 else [(1,1,1),(L-2,L-2,L-2)]
    ids=[9*si[x]+d for x in pins for d in range(9)]
    Gamma=Hinv[np.ix_(ids,ids)];m=len(pins)
    assert np.linalg.eigvalsh(Gamma)[0]>0
    C=np.tile(U,(m,1));capacity=C.T@np.linalg.solve(Gamma,C)
    G=Gamma[:9,:9];zeta=np.linalg.norm(Gamma-np.kron(np.eye(m),G),2)
    simple=m*(U.T@np.linalg.solve(G,U))/(1+zeta*np.linalg.norm(np.linalg.inv(G),2))
    assert np.linalg.eigvalsh(capacity-simple)[0]>-1e-8
    rng=np.random.default_rng(404+L)
    margins=[]
    for unused in range(5):
        f=rng.normal(size=n)+1j*rng.normal(size=n);f[ids]=0
        z=U.T@f.reshape((-1,9)).mean(axis=0)
        energy=float(np.vdot(f,K@f).real)
        bound=float(np.vdot(z,capacity@z).real)
        assert energy+1e-8>=bound
        margins.append(energy-bound)
    # Exact constrained mean-energy minimizer: q=-K^+ point C z.
    z=np.arange(1,6,dtype=float);amplitudes=np.linalg.solve(Gamma,C@z)
    q=-Hinv[:,ids]@amplitudes;f=np.tile(U@z,len(sites))+q
    assert np.max(np.abs(f[ids]))<1e-9
    assert np.max(np.abs(const.T@q))<1e-8
    e=float(f@K@f);cap=float(z@capacity@z)
    assert abs(e-cap)<2e-7*max(1,abs(cap))
    return {'L':L,'dimension':n,'selected_rows':rows,'five_zero_modes':True,'gap':float(values[5]),'proved_gap_lower':eps*a/(14*L*L),'pins':pins,'capacity_eigenvalues':np.linalg.eigvalsh(capacity).tolist(),'finite_block_error_norm':float(zeta),'mean_capacity_minimizer_residual':abs(e-cap),'random_pinned_margins':margins}

def main():
    guard();start=time.monotonic();cpu=time.process_time()
    result={'scope':'exact finite symbol and finite-cell capacity controls, not an asymptotic convergence test','symbols':exact_symbols(),'cells':[]}
    for L in (3,4,5):
        guard();result['cells'].append(cell(L));print('PASS finite cell',L,flush=True)
    result['source_sha256']=hashlib.sha256((HERE/'WORKING_PROOF.md').read_bytes()).hexdigest()
    result['runner_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['cpu_seconds']=time.process_time()-cpu;result['wall_seconds']=time.monotonic()-start
    result['peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    guard();(HERE/'CONTROLS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'cpu_seconds':result['cpu_seconds'],'wall_seconds':result['wall_seconds'],'peak_rss_bytes':result['peak_rss_bytes'],'exact_entries':result['symbols']['exact_Gaussian_integer_entries']}))
    print('TOTAL: PASS=4 FAIL=0')

if __name__=='__main__':main()
