"""Leading derived XY theory: collective density versus native composite readout.
Periodic effective chain only, not a full native isotropic Hamiltonian test.
Energy units t=J_z^2/(sqrt(2)*J_perp); the composite excludes its lambda^2 prefactor.
"""
from pathlib import Path
import numpy as np,json,itertools,time
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh
from scipy.linalg import eigh_tridiagonal
P=Path(__file__).resolve().parent
rows=[]
for L in [8,12,16,20]:
 start=time.monotonic();states=np.array([sum(1<<i for i in c) for c in itertools.combinations(range(L),L//2)],dtype=np.int64);dim=len(states)
 lookup=np.full(1<<L,-1,dtype=np.int32);lookup[states]=np.arange(dim);ix=np.arange(dim)
 rr=[];cc=[];vv=[]
 for j in range(L):
  k=(j+1)%L;mask=((states>>j)^(states>>k))&1;sel=ix[mask.astype(bool)];rr.extend(lookup[states[sel]^(1<<j)^(1<<k)]);cc.extend(sel);vv.extend([-1.]*len(sel))
 H=coo_matrix((vv,(rr,cc)),shape=(dim,dim)).tocsr();e,u=eigsh(H,k=1,which='SA',tol=1e-12,v0=np.random.default_rng(1818+L).normal(size=dim));g=u[:,0];E=float(e[0]);res=float(np.linalg.norm(H@g-E*g))
 ks=2*np.pi*(np.arange(L)+.5)/L;free=float(sum(np.sort(-2*np.cos(ks))[:L//2]));assert abs(E-free)<1e-9
 complement=lookup[((1<<L)-1)^states];px=float(g@g[complement]);assert abs(abs(px)-1)<1e-9
 for mode in [1,2]:
  weights=np.exp(2j*np.pi*mode*np.arange(L)/L)/np.sqrt(L)
  density=sum(weights[j]*(1-2*((states>>j)&1)) for j in range(L))*g
  source=np.zeros(dim,dtype=complex)
  for j in range(L):
   for a,b in [((j-1)%L,j),(j,(j+1)%L),((j-1)%L,(j+1)%L)]:
    sel=ix[(((states>>a)^(states>>b))&1).astype(bool)];target=lookup[states[sel]^(1<<a)^(1<<b)]
    source[target]+=.75*weights[j]*g[sel]
  sources={"collective_density":density,"native_composite_O2":source}
  cross=complex(np.vdot(density,source));assert abs(cross)<1e-9
  for name,b in sources.items():
   b-=g*np.vdot(g,b);weight=float(np.vdot(b,b).real);assert weight>1e-18
   parity=float(np.vdot(b,b[complement]).real/weight)
   v=b/np.sqrt(weight);prev=np.zeros_like(v);beta=0.;aa=[];bb=[]
   for step in range(96):
    z=H@v-E*v-beta*prev;a=float(np.vdot(v,z).real);z-=a*v;bn=float(np.linalg.norm(z));aa.append(a)
    if bn<1e-11:break
    bb.append(bn);prev,v=v,z/bn;beta=bn
   nodes,U=eigh_tridiagonal(aa,bb[:len(aa)-1]);ww=weight*U[0]**2
   visible=[dict(energy=float(x),weight=float(y)) for x,y in zip(nodes,ww) if y>1e-8*weight]
   mean=float(np.vdot(b,H@b-E*b).real/weight)
   row=dict(L=L,profile_mode=mode,source=name,weight=weight,parity=parity,ground_parity=px,mean=mean,nodes=visible,energy=E,ground_residual=res,cross_abs=abs(cross),q=2*np.pi*mode/L,scope='Finite leading XY effective theory, no native full-H remainder control')
   rows.append(row)
 (P/'neutral_xy_readout.json').write_text(json.dumps(dict(rows=rows),indent=2)+'\n');print(L,dim,'seconds',time.monotonic()-start,[(r['profile_mode'],r['source'],r['weight'],r['mean']) for r in rows if r['L']==L],flush=True)

checks=[]
for row in rows:
 L=row['L'];mode=row['profile_mode']
 if row['source']=='collective_density':
  assert abs(row['weight']-4*mode/L)<1e-9
 if row['source']=='native_composite_O2' and mode==2:
  target=4*np.sin(2*np.pi/L)*np.cos(np.pi/L)
  observed=sum(n['weight'] for n in row['nodes'] if abs(n['energy']-target)<1e-7)
  predicted=18*(1+2/(L*np.sin(np.pi/L)))**2/L*np.cos(2*np.pi/L)**2*np.sin(np.pi/L)**2
  assert abs(observed-predicted)<1e-9
  checks.append(dict(L=L,one_pair_weight=observed,analytic_weight=predicted,error=abs(observed-predicted)))
(P/'neutral_xy_readout.json').write_text(json.dumps(dict(rows=rows,analytic_checks=checks),indent=2)+'\n')

two_pair_checks=[]
for L in [8,12,16,20]:
 predicted=0.
 for r in [1,3]:
  hR=np.pi/2-r*np.pi/L;pR=hR+4*np.pi/L;hL=-np.pi/2+np.pi/L;pL=hL-2*np.pi/L
  F=(np.exp(1j*pR)-np.exp(1j*pL))*(np.exp(1j*hL)-np.exp(1j*hR))
  predicted+=(-3*F.real/L**1.5)**2
 target=4*(np.sin(np.pi/L)+np.sin(2*np.pi/L)*np.cos(np.pi/L))
 row=next(r for r in rows if r['L']==L and r['profile_mode']==1 and r['source']=='native_composite_O2')
 observed=sum(n['weight'] for n in row['nodes'] if abs(n['energy']-target)<1e-7)
 assert abs(observed-predicted)<1e-9
 two_pair_checks.append(dict(L=L,weight=observed,analytic_weight=predicted,error=abs(observed-predicted),scaled_L3=observed*L**3))
(P/'neutral_xy_readout.json').write_text(json.dumps(dict(rows=rows,analytic_checks=checks,two_pair_checks=two_pair_checks),indent=2)+'\n')
