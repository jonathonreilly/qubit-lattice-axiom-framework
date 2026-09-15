#!/usr/bin/env python3
"""Independent finite geometry and positive integral challenges for block21."""
from pathlib import Path
import itertools,json,math
import numpy as np
from scipy.sparse import coo_matrix,eye,block_diag,vstack
from scipy.sparse.linalg import splu
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


def nested_projection():
 # Hodge inverse and zero-extension identities are distinct constructions.
 import sympy as s
 small,ds=complex_box(4,1);large,dl=complex_box(4,2)
 ext=[]
 for r in range(5):
  ids={cell:i for i,cell in enumerate(large[r])}
  rows=[ids[cell] for cell in small[r]]
  ext.append(coo_matrix((np.ones(len(rows),dtype=np.int64),(rows,np.arange(len(rows)))),shape=(len(large[r]),len(small[r]))).tocsr())
 assert zero(dl[2].T@ext[3]-ext[2]@ds[2].T)
 assert zero(dl[1].T@ext[2]@ds[2].T)
 Dsmall=s.Matrix(np.vstack([ds[2].T.toarray(),ds[3].toarray()]))
 Hsmall=Dsmall.T*Dsmall;Psmall=Dsmall*Hsmall.inv()*Dsmall.T
 assert Psmall*Psmall==Psmall
 assert Psmall[24:25,24:25]==s.eye(1)
 assert Psmall[:24,24:25]==s.zeros(24,1)
 assert s.Matrix(ds[1].T.toarray())*Psmall[:24,:24]==s.zeros(len(small[1]),24)
 Dlarge=vstack([dl[2].T,dl[3]]).astype(float).tocsr()
 Hlarge=(Dlarge.T@Dlarge).tocsc()
 Plarge=Dlarge@splu(Hlarge).solve(Dlarge.T.toarray())
 E=block_diag([ext[2],ext[4]]).toarray()
 embedded=E@np.array(Psmall,dtype=float)@E.T
 nesting=np.linalg.norm(Plarge@embedded-embedded)
 minimum=float(np.linalg.eigvalsh(Plarge-embedded).min())
 assert nesting<2e-12 and minimum>-2e-12
 # Closed free-box three-charges do NOT obey the analogous zero-extension
 # rule. The two opposite 012 faces form a closed relative charge here.
 q=np.zeros(len(small[3]),dtype=np.int64);q[:2]=1
 assert np.max(abs(ds[3]@q))==0
 wrong=dl[3]@ext[3]@q
 assert np.max(abs(wrong))>0
 return dict(small_projection_rank=int(s.trace(Psmall)),large_projection_rank=int(round(np.trace(Plarge))),exact_codifferential_extension=True,nesting_error=float(nesting),minimum_projection_order_eigenvalue=minimum,wrong_closed_charge_extension_defect=wrong.tolist())


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
 covariance=points.T@(w0[:,None]*points)
 lower=K@np.linalg.inv(np.eye(3)+delta*K)
 upper=K@np.linalg.inv(np.eye(3)-delta*K)
 lower_margin=float(np.linalg.eigvalsh(Q.T@(covariance-lower)@Q).min())
 upper_margin=float(np.linalg.eigvalsh(Q.T@(upper-covariance)@Q).min())
 assert lower_margin>=-3e-12 and upper_margin>=-3e-12
 mean=float(w0@(points@a));var=float(w0@((points@a-mean)**2))
 for t in [.1,.3,1.,2.]:
  exact=math.log(float(np.sum(wg*np.exp(interaction+t*(points@a))))/z0)
  rem=abs(exact-t*mean-t*t*var/2);bound=M3*C**3*float(np.linalg.norm(t*a,ord=3))**3/6
  assert rem<=bound+3e-13
  rows.append(dict(source_scale=t,log_mgf_remainder=rem,derived_bound=bound))
 return dict(order=order,k_schur=k,delta=delta,M3=M3,contraction=k*delta,cramer_rao_lower_margin=lower_margin,convexity_upper_margin=upper_margin,cases=rows)


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


def theta_upper_hypothesis_control():
 x,w=hermgauss(100);z=np.sqrt(2)*x
 weights=w*np.exp(-.2*np.cos(z));weights/=weights.sum()
 variance=float(weights@(z*z))
 assert variance>1.05
 return dict(variance=variance,reference_variance=1.,hessian_perturbation_bound=.2,qualification='A uniformly convex small cosine perturbation need not have covariance below its Gaussian reference. The actual theta MGF domination is a separate structural input.')

if __name__=='__main__':
 low=positive_integrals(40);high=positive_integrals(60)
 comparison=max(abs(a.get('third_cumulant',a.get('log_mgf_remainder'))-b.get('third_cumulant',b.get('log_mgf_remainder'))) for a,b in zip(low['cases'],high['cases']))
 assert comparison<3e-12
 result=dict(reflection=reflection(),nested_projection=nested_projection(),positive_integrals=high,quadrature_order_comparison=comparison,collective_control=collective_control(),theta_upper_hypothesis_control=theta_upper_hypothesis_control(),qualification='Exact finite incidence identities and deterministic positive integrals challenge the proof. No Riesz lp theorem, stationary-flow differentiability theorem, covariance homogenization, or physical state matching is established by finite checks.')
 Path(__file__).with_name('BLOCK21_REFLECTION_FLOW_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
