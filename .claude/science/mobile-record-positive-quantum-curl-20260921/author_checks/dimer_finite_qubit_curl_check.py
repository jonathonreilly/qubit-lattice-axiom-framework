#!/usr/bin/env python3
"""Finite qubit occupancy, discrete curl and controlled-limit corroboration."""
from pathlib import Path
from itertools import product
import hashlib,json,math
import numpy as np
import sympy as s
from scipy import sparse as sp
from scipy.sparse.linalg import expm_multiply
ROOT=Path(__file__).resolve().parent

def basis(cap):
 return [(a,b,c) for a in range(cap+1) for b in range(cap+1-a) for c in range(cap+1-a-b)]

def physical_occupation_controls():
 rows=[]
 for K in [1,2,3]:
  states=list(product(range(4),repeat=K));lookup={x:i for i,x in enumerate(states)};bs=basis(K);U=s.zeros(4**K,len(bs))
  for j,n in enumerate(bs):
   chosen=[i for i,x in enumerate(states) if tuple(x.count(a) for a in [1,2,3])==n]
   expected=math.factorial(K)//(math.factorial(K-sum(n))*math.prod(math.factorial(a) for a in n))
   assert len(chosen)==expected
   for i in chosen:U[i,j]=1/s.sqrt(expected)
  assert U.T*U==s.eye(len(bs));bi={x:i for i,x in enumerate(bs)};transitions=0
  for mode in range(3):
   op=s.zeros(4**K)
   for col,conf in enumerate(states):
    for pos in range(K):
     if conf[pos]!=mode+1:continue
     changed=list(conf);changed[pos]=0;op[lookup[tuple(changed)],col]+=1/s.sqrt(K)
   exact=s.zeros(len(bs))
   for col,n in enumerate(bs):
    if not n[mode]:continue
    changed=list(n);changed[mode]-=1
    exact[bi[tuple(changed)],col]=s.sqrt(s.Rational(n[mode]*(K-sum(n)+1),K));transitions+=1
   assert s.simplify(U.T*op*U-exact)==s.zeros(len(bs))
   assert s.simplify(op*U-U*exact)==s.zeros(4**K,len(bs))
  rows.append(dict(K=K,physical_dimension=4**K,symmetric_dimension=len(bs),exact_nonzero_lowering_entries=transitions))
 return rows

def quadratures(cap,K=None):
 bs=basis(cap);bi={x:i for i,x in enumerate(bs)};n=np.array([sum(x) for x in bs]);low=[]
 for mode in range(3):
  rows=[];cols=[];values=[]
  for col,occ in enumerate(bs):
   if not occ[mode]:continue
   new=list(occ);new[mode]-=1
   factor=1 if K is None else math.sqrt(max(1-(sum(occ)-1)/K,0))
   rows.append(bi[tuple(new)]);cols.append(col);values.append(math.sqrt(occ[mode])*factor)
  low.append(sp.csr_matrix((values,(rows,cols)),shape=(len(bs),len(bs))))
 Q=[(a+a.T)/math.sqrt(2) for a in low];P=[1j*(a.T-a)/math.sqrt(2) for a in low]
 return bs,n,Q,P

def ham(Q,P,omega2):
 return sum((p@p for p in P),sp.csr_matrix(P[0].shape, dtype=complex))/2+sum((omega2[i]*(Q[i]@Q[i]) for i in range(3)),sp.csr_matrix(P[0].shape,dtype=complex))/2

def curl_controls():
 rows=[]
 for L in [3,4]:
  xyz=list(product(range(L),repeat=3));index={x:i for i,x in enumerate(xyz)};V=len(xyz);D=[]
  for axis in range(3):
   rr=[];cc=[];vv=[]
   for row,x in enumerate(xyz):
    for sign in [-1,1]:
     y=list(x);y[axis]=(y[axis]+sign)%L;rr.append(row);cc.append(index[tuple(y)]);vv.append(sign)
   D.append(sp.csr_matrix((vv,(rr,cc)),shape=(V,V),dtype=np.int64))
  assert all((d+d.T).nnz==0 for d in D)
  assert all((a@b-b@a).nnz==0 for a in D for b in D)
  Z=sp.csr_matrix((V,V),dtype=np.int64)
  C=sp.bmat([[Z,-D[2],D[1]],[D[2],Z,-D[0]],[-D[1],D[0],Z]],format='csr')
  assert (C-C.T).nnz==0
  Div=sp.hstack(D,format='csr');assert (Div@C).nnz==0
  eig=np.linalg.eigvalsh(C.toarray()/2);zeros=int(np.sum(abs(eig)<1e-10))
  zero_momenta=(2 if L%2==0 else 1)**3
  assert zeros==V+2*zero_momenta
  residual=0.0
  coords=np.array(xyz)
  for kk in product(range(L),repeat=3):
   k=2*np.pi*np.array(kk)/L;v=np.sin(k);phase=np.exp(1j*coords@k)
   symbol=1j*np.array([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]])
   for j in range(3):
    field=np.zeros((3,V),complex);field[j]=phase
    actual=(C@field.ravel()/2).reshape(3,V);expected=symbol[:,j,None]*phase[None,:]
    residual=max(residual,float(np.max(abs(actual-expected))))
  assert residual<1e-13
  rows.append(dict(L=L,vector_dimension=3*V,exact_adjoint_and_divergence=True,zero_momenta=zero_momenta,curl_nullity=zeros,derivative_EB_bracket_rank=2*(3*V-zeros),max_Fourier_residual=residual))
 return rows

def gaussian_target(t,z,omega2):
 S=np.zeros((6,6))
 for i,w2 in enumerate(omega2):
  if w2==0:co=1;si=t;lo=0
  else:
   w=math.sqrt(w2);co=math.cos(w*t);si=math.sin(w*t)/w;lo=-w*math.sin(w*t)
  S[i,i]=S[3+i,3+i]=co;S[i,3+i]=si;S[3+i,i]=lo
 return float(np.exp(-.25*z@(S@S.T)@z))

def limit_controls():
 w2=np.array([0,.75,.75]);bs,n,Q,P=quadratures(5);H=ham(Q,P,w2);core=np.flatnonzero(n<=3);core_rows=[]
 for K in [4,8,16,32,64,128]:
  _,_,q,p=quadratures(5,K);diff=(ham(q,p,w2)-H)[:,core].toarray();weighted=diff/((n[core]+1)**2)[None,:]
  norm=float(np.linalg.norm(weighted,2));assert K*norm<2
  core_rows.append(dict(K=K,core_maximum_number=3,output_cutoff=5,weighted_difference_norm=norm,K_scaled_norm=K*norm))
 zs=[np.array([.3,.2,-.1,.4,-.2,.3]),np.array([0,0,.7,0,.6,0])]
 dyn=[]
 for K in [4,8,16,32]:
  bs,n,Q,P=quadratures(K,K);H=ham(Q,P,w2);assert np.max(abs((H-H.getH()).data),initial=0)<1e-13
  if K==4:assert np.linalg.eigvalsh(H.toarray()).min()>-1e-12
  psi=np.zeros(len(bs),complex);psi[bs.index((0,0,0))]=1
  for t in [.25,.75,1.25]:
   evolved=expm_multiply((-1j*t)*H,psi);assert abs(np.vdot(evolved,evolved)-1)<2e-11
   for zi,z in enumerate(zs):
    W=sum((z[i]*Q[i]+z[3+i]*P[i] for i in range(3)),sp.csr_matrix(H.shape,dtype=complex))
    after=expm_multiply(1j*W,evolved);actual=np.vdot(evolved,after);target=gaussian_target(t,z,w2)
    error=abs(actual-target)
    if K==32:assert error<.02
    dyn.append(dict(K=K,dimension=len(bs),t=t,observable=zi,real=float(actual.real),imag=float(actual.imag),gaussian_target=target,absolute_error=float(error)))
  print('finite block K='+str(K)+' completed',flush=True)
 return dict(weighted_core_differences=core_rows,finite_block_Weyl_dynamics=dyn,
  scope='One three-mode block with squared frequencies (0,3/4,3/4), matching a nonzero L3 curl spectrum. This is a local polynomial control, not a simulation of the full coupled cubic lattice. Exact occupancy and discrete-curl controls are separate. No cutoff is imposed on the finite physical K block.')

def main():
 out=ROOT/'dimer_finite_qubit_curl_checks';out.mkdir(exist_ok=True);target=out/'RESULTS.json';assert not target.exists()
 groups={}
 for name,fn in [('physical_occupation',physical_occupation_controls),('discrete_curl',curl_controls),('finite_block_limit',limit_controls)]:
  groups[name]=fn();(out/(name+'.json')).write_text(json.dumps(groups[name],indent=2)+'\n');print(name+' PASS',flush=True)
 sources={n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in ['DIMER_FINITE_QUBIT_POSITIVE_CURL_LIMIT.md',Path(__file__).name]}
 target.write_text(json.dumps(dict(sources_sha256=sources,groups=groups),indent=2)+'\n')
if __name__=='__main__':main()
