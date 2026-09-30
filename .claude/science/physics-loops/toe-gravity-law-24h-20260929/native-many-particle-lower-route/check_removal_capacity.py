"""Actual pair-removal/capacity controls. Own new code; no route helper import.
Literal occupation action reuses the method of my independent N4 word check.
No finite check is represented as an all-N proof.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[name]='1'
import time,resource,signal,json,hashlib,gc
from pathlib import Path
from itertools import product,combinations
from collections import defaultdict
from fractions import Fraction as F
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
def guard():
 assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
 assert not (runtime/'STOP_REQUESTED.json').exists()
guard();resource.setrlimit(resource.RLIMIT_CPU,(30,35));signal.alarm(180)
started=time.monotonic();cpu=time.process_time()
import numpy as np
import_seconds=time.monotonic()-started
ROOT=Path(__file__).resolve().parent
unit=((1,0,0),(0,1,0),(0,0,1));zero=(0,0,0)
def add(x,y,L=None):
 v=tuple(a+b for a,b in zip(x,y));return v if L is None else tuple(a%L for a in v)
def mul(x,s):return tuple(s*a for a in x)
G=[mul(e,s) for e in unit for s in (-2,2)]+[add(mul(unit[i],s),mul(unit[j],t)) for i,j in combinations(range(3),2) for s,t in product((-1,1),repeat=2)]
planes=list(combinations(range(3),2))

def channel(x,L=None):
 ax=[frozenset((add(x,e,L),add(x,mul(e,-1),L))) for e in unit]
 pl=[[(frozenset((add(x,mul(unit[i],s),L),add(x,mul(unit[j],t),L))),F(s*t,2)) for s,t in product((-1,1),repeat=2)] for i,j in planes]
 return ax,pl

def action(S,L=None):
 S=frozenset(S);N=len(S);out=defaultdict(lambda:[F(0),F(0)])
 deg=[sum(add(x,d,L) in S for d in G) for x in S]
 out[tuple(sorted(S))][0]=N+sum(m*(m-1)//2 for m in deg)
 centers={add(x,mul(e,s),L) for x in S for e in unit for s in (-1,1)}
 shifts=[zero]+[mul(e,s) for e in unit for s in (-1,1)]
 def put(pair,res,cm,ct):
  if len(pair)!=2 or pair & res:return
  k=tuple(sorted(pair|res));out[k][0]+=cm;out[k][1]+=ct
 for x in centers:
  ax,pl=channel(x,L)
  for j,inside in enumerate(ax):
   if not inside<=S:continue
   res=S-inside
   for shift in shifts:
    dst,_=channel(add(x,shift,L),L)
    for i,pair in enumerate(dst):
     c=F(int(i==j))-F(1,3)
     put(pair,res,-2*c if shift==zero else 0,(6 if shift==zero else -1)*c)
  for p,pairs in enumerate(pl):
   for inside,ci in pairs:
    if not inside<=S:continue
    res=S-inside
    for shift in shifts:
     _,dst=channel(add(x,shift,L),L)
     for pair,co in dst[p]:
      c=ci*co;put(pair,res,-c if shift==zero else 0,(6 if shift==zero else -1)*c)
 return {k:tuple(v) for k,v in out.items() if any(v)}

def diagonal(S,L=None):
 S=set(S);ds=[sum(add(x,d,L) in S for d in G) for x in S]
 return {'N':len(S),'edges':sum(ds)//2,'D':sum((d-1)*(d-2)//2 for d in ds),'V3_over_mu':sum(d*(d-1)//2 for d in ds)}

def bond_data(L):
 rows=[];lookup={}
 for c in product(range(L),repeat=3):
  edges=[frozenset((add(c,e,L),add(c,mul(e,-1),L))) for e in unit]
  edges += [frozenset((c,add(c,add(unit[i],mul(unit[j],s)),L))) for i,j in planes for s in (1,-1)]
  for a,e in enumerate(edges):
   assert e not in lookup
   lookup[e]=len(rows);rows.append((c,a,e))
 assert len(rows)==9*L**3
 return rows,lookup

Z=np.zeros((9,5),complex)
Z[:3,0]=np.array([1,-1,0])/np.sqrt(2);Z[:3,1]=np.array([1,1,-2])/np.sqrt(6)
for p in range(3):Z[3+2*p:5+2*p,2+p]=np.array([-1,1])/np.sqrt(2)
assert np.max(abs(Z.conj().T@Z-np.eye(5)))<1e-14

def kernels(L,mu=1.,tau=1.,need_K=False):
 guard();shape=(L,L,L,9,9);Gk=np.empty(shape,complex);Kk=np.empty(shape,complex) if need_K else None
 bands_error=0.;zero_count=0
 for ns in product(range(L),repeat=3):
  k=2*np.pi*np.array(ns)/L;ell=4*np.sum(np.sin(k/2)**2)
  q=np.zeros((5,9),complex);q[:2,:3]=Z[:3,:2].T
  for p,(i,j) in enumerate(planes):
   for rr,r in enumerate((1,-1)):q[2+p,3+2*p+rr]=-r*(np.exp(-1j*r*k[j])+np.exp(-1j*k[i]))/2
  weights=np.array([-2*mu+tau*ell]*2+[-mu+tau*ell]*3)
  K=2*mu*np.eye(9)+q.conj().T@(weights[:,None]*q)
  vals,U=np.linalg.eigh(K);mask=vals>1e-9;zero_count+=9-int(sum(mask))
  expected=sorted([tau*ell]*2+[2*mu]*4+[mu*(1-np.cos(k[i])*np.cos(k[j]))+tau*ell*(1+np.cos(k[i])*np.cos(k[j])) for i,j in planes])
  bands_error=max(bands_error,float(np.max(abs(np.sort(vals)-expected))))
  assert min(vals)>-1e-10
  Gk[ns]=(U[:,mask]/vals[mask])@U[:,mask].conj().T
  if need_K:Kk[ns]=K
 assert zero_count==5 and bands_error<1e-12
 Gker=np.fft.ifftn(Gk,axes=(0,1,2));del Gk
 Kker=np.fft.ifftn(Kk,axes=(0,1,2)) if need_K else None
 del Kk
 return Gker,Kker,bands_error

def matrix_on(rows,indices,kernel,L):
 cs=np.array([rows[i][0] for i in indices]);aa=np.array([rows[i][1] for i in indices]);d=(cs[:,None,:]-cs[None,:,:])%L
 return kernel[d[:,:,0],d[:,:,1],d[:,:,2],aa[:,None],aa[None,:]]

def pin_indices(eta,L,lookup):
 return sorted({lookup[frozenset((x,add(x,d,L)))] for x in eta for d in G})

def components(eta,L):
 todo=set(eta);parts=[]
 while todo:
  comp={todo.pop()};stack=list(comp)
  while stack:
   x=stack.pop()
   for d in G:
    y=add(x,d,L)
    if y in todo:todo.remove(y);comp.add(y);stack.append(y)
  parts.append(comp)
 return parts

def capacity(eta,amp,rows,lookup,Gker,L,lam=1.):
 # amp is the actual physical-edge amplitude for one residual configuration.
 pins=pin_indices(eta,L,lookup);M=matrix_on(rows,pins,Gker,L)
 a=sum((Z[rows[e][1]].conj()*v for e,v in amp.items()),start=np.zeros(5,complex))/np.sqrt(L**3)
 r=np.array([Z[rows[e][1]]@a for e in pins])/np.sqrt(L**3)
 A=M+np.eye(len(pins))/lam
 val=float(np.vdot(r,np.linalg.solve(A,r)).real)
 assert val>=-1e-12 and np.max(abs(M-M.conj().T))<1e-12
 return val

L=7;rows,lookup=bond_data(L);Gker,Kker,banderror=kernels(L,need_K=True)
# Actual literal N2 columns control the symbol and cell phases, not only its eigenvalues.
column_error=0.;literal_columns=0
for idx in [0,1,2,3,4,5,6,7,8,9*57+4]:
 c,a,e=rows[idx];col=action(e,L);literal={lookup[frozenset(S)]:float(v[0]+v[1]) for S,v in col.items()}
 for j,(d,b,_) in enumerate(rows):
  delta=tuple((x-y)%L for x,y in zip(d,c));got=Kker[delta+(b,a)]
  column_error=max(column_error,abs(got-literal.get(j,0)))
 literal_columns+=1
assert column_error<1e-12

controls=[]
base_sets=[[(0,0,0),(2,0,0),(4,0,0)],[(0,0,0),(2,0,0),(4,0,0),(6,0,0)],list(unit)+[mul(e,-1) for e in unit]]
for raw in base_sets:
 S=tuple(sorted(tuple(x%L for x in p) for p in raw));support=[S]+list(action(S,L))[:6]
 support=list(dict.fromkeys(support));psi={U:complex(j+1,(-1)**j) for j,U in enumerate(support)}
 norm=sum(abs(v)**2 for v in psi.values());psi={U:v/np.sqrt(norm) for U,v in psi.items()};N=len(S)
 energy=0j;D=0.;pedges=0.;rem=defaultdict(dict)
 for U,v in psi.items():
  d=diagonal(U,L);D+=abs(v)**2*d['D'];pedges+=abs(v)**2*d['edges']
  assert d['D']==N-2*d['edges']+d['V3_over_mu']
  for W,c in action(U,L).items():energy+=np.conj(psi.get(W,0))*(float(c[0])+float(c[1]))*v
  for pair in combinations(U,2):
   e=frozenset(pair)
   if e in lookup:
    eta=tuple(sorted(set(U)-e));rem[eta][lookup[e]]=v
 qenergy=0.;mass=0.;caps={lam:0. for lam in (0.25,1.,4.)}
 for eta,amp in rem.items():
  inds=list(amp);f=np.array([amp[e] for e in inds]);Ksub=matrix_on(rows,inds,Kker,L)
  qenergy+=float(np.vdot(f,Ksub@f).real);mass+=float(np.vdot(f,f).real)
  for lam in caps:caps[lam]+=capacity(eta,amp,rows,lookup,Gker,L,lam)
 assert abs(energy.imag)<1e-12 and abs(energy.real-D-qenergy)<1e-10
 assert abs(mass-pedges)<1e-12
 assert all(c<=qenergy+1e-10 for c in caps.values())
 assert caps[.25]<=caps[1]+1e-12<=caps[4]+2e-12
 controls.append({'N':N,'support':len(support),'residuals':len(rem),'energy':energy.real,'D':D,'pair_form':qenergy,'pair_mass':mass,'capacity':caps,'identity_error':abs(energy.real-D-qenergy)})

# Exact occupation graph tests of matching normalization and rare-reset motifs.
def matching_count(S):
 S=tuple(sorted(S));adj=[sum(1<<j for j,y in enumerate(S) if tuple(y[k]-x[k] for k in range(3)) in G) for x in S]
 cache={0:1}
 def rec(mask):
  if mask in cache:return cache[mask]
  i=(mask&-mask).bit_length()-1;others=adj[i]&mask;total=0
  while others:
   bit=others&-others;others-=bit;total+=rec(mask^(1<<i)^bit)
  cache[mask]=total;return total
 return rec((1<<len(S))-1)
matchings=[]
for m in (2,4,8,12):
 cyc=[(2*j,0,0) for j in range(m+1)]+[(2*m,2,0),(2*m,4,0)]+[(2*j,4,0) for j in range(m-1,-1,-1)]+[(0,2,0)]
 edge=set(cyc[:2]);cut=m;opened=[p for j,p in enumerate(cyc) if j not in (cut,cut+1)]+[(0,100,0),(2,100,0)]
 assert matching_count(cyc)==2 and matching_count(set(cyc)-edge)==1
 assert matching_count(opened)==1 and matching_count(set(opened)-edge)==1
 matchings.append({'cycle_vertices':len(cyc),'cycle_matchings':2,'cycle_removal_coefficient_squared':'1/2','remote_cut_same_N_matchings':1,'remote_cut_removal_coefficient_squared':'1'})
star=list(unit)+[mul(e,-1) for e in unit]
tri=[zero,(2,0,0),(1,1,0)];two_tri=tri+[add(x,(0,0,4)) for x in tri]
assert matching_count(star)==15 and matching_count(two_tri)==0
assert diagonal(star)['D']==36 and diagonal(two_tri)['D']==0
star_diag=action(star)[tuple(sorted(star))];tri_diag=action(two_tri)[tuple(sorted(two_tri))]
assert star_diag==(F(56),F(48)) and tri_diag==(F(22,3),F(20))

# Finite exact matrix inequality for background component replacement.
# G and all matrix operations are numerical; conclusions rely on the analytic proof.
block_controls=[]
del rows,lookup,Gker,Kker;gc.collect()
for L in (7,11,15,19):
 guard();rows,lookup=bond_data(L);Gker,_,berr=kernels(L)
 shift=L//2;eta={zero,(2,0,0),(0,shift,shift),(2,shift,shift)}
 parts=components(eta,L);assert len(parts)==2 and all(len(c)==2 for c in parts)
 pp=[pin_indices(c,L,lookup) for c in parts];assert set(pp[0]).isdisjoint(pp[1]) and all(len(v)==35 for v in pp)
 pins=pp[0]+pp[1];M=matrix_on(rows,pins,Gker,L);AA=M+np.eye(70)
 Dblk=np.zeros((70,70),complex)
 for j in range(2):Dblk[j*35:(j+1)*35,j*35:(j+1)*35]=AA[j*35:(j+1)*35,j*35:(j+1)*35]
 ev,U=np.linalg.eigh(Dblk);Dinvsqrt=(U/np.sqrt(ev))@U.conj().T
 off=Dinvsqrt@(AA-Dblk)@Dinvsqrt;kappa=float(max(abs(np.linalg.eigvalsh(off))))
 exact=np.linalg.inv(AA);lower=np.linalg.inv(Dblk)/(1+kappa)
 eigmin=float(min(np.linalg.eigvalsh(exact-lower)))
 assert eigmin>-1e-11
 # The tested capacity matrix acts on the physical five-component uniform amplitudes.
 Zp=np.array([Z[rows[e][1]] for e in pins])/np.sqrt(L**3)
 capmat=Zp.conj().T@exact@Zp;lowercap=Zp.conj().T@lower@Zp
 gap=float(min(np.linalg.eigvalsh(capmat-lowercap)));assert gap>-1e-11
 block_controls.append({'L':L,'background_sites':4,'pin_blocks':[35,35],'lambda':1,'kappa':kappa,'full_inverse_lower_min_eigenvalue':eigmin,'capacity_lower_min_eigenvalue':gap,'capacity_eigenvalues_times_volume':list(map(float,np.linalg.eigvalsh(capmat)*L**3))})
 del rows,lookup,Gker;gc.collect()

out={'scope':'Author small controls of exact analytic all-N decomposition/capacity lemmas; not a dilute EOS or phase computation. No external/helper import.',
'parameters':{'mu':1,'tau':1},'literal_symbol_columns':literal_columns,'symbol_column_max_error':float(column_error),'band_max_error':banderror,
'physical_sector_controls':controls,'matching_controls':matchings,'reset_motifs':{'K6':dict(diagonal(star),matchings=15,diagonal_mu_tau=list(map(str,star_diag))),'two_triangles':dict(diagonal(two_tri),matchings=0,diagonal_mu_tau=list(map(str,tri_diag)))},
'background_block_controls':block_controls,'numpy_import_wall_seconds':import_seconds,'wall_seconds':time.monotonic()-started,'cpu_seconds':time.process_time()-cpu,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'capacity_controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
