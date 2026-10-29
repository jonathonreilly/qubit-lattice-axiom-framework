#!/usr/bin/env python3
"""Independent matrix SU(2) lift, lifted-brick and strong-good chart checks."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=[]
import itertools,json,math,time,sys,argparse
import numpy as np
from scipy.linalg import expm,logm
start=time.monotonic();L=3;h=1;parser=argparse.ArgumentParser();parser.add_argument('--torus-side',type=int,choices=[2,3],default=2);T=parser.parse_args().torus_side;n=L*T
local=list(itertools.product(range(-h,h+1),repeat=4));blocks=list(itertools.product(range(T),repeat=4));sites=list(itertools.product(range(n),repeat=4))
sid={x:i for i,x in enumerate(sites)};bid={x:i for i,x in enumerate(blocks)};orders=list(itertools.permutations(range(4)))
pauli=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex);I=np.eye(2);rng=np.random.default_rng(8711)
def group(a):return expm(1j*np.einsum('a,aij->ij',a,pauli))
def shift(x,mu,a=1,mod=n):return tuple((x[i]+a*(i==mu))%mod for i in range(4))
def locate(x):
 x=tuple(v%n for v in x);r=tuple((v+h)%L-h for v in x);b=tuple(((x[i]-r[i])//L)%T for i in range(4));return b,r
def lift(V):
 U=np.empty((len(sites),4,2,2),complex)
 for j,x in enumerate(sites):
  b,r=locate(x)
  for mu in range(4):U[j,mu]=V[bid[b],mu] if r[mu]==h else I
 return U
def word(x,y,order):
 out=[];p=x
 for mu in order:
  while p[mu]!=y[mu]:
   s=1 if y[mu]>p[mu] else -1;base=p if s==1 else tuple(p[i]-(i==mu) for i in range(4));out.append((base,mu,s));p=tuple(p[i]+s*(i==mu) for i in range(4))
 return out
def invword(w):return [(x,mu,-s) for x,mu,s in w[::-1]]
def hol(U,w):
 a=I.copy()
 for x,mu,s in w:
  b=U[sid[tuple(v%n for v in x)],mu];a=a@(b if s==1 else b.conj().T)
 return a
def plaq(U,x,mu,nu):return U[sid[x],mu]@U[sid[shift(x,mu)],nu]@U[sid[shift(x,nu)],mu].conj().T@U[sid[x],nu].conj().T
def cp(V,b,mu,nu):return V[bid[b],mu]@V[bid[shift(b,mu,mod=T)],nu]@V[bid[shift(b,nu,mod=T)],mu].conj().T@V[bid[b],nu].conj().T
def op(A):return float(np.linalg.norm(A,2))
checks=[];details={}
def gate(name,p,d=None):checks.append({'name':name,'pass':bool(p),'detail':d})
V=np.array([[group(rng.normal(size=3)) for mu in range(4)] for b in blocks]);U=lift(V)
err=0.;multip={};wrongorder=0.
for x in sites:
 b,r=locate(x)
 for mu,nu in itertools.combinations(range(4),2):
  P=plaq(U,x,mu,nu)
  if r[mu]==h and r[nu]==h:
   target=cp(V,b,mu,nu);key=(b,mu,nu);multip[key]=multip.get(key,0)+1
   wrongorder=max(wrongorder,op(P-target.conj().T))
  else:target=I
  err=max(err,op(P-target))
gate('all_fine_plaquettes_exact_lift_classification',err<2e-14,err)
gate('double_face_multiplicity_L_squared',len(multip)==6*T**4 and set(multip.values())=={L**2})
gate('wrong_coarse_orientation_control',wrongorder>.2,wrongorder)
selected=[((0,0,0,0),mu) for mu in range(4)]+[((T-1,)*4,mu) for mu in range(4)]
maxpath=0.;pathcount=0;maxbrick=0.;farerror=0.;maxlength=0;maxnormcount=0
for b,mu in selected:
 root=tuple(L*v for v in b);root2=tuple(root[i]+L*(i==mu) for i in range(4));vc=V[bid[b],mu]
 for r in local:
  y=tuple(root[i]+r[i] for i in range(4));y2=tuple(y[i]+L*(i==mu) for i in range(4))
  for order in orders:
   w=word(root,y,order)+word(y,y2,(mu,))+invword(word(root2,y2,order));maxlength=max(maxlength,len(w));pathcount+=1;maxpath=max(maxpath,op(hol(U,w)-vc))
   # Adjacent-step combing area bound, without an abelian chain shortcut.
   low=tuple(root[i]-h for i in range(4));width=tuple((2*L-1) if i==mu else L-1 for i in range(4))
   maxnormcount=max(maxnormcount,sum(width)*(len(w)+L))
 low=tuple(root[i]-h for i in range(4));high=tuple(root[i]+h+L*(i==mu) for i in range(4))
 vertices=list(itertools.product(*(range(low[i],high[i]+1) for i in range(4))))
 def g(x):return vc if x[mu]>root[mu]+h else I
 for x in vertices:
  for nu in range(4):
   if x[nu]>=high[nu]:continue
   y=tuple(x[i]+(i==nu) for i in range(4));a=U[sid[tuple(v%n for v in x)],nu]
   maxbrick=max(maxbrick,op(g(x)@a@g(y).conj().T-I))
 # The far seam in the torus-induced vertex graph is not a lifted brick edge.
 x=tuple(high[i] if i==mu else root[i] for i in range(4));y=tuple(low[i] if i==mu else root[i] for i in range(4));a=U[sid[tuple(v%n for v in x)],mu]
 farerror=max(farerror,op(g(x)@a@g(y).conj().T-I))
gate('all_selected_actual_contours_equal_coarse_V',maxpath<4e-14,{'words':pathcount,'error':maxpath,'max_length':maxlength})
gate('actual_lifted_two_block_gauge_is_exactly_flat',maxbrick<2e-14,maxbrick)
if T==2:gate('T2_induced_graph_far_seam_control',farerror>.2,farerror)
else:gate('T3_lifted_far_faces_not_periodic_neighbors',((high[mu]+1)%n)!=(low[mu]%n))
gate('nonabelian_combing_area_budget',maxnormcount<=30*L**2,{'max_width_times_loop_length':maxnormcount,'bound':30*L**2})
gate('wrong_crossing_assignment_control',op(V[bid[shift((0,0,0,0),0,mod=T)],0]-V[bid[(0,0,0,0)],0])>.1)
# Flat but large and noncommuting link representatives, via a coarse gauge.
angles=[.51,.37,.29,.19];H=[group(np.array([0,0,t])) for t in angles];gauges=np.array([group(rng.normal(size=3)) for b in blocks])
Vflat=np.array([[gauges[bid[b]]@H[mu]@gauges[bid[shift(b,mu,mod=T)]].conj().T for mu in range(4)] for b in blocks]);Uflat=lift(Vflat)
flaterr=max(op(cp(Vflat,b,mu,nu)-I) for b in blocks for mu,nu in itertools.combinations(range(4),2))
holdef=max(op(np.linalg.matrix_power(H[mu],T)-I) for mu in range(4));comm=op(Vflat[0,0]@Vflat[0,1]-Vflat[0,1]@Vflat[0,0])
gate('large_holonomy_flat_background',flaterr<3e-14 and holdef>.5 and comm>.1,{'curvature':flaterr,'holonomy_defect':holdef,'matrix_commutator':comm})
# Perturb the fine field, then independently reconstruct the pinned tree slice.
Vgood=Vflat.copy();Vgood[0,0]=group(np.array([1e-6,0,0]))@Vgood[0,0];Ug=lift(Vgood);good_coarse_delta=max(op(cp(Vgood,b,mu,nu)-I) for b in blocks for mu,nu in itertools.combinations(range(4),2));Uf=Ug.copy()
for j,x in enumerate(sites):
 for mu in range(4):Uf[j,mu]=group(rng.normal(size=3)*1e-7)@Uf[j,mu]
G=np.empty((len(sites),2,2),complex)
for b in blocks:
 root=tuple(L*v for v in b);G[sid[root]]=I
 for r in sorted((r for r in local if any(r)),key=lambda r:sum(abs(v) for v in r)):
  mu=max(i for i in range(4) if r[i]);s=1 if r[mu]>0 else -1;par=tuple(r[i]-s*(i==mu) for i in range(4));x=tuple((root[i]+par[i])%n for i in range(4));y=tuple((root[i]+r[i])%n for i in range(4));a=Uf[sid[x if s==1 else y],mu];G[sid[y]]=G[sid[x]]@(a if s==1 else a.conj().T)
W=np.empty_like(Uf)
for j,x in enumerate(sites):
 for mu in range(4):W[j,mu]=G[j]@Uf[j,mu]@G[sid[shift(x,mu)]].conj().T
fine_delta=max(op(plaq(Uf,x,mu,nu)-I) for x in sites for mu,nu in itertools.combinations(range(4),2));eta=0.;maxinternal=0.;maxcross=0.;maxlog=0
for b in blocks:
 root=tuple(L*v for v in b)
 for mu in range(4):eta=max(eta,op(hol(Uf,word(root,tuple(root[i]+L*(i==mu) for i in range(4)),(mu,)))-Vgood[bid[b],mu]))
for j,x in enumerate(sites):
 b,r=locate(x)
 for mu in range(4):
  target=Vgood[bid[b],mu] if r[mu]==h else I;rel=W[j,mu]@target.conj().T;dist=op(rel-I);maxlog=max(maxlog,float(np.linalg.norm(logm(rel),'fro')))
  if r[mu]==h:maxcross=max(maxcross,dist)
  else:maxinternal=max(maxinternal,dist)
bound=30*L**2*fine_delta+eta
gate('internal_tree_ribbon_bound',maxinternal<=30*L**2*fine_delta,{'measured':maxinternal,'bound':30*L**2*fine_delta})
gate('crossing_relative_background_ribbon_bound',maxcross<=bound,{'measured':maxcross,'bound':bound})
gate('entire_strong_good_sample_in_relative_chart',maxlog<=2*math.sqrt(2)*bound and 2*math.sqrt(2)*bound<.01,{'max_log_HS':maxlog,'bound':2*math.sqrt(2)*bound})
gate('coarse_curvature_implication',1e-7<good_coarse_delta<=L**2*fine_delta+4*eta,{'coarse':good_coarse_delta,'bound':L**2*fine_delta+4*eta})
# Hypothesis deletion controls.
interiorerr=max(op(plaq(U,x,mu,nu)-I) for x in sites for mu,nu in itertools.combinations(range(4),2) if locate(x)[1][mu]!=h and locate(x)[1][nu]!=h)
gate('interior_only_allows_rough_boundary_control',interiorerr<1e-14 and max(op(cp(V,b,mu,nu)-I) for b in blocks for mu,nu in itertools.combinations(range(4),2))>1)
gate('all_fine_good_without_mismatch_allows_large_relative_links',flaterr<1e-13 and max(op(v-I) for v in Vflat.reshape(-1,2,2))>.5)
Z3=np.exp(2j*math.pi/3)*np.eye(3);P3=logm(Z3)
gate('SU3_principal_log_trace_control',abs(np.trace(P3))>6 and np.linalg.norm(P3,'fro')>math.pi/math.sqrt(3),{'trace_imag':float(np.trace(P3).imag),'HS_norm':float(np.linalg.norm(P3,'fro'))})
out={'scope':'finite independent matrix-group diagnostics; uniform claims rely on written proof','L':L,'T':T,'passed':sum(c['pass'] for c in checks),'total':len(checks),'all_pass':all(c['pass'] for c in checks),'checks':checks,'elapsed_seconds':time.monotonic()-start,'external_scientific_inputs_read':[],'integrity_reads':[]};print(json.dumps(out,indent=2,allow_nan=False));sys.exit(0 if out['all_pass'] else 1)
