#!/usr/bin/env python3
"""Independent finite controls for the lattice Poisson/MGF current theorem."""
AUDIT_TIMEOUT_SEC = 180
from pathlib import Path
import itertools,json,math
import numpy as np
import sympy as sp

def complex_matrices(d):
 cells=[]
 for k in range(d+1):
  ck=[]
  for I in itertools.combinations(range(d),k):
   for bits in itertools.product([0,1],repeat=d-k):
    x=[0]*d
    for mu,b in zip([i for i in range(d) if i not in I],bits):x[mu]=b
    ck.append((tuple(x),I))
  cells.append(ck)
 deriv=[]
 for k in range(d):
  ids={c:i for i,c in enumerate(cells[k])};D=sp.zeros(len(cells[k+1]),len(cells[k]))
  for row,(x,J) in enumerate(cells[k+1]):
   for pos,mu in enumerate(J):
    I=J[:pos]+J[pos+1:];upper=list(x);upper[mu]+=1
    D[row,ids[(tuple(upper),I)]]+=(-1)**pos;D[row,ids[(x,I)]]-=(-1)**pos
  deriv.append(D)
 for k in range(d-1):assert deriv[k+1]*deriv[k]==sp.zeros(len(cells[k+2]),len(cells[k]))
 # A canonical rooted spanning tree from incidence endpoints.
 incidence=deriv[0];seen={0};tree=[]
 while len(seen)<len(cells[0]):
  for e in range(len(cells[1])):
   vertices=[i for i in range(len(cells[0])) if incidence[e,i]]
   if len(set(vertices)&seen)==1:
    tree.append(e);seen.update(vertices);break
  else:raise AssertionError('no spanning tree')
 non_tree=[i for i in range(len(cells[1])) if i not in tree];D=deriv[1][:,non_tree];Q=D.T*D;Qi=Q.inv();Pe=D*Qi*D.T;Pp=sp.eye(D.rows)-Pe
 assert D.rank()==D.cols and Pe*Pe==Pe and Pp*D==sp.zeros(D.rows,D.cols)
 rows=list(D.T.rref()[1]);minor=D[rows,:].det();assert abs(minor)==1
 complement=[i for i in range(D.rows) if i not in rows];R=sp.eye(D.rows)[:,complement];assert abs(D.row_join(R).det())==1
 B=R.T*Pp*R;M=Qi*D.T*R
 assert B.det()>0
 return dict(d=d,cells=cells,deriv=deriv,D=D,Q=Q,Qi=Qi,Pe=Pe,Pp=Pp,R=R,B=B,M=M,non_tree=non_tree,tree=tree)


def grid(r,K):return np.array(list(itertools.product(range(-K,K+1),repeat=r)),dtype=float)
def stats(x,w):
 z=float(w.sum());mean=w@x/z;cov=(x.T*w)@x/z-np.outer(mean,mean)
 return z,mean,cov

def nonsquare_lattice():
 B=np.array([[2.,1.],[0.,3.]]);A=np.array([[1.7,.3],[.3,.9]]);Ai=np.linalg.inv(A);C=2*np.pi/(abs(np.linalg.det(B))*math.sqrt(np.linalg.det(A)))
 nu=[(np.zeros(2),.5),(np.array([.31,-.22]),.25),(-np.array([.31,-.22]),.25)]
 x=grid(2,10)@B.T;k=grid(2,24)@np.linalg.inv(B)
 chi=sum(p*np.cos(2*np.pi*x@b) for b,p in nu);w=np.exp(-np.einsum('bi,ij,bj->b',x,A,x)/2)*chi
 assert min(w)>-1e-16
 z,mean,cov=stats(x,w);dualz=0.;dcov=np.zeros((2,2));mgfs=np.zeros(3);cosets=np.zeros(3,dtype=complex)
 hs=[np.array([.2,-.6]),np.array([1.3,.4]),np.array([-.5,.7])];ss=[np.array([.11,.07]),B@np.array([1.,0.]),np.array([.24,-.33])]
 for b,p in nu:
  R=k-b;v=p*np.exp(-2*np.pi**2*np.einsum('bi,ij,bj->b',R,Ai,R));dualz+=v.sum();dcov+=(R.T*v)@R
  for i,h in enumerate(hs):mgfs[i]+=v@np.cos(2*np.pi*R@Ai@h)
  for i,s in enumerate(ss):cosets[i]+=v@np.exp(2j*np.pi*k@s)
 assert abs(C*dualz-z)<1e-12
 target=Ai-4*np.pi**2*Ai@(dcov/dualz)@Ai
 assert np.max(abs(cov-target))<1e-12 and max(abs(mean))<1e-14
 rows=[]
 for i,(h,s) in enumerate(zip(hs,ss)):
  lhs=float(w@np.exp(x@h)/z);rhs=float(np.exp(h@Ai@h/2)*mgfs[i]/dualz);assert abs(lhs-rhs)<1e-12 and lhs<=np.exp(h@Ai@h/2)+1e-13
  xx=x+s;ww=np.exp(-np.einsum('bi,ij,bj->b',xx,A,xx)/2)*sum(p*np.cos(2*np.pi*xx@b) for b,p in nu)
  ratio=float(ww.sum()/z);assert abs(ratio-cosets[i]/dualz)<1e-12
  rows.append(dict(h=h.tolist(),s=s.tolist(),mgf=lhs,poisson_mgf=rhs,gaussian_bound=float(np.exp(h@Ai@h/2)),coset=ratio))
 return dict(covolume=abs(float(np.linalg.det(B))),normalization_error=float(abs(C*dualz-z)),covariance_error=float(np.max(abs(cov-target))),cases=rows)

def actual_current_cube():
 C=complex_matrices(3);D=np.array(C['D']).astype(int);Q=np.array(C['Q']).astype(float);Qi=np.array(C['Qi']).astype(float);M=np.array(C['M']).astype(float).ravel();r=len(M);N=2;beta=.5
 A=N*N/beta*Qi;Ai=beta/(N*N)*Q;normal=(2*np.pi)**(r/2)/math.sqrt(np.linalg.det(A));x=grid(r,7);k0=grid(r,6);m=np.arange(-8,9);p=np.exp(-2*np.pi**2*beta*float(C['B'][0])*m*m);p/=p.sum()
 # Two genuinely different summations: positive current lattice and the shifted dual.
 residue=np.rint((N*x)@(6*M)).astype(int)%6
 mag=np.cos(2*np.pi*np.arange(6)[:,None]*m[None,:]/6)@p
 assert min(mag)>0
 w=np.exp(-np.einsum('bi,ij,bj->b',x,A,x)/2)*mag[residue];z,mean,cov=stats(x,w)
 h=np.array([.2,-.3,.1,.4,-.2]);J=D[0].astype(float);s=J/N
 current_mgf=float(w@np.exp(x@h)/z)
 xx=x+s;classes=np.rint((N*xx)@(6*M)).astype(int)%6;zs=float((np.exp(-np.einsum('bi,ij,bj->b',xx,A,xx)/2)*mag[classes]).sum())
 dualz=0.;dcov=np.zeros((r,r));dualchar=0.;wilson=0.;wrong_wilson=0.;rep_error=0.
 ell=np.array([1.,-2.,0.,1.,3.])
 for mm,pp in zip(m,p):
  b=N*M*mm;k=k0+np.rint(b);R=k-b;v=pp*np.exp(-2*np.pi**2*np.einsum('bi,ij,bj->b',R,Ai,R));dualz+=v.sum();dcov+=(R.T*v)@R
  dualchar+=v@np.cos(2*np.pi*R@Ai@h);wilson+=v@np.cos(2*np.pi*k@s);wrong_wilson+=v@np.cos(2*np.pi*R@s)
  shifted_b=b+N*ell*mm;shifted_k=k+N*ell*mm
  rep_error=max(rep_error,float(np.max(abs((shifted_k-shifted_b)-R))),float(np.max(abs(np.cos(2*np.pi*shifted_k@s)-np.cos(2*np.pi*k@s)))))
 target=Ai-4*np.pi**2*Ai@(dcov/dualz)@Ai
 assert abs(normal*dualz-z)<3e-10 and np.max(abs(cov-target))<3e-10
 assert abs(current_mgf-np.exp(h@Ai@h/2)*dualchar/dualz)<3e-10
 assert abs(zs/z-wilson/dualz)<3e-10 and rep_error<1e-12
 # Direct N^5 clock enumeration is independent of the two lattice sums.
 theta=2*np.pi*np.array(list(itertools.product(range(N),repeat=r)))/N;u=theta@D.T;images=np.arange(-12,13);pw=np.exp(-beta*(u[...,None]-2*np.pi*images)**2/2).sum(-1).prod(1)
 direct=float(pw@np.cos(theta@J)/pw.sum());assert abs(direct-zs/z)<3e-10
 # A charge-N source is exactly the identity, in angle and shifted-current representations.
 alias=N*np.eye(r)[0];alias_direct=float(pw@np.cos(theta@alias)/pw.sum());ax=x+alias/N
 alias_classes=np.rint((N*ax)@(6*M)).astype(int)%6
 alias_current=float((np.exp(-np.einsum('bi,ij,bj->b',ax,A,ax)/2)*mag[alias_classes]).sum()/z)
 assert abs(alias_direct-1)<1e-13 and abs(alias_current-1)<3e-10
 # Third representation: the full plaquette Fourier lattice, with modular current constraint.
 flux=grid(D.shape[0],5);integer_div=flux@D;mask=np.all(np.rint(integer_div).astype(int)%N==0,axis=1)
 fw=np.exp(-np.sum(flux*flux,axis=1)/(2*beta));aa=integer_div[mask]/N;fz,fmean,fcov=stats(aa,fw[mask]);fmgf=float(fw[mask]@np.exp(aa@h)/fz)
 source_mask=np.all(np.rint(integer_div+J).astype(int)%N==0,axis=1);fWilson=float(fw[source_mask].sum()/fz)
 assert np.max(abs(fcov-cov))<3e-10 and abs(fmgf-current_mgf)<3e-10 and abs(fWilson-direct)<3e-10
 # Reconstruct integer conserved physical currents from tree-gauge charges.
 incidence=C['deriv'][0];tree=C['tree'];nt=C['non_tree'];T=sp.zeros(incidence.rows,r)
 for j,e in enumerate(nt):T[e,j]=1
 tt=-(incidence[tree,:].T[1:,:]).inv()*incidence[nt,:].T[1:,:]
 for i,e in enumerate(tree):
  for j in range(r):T[e,j]=tt[i,j]
 assert incidence.T*T==sp.zeros(incidence.cols,r)
 assert T*C['Q']*T.T==C['deriv'][1].T*C['deriv'][1]
 return dict(current_rank=r,N=N,beta=beta,normalization_error=float(abs(normal*dualz-z)),covariance_error=float(np.max(abs(cov-target))),mgf=current_mgf,gaussian_bound=float(np.exp(h@Ai@h/2)),wilson_current=zs/z,wilson_dual=float(wilson/dualz),wilson_direct=direct,charge_N_alias_direct=alias_direct,charge_N_alias_current=alias_current,wilson_plaquette_fourier=fWilson,plaquette_covariance_error=float(np.max(abs(fcov-cov))),wrong_R_instead_of_k=float(wrong_wilson/dualz),representative_error=rep_error,integer_current_basis=True)

def discrete_controls():
 n=np.arange(-80,81,dtype=float);rows=[]
 for alpha in (5.,8.,16.,32.,64.):
  centered=np.exp(-alpha*n*n/2);centered/=centered.sum();shifted=np.exp(-alpha*(n-.5)**2/2);shifted/=shifted.sum();vc=float(centered@(n*n));vt=float(shifted@((n-.5)**2));assert vc<=1/alpha and vt>=.25-1e-15 and vt>1/alpha
  h=alpha/2;mgf=float(np.exp(-alpha*n*n/2+h*n).sum()/np.exp(-alpha*n*n/2).sum());assert mgf<=np.exp(h*h/(2*alpha))*(1+1e-13)
  rr=math.exp(-alpha/2);upper=2*rr*(1+rr)/(1-rr)**3;assert vc<=upper
  rows.append(dict(alpha=alpha,centered_variance=vc,tilted_variance=vt,continuous_bound=1/alpha,alpha_times_centered_variance=alpha*vc,mgf=mgf))
 # Signed mixing measure is not admissible even when every lattice weight is positive.
 alpha=8.;p=.99;chi=(1-p*np.cos(np.pi*n))/(1-p);w=np.exp(-alpha*n*n/2)*chi;var=float(w@(n*n)/w.sum());assert var>1/alpha
 # A positive mixing measure alone does not make signed lattice weights a probability.
 signed=np.exp(-alpha*n*n/2)*np.cos(np.pi*n);assert signed[81]<0
 zeros=.5+.5*np.cos(2*np.pi*(n+.5));assert np.max(abs(zeros))<1e-14
 return dict(half_integer_zero_coset_max=float(np.max(abs(zeros))),half_shift_cases=rows,signed_mixture_variance=var,signed_mixture_gaussian_bound=1/alpha,positive_mixture_negative_weight=float(signed[81]))

def hodge_edge_bounds():
 rows=[]
 for d in (3,4):
  C=complex_matrices(d);d0,d1=C['deriv'][:2];H=d0*d0.T+d1.T*d1;P=d1.T*(d1*d1.T).pinv()*d1
  assert H*P==P*H and H*P==d1.T*d1
  assert all(0<=P[i,:].dot(H*P[:,i])<=H[i,i]<=2*d for i in range(H.rows))
  rows.append(dict(d=d,edges=H.rows,max_H_diagonal=int(max(H[i,i] for i in range(H.rows))),max_conserved_diagonal=str(max((H*P)[i,i] for i in range(H.rows))),tail_denominator=4*(d-1)))
 return rows

def run():return dict(nonorthogonal_lattice=nonsquare_lattice(),actual_three_cube=actual_current_cube(),hypothesis_and_tilt_controls=discrete_controls(),local_edge_bounds=hodge_edge_bounds())
if __name__=='__main__':
 rows=run()
 print(json.dumps(rows,indent=2))
 print('TOTAL: PASS=4 FAIL=0')
 print('per_element: executed exact finite-cube incidence, integer current basis and Hodge projector identities with charge-N aliases.')
 print('per_site: executed local edge diagonal bounds and half-shifted scalar controls; the arbitrary-volume density estimate is a written Chernoff proof.')
 print('per_mode: executed nonorthogonal-lattice Gaussian Poisson transforms, moment generating functions, covariance identities and distinct Wilson variables.')
 print('per_block: executed actual single-three-cube current, shifted dual, direct32-state clock and constrained plaquette-Fourier evaluations at identical parameters.')
 print('lattice_wide: checked and not executed: general full-rank lattice identities and all-volume centered bounds rely on the written proof; nondegenerate fixed-law photon correlations remain open.')
