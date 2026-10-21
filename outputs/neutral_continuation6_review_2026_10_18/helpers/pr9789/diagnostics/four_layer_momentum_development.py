import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['VECLIB_MAXIMUM_THREADS']='1'
import sys,json,time
from pathlib import Path
import numpy as np
from numba import njit
from scipy.linalg import eigh_tridiagonal
sys.path.insert(0,str(Path(__file__).resolve().parent))
from neutral_four_layer_periodic import geometry,makeorbits,diagonal
@njit
def apply(v,d,f):
 out=d*v
 for a in f:
  for j in range(len(v)):out[j]-=4*v[j^a]
 return out
@njit
def parity(x):
 x^=x>>16;x^=x>>8;x^=x>>4
 return (0x6996>>(x&15))&1
@njit
def edge_diag(states,edges,coeff):
 out=np.zeros(len(states),np.complex128)
 for j in range(len(states)):
  for k in range(len(edges)):out[j]+=coeff[k]*(1-2*parity(states[j]&edges[k]))
 return out
R=5;start=time.time();rot,ref,edges,flips=geometry(R,True)
ids,reps,sizes=makeorbits((R-1)**2,rot,ref)
a=np.load('/tmp/neutral_four_layer_periodic/R5.npz');g=a['u'][:,0][ids]/np.sqrt(sizes[ids].astype(float));e0=a['ev'][0]
states=np.arange(len(ids),dtype=np.int64);d=diagonal(states,edges)
print("lift", np.linalg.norm(g), e0, np.linalg.norm(apply(g,d,flips)-e0*g), flush=True)
out=[]
for mx,my in [(0,0),(1,0),(2,0),(1,1),(2,1),(2,2)]:
 Q=2*np.pi*np.array([mx,my])/R;ec=[];pc=[]
 for x in range(R):
  for y in range(R):
   ec.extend([-18*np.cos(Q[0]/2)*np.exp(-1j*(Q[0]*(x+.5)+Q[1]*y)),-18*np.cos(Q[1]/2)*np.exp(-1j*(Q[0]*x+Q[1]*(y+.5)))])
   pc.append(-12*np.cos(Q[0]/2)*np.cos(Q[1]/2)*np.exp(-1j*(Q[0]*(x+.5)+Q[1]*(y+.5))))
 q=edge_diag(states,edges,np.array(ec))*g
 for f,c in zip(flips,pc):q+=c*g[states^f]
 mean=np.vdot(g,q);q-=mean*g;norm=np.linalg.norm(q)
 if mx==my==0:
  check=-3*(-d/5-np.dot(g,(-d/5)*g))*g
  assert np.linalg.norm(q-check)<1e-9
 basis=[];alph=[];bet=[];v=q/norm;prev=np.zeros(len(g),complex);b=0
 for k in range(100):
  basis.append(v.copy());w=apply(v,d,flips)-e0*v-b*prev;aa=float(np.vdot(v,w).real);w-=aa*v
  for _ in range(2):
   for u in basis:w-=np.vdot(u,w)*u
  bb=np.linalg.norm(w);alph.append(aa)
  if bb<1e-11:break
  bet.append(bb);prev=v;v=w/bb;b=bb
 ev,u=eigh_tridiagonal(alph,bet[:len(alph)-1]);B=np.array(basis).T;peaks=[]
 for i in range(len(ev)):
  wt=float(norm**2*abs(u[0,i])**2)
  if wt<1e-6:continue
  vec=B@u[:,i];res=float(np.linalg.norm(apply(vec,d,flips)-(e0+ev[i])*vec))
  peaks.append(dict(gap=float(ev[i]),weight=wt,residual=res,accepted=res<1e-7))
 row=dict(momentum=[mx,my],Q=Q.tolist(),source_norm2=float(norm**2),mean_abs=float(abs(mean)),steps=len(alph),peaks=peaks)
 out.append(row);print(json.dumps(row),flush=True)
 Path('/tmp/neutral_four_layer_momentum.json').write_text(json.dumps(dict(R=R,results=out,elapsed=time.time()-start,scope='Fixed finite leading coefficient model; exposed development calculation, not observed data'),indent=2)+'\n')
