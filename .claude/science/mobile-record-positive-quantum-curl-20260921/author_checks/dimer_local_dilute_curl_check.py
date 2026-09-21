#!/usr/bin/env python3
"""Independent occupation, physical-cell and dilute-dynamics author controls."""
from pathlib import Path
from itertools import product,combinations
import hashlib,json,math,time
import numpy as np
from scipy import sparse as sp
from scipy.sparse.linalg import expm_multiply
from scipy.linalg import expm

ROOT=Path(__file__).resolve().parent

def accurate_norm(z):
 # The host BLAS norm lost 2.5e-13 on a 208980-entry almost-flat vector.
 # Compensated scalar accumulation keeps the original assertion tolerances.
 return math.sqrt(math.fsum(float(a) for a in np.abs(z).reshape(-1)**2))

def eps(i,j,k):
 if len({i,j,k})<3:return 0
 return 1 if (i,j,k) in [(0,1,2),(1,2,0),(2,0,1)] else -1

def curl(N):
 xyz=list(product(range(N),repeat=3));ix={x:i for i,x in enumerate(xyz)}
 rr=[];cc=[];vv=[]
 for x in xyz:
  for i,j,k in product(range(3),repeat=3):
   z=eps(i,j,k)
   if not z:continue
   for sign in [-1,1]:
    y=list(x);y[j]=(y[j]+sign)%N
    rr.append(3*ix[x]+i);cc.append(3*ix[tuple(y)]+k);vv.append(sign*z/2)
 C=sp.csr_matrix((vv,(rr,cc)),shape=(3*N**3,3*N**3))
 assert (C-C.T).nnz==0
 return np.array(xyz),C

def local_physical_controls():
 # Three actual four-dimensional pair cells; direct tensor operators.
 V=3;configs=list(product(range(4),repeat=V));ci={x:i for i,x in enumerate(configs)}
 count=np.array([sum(a!=0 for a in x) for x in configs]);ts=[]
 for x in range(V):
  for i in range(3):
   t=np.zeros((4**V,4**V),complex)
   for col,conf in enumerate(configs):
    if conf[x]==i+1:
     dest=list(conf);dest[x]=0;t[ci[tuple(dest)],col]=1
   ts.append(t)
 D=np.array([[0,.5,-.5],[-.5,0,.5],[.5,-.5,0]])
 h=np.zeros((3*V,3*V))
 for x,y,i,j in product(range(V),range(V),range(3),range(3)):
  h[3*x+i,3*y+j]=eps(i,0,j)*D[x,y]
 assert np.array_equal(h,h.T)
 H=sum((h[a,b]*ts[a].conj().T@ts[b] for a,b in product(range(3*V),repeat=2) if h[a,b]),np.zeros((4**V,4**V),complex))
 Hlab=H+2*np.diag(count)
 assert np.max(np.abs(H@np.diag(count)-np.diag(count)@H))==0
 vals=np.linalg.eigvalsh(Hlab);assert abs(vals[0])<1e-13 and vals[1]>2-math.sqrt(3)
 rows=[]
 for n in range(4):
  sel=np.where(count==n)[0];matrix=np.zeros((len(sel),len(sel)))
  byconf={configs[a]:i for i,a in enumerate(sel)}
  for col,a in enumerate(sel):
   conf=configs[a]
   for y in range(V):
    if not conf[y]:continue
    b=3*y+conf[y]-1
    for a1 in range(3*V):
     x,i=divmod(a1,3)
     if conf[x] or not h[a1,b]:continue
     dest=list(conf);dest[y]=0;dest[x]=i+1
     matrix[byconf[tuple(dest)],col]+=h[a1,b]
  err=float(np.max(np.abs(H[np.ix_(sel,sel)]-matrix))) if len(sel) else 0
  assert err==0
  rows.append(dict(n=n,physical_sector_dimension=len(sel),occupation_compression_error=err))
 cr=[]
 for m in [0,1,2]:
  sel=np.where(count<=m)[0];maxerr=0.
  bs=[sum((np.exp(-2j*np.pi*q*x/V)*ts[3*x+i] for x in range(V)),np.zeros((4**V,4**V),complex))/math.sqrt(V) for q in range(V) for i in range(3)]
  for a,b in product(range(3*V),repeat=2):
   z=bs[a]@bs[b].conj().T-bs[b].conj().T@bs[a]-(np.eye(4**V) if a==b else 0)
   maxerr=max(maxerr,float(np.linalg.norm(z[np.ix_(sel,sel)],2)))
  assert maxerr<=2*m/V+2e-14
  cr.append(dict(max_excitation=m,max_restricted_CCR_error=maxerr,bound=2*m/V))
 return dict(cell_count=V,physical_dimension=4**V,lab_gap=float(vals[1]),sector_rows=rows,CCR_rows=cr)

def physical_two_particle(C):
 M=C.shape[0];pairs=np.array([(a,b) for a,b in combinations(range(M),2) if a//3!=b//3],dtype=np.int32)
 lookup={int(a)*M+int(b):i for i,(a,b) in enumerate(pairs)}
 neighbors=[list(zip(C[:,b].tocoo().row,C[:,b].tocoo().data)) for b in range(M)]
 rr=[];cc=[];vv=[]
 for col,(a,b) in enumerate(pairs):
  for old,other in [(a,b),(b,a)]:
   for dest,value in neighbors[old]:
    if dest//3==other//3:continue
    lo,hi=sorted((int(dest),int(other)));rr.append(lookup[lo*M+hi]);cc.append(col);vv.append(value)
 H=sp.csr_matrix((vv,(rr,cc)),shape=(len(pairs),len(pairs)))
 assert (H-H.T).nnz==0
 return pairs,H

def plane(xyz,N,q,u):
 return (np.exp(2j*np.pi*(xyz@np.array(q))/N)[:,None]*np.asarray(u)[None,:]/math.sqrt(N**3)).reshape(-1)

def polarization(N,q,u,t):
 s=np.sin(2*np.pi*np.array(q)/N);h=1j*np.array([[0,-s[2],s[1]],[s[2],0,-s[0]],[-s[1],s[0],0]])
 return expm(-1j*t*h)@u

def two_particle_controls():
 rows=[];q1=(1,0,0);q2=(0,1,0);u=np.array([1,1j,0])/math.sqrt(2);v=np.array([0,1,1j])/math.sqrt(2)
 for N in [3,4,6]:
  start=time.monotonic();xyz,C=curl(N);pairs,H=physical_two_particle(C);a,b=pairs.T
  f=plane(xyz,N,q1,u);g=plane(xyz,N,q2,v);assert abs(np.vdot(f,g))<1e-13
  initial=f[a]*g[b]+g[a]*f[b];alpha=accurate_norm(initial);phi=initial/alpha
  exact_collision=(1+abs(np.vdot(u,v))**2)/N**3
  assert abs(1-alpha**2-exact_collision)<2e-13
  epsilon=2/math.sqrt(N**3)
  for tau in [.125,.375,.75]:
   t=N*tau;actual=expm_multiply(-1j*t*H,phi,traceA=0.)
   ut=polarization(N,q1,u,t);vt=polarization(N,q2,v,t)
   ft=plane(xyz,N,q1,ut);gt=plane(xyz,N,q2,vt);projected=ft[a]*gt[b]+gt[a]*ft[b]
   collision=(1+abs(np.vdot(ut,vt))**2)/N**3
   assert abs(accurate_norm(projected)**2+collision-1)<3e-13
   # Orthogonal missing collision sector contributes exactly its norm squared.
   strong_error=math.sqrt(accurate_norm(actual-projected)**2+collision)
   bound=epsilon*(1+2*math.sqrt(3)*abs(t))+epsilon**2
   assert strong_error<=bound+1e-12
   assert abs(accurate_norm(actual)-1)<3e-12
   cont_u=expm(-1j*tau*2*np.pi*1j*np.array([[0,0,0],[0,0,-1],[0,1,0]]))@u
   cont_v=expm(-1j*tau*2*np.pi*1j*np.array([[0,0,1],[0,0,0],[-1,0,0]]))@v
   fc=plane(xyz,N,q1,cont_u);gc=plane(xyz,N,q2,cont_v);pc=fc[a]*gc[b]+gc[a]*fc[b]
   cont_collision=(1+abs(np.vdot(cont_u,cont_v))**2)/N**3
   cont_error=math.sqrt(accurate_norm(actual-pc)**2+cont_collision)
   cont_bound=bound+2*tau*(2*np.pi)**3/(6*N*N)
   assert cont_error<=cont_bound+1e-12
   rows.append(dict(N=N,V=N**3,physical_two_particle_dimension=len(pairs),tau=tau,initial_collision=exact_collision,free_collision_at_time=collision,free_comparison_error=strong_error,proof_bound=bound,continuum_comparison_error=cont_error,combined_proof_bound=cont_bound,unitary_norm_error=abs(accurate_norm(actual)-1)))
  print('two_particle_N_complete',N,'seconds',round(time.monotonic()-start,3),flush=True)
 return rows

def one_particle_symbol_controls():
 rows=[]
 for N in [3,4,6,8,16,32,64,128,256]:
  maxs=max(abs(math.sin(2*math.pi*j/N)) for j in range(N));norm=math.sqrt(3)*maxs
  q=np.array([1,2,-1]);s=np.sin(2*np.pi*q/N)
  err=float(np.linalg.norm(N*s-2*np.pi*q));bound=float(np.linalg.norm(2*np.pi*q)**3/(6*N*N))
  assert err<=bound+1e-13
  zeros=(2 if N%2==0 else 1)**3
  rows.append(dict(N=N,one_particle_curl_norm=norm,mu2_gap_lower_bound=2-norm,sine_zero_momenta=zeros,low_mode_symbol_error=err,sine_remainder_bound=bound))
 # Direct real-space Fourier comparison on a genuinely three-dimensional grid.
 xyz,C=curl(4);maxerr=0.
 for q in [(0,0,0),(1,0,0),(1,1,1),(2,0,0)]:
  s=np.sin(2*np.pi*np.array(q)/4);hk=1j*np.array([[0,-s[2],s[1]],[s[2],0,-s[0]],[-s[1],s[0],0]])
  for i in range(3):
   u=np.eye(3)[i];maxerr=max(maxerr,float(np.linalg.norm(C@plane(xyz,4,q,u)-plane(xyz,4,q,hk@u))))
 assert maxerr<1e-13
 return dict(rows=rows,real_space_Fourier_max_error=maxerr)

def main():
 result={'status':'completed author corroboration; proof scope remains conditional','sources':[]}
 for name in ['DIMER_LOCAL_DILUTE_QUANTUM_CURL_LIMIT.md',Path(__file__).name]:
  p=ROOT/name;result['sources'].append(dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
 result['physical_cells']=local_physical_controls();print('physical_cells_complete',flush=True)
 result['one_particle_symbols']=one_particle_symbol_controls();print('one_particle_symbols_complete',flush=True)
 result['two_particle_dynamics']=two_particle_controls()
 result['scope']='Direct three-cell tensor algebra; exact one-particle symbols; sparse uncut two-particle dynamics for N=3,4,6. These controls do not numerically prove the asymptotic rate or establish finite-density dynamics, record permanence, or a gapless positive vacuum.'
 out=ROOT/'dimer_local_dilute_curl_checks';out.mkdir(exist_ok=True);(out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
 print('all_three_control_groups_complete',flush=True)

if __name__=='__main__':main()
