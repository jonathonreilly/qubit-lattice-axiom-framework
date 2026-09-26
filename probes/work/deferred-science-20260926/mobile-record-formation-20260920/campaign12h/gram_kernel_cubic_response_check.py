#!/usr/bin/env python3
"""Whole finite Markov-generator Taylor jets versus a marked-pair reduction.

The four-site ring has two neighbors per site. This finite diagnostic tests
the alphabet-dependent closure and coefficient ratio, not the separate
three-dimensional Green-function theorem.
"""
from pathlib import Path
from itertools import product, combinations
import hashlib,json,time
import numpy as np
import sympy as s
from scipy.sparse import coo_matrix,bmat
from scipy.sparse.linalg import expm_multiply
from scipy.integrate import solve_ivp

HERE=Path(__file__).resolve().parent
OUT=HERE/'gram_kernel_cubic_response';OUT.mkdir(exist_ok=True)
checks=[]
def check(name,ok,detail=None):
    assert bool(ok),(name,detail)
    checks.append(dict(name=name,passed=True,detail=detail));print('PASS:',name,flush=True)
unit=[s.eye(3)[:,i] for i in range(3)]
A=[sign*unit[i] for i in range(3) for sign in (-1,1)]
B=[s.Matrix(signs) for signs in product((-1,1),repeat=3)]
original=s.Matrix([list(v)+[0]*3 for v in A]+[[0]*3+list(v/2) for v in B])
born=s.Matrix([list(v) for v in A]+[list(v/s.sqrt(3)) for v in B])
old=s.Matrix([list(v) for v in A])
matrices={'old_six_axis':old,'original_fourteen':original,'Born_fourteen':born}
invariants={}
for name,F in matrices.items():
    M=F.T*F;n=F.rows
    value=s.trace(M**3)/n
    invariants[name]=value
    assert F.T*s.ones(n,1)==s.zeros(F.cols,1)
    assert all(sum(F[a,i]*F[a,j]*F[a,k] for a in range(n))==0
               for i,j,k in product(range(F.cols),repeat=3))
    check(name+'_Gram_moments',True,dict(n=n,M=str(M),trace_cubed_over_n=str(value)))
check('exact_kernel_coefficient_ratio',s.simplify(invariants['Born_fourteen']/invariants['original_fourteen'])==s.Rational(343,54))

V=4;edges=[(x,(x+1)%V) for x in range(V)]
beta=.2;kappa=.3;acceleration=4;rho0=.4;end=.35
pairs=list(combinations(range(V),2));pair_index={p:i for i,p in enumerate(pairs)}
H=np.zeros((len(pairs),len(pairs)))
for index,pair in enumerate(pairs):
    for x,y in edges:
        image=tuple(sorted(y if q==x else x if q==y else q for q in pair))
        H[index,pair_index[image]]+=1;H[index,index]-=1
source=np.array([int((a-b)%V in (1,V-1)) for a,b in pairs],float)
opposite=pair_index[(1,3)]
results={}
for name,F in matrices.items():
    begin=time.perf_counter();n=F.rows;q=n+1;size=q**V
    table=np.vstack([np.zeros((1,F.cols)),np.array(F,dtype=float)])
    G=table@table.T
    states=np.array(np.unravel_index(np.arange(size),(q,)*V)).T
    strides=q**np.arange(V-1,-1,-1)
    row=[[],[],[]];col=[[],[],[]];value=[[],[],[]]
    def transitions(order,src,dst,rates):
        row[order].extend([dst,src]);col[order].extend([src,src]);value[order].extend([rates,-rates])
    allstates=np.arange(size)
    for x,y in edges:
        dst=allstates+(states[:,y]-states[:,x])*strides[x]+(states[:,x]-states[:,y])*strides[y]
        transitions(0,allstates,dst,np.full(size,kappa*acceleration))
    for x in range(V):
        src=np.flatnonzero(states[:,x]==0)
        for a in range(1,q):
            dst=src+a*strides[x]
            left=G[a,states[src,(x-1)%V]];right=G[a,states[src,(x+1)%V]]
            for order,rate in enumerate([np.full(len(src),beta),beta*(left+right),beta*left*right]):
                transitions(order,src,dst,rate)
    generators=[]
    for r in range(3):
        L=coo_matrix((np.concatenate(value[r]),(np.concatenate(row[r]),np.concatenate(col[r]))),shape=(size,size)).tocsr()
        L.eliminate_zeros();assert max(abs(np.asarray(L.sum(axis=0)).ravel()))<3e-13
        generators.append(L)
    L0,L1,L2=generators
    J=bmat([[L0,None,None,None],[L1,L0,None,None],[L2,L1,L0,None],[None,L2,L1,L0]],format='csr')
    initial=np.prod(np.where(states==0,1-rho0,rho0/n),axis=1)
    jet0=np.r_[initial,np.zeros(size*3)]
    jet=expm_multiply(J*end,jet0,traceA=4*float(L0.diagonal().sum())*end).reshape(4,size)
    occupation=np.count_nonzero(states,axis=1)/V
    density=jet@occupation
    lam=n*beta;traceM3=float(n*invariants[name])
    def reduced(t,y):
        vacancy=(1-rho0)*np.exp(-lam*t);rho=1-vacancy
        covariance=kappa*acceleration*(H@y[:len(pairs)])+(2*beta*rho*vacancy/n)*source
        cubic=-lam*y[-1]+beta*vacancy*traceM3*y[opposite]
        return np.r_[covariance,cubic]
    sol=solve_ivp(reduced,(0,end),np.zeros(len(pairs)+1),method='DOP853',rtol=1e-12,atol=1e-15)
    assert sol.success
    target0=1-(1-rho0)*np.exp(-lam*end)
    assert abs(density[0]-target0)<3e-13 and max(abs(density[1:3]))<3e-13,(name,density)
    error=abs(density[3]-sol.y[-1,-1]);assert error<2e-13,(name,density,sol.y[:,-1],error)
    # Compare the full matrix pair coefficient and a separate vacancy projection.
    feat=table[states]
    pair01=np.einsum('s,si,sj->ij',jet[1],feat[:,0,:],feat[:,1,:])
    M=np.array(F.T*F,dtype=float)
    expected_pair=M@M*sol.y[pair_index[(0,1)],-1]
    assert np.max(abs(pair01-expected_pair))<3e-13
    triple=np.einsum('s,si,sj->ij',jet[1]*(states[:,2]==0),feat[:,0,:],feat[:,1,:])
    vacancy=(1-rho0)*np.exp(-lam*end)
    assert np.max(abs(triple-vacancy*expected_pair))<3e-13
    path=OUT/(name+'_jet.npz');np.savez_compressed(path,states=states,jet=jet,time=end,density_coefficients=density,reduced_solution=sol.y[:,-1])
    result=dict(states=size,jet_dimension=4*size,nonzeros=int(J.nnz),density_coefficients=density.tolist(),
                reduced_cubic=float(sol.y[-1,-1]),cubic_error=float(error),wall_seconds=time.perf_counter()-begin,
                artifact=path.name,artifact_sha256=hashlib.sha256(path.read_bytes()).hexdigest())
    results[name]=result
    check(name+'_full_generator_jet_vs_pair_and_vacancy_closure',True,result)
ratio=results['Born_fourteen']['density_coefficients'][3]/results['original_fourteen']['density_coefficients'][3]
check('full_finite_generator_cubic_ratio',abs(ratio-343/54)<3e-10,dict(measured_ratio=ratio,exact_ratio='343/54'))
report=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,
            parameters=dict(vertices=V,graph='four-site periodic ring, two neighbors per birth',beta=beta,kappa=kappa,acceleration=acceleration,rho0=rho0,time=end),
            scope='Whole finite-generator Taylor jets and independently built reduced marked-pair equations. Numerical controls do not establish the separate 3D heat-kernel limit or fixed-j remainder.')
(HERE/'GRAM_KERNEL_CUBIC_RESPONSE_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
print('TOTAL:',len(checks),'PASS',flush=True)
