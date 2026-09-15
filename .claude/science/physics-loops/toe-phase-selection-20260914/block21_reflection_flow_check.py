#!/usr/bin/env python3
"""Independent finite geometry and positive integral challenges for block21."""
from pathlib import Path
import itertools,json,math
import numpy as np
from scipy.sparse import coo_matrix,eye
from numpy.polynomial.hermite import hermgauss


def complex_box(d,L,periodic=False):
 side=2*(L+1);levels=[]
 for r in range(d+1):
  lev=[]
  for I in itertools.combinations(range(d),r):
   sizes=[side if periodic else (L if j in I else L+1) for j in range(d)]
   lev.extend((x,I) for x in itertools.product(*(range(n) for n in sizes)))
  levels.append(lev)
 ds=[]
 for r in range(d):
  ids={c:i for i,c in enumerate(levels[r])};rows=[];cols=[];vals=[]
  for a,(x,J) in enumerate(levels[r+1]):
   for j,mu in enumerate(J):
    I=J[:j]+J[j+1:];y=list(x);y[mu]+=1
    if periodic:y[mu]%=side
    rows.extend([a,a]);cols.extend([ids[(tuple(y),I)],ids[(x,I)]]);vals.extend([(-1)**j,-(-1)**j])
  ds.append(coo_matrix((vals,(rows,cols)),shape=(len(levels[r+1]),len(levels[r])),dtype=np.int64).tocsr())
 return levels,ds


def extensions(free,per,d,L):
 N=L+1;ext=[]
 for r in range(d+1):
  ids={c:i for i,c in enumerate(free[r])};rows=[];cols=[];vals=[]
  for a,(x,I) in enumerate(per[r]):
   y=[];sgn=1
   for j,t in enumerate(x):
    if j not in I:y.append(t if t<N else 2*N-1-t)
    else:
     if t in [N-1,2*N-1]:sgn=0;break
     if t<N-1:y.append(t)
     else:y.append(2*N-2-t);sgn*=-1
   if sgn:rows.append(a);cols.append(ids[(tuple(y),I)]);vals.append(sgn)
  ext.append(coo_matrix((vals,(rows,cols)),shape=(len(per[r]),len(free[r])),dtype=np.int64).tocsr())
 return ext


def zero(A):
 A.eliminate_zeros();return A.nnz==0


def reflection():
 rows=[]
 for d,L in [(1,1),(1,2),(1,3),(1,7),(2,1),(2,3),(3,1),(3,2),(4,1),(4,2)]:
  f,df=complex_box(d,L);p,dp=complex_box(d,L,True);E=extensions(f,p,d,L)
  for r in range(d+1):
   assert zero(E[r].T@E[r]-(2**d)*eye(len(f[r]),dtype=np.int64))
   assert np.max(np.diff(E[r].indptr),initial=0)<=1
   if r:assert np.max(abs(np.asarray(E[r].sum(axis=0))),initial=0)==0
   if r<d:
    assert zero(dp[r]@E[r]-E[r+1]@df[r])
    assert zero(dp[r].T@E[r+1]-E[r]@df[r].T)
  # Wrong even extension in an edge direction violates the derivative identity.
  bad=E[1].copy();bad.data=abs(bad.data)
  defect=dp[0]@E[0]-bad@df[0];assert not zero(defect)
  rows.append(dict(d=d,L=L,period=2*(L+1),free_dimensions=list(map(len,f)),periodic_dimensions=list(map(len,p)),both_derivatives_exact=True,norm_multiplicity=2**d,wrong_edge_parity_defect_entries=defect.nnz))
 return rows


def positive_integrals(order=60):
 # A non-coordinate two-dimensional subspace inside R3, non-diagonal K,
 # and several overlapping rank-one interactions.
 V=np.array([[1.,1.],[-1.,1.],[0.,-2.]])
 Q,_=np.linalg.qr(V);eigen=np.array([.7,1.1]);S=Q@np.diag(np.sqrt(eigen));K=S@S.T
 U=np.array([[1.,-1.,0.],[0.,1.,1.],[1.,0.,-1.],[1.,1.,0.]])
 coeff=np.array([.006,-.004,.005,.003]);absu=abs(U);u1=absu.sum(axis=1)
 delta=float(np.max((abs(coeff)*u1)@absu));M3=float(np.max((abs(coeff)*u1*u1)@absu))
 k=float(np.max(abs(K).sum(axis=1)));assert k*delta<1
 C=k/(1-k*delta)
 x,w=hermgauss(order);grid=np.array(list(itertools.product(x,x)));wg=np.outer(w,w).ravel()/np.pi
 points=np.sqrt(2)*grid@S.T;interaction=np.cos(points@U.T)@coeff
 rows=[]
 directions=[np.array([.3,-.2,.1]),np.array([-.2,.15,.45]),np.array([.1,.1,-.2])]
 for tilt in [np.array([0.,0.,0.]),np.array([.2,-.3,.1]),np.array([-.4,.1,.3])]:
  exponent=interaction+points@tilt;weights=wg*np.exp(exponent);norm=weights.sum();weights/=norm
  for a,b,c in [(directions[0],directions[0],directions[0]),tuple(directions)]:
   obs=[points@v for v in [a,b,c]];center=[v-weights@v for v in obs]
   third=float(weights@(center[0]*center[1]*center[2]))
   bound=M3*C**3*math.prod(float(np.linalg.norm(v,ord=3)) for v in [a,b,c])
   assert abs(third)<=bound+2e-12
   rows.append(dict(tilt=tilt.tolist(),third_cumulant=third,derived_bound=bound))
 # Taylor remainder for the exact positive finite measure at zero tilt.
 w0=wg*np.exp(interaction);z0=w0.sum();w0/=z0;a=directions[0]
 mean=float(w0@(points@a));var=float(w0@((points@a-mean)**2))
 for t in [.1,.3,1.,2.]:
  exact=math.log(float(np.sum(wg*np.exp(interaction+t*(points@a))))/z0)
  rem=abs(exact-t*mean-t*t*var/2);bound=M3*C**3*float(np.linalg.norm(t*a,ord=3))**3/6
  assert rem<=bound+3e-13
  rows.append(dict(source_scale=t,log_mgf_remainder=rem,derived_bound=bound))
 return dict(order=order,k_schur=k,delta=delta,M3=M3,contraction=k*delta,cases=rows)


def collective_control():
 # Exact one-dimensional reduction preserves a non-Gaussian fourth cumulant
 # at every ambient dimension. Gauss-Hermite integration is deterministic.
 x,w=hermgauss(100);z=np.sqrt(2)*x;zeta=.4;weights=w*np.exp(zeta*np.cos(z));weights/=weights.sum()
 var=float(weights@(z*z));fourth=float(weights@(z**4))-3*var*var
 assert abs(fourth)>.01
 cases=[]
 for n in [1,4,16,64,256,1024]:
  norm3cubed=n**(-.5);M3=zeta*math.sqrt(n)
  assert abs(M3*norm3cubed-zeta)<1e-14
  cases.append(dict(dimension=n,source_ell3_cubed=norm3cubed,third_influence_bound=M3,product=M3*norm3cubed))
 return dict(variance=var,fourth_cumulant=fourth,dimension_independent_non_gaussian=True,cases=cases)

if __name__=='__main__':
 low=positive_integrals(40);high=positive_integrals(60)
 comparison=max(abs(a.get('third_cumulant',a.get('log_mgf_remainder'))-b.get('third_cumulant',b.get('log_mgf_remainder'))) for a,b in zip(low['cases'],high['cases']))
 assert comparison<3e-12
 result=dict(reflection=reflection(),positive_integrals=high,quadrature_order_comparison=comparison,collective_control=collective_control(),qualification='Exact finite incidence identities and deterministic positive integrals challenge the proof. No Riesz lp theorem, stationary-flow differentiability theorem, covariance homogenization, or physical state matching is established by finite checks.')
 Path(__file__).with_name('BLOCK21_REFLECTION_FLOW_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
