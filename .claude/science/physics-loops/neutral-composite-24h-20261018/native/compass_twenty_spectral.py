"""Bounded Krylov response on 5x2x2; no infinite-volume extrapolation."""
from pathlib import Path
import itertools,json,numpy as np
from scipy.linalg import eigh_tridiagonal
from compass_twenty import mf
P=Path(__file__).resolve().parent
shape=(5,2,2);sites=list(itertools.product(*(range(x) for x in shape)));idx={x:i for i,x in enumerate(sites)}
bonds=[]
for x,i in idx.items():
 for a in range(3):
  y=list(x);y[a]=(y[a]+1)%shape[a];bonds.append((i,idx[tuple(y)],a,1.))
H=mf(shape,bonds);saved=np.load(P/'ground_5x2x2.npz');G=saved['vectors'];E=float(saved['energy']);rows=[]
for qx in [0.,2*np.pi/5]:
 terms=[]
 for x in sites:
  for a in range(3):
   l=list(x);r=list(x);l[a]=(l[a]-1)%shape[a];r[a]=(r[a]+1)%shape[a]
   terms.append((idx[tuple(l)],idx[tuple(r)],a,np.exp(1j*qx*x[0])))
 C=mf(shape,terms)
 for gi in range(G.shape[1]):
  v=C@G[:,gi];v-=G@(G.conj().T@v);weight=float(np.vdot(v,v).real)/G.shape[1];v/=np.linalg.norm(v)
  B=np.empty((64,len(v)),dtype=complex);aa=[];bb=[];prev=np.zeros_like(v);beta=0.;controls=[]
  for step in range(64):
   B[step]=v;w=H@v-E*v-beta*prev;alpha=float(np.vdot(v,w).real);w-=alpha*v
   for repeat in range(2):w-=B[:step+1].T@(B[:step+1].conj()@w);w-=G@(G.conj().T@w)
   bn=float(np.linalg.norm(w));aa.append(alpha)
   if len(aa) in [16,32,64] or bn<1e-10:
    ev,U=eigh_tridiagonal(np.array(aa),np.array(bb));ww=U[0]**2
    controls.append(dict(steps=len(aa),mean=float(ww@ev),variance=float(ww@(ev*ev)-(ww@ev)**2),weight_sum=float(ww.sum()),resolvent_imag=[float(np.sum(ww*eta/(ev**2+eta**2))) for eta in [.1,.5,1.]],strong_lines=[dict(delta=float(ev[i]),weight=float(weight*ww[i])) for i in np.argsort(-ww)[:8]]))
    print(qx,gi,controls[-1],flush=True)
   if bn<1e-10 or step==63:break
   bb.append(bn);prev=v;v=w/bn;beta=bn
  rows.append(dict(qx=qx,ground_index=gi,weight=weight,controls=controls,quadrature_lines=[dict(delta=float(en),weight=float(weight*z)) for en,z in zip(ev,ww) if z>1e-12]))
  (P/'compass_twenty_spectral.json').write_text(json.dumps(dict(scope='20spin thin torus; supplied computed ground mixture; finite Krylov quadrature',rows=rows),indent=2)+'\n')
  del B
