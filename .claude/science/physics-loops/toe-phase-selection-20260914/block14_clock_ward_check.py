#!/usr/bin/env python3
"""Finite independent falsifiers for the conditional mixture/Ward proof."""
import itertools,json,math
import numpy as np
from pathlib import Path
PI=np.pi

def phi(u,b):
 u=np.asarray(u);k=np.arange(-12,13);v=u[...,None]-2*PI*k
 w=np.exp(-b*v*v/2)
 return w.sum(-1),(-b*v*w).sum(-1)

def product(theta,bs,cs):
 p=np.ones_like(np.asarray(theta),dtype=float);logprime=np.zeros_like(p)
 for b,c in zip(bs,cs):
  v,d=phi(np.asarray(theta)+c,b);p*=v;logprime+=d/v
 return p,logprime

def tails(N,G,K=0):
 q=np.arange(1,100,dtype=float);e=np.exp(-(q*N-K)**2/(2*G))
 rho=np.exp(-(3*N*N-2*N*K)/(2*G));z=np.exp(-(N-K)**2/(2*G))
 return dict(eps=float(2*e.sum()),D=float(2*N*(q*e).sum()),eps_geometric=float(2*z/(1-rho)),D_geometric=float(2*N*z/(1-rho)**2))

def run():
 rows={};grid=2*PI*np.arange(16384)/16384
 # Complete-square mixture vs a product of image sums, including Fourier phases.
 mixtures=[]
 cases=[([.3],[.37],0),([.25,.8],[.37,-.63],6),([.5,1.1,.7],[.2,-.6,.4],4),([1.1]*6,[.1,-.4,.6,-.2,.5,-.3],2)]
 for bs,cs,M in cases:
  bs=np.array(bs);cs=np.array(cs);r=len(bs);G=bs.sum()
  ns=np.array([list(n)+[0] for n in itertools.product(range(-M,M+1),repeat=r-1)])
  d=cs[None,:]-2*PI*ns;bar=(d*bs).sum(1)/G
  A=np.exp(-.5*((d-bar[:,None])**2*bs).sum(1))
  theta=np.linspace(-PI,PI,71);direct,_=product(theta,bs,cs)
  mixed=(A[None,:]*phi(theta[:,None]+bar[None,:],G)[0]).sum(1)
  err=float(np.max(abs(direct-mixed))/max(direct));assert err<3e-12
  p,lp=product(grid,bs,cs);p0=p.mean();fourier=[]
  for m in [0,1,2,3,7]:
   actual=np.mean(p*np.exp(-1j*m*grid))/p0
   expected=np.exp(-m*m/(2*G))*np.sum(A*np.exp(1j*m*bar))/A.sum()
   assert abs(actual-expected)<3e-12
   assert abs(actual)<=np.exp(-m*m/(2*G))+3e-12
   fourier.append([m,float(abs(actual)),float(abs(expected))])
  mixtures.append(dict(r=r,Gamma=float(G),relative_product_error=err,fourier=fourier))
 rows['positive_mixture']=mixtures
 # Conditional means, exact alias sum and Fourier-polynomial Ward error.
 wards=[];max_force=0
 for bs,cs in [([.4],[.37]),([1.2],[.37]),([.7,1.3],[.21,-.52]),([1.]*6,[.1,-.4,.6,-.2,.5,-.3])]:
  p,lp=product(grid,bs,cs);p0=p.mean();G=sum(bs)
  for N in [3,5,9,17]:
   tn=2*PI*np.arange(N)/N;pn,lpn=product(tn,bs,cs);e0=tails(N,G)
   assert abs(pn.mean()/p0-1)<=e0['eps']+3e-12
   if e0['eps']>=1:continue
   coeff={0:.3,1:.6+.2j,-1:-.2j}
   f=sum(v*np.exp(1j*k*tn) for k,v in coeff.items());fp=sum(1j*k*v*np.exp(1j*k*tn) for k,v in coeff.items())
   ward=np.sum(pn*(fp+lpn*f))/pn.sum()
   fh=sum(v*np.exp(1j*k*grid) for k,v in coeff.items());fph=sum(1j*k*v*np.exp(1j*k*grid) for k,v in coeff.items())
   total_derivative=p*(fph+lp*fh)
   spectrum=np.fft.fft(total_derivative)/len(grid)
   alias=sum(spectrum[(q*N)%len(grid)] for q in range(-80,81) if q)
   assert abs(ward-alias/pn.mean())<3e-11
   assert abs(np.mean(total_derivative)/p0)<3e-12
   T=tails(N,G,1);B=sum(abs(v) for v in coeff.values());assert abs(ward)<=B*T['D']/(1-e0['eps'])+3e-11
   force=float(-np.sum(pn*lpn)/pn.sum());max_force=max(max_force,abs(force));assert abs(force)<=e0['D']/(1-e0['eps'])+3e-11
   assert T['eps']<=T['eps_geometric']+1e-14 and T['D']<=T['D_geometric']+1e-14
   wards.append(dict(r=len(bs),N=N,Gamma=G,force=force,ward_abs=float(abs(ward)),bound=B*T['D']/(1-e0['eps']),alias_error=float(abs(ward-alias/pn.mean()))))
 assert max_force>1e-3;rows['ward_and_alias']=wards
 # Exact single factor saturation, and forbidden charge-N counterexample.
 controls=[]
 for N,G in [(3,.8),(5,1.),(9,3.)]:
  tn=2*PI*np.arange(N)/N;p,_=phi(tn,G);p0=1/math.sqrt(2*PI*G);T=tails(N,G)
  error=p.mean()/p0-1;assert abs(error-T['eps'])<3e-12
  clock=np.sum(p*np.exp(1j*N*tn))/p.sum();haar=math.exp(-N*N/(2*G));assert abs(clock-1)<1e-12
  controls.append(dict(N=N,Gamma=G,normalization_error=error,saturated_bound=T['eps'],charge_N_clock=float(clock.real),charge_N_Haar=haar))
 rows['sharpness_and_charge_alias']=controls
 # Actual two-square gauge complex: seven edges, one shared edge, direct clock sum.
 F=np.array([[1,1,-1,-1,0,0,0],[0,0,1,0,1,1,-1]],dtype=int)
 bs=[.7,1.1];comp=[]
 for N in [3,5,7]:
  config=np.array(list(itertools.product(range(N),repeat=7)),dtype=np.int16)
  u=2*PI*(config@F.T)/N
  # Periodicity reduction also verifies integer representative invariance.
  u=(u+PI)%(2*PI)-PI
  factors=np.stack([phi(u[:,i],b)[0] for i,b in enumerate(bs)],axis=1);weight=factors.prod(1)
  Zn=float(weight.mean());Zhaar=np.prod([1/math.sqrt(2*PI*b) for b in bs]);G=max(bs)+min(bs);T0=tails(N,G)
  e=7
  if T0['eps']<1:assert (1-T0['eps'])**e-1e-12<=Zn/Zhaar<=(1+T0['eps'])**e+1e-12
  for m in [(1,0),(1,1),(1,-1)]:
   j=np.array(m)@F;K=int(abs(j).max());direct=np.sum(weight*np.exp(1j*(u@np.array(m))))/weight.sum()
   haar=np.exp(-sum(mi*mi/(2*b) for mi,b in zip(m,bs)))
   separate=1.+0j
   for mi,b in zip(m,bs):
    t=2*PI*np.arange(N)/N;w=phi(t,b)[0];separate*=np.sum(w*np.exp(1j*mi*t))/w.sum()
   assert abs(direct-separate)<3e-12
   bound=2 if T0['eps']>=1 else min(2,e*(tails(N,G,K)['eps']+T0['eps'])/(1-T0['eps']))
   assert abs(direct-haar)<=bound+3e-12
   comp.append(dict(N=N,states=N**7,max_link_charge=K,charge=list(m),clock=float(direct.real),haar=float(haar),absolute_error=float(abs(direct-haar)),bound=float(bound)))
 rows['full_gauge_Wilson']=comp
 # Explicit growing order sufficient family; fixed order bound does not shrink with E.
 scaling=[]
 G=6.;K=1;delta=.7
 for E in [100,10000,1000000,100000000]:
  N=math.ceil(K+math.sqrt(2*G*(1+delta)*math.log(2*E)));T=tails(N,G,K);T0=tails(N,G)
  err=E*(T['eps']+T0['eps'])/(1-T0['eps']);D=E*T['D']/(1-T0['eps'])
  scaling.append(dict(E=E,N=N,comparison_bound=err,summed_Ward_bound=D))
 assert scaling[-1]['comparison_bound']<scaling[0]['comparison_bound']/100
 rows['growing_order']=scaling
 return rows

if __name__=='__main__':
 rows=run();out=Path(__file__).with_name('BLOCK14_CHECKS.json');out.write_text(json.dumps(rows,indent=2)+'\n')
 print(json.dumps(rows,indent=2))
