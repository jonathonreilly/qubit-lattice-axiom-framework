#!/usr/bin/env python3
"""Exact sparse cochains and distinct finite cluster/convexity controls."""
from pathlib import Path
import itertools,json,math
import numpy as np
import mpmath as mp
mp.mp.dps=50

def exterior(q,d):
 out={}
 for (x,I),v in q.items():
  for mu in range(d):
   if mu in I:continue
   J=tuple(sorted(I+(mu,)));s=(-1)**J.index(mu)
   low=list(x);low[mu]-=1;low=tuple(low)
   out[(low,J)]=out.get((low,J),0)+s*v
   out[(x,J)]=out.get((x,J),0)-s*v
 return {k:v for k,v in out.items() if v}

def add(a,b):
 c=dict(a)
 for k,v in b.items():c[k]=c.get(k,0)+v
 return {k:v for k,v in c.items() if v}

def components(q,d):
 faces={}
 for x,I in q:
  for mu in range(d):
   if mu in I:continue
   J=tuple(sorted(I+(mu,)));low=list(x);low[mu]-=1
   for y in [x,tuple(low)]:faces.setdefault((y,J),[]).append((x,I))
 adj={k:set() for k in q}
 for cells in faces.values():
  for a in cells:adj[a].update(cells)
 remaining=set(q);comps=[]
 while remaining:
  active={min(remaining)};found=set()
  while active:
   x=active.pop();found.add(x);active.update(adj[x]-found)
  comps.append(found);remaining-=found
 return comps

def cancellation():
 rows=[]
 for d,p in [(3,2),(4,3)]:
  I=tuple(range(p-1));direction=p-1
  for R in [4,7,11]:
   n1={};n2={}
   for j in range(R+1):
    x=[0]*d;x[direction]=j;k=(tuple(x),I);n1[k]=1
    if 0<j<R:n2[k]=-1
   q1=exterior(n1,d);q2=exterior(n2,d);Q=add(q1,q2);U={k:1 for k in set(q1)|set(q2)}
   assert not exterior(q1,d) and not exterior(q2,d) and not exterior(Q,d)
   assert len(components(q1,d))==len(components(q2,d))==len(components(U,d))==1
   assert len(components(Q,d))==2 and set(q1)&set(q2)
   s=sum(abs(v) for v in q1.values())+sum(abs(v) for v in q2.values());net=sum(abs(v) for v in Q.values())
   assert s==4*R+4 and net==8
   # Mixed logarithm coefficient for two incompatible marked activities.
   # log(1+z1+z2) has coefficient -1 in z1 z2.
   coefficient=-math.comb(2,1)/2;assert coefficient==-1
   rows.append(dict(d=d,p=p,R=R,total_cluster_mass=s,net_charge_mass=net,net_components=2,carrier_components=1,marked_mixed_Ursell=coefficient,charge1=[dict(x=list(x),I=list(I),v=v) for (x,I),v in sorted(q1.items())],charge2=[dict(x=list(x),I=list(I),v=v) for (x,I),v in sorted(q2.items())]))
 return rows

def graph_index(n,edges):
 result=0;trees=0
 for bits in itertools.product([0,1],repeat=len(edges)):
  chosen=[e for e,b in zip(edges,bits) if b];visited={0}
  while True:
   nxt=visited|{v for u,v in chosen if u in visited}|{u for u,v in chosen if v in visited}
   if nxt==visited:break
   visited=nxt
  if len(visited)==n:
   result+=(-1)**len(chosen)
   trees+=len(chosen)==n-1
 return result,trees

def trees_and_logarithm():
 rows=[]
 for n in range(2,6):
  all_edges=list(itertools.combinations(range(n),2))
  for typ,edges in [('complete',all_edges),('path',[(i,i+1) for i in range(n-1)]),('cycle',sorted(set([(i,(i+1)%n) if i<(i+1)%n else ((i+1)%n,i) for i in range(n)])))]:
   U,T=graph_index(n,edges);assert abs(U)<=T
   if typ=='complete':assert U==(-1)**(n-1)*math.factorial(n-1) and T==n**(n-2)
   if typ=='path':assert U==(-1)**(n-1) and T==1
   rows.append(dict(n=n,kind=typ,U=U,spanning_trees=T))
 # Three species on an incompatibility path: first and third are compatible.
 # The coefficient of xyz in log(1+x+y+z+xz) is +1, not zero or a factorial multiple.
 # From -A^2/2: -xyz twice -> -1; from A^3/3: 6xyz/3 -> +2.
 mixed=-1+2;assert mixed==graph_index(3,[(0,1),(1,2)])[0]
 return dict(graphs=rows,three_species_mixed_coefficient=mixed)

def eulerian(m):
 a=[1]
 for n in range(2,m+1):
  a=[(k+1)*(a[k] if k<len(a) else 0)+(n-k)*(a[k-1] if k>0 else 0) for k in range(n)]
 return a

def constants():
 rows=[]
 for d,p in [(3,2),(4,1),(4,2),(4,3)]:
  Delta=2*(d-p)*(2*p+1);C0=2**d*d*d*6**d;C1=2**d*11**d;m=2*d+2;A=eulerian(m)
  assert sum(A)==math.factorial(m) and all(x>=0 for x in A)
  for beta in [50.,80.,100.,120.]:
   t=math.pi**2*beta/(4*d);r=math.exp(-t/2);u=2*r/(1-r**3);den=1-Delta**2*math.e*u
   if den<=0:continue
   R=math.e*u/den;poly=sum(v*r**k for k,v in enumerate(A));S=r*poly/(1-r)**(m+1)
   direct=sum(k**m*r**k for k in range(1,101));assert abs(S-direct)<=2e-13*max(S,1e-300)
   closed=math.factorial(m)*r/(1-r)**(m+1);assert S<=closed
   eps=4*math.pi**2*C0*C1*R*closed
   safe=(Delta+1)*R<=1 and beta*eps<=.5
   if beta==100:assert safe
   rows.append(dict(d=d,p=p,beta=beta,t=t,root_R=R,KP_left=(Delta+1)*R,beta_epsilon_upper=beta*eps,explicit_sufficient_conditions=safe))
 return rows

def finite_theta_hessian():
 rows=[]
 # One closed loop with four unit charges: exact one-dimensional theta.
 n=np.arange(-40,41);theta=np.linspace(-.5,.5,501)
 for t in [.08,.2,.5,1.]:
  w=np.exp(-4*t*n*n);phase=np.exp(2j*np.pi*theta[:,None]*n);Z=phase@w;Zp=phase@(2j*np.pi*n*w);Zpp=phase@(-(2*np.pi*n)**2*w)
  assert np.max(abs(Z.imag))<1e-12 and min(Z.real)>0
  hess=(Zpp/Z-(Zp/Z)**2).real
  # Independent Poisson representation of the same theta and log Hessian.
  k=np.arange(-40,41);v=theta[:,None]-k;wdual=np.exp(-np.pi**2*v*v/(4*t));zd=wdual.sum(1)
  mean=(wdual*v).sum(1)/zd;variance=(wdual*v*v).sum(1)/zd-mean*mean
  dual_hess=-np.pi**2/(2*t)+(np.pi**2/(2*t))**2*variance
  assert np.max(abs(hess-dual_hess))<1e-8
  # The effective action is quadratic minus log theta: subtract its Hessian.
  precision=10.;effective=precision-hess
  fd=[]
  for j in [0,137,250,499]:
   x=mp.mpf(str(theta[j]));step=mp.mpf('0.00001');mt=mp.mpf(str(t))
   def action(y):
    dual=mp.sqrt(mp.pi/(4*mt))*sum(mp.exp(-mp.pi**2*(y-k)**2/(4*mt)) for k in range(-8,9))
    return precision*y*y/2-mp.log(dual)
   actual=float((action(x+step)-2*action(x)+action(x-step))/step**2)
   assert abs(actual-effective[j])<2e-4
   fd.append(float(abs(actual-effective[j])))
  charge_variance=float(np.sum(n*n*w)/w.sum());assert abs(hess[250]+4*np.pi**2*charge_variance)<1e-10
  rows.append(dict(t=t,minimum_theta=float(min(Z.real)),min_log_hessian=float(min(hess)),max_log_hessian=float(max(hess)),min_effective_hessian=float(min(effective)),poisson_error=float(np.max(abs(hess-dual_hess))),finite_difference_error=max(fd),charge_variance=charge_variance))
 assert rows[0]['min_effective_hessian']<0 and rows[-1]['min_effective_hessian']>0
 return rows

def gaussian_precision():
 rows=[]
 for L in [3,5,8]:
  H=2*np.eye(L)-np.eye(L,k=1)-np.eye(L,k=-1);G=np.linalg.inv(H);c=.125
  residual=np.linalg.inv(G-c*np.eye(L));series=sum(c**k*np.linalg.matrix_power(H,k+1) for k in range(45))
  assert np.linalg.eigvalsh(G-c*np.eye(L)).min()>0
  assert np.linalg.eigvalsh(residual-H).min()>0
  assert np.max(abs(residual-series))<3e-12
  q=np.arange(L)%3-1.;beta=.8;exact=np.exp(-2*np.pi**2*beta*q@G@q)
  split=np.exp(-2*np.pi**2*beta*c*(q@q))*np.exp(-2*np.pi**2*beta*q@(G-c*np.eye(L))@q)
  assert abs(split-exact)<1e-12
  rows.append(dict(L=L,split_error=float(abs(split-exact)),series_error=float(np.max(abs(residual-series))),minimum_precision_increment=float(np.linalg.eigvalsh(residual-H).min())))
 return rows

def source_curvature():
 rows=[];n=np.arange(-20,21);nodes,weights=np.polynomial.hermite.hermgauss(160);weights=weights/math.sqrt(math.pi)
 G=.75;c=.125
 for beta in [.4,1.,2.]:
  t=2*math.pi**2*beta*c;variance=beta*(G-c);phi=math.sqrt(2*variance)*nodes
  w=np.exp(-t*n*n);original=np.exp(-2*math.pi**2*beta*G*n*n)
  for sigma in [0.,.13,.37]:
   phase=np.exp(2j*math.pi*(phi[:,None]+sigma)*n);Z=(phase@w).real;Zp=(phase@(2j*math.pi*n*w)).real;Zpp=(phase@(-(2*math.pi*n)**2*w)).real
   assert min(Z)>0
   normalization=weights@Z;mu=weights*Z/normalization;vprime=Zp/Z;vsecond=Zpp/Z-vprime*vprime
   first=float(mu@vprime);variance_term=float(mu@(vprime*vprime)-first*first);mean_curvature=float(mu@vsecond)
   assert variance_term>=-1e-12
   phase0=np.exp(2j*math.pi*sigma*n);z=(phase0@original).real;zp=(phase0@(2j*math.pi*n*original)).real;zpp=(phase0@(-(2*math.pi*n)**2*original)).real
   direct=zpp/z-(zp/z)**2;combined=mean_curvature+variance_term
   assert abs(normalization-z)<1e-12 and abs(combined-direct)<2e-10
   rows.append(dict(beta=beta,sigma=sigma,mean_curvature=mean_curvature,positive_variance_term=variance_term,combined=combined,direct_charge_curvature=float(direct),error=float(abs(combined-direct))))
 assert max(r['positive_variance_term'] for r in rows)>1
 return rows

def run():return dict(cancellation=cancellation(),trees=trees_and_logarithm(),constants=constants(),finite_theta_hessian=finite_theta_hessian(),gaussian_precision=gaussian_precision(),source_curvature=source_curvature())
if __name__=='__main__':
 rows=run();Path(__file__).with_name('BLOCK15_CHECKS.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows,indent=2))
