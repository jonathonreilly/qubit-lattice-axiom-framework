"""Independent torch complex-matrix density and NumPy transported variations.
No author or predecessor code is imported. Period-one block sector is a
translation invariant subspace of every stated T>=2 torus, not a T=1 theorem.
"""
import itertools as it
import json, math, time
import numpy as np
import torch
from scipy.linalg import expm
from scipy.optimize import minimize
from scipy.special import roots_legendre, ive
from scipy.linalg import eigvalsh

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)
rng=np.random.default_rng(4102809)
checks=[];controls=[];runs=[]
def ck(name,ok,**kw): checks.append(dict(name=name,passed=bool(ok),**kw))
def neg(name,ok,**kw): controls.append(dict(name=name,rejected=bool(ok),**kw))
I=np.eye(2,dtype=complex)
pauli=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex)
basis=1j*pauli/math.sqrt(2)
L=3;h=1;coords=list(it.product(range(-h,h+1),repeat=4));ci={x:i for i,x in enumerate(coords)}
def plus(x,mu,s=1):
 y=list(x);y[mu]+=s;return tuple(y)
def mod(x):return tuple((t+h)%L-h for t in x)
def ei(x,mu):return 4*ci[mod(x)]+mu
ned=4*L**4;pad=ned
edges=[(x,mu) for x in coords for mu in range(4)]
tree=set()
for r in coords:
 if not any(r):continue
 mu=max(i for i in range(4) if r[i]);sg=1 if r[mu]>0 else -1
 parent=plus(r,mu,-sg);tree.add(ei(parent if sg==1 else r,mu))
free=np.array([e for e in range(ned) if e not in tree],int);nf=len(free);dim=3*nf
freeindex=np.full(ned+1,-1,int);freeindex[free]=np.arange(nf)
assert nf==244

def pathsteps(x,y,order):
 out=[];x=tuple(x)
 for mu in order:
  while x[mu]!=y[mu]:
   sg=1 if y[mu]>x[mu] else -1;out.append((ei(x if sg==1 else plus(x,mu,-1),mu),sg));x=plus(x,mu,sg)
 assert x==tuple(y)
 return out
paths=[];pathmu=[];maxlen=0
for mu in range(4):
 end=plus((0,0,0,0),mu,L)
 for off in coords:
  other=plus(off,mu,L)
  for order in it.permutations(range(4)):
   word=pathsteps((0,0,0,0),off,order)+pathsteps(off,other,[mu])+pathsteps(other,end,tuple(reversed(order)))
   paths.append(word);pathmu.append(mu);maxlen=max(maxlen,len(word))
plaq=[]
for x in coords:
 for mu,nu in it.combinations(range(4),2):
  plaq.append([(ei(x,mu),1),(ei(plus(x,mu),nu),1),(ei(plus(x,nu),mu),-1),(ei(x,nu),-1)])
def arrays(words):
 length=max(len(w) for w in words);ix=np.full((len(words),length),pad,int);sg=np.ones_like(ix)
 for j,w in enumerate(words):
  for k,(e,s) in enumerate(w):ix[j,k]=e;sg[j,k]=s
 return ix,sg
pix,psg=arrays(paths);wix,wsg=arrays(plaq);pathmu=np.array(pathmu);nper=len(paths)//4
ck('actual local matrix-path inventory',len(paths)==7776 and len(plaq)==486 and maxlen==11,paths=len(paths),plaquettes=len(plaq),free_links=nf,max_length=maxlen)

def su2(v):return expm(np.einsum('a,aij->ij',np.asarray(v),basis))
def base(V):
 out=np.repeat(I[None],ned+1,axis=0)
 for e,(x,mu) in enumerate(edges):
  if x[mu]==h:out[e]=V[mu]
 return out

def products(U,ix,sg):
 P=torch.eye(2,dtype=torch.complex128).expand(len(ix),2,2)
 ix=torch.as_tensor(ix);sg=torch.as_tensor(sg)
 for k in range(ix.shape[1]):
  a=U[ix[:,k]];a=torch.where((sg[:,k]>0)[:,None,None],a,a.mH);P=P@a
 return P

def logj(a):
 w=(a*a).sum(dim=1)/2
 exact=2*torch.log(torch.sinc(torch.sqrt(torch.clamp(w,min=1e-30))/math.pi))
 series=-w/3-w*w/90-2*w*w*w/2835
 return torch.where(w<1e-5,series,exact)

def links(a,V):
 ae=torch.zeros((ned+1,3)).index_copy(0,torch.as_tensor(free),a)
 Aa=torch.einsum('ea,aij->eij',ae.to(torch.complex128),torch.as_tensor(basis))
 return torch.matrix_exp(Aa)@torch.as_tensor(base(V))

def pieces(a,V,u=5.,kap=.8,treephase=False):
 U=links(a,V);P=products(U,wix,wsg);Tp=products(U,pix,psg)
 M=Tp.reshape(4,nper,2,2).mean(dim=1)
 # Real SU(2) arithmetic means are quaternions. Their norm follows from matrices.
 rad=torch.sqrt((M.conj()*M).real.sum(dim=(1,2))/2)
 vm=(torch.as_tensor(V).mH@M).diagonal(dim1=-2,dim2=-1).sum(dim=-1).real
 wp=2-P.diagonal(dim1=-2,dim2=-1).sum(dim=-1).real
 classical=kap*(2*rad-vm).sum()
 if treephase:return wp,classical,torch.zeros(()),torch.zeros(())
 t=kap*u;x=t*rad
 f=lambda q: torch.log(2*torch.special.i1e(q)/q)
 centered=(2/u)*(f(x)-f(torch.as_tensor(t))).sum()
 haar=-(2/u)*logj(a).sum()
 return wp,classical,centered,haar

def action(a,V,u=5.,kap=.8,treephase=False):
 w,k,c,hj=pieces(a,V,u,kap,treephase);return w.sum()+k+c+hj

def value_grad(a,V,u=5.,kap=.8,treephase=False):
 z=torch.tensor(np.asarray(a).reshape(nf,3),requires_grad=True)
 f=action(z,V,u,kap,treephase);g=torch.autograd.grad(f,z)[0]
 return float(f.detach()),g.detach().numpy().ravel()

# An independent Haar quadrature of the real single-link tilt.
quad={}
for t in [.7,4.,20.]:
 vals=[]
 for nn in [96,192]:
  q,w=roots_legendre(nn);theta=math.pi*(q+1)/2
  weight=w*np.sin(theta)**2*np.exp(t*(np.cos(theta)-1))
  c=float(np.sum(weight*np.cos(theta))/np.sum(weight));z=float(np.sum(weight))
  vals.append((c,z))
 expected=float(ive(2,t)/ive(1,t));quad[t]=vals[-1][0]
 ck(f'Haar radial integral at t={t}',abs(vals[0][0]-vals[1][0])<2e-9 and abs(vals[1][0]-expected)<2e-9,c=vals[-1][0],bessel=expected,refinement=abs(vals[0][0]-vals[1][0]))
# General N exponential-Jacobian coefficient through all root differences.
for N in [2,3,4,7]:
 eigen=rng.normal(size=N);eigen-=eigen.mean();eigen/=np.linalg.norm(eigen)
 vals=[]
 for eps in [1e-3,5e-4]:
  ds=np.array([eps*(eigen[i]-eigen[j])/2 for i in range(N) for j in range(i+1,N)])
  lj=2*np.log(np.sinc(ds/math.pi)).sum();vals.append(float(lj/eps**2))
 ck(f'general SU({N}) Haar Casimir coefficient',max(abs(v+N/12) for v in vals)<2e-5,quotients=vals,expected=-N/12)

# Transported product derivatives independent of torch's matrix differentiation.
def tangent_data(V,ix,sg):
 U=base(V);nword,nstep=ix.shape
 pref=np.repeat(I[None],nword,axis=0);coeff=np.zeros((nword,nstep,3,3));Bm=np.zeros((nword,nstep,3,2,2),complex)
 for k in range(nstep):
  F=U[ix[:,k]];back=sg[:,k]<0;F=np.where(back[:,None,None],F.conj().transpose(0,2,1),F)
  G=np.where(back[:,None,None],pref@F,pref)
  transformed=np.einsum('wib,abc,wcj->waij',G,basis,G.conj().transpose(0,2,1))
  transformed*=sg[:,k,None,None,None]
  Bm[:,k]=transformed
  coeff[:,k]=np.einsum('aij,wbji->wab',-basis,transformed).real
  pref=pref@F
 return pref,coeff,Bm

def linear_map(ix,coeff):
 nword,nstep=ix.shape;out=np.zeros((nword,3,nf,3))
 for k in range(nstep):
  ff=freeindex[ix[:,k]];valid=ff>=0;ww=np.nonzero(valid)[0]
  for outa in range(3):
   for ina in range(3):np.add.at(out,(ww,np.full(len(ww),outa),ff[valid],np.full(len(ww),ina)),coeff[valid,k,outa,ina])
 return out.reshape(3*nword,dim)
V=np.array([su2([.9,0,0]),su2([0,.6,0]),su2([0,0,.4]),su2([.2,.3,.4])])
P0,wcoef,wBm=tangent_data(V,wix,wsg);T0,pcoef,pBm=tangent_data(V,pix,psg)
Dmap=linear_map(wix,wcoef);Theta=linear_map(pix,pcoef);Q=Theta.reshape(4,nper,3,dim).mean(axis=1).reshape(12,dim)
B=Theta.T@Theta/nper-Q.T@Q;H=Dmap.T@Dmap+.8*Q.T@Q
E=np.zeros((dim,dim));gmanual=np.zeros(dim)
for p in range(len(plaq)):
 R=P0[p]-I
 for i in range(4):
  fi=freeindex[wix[p,i]]
  if fi<0:continue
  A=wBm[p,i]
  gmanual[3*fi:3*fi+3]+=-np.einsum('aij,ji->a',A,P0[p]).real
  for j in range(i,4):
   fj=freeindex[wix[p,j]]
   if fj<0:continue
   Cb=wBm[p,j]
   block=-np.einsum('aij,bjk,ki->ab',A,Cb,R).real
   if i==j:block=(block+block.T)/2
   E[3*fi:3*fi+3,3*fj:3*fj+3]+=block
   if i!=j:E[3*fj:3*fj+3,3*fi:3*fi+3]+=block.T
blocks=E.reshape(nf,3,nf,3).transpose(0,2,1,3)
row=float(np.linalg.norm(blocks,ord=2,axis=(2,3)).sum(axis=1).max())
delta=max(float(np.linalg.norm(V[mu]@V[nu]@V[mu].conj().T@V[nu].conj().T-I,2)) for mu,nu in it.combinations(range(4),2))
ck('Wilson curvature error block row and column bound',row<=24*delta+2e-11 and np.max(abs(E-E.T))<2e-11,row=row,bound=24*delta,symmetry=float(np.max(abs(E-E.T))))
ck('full retained-mode principal tree precision positive in diagnostic sector',eigvalsh(H,subset_by_index=[0,0])[0]>0,minimum=float(eigvalsh(H,subset_by_index=[0,0])[0]),dimensions=dim)
# At least one direction lies in the kernel of Q but not in contour spread.
v=rng.normal(size=dim);v-=Q.T@np.linalg.solve(Q@Q.T,Q@v);v/=np.linalg.norm(v)
ck('zero-Q direction with nonzero contour spread retained',np.linalg.norm(Q@v)<2e-11 and v@B@v>1e-3,Q_norm=float(np.linalg.norm(Q@v)),spread=float(v@B@v))
mutsp=[];muthaar=[];mutnorm=[];mutE=[];mutscale=[]
for u in [3.,11.]:
 t=.8*u;c=float(ive(2,t)/ive(1,t));K=H+E+.8*(1-c)*B+4/(6*u)*np.eye(dim)
 z=torch.zeros((nf,3),requires_grad=True);f=action(z,V,u);g=torch.autograd.grad(f,z,create_graph=True)[0]
 gn=g.detach().numpy().ravel()
 ck(f'actual complete coordinate gradient at u={u}',np.max(abs(gn-gmanual))<2e-11 and np.linalg.norm(gn.reshape(nf,3),axis=1).max()<=6*math.sqrt(2)*delta+2e-11,max_error=float(np.max(abs(gn-gmanual))))
 for j,d in enumerate([v,rng.normal(size=dim),np.eye(dim)[12]]):
  d=d/np.linalg.norm(d);dt=torch.as_tensor(d.reshape(nf,3))
  hd=torch.autograd.grad((g*dt).sum(),z,retain_graph=True)[0]
  actual=float((hd*dt).sum().detach());expect=float(d@K@d)
  fd=[]
  fzero=float(f.detach())
  for step in [2e-4,1e-4]:
   with torch.no_grad():
    pp=float(action(step*dt,V,u));mm=float(action(-step*dt,V,u))
   fd.append((pp+mm-2*fzero)/step**2)
  ck(f'finite-u Hessian identity u={u} direction={j}',abs(actual-expect)<2e-9 and max(abs(x-expect) for x in fd)<2e-5,autodiff=actual,transported=expect,differences=fd)
  mutsp.append(abs(actual-float(d@(H+E+4/(6*u)*np.eye(dim))@d)))
  muthaar.append(abs(actual-float(d@(K-4/(6*u)*np.eye(dim))@d)))
  mutnorm.append(abs(actual-float(d@(H+E+.8*B+4/(6*u)*np.eye(dim))@d)))
  mutE.append(abs(actual-float(d@(K-E)@d)))
  mutscale.append(abs(actual-(2/u)*expect))
 # A local full-colour block determinant, separately checked for positivity.
 small=K[np.ix_([0,1,2,21,22,23],[0,1,2,21,22,23])]
 eigen=np.linalg.eigvalsh(small);chol=np.linalg.cholesky(small)
 ld=float(np.log(eigen).sum());lc=float(2*np.log(chol.diagonal()).sum())
 ck(f'colour-coupled Gaussian determinant u={u}',eigen.min()>0 and abs(ld-lc)<2e-11,logdet=ld,cholesky=lc)
 neg(f'colour determinant mistakenly cubed u={u}',abs(-.5*ld-(-1.5*ld))>1e-3,log_amplitude_error=abs(ld))
neg('finite-u contour spread omitted',max(mutsp)>2e-5,max_error=max(mutsp))
neg('Haar contribution omitted',max(muthaar)>2e-5,max_error=max(muthaar))
neg('single normalizer omitted',max(mutnorm)>2e-5,max_error=max(mutnorm))
neg('Wilson curvature error omitted',max(mutE)>2e-5,max_error=max(mutE))
neg('N over u conversion omitted in canonical Hessian',max(mutscale)>2e-5,max_error=max(mutscale))
# Explicit wrong parallel transport in a noncommuting background.
wrong=linear_map(pix,np.array([[np.eye(3)*s for s in row] for row in psg]))
neg('path adjoint transports discarded',np.linalg.norm(Theta-wrong)>1e-2,difference=float(np.linalg.norm(Theta-wrong)))
# Keep large matrices out of subsequent autograd solves.
del Theta,pBm,wBm,B,E,H,Dmap,K

Vsmall=np.array([su2([.7,0,0]),su2([.04,.02,0]),su2([.03,0,.02]),su2([.05,.01,-.015])])
dsmall=max(float(np.linalg.norm(Vsmall[mu]@Vsmall[nu]@Vsmall[mu].conj().T@Vsmall[nu].conj().T-I,2)) for mu,nu in it.combinations(range(4),2))
start=np.zeros(dim)
solutions={}
for label,u,treephase in [('tree',8.,True),('u8',8.,False),('u32',32.,False),('u128',128.,False)]:
 began=time.monotonic();ev=[0]
 def fg(a):ev[0]+=1;return value_grad(a,Vsmall,u,treephase=treephase)
 opt=minimize(fg,start,jac=True,method='L-BFGS-B',options={'gtol':2e-11,'ftol':1e-16,'maxiter':500,'maxls':40,'maxcor':25})
 val,grad=fg(opt.x);res=float(np.linalg.norm(grad.reshape(nf,3),axis=1).max())
 solutions[label]=opt.x.copy();start=opt.x.copy()
 record=dict(label=label,u=u,tree=treephase,iterations=int(opt.nit),evaluations=ev[0],residual=res,max_displacement=float(np.linalg.norm(opt.x.reshape(nf,3),axis=1).max()),objective=val,seconds=time.monotonic()-began,message=str(opt.message))
 runs.append(record);ck(f'actual full-periodic-sector critical residual {label}',res<2e-7,**record)
 # Preserve progress for a long bounded run, separately from final JSON.
 print(json.dumps({'progress':record},allow_nan=False),flush=True)
diffs={str(u):float(np.linalg.norm((solutions[f'u{u}']-solutions['tree']).reshape(nf,3),axis=1).max()) for u in [8,32,128]}
ck('finite-u point distinct from tree point',diffs['8']>1e-7,differences=diffs)
ck('finite-u point approaches tree point in diagnostic sequence',diffs['128']<diffs['32']<diffs['8'],differences=diffs,u_times_difference={k:float(k)*v for k,v in diffs.items()},coarse_curvature=dsmall)
neg('unshifted lift declared stationary',np.linalg.norm(value_grad(np.zeros(dim),Vsmall,8.)[1])>1e-4,gradient_norm=float(np.linalg.norm(value_grad(np.zeros(dim),Vsmall,8.)[1])))
# Sources remain at the zero-source critical point. Select an actual plaquette.
a=torch.tensor(solutions['u32'].reshape(nf,3),requires_grad=True)
wp,_,_,_=pieces(a,Vsmall,32.);p=int(torch.argmax(wp).detach())
s=wp[p]/2;sg=torch.autograd.grad(s,a,retain_graph=True)[0];sgn=float(torch.linalg.norm(sg).detach());sv=float(s.detach())
ck('individual Wilson source is not stationary at total-density critical point',sv>1e-8 and sgn>1e-4,plaquette=p,Wilson_s=sv,source_gradient_norm=sgn,total_residual=runs[2]['residual'])
d=sg/torch.linalg.norm(sg);rho=.05;vac=[];linear=[];quadratic=[]
for u in [8.,32.]:
 sigma=math.sqrt(2/u);eps=1e-4
 with torch.no_grad():
  def source(z):return float(rho*u*pieces(a+sigma*z*d,Vsmall,u)[0][p]/2)
  v0=source(0.);vp=source(eps);vm=source(-eps)
 vac.append(v0);linear.append((vp-vm)/(2*eps));quadratic.append((vp+vm-2*v0)/eps**2)
ck('source vacuum linear and quadratic canonical units',abs(vac[1]/vac[0]-4)<2e-9 and abs(linear[1]/linear[0]-2)<2e-5 and abs(quadratic[1]-quadratic[0])<2e-5,vacuum=vac,linear=linear,quadratic=quadratic)
neg('source vacuum cost discarded',min(vac)>1e-6,minimum=min(vac))
neg('source linear term discarded by total stationarity',min(abs(v) for v in linear)>1e-4,minimum=min(abs(v) for v in linear))
# Direct source budget on real canonical fluctuation vectors.
with torch.no_grad():
 Ustar=links(a,Vsmall);Pstar=products(Ustar,wix,wsg).numpy();delta_bg=max(float(np.linalg.norm(x-I,2)) for x in Pstar)
 z=rng.normal(size=(nf,3));z*=.08/np.linalg.norm(z,axis=1).max();pbound=.08
 value=pieces(a+math.sqrt(2/32)*torch.tensor(z),Vsmall,32.)[0].numpy()/2
 actual=float(np.max(abs(32*rho*value)));bound=16*rho*(32*delta_bg**2+math.sqrt(32)*delta_bg*pbound+pbound**2)
 ck('explicit per-plaquette original-source budget',actual<=bound+2e-11,actual=actual,bound=bound,delta_bg=delta_bg)
# Analytical Gaussian normalization sensitivity with all colour modes.
small=np.array([[2.,.2,.1],[.2,1.4,-.15],[.1,-.15,1.7]])
eig=np.linalg.eigvalsh(small);sigma=math.sqrt(2/7);hhaar=1/(4*math.sqrt(2)*math.pi**2);j0=float(np.exp(logj(torch.tensor([[.2,.1,-.05]])).item()));vacuum=.73
amp=vacuum*hhaar*j0*(2*math.pi*sigma*sigma)**1.5/np.sqrt(eig.prod())
for name,ratio in [('probability Haar density',1/hhaar),('translated Haar j(a*)',1/j0),('vacuum',1/vacuum),('scale Jacobian',sigma**-3),('determinant',math.sqrt(eig.prod()))]:
 neg('normalization omission: '+name,abs(amp*ratio-amp)>1e-8,amplitude_error=float(abs(amp*ratio-amp)))
result={'checks':checks,'controls':controls,'critical_runs':runs,'passed':sum(x['passed'] for x in checks),'total':len(checks),'controls_rejected':sum(x['rejected'] for x in controls),'controls_total':len(controls),'limits':'L=3 SU(2) period-one sector of T>=2; floating checks are not interval proofs, all-volume proof or certification of tiny delta_star. Quadrature N2; general-N Haar coefficient only. Gaussian omission controls are algebraic sensitivity, not complete hard-cut quadrature.'}
print('FINAL_JSON')
print(json.dumps(result,indent=2,allow_nan=False))
assert result['passed']==result['total'] and result['controls_rejected']==result['controls_total']
